import React from 'react';
import Icon from 'react-native-vector-icons/Ionicons';
import { useSettings } from '../../../app/settings/SettingsContext';
import type { TextStatus } from '../services/progress';

export default function StatusIcon({ status, size = 22 }: { status: TextStatus; size?: number }) {
  const { colors } = useSettings();
  switch (status) {
    case 'mastered':
      return <Icon name="star" size={size} color={colors.warning} />;
    case 'passed':
      return <Icon name="checkmark-circle" size={size} color={colors.success} />;
    case 'started':
      return <Icon name="ellipse-outline" size={size} color={colors.warning} />;
    default:
      return <Icon name="book-outline" size={size} color={colors.textSecondary} />;
  }
}
