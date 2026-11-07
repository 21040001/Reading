/**
 * Okuma ilerlemesi — ortak çekirdek (core) üzerinde:
 *  - Her metin bir tekrar kartı:  srs_cards  item_type='reading', item_id='<metin>'
 *    (sorular bitince puana göre planlanır → "qayta oʻqish vaqti keldi")
 *  - En iyi puan:                 kv 'reading.best.<metin>'
 *  - Her cevap günlük aktiviteye (ortak seri / hedef) yazılır.
 */
import { query } from '../../../core/db/userDb';
import { getKv, setKv } from '../../../core/profile/profile';
import { recordActivity } from '../../../core/progress/activity';
import { reviewItem, rowToCard, SrsCard } from '../../../core/srs/cards';
import { Grade, isDueState } from '../../../core/srs/sm2';
import { allTexts, BOOKS, bookTexts, wordCount } from '../content';
import type { ReadingText } from '../content/types';

export const PASS_SCORE = 70;
const BEST_PREFIX = 'reading.best.';

export type TextStatus = 'new' | 'started' | 'passed' | 'mastered';

export type TextProgress = {
  textId: string;
  best: number | null;
  status: TextStatus;
  due: boolean;
  card: SrsCard | null;
};

export const scorePercent = (correct: number, total: number) => (total ? Math.round((correct / total) * 100) : 0);

export function gradeForScore(score: number): Grade {
  if (score >= 90) {
    return 'easy';
  }
  if (score >= PASS_SCORE) {
    return 'good';
  }
  if (score >= 50) {
    return 'hard';
  }
  return 'again';
}

async function readingCards(): Promise<SrsCard[]> {
  const rows = await query("SELECT * FROM srs_cards WHERE item_type = 'reading' AND deleted = 0");
  return rows.map(r => rowToCard(r));
}

async function bestScores(): Promise<Record<string, number>> {
  const rows = await query(`SELECT key, value FROM kv WHERE key LIKE '${BEST_PREFIX}%'`);
  const out: Record<string, number> = {};
  for (const r of rows) {
    out[String(r.key).slice(BEST_PREFIX.length)] = Number(r.value);
  }
  return out;
}

export async function getAllProgress(now = Date.now()): Promise<Record<string, TextProgress>> {
  const [cards, best] = await Promise.all([readingCards(), bestScores()]);
  const byId = new Map(cards.map(c => [c.itemId, c]));
  const out: Record<string, TextProgress> = {};
  for (const t of allTexts()) {
    const card = byId.get(t.id) ?? null;
    const b = best[t.id] ?? null;
    let status: TextStatus = 'new';
    if (card?.status === 'mastered') {
      status = 'mastered';
    } else if (b != null && b >= PASS_SCORE) {
      status = 'passed';
    } else if (b != null) {
      status = 'started';
    }
    out[t.id] = { textId: t.id, best: b, status, due: !!card && isDueState(card, now), card };
  }
  return out;
}

/** Bir cevap: günlük aktiviteye (seri / hedef) */
export const recordAnswer = (correct: boolean) => recordActivity(correct);

export type FinishResult = { score: number; best: number; isNewBest: boolean; passed: boolean };

/** Sorular bitti: en iyi puanı ve tekrar kartını güncelle */
export async function finishText(textId: string, correct: number, total: number): Promise<FinishResult> {
  const score = scorePercent(correct, total);
  const prevRaw = await getKv(BEST_PREFIX + textId);
  const prev = prevRaw == null ? null : Number(prevRaw);
  const best = prev == null ? score : Math.max(prev, score);
  if (prev == null || score > prev) {
    await setKv(BEST_PREFIX + textId, String(best));
  }
  await reviewItem('reading', textId, gradeForScore(score));
  return { score, best, isNewBest: prev == null || score > prev, passed: score >= PASS_SCORE };
}

/** Sıradaki metin: ilk geçilmemiş metin (seviye sırasıyla); tercihen verilen seviyeden */
export function nextText(progress: Record<string, TextProgress>, preferBookId?: string): ReadingText | null {
  const order = preferBookId ? [...BOOKS].sort((a, b) => (a.id === preferBookId ? -1 : b.id === preferBookId ? 1 : 0)) : BOOKS;
  for (const book of order) {
    const t = bookTexts(book).find(x => {
      const s = progress[x.id]?.status;
      return s !== 'passed' && s !== 'mastered';
    });
    if (t) {
      return t;
    }
  }
  return null;
}

/** Qayta oʻqish vaqti kelgan metinlar */
export const dueTexts = (progress: Record<string, TextProgress>) =>
  allTexts().filter(t => progress[t.id]?.due);

export type ReadingStats = { textsDone: number; wordsRead: number; avgScore: number | null };

export function readingStats(progress: Record<string, TextProgress>): ReadingStats {
  const done = allTexts().filter(t => progress[t.id]?.best != null);
  const scores = done.map(t => progress[t.id]!.best!);
  return {
    textsDone: done.length,
    wordsRead: done.reduce((n, t) => n + wordCount(t), 0),
    avgScore: scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : null,
  };
}
