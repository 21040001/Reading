import React, { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { useSettings } from '../../../../app/settings/SettingsContext';
import type { TFunction } from '../../../../i18n/strings';
import { makeStyles } from '../../../../theme/makeStyles';
import { spacing } from '../../../../theme/spacing';
import type { ChoiceQuestion, GapQuestion, HeadingQuestion, Question as Q, TfngQuestion } from '../../content/types';
import OptionList from './OptionList';
import Prompt from './Prompt';
import TextAnswer from './TextAnswer';
import { paraLetter, QuestionProps } from './types';

const TFNG: TfngQuestion['answer'][] = ['T', 'F', 'NG'];

export const tfngLabel = (a: TfngQuestion['answer'], t: TFunction) =>
  a === 'T' ? t('q.true') : a === 'F' ? t('q.false') : t('q.notGiven');

/** Geri bildirimde gösterilecek doğru cevap */
export function correctAnswerText(q: Q, t: TFunction): string {
  switch (q.type) {
    case 'tfng':
      return tfngLabel(q.answer, t);
    case 'choice':
    case 'heading':
      return q.options[q.answer];
    case 'gap':
      return q.answers[0];
  }
}

/** Kısa görev başlığı (sorunun üstünde) */
export function taskLabel(q: Q, t: TFunction): string {
  switch (q.type) {
    case 'tfng':
      return q.ng ? t('q.taskTfng') : t('q.taskTf');
    case 'choice':
      return t('q.taskChoice');
    case 'gap':
      return q.maxWords ? t('q.taskGapMax', { n: q.maxWords }) : t('q.taskGap');
    case 'heading':
      return t('q.taskHeading');
  }
}

function usePicked(id: string) {
  const [picked, setPicked] = useState<number | null>(null);
  useEffect(() => setPicked(null), [id]);
  return [picked, setPicked] as const;
}

function Tfng({ question, answered, onAnswer }: QuestionProps<TfngQuestion>) {
  const { t } = useSettings();
  const [picked, setPicked] = usePicked(question.id);
  const choices = question.ng ? TFNG : TFNG.slice(0, 2);
  const answer = choices.indexOf(question.answer);
  return (
    <View>
      <Prompt text={question.statement} />
      <OptionList
        options={choices.map(c => tfngLabel(c, t))}
        answer={answer}
        picked={picked}
        onPick={i => {
          if (answered || picked != null) {
            return;
          }
          setPicked(i);
          onAnswer(i === answer);
        }}
      />
    </View>
  );
}

function Choice({ question, answered, onAnswer }: QuestionProps<ChoiceQuestion>) {
  const [picked, setPicked] = usePicked(question.id);
  return (
    <View>
      <Prompt text={question.prompt} />
      <OptionList
        options={question.options}
        answer={question.answer}
        picked={picked}
        onPick={i => {
          if (answered || picked != null) {
            return;
          }
          setPicked(i);
          onAnswer(i === question.answer);
        }}
      />
    </View>
  );
}

function Gap({ question, answered, onAnswer }: QuestionProps<GapQuestion>) {
  return (
    <View>
      <Prompt text={question.prompt} />
      <TextAnswer resetKey={question.id} accepted={question.answers} answered={answered} onAnswer={onAnswer} />
    </View>
  );
}

function Heading({ question, paragraphs, answered, onAnswer }: QuestionProps<HeadingQuestion>) {
  const s = useStyles();
  const { t } = useSettings();
  const [picked, setPicked] = usePicked(question.id);
  const para = paragraphs[question.para] ?? '';
  const excerpt = para.length > 160 ? `${para.slice(0, 160).replace(/\s+\S*$/, '')} …` : para;
  return (
    <View>
      <Prompt text={t('q.headingFor', { p: paraLetter(question.para) })} />
      <View style={s.excerpt}>
        <Text style={s.letter}>{paraLetter(question.para)}</Text>
        <Text style={s.excerptText}>{excerpt}</Text>
      </View>
      <OptionList
        options={question.options}
        answer={question.answer}
        picked={picked}
        onPick={i => {
          if (answered || picked != null) {
            return;
          }
          setPicked(i);
          onAnswer(i === question.answer);
        }}
      />
    </View>
  );
}

/** Savol turiga qarab kerakli komponent */
export default function Question({ question, ...rest }: Omit<QuestionProps<Q>, 'question'> & { question: Q }) {
  switch (question.type) {
    case 'tfng':
      return <Tfng question={question} {...rest} />;
    case 'choice':
      return <Choice question={question} {...rest} />;
    case 'gap':
      return <Gap question={question} {...rest} />;
    case 'heading':
      return <Heading question={question} {...rest} />;
  }
}

const useStyles = makeStyles(c => ({
  excerpt: {
    flexDirection: 'row',
    gap: spacing.sm,
    marginTop: spacing.md,
    padding: spacing.md,
    borderRadius: 12,
    backgroundColor: c.surface,
    borderWidth: 1,
    borderColor: c.border,
  },
  letter: { fontWeight: '800', color: c.primary, fontSize: 16 },
  excerptText: { flex: 1, color: c.textSecondary, lineHeight: 21, fontStyle: 'italic' },
}));
