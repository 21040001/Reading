"""B2 · 4-boʻlim: Summary va gap completion (NO MORE THAN N WORDS)"""
from lib import *

B = 'b2'

# ---------------------------------------------------------------- 16. Sardoba
text(B, 'b2-16-sardoba', 'Sardobalar — choʻldagi suv omborlari', 'Sardobas: Water Stores of the Desert', 'B2', 'exam',
     L('Tarix va meʼmorchilik', 'History and architecture'),
     'Topshiriq: Summary va sentence completion (NO MORE THAN N WORDS). Maslahat: boʻshliqdan oldingi va keyingi '
     'soʻzlarga qarang — «a/the» yoki sifatdan keyin odatda ot, «to» yoki «will»dan keyin feʼl keladi. Avval qaysi soʻz '
     'turkumi kerakligini aniqlang, keyin matndan shu turdagi soʻzni qidiring.',
     [
         P("Travelling across the deserts of Central Asia was always a test of endurance. For merchants on the caravan "
           "routes, the greatest danger was not bandits or heat alone, but thirst. Wells were often deep, and their water "
           "could be salty. To solve this problem, builders in the region developed a remarkable structure known as the "
           "sardoba, a covered cistern designed to collect and store fresh water."),
         P("A typical sardoba consisted of two parts. Below ground was a large round reservoir, lined with fired bricks and "
           "sealed with a special mortar so that water would not leak away. Above it rose a dome, also made of brick, which "
           "could be seen from a great distance. For a tired traveller, the shape of a dome on the horizon was a welcome "
           "sign that water was near."),
         P("The water itself came mainly from nature. In winter and spring, rain and melting snow ran across the surrounding "
           "land and were directed into the reservoir through channels and small openings. In some places, the land around "
           "the cistern was shaped deliberately so that it sloped towards the cistern. During the dry summer months, when no "
           "rain fell for weeks, travellers and their animals depended on this stored supply."),
         P("The dome was far more than decoration. By keeping out direct sunlight, it reduced evaporation and kept the water "
           "cool even in extreme heat. It also protected the supply from sand, dust and animals, so the water stayed "
           "relatively clean. Small openings near the top allowed air to circulate, which is believed to have helped prevent "
           "the water from becoming stale. Steps led down from the entrance to the water level, so people could fill their "
           "containers by hand."),
         P("Sardobas were usually built along trade routes, often roughly a day's journey apart, and many stood next to "
           "caravanserais, the roadside inns where merchants rested. Building one required considerable money and skill, and "
           "historians believe that rulers and wealthy patrons often paid for them as a public service. A well-maintained "
           "cistern could serve travellers for generations."),
         P("Today, most of these structures have disappeared or survive only as ruins. A number of them, however, can still "
           "be seen in Uzbekistan, and some have been restored. Between Navoiy and Bukhara, for example, the Sardoba Malik stands close "
           "to the remains of the Rabati Malik caravanserai. For modern visitors, these quiet brick domes are a reminder of "
           "how earlier generations solved the problem of water with simple materials and careful engineering."),
     ],
     [G('endurance', 'chidamlilik, bardosh'), G('merchant', 'savdogar'), G('cistern', 'yopiq suv ombori, sardoba'),
      G('reservoir', 'suv havzasi, rezervuar'), G('dome', 'gumbaz'), G('mortar', 'qorishma'),
      G('leak away', 'sizib chiqib ketmoq'), G('evaporation', 'bugʻlanish'), G('deliberately', 'ataylab, qasddan'),
      G('slope', 'qiya boʻlmoq; qiyalik'), G('circulate', 'aylanmoq, harakatlanmoq'), G('stale', 'aynigan, eskirgan'),
      G('caravanserai', 'karvonsaroy'), G('patron', 'homiy'), G('ruins', 'xarobalar'), G('restore', 'taʼmirlamoq, tiklamoq')],
     [GN('i64-so-that-in-order-to', 'so that: maqsadni bildirish', 'sealed with a special mortar so that water would not leak away'),
      GN('i31-it-is-said', 'is believed to have …', 'which is believed to have helped prevent the water from becoming stale')],
     [
         gap("For merchants crossing the desert, the biggest danger was ___.", 'thirst',
             '1-xatboshi: «the greatest danger was not bandits or heat alone, but thirst». «was»dan keyin ot kerak.', 0, 1),
         gap("The underground reservoir was lined with ___.", ['fired bricks', 'bricks'],
             '2-xatboshi: «lined with fired bricks». «with»dan keyin ot (koʻplikda) keladi.', 1, 2),
         gap("A special ___ was used so that the water would not escape.", 'mortar',
             '«sealed with a special mortar so that water would not leak away» — «a special»dan keyin birlikdagi ot.', 1, 1),
         gap("The cistern was filled mainly by rain and ___.", ['melting snow', 'snow'],
             '3-xatboshi: «rain and melting snow ran across the surrounding land». «and» bir xil turdagi soʻzlarni bogʻlaydi — ot.', 2, 2),
         gap("Because it kept out direct sunlight, the dome reduced ___.", 'evaporation',
             '4-xatboshi: «By keeping out direct sunlight, it reduced evaporation».', 3, 1),
         gap("Openings near the top of the dome allowed ___ to move around.", 'air',
             '«Small openings near the top allowed air to circulate» — «circulate» = «move around».', 3, 1),
         gap("Many sardobas were built beside ___, where merchants could rest.", ['caravanserais', 'roadside inns'],
             '5-xatboshi: «many stood next to caravanserais, the roadside inns where merchants rested». «beside» = «next to».', 4, 2),
         tf("The water in some desert wells had a high salt content.", 'T',
            '1-xatboshi: «their water could be salty» — tuzli boʻlishi mumkin edi.', 0, ng=True),
         tf("The domes of sardobas were hard to notice from far away.", 'F',
            '2-xatboshi aksini aytadi: «could be seen from a great distance».', 1, ng=True),
         tf("Guards were employed to protect the water in sardobas.", 'NG',
            '5-xatboshida kim qurish uchun pul toʻlagani aytilgan («rulers and wealthy patrons»), lekin suvni qoʻriqlovchilar haqida maʼlumot yoʻq.', 4),
         ch("Which statement about sardobas today is supported by the text?",
            ['All of them have been fully restored.', 'Most have gone or are in ruins, but some can still be seen.',
             'They are still used by caravans on trade routes.', 'They can be found only between Navoiy and Bukhara.'], 1,
            '6-xatboshi: «most of these structures have disappeared or survive only as ruins … some have been restored». '
            'Sardoba Malik faqat misol («for example»), «all» notoʻgʻri.', 5),
     ])

