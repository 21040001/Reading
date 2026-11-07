/**
 * Cevap karşılaştırma. Yazılan cevapta küçük farklar hata sayılmaz:
 *  - büyük/küçük harf, fazla boşluk, sondaki nokta / soru işareti
 *  - eğik kesme işareti (’) ve düz kesme işareti (')
 *  - kısaltmalar: isn't = is not, I'm = I am, don't = do not, can't = cannot …
 */

const CONTRACTIONS: [RegExp, string][] = [
  [/\bwon't\b/g, 'will not'],
  [/\bcan't\b/g, 'can not'],
  [/\bcannot\b/g, 'can not'],
  [/\bshan't\b/g, 'shall not'],
  [/\bain't\b/g, 'am not'],
  [/n't\b/g, ' not'],
  [/'m\b/g, ' am'],
  [/'re\b/g, ' are'],
  [/'ve\b/g, ' have'],
  [/'ll\b/g, ' will'],
  [/'d\b/g, ' would'],
  // 's sadece zamirlerden sonra "is" sayılır (Tom's book gibi iyelikler bozulmasın)
  [/\b(he|she|it|that|what|there|who|where|how|here)'s\b/g, '$1 is'],
];

export function normalizeAnswer(s: string): string {
  let x = s
    .toLowerCase()
    .replace(/[‘’ʼʻ`´]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/\s+/g, ' ')
    .trim()
    .replace(/[.!?,;:]+$/g, '')
    .trim();
  for (const [re, to] of CONTRACTIONS) {
    x = x.replace(re, to);
  }
  return x.replace(/\s*,\s*/g, ', ').replace(/\s+/g, ' ').trim();
}

export const isAnswerCorrect = (given: string, accepted: string[]) => {
  const g = normalizeAnswer(given);
  return g.length > 0 && accepted.some(a => normalizeAnswer(a) === g);
};

/** Cümlenin sonundaki noktalama (kelime kutucuklarında gösterilmez) */
export function splitEnding(sentence: string): { body: string; ending: string } {
  const m = sentence.trim().match(/^(.*?)([.!?]*)$/s);
  return { body: (m?.[1] ?? sentence).trim(), ending: m?.[2] ?? '' };
}

/** Sıralama alıştırmasının kutucukları: cevabın kelimeleri (+ çeldiriciler) */
export const orderTiles = (answer: string, extra: string[] = []) => [
  ...splitEnding(answer).body.split(/\s+/),
  ...extra,
];

/** Hata bulma: cümlenin kelimeleri ve yanlış kelime grubunun konumu */
export function errorTokens(sentence: string, wrong: string): { tokens: string[]; start: number; length: number } {
  const tokens = sentence.trim().split(/\s+/);
  const w = wrong.trim().split(/\s+/);
  const clean = (t: string) => t.replace(/[.!?,;:]+$/g, '').toLowerCase();
  for (let i = 0; i + w.length <= tokens.length; i++) {
    if (w.every((x, j) => clean(tokens[i + j]) === clean(x))) {
      return { tokens, start: i, length: w.length };
    }
  }
  return { tokens, start: -1, length: 0 };
}

/** Boşluklu cümleyi cevapla doldurur: "Look! It ___ (rain)." + "is raining" → "Look! It is raining." */
export function fillBlank(prompt: string, answer: string): string {
  // '—' şıkkı = "boş bırak" (artikl yoʻq): cümleye hiçbir şey eklenmez
  const a = answer.trim() === '—' ? '' : answer;
  // "'ve lost" gibi kısaltmalar önceki kelimeye bitişir: "I ___" → "I've lost"
  const p = /^['’]/.test(a) ? prompt.replace(/\s+___/, '___') : prompt;
  return p
    .replace(/___\s*\([^)]*\)/, a)
    .replace('___', a)
    .replace(/\s*\([^)]*\)\s*([.!?]?)$/, '$1')
    .replace(/\s+/g, ' ')
    .replace(/\s+([.!?,;:])/g, '$1')
    .trim();
}

export function shuffle<T>(a: readonly T[], rnd: () => number = Math.random): T[] {
  const r = [...a];
  for (let i = r.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [r[i], r[j]] = [r[j], r[i]];
  }
  return r;
}
