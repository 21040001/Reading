/**
 * İngilizce cümleleri telefonun ses motoruyla (TTS) okur. İnternet gerekmez.
 */
import { Platform } from 'react-native';
import Speech from '@mhpdev/react-native-speech';

// iOS ve Android hız ölçekleri farklı; ikisinde de biraz yavaş, öğrenmeye uygun
const RATE = Platform.OS === 'ios' ? 0.45 : 0.9;
let hasEnglish: boolean | null = null;

async function englishAvailable(): Promise<boolean> {
  if (hasEnglish === null) {
    try {
      hasEnglish = (await Speech.getAvailableVoices('en')).length > 0;
    } catch {
      hasEnglish = true; // listeyi veremeyen cihazlarda yine de deneyelim
    }
  }
  return hasEnglish;
}

/** false: cihazda İngilizce ses yok */
export async function speakEnglish(text: string, slow = false): Promise<boolean> {
  await Speech.stop().catch(() => undefined);
  if (!(await englishAvailable())) {
    return false;
  }
  await Speech.speak(text, { language: 'en-US', rate: slow ? RATE * 0.7 : RATE, silentMode: 'ignore' });
  return true;
}

export const stopSpeaking = () => Speech.stop().catch(() => undefined);

/** Android: ses paketi indirme ekranı */
export const openVoiceInstaller = () => Speech.openVoiceDataInstaller().catch(() => undefined);