# ---------------------------------------------------------------- 17. Honey
text(B, 'b2-17-honey', 'Asal', 'Honey', 'B2', 'exam',
     L('Tabiat', 'Nature'),
     'Topshiriq: Summary va sentence completion. Maslahat: soʻz chegarasiga qatʼiy amal qiling — «NO MORE THAN TWO WORDS» '
     'boʻlsa, uch soʻz yozgan javob xato hisoblanadi, hatto maʼnosi toʻgʻri boʻlsa ham. Ortiqcha artikl yoki sifat qoʻshmang '
     'va soʻzni matndagidek (birlik/koʻplik) koʻchiring.',
     [
         P("Honey is one of the oldest sweet foods known to humans, and the process that creates it is remarkable. It "
           "begins when worker bees visit flowers and collect nectar, a sugary liquid that plants produce to attract insects. "
           "A single bee carries only a tiny amount on each trip, so a colony must make an enormous number of flights to "
           "fill even one jar."),
         P("Back in the hive, the transformation begins. The bees pass the nectar from one to another, adding enzymes that "
           "break down larger sugar molecules into simpler ones. They then deposit it in the wax cells of the honeycomb. At this "
           "stage the liquid still contains a great deal of water, so the bees fan it with their wings to speed up "
           "evaporation. When the honey has become thick enough, they seal each cell with a thin cap of wax."),
         P("This careful process explains one of honey's most unusual qualities: it can keep for an extremely long time. "
           "Because honey contains very little water, bacteria and moulds find it difficult to grow in it. It is also "
           "slightly acidic, which creates further unfavourable conditions for microorganisms. Over time, "
           "honey may crystallise and turn solid, but this is a natural change, and gentle warming usually returns it to a "
           "liquid state."),
         P("Not all honey tastes the same. Its colour, aroma and flavour depend largely on the flowers the bees have "
           "visited. Honey from some plants is pale and mild, while honey from others is dark and strong. Beekeepers "
           "sometimes move their hives to areas where a particular plant is in flower in order to produce a honey with a "
           "distinctive character."),
         P("In Uzbekistan, beekeeping has a long tradition, especially in the mountain and foothill areas, where wild herbs "
           "and flowering meadows provide rich sources of nectar. Families often pass their knowledge from one generation "
           "to the next, and mountain honey is widely valued at local markets. In summer, some beekeepers move their hives "
           "higher up the slopes, as flowers bloom later at higher altitudes."),
         P("Honey has also been used in traditional remedies for centuries, and many people believe it soothes a sore "
           "throat. Such claims should be treated with some caution, however: honey is not a medicine, and since it consists "
           "mainly of sugar, eating large amounts is not healthy. Doctors also "
           "generally advise that it should not be given to babies under one year old. Enjoyed in moderation, though, honey "
           "remains a natural product that reflects both the work of bees and the landscape around them."),
     ],
     [G('nectar', 'gul shirasi, nektar'), G('colony', 'asalarilar oilasi, koloniya'), G('hive', 'asalari uyasi, qutisi'),
      G('enzyme', 'ferment'), G('deposit', 'joylamoq, toʻplamoq'), G('honeycomb', 'mum kataklar (asal kataklari)'),
      G('seal', 'yopmoq, muhrlamoq'), G('mould', 'mogʻor'), G('acidic', 'nordon, kislotali'),
      G('crystallise', 'kristallanmoq, qotmoq'), G('aroma', 'xushboʻy hid'), G('distinctive', 'oʻziga xos'),
      G('foothill', 'togʻ etagi'), G('meadow', 'yaylov, oʻtloq'), G('remedy', 'davo, dori'), G('moderation', 'meʼyor, chegara')],
     [GN('i64-so-that-in-order-to', 'in order to: maqsad', 'in order to produce a honey with a distinctive character'),
      GN('i30-passive-tenses', 'Modal + passive: should not be given', 'it should not be given to babies under one year old')],
     [
         gap("Plants produce nectar in order to ___.", 'attract insects',
             '1-xatboshi: «a sugary liquid that plants produce to attract insects». Ikki soʻz — chegaradan oshmaydi.', 0, 2),
         gap("Inside the hive, bees add ___ which break sugars down into simpler ones.", 'enzymes',
             '2-xatboshi: «adding enzymes that break down larger sugar molecules». Koʻplikda yozing — «which break» koʻplikni talab qiladi.', 1, 1),
         gap("To remove water from the nectar, the bees ___ it with their wings.", 'fan',
             '«the bees fan it with their wings to speed up evaporation». Bu yerda «fan» — feʼl.', 1, 1),
         gap("Finally, each cell is closed with a thin ___ of wax.", 'cap',
             '«they seal each cell with a thin cap of wax». «thin» savolda bor — uni takrorlamang, bitta soʻz kifoya.', 1, 1),
         gap("Honey keeps well because it has little water and is slightly ___.", 'acidic',
             '3-xatboshi: «It is also slightly acidic». «is slightly»dan keyin sifat keladi.', 2, 1),
         gap("Honey that has turned solid can usually be made liquid again by ___.", ['gentle warming', 'warming'],
             '«gentle warming usually returns it to a liquid state». Ikki soʻz — aynan chegarada.', 2, 2),
         gap("The colour and taste of honey depend mainly on the ___ that bees visit.", 'flowers',
             '4-xatboshi: «depend largely on the flowers the bees have visited». «largely» = «mainly».', 3, 1),
         tf("Each bee collects a large quantity of nectar on every flight.", 'F',
            '1-xatboshi: «A single bee carries only a tiny amount on each trip» — juda oz miqdor.', 0, ng=True),
         tf("When honey crystallises, it means the honey has gone bad.", 'F',
            '3-xatboshi: «this is a natural change» — buzilish emas, tabiiy oʻzgarish.', 2, ng=True),
         tf("Mountain honey from Uzbekistan is more expensive than honey from other regions.", 'NG',
            '5-xatboshi: «mountain honey is widely valued» — qadrlanadi, lekin narxi solishtirilmagan.', 4),
         ch("What is the writer's attitude to claims that honey is good for health?",
            ['strongly supportive', 'cautious', 'completely dismissive', 'uninterested'], 1,
            '6-xatboshi: «Such claims should be treated with some caution» — ehtiyotkor munosabat. '
            'Muallif ularni butunlay rad etmaydi, «in moderation» tavsiya qiladi.', 5),
     ])

