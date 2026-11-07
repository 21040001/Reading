import React, { useState } from 'react';
import { Alert, Platform, Pressable } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import { useSettings } from '../../../app/settings/SettingsContext';
import { openVoiceInstaller, speakEnglish } from '../../../services/speech/speech';
import { makeStyles } from '../../../theme/makeStyles';

type Props = { text: string; size?: number; slow?: boolean };

/** 🔈 İngilizce cümleyi sesli okur */
export default function SpeakButton({ text, size = 34, slow }: Props) {
  const s = useStyles();
  const { colors, t } = useSettings();
  const [busy, setBusy] = useState(false);

  const onPress = async () => {
    if (busy) {
      return;
    }
    setBusy(true);
    try {
      if (!(await speakEnglish(text, slow))) {
        Alert.alert(
          t('speak.noVoiceTitle'),
          t('speak.noVoiceMsg'),
          Platform.OS === 'android'
            ? [
                { text: t('common.cancel'), style: 'cancel' },
                { text: t('speak.openSettings'), onPress: openVoiceInstaller },
              ]
            : [{ text: t('common.ok') }],
        );
      }
    } catch (e) {
      console.warn('[speech]', e);
    } finally {
      setBusy(false);
    }
  };

  return (
    <Pressable
      onPress={onPress}
      hitSlop={8}
      accessibilityRole="button"
      accessibilityLabel={t('speak.listen')}
      style={[s.btn, { width: size, height: size, borderRadius: size / 2 }, busy && s.busy]}>
      <Icon name={slow ? 'hourglass-outline' : 'volume-medium-outline'} size={size * 0.55} color={colors.primary} />
    </Pressable>
  );
}

const useStyles = makeStyles(c => ({
  btn: { alignItems: 'center', justifyContent: 'center', borderWidth: 1, borderColor: c.border, backgroundColor: c.surface },
  busy: { borderColor: c.primary },
}));
