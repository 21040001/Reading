"""Okuma metinlerini Python'dan JSON'a yazmak için küçük yardımcılar."""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'features', 'reading', 'content', 'data')


def L(uz, en=None):
    d = {'uz': uz}
    if en:
        d['en'] = en
    return d


def P(en, uz=None):
    """Paragraf (İngilizce + isteğe bağlı Özbekçe çeviri)"""
    d = {'en': en}
    if uz:
        d['uz'] = uz
    return d


def G(en, uz):
    """Lugʻat satırı"""
    return {'en': en, 'uz': uz}


def GN(topic_id, uz, example, en=None):
    """Gramer notu → Grammar uygulamasındaki ders"""
    return {'topicId': topic_id, 'title': L(uz, en), 'example': example}


def _x(d, explain, para):
    if explain:
        d['explain'] = L(explain)
    if para is not None:
        d['para'] = para
    return d


def tf(statement, answer, explain=None, para=None, ng=False):
    """True/False(/Not Given). answer: 'T' | 'F' | 'NG'"""
    assert answer in ('T', 'F', 'NG')
    if answer == 'NG':
        ng = True
    d = {'type': 'tfng', 'statement': statement, 'answer': answer}
    if ng:
        d['ng'] = True
    return _x(d, explain, para)


def ch(prompt, options, answer, explain=None, para=None):
    return _x({'type': 'choice', 'prompt': prompt, 'options': options, 'answer': answer}, explain, para)


def gap(prompt, answers, explain=None, para=None, max_words=None):
    d = {'type': 'gap', 'prompt': prompt, 'answers': answers if isinstance(answers, list) else [answers]}
    if max_words:
        d['maxWords'] = max_words
    return _x(d, explain, para)


def hd(para, options, answer, explain=None):
    return _x({'type': 'heading', 'para': para, 'options': options, 'answer': answer}, explain, None)


def text(book, id, uz, en_title, level, kind, tag, intro, paragraphs, glossary, grammar, questions):
    qs = [{'id': f'{id}-q{i}', **q} for i, q in enumerate(questions, 1)]
    t = {
        'id': id, 'title': L(uz), 'en': en_title, 'level': level, 'kind': kind, 'tag': tag,
        'intro': L(intro), 'paragraphs': paragraphs, 'glossary': glossary, 'grammar': grammar,
        'questions': qs,
    }
    os.makedirs(os.path.join(OUT, book), exist_ok=True)
    path = os.path.join(OUT, book, f'{id}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(t, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(book, id, 'words:', sum(len(p['en'].split()) for p in paragraphs), 'q:', len(qs))
    return t
