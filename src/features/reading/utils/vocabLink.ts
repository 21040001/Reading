/**
 * Seri uygulamaları arası bağlantılar:
 *  - kelime  → Vocabulary  linguauz-vocab://word/<kelime>
 *  - gramer  → Grammar     linguauz-grammar://topic/<konu-id>
 * Uygulama kurulu değilse openURL hata verir → false; çağıran Play Market'i önerir.
 */
import { Linking } from 'react-native';
import { SUITE_LINKS } from '../../../core/config';

type SuiteApp = keyof typeof SUITE_LINKS;

export const suiteUrl = (app: SuiteApp, path: string) => `${SUITE_LINKS[app].scheme}://${path}`;
export const vocabWordUrl = (word: string) => suiteUrl('vocabulary', `word/${encodeURIComponent(word)}`);
export const grammarTopicUrl = (topicId: string) => suiteUrl('grammar', `topic/${encodeURIComponent(topicId)}`);

async function tryOpen(url: string): Promise<boolean> {
  try {
    await Linking.openURL(url);
    return true;
  } catch {
    return false;
  }
}

export const openInVocabulary = (word: string) => tryOpen(vocabWordUrl(word));
export const openInGrammar = (topicId: string) => tryOpen(grammarTopicUrl(topicId));

/** Uygulamanın mağaza sayfası (önce Play Market uygulaması, olmazsa web) */
export async function openStore(app: SuiteApp): Promise<void> {
  const id = SUITE_LINKS[app].androidPackage;
  for (const url of [`market://details?id=${id}`, `https://play.google.com/store/apps/details?id=${id}`]) {
    if (await tryOpen(url)) {
      return;
    }
  }
}

export const openVocabularyStore = () => openStore('vocabulary');
