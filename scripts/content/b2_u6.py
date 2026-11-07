"""B2 · 6-boʻlim: Toʻliq mashq testlari (imtihon tarzidagi toʻliq oʻqish testlari)"""
from lib import *

B = 'b2'


def intro(topic):
    return (f'Toʻliq mashq testi: {topic} Haqiqiy imtihondagidek bitta matnga 13 ta savol va bir nechta topshiriq turi beriladi: '
            'Matching headings, True/False/Not Given, boʻshliq toʻldirish va test savollari. Taxminan 20 daqiqa ajrating: '
            'avval matnga tez koʻz yugurtirib sarlavhalarni moslang, keyin TFNG va boʻshliqlarni bajaring, '
            'test savollarini esa oxiriga qoldiring.')


# ---------------------------------------------------------------- 1-test
H1 = ['A story that historians question', 'What made the sheets special',
      'Westward across the Islamic world and beyond', 'An old craft brought back to life',
      'A battle that changed trade routes', 'Why paper became more expensive']

text(B, 'b2-26-test1', '1-test: Qogʻoz yoʻli', 'The Paper Road', 'B2', 'exam',
     L('Tarix', 'History'), intro('qogʻozning Xitoydan Samarqand orqali dunyoga tarqalishi haqidagi matn.'),
     [
         P("Paper is so ordinary today that few people stop to think about where it came from. Yet the material we use for "
           "notebooks, books and packaging made a remarkable journey before it reached every corner of the world. That "
           "journey began in China, lasted more than a thousand years and passed through the heart of Central Asia. Its story shows how a simple invention can change the way knowledge is stored and shared."),
         P("Chinese tradition credits a court official named Cai Lun with improving the method of papermaking at the beginning "
           "of the second century, although older fragments found by archaeologists suggest that simpler forms of paper "
           "existed before him. Early papermakers did not rely only on fresh plants. Alongside tree bark and hemp, they "
           "used old rags and even worn fishing nets, which were soaked, beaten into a pulp and spread thinly to dry."),
         P("For centuries, the technique remained largely unknown outside East Asia. According to a famous tradition, it "
           "reached Samarkand after the Battle of Talas in 751, when Chinese prisoners of war are said to have taught local "
           "craftsmen their skills. Many historians treat this story with caution. They point out that knowledge often "
           "travelled quietly along trade routes, and papermaking may have arrived earlier and more gradually. Whatever the "
           "exact route, Samarkand soon became an important centre of production."),
         P("Samarkand paper gained a reputation that spread far beyond the city. It was valued for being smooth, strong and "
           "light in colour, and writers in the wider Islamic world praised its quality. Copyists and scholars, who needed a reliable surface for long texts, were among its most enthusiastic users. One reason was careful finishing: "
           "the sheets were often polished with a smooth stone so that ink would not spread into the fibres. The streams and "
           "canals around the city also supplied the clean water that the process required."),
         P("From Central Asia, the craft moved steadily westward. It is generally believed that Baghdad had its own paper "
           "mills by the end of the eighth century, and production later developed in Damascus, Cairo and across North "
           "Africa. Paper was far cheaper than parchment made from animal skin, so it became much easier to copy books, keep "
           "government records and share scientific ideas. Europe adopted the material considerably later, first in Spain "
           "and Italy, and the printing presses of later centuries would have been almost useless without it."),
         P("In Samarkand itself, however, the craft did not survive. As cheaper paper produced in factories became widely "
           "available, handmade sheets could no longer compete, and by the nineteenth century the local tradition had "
           "largely died out. For many years, Samarkand paper existed only in museums and old manuscripts, and few people knew exactly how it had been made."),
         P("In recent decades, craftsmen in the village of Konigil, near Samarkand, have revived the art using the bark of "
           "mulberry trees, which are common in the region because their leaves have long been used to feed silkworms. "
           "Young branches are cut, the bark is stripped and boiled for hours, and the softened fibres are beaten by a "
           "water-powered hammer. Visitors can now watch every stage and leave with a sheet of paper made much as it was "
           "centuries ago. For many, it is a rare chance to see history being made by hand."),
     ],
     [G('remarkable', 'ajoyib, eʼtiborga loyiq'), G('credit with', '… ga nisbat bermoq, … ni u qildi deb hisoblamoq'),
      G('fragment', 'parcha, boʻlak'), G('rag', 'latta'), G('pulp', 'boʻtqa, massa'),
      G('prisoner of war', 'harbiy asir'), G('treat with caution', 'ehtiyotkorlik bilan qaramoq'),
      G('gradually', 'asta-sekin'), G('reputation', 'obroʻ, nom'), G('polish', 'jilolamoq, silliqlamoq'),
      G('parchment', 'pergament (teridan qilingan yozuv materiali)'), G('adopt', 'qabul qilmoq, oʻzlashtirmoq'),
      G('compete', 'raqobatlashmoq'), G('revive', 'qayta tiklamoq'), G('mulberry', 'tut daraxti'),
      G('strip', 'shilmoq, archmoq')],
     [GN('i31-it-is-said', 'Majhul nisbat bilan xabar: are said to have taught / It is generally believed',
         'Chinese prisoners of war are said to have taught local craftsmen their skills'),
      GN('i11-past-perfect', 'Past Perfect: had largely died out',
         'by the nineteenth century the local tradition had largely died out')],
     [
         hd(2, H1, 0, 'Xatboshi C: Talas jangi haqidagi rivoyat — «Many historians treat this story with caution». '
                      '«A battle that changed trade routes» chalgʻitadi: jang tilga olinadi, lekin savdo yoʻllari oʻzgargani aytilmaydi.'),
         hd(3, H1, 1, 'Xatboshi D: Samarqand qogʻozi nega mashhur boʻlgani — silliq, mustahkam, tosh bilan jilolangan.'),
         hd(4, H1, 2, 'Xatboshi E: hunar Bagʻdod, Damashq, Qohira, Shimoliy Afrika, keyin Ispaniya va Italiyaga — gʻarbga tarqalgan.'),
         hd(6, H1, 3, 'Xatboshi G: Konigilda hunar qayta tiklangan — «have revived the art».'),
         tf('Early Chinese papermakers made paper only from fresh plant material.', 'F',
            'Aksincha: «did not rely only on fresh plants» — eski latta va baliq toʻrlari ham ishlatilgan.', 1, ng=True),
         tf('All historians accept that prisoners from the Battle of Talas brought papermaking to Samarkand.', 'F',
            '«Many historians treat this story with caution» — hamma ham qabul qilmaydi.', 2, ng=True),
         tf('Samarkand paper was sold at a higher price than paper from China.', 'NG',
            'Samarqand qogʻozining sifati maqtalgan, lekin narxini Xitoy qogʻozi bilan solishtirish yoʻq.', 3),
         tf('The use of paper made it simpler to keep official documents.', 'T',
            '«it became much easier to … keep government records» — paraphrase.', 4, ng=True),
         tf('Most of the paper made in Konigil today is sold to other countries.', 'NG',
            'Mehmonlar qogʻoz olib ketishi mumkin, lekin eksport haqida maʼlumot yoʻq.', 6),
         gap('To stop ink spreading, sheets of Samarkand paper were polished with a smooth ___.', 'stone',
             '«the sheets were often polished with a smooth stone so that ink would not spread».', 3, 1),
         gap('In Konigil, the ___ is stripped from young mulberry branches and boiled for hours.', 'bark',
             '«Young branches are cut, the bark is stripped and boiled for hours».', 6, 1),
         ch('According to the writer, why did handmade paper disappear from Samarkand?',
            ['Mulberry trees became rare in the region.', 'Cheaper factory-made paper replaced it.',
             'The city lost its supply of clean water.', 'Parchment became popular again.'], 1,
            '«As cheaper paper produced in factories became widely available, handmade sheets could no longer compete». '
            'Tut daraxti, toza suv matnda bor, lekin sabab sifatida emas.', 5),
         ch('Why are mulberry trees common around Samarkand?',
            ['Their bark has always been used for paper.', 'Their leaves are used to feed silkworms.',
             'They grow well beside canals.'], 1,
            '«because their leaves have long been used to feed silkworms». Qogʻoz uchun poʻstloq yaqinda qayta ishlatila boshlangan.', 6),
     ])


