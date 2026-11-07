"""B2 · 3-boʻlim: Matching headings (har bir xatboshi uchun sarlavha + TFNG / gap)"""
from lib import *

B = 'b2'

# ---------------------------------------------------------------- 1. Cotton
H1 = ['Separating fibre from seed', 'Hand or machine: a choice with costs', 'Machines that replace spinning workers',
      'A demanding plant and where it grows', 'Keeping more of the profit at home', 'From loose fibres to strong thread',
      'Why seeds are worth more than fibre', 'Two ways of making cloth, and what follows', 'A thirsty crop under criticism']

text(B, 'b2-11-cotton', 'Paxta tolasidan kiyimgacha', 'From Cotton Field to Clothing', 'B2', 'exam',
     L('Iqtisod va sanoat', 'Economy and industry'),
     'Topshiriq: Matching headings, True/False/Not Given va gap. Har bir xatboshining birinchi va oxirgi jumlasiga '
     'alohida eʼtibor bering — asosiy gʻoya koʻpincha shu yerda boʻladi. Lekin «however», «by contrast» kabi '
     'soʻzlardan keyin fikr burilishi mumkin, shuning uchun xatboshini oxirigacha oʻqing.',
     [
         P("Most of us wear cotton every day, yet few people stop to think about where it comes from. Cotton is a natural "
           "fibre that grows around the seeds of the cotton plant, protecting them inside a round pod known as a boll. The "
           "plant is demanding: it needs a long, hot growing season, plenty of sunshine and a reliable supply of water. For "
           "this reason, it is cultivated mainly in warm regions of Asia, Africa and the Americas."),
         P("When the bolls ripen and burst open, the soft white fibre is ready to be collected. For centuries, this was done "
           "entirely by hand, and in many countries it still is. Hand-picking is slow and physically exhausting, but it has "
           "one clear advantage: pickers can select only the ripe bolls and leave behind leaves and stems. Harvesting "
           "machines, by contrast, can clear a large field in a fraction of the time, although the cotton they gather "
           "usually contains more unwanted plant material."),
         P("The next stage takes place in a factory called a gin. Here, machines separate the fibre, known as lint, from the "
           "seeds, which make up a large part of the weight of the harvested crop. Little is wasted at this point. The seeds "
           "can be pressed to produce cooking oil, and what remains is often used as animal feed. The clean lint, meanwhile, "
           "is squeezed into large, tightly packed bales so that it can be stored and transported easily."),
         P("At a spinning mill, the bales are opened and the fibres are cleaned once more. They are then carded, a process that untangles "
           "them and lays them roughly parallel, and are gradually drawn out into a thin, loose rope. Finally, this rope is twisted "
           "to make yarn. The quality of the yarn depends largely on the raw material: as a general rule, longer fibres "
           "produce yarn that is finer and stronger."),
         P("Yarn becomes fabric in one of two main ways. In weaving, two sets of threads cross each other at right angles, "
           "creating a firm material suitable for shirts, sheets and jeans. In knitting, a single thread is formed into rows "
           "of connected loops, which gives the fabric its stretch, as in a typical T-shirt. Most fabric is then dyed and "
           "finished, processes that can require considerable amounts of water, energy and chemicals."),
         P("It is this heavy use of resources that has made cotton the subject of growing debate. The crop is often "
           "described as thirsty, and in dry regions it depends almost completely on irrigation. The shrinking of the Aral "
           "Sea, caused largely by the diversion of river water for irrigation, much of it for cotton, is frequently given as a warning. In "
           "response, many farmers have begun to adopt water-saving methods such as drip irrigation, while some producers "
           "are trying to reduce their use of pesticides."),
         P("Uzbekistan has long been one of the world's major cotton producers, and the crop has shaped the country's "
           "landscape and economy for generations. For much of the twentieth century, however, most of the harvest was exported as "
           "raw fibre, so the greater profits from making yarn, fabric and clothing were earned elsewhere. In recent years, "
           "the country has set out to change this by building spinning mills and textile factories at home. The aim is to "
           "keep more of the value inside the country and to create jobs."),
     ],
     [G('fibre', 'tola'), G('demanding', 'talabchan'), G('cultivate', 'yetishtirmoq'), G('ripen', 'pishmoq, yetilmoq'),
      G('exhausting', 'juda charchatadigan'), G('advantage', 'afzallik'), G('separate', 'ajratmoq'),
      G('bale', 'toy (presslangan paxta)'), G('parallel', 'parallel, bir yoʻnalishda yonma-yon'), G('yarn', 'ip, kalava'),
      G('weaving', 'toʻqish (dastgohda)'), G('dye', 'boʻyamoq'), G('irrigation', 'sugʻorish'),
      G('diversion', 'boshqa tomonga burish'), G('pesticide', 'pestitsid, zararkunandalarga qarshi kimyoviy modda'),
      G('export', 'eksport qilmoq')],
     [GN('c57-cleft-sentences', 'Ajratib koʻrsatish: It is … that …',
         'It is this heavy use of resources that has made cotton the subject of growing debate.'),
      GN('i30-passive-tenses', 'Majhul nisbat: is cultivated, was exported',
         'it is cultivated mainly in warm regions of Asia, Africa and the Americas')],
     [
         hd(0, H1, 3, 'Xatboshi A: paxta qanday oʻsimlik va unga nima kerak (issiqlik, quyosh, suv), qayerda ekiladi. '
                      '«Thirsty crop under criticism» emas — bu yerda tanqid yoʻq.'),
         hd(1, H1, 1, 'Xatboshi B: qoʻlda terish sekin, lekin toza; mashina tez, lekin ortiqcha oʻsimlik qismlari koʻp — '
                      'har bir usulning oʻz «narxi» bor.'),
         hd(2, H1, 0, 'Xatboshi C: jinda tola (lint) chigitdan ajratiladi. «Why seeds are worth more…» — chigit haqida '
                      'gap bor, lekin u toladan qimmatroq deyilmagan.'),
         hd(3, H1, 5, 'Xatboshi D: tolalar tozalanadi, titilib bir yoʻnalishga keltiriladi va eshilib ipga aylanadi. «Machines that replace spinning '
                      'workers» — ishchilar haqida hech narsa yoʻq.'),
         hd(4, H1, 7, 'Xatboshi E: toʻqish (weaving) va trikotaj (knitting) — ikki usul, keyin boʻyash va pardozlash.'),
         hd(5, H1, 8, 'Xatboshi F: paxta «thirsty» — koʻp suv talab qiladi, Orol misoli, tanqidga javob choralari.'),
         hd(6, H1, 4, 'Xatboshi G: Oʻzbekiston xom tolani emas, ip va gazlamani oʻzi ishlab chiqarib, foydani mamlakatda '
                      'qoldirmoqchi.'),
         tf('Cotton gathered by machines is usually cleaner than cotton picked by hand.', 'F',
            'Aksincha: mashina yigʻgan paxtada «more unwanted plant material» boʻladi; qoʻl bilan terganda barg va '
            'poyalar qoldiriladi.', 1, ng=True),
         gap('Generally, yarn made from longer fibres is finer and ___.', 'stronger',
             '«longer fibres produce yarn that is finer and stronger».', 3, 1),
         tf('Knitted fabric is more popular with shoppers than woven fabric.', 'NG',
            'Matnda ikki usul tasvirlangan, lekin qaysi biri xaridorlarga koʻproq yoqishi aytilmagan.', 4),
         tf('In the past, much of Uzbekistan\'s cotton left the country before it was made into yarn.', 'T',
            '«most of the harvest was exported as raw fibre» — xom tola holida eksport qilingan.', 6, ng=True),
     ])

