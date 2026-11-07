"""B2 · 1-boʻlim (davomi): Topshiriq turlari bilan tanishuv — summary completion, multiple choice, aralash"""
from lib import *

B = 'b2'

# ---------------------------------------------------------------- b2-03 silkworm
SUM_INTRO = ('Topshiriq: Summary completion (xulosani toʻldirish). Boʻshliqlarga matndan aynan olingan soʻz yozing — '
             'NO MORE THAN ONE / TWO WORDS. Maslahat: avval boʻshliq atrofidagi soʻzlarga qarab qanday soʻz kerakligini '
             '(ot, feʼl, sifat) aniqlang; xulosadagi jumlalar odatda matn tartibida keladi.')

text(B, 'b2-03-silkworm', 'Ipak qurti', 'The Silkworm: From Leaf to Fabric', 'B2', 'exam',
     L('Hunarmandchilik', 'Crafts'), SUM_INTRO,
     [
         P("Few fabrics have a history as long or as glamorous as silk. For thousands of years it has been associated with "
           "wealth and beauty, and the trade routes that once linked China with the Mediterranean are known today as the Silk "
           "Road. What many people do not realise, however, is that this luxurious material begins its life inside a small "
           "and rather unremarkable insect."),
         P("The silkworm is not actually a worm but the caterpillar of a moth. It has an extremely limited diet: it feeds "
           "almost exclusively on the leaves of the mulberry tree. After hatching from tiny eggs, the caterpillars eat almost "
           "constantly and grow remarkably fast. Over roughly a month, they increase in size many times over, shedding their "
           "skin several times as they grow."),
         P("When it is fully grown, the caterpillar stops eating and begins to spin a cocoon around itself. It produces a "
           "liquid in special glands which hardens into a fine thread as it leaves the insect's body. Moving its head in a "
           "repeated figure-of-eight pattern, the insect wraps itself in a single continuous filament that may be hundreds of "
           "metres long. Inside this protective shell, it slowly transforms into a moth."),
         P("If the moth were allowed to emerge, it would break the thread, so silk producers do not wait. Instead, the "
           "cocoons are heated, typically with steam, hot air or boiling water. The heat also softens the natural gum "
           "that holds the filament together, making it possible to find the end of the thread and unwind it. Because a single "
           "filament is too thin to use on its own, several are reeled together to form one strong thread, which can then be "
           "dyed and woven."),
         P("In Uzbekistan, this craft has deep roots. The Fergana Valley has been a centre of silk production for centuries, "
           "and in many villages families still raise silkworms each spring, collecting fresh mulberry leaves several times a "
           "day. The work is demanding, but the cocoons provide a valuable source of income, and the country is often "
           "described as one of the world's major cocoon producers."),
         P("The town of Margilan is particularly famous for its weavers. Here, craftspeople produce khan-atlas, a shiny silk "
           "fabric decorated with bold, slightly blurred patterns. The effect is created using a technique in which bundles of "
           "threads are tied and dyed before weaving, so the design appears gradually as the cloth is made. Visitors can watch "
           "every stage of the process in local workshops, and the fabric remains popular for traditional dresses as well as "
           "modern fashion."),
     ],
     [G('glamorous', 'jozibali, hashamatli'), G('luxurious', 'hashamatli, qimmatbaho'), G('caterpillar', 'kapalak qurti, lichinka'),
      G('diet', 'ozuqa, ratsion'), G('exclusively', 'faqat, mutlaqo'), G('hatch', '(tuxumdan) chiqmoq'),
      G('shed (skin)', 'poʻst tashlamoq'), G('gland', 'bez'), G('filament', 'ingichka tola'),
      G('transform into', '… ga aylanmoq'), G('emerge', 'chiqmoq, paydo boʻlmoq'), G('unwind', '(ipni) yechmoq, chuvamoq'),
      G('reel', 'gʻaltakka oʻramoq; pilla chuvamoq'), G('demanding', 'mashaqqatli, koʻp kuch talab qiladigan'),
      G('bundle', 'dasta, toʻp'), G('dye', 'boʻyamoq')],
     [GN('i26-second-conditional', 'Ikkinchi shart: If … were …, it would …',
         'If the moth were allowed to emerge, it would break the thread'),
      GN('i29-passive-basics', 'Majhul nisbat: are heated, are reeled', 'the cocoons are heated')],
     [
         gap('Summary: The silkworm is in fact the caterpillar of a ___.', 'moth',
             '2-xatboshi: «not actually a worm but the caterpillar of a moth».', 1, 1),
         gap('It eats almost nothing except the leaves of the ___.', ['mulberry tree', 'mulberry'],
             '«feeds almost exclusively on the leaves of the mulberry tree» — «almost nothing except» = «almost exclusively».', 1, 2),
         gap('When it has finished growing, it spins a ___ around its body.', 'cocoon',
             '3-xatboshi: «begins to spin a cocoon around itself».', 2, 1),
         gap('This shell consists of one ___ filament, which can be hundreds of metres long.', 'continuous',
             '«a single continuous filament that may be hundreds of metres long». Xulosadagi «one» matndagi «single» oʻrnida '
             'turibdi, shuning uchun boʻshliqqa «continuous» kerak.', 2, 1),
         gap('Producers heat the cocoons, which also softens the natural ___ holding the filament together.', 'gum',
             '4-xatboshi: «softens the natural gum that holds the filament together».', 3, 1),
         gap('Since one filament is too thin, several are ___ together to make a strong thread.', 'reeled',
             '«several are reeled together to form one strong thread». «dyed» va «woven» keyingi bosqichlarga tegishli.', 3, 1),
         tf('The liquid produced by the silkworm turns solid once it is outside the insect\'s body.', 'T',
            '3-xatboshi: «hardens into a fine thread as it leaves the insect\'s body» — «hardens» = «turns solid».', 2, ng=True),
         tf('Raising silkworms requires little effort from village families.', 'F',
            '5-xatboshi: «The work is demanding» — mehnat talab qiladi, demak «little effort» notoʻgʻri.', 4, ng=True),
         tf('Most of the silk woven in Margilan is sold to other countries.', 'NG',
            '6-xatboshida Margʻilon toʻquvchilari va xon-atlas haqida gap bor, lekin mato qayerga sotilishi aytilmagan.', 5),
         ch('How are the patterns of khan-atlas created?',
            ['by painting designs onto the finished cloth', 'by tying and dyeing bundles of thread before weaving',
             'by weaving threads of different thickness', 'by heating the cloth in boiling water'], 1,
            '6-xatboshi: «bundles of threads are tied and dyed before weaving». Qaynoq suv pillaga ishlatiladi, matoga emas; '
            'naqsh tayyor matoga chizilmaydi.', 5),
     ])