# ---------------------------------------------------------------- 2-test
H2 = ['Three parts of a repeating cycle', 'Why self-control is not enough', 'Building on what you already do',
      'Ways to weaken unwanted habits', 'The exact time a habit needs', 'How the brain stores memories']

text(B, 'b2-27-test2', '2-test: Odatlar ilmi', 'The Science of Habits', 'B2', 'exam',
     L('Psixologiya', 'Psychology'), intro('odatlar qanday shakllanishi haqidagi ilmiy-ommabop matn.'),
     [
         P("Think about the first hour of your day. You probably brushed your teeth, made a drink and checked your phone "
           "without really deciding to do any of these things. Psychologists believe that a considerable part of everyday "
           "behaviour works in this way. Rather than being the result of careful choices, many of our actions are habits, "
           "performed almost automatically and often without our full awareness. This is not necessarily a bad thing."),
         P("Researchers often describe a habit as a loop made up of three parts. First comes a cue, a signal that triggers "
           "the behaviour, such as a particular time, place or feeling. Next is the routine, which is the behaviour itself. "
           "Finally, there is a reward, something pleasant that makes the brain more likely to repeat the loop. When a "
           "phone vibrates, for example, the sound acts as a cue, picking up the phone is the routine, and the small "
           "satisfaction of a new message is the reward."),
         P("Habits appear to form through repetition in a stable context. Each time a cue is followed by the same action "
           "and a reward, the connection between them grows stronger, until the behaviour requires very little conscious "
           "thought. This has a clear advantage, because it frees attention for other tasks. How long the process takes, "
           "however, is far from certain. The popular claim that any habit forms in exactly three weeks is probably an "
           "oversimplification, since the time seems to vary greatly between people and between behaviours."),
         P("Many people who want to change their lives rely on willpower. Unfortunately, self-control is not always "
           "dependable. Some psychologists have argued that it works like a limited resource which becomes weaker as the day "
           "goes on, although this idea remains controversial and later research has not always supported it. Whatever "
           "the explanation, people who seem highly disciplined often depend less on willpower than others imagine. "
           "Instead, they tend to organise their surroundings so that temptation rarely appears."),
         P("One practical strategy is known as habit stacking. Instead of trying to create a new habit from nothing, a "
           "person attaches it to something they already do every day. A simple plan might be: after I pour my morning "
           "tea, I will read one page of a book. Because the existing habit is already firmly established, it can serve as "
           "a reliable cue for the new behaviour. The more specific the plan, the easier it tends to be to follow."),
         P("Breaking a bad habit is often harder than starting a good one. Some experts recommend keeping the cue and the "
           "reward but changing the routine in between, for instance going for a short walk instead of reaching for a "
           "snack when feeling stressed. It also helps to make cues for unwanted habits less visible and to make good habits "
           "as easy as possible. Someone who wants to exercise in the morning might leave their sports clothes next to the "
           "bed the night before."),
         P("None of this means that change happens overnight. Building a habit is usually a slow process, and progress is "
           "rarely smooth. Encouragingly, missing a single day does not seem to undo the effort that has already been made. "
           "What matters most, it appears, is returning to the routine rather than giving up after one mistake. Small, realistic steps are generally more successful than dramatic promises."),
     ],
     [G('considerable', 'katta, salmoqli'), G('awareness', 'ongli his, xabardorlik'), G('cue', 'signal, turtki'),
      G('trigger', 'qoʻzgʻatmoq, boshlab bermoq'), G('routine', 'odatiy harakat, tartib'), G('reward', 'mukofot'),
      G('repetition', 'takrorlash'), G('conscious', 'ongli'), G('oversimplification', 'haddan tashqari soddalashtirish'),
      G('willpower', 'iroda kuchi'), G('dependable', 'ishonchli'), G('controversial', 'bahsli'),
      G('temptation', 'vasvasa, nafsni qoʻzgʻatadigan narsa'), G('attach', 'biriktirmoq, bogʻlamoq'),
      G('establish', 'mustahkamlamoq, oʻrnatmoq'), G('undo', 'yoʻqqa chiqarmoq, bekor qilmoq')],
     [GN('i29-passive-basics', 'Majhul nisbat: is known as, is followed by',
         'Each time a cue is followed by the same action'),
      GN('i56-ing-ed-clauses', 'Sifatdoshli (-ed) qisqartirilgan ergash gap: performed almost automatically',
         'many of our actions are habits, performed almost automatically')],
     [
         hd(1, H2, 0, 'Xatboshi B: odat — cue, routine, reward dan iborat takrorlanuvchi halqa.'),
         hd(3, H2, 1, 'Xatboshi D: iroda kuchiga tayanish ishonchli emas — «self-control is not always dependable».'),
         hd(4, H2, 2, 'Xatboshi E: habit stacking — yangi odatni mavjud odatga biriktirish.'),
         hd(5, H2, 3, 'Xatboshi F: yomon odatni zaiflashtirish yoʻllari — oʻrtadagi harakatni almashtirish, signallarni koʻzdan yashirish. '
                      '«The exact time a habit needs» chalgʻitadi: C xatboshida aniq muddat yoʻqligi aytilgan.'),
         tf('According to the writer, people are usually fully conscious of every habitual action.', 'F',
            '«often without our full awareness» — doim ham anglamaymiz.', 0, ng=True),
         tf('The belief that every habit takes three weeks to form is probably too simple.', 'T',
            '«is probably an oversimplification» — paraphrase.', 2, ng=True),
         tf('Scientists now agree that willpower runs out like fuel during the day.', 'F',
            '«this idea remains controversial and later research has not always supported it» — kelishuv yoʻq.', 3, ng=True),
         tf('Habit stacking was first developed by professional sports coaches.', 'NG',
            'Usul nima ekani tushuntirilgan, lekin kim oʻylab topgani aytilmagan.', 4),
         gap('In the habit loop, the ___ is the signal that starts the behaviour.', 'cue',
             '«First comes a cue, a signal that triggers the behaviour».', 1, 1),
         gap('Disciplined people often arrange their ___ so that they are rarely tempted.', 'surroundings',
             '«they tend to organise their surroundings so that temptation rarely appears».', 3, 1),
         gap('Missing a single ___ does not seem to cancel earlier progress.', 'day',
             '«missing a single day does not seem to undo the effort».', 6, 1),
         ch('Why does the writer mention leaving sports clothes next to the bed?',
            ['to show how a good habit can be made easier', 'to describe a reward for exercising',
             'to warn about cues for bad habits', 'to show how willpower becomes weaker'], 0,
            '«to make good habits as easy as possible» jumlasidan keyin misol sifatida keltirilgan.', 5),
         ch('What is the main message of the final paragraph?',
            ['Habits change quickly if the plan is good.', 'One mistake means a person must start again.',
             'Continuing after a setback matters more than being perfect.'], 2,
            '«What matters most … is returning to the routine rather than giving up after one mistake».', 6),
     ])


