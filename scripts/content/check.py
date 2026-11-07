"""İçerik denetimi (jest içerik testinin Python karşılığı) — yazarken hızlı kontrol için.
Kullanım:  python3 scripts/content/check.py [kitap ...]      (örn. a1)
Grammar konu id'leri GRAMMAR_IDS dosyasından okunur (varsa).
"""
import glob, json, os, re, sys

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, '..', '..', 'src', 'features', 'reading', 'content', 'data')
RANGE = {'A1': (50, 130), 'A2': (110, 260), 'B1': (230, 460), 'B2': (230, 650), 'C1': (550, 950)}
BAD = re.compile(r"[oOgG]['’`](?!clock)")
ids_file = os.path.join(HERE, 'grammar_ids.txt')
GRAMMAR_IDS = set(open(ids_file).read().split()) if os.path.exists(ids_file) else None


def norm(s):
    return s.lower().replace('’', "'")


def check(t):
    errs = []
    full = norm(' '.join(p['en'] for p in t['paragraphs']))
    n = len(full.split())
    lo, hi = RANGE[t['level']]
    if not lo <= n <= hi:
        errs.append(f'length {n} not in {lo}-{hi}')
    if len(t['paragraphs']) < 2:
        errs.append('need 2+ paragraphs')
    if len(t['questions']) < 6:
        errs.append('need 6+ questions')
    if len(t['glossary']) < 5:
        errs.append('need 5+ glossary entries')
    for p in t['paragraphs']:
        if re.search(r'\s{2,}|\(|\)', p['en']):
            errs.append(f'paragraph has parentheses/double space: {p["en"][:40]}')
        if t['level'] in ('A1', 'A2') and not p.get('uz'):
            errs.append('A1/A2 paragraph without uz')
    uz = [t['title']['uz'], t['intro']['uz'], t['tag']['uz']] + [p.get('uz', '') for p in t['paragraphs']] + \
         [g['uz'] for g in t['glossary']] + [g['title']['uz'] for g in t['grammar']] + \
         [q.get('explain', {}).get('uz', '') for q in t['questions']]
    for s in uz:
        if BAD.search(s):
            errs.append(f"ASCII apostrophe in Uzbek: {s[:50]}")
    for g in t['glossary']:
        ok = any(norm(v).removeprefix('be ').removeprefix('to ').split(' ')[0][:4] in full for v in g['en'].split(' / '))
        if not ok:
            errs.append(f'glossary word not in text: {g["en"]}')
    for g in t['grammar']:
        if GRAMMAR_IDS is not None and g['topicId'] not in GRAMMAR_IDS:
            errs.append(f'unknown Grammar topic: {g["topicId"]}')
        for piece in [x.strip() for x in g['example'].split('…') if x.strip()]:
            if norm(piece).rstrip('.!?') not in full:
                errs.append(f'grammar example not in text: {piece}')
    for q in t['questions']:
        qid = q['id']
        if not q.get('explain', {}).get('uz'):
            errs.append(f'{qid}: no explain')
        if 'para' in q and not 0 <= q['para'] < len(t['paragraphs']):
            errs.append(f'{qid}: bad para')
        if q['type'] == 'tfng':
            if t['level'] in ('A1', 'A2') and q.get('ng'):
                errs.append(f'{qid}: Not Given is for B1+')
            if q['answer'] == 'NG' and not q.get('ng'):
                errs.append(f'{qid}: NG without ng')
        elif q['type'] in ('choice', 'heading'):
            if len(q['options']) < 3 or len(set(q['options'])) != len(q['options']):
                errs.append(f'{qid}: need 3+ distinct options')
            if not 0 <= q['answer'] < len(q['options']):
                errs.append(f'{qid}: answer index')
        elif q['type'] == 'gap':
            if q['prompt'].count('___') != 1:
                errs.append(f'{qid}: need exactly one ___')
            if norm(q['answers'][0]) not in full:
                errs.append(f'{qid}: first answer not in text: {q["answers"][0]}')
            if q.get('maxWords') and any(len(a.split()) > q['maxWords'] for a in q['answers']):
                errs.append(f'{qid}: answer longer than maxWords')
    return errs


books = sys.argv[1:] or sorted(os.listdir(DATA))
total = 0
for b in books:
    for p in sorted(glob.glob(os.path.join(DATA, b, '*.json'))):
        t = json.load(open(p, encoding='utf-8'))
        e = check(t)
        total += len(e)
        print(('OK  ' if not e else 'ERR ') + t['id'], *(['\n   - ' + x for x in e] if e else []))
print('errors:', total)
sys.exit(1 if total else 0)
