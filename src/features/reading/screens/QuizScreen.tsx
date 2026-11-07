import React, { useCallback, useEffect, useRef, useState } from 'react';
import { Alert, KeyboardAvoidingView, Modal, Platform, Pressable, ScrollView, Text, View } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { RouteProp, useNavigation, useRoute } from '@react-navigation/native';
import { RootStackParamList, StackNav } from '../../../app/navigation/AppNavigator';
import { useSettings } from '../../../app/settings/SettingsContext';
import { pick } from '../../../i18n/l10n';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import ProgressBar from '../components/ProgressBar';
import Question, { correctAnswerText, taskLabel } from '../components/questions/Questions';
import { paraLetter } from '../components/questions/types';
import { getText } from '../content';
import type { ReadingText } from '../content/types';
import { FinishResult, finishText, getAllProgress, nextText, recordAnswer } from '../services/progress';
import { reportByEmail, reportByTelegram, reportText } from '../utils/report';

/** Matn savollari: bittadan, har biridan keyin izoh; oxirida natija */
export default function QuizScreen() {
  const s = useStyles();
  const { t, language, colors } = useSettings();
  const nav = useNavigation<StackNav>();
  const { params } = useRoute<RouteProp<RootStackParamList, 'Quiz'>>();
  const text = getText(params.textId);

  const [index, setIndex] = useState(0);
  const [current, setCurrent] = useState<boolean | null>(null);
  const [results, setResults] = useState<boolean[]>([]);
  const [finished, setFinished] = useState<FinishResult | null>(null);
  const [next, setNext] = useState<ReadingText | null>(null);
  const [showText, setShowText] = useState<{ open: boolean; para?: number }>({ open: false });
  const scrollRef = useRef<ScrollView>(null);

  const restart = useCallback(() => {
    setIndex(0);
    setCurrent(null);
    setResults([]);
    setFinished(null);
  }, []);

  useEffect(restart, [params.textId, restart]);

  if (!text) {
    return null;
  }
  const qs = text.questions;

  if (finished) {
    const correct = results.filter(Boolean).length;
    return (
      <ScrollView style={s.c} contentContainerStyle={s.p}>
        <Text style={s.emoji}>{finished.passed ? '🎉' : '📖'}</Text>
        <Text style={s.title}>{finished.passed ? t('quiz.passed') : t('quiz.notPassed')}</Text>
        <Text style={[s.score, !finished.passed && s.scoreLow]}>{finished.score}%</Text>
        <Text style={s.sub}>
          {t('quiz.correctOf', { n: correct, total: qs.length })} ·{' '}
          {finished.isNewBest ? t('quiz.newBest') : t('quiz.best', { n: finished.best })}
        </Text>
        {!finished.passed && <Text style={s.hint}>{t('quiz.tryAgainHint')}</Text>}

        <View style={s.card}>
          {qs.map((q, i) => (
            <View key={q.id} style={[s.row, i > 0 && s.divider]}>
              <Icon
                name={results[i] ? 'checkmark-circle' : 'close-circle'}
                size={20}
                color={results[i] ? colors.success : colors.danger}
              />
              <Text style={s.rowText} numberOfLines={2}>
                {i + 1}. {q.type === 'tfng' ? q.statement : q.type === 'heading' ? t('q.headingFor', { p: paraLetter(q.para) }) : q.prompt}
              </Text>
              {!results[i] && <Text style={s.rowAns}>{correctAnswerText(q, t)}</Text>}
            </View>
          ))}
        </View>

        {next && finished.passed && (
          <Pressable style={s.primary} onPress={() => nav.replace('Reader', { textId: next.id })}>
            <Text style={s.primaryText}>{t('quiz.nextText', { title: pick(next.title, language) })}</Text>
          </Pressable>
        )}
        {!finished.passed && (
          <Pressable style={s.primary} onPress={() => nav.goBack()}>
            <Text style={s.primaryText}>{t('quiz.rereadText')}</Text>
          </Pressable>
        )}
        <Pressable style={s.secondary} onPress={restart}>
          <Text style={s.secondaryText}>{t('quiz.retry')}</Text>
        </Pressable>
        <Pressable style={s.secondary} onPress={() => nav.popToTop()}>
          <Text style={s.secondaryText}>{t('common.toHome')}</Text>
        </Pressable>
      </ScrollView>
    );
  }

  const q = qs[index];
  const last = index === qs.length - 1;

  const report = () => {
    const body = reportText(text, q, correctAnswerText(q, t));
    Alert.alert(t('report.title'), t('report.message'), [
      { text: t('common.cancel'), style: 'cancel' },
      { text: 'E-mail', onPress: () => reportByEmail(body).catch(() => undefined) },
      { text: 'Telegram', onPress: () => reportByTelegram(body).catch(() => undefined) },
    ]);
  };

  const onAnswer = (ok: boolean) => {
    if (current != null) {
      return;
    }
    setCurrent(ok);
    setResults(r => [...r, ok]);
    recordAnswer(ok).catch(e => console.warn('[quiz]', e));
  };

  const goNext = async () => {
    if (!last) {
      setIndex(i => i + 1);
      setCurrent(null);
      return;
    }
    const correct = results.filter(Boolean).length;
    try {
      const r = await finishText(text.id, correct, qs.length);
      const prog = await getAllProgress();
      setNext(nextText(prog, undefined));
      setFinished(r);
    } catch (e) {
      console.warn('[quiz] finish', e);
      setFinished({ score: Math.round((correct / qs.length) * 100), best: 0, isNewBest: false, passed: correct / qs.length >= 0.7 });
    }
  };

  return (
    <KeyboardAvoidingView style={s.c} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
      <View style={s.top}>
        <View style={{ flex: 1 }}>
          <ProgressBar value={(index + (current != null ? 1 : 0)) / qs.length} />
          <Text style={s.counter}>{t('quiz.counter', { n: index + 1, total: qs.length })}</Text>
        </View>
        <Pressable style={s.textBtn} onPress={() => setShowText({ open: true })} accessibilityRole="button" testID="show-text">
          <Icon name="document-text-outline" size={18} color={colors.primary} />
          <Text style={s.textBtnText}>{t('quiz.text')}</Text>
        </Pressable>
      </View>

      <ScrollView contentContainerStyle={s.p} keyboardShouldPersistTaps="handled">
        <Text style={s.task}>{taskLabel(q, t)}</Text>
        <Question
          key={q.id}
          question={q}
          paragraphs={text.paragraphs.map(p => p.en)}
          answered={current != null}
          onAnswer={onAnswer}
        />

        {current != null && (
          <View style={[s.feedback, current ? s.fbOk : s.fbBad]}>
            <Text style={[s.fbTitle, { color: current ? colors.success : colors.danger }]}>
              {current ? t('q.correct') : t('q.wrong')}
            </Text>
            {!current && <Text style={s.fbAnswer}>{t('q.answerIs', { a: correctAnswerText(q, t) })}</Text>}
            {q.explain && <Text style={s.fbExplain}>{pick(q.explain, language)}</Text>}
            {q.para != null && (
              <Pressable style={s.fbLink} onPress={() => setShowText({ open: true, para: q.para })} accessibilityRole="button">
                <Icon name="search-outline" size={16} color={colors.primary} />
                <Text style={s.fbLinkText}>{t('quiz.showInText', { p: paraLetter(q.para) })}</Text>
              </Pressable>
            )}
            <Pressable style={s.fbLink} onPress={report} accessibilityRole="button">
              <Icon name="flag-outline" size={16} color={colors.textSecondary} />
              <Text style={s.fbReport}>{t('report.button')}</Text>
            </Pressable>
          </View>
        )}
      </ScrollView>

      {current != null && (
        <View style={s.footer}>
          <Pressable style={s.nextBtn} onPress={goNext} accessibilityRole="button">
            <Text style={s.primaryText}>{last ? t('quiz.finish') : t('quiz.next')}</Text>
          </Pressable>
        </View>
      )}

      <Modal visible={showText.open} animationType="slide" onRequestClose={() => setShowText({ open: false })}>
        <View style={s.modal}>
          <View style={s.modalHead}>
            <Text style={s.modalTitle} numberOfLines={1}>
              {text.en}
            </Text>
            <Pressable onPress={() => setShowText({ open: false })} hitSlop={10} accessibilityRole="button">
              <Icon name="close" size={26} color={colors.text} />
            </Pressable>
          </View>
          <ScrollView ref={scrollRef} contentContainerStyle={s.p}>
            {text.paragraphs.map((p, i) => (
              <View
                key={i}
                style={[s.mPara, showText.para === i && s.mParaHi]}
                onLayout={e => {
                  if (showText.para === i) {
                    scrollRef.current?.scrollTo({ y: Math.max(0, e.nativeEvent.layout.y - 12), animated: true });
                  }
                }}>
                <Text style={s.mLetter}>{paraLetter(i)}</Text>
                <Text style={s.mText}>{p.en}</Text>
              </View>
            ))}
          </ScrollView>
        </View>
      </Modal>
    </KeyboardAvoidingView>
  );
}

