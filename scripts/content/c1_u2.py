"""C1 · 2-boʻlim: Iqtisod va jamiyat (IELTS Academic darajasidagi oʻqish matnlari)"""
from lib import *

B = 'c1'

# ---------------------------------------------------------------- 1. Remittances
text(B, 'c1-06-remittances', 'Pul oʻtkazmalari va iqtisod', 'Remittances and the Economy', 'C1', 'exam',
     L('Iqtisodiyot', 'Economics'),
     'Akademik maqola: migrant ishchilar vataniga yuboradigan pul oʻtkazmalari — ularning oilalar va milliy iqtisod '
     'uchun foydasi hamda xavflari. Asosiy topshiriq: True / False / Not Given (savollarning koʻpchiligi), qoʻshimcha '
     'test va boʻshliq toʻldirish. Esda tuting: matn aksini aytsa — FALSE, umuman aytmasa yoki xulosa chiqarib boʻlmasa — '
     'NOT GIVEN. Oʻz bilimingizga emas, faqat matnga tayaning. Taxminan 20 daqiqa ajrating: har bir tasdiqdagi kalit '
     'soʻzning sinonimini matndan qidiring, TFNG tasdiqlari matn tartibida joylashgan.',
     [
         P("For millions of families across the developing world, the most important economic event of the month is not a "
           "change in interest rates or a government announcement but the arrival of money from a relative working abroad. "
           "These transfers, known as remittances, are typically modest sums sent by migrant workers to parents, spouses and "
           "children who remain at home. Taken together, however, they amount to an enormous flow of capital. International "
           "organisations have estimated that remittances to low- and middle-income countries now exceed official development "
           "aid by a wide margin, and in a number of smaller economies they are equivalent to a significant share of national output."),
         P("Central Asia offers a striking illustration. Since the 1990s, large numbers of workers from countries such as "
           "Tajikistan, Kyrgyzstan and Uzbekistan have sought employment abroad, with Russia historically serving as the "
           "principal destination because of a widely shared language, relatively easy entry and a persistent demand for "
           "labour in construction, trade and services. For some of these countries, money sent home has at times represented "
           "a very large share of national income, placing them among the most remittance-dependent economies in the world. "
           "In recent years, destinations appear to have become more varied, but the dominant pattern has proved remarkably persistent."),
         P("At the household level, the benefits are tangible. Studies in many countries suggest that families receiving "
           "remittances are better able to afford food, medicine and school fees, and are less likely to fall into poverty "
           "when a harvest fails or a breadwinner falls ill. In this sense, remittances act as a form of private insurance, "
           "and one that tends to be countercyclical: when the home economy suffers a downturn, migrants often send more "
           "rather than less. Unlike foreign aid, moreover, the money goes directly to recipients, bypassing bureaucracies "
           "and the risk of diversion by officials."),
         P("Whether remittances promote long-term development, however, is a more contested question. Critics have observed "
           "that a large proportion of the money is spent on everyday consumption, on lavish celebrations and on the "
           "construction of houses, rather than on productive enterprises. Defenders reply that the distinction is less clear "
           "than it appears. Spending on education and health is arguably an investment in human capital, and even house "
           "building creates work for local builders and suppliers. What appears to matter most is whether the surrounding "
           "economy offers opportunities for investment: where small businesses face burdensome regulation, unreliable credit "
           "and weak property rights, it is hardly surprising that families prefer to spend rather than invest."),
         P("There are also concerns about dependence. When a substantial proportion of working-age adults spends much of the "
           "year abroad, villages may face labour shortages, children may grow up with an absent parent, and elderly relatives "
           "may lose a source of everyday care. At the national level, a steady inflow of foreign currency can reduce the "
           "pressure on governments to undertake difficult reforms. Some economists have also argued that large inflows may "
           "push up the value of the domestic currency, making local exports less competitive, a phenomenon sometimes compared "
           "to the problems associated with sudden natural resource wealth."),
         P("Perhaps the most immediate risk, however, lies in the vulnerability of remittance flows to events in the host "
           "country. Because migrants are usually paid in the currency of the country where they work, a sharp depreciation "
           "of that currency reduces the value of what they send home, even if their wages remain unchanged. Central Asian "
           "economies experienced precisely this in the middle of the last decade, when a fall in oil prices and the weakening "
           "of the Russian rouble led to a marked decline in the dollar value of transfers. Households that had come to rely "
           "on regular payments suddenly found their incomes reduced, and the effects spread to shops, builders and banks."),
         P("None of this suggests that remittances are harmful in themselves; rather, it implies that their benefits depend "
           "heavily on the policies that surround them. Governments have experimented with lowering the cost of transfers, "
           "which can be considerable when money passes through expensive intermediaries, with encouraging migrants to use "
           "formal banking, and with schemes that channel savings into local businesses. Diversifying destinations and "
           "improving the skills of departing workers may also reduce exposure to a single foreign economy. Ultimately, "
           "remittances are perhaps best understood not as a substitute for domestic development but as a bridge, one that "
           "can support families through difficult years while more durable sources of growth are built."),
     ],
     [G('remittance', 'pul oʻtkazmasi (chet eldan oilaga yuboriladigan pul)'), G('exceed', 'oshib ketmoq, ortiq boʻlmoq'),
      G('by a wide margin', 'katta farq bilan'), G('equivalent to', '… ga teng'),
      G('striking illustration', 'yorqin misol'), G('principal destination', 'asosiy yoʻnalish (boriladigan joy)'),
      G('tangible', 'aniq, sezilarli, moddiy'), G('breadwinner', 'oila boquvchisi'),
      G('countercyclical', 'iqtisodiy siklga qarshi (inqirozda kuchayadigan)'), G('bypass', 'chetlab oʻtmoq'),
      G('contested', 'bahsli, munozarali'), G('lavish', 'dabdabali, isrofgarona'),
      G('human capital', 'inson kapitali (bilim, sogʻliq, koʻnikma)'), G('burdensome regulation', 'ogʻir, ortiqcha tartibga solish'),
      G('inflow', 'kirib kelish, oqim'), G('depreciation', 'qadrsizlanish (valyuta)'),
      G('intermediary', 'vositachi'), G('durable', 'barqaror, uzoq muddatli')],
     [GN('c57-cleft-sentences', 'Pseudo-cleft: What … is … (fikrni urgʻu bilan ajratish)',
         'What appears to matter most is whether the surrounding economy offers opportunities for investment'),
      GN('c34-participle-clauses', 'Sifatdosh (-ing) oborot: bypassing …',
         'the money goes directly to recipients, bypassing bureaucracies')],
     [
         tf('Individual remittance payments are usually fairly small.', 'T',
            '«typically modest sums» — «modest» = «fairly small». Yigʻindisi katta, lekin har bir toʻlov kichik.', 0, ng=True),
         tf('Remittances to poorer countries are now smaller than official development aid.', 'F',
            'Matnda aksi: remittances «now exceed official development aid by a wide margin» — kichik emas, ancha katta.', 0, ng=True),
         tf('Language was one of the reasons why Russia attracted workers from Central Asia.', 'T',
            '«because of a widely shared language» — til sabablardan biri sifatida aniq keltirilgan.', 1, ng=True),
         tf('Migrants from Kyrgyzstan generally earn more in Russia than migrants from Tajikistan.', 'NG',
            'Matnda Tojikiston va Qirgʻiziston faqat migrant yuboruvchi mamlakatlar sifatida tilga olingan; ularning '
            'maoshlari solishtirilmagan — NOT GIVEN.', 1),
         tf('Children in households receiving remittances perform better at school than other children.', 'NG',
            'Matnda pul maktab toʻlovlariga ishlatilishi aytilgan («school fees»), lekin bolalarning oʻqish natijalari '
            'solishtirilmagan — NOT GIVEN.', 2),
         tf('Migrants tend to send more money home when their own country is going through economic difficulties.', 'T',
            '«when the home economy suffers a downturn, migrants often send more rather than less» — parafraz.', 2, ng=True),
         tf('Remittances usually reach families only after passing through government agencies.', 'F',
            'Aksincha: «the money goes directly to recipients, bypassing bureaucracies» — davlat idoralarini chetlab oʻtadi.', 2, ng=True),
         tf('Supporters of remittances claim that spending on new houses brings no benefit to local communities.', 'F',
            'Himoyachilar aksini aytadi: «even house building creates work for local builders and suppliers».', 3, ng=True),
         ch('According to paragraph D, what mainly determines whether families invest remittances productively?',
            ['how much money each migrant is able to send', 'the wider conditions for doing business at home',
             'the level of education of the family members', 'advice given by banks in the host country'], 1,
            '«What appears to matter most is whether the surrounding economy offers opportunities for investment» — tartibga '
            'solish, kredit, mulk huquqi, yaʼni biznes muhiti hal qiluvchi.', 3),
         ch('Why does the writer compare the effect of remittances to the effect of natural resource wealth?',
            ['to show that both can make a country\'s exports more expensive',
             'to argue that remittances are a more reliable source of income',
             'to suggest that migrants often work in the oil industry',
             'to explain why governments prefer remittances to aid'], 0,
            'Taqqoslash «push up the value of the domestic currency, making local exports less competitive» jumlasidan keyin '
            'keladi — ikkalasi ham eksportni qimmatlashtirishi mumkin.', 4),
         ch('What caused the fall in the dollar value of remittances to Central Asia described in paragraph F?',
            ['Migrants\' wages in Russia were cut.', 'Many migrants returned home at the same time.',
             'The Russian currency lost value.', 'Banks raised the fees for international transfers.'], 2,
            '«the weakening of the Russian rouble led to a marked decline in the dollar value of transfers»; matnda maoshlar '
            'oʻzgarmasa ham qiymat tushishi taʼkidlangan — «even if their wages remain unchanged».', 5),
         gap('Because they help families cope with sudden losses, remittances can work as a kind of private ___.',
             ['insurance'],
             '«remittances act as a form of private insurance» — «a form of» = «a kind of».', 2, 2),
         gap('In the writer\'s view, remittances should be seen as a ___ rather than as a replacement for domestic development.',
             ['bridge', 'a bridge'],
             '«not as a substitute for domestic development but as a bridge» — «substitute» = «replacement».', 6, 2),
         ch('Which statement best summarises the writer\'s overall position?',
            ['Remittances do more harm than good to developing economies.',
             'The value of remittances depends largely on the policies around them.',
             'Governments should discourage citizens from working abroad.',
             'Remittances have replaced the need for foreign investment.'], 1,
            '«their benefits depend heavily on the policies that surround them» — muallif zararli ham, mukammal ham demaydi.', 6),
     ])


