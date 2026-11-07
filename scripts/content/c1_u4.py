"""C1 · 4-boʻlim: Fikr va munozara (Opinion and debate) — argumentativ esselar"""
from lib import *

B = 'c1'


def intro(what, extra):
    return (f'Fikr-mulohaza matni (argumentativ esse): {what} Bu matnda True/False/Not Given savollari muallifning '
            'qarashlari haqida — IELTSdagi YES / NO / NOT GIVEN kabi: TRUE (YES) — muallif shu fikrni bildiradi; '
            'FALSE (NO) — muallif bunga zid fikrda; NOT GIVEN — muallif bu masalada fikr bildirmagan. '
            'Faktlarni emas, muallifning munosabatini koʻrsatuvchi soʻzlarni qidiring: I would argue, in my view, '
            f'arguably, it seems to me, with some justification. {extra} Taxminan 20 daqiqa ajrating.')


# ---------------------------------------------------------------- 16
H16 = ['Why removing a fee may not change who visits', 'The principle of open doors',
       'An argument from financial necessity', 'Why the income argument is overstated',
       'A practical middle way', 'Barriers beyond the ticket price',
       'How museums decide what to display', 'The history of public collections']

text(B, 'c1-16-free-museums', 'Muzeylar bepul boʻlishi kerakmi?', 'Should Museums Be Free?', 'C1', 'exam',
     L('Madaniyat va jamiyat', 'Culture and society'),
     intro('muzeylarga kirish bepul boʻlishi yoki pullik boʻlishi haqida — imkoniyat va moliyalashtirish oʻrtasidagi bahs.',
           'Avval sarlavhalarni moslang: har bir xatboshining birinchi va oxirgi jumlasi muallif fikrining yoʻnalishini koʻrsatadi.'),
     [
         P("Few questions in cultural policy provoke as much quiet disagreement as whether public museums should charge "
           "visitors for admission. On one side stand those who regard a museum as a civic institution, comparable to a "
           "public library, whose collections belong in some meaningful sense to everyone. On the other are those who "
           "point out that collections must be conserved, buildings heated and staff paid, and that someone has to bear "
           "these costs. My own view is that both camps are right about something important, and that the debate is "
           "often conducted as if a single answer must apply to every institution."),
         P("The case for free entry rests largely on the principle of access. A charge that seems trivial to a "
           "comfortably off tourist may be a genuine deterrent to a family on a low income, or to a teenager who simply "
           "wants to wander in out of curiosity. Free admission removes not only a financial barrier but also a "
           "psychological one: it signals that the building is a place where anyone is welcome, rather than a venue "
           "reserved for those who already feel at home in it. Where entry has been made free, attendance has generally "
           "been reported to rise, although it is less clear whether the new visitors come from groups that previously "
           "stayed away."),
         P("That last point deserves more attention than campaigners usually give it. Abolishing a ticket price does not "
           "automatically change who feels entitled to walk through the door. People who grew up visiting galleries are "
           "likely to make the most of free entry, visiting more often and staying longer, while those for whom museums "
           "seemed distant and formal may continue to stay away. In other words, free admission may be a necessary "
           "condition for wider participation, but it is unlikely to be a sufficient one. Outreach work with schools "
           "and local communities, and exhibitions that speak to a broad range of experiences, arguably matter at least "
           "as much as the price at the door."),
         P("The case for charging is usually presented as a matter of hard necessity. Public funding for culture is "
           "rarely generous and is often among the first budgets to be cut when governments face difficult choices. "
           "Ticket income can give a museum a degree of independence from such political pressures, allowing it to plan "
           "exhibitions years in advance. Critics of free entry also note, with some justification, that when admission "
           "is free, the cost does not disappear; it is simply transferred to taxpayers, many of whom may never visit "
           "at all."),
         P("Yet the revenue argument is weaker than it first appears. Admission charges at many institutions cover only "
           "a modest share of running costs, and the expense of collecting fees, staffing ticket desks and handling "
           "payments eats into whatever is raised. Moreover, visitors who enter without paying frequently spend money "
           "in cafes and shops, and a busy building may make it easier to attract private donors and sponsors. None of "
           "this proves that free entry pays for itself, but it does suggest that the financial gap is smaller than the "
           "headline price would imply."),
         P("What, then, should be done? I would argue that permanent collections, particularly those acquired with "
           "public money or through donations made in the public interest, should as a rule be free to see. Temporary "
           "exhibitions are a different matter. They are expensive to organise, often involve borrowing works from "
           "abroad, and are visited by people who have actively chosen to attend; a reasonable charge for these seems "
           "entirely defensible. Many institutions already operate along these lines, and the arrangement strikes me "
           "as a sensible compromise rather than a failure of principle."),
         P("Finally, it is worth remembering that the price of a ticket is only one of the costs of a visit. Transport, "
           "time off work and the simple matter of whether a museum is open when people are free all shape who comes. "
           "A museum that is free but closes at five o'clock on weekdays may be less accessible to working people than "
           "one that charges a small fee but stays open late. Debates about admission would be more productive if they "
           "treated price as one part of a wider question: not simply whether a museum costs money, but for whom it is "
           "genuinely open."),
     ],
     [G('provoke', 'qoʻzgʻatmoq, keltirib chiqarmoq'), G('civic institution', 'jamoat muassasasi'),
      G('conserve', 'asrab-avaylamoq, saqlamoq (restavratsiya qilib)'), G('deterrent', 'toʻsiq, qaytaruvchi omil'),
      G('feel entitled to', '… ga haqli deb his qilmoq'), G('make the most of', 'imkoniyatdan toʻliq foydalanmoq'),
      G('sufficient condition', 'yetarli shart'), G('outreach', 'aholi bilan ishlash, keng qatlamga yetib borish'),
      G('with some justification', 'maʼlum darajada asosli ravishda'), G('revenue', 'daromad, tushum'),
      G('modest share', 'kichik ulush'), G('eat into', '(pul, vaqtni) asta-sekin yeb qoʻymoq'),
      G('sponsor', 'homiy'), G('acquire', 'qoʻlga kiritmoq, sotib olmoq'),
      G('defensible', 'oqlab boʻladigan, himoya qilsa boʻladigan'), G('compromise', 'murosa, kelishuv')],
     [GN('c39-it-there', 'Oldindan keluvchi it: it is worth remembering that …',
         'it is worth remembering that the price of a ticket is only one of the costs of a visit'),
      GN('c61-linking-adverbials', 'Bogʻlovchi ravishlar: Moreover, Yet, In other words',
         'Moreover, visitors who enter without paying frequently spend money in cafes and shops')],
     [
         hd(1, H16, 1, 'Xatboshi B: bepul kirish tarafdorlari «the principle of access» ga tayanadi — moliyaviy va '
                       'psixologik toʻsiq olib tashlanadi, hamma xush kelibsiz. «Ochiq eshiklar tamoyili».'),
         hd(2, H16, 0, 'Xatboshi C: narxni olib tashlash «does not automatically change who feels entitled to walk '
                       'through the door» — tashrif buyuruvchilar tarkibi oʻzgarmasligi mumkin.'),
         hd(4, H16, 3, 'Xatboshi E: «the revenue argument is weaker than it first appears» — chipta daromadi '
                       'kichik ulush, yigʻish xarajati bor. «Overstated» = boʻrttirilgan.'),
         hd(6, H16, 5, 'Xatboshi G: transport, ish vaqti, muzeyning ochiq soatlari — narxdan tashqari toʻsiqlar. '
                       '«How museums decide what to display» chalgʻitadi: koʻrgazma tanlovi haqida gap yoʻq.'),
         tf('The writer believes that one admission policy should be applied to all museums.', 'F',
            'Muallif bahsni tanqid qiladi: «the debate is often conducted as if a single answer must apply to every '
            'institution» — yaʼni bitta javob hammaga mos degan yondashuvga qarshi. Bundan tashqari F xatboshida '
            'doimiy va vaqtinchalik koʻrgazmalarni farqlaydi.', 0, ng=True),
         tf('According to the writer, free entry by itself is unlikely to attract people who have previously felt '
            'excluded from museums.', 'T',
            '«free admission may be a necessary condition … but it is unlikely to be a sufficient one»; muzeyni '
            'begona his qilganlar «may continue to stay away». Bu YES.', 2, ng=True),
         tf('The writer considers outreach work to be less important than the price of admission.', 'F',
            'Aksincha: outreach «arguably matter at least as much as the price at the door» — kamida narx '
            'darajasida muhim.', 2, ng=True),
         tf('The writer believes that museums in small towns need free entry more than those in large cities.', 'NG',
            'Muallif kichik shahar va yirik shahar muzeylarini umuman solishtirmaydi — NOT GIVEN.', None),
         tf('The writer thinks it is reasonable to charge visitors for temporary exhibitions.', 'T',
            '«a reasonable charge for these seems entirely defensible» — muallif rozi (YES).', 5, ng=True),
         tf('The writer believes that museum employees should be consulted before admission policies are changed.',
            'NG', 'Xodimlar faqat xarajat sifatida tilga olinadi («staff paid»); ularning fikrini soʻrash haqida '
                  'muallif hech narsa demaydi.', None),
         ch('In paragraph D, what is the writer\'s attitude to the claim that free entry shifts costs to taxpayers?',
            ['The writer dismisses it as unfounded.', 'The writer accepts that there is some truth in it.',
             'The writer regards it as the strongest argument in the debate.',
             'The writer believes it applies only to temporary exhibitions.'], 1,
            '«Critics of free entry also note, with some justification, that …» — «with some justification» = '
            'qisman asosli deb tan oladi. Eng kuchli dalil deb aytmaydi; keyingi xatboshida daromad dalilini zaif deydi.', 3),
         ch('What is the main purpose of paragraph E?',
            ['To show that free museums cost taxpayers nothing.',
             'To suggest that the financial loss from free entry is smaller than it seems.',
             'To argue that museums should depend entirely on private donors.',
             'To explain why cafes and shops are important to visitors.'], 1,
            '«the financial gap is smaller than the headline price would imply». A notoʻgʻri: «None of this proves '
            'that free entry pays for itself». Kafe va homiylar faqat dalil sifatida keltirilgan.', 4),
         gap('According to the writer, free admission removes a financial barrier and also a ___ one.',
             ['psychological'], '«removes not only a financial barrier but also a psychological one».', 1, 2),
         gap('The writer describes charging for temporary exhibitions while keeping permanent collections free as '
             'a sensible ___.', ['compromise'],
             '«the arrangement strikes me as a sensible compromise rather than a failure of principle».', 5, 2),
     ])


