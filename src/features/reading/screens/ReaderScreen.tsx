import React, { useEffect, useMemo, useState } from 'react';
import { Alert, Pressable, ScrollView, Switch, Text, View } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { RouteProp, useNavigation, useRoute } from '@react-navigation/native';
import { RootStackParamList, StackNav } from '../../../app/navigation/AppNavigator';
import { useSettings } from '../../../app/settings/SettingsContext';
import { pick } from '../../../i18n/l10n';
import { stopSpeaking } from '../../../services/speech/speech';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import SpeakButton from '../components/SpeakButton';
import TappableText from '../components/TappableText';
import { paraLetter } from '../components/questions/types';
import { getText, readingMinutes, wordCount } from '../content';
import type { TextKind } from '../content/types';
import useProgress from '../hooks/useProgress';
import { buildGloss, splitTurns } from '../utils/gloss';
import { openInGrammar, openStore } from '../utils/vocabLink';

export const KIND_KEYS: Record<TextKind, `kind.${TextKind}`> = {
  story: 'kind.story',
  article: 'kind.article',
  email: 'kind.email',
  dialogue: 'kind.dialogue',
  blog: 'kind.blog',
  notice: 'kind.notice',
  biography: 'kind.biography',
  exam: 'kind.exam',
};

/** Matn: oʻqishdan oldin → matn (soʻzga bosish, tinglash, tarjima) → lugʻat → grammatika → savollar */
export default function ReaderScreen() {
  const s = useStyles();
  const { t, language, colors } = useSettings();
  const nav = useNavigation<StackNav>();
  const { params } = useRoute<RouteProp<RootStackParamList, 'Reader'>>();
  const text = getText(params.textId);
  const { progress } = useProgress();
  const hasTranslation = !!text?.paragraphs.some(p => p.uz);
  const [showUz, setShowUz] = useState(false);
  const gloss = useMemo(() => buildGloss(text?.glossary ?? []), [text]);

  useEffect(() => () => {
    stopSpeaking();
  }, []);

  if (!text) {
    return null;
  }
  const best = progress?.[text.id]?.best;
  const lettered = text.kind === 'exam';

  const openGrammar = async (topicId: string) => {
    if (!(await openInGrammar(topicId))) {
      Alert.alert(t('grammar.noAppTitle'), t('grammar.noAppMsg'), [
        { text: t('common.cancel'), style: 'cancel' },
        { text: t('word.install'), onPress: () => openStore('grammar').catch(() => undefined) },
      ]);
    }
  };

  return (
    <View style={s.c}>
      <ScrollView contentContainerStyle={s.p}>
        <Text style={s.en}>{text.en}</Text>
        <Text style={s.uzTitle}>{pick(text.title, language)}</Text>
        <View style={s.meta}>
          <Text style={s.chip}>{text.level}</Text>
          <Text style={s.chip}>{t(KIND_KEYS[text.kind])}</Text>
          <Text style={s.chip}>{pick(text.tag, language)}</Text>
          <Text style={s.metaText}>
            {t('text.minutes', { n: readingMinutes(text) })} · {t('text.words', { n: wordCount(text) })}
          </Text>
        </View>

        <View style={s.intro}>
          <Icon name="compass-outline" size={18} color={colors.primary} />
          <Text style={s.introText}>{pick(text.intro, language)}</Text>
        </View>

        <View style={s.tools}>
          <Icon name="hand-left-outline" size={16} color={colors.textSecondary} />
          <Text style={s.toolsText}>{t('reader.tapHint')}</Text>
        </View>
        {hasTranslation && (
          <View style={s.switchRow}>
            <Text style={s.switchText}>{t('reader.translation')}</Text>
            <Switch
              value={showUz}
              onValueChange={setShowUz}
              trackColor={{ true: colors.primary, false: colors.border }}
              thumbColor={colors.white}
              testID="translation-switch"
            />
          </View>
        )}

        <View style={s.textBox}>
          {text.paragraphs.map((p, i) => (
            <View key={i} style={[s.para, i > 0 && s.paraGap]}>
              <View style={s.paraHead}>
                {lettered && <Text style={s.letter}>{paraLetter(i)}</Text>}
                <View style={{ flex: 1 }} />
                <SpeakButton text={p.en} size={30} />
              </View>
              {text.kind === 'dialogue' ? (
                splitTurns(p.en).map((turn, k) => (
                  <View key={k} style={k > 0 && s.turnGap}>
                    {turn.speaker && <Text style={s.speaker}>{turn.speaker}</Text>}
                    <TappableText text={turn.line} style={s.paraText} gloss={gloss} />
                  </View>
                ))
              ) : (
                <TappableText text={p.en} style={s.paraText} gloss={gloss} />
              )}
              {showUz && p.uz && (
                <Text style={s.paraUz}>
                  {text.kind === 'dialogue'
                    ? splitTurns(p.uz)
                        .map(turn => (turn.speaker ? `${turn.speaker}: ${turn.line}` : turn.line))
                        .join('\n')
                    : p.uz}
                </Text>
              )}
            </View>
          ))}
        </View>

        {text.glossary.length > 0 && (
          <>
            <Text style={s.section}>{t('reader.glossary')}</Text>
            <View style={s.card}>
              {text.glossary.map((g, i) => (
                <View key={g.en} style={[s.gRow, i > 0 && s.divider]}>
                  <Text style={s.gEn}>{g.en}</Text>
                  <Text style={s.gUz}>{g.uz}</Text>
                </View>
              ))}
            </View>
          </>
        )}

        {text.grammar.length > 0 && (
          <>
            <Text style={s.section}>{t('reader.grammar')}</Text>
            {text.grammar.map(g => (
              <View key={g.topicId} style={s.gram}>
                <Text style={s.gramTitle}>{pick(g.title, language)}</Text>
                <Text style={s.gramEx}>«{g.example}»</Text>
                <Pressable style={s.gramBtn} onPress={() => openGrammar(g.topicId)} accessibilityRole="button">
                  <Icon name="school-outline" size={16} color={colors.primary} />
                  <Text style={s.gramBtnText}>{t('reader.openGrammar')}</Text>
                </Pressable>
              </View>
            ))}
          </>
        )}
      </ScrollView>

      <View style={s.footer}>
        {best != null && <Text style={s.best}>{t('reader.best', { n: best })}</Text>}
        <Pressable style={s.start} onPress={() => nav.navigate('Quiz', { textId: text.id })} accessibilityRole="button">
          <Icon name="help-circle-outline" size={20} color={colors.white} />
          <Text style={s.startText}>{t('reader.questions', { n: text.questions.length })}</Text>
        </Pressable>
      </View>
    </View>
  );
}