# ---------------------------------------------------------------- b2-04 online learning
MC_INTRO = ('Topshiriq: Multiple choice. Har bir savol uchun bitta toʻgʻri javobni tanlang. Maslahat: avval savolni oʻqib, '
            'matndan kerakli joyni toping, keyin har bir variantni matn bilan solishtiring — matndagi soʻzlarni aynan '
            'takrorlagan variant koʻpincha tuzoq boʻladi. Muallif fikri haqidagi savollarda «yet», «however», «then» '
            'kabi soʻzlarga eʼtibor bering.')

text(B, 'b2-04-online-learning', 'Masofaviy taʼlim', 'Online Learning: Promise and Limits', 'B2', 'exam',
     L('Taʼlim', 'Education'), MC_INTRO,
     [
         P("Not long ago, studying for a degree meant moving to a university town, attending lectures in person and "
           "borrowing books from a library. Today, a student in a small village can follow a course taught hundreds of "
           "kilometres away, watch recorded lectures at midnight and submit assignments without leaving home. Distance "
           "learning is hardly new, since courses by post existed long before the internet, but digital technology has "
           "transformed both its scale and its reputation."),
         P("The most obvious advantage is access. Online courses can reach people who would otherwise be excluded from "
           "education: those living far from cities, parents with young children, people with disabilities and adults who "
           "need to keep working while they study. Flexibility is another attraction. Learners can usually choose when to "
           "study, replay difficult explanations as many times as they need and move faster through material they already "
           "understand."),
         P("Yet flexibility comes at a price. Without a fixed timetable and a teacher in the room, it is surprisingly easy to "
           "fall behind. Many teachers report that the students who do well online are those who are already organised and "
           "motivated, while those who struggle with self-discipline may quietly drop out. In other words, the freedom that "
           "makes online study attractive can also make it fragile."),
         P("There are practical limits, too. A reliable internet connection and a suitable device are still not available to "
           "everyone, and studying on a small phone screen for hours is tiring. Some subjects are also harder to teach at a "
           "distance. A chemistry student needs a laboratory, and a future surgeon or mechanic needs hands-on practice that no "
           "video can fully replace. Even in theoretical subjects, something is lost when discussion happens only in written "
           "comments rather than in face-to-face conversation."),
         P("For these reasons, many educators now favour blended learning, which combines online and classroom study. In a "
           "typical blended course, students might watch short lectures and complete exercises at home, then use class time "
           "for discussion, group projects and practical work. Supporters argue that this approach makes better use of the "
           "teacher, who spends less time repeating information and more time responding to students' questions."),
         P("It would be a mistake, then, to see online learning either as a miracle or as a second-rate substitute for "
           "traditional education. Its value depends largely on how a course is designed and on who is using it. A "
           "well-planned course with regular deadlines, active tasks and contact with a tutor can be highly effective, whereas "
           "a collection of uploaded videos rarely is. The real question is not whether to study online, but how to do it well."),
     ],
     [G('submit', 'topshirmoq'), G('assignment', 'vazifa, topshiriq'), G('transform', 'tubdan oʻzgartirmoq'),
      G('reputation', 'obroʻ, nom'), G('access', 'foydalanish imkoniyati'), G('exclude', 'chetlatmoq, chetda qoldirmoq'),
      G('flexibility', 'moslashuvchanlik'), G('timetable', 'dars jadvali'), G('self-discipline', 'oʻzini oʻzi intizomga sola olish'),
      G('drop out', '(oʻqishni) tashlab ketmoq'), G('fragile', 'moʻrt, oson buziladigan'), G('reliable', 'ishonchli'),
      G('hands-on', 'amaliy'), G('blended learning', 'aralash (onlayn + sinf) taʼlim'),
      G('substitute', 'oʻrnini bosuvchi narsa'), G('deadline', 'muddat, oxirgi sana')],
     [GN('c52-but-for-otherwise', 'otherwise: aks holda', 'people who would otherwise be excluded from education'),
      GN('i53-who-which-that', 'Nisbiy olmosh: those who …',
         'the students who do well online are those who are already organised and motivated')],
     [
         ch('What is the main purpose of the passage?',
            ['to persuade readers to choose online courses', 'to give a balanced view of the strengths and weaknesses of online learning',
             'to describe the history of distance learning', 'to prove that online learning cannot replace classrooms'], 1,
            'Muallif afzalliklar (B), kamchiliklar (C, D) va yechim (E)ni koʻrsatib, «It would be a mistake … to see online '
            'learning either as a miracle or as a second-rate substitute» degan muvozanatli xulosaga keladi. Tarix faqat A xatboshida qisqa tilga olingan.', 5),
         ch('According to the writer, what has digital technology changed about distance learning?',
            ['It has created distance learning for the first time.', 'It has changed how widely it is used and how it is viewed.',
             'It has made library books unnecessary.', 'It has made courses by post more popular.'], 1,
            '«transformed both its scale and its reputation» — koʻlami va obroʻsi. Birinchi variant notoʻgʻri: '
            '«courses by post existed long before the internet».', 0),
         ch('Which group is NOT mentioned as benefiting from online courses?',
            ['people living far from cities', 'adults who work while studying', 'parents with young children', 'retired people'], 3,
            '2-xatboshida qolgan uch guruh sanab oʻtilgan, nafaqaxoʻrlar haqida gap yoʻq.', 1),
         ch('What can be inferred about students who lack self-discipline?',
            ['They usually prefer online study.', 'They may leave a course without anyone noticing.',
             'Their teachers give them extra help.', 'They move faster through the material.'], 1,
            '«may quietly drop out» — «quietly» jimgina, hech kim sezmasdan tashlab ketishini bildiradi. Qolgan variantlar '
            'haqida matnda maʼlumot yoʻq yoki ular yaxshi oʻqiydiganlarga tegishli.', 2),
         ch('The word "fragile" in paragraph C is closest in meaning to',
            ['easily damaged or weakened', 'very expensive', 'popular with young people', 'difficult to understand'], 0,
            'Erkinlik onlayn taʼlimni jozibali qiladi, lekin uni «fragile» — oson buziladigan, moʻrt ham qiladi.', 2),
         ch('Why does the writer mention a chemistry student and a future surgeon?',
            ['to show that some skills require practical training', 'to suggest that science is the most popular online subject',
             'to compare the difficulty of different careers', 'to argue that videos are better than laboratories'], 0,
            '«hands-on practice that no video can fully replace» — bu misollar amaliy mashgʻulot zarurligini koʻrsatadi.', 3),
         ch('What is the writer\'s opinion of courses that consist only of uploaded videos?',
            ['They are the most effective type of online course.', 'They are rarely effective.',
             'They are useful for practical subjects.', 'They should include more written comments.'], 1,
            '6-xatboshi: «a collection of uploaded videos rarely is» — yaʼni kamdan-kam samarali.', 5),
         tf('Some form of distance learning existed before the internet.', 'T',
            '1-xatboshi: «courses by post existed long before the internet».', 0, ng=True),
         tf('Online students generally get higher marks than students in classrooms.', 'NG',
            'Matnda baholar solishtirilmagan — faqat kim muvaffaqiyatli boʻlishi haqida gap bor.', 2),
         tf('In blended learning, students complete all of their work at home.', 'F',
            '5-xatboshi: uyda maʼruza va mashqlar, sinfda esa muhokama va amaliy ish — hammasi uyda emas.', 4, ng=True),
         gap('Supporters believe blended learning makes better use of the ___.', 'teacher',
             '«this approach makes better use of the teacher» — oʻqituvchi takrorlashga emas, savollarga koʻproq vaqt ajratadi.', 4, 1),
     ])