# ---------------------------------------------------------------- 17
text(B, 'c1-17-automation', 'Avtomatlashtirish', 'Will Machines Take Our Jobs?', 'C1', 'exam',
     L('Texnologiya va iqtisod', 'Technology and economy'),
     intro('avtomatlashtirish mehnatni yoʻq qiladimi yoki oʻzgartiradimi — tarixiy oʻxshashliklar va oʻtish davrining narxi.',
           'Muallifning umumiy pozitsiyasini (ehtiyotkor optimizm) aniqlang — test savollari koʻpincha shunga tayanadi; '
           'xulosa (summary) boʻshliqlari uchun soʻzni matndan aynan koʻchiring.'),
     [
         P("Every few decades, a new wave of technology prompts confident predictions that human work is about to "
           "become obsolete. Machines capable of driving vehicles, diagnosing illnesses and drafting documents have "
           "revived these fears with unusual intensity. It would be foolish to dismiss such concerns, but it would be "
           "equally unwise to accept them uncritically. The more useful question is not whether automation will change "
           "work, which it plainly will, but how that change is likely to unfold and who will bear its costs."),
         P("History offers some reassurance. When mechanised looms spread through the textile industry in the early "
           "nineteenth century, skilled textile workers protested, and some destroyed machinery, fearing for their livelihoods. "
           "Their fears were justified in the short term: many lost their trades. Over the longer term, however, "
           "industrialised economies created far more jobs than they destroyed, many of them in occupations that no one "
           "in 1810 could have imagined. Similarly, the steady decline of agricultural employment over the twentieth "
           "century did not produce permanent mass unemployment; workers moved, often reluctantly, into factories, "
           "offices and services."),
         P("Part of the reason is that automation rarely replaces whole jobs; it replaces tasks. A job is a bundle of "
           "activities, and when machines take over some of them, the remaining ones often become more valuable. Cash "
           "machines, for instance, did not eliminate the bank clerk overnight; instead, the role gradually shifted "
           "towards advising customers and selling services. Cheaper production also tends to lower prices, leaving "
           "consumers with more money to spend elsewhere, which in turn generates demand for new kinds of work. Spreadsheet "
           "software, similarly, changed the daily work of accountants without making the profession disappear."),
         P("Nevertheless, I am wary of treating these historical parallels as a guarantee. Earlier machines mainly "
           "substituted for physical strength and routine manual effort, whereas today's systems increasingly perform "
           "cognitive tasks, such as summarising reports or recognising patterns in data, that were once thought to "
           "require human judgement. It is possible that the pace of change will also be faster than in the past, "
           "leaving less time for workers and institutions to adjust. Optimism grounded in history is reasonable, but "
           "it should be held with a degree of humility."),
         P("Even if the long-term outcome proves broadly positive, the transition itself deserves far more attention "
           "than it typically receives. The familiar reassurance that everything will improve in the long run conceals "
           "a great deal of hardship. A fifty-year-old machine operator whose skills have suddenly become redundant "
           "cannot easily retrain as a software engineer, and the new jobs created by technology often appear in "
           "different cities, or even different countries, from the ones that disappear. Whole communities can be "
           "left behind, and the resentment this produces may have consequences that extend well beyond economics."),
         P("It follows that the central challenge is political rather than technological. Societies that wish to "
           "benefit from automation without abandoning those it displaces will need to invest seriously in adult "
           "education, make it easier for people to move between occupations, and provide adequate support during "
           "periods of unemployment. These measures are expensive and unglamorous, and they produce results slowly, "
           "which is precisely why they tend to be neglected. Yet without them, public hostility may grow strong enough "
           "to slow the adoption of genuinely useful technologies. More radical proposals, such as a guaranteed basic income, "
           "continue to divide opinion, but even the more modest measures described here would be a considerable "
           "improvement on simply hoping that markets will adjust by themselves."),
         P("On balance, then, I remain cautiously optimistic. The evidence of the past two centuries suggests that work "
           "is far more likely to be transformed than destroyed, and many of the tasks that machines absorb are ones "
           "that few people would choose to do. But the benefits of automation will not distribute themselves fairly "
           "by default. Whether this wave of change is remembered as a period of progress or of upheaval will depend "
           "less on the capabilities of the machines than on the choices we make about the people they affect."),
     ],
     [G('obsolete', 'eskirgan, keraksiz boʻlib qolgan'), G('prompt', 'sabab boʻlmoq, undamoq'),
      G('uncritically', 'tanqidiy fikrlamasdan'), G('unfold', 'kechmoq, asta-sekin yuz bermoq'),
      G('livelihood', 'tirikchilik manbai'), G('reluctantly', 'istar-istamas'), G('bundle', 'toʻplam, majmua'),
      G('eliminate', 'yoʻq qilmoq, bartaraf etmoq'), G('substitute for', '… oʻrnini bosmoq'),
      G('cognitive', 'aqliy, kognitiv'), G('humility', 'kamtarlik, oʻz bilimining chegarasini tan olish'),
      G('redundant', 'keraksiz (ish oʻrni qisqargan)'), G('resentment', 'norozilik, alam'),
      G('displace', 'siqib chiqarmoq, oʻrnidan mahrum qilmoq'), G('hostility', 'dushmanlik, keskin qarshilik'),
      G('by default', 'oʻz-oʻzidan, hech narsa qilinmasa'), G('upheaval', 'keskin toʻntarilish, gʻalayon')],
     [GN('c12-modal-perfect', 'Modal + have + V3: could have imagined',
         'many of them in occupations that no one in 1810 could have imagined'),
      GN('c46-contrast-concession', 'Toʻsiqsizlik: Even if …',
         'Even if the long-term outcome proves broadly positive, the transition itself deserves far more attention')],
     [
         tf('The writer believes that fears about automation can safely be ignored.', 'F',
            '«It would be foolish to dismiss such concerns» — muallif bu xavotirlarni eʼtiborsiz qoldirmaslik kerak '
            'deydi (NO).', 0, ng=True),
         tf('The writer thinks that the textile workers who protested against new machinery were wrong to fear for their jobs.',
            'F', '«Their fears were justified in the short term: many lost their trades» — qisqa muddatda ular haq edi.',
            1, ng=True),
         tf('The writer claims that automation usually takes over particular activities rather than entire occupations.',
            'T', '«automation rarely replaces whole jobs; it replaces tasks» — whole jobs = entire occupations, '
                 'tasks = particular activities.', 2, ng=True),
         tf('The writer believes that companies which replace workers with machines should pay higher taxes.', 'NG',
            'Muallif kattalar taʼlimi, kasb almashtirish va ishsizlik davridagi yordamni taklif qiladi, lekin '
            'kompaniyalarga soliq haqida hech narsa demaydi.', None),
         tf('According to the writer, new jobs created by technology are often located far from the jobs that are lost.',
            'T', '«the new jobs … often appear in different cities, or even different countries, from the ones that '
                 'disappear».', 4, ng=True),
         tf('The writer believes that older workers should be given priority in retraining programmes.', 'NG',
            '50 yoshli operator misol sifatida keltiriladi — unga qayta oʻqish qiyin deyiladi, lekin keksa '
            'ishchilarga ustuvorlik berish kerakmi — muallif fikr bildirmaydi.', None),
         ch('What is the writer\'s view of the historical parallels described in paragraphs B and C?',
            ['They prove that automation will create more jobs than it destroys.',
             'They are useful evidence but cannot be relied on completely.',
             'They are irrelevant because modern machines are entirely different.',
             'They show that workers have always resisted change successfully.'], 1,
            '«I am wary of treating these historical parallels as a guarantee» va «Optimism grounded in history is '
            'reasonable, but it should be held with a degree of humility» — foydali, lekin kafolat emas.', 3),
         ch('Why does the writer mention cash machines?',
            ['To show that banks were the first industry to be automated.',
             'To illustrate how a job can change when some of its tasks are automated.',
             'To argue that bank clerks lost their jobs overnight.',
             'To prove that automation always lowers prices.'], 1,
            'Bankomatlar «did not eliminate the bank clerk overnight; instead, the role gradually shifted towards '
            'advising customers» — «tasks, not jobs» gʻoyasining misoli. C javob matnga zid.', 2),
         ch('According to the writer, why are measures such as adult education often neglected?',
            ['They are unpopular with workers.', 'They are costly and take a long time to show results.',
             'They slow down the adoption of new technology.', 'They are the responsibility of private companies.'], 1,
            '«These measures are expensive and unglamorous, and they produce results slowly, which is precisely why '
            'they tend to be neglected».', 5),
         ch('Which of the following best summarises the writer\'s overall position?',
            ['Automation will lead to permanent mass unemployment.',
             'Automation poses no real threat, so no action is needed.',
             'Work will probably be transformed rather than destroyed, but the costs of transition must be addressed.',
             'Technological progress should be slowed down to protect existing jobs.'], 2,
            '«I remain cautiously optimistic … work is far more likely to be transformed than destroyed», lekin '
            '«the benefits … will not distribute themselves fairly by default».', 6),
         gap('Summary: The writer accepts that optimism based on history is reasonable but says it should be held with '
             'a degree of ___.', ['humility'], '«it should be held with a degree of humility».', 3, 2),
         gap('Summary: Because new jobs may appear elsewhere, whole ___ can be left behind.', ['communities'],
             '«Whole communities can be left behind».', 4, 2),
         gap('Summary: For the writer, the main challenge of automation is ___ rather than technological.',
             ['political'], '«the central challenge is political rather than technological».', 5, 2),
     ])


