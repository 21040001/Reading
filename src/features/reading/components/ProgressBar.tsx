import React from 'react';
import { View } from 'react-native';
import { makeStyles } from '../../../theme/makeStyles';

/** 0–1 arası ilerleme çubuğu */
export default function ProgressBar({ value, height = 8 }: { value: number; height?: number }) {
  const s = useStyles();
  const pct = Math.round(Math.max(0, Math.min(1, value)) * 100);
  return (
    <View style={[s.track, { height, borderRadius: height / 2 }]}>
      <View style={[s.fill, { height, width: `${pct}%` }]} />
    </View>
  );
}

const useStyles = makeStyles(c => ({
  track: { backgroundColor: c.border, overflow: 'hidden' },
  fill: { backgroundColor: c.primary },
}));