# ---------------------------------------------------------------- b2-05 city transport
MIX_INTRO = ('Topshiriq: aralash — Matching headings, True / False / Not Given va qisqa javobli savollar. Haqiqiy imtihonda '
             'bitta matnga bir necha xil topshiriq beriladi. Maslahat: avval sarlavhalarni moslang — bu butun matn '
             'tuzilishini tushunishga yordam beradi va keyingi savollarda kerakli xatboshini tezroq topasiz.')

HEADINGS = ['Paying to use the busiest roads', 'Going underground to escape the traffic', 'Feeling safe is what gets people cycling',
            'Cheaper tickets for metro passengers', 'Painting new lines on city roads']

text(B, 'b2-05-city-transport', 'Shahar transporti', 'Moving the City', 'B2', 'exam',
     L('Shahar hayoti', 'City life'), MIX_INTRO,
     [
         P("Anyone who has sat in a traffic jam knows that big cities have a transport problem. As urban populations grow and "
           "more families buy cars, roads that once seemed wide enough become crowded for much of the day. The result is not "
           "only lost time but also noise, air pollution and stress. City authorities around the world are therefore looking "
           "for ways to move more people while putting fewer vehicles on the streets."),
         P("For many large cities, the backbone of the solution is an underground railway. A metro can carry enormous numbers "
           "of passengers quickly, and because it runs beneath the streets, it is not affected by the traffic above. The "
           "drawback is cost: building tunnels and stations is extremely expensive and can take many years, which is why new "
           "lines are often planned decades in advance."),
         P("Buses are cheaper and more flexible, since routes can be changed without major construction. However, a bus stuck "
           "in traffic is no faster than a car. To deal with this, some cities have introduced dedicated bus lanes, and a few "
           "have built rapid bus systems in which buses run on separate roads and passengers pay before boarding, so that the "
           "service works rather like a metro above ground."),
         P("Cycling is also receiving more attention. In several European cities, a large share of daily journeys is made by "
           "bicycle, largely because safe, separated cycle paths have been built over many years. Planners have learned that "
           "painting a line on a busy road is not enough: people will only cycle in large numbers if they feel protected from "
           "cars. Bike-sharing schemes, which allow users to rent a bicycle for a short trip, have spread to many countries."),
         P("A more controversial approach is to make driving itself more expensive. A number of cities, including London, "
           "Stockholm and Singapore, charge drivers a fee for entering busy central areas or using the most crowded "
           "roads at certain times. Supporters "
           "point out that such congestion charges reduce traffic and raise money that can be spent on public transport. "
           "Critics argue that they are unfair to people on low incomes who have no real alternative to driving."),
         P("Tashkent offers an interesting example of a city adapting to rapid growth. Its metro, which opened in 1977, was "
           "the first in Central Asia, and its stations are famous for their richly decorated halls. In recent years the "
           "network has been expanded considerably, including a new line that runs above ground around parts of the city, and "
           "many old buses have been replaced with newer ones. As in other growing cities, the challenge is to make public transport attractive "
           "enough that residents choose it over their cars."),
     ],
     [G('traffic jam', 'tirbandlik'), G('urban', 'shahar(ga oid)'), G('pollution', 'ifloslanish'),
      G('authorities', 'hokimiyat, mutasaddi idoralar'), G('backbone', 'asos, tayanch'), G('drawback', 'kamchilik'),
      G('flexible', 'moslashuvchan'), G('dedicated', 'maxsus ajratilgan'), G('board', '(transportga) chiqmoq'),
      G('separated', 'ajratilgan'), G('scheme', 'tizim, dastur'), G('controversial', 'bahsli'),
      G('congestion', 'tirbandlik, gavjumlik'), G('alternative', 'muqobil'), G('adapt to', '… ga moslashmoq'),
      G('expand', 'kengaytirmoq')],
     [GN('i55-non-defining', 'Aniqlovchi boʻlmagan ergash gap: , which …,', 'Its metro, which opened in 1977, was the first in Central Asia'),
      GN('i30-passive-tenses', 'Majhul nisbat (Present Perfect): has been expanded', 'the network has been expanded considerably')],
     [
         hd(1, HEADINGS, 1, 'B xatboshi: metro koʻchalar ostida yuradi va tirbandlikka bogʻliq emas. «Cheaper tickets» notoʻgʻri — '
            'aksincha, metro qimmat ekani aytilgan.'),
         hd(3, HEADINGS, 2, 'D xatboshi: odamlar oʻzini xavfsiz his qilsagina velosipedda yuradi. «Painting new lines» — tuzoq: '
            'matnda chiziq chizish «not enough» deyilgan.'),
         hd(4, HEADINGS, 0, 'E xatboshi: gavjum markazga kirish yoki eng tirband yoʻllardan foydalanish uchun haq toʻlash — congestion charges.'),
         tf('Traffic congestion causes problems other than wasted time.', 'T',
            '1-xatboshi: «not only lost time but also noise, air pollution and stress».', 0, ng=True),
         tf('In rapid bus systems, passengers buy their tickets after getting on the bus.', 'F',
            '3-xatboshi: «passengers pay before boarding» — avtobusga chiqishdan oldin.', 2, ng=True),
         tf('Bike-sharing schemes are used more by tourists than by local residents.', 'NG',
            '4-xatboshida bike-sharing koʻp mamlakatlarga tarqalgani aytilgan, lekin kim koʻproq foydalanishi haqida maʼlumot yoʻq.', 3),
         tf('No other city in Central Asia had a metro before Tashkent.', 'T',
            '6-xatboshi: «was the first in Central Asia» — demak undan oldin boshqasida boʻlmagan.', 5, ng=True),
         ch('According to the writer, what is the main disadvantage of a metro?',
            ['It is affected by traffic on the streets.', 'It is very expensive and slow to build.',
             'It cannot carry many passengers.'], 1,
            '«The drawback is cost: … extremely expensive and can take many years». Birinchi va uchinchi variant matnga zid.', 1),
         gap('To help buses move faster, some cities have introduced dedicated ___.', 'bus lanes',
             '3-xatboshi: «some cities have introduced dedicated bus lanes».', 2, 2),
         gap('Critics say congestion charges are unfair to people on ___ who must drive.', ['low incomes', 'low income'],
             '5-xatboshi: «unfair to people on low incomes who have no real alternative to driving».', 4, 2),
     ])