# ---------------------------------------------------------------- 18
H18 = ['Language as a source of belonging', 'The real advantages of global languages',
       'A false choice between languages', 'Why being spoken at home is not enough',
       'Supporting one language without rejecting others', 'Borrowing as a sign of life rather than decline',
       'Why young people abandon their parents\' language', 'The case for a single official language']

text(B, 'c1-18-language-identity', 'Til va milliy oʻzlik', 'Language and Identity', 'C1', 'exam',
     L('Til va jamiyat', 'Language and society'),
     intro('ona tili milliy oʻzlik sifatida va global tillarning amaliy foydasi, koʻp tillilik haqida.',
           'Muallif ikki tomonni ham hurmat bilan koʻrib chiqadi — «both positions … rest on a mistaken assumption» '
           'kabi jumlalar uning haqiqiy fikrini koʻrsatadi.'),
     [
         P("Language is rarely just a tool for exchanging information. The words a child first hears, the songs sung at "
           "family celebrations and the proverbs repeated by grandparents carry a sense of belonging that is difficult "
           "to describe and harder still to replace. It is hardly surprising, then, that debates about which languages "
           "should be taught, used in government or required for employment so often arouse strong feelings. They touch "
           "not only on practical arrangements but on people's sense of who they are."),
         P("At the same time, it would be naive to ignore the practical value of languages spoken across borders. A "
           "small number of languages dominate international science, business and online communication, and "
           "proficiency in one of them can open doors to education abroad, better-paid work and a vast body of "
           "knowledge. A shared language also allows people from very different backgrounds to cooperate, trade and learn "
           "from one another. Parents who encourage their children to study such languages are not betraying their "
           "heritage; they are responding sensibly to the world as it is, and to criticise them for doing so would be "
           "both unfair and unrealistic."),
         P("The difficulty arises when these two considerations are presented as a choice. Some voices warn that every "
           "hour devoted to a global language weakens the national one, while others treat the mother tongue as a "
           "sentimental attachment with little relevance to modern life. Both positions, in my view, rest on a mistaken "
           "assumption: that a person has room for only one language that truly matters. A large part of the world's "
           "population has always lived with several languages, and there is no convincing reason to believe that the "
           "human mind is overwhelmed by more than one. On the contrary, researchers have often suggested that learning "
           "several languages may bring cognitive and social benefits, although the precise nature of these advantages "
           "continues to be debated."),
         P("Uzbekistan offers an instructive example. Many Uzbeks, particularly in the cities, move comfortably between Uzbek and Russian, and "
           "growing numbers of young people are adding English, alongside other languages, to their repertoire. This is "
           "a considerable asset. Yet a language does not remain strong merely because it is spoken at home. It needs to "
           "be used in science, technology, law and the media, to acquire new vocabulary for new ideas, and to be the "
           "language in which people choose to write when they have something important to say. If ambitious young "
           "people come to associate their mother tongue only with the kitchen and the village, and a foreign language "
           "with success, the national language may gradually lose prestige even while remaining widely spoken."),
         P("This is why investment in the national language is not an act of nostalgia but a practical necessity. Good "
           "dictionaries, up-to-date textbooks, translated scientific works and high-quality writing for children all "
           "help to ensure that a language can express the full range of modern experience. Such efforts do not require "
           "hostility to other languages. A country can promote its own language with confidence while also encouraging "
           "its citizens to master English, Russian or any other language that serves them well. Equally important is the "
           "example set by writers, teachers and public figures who use the national language with skill and evident pride."),
         P("Nor should identity be understood as fixed. Languages have always borrowed from one another, and the "
           "presence of foreign words is not in itself a sign of decline; Uzbek, like English, has absorbed vocabulary "
           "from many sources over the centuries and remains unmistakably itself. What matters is less the purity of a "
           "language than its vitality: whether people continue to use it creatively, argue in it, joke in it and pass "
           "it on to their children."),
         P("The most productive approach, then, is to regard languages as complementary rather than competing. A strong "
           "first language provides a foundation of identity and, arguably, a firmer base for learning others, while "
           "additional languages extend a person's reach into the wider world. The aim should not be to choose between "
           "roots and wings, but to ensure that young people are offered both. Such an approach asks more of schools and families, but it "
           "respects both the practical and the emotional dimensions of language."),
     ],
     [G('arouse', 'uygʻotmoq, qoʻzgʻatmoq (his-tuygʻu)'), G('naive', 'soddadil, yuzaki'),
      G('proficiency', 'yuqori malaka, erkin bilish'), G('betray', 'xiyonat qilmoq'),
      G('heritage', 'meros'), G('devote', 'bagʻishlamoq, ajratmoq'),
      G('sentimental attachment', 'hissiy bogʻliqlik'), G('overwhelm', 'haddan tashqari yuklamoq, bosib ketmoq'),
      G('instructive', 'ibratli, saboq beruvchi'), G('repertoire', 'toʻplam, egallangan koʻnikmalar doirasi'),
      G('asset', 'boylik, afzallik'), G('prestige', 'nufuz, obroʻ'),
      G('nostalgia', 'oʻtmishni qoʻmsash, nostalgiya'), G('master', 'puxta egallamoq'),
      G('absorb', 'oʻziga singdirmoq'), G('vitality', 'hayotiylik, jonlilik'),
      G('complementary', 'bir-birini toʻldiruvchi')],
     [GN('c58-inversion', 'Inversiya: Nor should identity be understood …',
         'Nor should identity be understood as fixed'),
      GN('c57-cleft-sentences', 'Pseudo-cleft: What matters is …',
         'What matters is less the purity of a language than its vitality')],
     [
         hd(2, H18, 2, 'Xatboshi C: ikki qarash ham «rest on a mistaken assumption: that a person has room for only one '
                       'language» — tanlov yolgʻon qoʻyilgan.'),
         hd(3, H18, 3, 'Xatboshi D: «a language does not remain strong merely because it is spoken at home» — fan, '
                       'huquq, mediada ham ishlatilishi kerak.'),
         hd(4, H18, 4, 'Xatboshi E: milliy tilga sarmoya + «Such efforts do not require hostility to other languages».'),
         hd(5, H18, 5, 'Xatboshi F: «the presence of foreign words is not in itself a sign of decline» — muhimi '
                       'hayotiylik (vitality). «Why young people abandon …» chalgʻitadi: bu D dagi ehtimol, F emas.'),
         tf('The writer criticises parents who encourage their children to learn global languages.', 'F',
            '«Parents … are not betraying their heritage; they are responding sensibly» va «to criticise them for doing so would '
            'be both unfair and unrealistic» — muallif ularni tanqid qilmaydi (NO).', 1, ng=True),
         tf('The writer believes that learning more than one language overloads the human mind.', 'F',
            '«there is no convincing reason to believe that the human mind is overwhelmed by more than one» — aksi.',
            2, ng=True),
         tf('The writer suggests that a language which is widely spoken may still lose status.', 'T',
            '«the national language may gradually lose prestige even while remaining widely spoken» — prestige = status.',
            3, ng=True),
         tf('The writer believes that English should be compulsory at all universities.', 'NG',
            'Muallif ingliz tilini oʻrganishni ragʻbatlantirish mumkin deydi, lekin uni universitetlarda majburiy '
            'qilish haqida fikr bildirmaydi.', None),
         tf('The writer believes that schools should teach every subject in two languages.', 'NG',
            'Muallif faqat «Such an approach asks more of schools and families» deydi; har bir fanni ikki tilda oʻqitish haqida hech narsa aytilmagan.', 6),
         ch('What is the writer\'s attitude to the research on the benefits of learning several languages?',
            ['The writer rejects it as unconvincing.', 'The writer regards its conclusions as fully proven.',
             'The writer accepts it as suggestive while noting that details are still debated.',
             'The writer believes it applies only to children.'], 2,
            '«researchers have often suggested that … may bring … benefits, although the precise nature of these '
            'advantages continues to be debated» — ehtiyotkor qabul qilish.', 2),
         ch('In paragraph E, why does the writer mention dictionaries, textbooks and translated scientific works?',
            ['To show that the national language is already fully developed.',
             'To give examples of practical steps that keep a language able to express modern life.',
             'To argue that foreign books should not be translated.',
             'To criticise the quality of existing teaching materials.'], 1,
            'Ular «help to ensure that a language can express the full range of modern experience» — amaliy chora-tadbirlar.',
            4),
         ch('What does the writer mean by choosing between «roots and wings»?',
            ['Choosing between living in the village and moving to the city.',
             'Choosing between a secure identity and access to the wider world.',
             'Choosing between Russian and English.',
             'Choosing between traditional and modern teaching methods.'], 1,
            'Oldingi jumla: birinchi til «a foundation of identity» (roots), qoʻshimcha tillar «extend a person\'s reach '
            'into the wider world» (wings). Muallif ikkalasi ham kerak deydi.', 6),
         gap('According to the writer, what matters is less the purity of a language than its ___.', ['vitality'],
             '«What matters is less the purity of a language than its vitality».', 5, 2),
         gap('The writer argues that investment in the national language is a practical necessity, not an act of ___.',
             ['nostalgia'], '«not an act of nostalgia but a practical necessity».', 4, 2),
     ])


