import React, { useEffect, useState } from 'react';
import { Pressable, Text, TextInput, View } from 'react-native';
import { useSettings } from '../../../../app/settings/SettingsContext';
import { makeStyles } from '../../../../theme/makeStyles';
import { spacing } from '../../../../theme/spacing';
import { isAnswerCorrect } from '../../utils/answer';

type Props = {
  resetKey: string;
  accepted: string[];
  answered: boolean;
  onAnswer: (correct: boolean) => void;
  placeholder?: string;
};

/** Yazarak cevap: kutu + Tekshirish düğmesi */
export default function TextAnswer({ resetKey, accepted, answered, onAnswer, placeholder }: Props) {
  const s = useStyles();
  const { t, colors } = useSettings();
  const [value, setValue] = useState('');
  const [result, setResult] = useState<boolean | null>(null);
  useEffect(() => {
    setValue('');
    setResult(null);
  }, [resetKey]);

  const check = () => {
    if (answered || !value.trim()) {
      return;
    }
    const ok = isAnswerCorrect(value, accepted);
    setResult(ok);
    onAnswer(ok);
  };

  return (
    <View style={{ marginTop: spacing.lg }}>
      <TextInput
        value={value}
        onChangeText={setValue}
        editable={!answered}
        autoCapitalize="none"
        autoCorrect={false}
        spellCheck={false}
        placeholder={placeholder ?? t('q.typeHere')}
        placeholderTextColor={colors.textSecondary}
        onSubmitEditing={check}
        returnKeyType="done"
        style={[s.input, result === true && s.ok, result === false && s.bad]}
      />
      {!answered && (
        <Pressable style={[s.btn, !value.trim() && s.btnOff]} disabled={!value.trim()} onPress={check}>
          <Text style={s.btnText}>{t('q.check')}</Text>
        </Pressable>
      )}
    </View>
  );
}

const useStyles = makeStyles(c => ({
  input: {
    padding: 15,
    fontSize: 18,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: c.border,
    backgroundColor: c.surface,
    color: c.text,
  },
  ok: { borderColor: c.success },
  bad: { borderColor: c.danger },
  btn: { marginTop: spacing.md, padding: 15, borderRadius: 14, alignItems: 'center', backgroundColor: c.primary },
  btnOff: { opacity: 0.5 },
  btnText: { color: c.white, fontWeight: '800', fontSize: 16 },
}));
