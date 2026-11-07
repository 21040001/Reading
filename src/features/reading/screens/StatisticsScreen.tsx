import React, { useCallback, useState } from 'react';
import { ScrollView, Text, View } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { useSettings } from '../../../app/settings/SettingsContext';
import { APP } from '../../../core/config';
import { ActivityLog, computeStreak, getActivity, lastDays } from '../../../core/progress/activity';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import ActivityHeatmap from '../../progress/components/ActivityHeatmap';
import WeeklyChart from '../../progress/components/WeeklyChart';
import { allTexts } from '../content';
import useProgress from '../hooks/useProgress';
import { readingStats } from '../services/progress';

export default function StatisticsScreen() {
  const s = useStyles();
  const { t, dailyGoal } = useSettings();
  const { progress } = useProgress();
  const [log, setLog] = useState<ActivityLog>({});
  const [own, setOwn] = useState<ActivityLog>({});

  useFocusEffect(
    useCallback(() => {
      getActivity().then(setLog).catch(() => undefined); // tüm uygulamalar: ortak seri
      getActivity(APP.key).then(setOwn).catch(() => undefined); // sadece okuma
    }, []),
  );

  const streak = computeStreak(log, dailyGoal);
  const texts = allTexts();
  const st = progress ? readingStats(progress) : { textsDone: 0, wordsRead: 0, avgScore: null };
  const passed = texts.filter(x => ['passed', 'mastered'].includes(progress?.[x.id]?.status ?? '')).length;
  const answers = Object.values(own).reduce((a, d) => a + d.reviews, 0);
  const correct = Object.values(own).reduce((a, d) => a + d.correct, 0);

  const cards: [string, string | number][] = [
    [t('stats.textsPassed'), `${passed} / ${texts.length}`],
    [t('stats.wordsRead'), st.wordsRead],
    [t('stats.avgScore'), st.avgScore == null ? '—' : `${st.avgScore}%`],
    [t('stats.accuracy'), (answers ? Math.round((correct / answers) * 100) : 0) + '%'],
  ];

  return (
    <ScrollView style={s.c} contentContainerStyle={s.p}>
      <View style={s.streakRow}>
        <View style={s.box}>
          <Text style={s.big}>🔥 {streak.current}</Text>
          <Text style={s.l}>{t('streak.days', { n: streak.current })}</Text>
        </View>
        <View style={s.box}>
          <Text style={s.big}>🏆 {streak.best}</Text>
          <Text style={s.l}>{t('streak.best', { n: streak.best })}</Text>
        </View>
      </View>
      <Text style={s.shared}>{t('stats.sharedNote')}</Text>

      <View style={s.grid}>
        {cards.map(([label, value]) => (
          <View key={label} style={s.card}>
            <Text style={s.n}>{value}</Text>
            <Text style={s.l}>{label}</Text>
          </View>
        ))}
      </View>

      <View style={s.sec}>
        <Text style={s.st}>{t('stats.week')}</Text>
        <WeeklyChart days={lastDays(log, 7)} goal={dailyGoal} />
      </View>
      <View style={s.sec}>
        <Text style={s.st}>{t('stats.activity')}</Text>
        <ActivityHeatmap log={log} goal={dailyGoal} />
        <Text style={s.l}>{t('stats.activeDays', { n: streak.activeDays })}</Text>
      </View>
    </ScrollView>
  );
}

const useStyles = makeStyles(c => ({
  c: { flex: 1, backgroundColor: c.background },
  p: { padding: spacing.lg, paddingBottom: 40 },
  streakRow: { flexDirection: 'row', gap: 8 },
  box: { flex: 1, padding: 16, borderRadius: 14, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  big: { fontSize: 24, fontWeight: '800', color: c.text },
  shared: { marginTop: 6, fontSize: 12, color: c.textSecondary },
  sec: { marginTop: 16, padding: 20, borderRadius: 16, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  st: { fontSize: 18, fontWeight: '700', color: c.text },
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginTop: 16 },
  card: { width: '48%', padding: 16, borderRadius: 14, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border },
  n: { fontSize: 24, fontWeight: '700', color: c.primary },
  l: { marginTop: 4, color: c.textSecondary },
}));