# ---------------------------------------------------------------- 3-test
H3 = ['Signs of retreat in a warming climate', 'A temporary gain that may not last',
      'Risks for farms, power and neighbours', 'Measuring ice in difficult places',
      'Why the deserts are getting wetter', 'New glaciers forming in the Pamir']

text(B, 'b2-28-test3', '3-test: Togʻ muzliklari', 'Mountain Glaciers of Central Asia', 'B2', 'exam',
     L('Atrof-muhit', 'Environment'), intro('Markaziy Osiyo togʻ muzliklari va suv taqdiri haqidagi matn.'),
     [
         P("Much of Central Asia is dry, with long hot summers and little rain on the plains. Yet great rivers manage to flow "
           "through its deserts, supporting farms and cities along their banks. The secret lies high in the mountains of "
           "the Tian Shan and the Pamir, where thousands of glaciers store enormous quantities of frozen water. For millions of people in the lowlands, the condition of these distant glaciers is therefore a matter of daily importance."),
         P("Glaciers act as natural water towers. In winter, snow builds up on the high slopes and, over many years, is "
           "pressed into dense ice. In summer, part of this ice melts, releasing water precisely in the hot, dry months when "
           "farmers downstream need it most for irrigation. The Amu Darya draws much of its water from the Pamir and "
           "neighbouring ranges, while the Syr Darya is fed mainly by the Tian Shan."),
         P("Scientists who study the region report that many of these glaciers have become smaller and thinner in recent "
           "decades as average temperatures have risen. The change is not the same everywhere. Small glaciers at lower "
           "altitudes appear to be the most vulnerable, and some of them are thought to have disappeared completely, "
           "while certain larger glaciers at higher elevations have changed more slowly. Shrinking glaciers are often described as one of the clearest visible signs of a warming climate."),
         P("At first, this loss of ice can seem to bring good news. As glaciers melt faster, rivers may carry more water than "
           "before, and some farmers may notice little difference. Researchers warn, however, that this increase is likely "
           "to be temporary. Once a glacier has shrunk beyond a certain point, there is simply less ice left to melt, and "
           "summer flow may eventually decline. Exactly when this turning point will arrive in each river basin is still "
           "uncertain."),
         P("The possible consequences are serious. Agriculture in the lowlands depends heavily on summer meltwater, and "
           "countries upstream rely on the same rivers to generate hydroelectric power. Because upstream countries tend to "
           "need water for electricity in winter, while downstream farmers need it in summer, sharing the rivers has long "
           "required careful negotiation. Melting ice can also create new lakes held back by unstable walls of ice or rock, "
           "and if these walls fail, sudden floods may threaten villages in the valleys below."),
         P("Keeping track of these changes is far from easy. Many glaciers lie in remote areas at great heights, where the "
           "weather is harsh and the working season is short. Researchers therefore combine satellite images with "
           "measurements taken on the ground. In some places, they drill stakes into the ice to record how much melts each "
           "year, and they install weather stations nearby. Sharing such data between neighbouring countries is widely seen "
           "as essential."),
         P("Local action cannot stop glaciers from melting, since that depends largely on global temperatures. However, it "
           "can soften the effects. Repairing leaking canals, adopting more efficient irrigation methods and planning water "
           "use more carefully could help the region cope with whatever the mountains provide in the future. Education also plays a part, since farmers who understand the changes are more likely to try new methods."),
     ],
     [G('glacier', 'muzlik'), G('enormous', 'ulkan'), G('irrigation', 'sugʻorish'), G('downstream', 'quyi oqimda (daryoning)'),
      G('altitude', 'balandlik (dengiz sathidan)'), G('vulnerable', 'zaif, xavf ostidagi'),
      G('elevation', 'balandlik'), G('temporary', 'vaqtinchalik'), G('shrink', 'kichraymoq'),
      G('decline', 'kamaymoq, pasaymoq'), G('basin', 'havza'), G('hydroelectric', 'gidroelektr'),
      G('negotiation', 'muzokara'), G('unstable', 'beqaror, mustahkam boʻlmagan'), G('remote', 'olis, chekka'),
      G('cope with', 'uddalamoq, bardosh bermoq')],
     [GN('i31-it-is-said', 'Majhul nisbat bilan xabar: are thought to have disappeared',
         'some of them are thought to have disappeared completely'),
      GN('i16-future-time-clauses', 'Once + Present Perfect: vaqt ergash gapi',
         'Once a glacier has shrunk beyond a certain point')],
     [
         hd(2, H3, 0, 'Xatboshi C: harorat koʻtarilishi bilan muzliklar kichraymoqda — chekinish belgilari.'),
         hd(3, H3, 1, 'Xatboshi D: suvning koʻpayishi vaqtinchalik — «this increase is likely to be temporary».'),
         hd(4, H3, 2, 'Xatboshi E: dehqonchilik, gidroelektr va qoʻshni davlatlar oʻrtasida suv taqsimoti, toshqin xavfi.'),
         hd(5, H3, 3, 'Xatboshi F: olis, baland joylarda muzni oʻlchash — sunʼiy yoʻldosh va yerdagi oʻlchovlar. '
                      '«New glaciers forming in the Pamir» — matnda yangi muzliklar haqida gap yoʻq.'),
         tf('Glaciers release water at the time of year when it is most needed for farming.', 'T',
            '«releasing water precisely in the hot, dry months when farmers downstream need it most».', 1, ng=True),
         tf('The Syr Darya depends mainly on glaciers in the Pamir.', 'F',
            '«the Syr Darya is fed mainly by the Tian Shan» — Pomir emas.', 1, ng=True),
         tf('Small glaciers at lower altitudes seem to be more at risk than large glaciers higher up.', 'T',
            '«Small glaciers at lower altitudes appear to be the most vulnerable … certain larger glaciers at higher elevations have changed more slowly».', 2, ng=True),
         tf('Faster melting will permanently increase the amount of water in the rivers.', 'F',
            '«this increase is likely to be temporary … summer flow may eventually decline».', 3, ng=True),
         tf('The countries of the region recently signed a treaty on glacier research.', 'NG',
            'Maʼlumot almashish muhimligi aytilgan, lekin shartnoma haqida hech narsa yoʻq.', 5),
         gap('Melting ice can form new ___ that are held back by unstable walls of ice or rock.', 'lakes',
             '«Melting ice can also create new lakes held back by unstable walls».', 4, 1),
         gap('To record yearly melting, researchers drill ___ into the ice.', 'stakes',
             '«they drill stakes into the ice to record how much melts each year».', 5, 1),
         ch('Why has sharing the rivers required careful negotiation?',
            ['Upstream and downstream countries need the water at different times of year.',
             'The rivers change their direction every summer.',
             'Hydroelectric stations use up most of the water.'], 0,
            'Yuqori oqimdagilar suvni qishda elektr uchun, quyidagilar yozda dehqonchilik uchun talab qiladi.', 4),
         ch('What is the writer\'s main point in the last paragraph?',
            ['Local efforts can stop glaciers from melting.',
             'Better water management can reduce the impact of glacier loss.',
             'New canals should be built in the mountains.',
             'Global temperatures are no longer rising.'], 1,
            '«Local action cannot stop glaciers from melting … However, it can soften the effects».', 6),
     ])