# ---------------------------------------------------------------- 2. Urbanisation
H2 = ['Weighing the reasons for leaving the land', 'Homes built outside the official system',
      'Management, not movement, as the decisive factor', 'Why concentration makes economic sense',
      'Governments that have halted migration to cities', 'Pressures felt even by wealthier cities',
      'A more positive view of unplanned neighbourhoods', 'A historic change in where people live',
      'The decline of farming as an occupation']

text(B, 'c1-07-urbanisation', 'Shaharlashuv', 'Urbanisation', 'C1', 'exam',
     L('Jamiyat', 'Society'),
     'Akademik matn: odamlar nega shaharlarga koʻchadi, norasmiy turar joylar, infratuzilmaga bosim va zichlikning '
     'iqtisodiy afzalliklari. Asosiy topshiriq: Matching headings — 9 ta sarlavhadan har bir xatboshiga bittasini tanlang '
     '(ikkitasi ortiqcha). Sarlavha xatboshining umumiy gʻoyasini ifodalaydi, bitta mos soʻzga aldanmang: avval xatboshining '
     'birinchi va oxirgi jumlasini oʻqing. Keyin TFNG, boʻshliq va test savollari. Taxminan 20 daqiqa.',
     [
         P("For most of human history, the overwhelming majority of people lived in the countryside. That balance has now "
           "shifted decisively. It is widely reported that, at some point in the first decade of this century, the number of "
           "people living in urban areas overtook the rural population for the first time, and demographers expect the urban "
           "share to keep rising for decades, with most of the growth concentrated in Asia and Africa. The process, known as "
           "urbanisation, is among the defining transformations of the modern era, yet its consequences remain the subject of "
           "lively debate among economists, planners and the residents of cities themselves."),
         P("Explanations of why people move to cities typically distinguish between push and pull factors. On the one hand, "
           "rural life may offer limited prospects: farm incomes are often low and unpredictable, land may be divided into ever "
           "smaller plots between heirs, and a drought or flood can wipe out a year's work. On the other hand, cities appear to "
           "promise higher wages, a wider range of jobs and better access to schools and hospitals. Migrants do not always find "
           "what they were hoping for, but for many the decision is a rational calculation: even an insecure urban job may pay "
           "more than agricultural labour, and the presence of relatives who have already made the move can ease the transition "
           "considerably."),
         P("Economists have long argued that cities are not merely large collections of people but engines of productivity. "
           "When firms, workers and suppliers are concentrated in one place, they benefit from what are known as agglomeration "
           "economies. Businesses can draw on a deep pool of skilled labour, workers can change employers without relocating, "
           "and ideas spread more rapidly through informal contact. It is partly for this reason that a disproportionate share "
           "of national output in many countries is generated in a handful of large cities. Density also makes certain services "
           "cheaper to provide per person, since a single water main or bus route can serve thousands of households."),
         P("Rapid growth, however, frequently outpaces the capacity of governments to plan for it. When new arrivals cannot "
           "afford formal housing, they often build their own homes on land they do not legally own, typically on the urban "
           "fringe or on sites considered unsuitable for construction, such as steep slopes or riverbanks prone to flooding. "
           "Such informal settlements now house a very large number of people worldwide. Living conditions in them vary "
           "enormously, but residents commonly lack secure tenure, adequate sanitation and reliable access to clean water, and "
           "the constant threat of eviction discourages them from investing in their homes."),
         P("It would be misleading, however, to regard informal settlements purely as places of misery. Many are vibrant "
           "communities with active local economies, in which residents run shops, workshops and services and gradually "
           "improve their dwellings as their incomes rise. Some urban planners now argue that demolishing such neighbourhoods "
           "and relocating their inhabitants to distant housing estates has often done more harm than good, cutting people off "
           "from jobs and social networks. Instead, they advocate upgrading in place: providing legal title, paved roads, "
           "drainage and electricity while allowing communities to remain where they are."),
         P("Even in more prosperous cities, growth places considerable strain on infrastructure. Roads become congested, public "
           "transport is overcrowded, and the cost of housing may rise faster than incomes, pushing lower-paid workers ever "
           "further from their jobs. Air pollution, much of it caused by traffic and heating, is a persistent problem in many "
           "large cities. Because major infrastructure takes years to plan, finance and build, cities that grow quickly are "
           "often perpetually catching up, investing to meet yesterday's demand rather than tomorrow's."),
         P("Whether urbanisation proves beneficial thus depends less on the movement of people itself than on how it is "
           "managed. Cities that invest early in transport, coordinate the use of land and include informal neighbourhoods in "
           "their plans appear better able to translate density into prosperity. Those that do not risk concentrating poverty "
           "rather than reducing it. The question for policymakers is therefore not whether to allow urban growth, which is in "
           "any case largely unstoppable, but how to ensure that its benefits are widely shared."),
     ],
     [G('overwhelming majority', 'mutlaq koʻpchilik'), G('decisively', 'qatʼiy, hal qiluvchi tarzda'),
      G('defining transformation', 'davrni belgilovchi oʻzgarish'), G('prospects', 'istiqbol, imkoniyatlar'),
      G('heir', 'merosxoʻr'), G('ease the transition', 'oʻtishni yengillashtirmoq'),
      G('agglomeration economies', 'aglomeratsiya samarasi (bir joyda toʻplanishdan foyda)'),
      G('disproportionate share', 'nomutanosib (haddan ortiq) ulush'), G('outpace', 'ortda qoldirmoq, oʻzib ketmoq'),
      G('urban fringe', 'shahar chekkasi'), G('prone to', '… ga moyil, … xavfi yuqori'),
      G('informal settlement', 'norasmiy (rejasiz) turar joy'), G('secure tenure', 'mulk/turar joyga kafolatlangan huquq'),
      G('eviction', 'majburan koʻchirish, uydan chiqarish'), G('vibrant', 'jonli, gavjum'),
      G('advocate', 'yoqlamoq, targʻib qilmoq'), G('congested', 'tirband, gavjum'),
      G('perpetually', 'doimo, toʻxtovsiz')],
     [GN('c16-reporting-passive', 'Xabar qiluvchi majhul nisbat: It is widely reported that …',
         'It is widely reported that'),
      GN('c39-it-there', 'Kirish «it»: It would be misleading … to regard …',
         'It would be misleading, however, to regard informal settlements purely as places of misery')],
     [
         hd(0, H2, 7, 'Xatboshi A: «the number of people living in urban areas overtook the rural population for the first '
                      'time» — odamlar yashaydigan joyda tarixiy burilish.'),
         hd(1, H2, 0, 'Xatboshi B: «push and pull factors» — qishloqdan ketish sabablari tarozida tortiladi, qaror «a rational '
                      'calculation». «The decline of farming as an occupation» chalgʻitadi: dehqonchilik kamayishi emas, '
                      'migratsiya sabablari muhokama qilinadi.'),
         hd(2, H2, 3, 'Xatboshi C: firmalar va ishchilar bir joyda toʻplansa unumdorlik oshadi — «agglomeration economies», '
                      '«engines of productivity». Bu — zichlikning iqtisodiy mantigʻi.'),
         hd(3, H2, 1, 'Xatboshi D: odamlar oʻzlariga tegishli boʻlmagan yerda uy quradi — «land they do not legally own», '
                      '«informal settlements». «official system» = formal housing / legal ownership.'),
         hd(4, H2, 6, 'Xatboshi E: «It would be misleading … to regard informal settlements purely as places of misery» — '
                      'norasmiy mahallalarga ijobiyroq qarash, «upgrading in place».'),
         hd(5, H2, 5, 'Xatboshi F: yoʻllar, transport, uy-joy oʻsishga ulgurmaydi — «strain on infrastructure», '
                      '«Even in more prosperous cities» — boy shaharlar ham bosimni his qiladi; «perpetually catching up».'),
         hd(6, H2, 2, 'Xatboshi G: «depends less on the movement of people itself than on how it is managed» — sarlavha shu '
                      'fikrning aniq qayta ifodasi. «Governments that have halted migration» notoʻgʻri: oʻsish «largely '
                      'unstoppable» deyilgan.'),
         tf('Most future urban growth is expected to take place in Europe and North America.', 'F',
            '«most of the growth concentrated in Asia and Africa» — Yevropa va Shimoliy Amerika emas.', 0, ng=True),
         tf('Having family members already living in a city can make moving there easier.', 'T',
            '«the presence of relatives who have already made the move can ease the transition considerably».', 1, ng=True),
         tf('Informal settlements are more common in coastal cities than in inland ones.', 'NG',
            'Matnda daryo boʻyidagi xavfli joylar («riverbanks prone to flooding») tilga olingan, lekin qirgʻoqboʻyi va ichki '
            'shaharlar solishtirilmagan — NOT GIVEN.', 3),
         gap('Rather than relocating residents, some planners prefer ___ in place.', 'upgrading',
             '«they advocate upgrading in place» — «advocate» = «prefer / support».', 4, 2),
         gap('When firms and workers cluster together, they gain from what economists call ___ economies.', 'agglomeration',
             '«they benefit from what are known as agglomeration economies».', 2, 2),
         ch('What does the writer mean by saying that fast-growing cities are "perpetually catching up"?',
            ['They copy the infrastructure of older cities.', 'Their investment always responds to past rather than future needs.',
             'They grow faster than any other type of settlement.', 'They eventually overtake richer cities economically.'], 1,
            'Izoh darhol keladi: «investing to meet yesterday\'s demand rather than tomorrow\'s» — sarmoya kechikib, '
            'oʻtgan ehtiyojga javob beradi.', 5),
         ch('What is the writer\'s main conclusion about urbanisation?',
            ['It should be slowed down by governments.', 'Its outcome depends mainly on the quality of planning.',
             'It inevitably increases poverty.', 'Its benefits are mostly limited to rich countries.'], 1,
            '«depends less on the movement of people itself than on how it is managed»; sekinlashtirish emas — oʻsish '
            '«largely unstoppable».', 6),
     ])


