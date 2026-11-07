import React from 'react';
import { Text } from 'react-native';
import { makeStyles } from '../../../../theme/makeStyles';

/** Savol matni; "___" boʻsh joy sifatida ajratib koʻrsatiladi */
export default function Prompt({ text, small }: { text: string; small?: boolean }) {
  const s = useStyles();
  const parts = text.split('___');
  return (
    <Text style={[s.prompt, small && s.small]}>
      {parts.map((p, i) => (
        <React.Fragment key={i}>
          {p}
          {i < parts.length - 1 && <Text style={s.blank}>{'  _____  '}</Text>}
        </React.Fragment>
      ))}
    </Text>
  );
}

const useStyles = makeStyles(c => ({
  prompt: { fontSize: 20, lineHeight: 29, color: c.text, fontWeight: '600' },
  small: { fontSize: 17, lineHeight: 25 },
  blank: { color: c.primary, fontWeight: '800', textDecorationLine: 'underline' },
}));