# ---------------------------------------------------------------- 4-test
H4 = ['Making use of empty roofs', 'Farming without soil or sunlight', 'An old local tradition on a shared scale',
      'Why the enthusiasm has limits', 'Growing grain in city centres', 'How neighbours share the cost of energy']

text(B, 'b2-29-test4', '4-test: Shahar dehqonchiligi', 'Farming in the City', 'B2', 'exam',
     L('Shahar va jamiyat', 'Cities and society'), intro('shaharlar ichida oziq-ovqat yetishtirish haqidagi matn.'),
     [
         P("As cities grow, the distance between the people who eat food and the places where it is grown keeps increasing. "
           "Fruit and vegetables often travel long distances before they reach a shop. In response, a growing number of "
           "residents, businesses and local authorities are experimenting with urban farming, the practice of producing "
           "food within the city itself. Supporters believe that growing food closer to home could reduce transport, provide fresher produce and reconnect city dwellers with nature."),
         P("One of the most visible forms is the rooftop garden. Many buildings have flat roofs that are used for nothing at "
           "all, and these can be covered with raised beds or containers of soil. Supporters point out that such gardens do "
           "more than produce vegetables. A layer of plants can help keep the building beneath cooler in summer and can "
           "absorb some of the rainwater that would otherwise rush into drains. Before a garden is created, however, "
           "engineers should check whether the roof can carry the extra weight of wet soil."),
         P("A more technological approach is the vertical farm. Here, crops are grown indoors on shelves stacked one above "
           "another, under artificial lights. Instead of soil, the roots receive water containing nutrients, and the "
           "conditions can be controlled so carefully that harvests are possible all year round. Such farms often use "
           "much less water than open fields. Their main weakness is cost, since lighting and climate control consume a "
           "great deal of electricity. For this reason, they mostly grow leafy greens and herbs rather than staple crops."),
         P("Community gardens take a simpler and more social form. A piece of unused land is divided into small plots, and "
           "local people grow whatever they like. Gardeners often say that the friendships formed over the fence are as "
           "valuable as the tomatoes, and children who take part learn where their food actually comes from. Such gardens can also turn neglected corners of a neighbourhood into pleasant green spaces."),
         P("In Uzbekistan, this idea is hardly new. Traditional courtyard houses have long had grapevines, apricot trees and "
           "small vegetable beds, and many families still grow part of their own food. Some mahallas are now applying the "
           "same tradition on a shared scale, planting fruit trees and vegetables on unused land near schools or apartment "
           "blocks. Such projects are often carried out through hashar, the custom of neighbours working together "
           "voluntarily for the common good."),
         P("Despite the enthusiasm, urban farming has clear limits. Land in cities is expensive, and developers usually "
           "prefer to build on it. Soil in former industrial areas may be polluted, so it needs testing before anything "
           "edible is planted. Most importantly, city farms produce only a small share of what urban populations eat, and "
           "some critics argue that they are closer to a hobby than a real solution. Growing food in a small space also requires time and knowledge, which not every resident has."),
         P("Even so, it would be a mistake to judge urban farming only by the amount of food it produces. It can bring "
           "neighbours together, make cities greener and teach young people valuable skills. Rather than replacing rural "
           "agriculture, it is perhaps best understood as a useful addition to it."),
     ],
     [G('resident', 'aholi, yashovchi'), G('local authorities', 'mahalliy hokimiyat'), G('rooftop', 'tom usti'),
      G('raised bed', 'baland pushta (hoshiyali koʻtarma egat)'), G('absorb', 'shimmoq'), G('drain', 'yomgʻir suvi quvuri, drenaj'),
      G('artificial', 'sunʼiy'), G('nutrient', 'ozuqa moddasi'), G('harvest', 'hosil'), G('consume', 'sarflamoq, isteʼmol qilmoq'),
      G('staple crop', 'asosiy ekin (bugʻdoy, guruch kabi)'), G('plot', 'yer uchastkasi, boʻlak'),
      G('voluntarily', 'ixtiyoriy ravishda'), G('enthusiasm', 'ishtiyoq'), G('edible', 'yeyiladigan'),
      G('critic', 'tanqidchi')],
     [GN('i64-so-that-in-order-to', 'so … that: natija', 'the conditions can be controlled so carefully that harvests are possible all year round'),
      GN('i29-passive-basics', 'Majhul nisbat: are grown, is divided',
         'A piece of unused land is divided into small plots')],
     [
         hd(1, H4, 0, 'Xatboshi B: boʻsh tekis tomlardan bogʻ sifatida foydalanish.'),
         hd(2, H4, 1, 'Xatboshi C: vertikal fermalar — tuproq oʻrniga ozuqali suv, quyosh oʻrniga sunʼiy chiroq. '
                      '«Growing grain in city centres» chalgʻitadi: aksincha, asosiy ekinlar yetishtirilmaydi.'),
         hd(4, H4, 2, 'Xatboshi E: hovli bogʻlari va hashar — eski anʼana endi mahalla miqyosida.'),
         hd(5, H4, 3, 'Xatboshi F: «Despite the enthusiasm, urban farming has clear limits».'),
         tf('Rooftop gardens can help to lower the temperature of the building below them in summer.', 'T',
            '«can help keep the building beneath cooler in summer».', 1, ng=True),
         tf('Vertical farms are mainly used to grow crops such as wheat and rice.', 'F',
            '«they mostly grow leafy greens and herbs rather than staple crops».', 2, ng=True),
         tf('Most community gardens are managed by local authorities.', 'NG',
            'Jamoat bogʻlari tasvirlangan, lekin ularni kim boshqarishi aytilmagan (hokimiyat faqat A xatboshida umumiy tilga olinadi).', 3),
         tf('People who take part in hashar are paid for their work.', 'F',
            '«neighbours working together voluntarily» — ixtiyoriy, haq toʻlanmaydi.', 4, ng=True),
         gap('Before a roof garden is built, ___ should check that the roof can hold the weight.', 'engineers',
             '«engineers should check whether the roof can carry the extra weight».', 1, 1),
         gap('In vertical farms, roots get water that contains ___.', 'nutrients',
             '«the roots receive water containing nutrients».', 2, 1),
         gap('Soil in former industrial areas may need ___ before food is planted in it.', 'testing',
             '«so it needs testing before anything edible is planted».', 5, 1),
         ch('What is the main disadvantage of vertical farms, according to the text?',
            ['They need a lot of water.', 'They can only produce food in summer.',
             'They use large amounts of electricity.', 'They take up valuable land.'], 2,
            '«lighting and climate control consume a great deal of electricity». Suv aksincha kam ishlatiladi.', 2),
         ch('Which statement best reflects the writer\'s conclusion?',
            ['Urban farming should replace farming in the countryside.',
             'Urban farming is only a hobby with no real value.',
             'Urban farming is valuable as a complement to rural agriculture.'], 2,
            '«Rather than replacing rural agriculture, it is perhaps best understood as a useful addition to it». '
            '«hobby» fikri tanqidchilarniki, muallifniki emas.', 6),
     ])


