import type { AppLanguage } from './strings';

/** İçerikteki çok dilli metin: İngilizce arayüzde `en` varsa o, yoksa Özbekçe */
export const pick = (x: { uz: string; en?: string } | undefined, language: AppLanguage) =>
  x ? (language === 'en' && x.en) || x.uz : '';