# ---------------------------------------------------------------- 18. Cycling cities
text(B, 'b2-18-cycling-cities', 'Velosiped shaharlari', 'Cycling Cities', 'B2', 'exam',
     L('Shahar hayoti', 'City life'),
     'Topshiriq: Summary va sentence completion. Maslahat: savoldagi soʻzlar matnda koʻpincha sinonim bilan berilgan '
     '(masalan, «help» oʻrniga «encourage»). Avval sinonimni topib, kerakli joyni aniqlang, javobni esa matndan aynan '
     'koʻchiring — oʻz soʻzingiz bilan almashtirmang.',
     [
         P("In many cities around the world, planners are asking a question that few of their predecessors took seriously: "
           "how can we persuade more people to leave their cars at home and travel by bicycle? The reasons are easy to "
           "understand. Bicycles produce no exhaust fumes, take up little space and give riders regular exercise. For short "
           "journeys in crowded streets, they are often faster than cars."),
         P("Cities such as Amsterdam and Copenhagen are frequently mentioned as models. In both places, cycling is not a "
           "hobby for enthusiasts but an ordinary way of getting to work, school and the shops. This did not happen by "
           "accident. Over several decades, these cities invested steadily in infrastructure, built networks of connected "
           "routes and gave cyclists priority at many junctions."),
         P("Experts generally agree that the most important factor is safety. Many people say they would cycle more if they "
           "did not feel threatened by heavy traffic. Painted lines on the road offer limited protection, so cities that are "
           "serious about cycling build separated lanes, divided from cars by kerbs or barriers. Lower speed limits in "
           "residential streets and secure places to park bicycles also encourage newcomers to try."),
         P("Bike-sharing schemes have spread rapidly in recent years. Users can unlock a bicycle at one station, ride it "
           "across town and leave it at another, paying a small fee. Such schemes are particularly useful for people who do "
           "not own a bicycle or who want to combine cycling with public transport, for example by riding from a metro "
           "station to the office. However, they work well only if the bicycles are maintained and distributed sensibly "
           "around the city."),
         P("Climate presents a different challenge. In northern Europe, cyclists mainly have to cope with rain, wind and "
           "cold. In hot, dry cities, including many in Central Asia, the problem is the opposite: in summer, cycling in the "
           "middle of the day can be exhausting and even dangerous. Planners in such places are experimenting with "
           "tree-lined routes that provide shade, and some suggest that electric bicycles could reduce the physical effort "
           "needed."),
         P("Critics point out that not every city can copy the Dutch or Danish model. Hills, long distances and a strong car "
           "culture can make change slow and sometimes unpopular. Even so, the experience of cycling cities suggests that "
           "when safe and convenient routes exist, people tend to use them. In other words, good infrastructure often "
           "creates its own demand."),
     ],
     [G('persuade', 'koʻndirmoq'), G('exhaust fumes', 'chiqindi gazlar'), G('enthusiast', 'ishqiboz, havaskor'),
      G('infrastructure', 'infratuzilma'), G('priority', 'ustuvorlik, birinchi navbat huquqi'), G('junction', 'chorraha'),
      G('threatened', 'xavf ostida qolgan, tahdid his qilgan'), G('kerb', 'yoʻl chetidagi baland tosh, bordyur'),
      G('residential', 'turar-joy (hududi)'), G('scheme', 'tizim, dastur'), G('distribute', 'taqsimlamoq'),
      G('cope with', 'uddalamoq, bardosh bermoq'), G('exhausting', 'charchatuvchi'), G('shade', 'soya'),
      G('critic', 'tanqidchi'), G('demand', 'talab')],
     [GN('i26-second-conditional', 'Second conditional: would … if …',
         'Many people say they would cycle more if they did not feel threatened by heavy traffic'),
      GN('i39-want-somebody-to', 'persuade somebody to do', 'persuade more people to leave their cars at home')],
     [
         gap("One environmental advantage of bicycles is that they produce no ___.", ['exhaust fumes', 'fumes'],
             '1-xatboshi: «Bicycles produce no exhaust fumes». Ikki soʻz.', 0, 2),
         gap("In Amsterdam and Copenhagen, cyclists were given ___ at many junctions.", 'priority',
             '2-xatboshi: «gave cyclists priority at many junctions».', 1, 1),
         gap("Cities that take cycling seriously build ___ lanes, which are divided from cars.", 'separated',
             '3-xatboshi: «build separated lanes, divided from cars by kerbs or barriers». «lanes» oldidan sifat kerak.', 2, 1),
         gap("Reduced ___ in residential streets also encourage people to start cycling.", 'speed limits',
             '«Lower speed limits in residential streets … also encourage newcomers to try». «Reduced» = «Lower», «start» = «try».', 2, 2),
         gap("Users of bike-sharing schemes pay a ___ for each ride.", ['small fee', 'fee'],
             '4-xatboshi: «paying a small fee». «a»dan keyin birlikdagi ot.', 3, 2),
         gap("In hot cities, planners are testing routes lined with trees that give ___.", 'shade',
             '5-xatboshi: «tree-lined routes that provide shade». «give» = «provide».', 4, 1),
         gap("Electric bicycles might lower the ___ that riders need.", ['physical effort', 'effort'],
             '«electric bicycles could reduce the physical effort needed». «lower» = «reduce».', 4, 2),
         tf("High levels of cycling in Amsterdam and Copenhagen were the result of long-term investment.", 'T',
            '2-xatboshi: «This did not happen by accident. Over several decades, these cities invested steadily…».', 1, ng=True),
         tf("Lines painted on the road are considered enough to protect cyclists.", 'F',
            '3-xatboshi: «Painted lines on the road offer limited protection» — yetarli emas.', 2, ng=True),
         tf("Bike-sharing schemes cost cities less to run than bus services.", 'NG',
            '4-xatboshida ijara tizimlari va jamoat transporti bogʻlanadi, lekin xarajatlar solishtirilmagan.', 3),
         ch("What is the main point of the final paragraph?",
            ['Every city should copy the Dutch model exactly.',
             'Change can be hard in some cities, but safe routes usually attract cyclists.',
             'Hills and long distances make cycling impossible.',
             'Cycling cities have become unpopular with drivers.'], 1,
            '6-xatboshi: qiyinchiliklar bor («change slow and sometimes unpopular»), lekin «when safe and convenient routes '
            'exist, people tend to use them». «impossible» va «unpopular with drivers» matnda yoʻq.', 5),
     ])

