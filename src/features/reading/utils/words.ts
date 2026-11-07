/**
 * Örnek cümleleri dokunulabilir kelimelere bölmek ve bir kelimenin sözlükte
 * aranacak biçimini bulmak için saf yardımcılar (test edilebilir).
 */

export type Token = { text: string; word: string | null };

/** Harf + iç kesme işareti/tire: don't, Ali's, well-known */
const WORD_RE = /[A-Za-z]+(?:['’-][A-Za-z]+)*/g;

/** Cümleyi parçalara böler; birleştirince orijinal metin aynen geri gelir. */
export function tokenize(sentence: string): Token[] {
  const out: Token[] = [];
  let last = 0;
  for (const m of sentence.matchAll(WORD_RE)) {
    const i = m.index ?? 0;
    if (i > last) {
      out.push({ text: sentence.slice(last, i), word: null });
    }
    out.push({ text: m[0], word: lookupForm(m[0]) });
    last = i + m[0].length;
  }
  if (last < sentence.length) {
    out.push({ text: sentence.slice(last), word: null });
  }
  return out;
}

const NEG_IRREGULAR: Record<string, string> = { "can't": 'can', "won't": 'will', "shan't": 'shall', "ain't": 'be' };
const PRONOUN_I = new Set(['i']);

/**
 * Sözlükte aranacak biçim (küçük harf): Ali's → ali, doesn't → does,
 * can't → can, I'm → i, they're → they. Tek harf (a, I) da kelimedir.
 * Aranmaya değmeyecek parçalar için null.
 */
export function lookupForm(raw: string): string | null {
  let w = raw.replace(/’/g, "'").toLowerCase();
  if (NEG_IRREGULAR[w]) {
    return NEG_IRREGULAR[w];
  }
  if (w.endsWith("n't")) {
    w = w.slice(0, -3);
  } else {
    const k = w.indexOf("'");
    if (k > 0) {
      w = w.slice(0, k); // 's, 're, 've, 'll, 'd, 'm
    }
  }
  if (!/^[a-z]+(?:-[a-z]+)*$/.test(w)) {
    return null;
  }
  if (w.length < 2 && w !== 'a' && !PRONOUN_I.has(w)) {
    return null;
  }
  return w;
}