# ---------------------------------------------------------------- 2. Museums
H2 = ['Damage caused by large crowds', 'Who should keep the treasures?', 'Hidden collections brought into view',
      'A traditional model under challenge', 'Visiting from a distance', 'Learning through activity',
      'Why children prefer screens to objects', 'Rich national collections and a blended future']

text(B, 'b2-12-museums', 'Muzeylar kelajagi', 'The Future of Museums', 'B2', 'exam',
     L('Madaniyat', 'Culture'),
     'Topshiriq: Matching headings, True/False/Not Given va gap. Avval eng oson xatboshilardan boshlang va ishlatilgan '
     'sarlavhalarni chizib qoʻying: qiyin xatboshilarga yetganda tanlov kamayadi. Har bir sarlavha faqat bir marta ishlatiladi.',
     [
         P("For most of the last two centuries, the typical museum followed a familiar model. Valuable objects were "
           "displayed behind glass in quiet halls, visitors walked slowly from room to room reading small labels, and signs "
           "reminded everyone not to touch anything. This model has not disappeared, but it is under pressure. Younger "
           "audiences expect to take part rather than simply look, and museums now compete for attention with countless "
           "other forms of entertainment."),
         P("One of the biggest changes has taken place behind the scenes. Many museums are photographing and scanning their "
           "collections and publishing the images in online catalogues. Only a small proportion of what a large museum owns "
           "is ever on display at one time, so digitisation allows researchers and curious members of the public to examine "
           "objects that would otherwise stay in storage. A detailed digital record can also be valuable if an original is "
           "damaged by fire, flood or simply the passage of time."),
         P("Virtual tours have taken this idea further. Using a computer or phone, a person in a small village can now walk "
           "through the galleries of a famous museum on another continent, zooming in on paintings in a way that would be "
           "impossible in a crowded room. Such tours became especially popular when many buildings were forced to close "
           "their doors for long periods. Critics, however, argue that a screen can never reproduce the experience of "
           "standing in front of the real thing."),
         P("Inside the buildings themselves, interactive exhibits are becoming common. Touch screens allow visitors to "
           "explore the history of an object, sound and light recreate the atmosphere of a past era, and hands-on displays "
           "invite children to build, test and experiment. Supporters say that people remember what they do far better than "
           "what they read. Some curators worry, though, that visitors may become so absorbed in the technology that they "
           "hardly notice the objects the exhibition was designed to show."),
         P("Museums are also facing difficult questions about the objects they hold. A number of famous collections include "
           "items that were taken from other countries during periods of colonial rule or war, sometimes without the "
           "agreement of the communities they came from. Some institutions have returned such objects or begun discussions "
           "with the countries concerned, while others argue that keeping them allows a global audience to see them. The "
           "debate is unlikely to be settled soon."),
         P("Museums in Uzbekistan face many of the same challenges and opportunities. Collections in cities such as Tashkent, Samarkand and "
           "Bukhara contain manuscripts, ceramics, textiles and jewellery of great historical importance, and work is under "
           "way in several places to modernise displays and make collections more accessible. Many experts believe that the "
           "museum of the future will combine both worlds: a building where people can meet original objects face to face, "
           "supported by digital tools that extend its reach far beyond its walls."),
     ],
     [G('display', 'namoyish qilmoq; ekspozitsiya'), G('label', 'yorliq, tavsif yozuvi'), G('audience', 'tomoshabinlar, auditoriya'),
      G('compete', 'raqobatlashmoq'), G('scan', 'skanerlamoq'), G('proportion', 'ulush, qism'),
      G('digitisation', 'raqamlashtirish'), G('storage', 'ombor, saqlash joyi'), G('reproduce', 'aynan takrorlamoq'),
      G('interactive', 'interaktiv'), G('atmosphere', 'muhit, ruh'), G('curator', 'kurator, muzey xodimi'),
      G('absorbed in', '… ga berilib ketgan'), G('colonial', 'mustamlakachilik davriga oid'),
      G('manuscript', 'qoʻlyozma'), G('accessible', 'ochiq, foydalanish oson')],
     [GN('c34-participle-clauses', 'Ravishdosh oborot: Using a computer…',
         'Using a computer or phone, a person in a small village can now walk through the galleries'),
      GN('c52-but-for-otherwise', 'otherwise — «aks holda»', 'objects that would otherwise stay in storage')],
     [
         hd(0, H2, 3, 'Xatboshi A: oynavand vitrinalar, sukunat, «tegmang» — anʼanaviy model endi bosim ostida.'),
         hd(1, H2, 2, 'Xatboshi B: omborda yotgan buyumlar raqamlashtirilib, onlayn katalog orqali hammaga koʻrinadi. '
                      '«Damage caused by large crowds» — «damaged» soʻzi bor, lekin olomon haqida emas.'),
         hd(2, H2, 4, 'Xatboshi C: virtual sayohat — boshqa qitʼadagi muzeyni uydan turib koʻrish.'),
         hd(3, H2, 5, 'Xatboshi D: interaktiv eksponatlar: «people remember what they do» — harakat orqali oʻrganish. '
                      '«Why children prefer screens…» — bolalar tilga olingan, lekin bunday fikr yoʻq.'),
         hd(4, H2, 1, 'Xatboshi E: boshqa mamlakatlardan olib ketilgan buyumlar kimda qolishi kerak — egalik masalasi.'),
         hd(5, H2, 7, 'Xatboshi F: Oʻzbekiston muzeylaridagi boy meros hamda haqiqiy va raqamli dunyoni birlashtirgan kelajak muzeyi. «Hidden collections…» emas — bu B xatboshining asosiy gʻoyasi.'),
         tf('At any given time, most of the objects owned by a large museum are on display.', 'F',
            '«Only a small proportion … is ever on display» — faqat kichik qismi koʻrsatiladi.', 1, ng=True),
         tf('Virtual tours now attract more people than visits to museum buildings.', 'NG',
            'Virtual sayohatlar mashhur boʻlgani aytilgan, lekin binolarga tashrif bilan solishtirilmagan.', 2),
         gap('Supporters of interactive exhibits claim that people remember what they ___ far better than what they read.',
             'do', '«people remember what they do far better than what they read».', 3, 1),
         tf('Some museums think that keeping disputed objects benefits visitors from around the world.', 'T',
            '«others argue that keeping them allows a global audience to see them».', 4, ng=True),
     ])

