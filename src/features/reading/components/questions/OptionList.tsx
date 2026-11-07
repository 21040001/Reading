import React from 'react';
import { Pressable, Text, View } from 'react-native';
import { makeStyles } from '../../../../theme/makeStyles';
import { spacing } from '../../../../theme/spacing';

type Props = {
  options: string[];
  answer: number;
  picked: number | null;
  onPick: (i: number) => void;
};

/** Şıklar: cevaptan sonra doğru yeşil, seçilen yanlış kırmızı */
export default function OptionList({ options, answer, picked, onPick }: Props) {
  const s = useStyles();
  const done = picked != null;
  return (
    <View style={s.list}>
      {options.map((o, i) => {
        const state = !done ? null : i === answer ? 'ok' : i === picked ? 'bad' : 'dim';
        return (
          <Pressable
            key={i}
            disabled={done}
            onPress={() => onPick(i)}
            accessibilityRole="button"
            style={[s.opt, state === 'ok' && s.okBox, state === 'bad' && s.badBox, state === 'dim' && s.dim]}>
            <Text style={[s.optText, (state === 'ok' || state === 'bad') && s.strong]}>{o}</Text>
          </Pressable>
        );
      })}
    </View>
  );
}

const useStyles = makeStyles(c => ({
  list: { marginTop: spacing.lg, gap: 10 },
  opt: { padding: 15, borderRadius: 14, borderWidth: 2, borderColor: c.border, backgroundColor: c.surface },
  optText: { fontSize: 17, color: c.text },
  okBox: { borderColor: c.success },
  badBox: { borderColor: c.danger },
  dim: { opacity: 0.5 },
  strong: { fontWeight: '700' },
}));