const useStyles = makeStyles(c => ({
  c: { flex: 1, backgroundColor: c.background },
  p: { padding: spacing.lg, paddingBottom: 130 },
  en: { fontSize: 22, fontWeight: '800', color: c.text },
  uzTitle: { marginTop: 2, color: c.textSecondary, fontSize: 15 },
  meta: { flexDirection: 'row', flexWrap: 'wrap', alignItems: 'center', gap: 6, marginTop: spacing.sm },
  chip: {
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 8,
    overflow: 'hidden',
    fontSize: 12,
    fontWeight: '700',
    color: c.primary,
    borderWidth: 1,
    borderColor: c.border,
  },
  metaText: { fontSize: 12, color: c.textSecondary },
  intro: {
    flexDirection: 'row',
    gap: 8,
    marginTop: spacing.md,
    padding: spacing.md,
    borderRadius: 14,
    backgroundColor: c.surface,
    borderWidth: 1,
    borderColor: c.border,
  },
  introText: { flex: 1, color: c.text, lineHeight: 21 },
  tools: { flexDirection: 'row', alignItems: 'center', gap: 6, marginTop: spacing.md },
  toolsText: { flex: 1, fontSize: 13, color: c.textSecondary },
  switchRow: { flexDirection: 'row', alignItems: 'center', marginTop: 4 },
  switchText: { flex: 1, fontWeight: '700', color: c.text },
  textBox: { marginTop: spacing.sm, padding: spacing.md, borderRadius: 16, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  para: {},
  paraGap: { marginTop: spacing.md },
  paraHead: { flexDirection: 'row', alignItems: 'center', marginBottom: 2 },
  letter: { fontWeight: '800', color: c.primary, fontSize: 16 },
  paraText: { fontSize: 18, lineHeight: 29, color: c.text },
  speaker: { fontSize: 13, fontWeight: '800', color: c.primary },
  turnGap: { marginTop: 6 },
  paraUz: { marginTop: 6, fontSize: 15, lineHeight: 22, color: c.textSecondary, fontStyle: 'italic' },
  section: { marginTop: spacing.lg, marginBottom: spacing.sm, fontSize: 13, fontWeight: '700', color: c.textSecondary, textTransform: 'uppercase' },
  card: { borderRadius: 16, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  gRow: { flexDirection: 'row', gap: spacing.sm, paddingHorizontal: spacing.md, paddingVertical: 9 },
  divider: { borderTopWidth: 1, borderTopColor: c.border },
  gEn: { flex: 1, fontWeight: '700', color: c.text },
  gUz: { flex: 1, color: c.textSecondary },
  gram: { marginBottom: spacing.sm, padding: spacing.md, borderRadius: 14, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  gramTitle: { fontWeight: '800', color: c.text },
  gramEx: { marginTop: 4, color: c.textSecondary, fontStyle: 'italic' },
  gramBtn: { flexDirection: 'row', alignItems: 'center', gap: 6, marginTop: 8, alignSelf: 'flex-start' },
  gramBtnText: { color: c.primary, fontWeight: '700' },
  footer: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: 0,
    padding: spacing.md,
    backgroundColor: c.surface,
    borderTopWidth: 1,
    borderTopColor: c.border,
  },
  best: { textAlign: 'center', marginBottom: 6, color: c.textSecondary, fontSize: 13 },
  start: { flexDirection: 'row', gap: 8, justifyContent: 'center', alignItems: 'center', padding: 15, borderRadius: 14, backgroundColor: c.primary },
  startText: { color: c.white, fontWeight: '800', fontSize: 16 },
}));