# ---------------------------------------------------------------- 3. Insomnia
H3 = ['Why some people need less sleep', 'When poor sleep becomes a real condition', 'Signs that professional advice is needed',
      'Daily routines that support rest', 'Screens that help the mind relax', 'Caught in a circle of worry',
      'A range of possible triggers', 'The pull of the glowing screen']

text(B, 'b2-13-insomnia', 'Uyqusizlik', 'Insomnia', 'B2', 'exam',
     L('Sogʻliq', 'Health'),
     'Topshiriq: Matching headings, True/False/Not Given va gap. Xatboshidagi soʻzni aynan takrorlaydigan sarlavhadan '
     'ehtiyot boʻling — u koʻpincha tuzoq. Toʻgʻri sarlavha odatda xatboshining gʻoyasini boshqa soʻzlar bilan ifodalaydi.',
     [
         P("Almost everyone has experienced a night when sleep simply would not come. Insomnia, however, is more than an "
           "occasional bad night. Doctors use the term to describe persistent difficulty falling asleep, staying asleep or "
           "waking far too early, even when a person has the time and opportunity to rest. Crucially, it also affects the "
           "following day, leaving people tired, irritable or unable to concentrate. Short episodes are very common, but "
           "when the problem continues for months it is usually described as chronic."),
         P("There is rarely a single cause. Stress is among the most frequent triggers, whether it comes from exams, work, "
           "money or relationships, and a major life change can disrupt sleep for weeks. The environment matters too: a "
           "noisy street, a bright room or a bedroom that is too warm can all make rest harder. Irregular working hours, "
           "such as night shifts, confuse the body's internal clock, while caffeine taken late in the day may keep the "
           "brain alert long after the last cup."),
         P("Many researchers believe that modern evening habits play a part as well. Phones, tablets and computers give off "
           "bright light at a time when the body would naturally be preparing for sleep. Perhaps more importantly, the "
           "content on them is designed to hold attention. Reading messages, watching one more video or checking the news "
           "can keep the mind active, so that a person who intended to sleep at eleven may still be scrolling an hour later."),
         P("To counter these influences, specialists often recommend a set of simple habits, sometimes called sleep hygiene. Going to bed "
           "and getting up at roughly the same time every day, including weekends, helps to stabilise the internal clock. "
           "The bedroom should ideally be dark, quiet and cool, and used mainly for sleep. Regular physical activity during "
           "the day tends to improve sleep, although intense exercise just before bed may have the opposite effect. Heavy "
           "meals late in the evening are also best avoided."),
         P("Ironically, one of the strongest forces keeping people awake can be anxiety about sleep itself. After several "
           "difficult nights, a person may start to dread going to bed, and this tension makes sleep even less likely. "
           "Watching the clock and calculating how few hours remain only adds to the pressure. A common piece of advice, "
           "therefore, is to get up after lying awake for a long time and do something calm in dim light until sleepiness "
           "returns."),
         P("Occasional poor sleep is normal and usually improves on its own. However, it is sensible to see a doctor if the "
           "problem lasts for several weeks, if it seriously affects work, study or mood, or if a partner notices loud "
           "snoring or pauses in breathing during the night. A doctor can look for underlying causes and suggest suitable "
           "treatment. Talking therapies that focus on thoughts and habits around sleep are widely recommended and have "
           "helped many people."),
     ],
     [G('occasional', 'vaqti-vaqti bilan boʻladigan'), G('persistent', 'uzoq davom etadigan, surunkali'),
      G('irritable', 'jahldor, asabiy'), G('concentrate', 'diqqatni jamlamoq'), G('chronic', 'surunkali'),
      G('trigger', 'qoʻzgʻatuvchi sabab'), G('disrupt', 'buzmoq, izdan chiqarmoq'), G('internal clock', 'ichki (biologik) soat'),
      G('alert', 'hushyor, sergak'), G('stabilise', 'barqarorlashtirmoq'), G('intense', 'jadal, kuchli'),
      G('ironically', 'ajablanarlisi shundaki'), G('dread', 'qoʻrqmoq, xavotir bilan kutmoq'),
      G('dim', 'xira (yorugʻlik)'), G('underlying', 'asosiy, yashirin (sabab)'), G('sensible', 'oqilona')],
     [GN('i37-verb-ing', '-ing shakli ega vazifasida: Going to bed … helps',
         'Going to bed and getting up at roughly the same time every day, including weekends, helps'),
      GN('i61-although-despite', 'although — «garchi … boʻlsa ham»',
         'although intense exercise just before bed may have the opposite effect')],
     [
         hd(0, H3, 1, 'Xatboshi A: uyqusizlik — bitta yomon kecha emas («more than an occasional bad night»): u uzoq davom etadi '
                      'va ertasi kunga ham taʼsir qiladi, yaʼni haqiqiy muammoga aylanadi.'),
         hd(1, H3, 6, 'Xatboshi B: «There is rarely a single cause» — stress, muhit, ish tartibi, kofein: turli sabablar.'),
         hd(2, H3, 7, 'Xatboshi C: kechki ekran yorugʻligi va diqqatni tortadigan kontent. «Screens that help the mind '
                      'relax» — ekran bor, lekin matn aksini aytadi.'),
         hd(3, H3, 3, 'Xatboshi D: «sleep hygiene» — muntazam vaqt, qorongʻi xona, kunduzgi harakat.'),
         hd(4, H3, 5, 'Xatboshi E: uyqu haqidagi xavotirning oʻzi uyqusizlikni kuchaytiradi — yopiq doira.'),
         hd(5, H3, 2, 'Xatboshi F: qachon shifokorga borish kerak: bir necha hafta davom etsa, kayfiyatga taʼsir qilsa va hokazo.'),
         tf('Short periods of insomnia are rare.', 'F',
            '«Short episodes are very common» — qisqa davrlar juda koʻp uchraydi.', 0, ng=True),
         tf('Insomnia is more common among people who live in cities than in the countryside.', 'NG',
            'Shovqinli koʻcha tilga olingan, lekin shahar va qishloq solishtirilmagan.', 1),
         gap('Specialists advise keeping the bedroom dark, quiet and ___.', 'cool',
             '«The bedroom should ideally be dark, quiet and cool».', 3, 1),
         tf('Checking the time repeatedly during the night can make sleeping more difficult.', 'T',
            '«Watching the clock … only adds to the pressure» — bosimni oshiradi.', 4, ng=True),
     ])

