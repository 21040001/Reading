/**
 * Soru hatası bildirme: Telegram (öncelikli) ya da e-posta ile hazır metin açılır.
 * Kullanıcı yalnızca kendi açıklamasını ekleyip gönderir.
 */
import { Linking } from 'react-native';
import { APP, SUITE } from '../../../core/config';
import type { Question, ReadingText } from '../content/types';

export function reportText(text: ReadingText, q: Question, answer: string): string {
  const shown = q.type === 'tfng' ? q.statement : q.type === 'heading' ? `Heading, paragraph ${q.para + 1}` : q.prompt;
  return [`[${APP.name} ${APP.version}] Savolda xato`, `ID: ${text.id}/${q.id}`, `Savol: ${shown}`, `Javob: ${answer}`, 'Izoh: '].join(
    '\n',
  );
}

export async function reportByTelegram(text: string): Promise<boolean> {
  const url = `https://t.me/${SUITE.telegram}?text=${encodeURIComponent(text)}`;
  try {
    await Linking.openURL(url);
    return true;
  } catch {
    return false;
  }
}

export async function reportByEmail(text: string): Promise<boolean> {
  const url = `mailto:${SUITE.contactEmail}?subject=${encodeURIComponent(`${APP.name}: savolda xato`)}&body=${encodeURIComponent(text)}`;
  try {
    await Linking.openURL(url);
    return true;
  } catch {
    return false;
  }
}
