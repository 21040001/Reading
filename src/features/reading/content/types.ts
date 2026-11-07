/**
 * Okuma içeriğinin biçimi. İçerik JSON dosyalarında durur (content/data/<kitap>/<metin>.json),
 * Python betikleriyle üretilir (scripts/content). Kod değiştirmeden metin eklenebilir.
 *
 * Kurallar:
 *  - Metinler ÖZGÜN (kitaplardan kopya yok). İngilizce paragraflar; A1–A2'de her
 *    paragrafın Özbekçe çevirisi (uz) de verilir.
 *  - Açıklamalar Özbekçe zorunlu, İngilizce isteğe bağlı (L10n).
 *  - id'ler SONRADAN DEĞİŞTİRİLMEZ (ilerleme bunlara bağlı).
 *  - Biçim `__tests__/content.test.ts` ile denetlenir.
 */
import type { CefrLevel } from '../../../core/profile/profile';

export type L10n = { uz: string; en?: string };

export type Paragraph = {
  en: string;
  /** Özbekçe çeviri (A1–A2'de zorunlu, sonra isteğe bağlı) */
  uz?: string;
};

/** Metindeki önemli kelime / ifade */
export type GlossEntry = { en: string; uz: string };

/** Metinde geçen gramer: Grammar uygulamasındaki ders */
export type GrammarNote = { topicId: string; title: L10n; example: string };

type Base = {
  id: string;
  /** Cevaptan sonra: neden doğru, metnin hangi cümlesinde */
  explain?: L10n;
  /** Cevabın geçtiği paragraf (0'dan) — "Matnda koʻrsatish" için */
  para?: number;
};

/** True / False / Not Given (B1+ sınav tarzı; A1–A2'de yalnız True/False) */
export type TfngQuestion = Base & {
  type: 'tfng';
  statement: string;
  answer: 'T' | 'F' | 'NG';
  /** Not Given seçeneği gösterilsin mi (A1–A2: hayır) */
  ng?: boolean;
};

/** Çoktan seçmeli soru */
export type ChoiceQuestion = Base & {
  type: 'choice';
  /** Soru metni (İngilizce) */
  prompt: string;
  options: string[];
  answer: number;
};

/** Özet / cümle tamamlama: metinden kelime yazılır. prompt'ta tek ___ */
export type GapQuestion = Base & {
  type: 'gap';
  prompt: string;
  answers: string[];
  /** "NO MORE THAN TWO WORDS" gibi sınırlama (sınav tarzı) */
  maxWords?: number;
};

/** Paragraf başlığı eşleştirme: para numaralı paragrafa uygun başlık */
export type HeadingQuestion = Base & {
  type: 'heading';
  para: number;
  options: string[];
  answer: number;
};

export type Question = TfngQuestion | ChoiceQuestion | GapQuestion | HeadingQuestion;
export type QuestionType = Question['type'];

/** Metin türü: kartta küçük etiket */
export type TextKind = 'story' | 'article' | 'email' | 'dialogue' | 'blog' | 'notice' | 'biography' | 'exam';

export type ReadingText = {
  id: string;
  title: L10n;
  /** İngilizce başlık (metnin kendi başlığı) */
  en: string;
  level: CefrLevel;
  kind: TextKind;
  /** Konu etiketi: "Oila", "Shahar", "Fan"… */
  tag: L10n;
  /** Okumadan önce: kısa giriş / hazırlık sorusu (Özbekçe) */
  intro: L10n;
  paragraphs: Paragraph[];
  glossary: GlossEntry[];
  grammar: GrammarNote[];
  questions: Question[];
};

export type Unit = {
  id: string;
  title: L10n;
  /** Hazır metinlerin id'leri (sırayla) */
  texts: string[];
  /** Henüz yazılmamış metinlerin adları — "tez orada" */
  planned?: L10n[];
};

export type Book = {
  id: string;
  title: L10n;
  subtitle: L10n;
  level: CefrLevel;
  /** 'general' = umumiy ingliz tili, 'exam' = IELTS / Multilevel tarzı */
  focus: 'general' | 'exam';
  color?: 'primary' | 'danger' | 'warning' | 'success';
  units: Unit[];
};
