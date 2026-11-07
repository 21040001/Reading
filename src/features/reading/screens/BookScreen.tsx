import React from 'react';
import { Pressable, ScrollView, Text, View } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { RouteProp, useNavigation, useRoute } from '@react-navigation/native';
import { RootStackParamList, StackNav } from '../../../app/navigation/AppNavigator';
import { useSettings } from '../../../app/settings/SettingsContext';
import { pick } from '../../../i18n/l10n';
import { makeStyles } from '../../../theme/makeStyles';
import { spacing } from '../../../theme/spacing';
import StatusIcon from '../components/StatusIcon';
import { getBook, getText, readingMinutes, wordCount } from '../content';
import useProgress from '../hooks/useProgress';

/** Kitob: boʻlimlar va matnlar */
export default function BookScreen() {
  const s = useStyles();
  const { t, language, colors } = useSettings();
  const nav = useNavigation<StackNav>();
  const { params } = useRoute<RouteProp<RootStackParamList, 'Book'>>();
  const book = getBook(params.bookId);
  const { progress } = useProgress();

  if (!book) {
    return null;
  }

  let n = 0;
  return (
    <ScrollView style={s.c} contentContainerStyle={s.p}>
      <Text style={s.level}>
        {book.level}
        {book.focus === 'exam' ? ' · IELTS · Multilevel' : ''}
      </Text>
      <Text style={s.sub}>{pick(book.subtitle, language)}</Text>
      {book.focus === 'exam' && (
        <View style={s.tip}>
          <Icon name="bulb-outline" size={18} color={colors.warning} />
          <Text style={s.tipText}>{t('book.examTip')}</Text>
        </View>
      )}

      {book.units.map((u, ui) => {
        const ready = u.texts.length > 0;
        return (
          <View key={u.id} style={[s.unit, !ready && s.unitSoon]}>
            <View style={s.unitHead}>
              <Text style={s.unitNo}>{ui + 1}</Text>
              <Text style={s.unitTitle}>{pick(u.title, language)}</Text>
            </View>
            {u.texts.map(id => {
              const tx = getText(id);
              if (!tx) {
                return null;
              }
              n++;
              const p = progress?.[id];
              return (
                <Pressable
                  key={id}
                  style={s.row}
                  onPress={() => nav.navigate('Reader', { textId: id })}
                  accessibilityRole="button">
                  <StatusIcon status={p?.status ?? 'new'} />
                  <View style={{ flex: 1 }}>
                    <Text style={s.rowTitle}>
                      {n}. {pick(tx.title, language)}
                    </Text>
                    <Text style={s.rowSub}>
                      {tx.en} · {t('text.minutes', { n: readingMinutes(tx) })} · {t('text.words', { n: wordCount(tx) })}
                    </Text>
                  </View>
                  {p?.best != null && <Text style={s.best}>{p.best}%</Text>}
                  <Icon name="chevron-forward" size={16} color={colors.textSecondary} />
                </Pressable>
              );
            })}
            {(u.planned ?? []).map((pl, i) => (
              <View key={`p${i}`} style={s.row}>
                <Icon name="time-outline" size={20} color={colors.textSecondary} />
                <Text style={[s.rowTitle, s.soonText]}>{pick(pl, language)}</Text>
                <Text style={s.soon}>{t('book.soon')}</Text>
              </View>
            ))}
          </View>
        );
      })}
    </ScrollView>
  );
}

const useStyles = makeStyles(c => ({
  c: { flex: 1, backgroundColor: c.background },
  p: { padding: spacing.lg, paddingBottom: 40 },
  level: { fontWeight: '800', color: c.primary },
  sub: { marginTop: 4, color: c.textSecondary, lineHeight: 20 },
  tip: {
    flexDirection: 'row',
    gap: 8,
    marginTop: spacing.md,
    padding: spacing.md,
    borderRadius: 14,
    backgroundColor: c.surface,
    borderWidth: 1,
    borderColor: c.warning,
  },
  tipText: { flex: 1, color: c.text, lineHeight: 20 },
  unit: { marginTop: spacing.md, borderRadius: 16, backgroundColor: c.surface, borderWidth: 1, borderColor: c.border, overflow: 'hidden' },
  unitSoon: { opacity: 0.75 },
  unitHead: { flexDirection: 'row', alignItems: 'center', gap: spacing.sm, padding: spacing.md, paddingBottom: 6 },
  unitNo: {
    width: 26,
    height: 26,
    borderRadius: 8,
    overflow: 'hidden',
    textAlign: 'center',
    lineHeight: 26,
    fontWeight: '800',
    color: c.white,
    backgroundColor: c.primary,
  },
  unitTitle: { flex: 1, fontSize: 16, fontWeight: '800', color: c.text },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    paddingHorizontal: spacing.md,
    paddingVertical: 11,
    borderTopWidth: 1,
    borderTopColor: c.border,
  },
  rowTitle: { flex: 1, fontWeight: '700', color: c.text },
  rowSub: { marginTop: 2, fontSize: 12, color: c.textSecondary },
  best: { fontWeight: '800', color: c.success },
  soonText: { color: c.textSecondary, fontWeight: '600' },
  soon: { fontSize: 11, color: c.textSecondary },
}));
