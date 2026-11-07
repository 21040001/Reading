import type { GlossEntry } from '../content/types';

/**
 * Metin lugʻatidan kelime → maʼno haritası (TappableText için).
 * "be good at", "to leave" gibi kalıpların ilk feʼli; "accuracy / precision" ikisi de;
 * basit çekimler (tourists, cooked, cooking) de aynı anlamı gösterir.
 */
export function buildGloss(entries: GlossEntry[]): Record<string, string> {
  const out: Record<string, string> = {};
  const add = (k: string, v: string) => {
    if (k && !out[k]) {
      out[k] = v;
    }
  };
  for (const e of entries) {
    for (const variant of e.en.split(' / ')) {
      const w = variant.trim().toLowerCase().replace(/^(be|to) /, '');
      if (!/^[a-z][a-z-]*$/.test(w)) {
        continue; // çok kelimeli ifade: sadece lugʻat listesinde görünür
      }
      add(w, e.uz);
    }
  }
  for (const [k, v] of Object.entries({ ...out })) {
    const stem = k.endsWith('e') ? k.slice(0, -1) : k;
    for (const f of [`${k}s`, `${k}es`, `${k}d`, `${k}ed`, `${stem}ing`, k.endsWith('y') ? `${k.slice(0, -1)}ies` : '']) {
      add(f, v);
    }
  }
  return out;
}

export type Turn = { speaker: string | null; line: string };

/** Suhbat xatboshisi: "Malika: … Seller: …" → navbatlar (gapiruvchi + gap) */
export function splitTurns(paragraph: string): Turn[] {
  // Gapiruvchi: "Malika:", "Ms Rahimova:", "Dr. Karimov:"
  const re = /(?:^|\s)((?:(?:Mr|Ms|Mrs|Dr)\.? )?[A-ZÀ-ɏ][\wÀ-ɏʻʼ'-]{1,20}):\s/g;
  const marks: { at: number; end: number; speaker: string }[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(paragraph))) {
    const at = m.index + (m[0].startsWith(' ') ? 1 : 0);
    marks.push({ at, end: m.index + m[0].length, speaker: m[1] });
  }
  if (!marks.length) {
    return [{ speaker: null, line: paragraph }];
  }
  const out: Turn[] = [];
  if (marks[0].at > 0) {
    out.push({ speaker: null, line: paragraph.slice(0, marks[0].at).trim() });
  }
  marks.forEach((mk, i) => {
    out.push({ speaker: mk.speaker, line: paragraph.slice(mk.end, i + 1 < marks.length ? marks[i + 1].at : undefined).trim() });
  });
  return out;
}
