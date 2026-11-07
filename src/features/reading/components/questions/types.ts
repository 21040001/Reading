import type { Question } from '../../content/types';

export type QuestionProps<Q extends Question> = {
  question: Q;
  /** Metin (heading savoli xatboshidan parcha koʻrsatadi) */
  paragraphs: string[];
  /** Cevap verildi mi (verildiyse bileşen sonucu gösterir, yeni cevap almaz) */
  answered: boolean;
  onAnswer: (correct: boolean) => void;
};

/** Xatboshi harfi: A, B, C… */
export const paraLetter = (i: number) => String.fromCharCode(65 + i);