# ---------------------------------------------------------------- 3. Four-day week
text(B, 'c1-08-four-day-week', 'Toʻrt kunlik ish haftasi', 'The Four-Day Week', 'C1', 'exam',
     L('Mehnat', 'Work'),
     'Akademik matn: toʻrt kunlik ish haftasi boʻyicha tajribalar, unumdorlik, xodimlar farovonligi va bu tizim qiyin '
     'boʻlgan sohalar. Asosiy topshiriq: koʻp variantli test (multiple choice) — maqsad, munosabat, xulosa va asosiy gʻoya '
     'savollari; qoʻshimcha TFNG va boʻshliq. Har bir variantni matn bilan solishtiring: notoʻgʻri variantlar koʻpincha '
     'matndagi soʻzni takrorlaydi, lekin maʼnosini buzadi. Muallifning ehtiyotkor soʻzlariga («reportedly», «may», '
     '«appears») eʼtibor bering. Taxminan 20 daqiqa.',
     [
         P("The idea that people might one day work far fewer hours is hardly new. In the first half of the twentieth century, as the "
           "five-day week gradually became standard in many industrialised countries, some commentators predicted that "
           "technological progress would eventually allow working time to shrink much further. That prediction has largely "
           "failed to materialise: in much of the world, the standard full-time week has changed little for decades. In recent "
           "years, however, the four-day week has returned to public debate, encouraged by a series of experiments in which "
           "employers reduced working time while, crucially, keeping pay unchanged."),
         P("It is worth clarifying what the term actually means, since it is used to describe quite different arrangements. "
           "In some versions, employees compress their usual hours into four longer days, so that total working time stays "
           "the same. The model that has attracted most attention, by contrast, involves a genuine reduction in hours, with "
           "full pay offered on condition that productivity is maintained. Some trials have not involved a fixed day off at "
           "all, but rather a reduction in weekly hours distributed in whatever way suits the organisation. Comparisons "
           "between studies are inevitably complicated by these differences."),
         P("Trials of this kind have been conducted in several countries, including Iceland, where public-sector employees "
           "took part in widely publicised experiments with shorter hours, and the United Kingdom, where dozens of companies "
           "joined a coordinated pilot scheme. The results reported have been mixed but often encouraging. In many "
           "participating organisations, managers stated that output was largely maintained, and in some pilots a majority of "
           "firms reportedly chose to continue with the shorter week after the trial had ended. Employees frequently described "
           "lower levels of stress and fatigue, better sleep and more time for family and personal responsibilities."),
         P("How could the same work be done in less time? Advocates point to the familiar inefficiencies of the conventional "
           "working day: lengthy meetings, constant interruptions and tasks that expand to fill the time available. When hours "
           "are reduced, teams are often obliged to scrutinise their routines, cancelling unnecessary meetings and protecting "
           "periods of uninterrupted concentration. There may also be indirect gains. Rested employees may make fewer errors, "
           "take fewer sick days and be less inclined to resign, which in turn reduces the considerable cost of recruiting "
           "and training replacements."),
         P("Sceptics, however, urge caution in interpreting these findings. Organisations that volunteer for trials are "
           "unlikely to be typical: they tend to be enthusiastic about the idea and may be particularly well suited to it from "
           "the outset. Many studies rely heavily on self-reported measures of wellbeing and productivity, which may be coloured "
           "by participants' hopes that the experiment will succeed. Moreover, trials typically last months rather than years, "
           "and it remains unclear whether initial gains would persist once the novelty had worn off."),
         P("There is also the question of which jobs lend themselves to a shorter week. In office-based work, where output is "
           "difficult to measure precisely and much time is lost to inefficiency, reorganisation may well compensate for fewer "
           "hours. In sectors where services must be provided continuously, such as hospitals, care homes, public transport "
           "and retail, the situation is different. A nurse cannot treat patients more quickly simply because a shift has been "
           "shortened; maintaining the same level of service would require hiring additional staff, raising costs considerably. "
           "Similar difficulties arise in manufacturing processes that depend on machinery running for fixed periods. Staggered "
           "rotas can soften the problem, but they rarely eliminate it."),
         P("On balance, the evidence so far suggests that a four-day week can work well for certain organisations, particularly "
           "those in which the main obstacle to productivity is the organisation of time rather than its quantity. Whether it "
           "could become a universal standard is far less certain. Perhaps the most valuable lesson of the trials is not that "
           "every employer should adopt a particular model, but that the length of the working week is a matter of choice "
           "rather than a fixed law of economic life, and that the relationship between hours and output is more complicated "
           "than is often assumed."),
     ],
     [G('fail to materialise', 'roʻyobga chiqmaslik, amalga oshmaslik'), G('crucially', 'eng muhimi, hal qiluvchi jihati'),
      G('compress', 'siqmoq, qisqa muddatga jamlamoq'), G('genuine reduction', 'haqiqiy qisqarish'),
      G('on condition that', '… sharti bilan'), G('pilot scheme', 'sinov loyihasi'),
      G('fatigue', 'charchoq, holsizlik'), G('scrutinise', 'sinchiklab tekshirmoq'),
      G('uninterrupted', 'uzluksiz, toʻxtovsiz'), G('be inclined to', '… ga moyil boʻlmoq'),
      G('urge caution', 'ehtiyotkorlikka chaqirmoq'), G('from the outset', 'boshidanoq'),
      G('self-reported', 'ishtirokchining oʻzi xabar bergan (soʻrovnoma asosidagi)'), G('novelty', 'yangilik (zavqi)'),
      G('lend itself to', '… ga mos kelmoq, qulay boʻlmoq'), G('compensate for', 'oʻrnini qoplamoq'),
      G('staggered rota', 'navbatma-navbat (surilgan) ish jadvali'), G('obstacle', 'toʻsiq')],
     [GN('c09-probability-deduction', 'Ehtimollik: be unlikely to …',
         'Organisations that volunteer for trials are unlikely to be typical'),
      GN('c34-participle-clauses', 'Sifatdosh (-ed) oborot: encouraged by …',
         'the four-day week has returned to public debate, encouraged by a series of experiments')],
     [
         ch('What does the writer say about past predictions of much shorter working hours?',
            ['They were based on inaccurate economic data.', 'They have, for the most part, not come true.',
             'They led directly to the recent trials.', 'They were rejected by most commentators at the time.'], 1,
            '«That prediction has largely failed to materialise» — «largely» = «for the most part».', 0),
         ch('Why does the writer explain the different meanings of "four-day week" in paragraph B?',
            ['to show that the compressed model is the most popular',
             'to point out that varied arrangements make studies hard to compare',
             'to criticise campaigners for using the term incorrectly',
             'to argue that a fixed day off is essential'], 1,
            'Xatboshi oxirida: «Comparisons between studies are inevitably complicated by these differences».', 1),
         tf('In the compressed version of the four-day week, employees work fewer hours in total.', 'F',
            '«compress their usual hours into four longer days, so that total working time stays the same» — jami soat '
            'kamaymaydi.', 1, ng=True),
         tf('Every organisation that took part in the trials decided to keep the shorter week.', 'F',
            'Faqat «in some pilots a majority of firms reportedly chose to continue» — hammasi emas.', 2, ng=True),
         tf('Most of the trials described were organised by trade unions.', 'NG',
            'Sinovlarni kim tashkil qilgani haqida matnda maʼlumot yoʻq — NOT GIVEN.', 2),
         ch('The phrase "tasks that expand to fill the time available" is given as an example of',
            ['a reason why employees feel stressed.', 'inefficiency in the traditional working day.',
             'a benefit of reducing working hours.', 'the cost of training new staff.'], 1,
            'U «the familiar inefficiencies of the conventional working day» roʻyxatining bir qismi.', 3),
         tf('Lower staff turnover may reduce some of an employer\'s costs.', 'T',
            '«be less inclined to resign, which in turn reduces the considerable cost of recruiting and training '
            'replacements» — «turnover» = ishdan ketish.', 3, ng=True),
         gap('With fewer hours, teams often try to protect periods of ___ concentration.', 'uninterrupted',
             '«protecting periods of uninterrupted concentration».', 3, 2),
         ch('What is the sceptics\' concern about organisations that volunteer for trials?',
            ['They usually stop the trial early.', 'They may not represent employers in general.',
             'They often hide negative results.', 'They tend to be large public institutions.'], 1,
            '«are unlikely to be typical … may be particularly well suited to it from the outset» — umumiy holatni aks '
            'ettirmasligi mumkin.', 4),
         gap('Sceptics note that many studies depend on ___ measures, which may reflect participants\' hopes.',
             'self-reported',
             '«rely heavily on self-reported measures of wellbeing and productivity, which may be coloured by participants\' '
             'hopes».', 4, 2),
         ch('Why does the writer mention a nurse in paragraph F?',
            ['to show that some work cannot simply be done faster',
             'to suggest that hospital staff are the most overworked',
             'to prove that the four-day week has failed in health care',
             'to recommend staggered rotas for all sectors'], 0,
            '«A nurse cannot treat patients more quickly simply because a shift has been shortened» — uzluksiz xizmat '
            'sohalarida ishni tezlashtirib boʻlmaydi.', 5),
         tf('Staggered rotas usually solve the staffing problems of continuous services completely.', 'F',
            '«they rarely eliminate it» — kamdan-kam toʻliq hal qiladi.', 5, ng=True),
         ch('Which best describes the writer\'s attitude to the four-day week?',
            ['enthusiastic support for making it universal', 'complete rejection based on weak evidence',
             'cautious recognition of its potential in some settings', 'indifference to the results of the trials'], 2,
            '«can work well for certain organisations» lekin «Whether it could become a universal standard is far less '
            'certain» — ehtiyotkor, qisman ijobiy.', 6),
     ])