# ---------------------------------------------------------------- 19. Language learning
text(B, 'b2-19-language-learning', 'Til qanday oʻrganiladi', 'How We Learn Languages', 'B2', 'exam',
     L('Taʼlim', 'Education'),
     'Topshiriq: Sentence completion (NO MORE THAN N WORDS) va True/False/Not Given. Maslahat: gaplar odatda matn '
     'tartibida keladi, shuning uchun bitta javobni topsangiz, keyingisini shu joydan keyin qidiring.',
     [
         P("Almost everyone who has tried to learn a foreign language has wondered why it seems so easy for some people and "
           "so difficult for others. Researchers who study second language learning do not agree on every point, but "
           "several ideas are widely accepted. Taken together, they suggest that there is no single secret method, but "
           "rather a combination of habits that make progress more likely."),
         P("The first is input. Learners need to hear and read a large amount of the language, and it helps if this "
           "material is understandable but slightly above their current level. Through repeated exposure, they gradually "
           "notice how words are combined and how sentences are built. Many teachers therefore recommend reading graded "
           "books or listening to podcasts on familiar topics, rather than struggling with material that is far too "
           "difficult."),
         P("Input alone, however, is rarely enough. To speak and write with confidence, learners also need practice in "
           "producing the language. When people try to express their own ideas, they discover gaps in their knowledge: a "
           "word they cannot remember, or a structure they are unsure about. Conversation, writing short texts and even "
           "talking to oneself can all provide valuable output practice."),
         P("Memory also plays a central role. New vocabulary is easily forgotten if it is studied only once. A technique "
           "known as spaced repetition addresses this problem by reviewing words at gradually increasing intervals: after a "
           "day, then a few days, then a week, and so on. Ideally, each review comes just as the word is about to be forgotten, which "
           "is thought to strengthen long-term memory. Flashcards, on paper or on a phone, are a common way of applying this "
           "idea."),
         P("Motivation is perhaps the hardest factor to control. Learners who have a clear personal reason, such as "
           "studying abroad, finding a job or communicating with relatives, often persist longer than those who study only "
           "because they must. Setting small, achievable goals and noticing one's own progress can help to maintain "
           "motivation during the difficult middle stage, when improvement seems slow."),
         P("Finally, it is worth rethinking the role of mistakes. Many learners are afraid of making errors, especially in "
           "front of others, and so they avoid speaking. Yet mistakes are a normal and even necessary part of learning, "
           "because they show that the learner is testing ideas about how the language works. Feedback from a teacher or a "
           "patient friend turns those errors into opportunities. In the end, for most learners, steady practice over months and years "
           "is likely to matter more than natural talent."),
     ],
     [G('combination', 'birikma, uygʻunlik'), G('input', 'oʻqib-eshitib qabul qilinadigan til materiali (input)'),
      G('exposure', 'tilga duch kelib turish, til muhitida boʻlish'), G('graded', 'darajalarga moslangan'),
      G('struggle with', 'qiynalmoq, kurashmoq'), G('confidence', 'ishonch, oʻziga ishonch'), G('output', 'oʻzi gapirish va yozish (output)'),
      G('vocabulary', 'lugʻat boyligi'), G('spaced repetition', 'oraliqli takrorlash'), G('interval', 'oraliq, vaqt oraligʻi'),
      G('strengthen', 'mustahkamlamoq'), G('persist', 'davom ettirmoq, qatʼiyat koʻrsatmoq'),
      G('achievable', 'erishsa boʻladigan'), G('feedback', 'fikr-mulohaza, qayta aloqa'), G('talent', 'isteʼdod')],
     [GN('i66-adjective-preposition', 'afraid of + -ing', 'Many learners are afraid of making errors'),
      GN('c34-participle-clauses', 'Participle clause: Taken together, …', 'Taken together, they suggest that there is no single secret method')],
     [
         gap("Useful input is easy to understand but a little above the learner's ___.", ['current level', 'level'],
             '2-xatboshi: «slightly above their current level». «a little» = «slightly».', 1, 2),
         gap("Through repeated ___, learners start to notice how sentences are formed.", 'exposure',
             '«Through repeated exposure, they gradually notice how … sentences are built».', 1, 1),
         gap("When learners try to express their own ideas, they find ___ in what they know.", 'gaps',
             '3-xatboshi: «they discover gaps in their knowledge». Koʻplikda yozing.', 2, 1),
         gap("With spaced repetition, words are reviewed at gradually increasing ___.", 'intervals',
             '4-xatboshi: «reviewing words at gradually increasing intervals».', 3, 1),
         gap("Reviewing a word just before it is forgotten is thought to strengthen ___.", 'long-term memory',
             '«which is thought to strengthen long-term memory». «long-term» bitta soʻz sanaladi — jami ikki soʻz.', 3, 2),
         gap("Learners who have a clear ___ for studying often continue for longer.", ['personal reason', 'reason'],
             '5-xatboshi: «Learners who have a clear personal reason … often persist longer». «continue» = «persist».', 4, 2),
         gap("With ___ from a teacher or a friend, mistakes can become opportunities.", 'feedback',
             '6-xatboshi: «Feedback from a teacher or a patient friend turns those errors into opportunities».', 5, 1),
         tf("Researchers have identified one method that works best for all learners.", 'F',
            '1-xatboshi: «there is no single secret method» — yagona usul yoʻq.', 0, ng=True),
         tf("Talking to yourself can be a useful way to practise a language.", 'T',
            '3-xatboshi: «even talking to oneself can all provide valuable output practice».', 2, ng=True),
         tf("Flashcards on paper are more effective than flashcards on a phone.", 'NG',
            '4-xatboshida ikkalasi ham tilga olinadi («on paper or on a phone»), lekin solishtirilmagan.', 3),
         ch("According to the writer, mistakes are",
            ['something to avoid in front of others.', 'a sign that a learner lacks talent.',
             'a natural part of the learning process.', 'important only when writing.'], 2,
            '6-xatboshi: «mistakes are a normal and even necessary part of learning». Xatolardan qochish — '
            'oʻquvchilarning odati, muallifning fikri emas.', 5),
     ])

