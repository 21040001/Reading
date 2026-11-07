import React, { useCallback, useState } from 'react';
import { Pressable, ScrollView, Text, View } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { useFocusEffect, useNavigation } from '@react-navigation/native';
import { StackNav } from '../../../app/navigation/AppNavigator';
import { useSettings } from '../../../app/settings/SettingsContext';
import { computeStreak, getActivity, StreakInfo } from '../../../core/progress/activity';
import { getProfile } from '../../../core/profile/profile';
import { pick } from '../../../i18n/l10n';
import { Colors } from '../../../theme/colors';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import StreakCard from '../../progress/components/StreakCard';
import ProgressBar from '../components/ProgressBar';
import { BOOKS, bookPlannedCount, bookTexts, readingMinutes, wordCount } from '../content';
import useProgress from '../hooks/useProgress';
import { dueTexts, nextText } from '../services/progress';

export default function HomeScreen() {
  const s = useStyles();
  const { t, language, colors, dailyGoal } = useSettings();
  const nav = useNavigation<StackNav>();
  const { progress } = useProgress();
  const [streak, setStreak] = useState<StreakInfo | null>(null);
  const [levelBook, setLevelBook] = useState<string | undefined>(undefined);

  useFocusEffect(
    useCallback(() => {
      getActivity()
        .then(log => setStreak(computeStreak(log, dailyGoal)))
        .catch(() => undefined);
      // Grammar'daki seviye testi natijasi (umumiy profil) — mos kitobdan boshlash
      getProfile()
        .then(p => setLevelBook(p.level ? BOOKS.find(b => b.level === p.level)?.id : undefined))
        .catch(() => undefined);
    }, [dailyGoal]),
  );

  const next = progress ? nextText(progress, levelBook) : null;
  const due = progress ? dueTexts(progress) : [];

  return (
    <ScrollView style={s.c} contentContainerStyle={s.p}>
      <Text style={s.title}>{t('home.title')}</Text>
      <Text style={s.sub}>{t('home.subtitle')}</Text>

      {streak && <View style={{ marginTop: spacing.md }}><StreakCard info={streak} onPractice={() => next && nav.navigate('Reader', { textId: next.id })} /></View>}

      {next && (
        <Pressable style={s.next} onPress={() => nav.navigate('Reader', { textId: next.id })} accessibilityRole="button">
          <Text style={s.nextLabel}>{progress?.[next.id]?.status === 'started' ? t('home.continue') : t('home.nextText')}</Text>
          <Text style={s.nextTitle}>{pick(next.title, language)}</Text>
          <Text style={s.nextMeta}>
            {next.level} · {t('text.words', { n: wordCount(next) })} · {t('text.minutes', { n: readingMinutes(next) })}
          </Text>
          <View style={s.nextBtn}>
            <Icon name="book" size={18} color={colors.white} />
            <Text style={s.nextBtnText}>{t('home.read')}</Text>
          </View>
        </Pressable>
      )}

      {due.length > 0 && (
        <Pressable style={s.due} onPress={() => nav.navigate('Reader', { textId: due[0].id })} accessibilityRole="button">
          <Icon name="refresh-circle" size={26} color={colors.warning} />
          <View style={{ flex: 1 }}>
            <Text style={s.dueTitle}>{t('home.reread', { n: due.length })}</Text>
            <Text style={s.dueSub}>{pick(due[0].title, language)}</Text>
          </View>
          <Icon name="chevron-forward" size={18} color={colors.textSecondary} />
        </Pressable>
      )}

      <Text style={s.section}>{t('home.books')}</Text>
      {BOOKS.map(book => {
        const texts = bookTexts(book);
        const done = texts.filter(x => ['passed', 'mastered'].includes(progress?.[x.id]?.status ?? '')).length;
        const planned = bookPlannedCount(book);
        const color = colors[(book.color ?? 'primary') as keyof Colors] as string;
        return (
          <Pressable
            key={book.id}
            style={s.book}
            onPress={() => nav.navigate('Book', { bookId: book.id })}
            accessibilityRole="button">
            <View style={[s.spine, { backgroundColor: color }]}>
              <Text style={s.spineText}>{book.level}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <View style={s.bookHead}>
                <Text style={s.bookTitle}>{pick(book.title, language)}</Text>
                {book.focus === 'exam' && <Text style={s.examChip}>IELTS · Multilevel</Text>}
              </View>
              <Text style={s.bookSub} numberOfLines={2}>
                {pick(book.subtitle, language)}
              </Text>
              {texts.length > 0 ? (
                <>
                  <View style={{ marginTop: 8 }}>
                    <ProgressBar value={texts.length ? done / texts.length : 0} height={6} />
                  </View>
                  <Text style={s.bookMeta}>
                    {t('book.progress', { done, total: texts.length })} · {t('book.ready', { ready: texts.length, total: planned })}
                  </Text>
                </>
              ) : (
                <Text style={s.bookMeta}>{t('book.soonCount', { total: planned })}</Text>
              )}
            </View>
          </Pressable>
        );
      })}
    </ScrollView>
  );
}

const useStyles = makeStyles(c => ({
  c: { flex: 1, backgroundColor: c.background },
  p: { padding: spacing.lg, paddingBottom: 40 },
  title: { fontSize: 26, fontWeight: '800', color: c.text },
  sub: { marginTop: 2, color: c.textSecondary },
  next: { marginTop: spacing.md, padding: spacing.lg, borderRadius: 18, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  nextLabel: { fontSize: 12, fontWeight: '800', color: c.primary, textTransform: 'uppercase' },
  nextTitle: { marginTop: 4, fontSize: 20, fontWeight: '800', color: c.text },
  nextMeta: { marginTop: 2, color: c.textSecondary },
  nextBtn: {
    flexDirection: 'row',
    gap: 8,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: spacing.md,
    padding: 13,
    borderRadius: 12,
    backgroundColor: c.primary,
  },
  nextBtnText: { color: c.white, fontWeight: '800', fontSize: 16 },
  due: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    marginTop: spacing.sm,
    padding: spacing.md,
    borderRadius: 14,
    backgroundColor: c.surface,
    borderWidth: 1,
    borderColor: c.warning,
  },
  dueTitle: { fontWeight: '800', color: c.text },
  dueSub: { marginTop: 2, fontSize: 13, color: c.textSecondary },
  section: { marginTop: spacing.lg, marginBottom: spacing.sm, fontSize: 13, fontWeight: '700', color: c.textSecondary, textTransform: 'uppercase' },
  book: {
    flexDirection: 'row',
    gap: spacing.md,
    marginBottom: spacing.sm,
    padding: spacing.md,
    borderRadius: 16,
    backgroundColor: c.surface,
    borderWidth: 1,
    borderColor: c.border,
  },
  spine: { width: 46, borderRadius: 10, alignItems: 'center', justifyContent: 'center', minHeight: 64 },
  spineText: { color: c.white, fontWeight: '800', fontSize: 16 },
  bookHead: { flexDirection: 'row', alignItems: 'center', gap: 6, flexWrap: 'wrap' },
  bookTitle: { fontSize: 17, fontWeight: '800', color: c.text },
  examChip: {
    paddingHorizontal: 6,
    paddingVertical: 1,
    borderRadius: 6,
    overflow: 'hidden',
    fontSize: 11,
    fontWeight: '700',
    color: c.danger,
    borderWidth: 1,
    borderColor: c.danger,
  },
  bookSub: { marginTop: 2, fontSize: 13, color: c.textSecondary, lineHeight: 18 },
  bookMeta: { marginTop: 4, fontSize: 12, color: c.textSecondary },
}));
