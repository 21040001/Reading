/**
 * İçerik denetimi: her metin JSON'u biçime uyuyor mu, sorular metinle tutarlı mı.
 * Yeni metin eklendiğinde otomatik olarak denetlenir.
 */
import * as fs from 'fs';
import * as path from 'path';
import { BOOKS, getText, TEXT_LIST } from '../src/features/reading/content';
import type { Question, ReadingText } from '../src/features/reading/content/types';

const DATA = path.join(__dirname, '../src/features/reading/content/data');

/** Özbekçe metinde oʻ / gʻ için düz kesme işareti kullanılmamalı (ʻ U+02BB) */
const badApostrophe = (s: string) => /[oOgG]['’`](?!clock)/.test(s);
const words = (s: string) => s.trim().split(/\s+/).filter(Boolean);
const norm = (s: string) => s.toLowerCase().replace(/[’']/g, "'");

const uzStrings = (t: ReadingText): string[] => [
  t.title.uz,
  t.intro.uz,
  t.tag.uz,
  ...t.paragraphs.map(p => p.uz ?? ''),
  ...t.glossary.map(g => g.uz),
  ...t.grammar.map(g => g.title.uz),
  ...t.questions.map(q => q.explain?.uz ?? ''),
];

test('every JSON file is listed, ids are unique', () => {
  const files = fs.readdirSync(DATA).flatMap(b => fs.readdirSync(path.join(DATA, b)).map(f => f.replace(/\.json$/, '')));
  expect(new Set(TEXT_LIST.map(t => t.id))).toEqual(new Set(files));
  expect(new Set(TEXT_LIST.map(t => t.id)).size).toBe(TEXT_LIST.length);
});

test('books: units reference existing texts of the same level, each text in exactly one unit', () => {
  const seen = new Map<string, number>();
  for (const b of BOOKS) {
    for (const u of b.units) {
      for (const id of u.texts) {
        const t = getText(id);
        expect(t).toBeDefined();
        expect(t!.level).toBe(b.level);
        seen.set(id, (seen.get(id) ?? 0) + 1);
      }
    }
  }
  for (const t of TEXT_LIST) {
    expect([t.id, seen.get(t.id)]).toEqual([t.id, 1]);
  }
});

describe.each(TEXT_LIST.map(t => [t.id, t] as const))('%s', (_id, t) => {
  const full = norm(t.paragraphs.map(p => p.en).join(' '));

  test('basic structure', () => {
    expect(t.title.uz.length).toBeGreaterThan(0);
    expect(t.en.length).toBeGreaterThan(0);
    expect(t.paragraphs.length).toBeGreaterThan(1);
    expect(t.questions.length).toBeGreaterThanOrEqual(6);
    expect(t.glossary.length).toBeGreaterThanOrEqual(5);
    expect(new Set(t.questions.map(q => q.id)).size).toBe(t.questions.length);
    for (const p of t.paragraphs) {
      expect(p.en).not.toMatch(/\s{2,}|\(|\)/); // TTS qavslarni oʻqiydi; ortiqcha boʻshliq yoʻq
    }
  });

  test('length fits the level', () => {
    const n = words(t.paragraphs.map(p => p.en).join(' ')).length;
    const range: Record<string, [number, number]> = { A1: [50, 130], A2: [110, 260], B1: [230, 460], B2: [230, 650], C1: [550, 950] };
    const [min, max] = range[t.level];
    expect(n).toBeGreaterThanOrEqual(min);
    expect(n).toBeLessThanOrEqual(max);
  });

  test('A1–A2: every paragraph has an Uzbek translation, no "Not Given"', () => {
    if (t.level === 'A1' || t.level === 'A2') {
      for (const p of t.paragraphs) {
        expect(p.uz?.length).toBeGreaterThan(0);
      }
      for (const q of t.questions) {
        if (q.type === 'tfng') {
          expect(q.ng).toBeFalsy();
        }
      }
    }
  });

  test('Uzbek text uses ʻ / ʼ, not ASCII apostrophes', () => {
    for (const s of uzStrings(t)) {
      expect([s, badApostrophe(s)]).toEqual([s, false]);
    }
  });

  test('glossary words appear in the text', () => {
    for (const g of t.glossary) {
      const ok = g.en.split(' / ').some(v => {
        const w = v.toLowerCase().replace(/^(be|to) /, '').split(' ')[0];
        return full.includes(w.slice(0, Math.min(4, w.length)));
      });
      expect([g.en, ok]).toEqual([g.en, true]);
    }
  });

  test('grammar notes: topic id format, example comes from the text', () => {
    for (const g of t.grammar) {
      expect(g.topicId).toMatch(/^[a-z0-9-]+$/);
      for (const piece of g.example.split('…').map(x => x.trim()).filter(Boolean)) {
        expect([g.example, full.includes(norm(piece).replace(/[.!?]$/, ''))]).toEqual([g.example, true]);
      }
    }
  });

  test.each(t.questions.map(q => [q.id, q] as const))('question %s', (_qid, q: Question) => {
    if (q.para != null) {
      expect(q.para).toBeGreaterThanOrEqual(0);
      expect(q.para).toBeLessThan(t.paragraphs.length);
    }
    expect(q.explain?.uz.length).toBeGreaterThan(0);
    switch (q.type) {
      case 'tfng':
        expect(['T', 'F', 'NG']).toContain(q.answer);
        if (q.answer === 'NG') {
          expect(q.ng).toBe(true);
        }
        break;
      case 'choice':
      case 'heading':
        expect(q.options.length).toBeGreaterThanOrEqual(3);
        expect(new Set(q.options).size).toBe(q.options.length);
        expect(q.answer).toBeGreaterThanOrEqual(0);
        expect(q.answer).toBeLessThan(q.options.length);
        break;
      case 'gap': {
        expect(q.prompt.split('___').length).toBe(2);
        expect(q.answers.length).toBeGreaterThan(0);
        // birinchi javob matnda aynan bor va soʻz chegarasiga sigʻadi
        expect([q.answers[0], full.includes(norm(q.answers[0]))]).toEqual([q.answers[0], true]);
        if (q.maxWords) {
          for (const a of q.answers) {
            expect(words(a).length).toBeLessThanOrEqual(q.maxWords);
          }
        }
        break;
      }
    }
  });
});

import { splitTurns } from '../src/features/reading/utils/gloss';

test('dialogue paragraphs split into speaker turns', () => {
  expect(splitTurns("Malika: Good morning! Seller: They are 15,000 sum a kilo.")).toEqual([
    { speaker: 'Malika', line: 'Good morning!' },
    { speaker: 'Seller', line: 'They are 15,000 sum a kilo.' },
  ]);
  expect(splitTurns('Malika: Xayrli tong! Sotuvchi: Mana.').map(t => t.speaker)).toEqual(['Malika', 'Sotuvchi']);
  expect(splitTurns('Ms Rahimova: Hello. Laylo: Hi!').map(t => t.speaker)).toEqual(['Ms Rahimova', 'Laylo']);
  expect(splitTurns('No speakers here: just text.')).toEqual([{ speaker: null, line: 'No speakers here: just text.' }]);
  // suhbat matnlarida koʻpchilik xatboshilar gapiruvchi bilan boshlanadi (bitta hikoya qismi boʻlishi mumkin)
  for (const t of TEXT_LIST.filter(x => x.kind === 'dialogue')) {
    const withSpeaker = t.paragraphs.filter(p => splitTurns(p.en)[0].speaker !== null).length;
    expect([t.id, withSpeaker >= t.paragraphs.length - 1]).toEqual([t.id, true]);
  }
});