# ---------------------------------------------------------------- 19
text(B, 'c1-19-sport-money', 'Sport va pul', 'Sport and Money', 'C1', 'exam',
     L('Sport va jamiyat', 'Sport and society'),
     intro('sportning tijoratlashuvi, transfer summalari, ommaviy sportni moliyalashtirish va muxlislarning «mijoz»ga aylanishi haqida.',
           'Muallif uchta muammoni ketma-ket sanaydi (The first … The second … A third …) — bu tuzilma savollarni '
           'tez topishga yordam beradi.'),
     [
         P("Professional sport has never been entirely separate from money. Even in eras that are now remembered with "
           "affection as more innocent, clubs charged admission, owners sought profit and talented players were tempted "
           "by better offers elsewhere. What has changed in recent decades is the scale. Broadcasting deals, global "
           "sponsorship and the arrival of extremely wealthy owners have transformed the leading clubs in the most "
           "popular sports into international businesses, and the sum paid to transfer a single player can now exceed "
           "the annual budget of a small town. Few would deny that these changes have made elite sport more spectacular; "
           "the harder question is what they have done to everything around it."),
         P("Defenders of this transformation make several reasonable points. Commercial income has paid for modern "
           "stadiums, better medical care for athletes and a standard of play that would have been unthinkable a few "
           "generations ago. Elite athletes, whose careers are short and physically punishing, are arguably entitled to "
           "a share of the wealth their performances generate. And the global audience for top competitions suggests "
           "that, whatever purists may say, very large numbers of people enjoy the product they are offered."),
         P("The difficulties lie elsewhere. The first is concentration. When broadcasting revenue rewards success, the "
           "most successful clubs grow richer, attract the best players and become more successful still. Competitions "
           "in which the same handful of teams win year after year risk losing the uncertainty of outcome that makes "
           "sport compelling in the first place. Some leagues have attempted to counter this through limits on salaries "
           "or by sharing income more evenly, and although such measures are imperfect, they at least acknowledge that "
           "a sporting contest is not the same as an ordinary market."),
         P("The second concern is the neglect of the grassroots. Almost every professional athlete began by playing in a "
           "local park, school or amateur club, often coached by volunteers. These are the foundations on which the "
           "entire structure rests, yet they frequently receive a tiny fraction of the money that flows through the "
           "professional game. Pitches fall into disrepair, youth teams struggle to pay for equipment, and children from "
           "poorer families may be priced out of sports that were once accessible to almost everyone. It seems to me "
           "both unwise and unjust that so little of the wealth at the top finds its way back to the base."),
         P("A third, subtler change concerns the relationship between clubs and their supporters. Fans were once "
           "regarded, and regarded themselves, as members of a community whose loyalty gave a club its identity. "
           "Increasingly, they are treated as customers, to be offered premium seating, expensive replica shirts and "
           "subscription packages. The distinction matters. A customer who is dissatisfied can simply take their "
           "business elsewhere; a lifelong supporter cannot, and it is precisely this loyalty that makes them "
           "vulnerable to rising prices. When long-standing fans can no longer afford to attend matches, something of "
           "value is lost that no balance sheet records."),
         P("None of this means that money should be driven out of sport, which would be neither possible nor desirable. "
           "The question is how it is distributed and on what terms. A modest levy on transfer fees or broadcasting "
           "income, directed to community facilities and youth programmes, would cost the wealthiest clubs relatively "
           "little while making a considerable difference at local level. Giving supporters a formal voice in the "
           "running of their clubs, as some leagues and clubs already do in various forms, could help to ensure that commercial decisions "
           "take account of those with the deepest attachment to the game."),
         P("Sport occupies an unusual position: it is at once an industry, a form of entertainment and, for many "
           "people, a part of who they are. Treating it purely as a business misunderstands why people care about it so "
           "deeply. The challenge is to keep the benefits that commercial success has brought while remembering that "
           "the game's value has never been measured only in money. Getting that balance right will require clubs, governing "
           "bodies and governments to act together rather than leaving the matter to the market alone."),
     ],
     [G('remember with affection', 'iliqlik bilan eslamoq'), G('tempt', 'vasvasaga solmoq, oʻziga tortmoq'),
      G('broadcasting deal', 'teleradio translyatsiya shartnomasi'), G('punishing', 'juda ogʻir, toliqtiruvchi'),
      G('purist', 'anʼanaparast, «sof» qoidalar tarafdori'), G('concentration', 'toʻplanib qolish, jamlanish'),
      G('compelling', 'qiziqtiruvchi, oʻziga tortuvchi'), G('counter', 'qarshi chora koʻrmoq'),
      G('grassroots', 'quyi boʻgʻin, ommaviy (havaskor) daraja'), G('fall into disrepair', 'yaroqsiz holga kelmoq'),
      G('priced out', 'narx tufayli chetda qolgan'), G('subtle', 'nozik, sezilmas'),
      G('replica shirt', 'jamoa formasining nusxasi'), G('vulnerable', 'zaif, himoyasiz'),
      G('levy', 'yigʻim, majburiy toʻlov'), G('take account of', 'hisobga olmoq')],
     [GN('c43-comparison-advanced', 'Kuchaytirilgan qiyos: richer … more successful still',
         'the most successful clubs grow richer, attract the best players and become more successful still'),
      GN('c34-participle-clauses', 'Sifatdosh oborot: directed to …',
         'A modest levy on transfer fees or broadcasting income, directed to community facilities and youth programmes, '
         'would cost the wealthiest clubs relatively little')],
     [
         tf('The writer believes that sport used to be completely free of financial motives.', 'F',
            '«Professional sport has never been entirely separate from money» — eski davrlarda ham chipta, foyda '
            'boʻlgan. Oʻzgargan narsa — miqyos.', 0, ng=True),
         tf('The writer accepts that top athletes may deserve a share of the money they help to create.', 'T',
            '«Elite athletes … are arguably entitled to a share of the wealth their performances generate» — YES.', 1,
            ng=True),
         tf('The writer believes that limits on salaries have completely solved the problem of concentration.', 'F',
            '«although such measures are imperfect» — muammoni toʻliq hal qilmagan.', 2, ng=True),
         tf('The writer thinks that volunteer coaches should be paid by professional clubs.', 'NG',
            'Koʻngilli murabbiylar tilga olinadi («often coached by volunteers»), lekin ularga haq toʻlash kerakmi — '
            'muallif fikr bildirmaydi.', 3),
         tf('The writer believes that ticket prices for international matches have risen faster than those for '
            'league matches.', 'NG',
            'Narx oshishi haqida umumiy gap bor, ammo xalqaro va liga oʻyinlari narxlari solishtirilmaydi.', None),
         tf('According to the writer, loyal supporters are more exposed to price increases than ordinary customers.',
            'T', 'Mijoz boshqa joyga keta oladi, sodiq muxlis esa yoʻq — «it is precisely this loyalty that makes them '
                 'vulnerable to rising prices».', 4, ng=True),
         ch('How does the writer regard the arguments of those who defend the commercialisation of sport?',
            ['The writer considers all of them misleading.', 'The writer accepts that some of them are reasonable.',
             'The writer believes they are supported only by purists.',
             'The writer thinks they matter more than the problems the essay raises.'], 1,
            '«Defenders of this transformation make several reasonable points», keyin «The difficulties lie elsewhere» '
            '— dalillarini tan oladi, lekin muammo boshqa joyda deydi.', 1),
         ch('Why does the writer refer to «the uncertainty of outcome»?',
            ['To explain what makes sport attractive and what concentration threatens.',
             'To argue that results in sport are random.', 'To praise leagues that share income evenly.',
             'To show that fans prefer the same teams to win.'], 0,
            'Bir xil jamoalar yutaversa, raqobat «risk losing the uncertainty of outcome that makes sport compelling» '
            '— sport aynan shu noaniqlik tufayli qiziqarli.', 2),
         ch('What does the writer propose in paragraph F?',
            ['Banning wealthy owners from buying clubs.', 'Removing money from sport altogether.',
             'A small charge on transfer fees or broadcasting income to fund local sport.',
             'Lower salaries for elite athletes.'], 2,
            '«A modest levy on transfer fees or broadcasting income, directed to community facilities and youth '
            'programmes». B javob rad etilgan: «neither possible nor desirable».', 5),
         ch('Which statement best describes the writer\'s overall approach?',
            ['The writer argues that commercialisation has destroyed sport.',
             'The writer presents commercial success as entirely positive.',
             'The writer recognises the benefits of money but calls for fairer distribution.',
             'The writer focuses mainly on the problems of individual athletes.'], 2,
            '«The question is how it is distributed and on what terms» va «keep the benefits … while remembering …» — '
            'muvozanatli pozitsiya.', 6),
         gap('Summary: Because of rising costs, children from poorer families may be ___ out of sports that were once '
             'open to almost everyone.', ['priced'], '«children from poorer families may be priced out of sports».', 3, 2),
         gap('Summary: Fans, once seen as members of a community, are increasingly treated as ___.', ['customers'],
             '«Increasingly, they are treated as customers».', 4, 2),
         gap('Summary: The writer suggests that supporters should be given a formal ___ in the running of their clubs.',
             ['voice'], '«Giving supporters a formal voice in the running of their clubs».', 5, 2),
     ])