# ---------------------------------------------------------------- 4. Architecture
H4 = ['Towers built for defence', 'Keeping whole districts cool', 'Traditional wisdom rediscovered',
      'Turning the breeze downwards', 'Walls that slow down the heat', 'Lessons rather than copies',
      'Half indoors, half outdoors', 'The art of carving wood', 'A private world looking inward']

text(B, 'b2-14-architecture', 'Arxitektura va iqlim', 'Architecture and Climate', 'B2', 'exam',
     L('Arxitektura', 'Architecture'),
     'Topshiriq: Matching headings, True/False/Not Given va gap. Sarlavhalarga qarashdan oldin xatboshining mazmunini '
     'oʻzbekcha 3–5 soʻz bilan ifodalang, masalan «qalin devor issiqni ushlaydi». Soʻng shu gʻoyaga eng yaqin sarlavhani qidiring.',
     [
         P("Long before electric fans and air conditioning, people living in some of the hottest places on Earth managed to "
           "keep their homes comfortable. They did so not with machines but with careful design, using local materials and "
           "knowledge passed down through generations. Today, as the cost of cooling buildings rises and summers become "
           "hotter in many regions, architects are taking a fresh look at these traditional solutions."),
         P("One of the most important features was the wall itself. Houses across Central Asia and the Middle East were "
           "traditionally built from mud brick or packed earth, often with walls of considerable thickness. Such walls "
           "absorb the heat of the sun very slowly, so that often, by the time the warmth reaches the interior, the day is almost over. "
           "At night, when the air outside cools, the stored heat escapes again. Small windows further limited the amount "
           "of sunlight entering the rooms."),
         P("Many homes were also organised around an open courtyard, known in Uzbekistan as a hovli. Instead of facing the "
           "hot, dusty street, the rooms looked inward onto this private space. Trees and vines provided shade, and a small "
           "pool or channel of water helped to cool the air as it evaporated. The courtyard was not only a cooling device "
           "but also the centre of family life, where children played and guests were received."),
         P("Facing the courtyard, many Uzbek houses had an ayvon, a covered veranda supported by wooden columns that were "
           "often beautifully carved. This semi-open space allowed air to move freely while keeping out the direct rays of "
           "the sun. During the hottest months, families would spend much of the day there, eating, working and resting, "
           "and on summer nights some people even slept outdoors."),
         P("In parts of Iran and the Persian Gulf, builders developed an even more ingenious solution: the wind catcher. "
           "These tall towers rise above the roofline and have openings near the top to capture breezes, which are usually "
           "stronger higher up than at street level. The moving air is directed down into the rooms below, while warmer air "
           "is pushed out. In some buildings, the air passes over water or through underground spaces first, which cools "
           "it further."),
         P("Cooling was considered at the scale of whole towns as well. In many old cities, narrow, winding streets and "
           "closely packed houses meant that buildings shaded one another and the lanes between them for much of the day. "
           "In some regions, walls were finished in pale colours, which reflect rather than absorb sunlight. On a summer "
           "afternoon, the old quarter of such a city can feel noticeably cooler than a wide modern avenue."),
         P("None of this means that modern cities should simply copy the past. People today expect more light, more space "
           "and different standards of comfort. Nevertheless, many architects argue that the principles behind traditional "
           "buildings, such as using thick walls to delay heat, shading open spaces and allowing air to flow naturally, can "
           "be combined with modern materials. Buildings designed in this way may need far less energy for cooling."),
     ],
     [G('air conditioning', 'havoni sovutish tizimi, konditsioner'), G('generation', 'avlod'), G('feature', 'xususiyat, element'),
      G('mud brick', 'xom gʻisht'), G('considerable', 'ancha katta'), G('absorb', 'yutmoq, singdirmoq'),
      G('interior', 'ichki qism'), G('courtyard', 'hovli'), G('evaporate', 'bugʻlanmoq'),
      G('veranda', 'ayvon, peshayvon'), G('carved', 'oʻymakor, naqsh oʻyilgan'), G('ingenious', 'mohirona oʻylab topilgan, topqir'),
      G('capture', 'tutib olmoq'), G('winding', 'egri-bugri'), G('reflect', 'qaytarmoq (nurni)'),
      G('principle', 'tamoyil')],
     [GN('c45-time-clauses', 'by the time … — «… ga qadar»',
         'by the time the warmth reaches the interior, the day is almost over'),
      GN('i12-used-to-would', 'would — oʻtmishdagi odat', 'families would spend much of the day there')],
     [
         hd(0, H4, 2, 'Xatboshi A: elektr va konditsionerdan oldingi anʼanaviy yechimlarga meʼmorlar qayta qaramoqda.'),
         hd(1, H4, 4, 'Xatboshi B: qalin loy devor issiqni sekin yutadi — issiqlik ichkariga kech kiradi.'),
         hd(2, H4, 8, 'Xatboshi C: xonalar koʻchaga emas, ichkaridagi hovliga qaragan — shaxsiy, ichkariga yoʻnalgan makon.'),
         hd(3, H4, 6, 'Xatboshi D: ayvon — yarim ochiq makon, oilalar kun boʻyi shu yerda. «The art of carving wood» — '
                      'oʻymakor ustunlar faqat tafsilot.'),
         hd(4, H4, 3, 'Xatboshi E: shamol ushlagich minoralar shabadani pastga, xonalarga yoʻnaltiradi. «Towers built for '
                      'defence» — minora bor, lekin mudofaa haqida emas.'),
         hd(5, H4, 1, 'Xatboshi F: tor koʻchalar, zich uylar va och rangli devorlar butun mahallani salqin saqlaydi.'),
         hd(6, H4, 5, 'Xatboshi G: oʻtmishni nusxalash emas, balki uning tamoyillaridan saboq olish.'),
         tf('Thick earth walls give back the heat they have stored once the outside air cools at night.', 'T',
            '«At night, when the air outside cools, the stored heat escapes again».', 1, ng=True),
         gap('In a hovli, a pool or channel of water cooled the air as the water ___.', 'evaporated',
             '«helped to cool the air as it evaporated».', 2, 1),
         tf('Wind catchers are still included in many new houses in Iran today.', 'NG',
            'Matnda shamol ushlagichlar qanday ishlashi aytilgan, bugungi yangi uylar haqida maʼlumot yoʻq.', 4),
         tf('The writer believes modern cities should reproduce traditional buildings exactly.', 'F',
            '«None of this means that modern cities should simply copy the past» — nusxalash emas, tamoyillar.', 6, ng=True),
     ])