const useStyles = makeStyles(c => ({
  c: { flex: 1, backgroundColor: c.background },
  p: { padding: spacing.lg, paddingBottom: 120 },
  top: { flexDirection: 'row', alignItems: 'center', gap: spacing.md, paddingHorizontal: spacing.lg, paddingTop: spacing.md },
  counter: { marginTop: 4, fontSize: 12, color: c.textSecondary },
  textBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: c.border,
    backgroundColor: c.surface,
  },
  textBtnText: { color: c.primary, fontWeight: '700' },
  task: { marginBottom: spacing.sm, fontSize: 13, fontWeight: '700', color: c.textSecondary },
  feedback: { marginTop: spacing.lg, padding: spacing.md, borderRadius: 14, borderWidth: 1, backgroundColor: c.surface },
  fbOk: { borderColor: c.success },
  fbBad: { borderColor: c.danger },
  fbTitle: { fontSize: 17, fontWeight: '800' },
  fbAnswer: { marginTop: 4, color: c.text, fontWeight: '700' },
  fbExplain: { marginTop: 6, color: c.text, lineHeight: 21 },
  fbLink: { flexDirection: 'row', alignItems: 'center', gap: 6, marginTop: 10 },
  fbLinkText: { color: c.primary, fontWeight: '700' },
  fbReport: { color: c.textSecondary },
  footer: { position: 'absolute', left: 0, right: 0, bottom: 0, padding: spacing.md, backgroundColor: c.background },
  nextBtn: { padding: 15, borderRadius: 14, alignItems: 'center', backgroundColor: c.primary },
  modal: { flex: 1, backgroundColor: c.background },
  modalHead: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    padding: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: c.border,
    backgroundColor: c.surface,
  },
  modalTitle: { flex: 1, fontSize: 17, fontWeight: '800', color: c.text },
  mPara: { flexDirection: 'row', gap: spacing.sm, padding: spacing.sm, borderRadius: 12, marginBottom: spacing.sm },
  mParaHi: { backgroundColor: c.surface, borderWidth: 2, borderColor: c.primary },
  mLetter: { fontWeight: '800', color: c.primary },
  mText: { flex: 1, fontSize: 17, lineHeight: 27, color: c.text },
  emoji: { fontSize: 56, textAlign: 'center', marginTop: spacing.md },
  title: { marginTop: spacing.sm, fontSize: 24, fontWeight: '800', color: c.text, textAlign: 'center' },
  score: { marginTop: spacing.sm, fontSize: 56, fontWeight: '800', color: c.success, textAlign: 'center' },
  scoreLow: { color: c.warning },
  sub: { color: c.textSecondary, textAlign: 'center' },
  hint: { marginTop: spacing.sm, color: c.textSecondary, textAlign: 'center', lineHeight: 20 },
  card: { marginTop: spacing.lg, borderRadius: 16, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  row: { flexDirection: 'row', alignItems: 'center', gap: 10, padding: spacing.md },
  divider: { borderTopWidth: 1, borderTopColor: c.border },
  rowText: { flex: 1, color: c.text },
  rowAns: { maxWidth: '35%', fontWeight: '700', color: c.success, textAlign: 'right' },
  primary: { marginTop: spacing.lg, padding: 15, borderRadius: 14, alignItems: 'center', backgroundColor: c.primary },
  primaryText: { color: c.white, fontWeight: '800', fontSize: 16 },
  secondary: { marginTop: spacing.sm, padding: 14, borderRadius: 14, alignItems: 'center' },
  secondaryText: { color: c.primary, fontWeight: '700', fontSize: 16 },
}));