# ---------------------------------------------------------------- 4. Cooperatives
text(B, 'c1-09-cooperatives', 'Kooperativlar', 'Cooperatives', 'C1', 'exam',
     L('Iqtisodiyot', 'Economics'),
     'Akademik matn: kooperativlar — aʼzolari egalik qiladigan korxonalar, ularning tarixi (Rochdeyl kashshoflari), '
     'fermer va kredit kooperativlari, kuchli va zaif tomonlari. Asosiy topshiriq: summary completion — xulosa matnidagi '
     'boʻshliqlarni matndan olingan soʻzlar bilan toʻldiring (NO MORE THAN TWO WORDS). Xulosa matn tartibida boradi: '
     'avval boʻshliq atrofidagi sinonimlarni toping, keyin soʻzni aynan koʻchiring, grammatikasini tekshiring. Qolgan '
     'savollar — TFNG va test. Taxminan 20 daqiqa.',
     [
         P("Most businesses are owned by investors who expect a return on the capital they have provided. A cooperative works "
           "on a different principle. It is an enterprise owned and controlled by the people who use its services, whether as "
           "customers, workers, farmers or savers, and its primary purpose is to meet their needs rather than to maximise "
           "profit for outside shareholders. Cooperatives can be found in almost every country and in sectors as diverse as "
           "retail, agriculture, banking, housing and insurance, and their combined membership is very large indeed."),
         P("Although people have pooled resources for mutual benefit throughout history, the modern cooperative movement is "
           "usually traced to 1844, when a group of weavers and other workers in the English town of Rochdale opened a small "
           "shop selling basic goods such as flour, butter and sugar. Calling themselves the Rochdale Society of Equitable "
           "Pioneers, they were responding to hardship and to the widespread practice among traders of selling adulterated "
           "food at inflated prices. Their store was by no means the first cooperative venture, and several earlier attempts "
           "had failed, but it proved remarkably durable, and the rules the Pioneers adopted became a model for others."),
         P("Those rules contained several ideas that remain central to cooperatives today. Membership was open to anyone "
           "willing to accept its responsibilities. Each member had one vote, regardless of how much capital he or she had "
           "invested, which distinguished the society sharply from a conventional company, where voting power follows "
           "shareholding. Any surplus, after costs and reserves had been covered, was returned to members in proportion to "
           "their purchases rather than their investment, a payment commonly known as the dividend. Versions of these "
           "principles were later adopted by an international alliance of cooperatives founded at the end of the nineteenth "
           "century."),
         P("The idea soon spread beyond retail. In the countryside, farmers discovered that by combining their produce they "
           "could afford equipment that none of them could have bought alone, and could negotiate better prices with "
           "merchants. Denmark became a celebrated example, with cooperative dairies spreading rapidly across the country in "
           "the late nineteenth century. Somewhat earlier, from the middle of the century, credit cooperatives had emerged in "
           "Germany, where reformers sought to give farmers and craftsmen access to loans on fair terms. Because members knew one another and shared "
           "liability, these institutions could lend to people whom commercial banks considered too risky, relying on local "
           "knowledge and social pressure instead of collateral."),
         P("Supporters argue that cooperatives offer distinctive advantages. Because they are owned by their users, they have "
           "less incentive to exploit customers, and because profits are not paid out to distant shareholders, they tend to "
           "keep wealth within local communities. Some research suggests that cooperatives may be more resilient during "
           "economic crises, partly because they take a longer-term view and are less exposed to pressure for short-term "
           "returns. Worker cooperatives, in which employees own the business, have been credited with greater job security, "
           "since members may prefer to share reduced hours rather than dismiss colleagues."),
         P("The model is not without its difficulties. Raising capital can be hard, since outside investors cannot buy "
           "control, and members may be unwilling or unable to contribute large sums. Democratic decision-making can be slow, "
           "and as cooperatives grow, ordinary members may lose interest in governance, leaving power in the hands of "
           "professional managers whose priorities differ from their own. Some large cooperatives have struggled to compete "
           "with conventional rivals, and a number have converted into ordinary companies, sometimes because existing members "
           "stood to gain financially from the change."),
         P("The reputation of cooperatives also varies with history. In the Soviet Union and other socialist states, collective "
           "farms and many other enterprises were described as cooperatives but were in practice subject to tight state "
           "control, and membership was frequently far from voluntary. In some post-Soviet countries, this legacy appears to "
           "have left a degree of suspicion towards the very word. Elsewhere, cooperatives are associated with independence "
           "and self-help. Their future may depend on whether they can preserve the democratic spirit of the Rochdale weavers "
           "while adapting to markets far larger and more complex than those of the nineteenth century."),
     ],
     [G('maximise profit', 'foydani maksimal darajaga yetkazmoq'), G('pool resources', 'mablagʻlarni birlashtirmoq'),
      G('mutual benefit', 'oʻzaro manfaat'), G('be traced to', '… dan boshlangan deb hisoblanmoq'),
      G('adulterated', 'aralashma qoʻshilgan, soxtalashtirilgan (oziq-ovqat)'), G('inflated prices', 'sunʼiy oshirilgan narxlar'),
      G('venture', 'tashabbus, korxona'), G('regardless of', '… dan qatʼi nazar'),
      G('surplus', 'ortiqcha daromad, profitsit'), G('in proportion to', '… ga mutanosib ravishda'),
      G('liability', 'javobgarlik (moliyaviy)'), G('collateral', 'garov'),
      G('incentive', 'ragʻbat, qiziqtiruvchi omil'), G('resilient', 'chidamli, barqaror'),
      G('be credited with', '… ga erishgan deb eʼtirof etilmoq'), G('governance', 'boshqaruv'),
      G('stand to gain', 'foyda koʻrish imkoniga ega boʻlmoq'), G('legacy', 'meros, asorat')],
     [GN('c34-participle-clauses', 'Sifatdosh (-ing) oborot gap boshida: Calling themselves …',
         'Calling themselves the Rochdale Society of Equitable Pioneers, they were responding to hardship'),
      GN('c33-relative-advanced', 'Murakkab nisbiy gap: whom commercial banks considered too risky',
         'these institutions could lend to people whom commercial banks considered too risky')],
     [
         gap('Summary: The modern cooperative movement is usually said to have begun in 1844, when ___ and other workers in '
             'Rochdale opened a shop.', 'weavers',
             '«a group of weavers and other workers in the English town of Rochdale opened a small shop» — «traced to» = '
             '«said to have begun».', 1, 2),
         gap('Summary: The founders were reacting partly to traders who sold ___ food at high prices.', 'adulterated',
             '«selling adulterated food at inflated prices» — «inflated» = «high».', 1, 2),
         gap('Summary: Unlike in an ordinary company, where voting power depends on ___, every member had one vote.',
             'shareholding',
             '«a conventional company, where voting power follows shareholding» — «follows» = «depends on».', 2, 2),
         gap('Summary: Any surplus was returned according to what members had bought, in a payment called the ___.',
             ['dividend', 'the dividend'],
             '«in proportion to their purchases … a payment commonly known as the dividend».', 2, 2),
         gap('Summary: In Denmark, cooperative ___ spread quickly in the late nineteenth century.', 'dairies',
             '«cooperative dairies spreading rapidly across the country in the late nineteenth century».', 3, 2),
         gap('Summary: German credit cooperatives relied on local knowledge and social pressure rather than ___.', 'collateral',
             '«relying on local knowledge and social pressure instead of collateral» — «instead of» = «rather than».', 3, 2),
         tf('The Rochdale shop was the first cooperative ever established.', 'F',
            '«Their store was by no means the first cooperative venture, and several earlier attempts had failed».', 1, ng=True),
         tf('Credit cooperatives were able to lend to people whom ordinary banks were reluctant to lend to.', 'T',
            '«could lend to people whom commercial banks considered too risky» — paraphrase.', 3, ng=True),
         tf('Worker cooperatives generally pay higher wages than conventional firms.', 'NG',
            'Matnda faqat ish oʻrni xavfsizligi («greater job security») aytilgan; maosh darajasi haqida maʼlumot yoʻq — '
            'NOT GIVEN.', 4),
         ch('According to paragraph E, why may worker cooperatives offer greater job security?',
            ['They are protected by special laws.', 'Members may choose to cut hours instead of dismissing staff.',
             'They receive support from local communities.', 'They never face pressure from competitors.'], 1,
            '«members may prefer to share reduced hours rather than dismiss colleagues».', 4),
         ch('Why can it be difficult for cooperatives to raise capital?',
            ['Banks are not allowed to lend to them.', 'Outside investors cannot gain control in return for their money.',
             'Their managers are unwilling to borrow.', 'Their profits are too small to attract members.'], 1,
            '«Raising capital can be hard, since outside investors cannot buy control».', 5),
         tf('As cooperatives become larger, ordinary members may become less involved in running them.', 'T',
            '«as cooperatives grow, ordinary members may lose interest in governance».', 5, ng=True),
         ch('Why does the writer refer to collective farms in the Soviet Union?',
            ['to show that cooperatives work best under state control',
             'to explain why the word "cooperative" is viewed with suspicion in some places',
             'to argue that cooperatives cannot succeed in large markets',
             'to compare their efficiency with that of the Rochdale store'], 1,
            'Ular faqat nomigagina kooperativ edi — «in practice subject to tight state control»; natijada «a degree of '
            'suspicion towards the very word».', 6),
     ])