# ---------------------------------------------------------------- 5. AI and work
H5 = ['Machines that never make mistakes', 'Uncertain forecasts', 'What the past can and cannot teach',
      'Parts of a job, not the whole', 'Jobs that have already vanished', 'Opportunities that did not exist before',
      'Risks and limits', 'Preparing to keep up', 'An outcome shaped by human choices']

text(B, 'b2-15-ai-work', 'Sunʼiy intellekt va ish', 'Artificial Intelligence and Work', 'B2', 'exam',
     L('Texnologiya', 'Technology'),
     'Topshiriq: Matching headings, True/False/Not Given va gap. Javobni yakunlashdan oldin tekshiring: sarlavha butun '
     'xatboshini qamrab oladimi yoki faqat bitta misol yoki jumlanimi? Misollar — tafsilot, asosiy gʻoya emas.',
     [
         P("Few technologies have produced as much discussion in such a short time as artificial intelligence. Tools that "
           "can draft letters, summarise long reports, translate texts and recognise images are now used in offices, "
           "hospitals and classrooms. Opinions about what this means for employment vary enormously. Some commentators "
           "expect dramatic job losses, while others believe the changes will be gradual. The honest answer is that nobody "
           "knows for certain, and confident predictions in either direction should be treated with caution."),
         P("History offers some perspective, although it cannot tell us exactly what will happen. When machines first "
           "appeared in factories during the Industrial Revolution, many workers feared, with good reason, that their "
           "skills would no longer be needed. Some occupations did largely disappear. Over the following decades, however, "
           "entirely new industries and types of work emerged, many of which earlier generations could not have imagined. "
           "Whether the same pattern will repeat itself is one of the central questions of the debate."),
         P("One useful way to think about the issue is to look at tasks rather than whole jobs. Most jobs consist of many "
           "different activities, some routine and some requiring judgement, creativity or personal contact. AI tools are "
           "generally best at the routine part: sorting documents, filling in forms, checking data or producing a first "
           "draft. As a result, in many professions the technology may change what people spend their time on rather than "
           "replace them entirely."),
         P("At the same time, new roles are appearing. Organisations need people to design, test and maintain AI systems, "
           "to prepare the data they learn from and to make sure they are used fairly and safely. Other positions involve "
           "explaining the technology to customers or combining it with expert knowledge in fields such as medicine, law or "
           "education. Some of the jobs that will be common in twenty years may not even have names yet."),
         P("This does not mean the transition will be painless. Workers whose jobs consist mainly of routine tasks may find "
           "their positions under real pressure, and there is no guarantee that the benefits will be shared evenly. There "
           "are also practical concerns. AI systems can produce answers that sound convincing but are simply wrong, which "
           "means that human checking remains essential, especially where mistakes could be costly or dangerous."),
         P("For individuals, the most widely shared advice concerns skills. Being able to use digital tools confidently is "
           "increasingly important, but so are abilities that machines find difficult, such as critical thinking, "
           "communication, teamwork and adaptability. Perhaps the most valuable skill of all is the willingness to keep "
           "learning throughout one's career, since the tools themselves are likely to keep changing."),
         P("In the end, the effect of artificial intelligence on work will depend not only on the technology but also on the "
           "decisions people make about how to use it. Governments, companies and workers will all shape the outcome. For a "
           "country like Uzbekistan, with a large and young population, investing in education, languages and digital "
           "skills could help to ensure that the changes bring new opportunities rather than new problems."),
     ],
     [G('summarise', 'qisqacha bayon qilmoq'), G('employment', 'bandlik, ish bilan taʼminlanish'),
      G('dramatic', 'keskin, katta'), G('gradual', 'asta-sekin boʻladigan'), G('caution', 'ehtiyotkorlik'),
      G('perspective', 'nuqtai nazar, kengroq qarash'), G('occupation', 'kasb'), G('emerge', 'paydo boʻlmoq'),
      G('routine', 'bir xil takrorlanadigan, odatiy'), G('judgement', 'mulohaza, toʻgʻri baho bera olish'),
      G('maintain', 'xizmat koʻrsatmoq, saqlab turmoq'), G('transition', 'oʻtish davri'),
      G('convincing', 'ishonarli'), G('essential', 'zarur, muhim'), G('adaptability', 'moslashuvchanlik'),
      G('willingness', 'tayyorlik, xohish')],
     [GN('c33-relative-advanced', 'many of which — murakkab nisbiy gap',
         'many of which earlier generations could not have imagined'),
      GN('i30-passive-tenses', 'Modal + majhul: should be treated',
         'confident predictions in either direction should be treated with caution')],
     [
         hd(0, H5, 1, 'Xatboshi A: fikrlar juda xilma-xil, «nobody knows for certain» — bashoratlar noaniq.'),
         hd(1, H5, 2, 'Xatboshi B: sanoat inqilobi tajribasi — tarix «some perspective» beradi, lekin aniq javob bermaydi. '
                      '«Jobs that have already vanished» — bir jumla, butun xatboshi emas.'),
         hd(2, H5, 3, 'Xatboshi C: butun ish emas, uning ayrim vazifalari (routine part) avtomatlashadi.'),
         hd(3, H5, 5, 'Xatboshi D: yangi rollar paydo boʻlmoqda, baʼzilarining hali nomi ham yoʻq.'),
         hd(4, H5, 6, 'Xatboshi E: oʻtish davri xavflari va SI xatolari. «Machines that never make mistakes» — matn aksini '
                      'aytadi: SI xato qilishi mumkin.'),
         hd(5, H5, 7, 'Xatboshi F: koʻnikmalar va umr boʻyi oʻrganish — oʻzgarishlarga moslashish uchun tayyorgarlik.'),
         hd(6, H5, 8, 'Xatboshi G: natija texnologiyaga emas, odamlarning qarorlariga ham bogʻliq.'),
         tf('The writer states that AI will certainly lead to large-scale unemployment.', 'F',
            '«nobody knows for certain» — muallif aniq bashorat qilmaydi, aksincha ehtiyotkorlikka chaqiradi.', 0, ng=True),
         gap('AI tools tend to be most effective at the ___ part of a job.', 'routine',
             '«AI tools are generally best at the routine part».', 2, 1),
         tf('AI systems sometimes give answers that seem believable but are incorrect.', 'T',
            '«answers that sound convincing but are simply wrong».', 4, ng=True),
         tf('Most companies in Uzbekistan already use AI tools in their daily work.', 'NG',
            'Oʻzbekiston haqida faqat yosh aholi va taʼlimga sarmoya aytilgan; kompaniyalar haqida maʼlumot yoʻq.', 6),
     ])
