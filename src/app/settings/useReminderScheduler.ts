import { useEffect } from 'react';
import { AppState } from 'react-native';
import { computeStreak, getActivity } from '../../core/progress/activity';
import { dueTexts, getAllProgress } from '../../features/reading/services/progress';
import { scheduleReminders } from '../../services/notifications/reminders';
import { useSettings } from './SettingsContext';

/** Uygulama açılınca, arka plana geçince ve ayar değişince hatırlatmaları yeniden planlar */
export default function useReminderScheduler() {
  const { reminderEnabled, reminderTime, dailyGoal, t } = useSettings();

  useEffect(() => {
    const run = async () => {
      const [log, progress] = await Promise.all([getActivity(), getAllProgress()]);
      const now = new Date();
      const streak = computeStreak(log, dailyGoal, now);
      await scheduleReminders({
        enabled: reminderEnabled,
        time: reminderTime,
        dueCount: dueTexts(progress).length,
        goalMetToday: streak.goalMet,
        streak: streak.current,
        t,
      });
    };
    run().catch(e => console.warn('[reminders]', e));
    const sub = AppState.addEventListener('change', st => {
      if (st === 'background' || st === 'active') {
        run().catch(() => undefined);
      }
    });
    return () => sub.remove();
  }, [reminderEnabled, reminderTime, dailyGoal, t]);
}
