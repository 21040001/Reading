import { useCallback, useState } from 'react';
import { useFocusEffect } from '@react-navigation/native';
import { getAllProgress, TextProgress } from '../services/progress';

/** Ekran her açıldığında metinlerin durumunu yeniden okur */
export default function useProgress() {
  const [progress, setProgress] = useState<Record<string, TextProgress> | null>(null);
  const reload = useCallback(() => {
    getAllProgress()
      .then(setProgress)
      .catch(e => console.warn('[progress]', e));
  }, []);
  useFocusEffect(reload);
  return { progress, reload };
}