# ---------------------------------------------------------------- 20. Earthquakes
text(B, 'b2-20-earthquakes', 'Yer qimirlashi', 'Earthquakes', 'B2', 'exam',
     L('Fan va tarix', 'Science and history'),
     'Topshiriq: Sentence completion. Maslahat: savollardagi raqamlar, sanalar va atoqli otlar (masalan, «1966», '
     '«Tashkent») matnda tez topiladigan «belgilar»dir. Ularni koʻz yugurtirib (scanning) toping, keyin shu gapni '
     'diqqat bilan oʻqib, boʻshliqqa mos soʻzni tanlang.',
     [
         P("The surface of the Earth may seem solid and still, but it is constantly, if very slowly, moving. The outer layer "
           "of the planet is broken into huge pieces called tectonic plates, which drift by a few centimetres a year. Where "
           "plates meet, they may push against each other, pull apart or slide past one another. Usually their edges are "
           "locked together by friction, and stress builds up over many years. When the rock finally breaks and moves "
           "suddenly, the stored energy is released as waves that shake the ground. This is an earthquake."),
         P("Central Asia is one of the regions where this process is active, largely because the land is being squeezed as the "
           "Indian plate pushes northwards into Asia. As a result, earthquakes are a familiar part of life in many parts of "
           "Uzbekistan and its neighbours. Most are small and pass almost unnoticed, but occasionally a stronger one causes "
           "serious damage."),
         P("The best-known example in the country's modern history is the Tashkent earthquake of 26 April 1966. It struck "
           "early in the morning, and its centre lay almost directly beneath the city at a shallow depth. Although the "
           "earthquake was not exceptionally powerful by world standards, its location meant that the shaking was intense "
           "in the centre. The number of deaths was relatively low, but a huge number of buildings, especially older houses "
           "made of mud brick, were destroyed or badly damaged, and many thousands of families lost their homes."),
         P("What followed is remembered as a remarkable example of solidarity. Builders, engineers and volunteers arrived "
           "from across the Soviet Union, and different republics took responsibility for constructing whole streets and "
           "neighbourhoods. Within a few years, large new residential districts had appeared, along with wide avenues, parks "
           "and public buildings. The rebuilding transformed the appearance of Tashkent, turning it into a much more modern "
           "city. A memorial in the city centre, known as the Courage monument, still commemorates the disaster and the people "
           "who rebuilt the city."),
         P("Since then, engineers have learned a great deal about how to make buildings safer. Earthquake-resistant "
           "structures are designed to bend slightly rather than break. They use reinforced concrete, strong connections "
           "between walls and floors, and foundations suited to the local ground. In areas at risk, building codes set "
           "minimum standards, although these rules are effective only if they are actually followed."),
         P("Individuals can also prepare. Experts advise fixing heavy furniture to walls and keeping a small emergency kit "
           "with water, a torch and basic medicines. During shaking, the usual recommendation is to drop to the ground, take "
           "cover under a sturdy table and hold on until the movement stops. Running outside while the ground is moving is "
           "generally considered more dangerous, since falling glass and bricks cause many injuries."),
     ],
     [G('tectonic plate', 'tektonik plita'), G('drift', 'siljimoq'), G('friction', 'ishqalanish'),
      G('stress', 'kuchlanish, zoʻriqish'), G('release', 'chiqarmoq, boʻshatmoq'), G('squeeze', 'siqmoq'),
      G('shallow', 'sayoz, chuqur boʻlmagan'), G('exceptionally', 'gʻoyat, favqulodda'), G('solidarity', 'birdamlik'),
      G('volunteer', 'koʻngilli'), G('residential district', 'turar-joy massivi, mavze'), G('commemorate', 'xotirasini abadiylashtirmoq'),
      G('reinforced concrete', 'temir-beton'), G('foundation', 'poydevor'), G('building code', 'qurilish meʼyorlari'),
      G('sturdy', 'mustahkam, pishiq')],
     [GN('i30-passive-tenses', 'Present Continuous Passive: is being squeezed', 'the land is being squeezed'),
      GN('i11-past-perfect', 'Past Perfect: had appeared', 'Within a few years, large new residential districts had appeared')],
     [
         gap("The edges of tectonic plates are usually held together by ___.", 'friction',
             '1-xatboshi: «their edges are locked together by friction». «held» = «locked».', 0, 1),
         gap("When rock breaks, the stored energy travels as ___ that shake the ground.", 'waves',
             '«the stored energy is released as waves that shake the ground».', 0, 1),
         gap("In 1966, the centre of the earthquake was at a ___ depth below Tashkent.", 'shallow',
             '3-xatboshi: «almost directly beneath the city at a shallow depth». «a … depth» oraligʻida sifat keladi.', 2, 1),
         gap("Many of the houses destroyed in 1966 were built of ___.", ['mud brick', 'mud bricks'],
             '«older houses made of mud brick, were destroyed». Ikki soʻz.', 2, 2),
         gap("Earthquake-resistant buildings are designed to ___ instead of breaking.", ['bend slightly', 'bend'],
             '5-xatboshi: «designed to bend slightly rather than break». «to»dan keyin feʼl keladi.', 4, 2),
         gap("In areas at risk, minimum standards for buildings are set by ___.", 'building codes',
             '«building codes set minimum standards».', 4, 2),
         gap("An emergency kit should contain water, basic medicines and a ___.", 'torch',
             '6-xatboshi: «a small emergency kit with water, a torch and basic medicines». «a»dan keyin birlikdagi ot.', 5, 1),
         tf("Most earthquakes in Uzbekistan cause serious damage.", 'F',
            '2-xatboshi: «Most are small and pass almost unnoticed» — koʻpchiligi kichik.', 1, ng=True),
         tf("The 1966 earthquake was one of the most powerful ever recorded in the world.", 'F',
            '3-xatboshi: «not exceptionally powerful by world standards» — kuchi jahon miqyosida unchalik katta emas edi.', 2, ng=True),
         tf("Most residents of Tashkent approved of the new design of the city.", 'NG',
            '4-xatboshi shahar qiyofasi oʻzgarganini aytadi, lekin aholining fikri haqida maʼlumot yoʻq.', 3),
         ch("What do experts recommend doing while the ground is shaking?",
            ['running outside immediately', 'taking cover under a strong table',
             'standing next to a window', 'fixing furniture to the walls'], 1,
            '6-xatboshi: «take cover under a sturdy table and hold on». Mebelni mahkamlash — oldindan tayyorgarlik, '
            'tashqariga yugurish esa «more dangerous».', 5),
     ])
