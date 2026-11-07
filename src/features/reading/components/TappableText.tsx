import React, { useMemo, useState } from 'react';
import { Alert, Modal, Pressable, StyleProp, Text, TextStyle, View } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { useSettings } from '../../../app/settings/SettingsContext';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import { speakEnglish } from '../../../services/speech/speech';
import { tokenize } from '../utils/words';
import { openInVocabulary, openVocabularyStore } from '../utils/vocabLink';

type Props = {
  text: string;
  style?: StyleProp<TextStyle>;
  /** Metnin lugʻati: kelime (küçük harf) → Özbekçe anlamı. Varsa kelime noktalı altı çizili gösterilir. */
  gloss?: Record<string, string>;
};

/**
 * İngilizce metin; her kelimesine dokunulabilir. Dokunulan kelime için alt pencere:
 * lugʻatdagi maʼnosi (varsa), dinle, Vocabulary'de aç.
 */
export default function TappableText({ text, style, gloss }: Props) {
  const s = useStyles();
  const tokens = useMemo(() => tokenize(text), [text]);
  const [picked, setPicked] = useState<{ index: number; word: string } | null>(null);

  return (
    <>
      <Text style={style}>
        {tokens.map((tk, i) =>
          tk.word ? (
            <Text
              key={i}
              onPress={() => setPicked({ index: i, word: tk.word! })}
              style={picked?.index === i ? s.picked : gloss?.[tk.word] ? s.glossed : undefined}
              accessibilityRole="button"
              testID={`word-${tk.word}`}>
              {tk.text}
            </Text>
          ) : (
            tk.text
          ),
        )}
      </Text>
      <WordSheet
        word={picked?.word ?? null}
        meaning={picked ? gloss?.[picked.word] : undefined}
        onClose={() => setPicked(null)}
      />
    </>
  );
}

function WordSheet({ word, meaning, onClose }: { word: string | null; meaning?: string; onClose: () => void }) {
  const s = useStyles();
  const { t, colors } = useSettings();

  const openVocab = async () => {
    if (!word) {
      return;
    }
    if (await openInVocabulary(word)) {
      onClose();
      return;
    }
    Alert.alert(t('word.noVocabTitle'), t('word.noVocabMsg'), [
      { text: t('common.cancel'), style: 'cancel' },
      {
        text: t('word.install'),
        onPress: () => {
          openVocabularyStore().catch(() => undefined);
        },
      },
    ]);
  };

  return (
    <Modal visible={!!word} transparent animationType="fade" onRequestClose={onClose}>
      <Pressable style={s.backdrop} onPress={onClose} testID="word-sheet-backdrop">
        <Pressable style={s.sheet} onPress={() => undefined}>
          <View style={s.head}>
            <Text style={s.word}>{word}</Text>
            <Pressable
              onPress={() => word && speakEnglish(word).catch(() => undefined)}
              hitSlop={8}
              style={s.speak}
              accessibilityRole="button"
              accessibilityLabel={t('speak.listen')}>
              <Icon name="volume-medium-outline" size={22} color={colors.primary} />
            </Pressable>
          </View>
          {!!meaning && <Text style={s.meaning}>{meaning}</Text>}
          <Text style={s.hint}>{t('word.sheetHint')}</Text>
          <Pressable style={s.primary} onPress={openVocab} accessibilityRole="button">
            <Icon name="book-outline" size={18} color={colors.white} />
            <Text style={s.primaryText}>{t('word.openVocab')}</Text>
          </Pressable>
          <Pressable style={s.secondary} onPress={onClose} accessibilityRole="button">
            <Text style={s.secondaryText}>{t('common.close')}</Text>
          </Pressable>
        </Pressable>
      </Pressable>
    </Modal>
  );
}

const useStyles = makeStyles(c => ({
  picked: { color: c.primary, textDecorationLine: 'underline' },
  glossed: { textDecorationLine: 'underline', textDecorationStyle: 'dotted', textDecorationColor: c.primary },
  meaning: { marginTop: 4, fontSize: 18, fontWeight: '700', color: c.primary },
  backdrop: { flex: 1, justifyContent: 'flex-end', backgroundColor: 'rgba(0,0,0,0.35)' },
  sheet: {
    padding: spacing.lg,
    paddingBottom: spacing.lg + 8,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    backgroundColor: c.surface,
  },
  head: { flexDirection: 'row', alignItems: 'center', gap: spacing.sm },
  word: { flex: 1, fontSize: 26, fontWeight: '800', color: c.text },
  speak: {
    width: 40,
    height: 40,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: c.border,
  },
  hint: { marginTop: 6, color: c.textSecondary, lineHeight: 20 },
  primary: {
    flexDirection: 'row',
    gap: 8,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: spacing.md,
    padding: 14,
    borderRadius: 14,
    backgroundColor: c.primary,
  },
  primaryText: { color: c.white, fontWeight: '800', fontSize: 16 },
  secondary: { marginTop: spacing.sm, padding: 12, alignItems: 'center' },
  secondaryText: { color: c.primary, fontWeight: '700', fontSize: 16 },
}));