# ---------------------------------------------------------------- 20
H20 = ['How a single score is put together', 'Research counted, teaching barely captured',
       'Fame that feeds itself', 'When the table starts to steer the institution', 'Some genuine benefits',
       'Reading the tables wisely', 'Why governments fund universities', 'The rise of online degrees']

text(B, 'c1-20-university-rankings', 'Universitet reytinglari', 'University Rankings', 'C1', 'exam',
     L('Taʼlim', 'Education'),
     intro('xalqaro universitet reytinglari nimani oʻlchaydi, nimani eʼtibordan chetda qoldiradi va universitetlar hamda '
           'talabalar xulq-atvoriga qanday taʼsir qiladi.',
           'Muallif skeptik, lekin adolatli: «It would be unfair, however, to dismiss rankings altogether» kabi '
           'burilish nuqtalariga eʼtibor bering.'),
     [
         P("Each year, the publication of international university rankings is greeted with a mixture of celebration "
           "and anxiety. Institutions that climb a few places announce the news on their websites; those that fall may "
           "face awkward questions from governments and governing boards. For prospective students and their families, "
           "rankings offer something genuinely attractive: an apparently simple answer to the bewildering question of "
           "where to study. It is worth asking, however, what these tables actually measure, and what happens when so "
           "much weight is placed on them."),
         P("Most prominent rankings combine a number of indicators into a single score. These typically include research "
           "output and the frequency with which that research is cited, the proportion of international staff and "
           "students, the ratio of staff to students and, in some cases, surveys of academic reputation. Each of these "
           "is a legitimate thing to know about a university. The difficulty lies in the decisions, largely invisible to "
           "readers, about which indicators to include and how heavily to weight them. A modest change to the formula "
           "can move an institution many places without anything about the institution itself having changed."),
         P("What the indicators measure most reliably is research, and in particular research published in widely read "
           "journals, which are disproportionately in English. Teaching quality, by contrast, is notoriously difficult to "
           "quantify and is captured, if at all, only through rough proxies. Yet for most undergraduates it is the "
           "quality of teaching, the support they receive and the skills they leave with that matter most. A university "
           "may produce outstanding research while offering a mediocre experience to its first-year students, and the "
           "reverse is equally possible. A student who chooses an institution on the strength of its research "
           "position alone may therefore be disappointed by what they find in the lecture hall."),
         P("Reputation surveys raise a further problem. Academics asked to name the best institutions in their field "
           "tend to name those that are already famous, and those institutions remain famous partly because they keep "
           "being named. Rankings built partly on reputation may therefore reinforce existing hierarchies rather than "
           "reveal genuine change, making it harder for younger universities to gain recognition however good their "
           "work may be. Reputation, in other words, can lag years behind reality."),
         P("Perhaps the most troubling effect of rankings is the way they shape behaviour. Once a position in the table "
           "becomes a target, universities have an incentive to pursue whatever the formula rewards. Resources may be "
           "shifted towards activities that improve scores, such as recruiting highly cited researchers, while less "
           "visible work, such as teaching, community engagement or research on local problems, receives less "
           "attention. This is a familiar pattern: when a measure becomes a target, it tends to lose its value as a "
           "measure. Students, too, may choose an institution because of its overall position rather than the strength "
           "of the particular course they intend to take."),
         P("It would be unfair, however, to dismiss rankings altogether. They have encouraged some universities to "
           "collect and publish information that was previously hard to obtain, and they have drawn attention to "
           "institutions outside the traditional centres of academic prestige that have improved rapidly. For a student "
           "comparing universities in an unfamiliar country, a ranking may be a reasonable starting point, provided that "
           "it is not also the finishing point."),
         P("The sensible response, then, is not to abolish rankings but to read them critically. Students would be better "
           "served by looking at information for individual subjects, talking to current students and examining what a "
           "course actually involves. Governments and university leaders, for their part, should resist the temptation "
           "to treat a position in a league table as a goal in itself. A ranking can describe certain features of a "
           "university with reasonable accuracy; it cannot tell anyone whether that university is the right place for "
           "them. Universities, meanwhile, could do more to publish clear and comparable information about teaching, so "
           "that applicants are not left to rely on a single number."),
     ],
     [G('bewildering', 'chalkashtiruvchi, boshni qotiruvchi'), G('prospective student', 'boʻlajak talaba, abituriyent'),
      G('prominent', 'taniqli, koʻzga koʻringan'), G('indicator', 'koʻrsatkich'),
      G('legitimate', 'qonuniy, asosli'), G('weight', '(koʻrsatkichga) vazn/ahamiyat bermoq'),
      G('disproportionately', 'nomutanosib ravishda, haddan koʻp'), G('notoriously', 'hammaga maʼlumki (salbiy maʼnoda)'),
      G('quantify', 'miqdoriy oʻlchamoq'), G('proxy', 'bilvosita koʻrsatkich, oʻrinbosar oʻlchov'),
      G('mediocre', 'oʻrtacha, past sifatli'), G('reinforce', 'mustahkamlamoq, kuchaytirmoq'),
      G('hierarchy', 'iyerarxiya, darajalar tizimi'), G('incentive', 'ragʻbat, undovchi omil'),
      G('abolish', 'bekor qilmoq'), G('resist the temptation', 'vasvasaga berilmaslik')],
     [GN('c33-relative-advanced', 'Predlogli nisbiy gap: with which …',
         'the frequency with which that research is cited'),
      GN('c51-supposing-provided', 'Shart: provided that …',
         'a ranking may be a reasonable starting point, provided that it is not also the finishing point')],
     [
         hd(2, H20, 1, 'Xatboshi C: indikatorlar eng ishonchli oʻlchaydigan narsa — tadqiqot; oʻqitish sifati esa '
                       '«notoriously difficult to quantify».'),
         hd(3, H20, 2, 'Xatboshi D: mashhur universitetlar nomlanadi va nomlangani uchun mashhur boʻlib qoladi — '
                       '«Fame that feeds itself».'),
         hd(4, H20, 3, 'Xatboshi E: reyting maqsadga aylansa, universitetlar formula mukofotlaydigan narsaga intiladi — '
                       'jadval muassasani «boshqara» boshlaydi.'),
         hd(5, H20, 4, 'Xatboshi F: «It would be unfair … to dismiss rankings altogether» — maʼlumot ochiqligi, '
                       'tez rivojlangan universitetlarga eʼtibor. «Reading the tables wisely» G xatboshiga mos.'),
         tf('The writer believes that the information used in rankings is worthless in itself.', 'F',
            '«Each of these is a legitimate thing to know about a university» — muammo koʻrsatkichlarda emas, ularni '
            'tanlash va vazn berishda.', 1, ng=True),
         tf('According to the writer, a university can rise or fall in a ranking even if nothing about it has changed.',
            'T', '«A modest change to the formula can move an institution many places without anything about the '
                 'institution itself having changed».', 1, ng=True),
         tf('The writer believes that reputation surveys help newer universities to gain recognition.', 'F',
            'Aksincha: «making it harder for younger universities to gain recognition».', 3, ng=True),
         tf('The writer thinks that rankings should be published less often.', 'NG',
            'Reytinglar har yili chiqishi aytiladi, lekin ularni kamroq chiqarish kerakmi — muallif fikr bildirmaydi. '
            'U «not to abolish rankings but to read them critically» deydi, xolos.', None),
         tf('The writer believes that universities in Asia have gained more from rankings than those in Europe.', 'NG',
            'Muallif «institutions outside the traditional centres» haqida umumiy gapiradi; Osiyo va Yevropa '
            'solishtirilmaydi.', 5),
         ch('According to paragraph B, what is the main weakness of rankings?',
            ['They ignore research output.', 'They rely on false information supplied by universities.',
             'The choices about which indicators to use and how to weight them are largely hidden.',
             'They include too few international students.'], 2,
            '«The difficulty lies in the decisions, largely invisible to readers, about which indicators to include and '
            'how heavily to weight them».', 1),
         ch('How, according to the writer, should a student use a ranking?',
            ['As the only basis for choosing a university.', 'As a reasonable starting point but not a final answer.',
             'Not at all, because rankings are misleading.', 'Only when choosing a university at home.'], 1,
            '«a reasonable starting point, provided that it is not also the finishing point».', 5),
         ch('Which best describes the writer\'s overall attitude to university rankings?',
            ['Enthusiastic support.', 'Complete rejection.', 'Sceptical but willing to acknowledge their value.',
             'Indifferent.'], 2,
            'Muallif koʻp kamchiliklarni koʻrsatadi, lekin «It would be unfair … to dismiss rankings altogether» va '
            '«not to abolish rankings but to read them critically» deydi.', 6),
         gap('Because teaching quality is hard to quantify, it is captured only through rough ___.', ['proxies'],
             '«is captured, if at all, only through rough proxies».', 2, 2),
         gap('Once a position in the table becomes a ___, universities have an incentive to pursue whatever the formula '
             'rewards.', ['target'], '«Once a position in the table becomes a target, universities have an incentive».', 4, 2),
     ])