# ---------------------------------------------------------------- 5. Inequality
H5 = ['What one figure can hide', 'Policies that have successfully reduced inequality', 'Deciding what to count',
      'Two trends that seem to contradict each other', 'Where data ends and values begin', 'A single number explained',
      'Competing accounts of widening gaps', 'Does inequality shape the next generation?']

text(B, 'c1-10-inequality', 'Ijtimoiy tengsizlik', 'Measuring Inequality', 'C1', 'exam',
     L('Jamiyat', 'Society'),
     'Toʻliq mashq testi: ijtimoiy tengsizlikni oʻlchash (Jini koeffitsiyenti), uning sabablari haqidagi bahslar va '
     'avlodlararo ijtimoiy harakatchanlikka taʼsiri. Imtihondagidek aralash topshiriqlar: Matching headings, True / False / '
     'Not Given, test va boʻshliq toʻldirish. Matn betaraf: muallif turli qarashlarni keltiradi — kimning fikri ekaniga '
     'eʼtibor bering. Taxminan 20 daqiqa: avval sarlavhalar, keyin TFNG va boʻshliqlar, test savollari oxirida.',
     [
         P("Few economic topics provoke as much disagreement as inequality. Yet before one can debate whether inequality is "
           "too high, too low or simply inevitable, one must first decide what is being measured, and among whom. Income, the "
           "flow of money people receive from wages, investments and benefits over a period, is the most commonly studied. "
           "Wealth, the stock of assets people own minus their debts, is another, and it is typically distributed far more "
           "unevenly than income, since assets accumulate over lifetimes and can be passed between generations. Economists "
           "also distinguish inequality of outcomes from inequality of opportunity, the extent to which a person's prospects "
           "are shaped by circumstances beyond their control, such as the family into which they are born."),
         P("The most widely cited single measure is the Gini coefficient, named after the Italian statistician who proposed "
           "it in the early twentieth century. Its logic can be explained quite simply. Imagine lining up a population from poorest to richest "
           "and plotting the share of total income received by each successive portion. If income were shared perfectly "
           "equally, the poorest tenth would receive a tenth of the total, the poorest half would receive half, and so on, "
           "producing a straight diagonal line. In reality, the line sags below this diagonal, and the Gini coefficient "
           "expresses the size of that gap as a number between zero, representing perfect equality, and one, representing a "
           "situation in which a single person receives everything. It is often multiplied by a hundred for convenience."),
         P("Convenient as it is, the Gini coefficient has limitations. Because it compresses an entire distribution into a "
           "single figure, very different societies can share the same score: one in which the middle class is squeezed, "
           "for instance, and another in which the very top pulls away from everyone else. For this reason, researchers often "
           "supplement it with other indicators, such as the share of income going to the top tenth or top hundredth of "
           "earners. Measurement is further complicated by the fact that the very wealthy may under-report their income in "
           "surveys, while tax records may miss informal earnings altogether."),
         P("Explanations for changes in inequality within countries are contested, and most economists believe that several "
           "forces operate simultaneously. One influential account emphasises technology, which is thought to have raised the "
           "demand for highly educated workers while reducing it for routine tasks that machines can perform. Another stresses "
           "globalisation, which has exposed some workers in richer countries to competition from lower-wage economies while "
           "creating opportunities for others. Still others point to institutions and policy: changes in taxation, declining "
           "trade union membership in some countries, and the rules governing finance and executive pay. Disentangling these "
           "influences is difficult, and the relative weight given to each often reflects underlying assumptions as well as evidence."),
         P("It is also important to distinguish between trends within countries and across the world as a whole. Over recent "
           "decades, rapid growth in several large Asian economies is generally believed to have lifted hundreds of millions "
           "of people out of extreme poverty, narrowing the gap between the average citizen of poorer and richer nations. At "
           "the same time, inequality within many individual countries has widened. Both observations can be true at once, "
           "which helps to explain why people examining the same data sometimes reach opposite conclusions."),
         P("Perhaps the most consequential debate concerns the relationship between inequality and social mobility, the "
           "ability of individuals to move up or down the economic ladder relative to their parents. Comparisons across "
           "countries suggest that societies with higher income inequality tend to have lower mobility between generations, "
           "a pattern sometimes referred to as the Great Gatsby curve. Several mechanisms have been proposed: wealthier "
           "families can invest more in education, housing near good schools and social connections, so advantages may be "
           "transmitted more effectively when the gaps between families are wider. Nevertheless, a correlation of this kind "
           "does not in itself prove causation, and the strength of the relationship remains disputed."),
         P("Ultimately, measurement can inform but not settle the question of how much inequality a society should accept. "
           "Some argue that a degree of inequality is a necessary consequence of rewarding effort, risk-taking and innovation, "
           "and that the priority should be raising living standards at the bottom rather than narrowing gaps. Others contend "
           "that large disparities undermine social cohesion and trust and concentrate political influence. These are "
           "questions of values as well as evidence. What careful measurement can offer is a shared factual basis, without "
           "which the debate risks becoming a mere exchange of assertions."),
     ],
     [G('provoke disagreement', 'kelishmovchilik keltirib chiqarmoq'), G('inevitable', 'muqarrar'),
      G('distributed unevenly', 'notekis taqsimlangan'), G('accumulate', 'toʻplanmoq, jamgʻarilmoq'),
      G('circumstances beyond their control', 'oʻz ixtiyoridan tashqaridagi sharoitlar'),
      G('coefficient', 'koeffitsiyent'), G('successive', 'ketma-ket keluvchi'),
      G('supplement', 'toʻldirmoq, qoʻshimcha qilmoq'), G('under-report', 'kamaytirib koʻrsatmoq'),
      G('simultaneously', 'bir vaqtning oʻzida'), G('disentangle', 'ajratib olmoq, chigalini yechmoq'),
      G('underlying assumptions', 'asosdagi (yashirin) farazlar'), G('consequential', 'muhim oqibatli'),
      G('social mobility', 'ijtimoiy harakatchanlik'), G('correlation', 'oʻzaro bogʻliqlik, korrelyatsiya'),
      G('causation', 'sababiyat'), G('disparity', 'tafovut, nomutanosiblik'),
      G('social cohesion', 'ijtimoiy birdamlik')],
     [GN('c46-contrast-concession', 'Toʻsiqsiz ergash gap: Convenient as it is, …',
         'Convenient as it is, the Gini coefficient has limitations'),
      GN('c14-complex-passive', 'Murakkab majhul nisbat: is thought to have raised',
         'which is thought to have raised the demand for highly educated workers')],
     [
         hd(2, H5, 0, 'Xatboshi C: Jini koeffitsiyenti butun taqsimotni bitta raqamga siqadi, shuning uchun turli jamiyatlar '
                      'bir xil natijaga ega boʻlishi mumkin — «very different societies can share the same score».'),
         hd(3, H5, 6, 'Xatboshi D: texnologiya, globallashuv, institutlar — tengsizlik oʻsishining raqobatdosh izohlari '
                      '(«One influential account … Another … Still others»).'),
         hd(4, H5, 3, 'Xatboshi E: mamlakatlar oʻrtasidagi farq qisqargan, mamlakatlar ichidagi farq esa oʻsgan — «Both '
                      'observations can be true at once». Bir-biriga zid koʻringan ikki tendensiya.'),
         hd(6, H5, 4, 'Xatboshi G: «measurement can inform but not settle the question … These are questions of values as well '
                      'as evidence». «Policies that have successfully reduced inequality» — matnda bunday siyosatlar yoʻq.'),
         tf('Wealth is generally shared more equally than income.', 'F',
            'Aksincha: wealth «is typically distributed far more unevenly than income».', 0, ng=True),
         tf('A Gini coefficient of zero would describe a society in which one person receives all the income.', 'F',
            'Nol — «perfect equality»; bir kishi hammasini olishi — bir («one»).', 1, ng=True),
         tf('Most countries publish an official Gini coefficient every year.', 'NG',
            'Matnda koeffitsiyent «the most widely cited» ekani va qanday hisoblanishi aytilgan, lekin davlatlar uni har yili '
            'eʼlon qilishi haqida maʼlumot yoʻq — NOT GIVEN.', 1),
         tf('Surveys may underestimate the incomes of the richest people.', 'T',
            '«the very wealthy may under-report their income in surveys» — «under-report» → natija kam koʻrsatiladi.', 2, ng=True),
         gap('If income were equally shared, the plotted line would be a straight ___.', ['diagonal', 'diagonal line'],
             '«producing a straight diagonal line».', 1, 2),
         gap('Technology is thought to have reduced the demand for workers who perform ___ tasks.', 'routine',
             '«reducing it for routine tasks that machines can perform».', 3, 2),
         ch('According to paragraph D, why do economists disagree about the importance of each cause?',
            ['because reliable data on inequality does not exist',
             'because their judgements partly depend on their prior assumptions',
             'because only one cause can operate at a time',
             'because globalisation has affected all workers equally'], 1,
            '«the relative weight given to each often reflects underlying assumptions as well as evidence».', 3),
         ch('The example of large Asian economies is used to show that',
            ['inequality within those countries has fallen sharply.',
             'gaps between countries can narrow while gaps within them widen.',
             'globalisation has harmed workers in poorer nations.',
             'extreme poverty has been eliminated worldwide.'], 1,
            'Osiyo oʻsishi «narrowing the gap between … poorer and richer nations», lekin «inequality within many individual '
            'countries has widened».', 4),
         ch('What is the writer\'s view of the link between inequality and social mobility?',
            ['It has been proved that inequality causes low mobility.', 'There is no connection between the two.',
             'There is a suggestive pattern, but cause and effect are not established.',
             'Mobility is highest in the most unequal societies.'], 2,
            '«societies with higher income inequality tend to have lower mobility» lekin «a correlation … does not in itself '
            'prove causation».', 5),
         gap('According to the writer, careful measurement can provide a shared ___ for the debate.', 'factual basis',
             '«What careful measurement can offer is a shared factual basis».', 6, 2),
     ])