# ---------------------------------------------------------------- 5-test
H5 = ['The advantage of speed', 'Why slower may be better', 'An art of patience', 'Practical strengths beyond note-taking',
      'The end of handwriting in schools', 'Teaching children to type']

text(B, 'b2-30-test5', '5-test: Qoʻlda yozish kuchi', 'The Power of Handwriting', 'B2', 'exam',
     L('Taʼlim', 'Education'), intro('qoʻlda yozish va klaviaturada yozishning oʻqishga taʼsiri haqidagi matn.'),
     [
         P("In many classrooms and lecture halls, the sound of pens on paper is being replaced by the quiet tapping of "
           "keyboards. Students take notes on laptops, teachers set assignments online, and some schools spend less time "
           "than before teaching children to write neatly. This shift raises an interesting question: does it matter "
           "whether we learn with a pen or a keyboard? For teachers and parents alike, the answer has practical consequences."),
         P("At first sight, the keyboard seems to win easily. Most people type considerably faster than they can write by "
           "hand, so students using laptops can record far more of what a lecturer says. Some are able to produce notes "
           "that are almost a word-for-word copy of the lecture. For anyone who fears missing an important detail, this "
           "can feel reassuring. Typed notes are also easier to read later than hurried handwriting."),
         P("Yet some researchers suggest that this speed may come at a price. Because writing by hand is slower, students "
           "cannot write down everything they hear. Instead, they are forced to listen, select the key points and summarise "
           "ideas in their own words. According to this view, it is precisely this extra mental effort that helps "
           "information to be understood and remembered. Not every study has reached the same conclusion, however, and "
           "the debate is far from settled."),
         P("A related line of research concerns young children. Some experts believe that forming letters by hand helps "
           "children to recognise them more easily, perhaps because the movement of the hand gives the brain an additional "
           "way of storing the shape of each letter. How strong this effect is, and whether it lasts into adulthood, "
           "remains a matter of discussion. Even so, many teachers of young pupils still consider handwriting practice an important part of early education."),
         P("In Central Asia, the value of careful writing has long been recognised. In cities such as Samarkand and Bukhara, "
           "skilled calligraphers copied manuscripts with a pen cut from reed, and their work was admired as a form of art. Beautifully written books were often decorated with fine patterns and treasured by their owners for generations. "
           "Training usually lasted many years, and students were expected to develop not only a steady hand but also "
           "patience and deep concentration. Calligraphy is still taught in Uzbekistan today, and many people see it as "
           "an important part of the national heritage."),
         P("None of this means that keyboards are harmful. Typed work is easy to edit, share and search, which saves a "
           "great deal of time when writing long essays or reports. For students who find handwriting physically difficult, "
           "a keyboard can make learning far more accessible. In many modern jobs, fast and accurate typing is simply an "
           "essential skill."),
         P("The most sensible conclusion may be that each tool suits different purposes. When the goal is to understand and "
           "remember new material, writing by hand could be worth the extra time. When the task involves long drafts, "
           "frequent changes or collaboration, a keyboard is likely to be more practical. Rather than choosing one and "
           "abandoning the other, learners may benefit most from knowing when to use each."),
     ],
     [G('assignment', 'topshiriq, vazifa'), G('shift', 'oʻzgarish, siljish'), G('considerably', 'ancha, sezilarli darajada'),
      G('reassuring', 'xotirjam qiladigan'), G('summarise', 'qisqacha bayon qilmoq'), G('settled', 'hal boʻlgan'),
      G('recognise', 'tanimoq, eʼtirof etmoq'), G('adulthood', 'kattalik davri'), G('manuscript', 'qoʻlyozma'),
      G('reed', 'qamish'), G('concentration', 'diqqatni jamlash'), G('heritage', 'meros'),
      G('accessible', 'qulay, foydalanish mumkin boʻlgan'), G('collaboration', 'hamkorlik'),
      G('abandon', 'voz kechmoq, tashlab ketmoq')],
     [GN('i30-passive-tenses', 'Majhul nisbat (Present Continuous): is being replaced',
         'the sound of pens on paper is being replaced by the quiet tapping of keyboards'),
      GN('c57-cleft-sentences', 'Taʼkidli gap: it is … that',
         'it is precisely this extra mental effort that helps information to be understood and remembered')],
     [
         hd(1, H5, 0, 'Xatboshi B: klaviatura tezroq — koʻproq yozib olish mumkin.'),
         hd(2, H5, 1, 'Xatboshi C: sekin yozish tanlash va oʻz soʻzi bilan ifodalashga majbur qiladi — bu oʻrganishga yordam berishi mumkin.'),
         hd(4, H5, 2, 'Xatboshi E: xattotlik — yillab oʻqish, sabr va diqqat talab qiladigan sanʼat.'),
         hd(5, H5, 3, 'Xatboshi F: klaviaturaning konspektdan tashqari afzalliklari — tahrir, ulashish, qidirish, qulaylik, kasbiy koʻnikma. '
                      '«The end of handwriting in schools» chalgʻitadi: A xatboshida faqat kamroq vaqt ajratilishi aytilgan.'),
         tf('Students who type their notes can usually record more of a lecture.', 'T',
            '«students using laptops can record far more of what a lecturer says».', 1, ng=True),
         tf('All studies agree that taking notes by hand helps students remember more.', 'F',
            '«Not every study has reached the same conclusion» — demak, hamma tadqiqotlar bir xil xulosaga kelmagan.', 2, ng=True),
         tf('Calligraphers in the past usually trained for only a few months.', 'F',
            '«Training usually lasted many years».', 4, ng=True),
         tf('Most universities in Uzbekistan now require exams to be written by hand.', 'NG',
            'Xattotlik oʻqitilishi aytilgan, imtihonlar haqida maʼlumot yoʻq.', 4),
         tf('A keyboard can make learning easier for students who struggle physically with handwriting.', 'T',
            '«a keyboard can make learning far more accessible» — paraphrase.', 5, ng=True),
         gap('Traditional calligraphers wrote with a pen cut from ___.', 'reed',
             '«with a pen cut from reed».', 4, 1),
         gap('Writing by hand forces students to ___ ideas in their own words.', ['summarise', 'summarize'],
             '«they are forced to … summarise ideas in their own words».', 2, 1),
         ch('What does the writer say about the effect of handwriting on young children?',
            ['It has been shown to last into adulthood.', 'It may help them recognise letters.',
             'It makes them write faster than adults.'], 1,
            '«forming letters by hand helps children to recognise them more easily» — lekin kattalikda saqlanishi hali bahsli.', 3),
         ch('What is the writer\'s overall opinion?',
            ['Keyboards should be removed from classrooms.', 'Handwriting is no longer a useful skill.',
             'Learners should choose the tool that suits the task.', 'Calligraphy should replace typing in schools.'], 2,
            '«each tool suits different purposes … knowing when to use each».', 6),
     ])
