"""B1 · 2-boʻlim: Ilm-fan sodda tilda (Science made simple) — 5 ta matn"""
from lib import *

B = 'b1'
SCI = L('Ilm-fan', 'Science')

# 1 ─────────────────────────────────────────────────────────────────────────────
text(B, 'b1-06-blue-sky', 'Nega osmon koʻk?', 'Why Is the Sky Blue?', 'B1', 'article', SCI,
     'Bu ilmiy-ommabop maqola osmonning rangi va quyosh botishi haqida. Oʻqishdan oldin oʻylab koʻring: '
     'nega kunduzi osmon koʻk, kechqurun esa qizgʻish boʻladi?',
     [
         P("Have you ever wondered why the sky is blue on a clear day? It is one of the first questions that many children ask, "
           "and it is a surprisingly good one. The answer has nothing to do with the colour of the sea or with the colour of the air itself. "
           "In fact, the air is almost completely transparent. To understand the blue sky, we need to start with sunlight."),
         P("Sunlight looks white, but it is really a mixture of all the colours of the rainbow. You can see this when sunlight passes "
           "through a glass prism or through raindrops: the white light is separated into red, orange, yellow, green, blue and violet. "
           "Each colour travels as a wave, and the waves have different lengths. Red light has the longest waves, while blue and violet "
           "light have much shorter ones."),
         P("When sunlight enters the atmosphere, it meets billions of tiny gas molecules, mostly nitrogen and oxygen. These molecules are "
           "much smaller than the waves of light, and they scatter some of the light in all directions. However, they do not treat all "
           "colours equally. Light with short waves is scattered far more strongly than light with long waves. So blue light is bounced "
           "around the sky, and it reaches our eyes from every direction. That is why, wherever we look, the sky appears blue. This effect "
           "was explained in the nineteenth century by a British scientist, Lord Rayleigh, and it is now called Rayleigh scattering."),
         P("If violet waves are even shorter, why isn't the sky violet? There are two main reasons. The Sun sends us less violet light "
           "than blue light, and our eyes are much more sensitive to blue. As a result, the mixture of scattered colours looks blue to us."),
         P("The same idea explains red and orange sunsets. When the Sun is low in the sky, its light has to travel through much more air "
           "before it reaches us. On this long journey, most of the blue light is scattered away to the sides, so the light that finally "
           "arrives is mostly red, orange and yellow. Dust or smoke in the air can make sunsets even more colourful. And on the Moon, where "
           "there is no air at all, the sky stays black even during the day."),
     ],
     [G('wonder', 'qiziqmoq, hayron boʻlib oʻylamoq'), G('transparent', 'shaffof, tiniq'), G('mixture', 'aralashma'),
      G('prism', 'prizma (uch qirrali shisha jism)'), G('separate', 'ajratmoq, boʻlmoq'), G('wave', 'toʻlqin'),
      G('atmosphere', 'atmosfera, havo qatlami'), G('molecule', 'molekula'), G('scatter', 'sochmoq, har tomonga tarqatmoq'),
      G('equally', 'teng, bir xilda'), G('bounce', 'urilib qaytmoq, sakramoq'), G('sensitive to', '… ga sezgir'),
      G('as a result', 'natijada'), G('sunset', 'quyosh botishi')],
     [GN('i05-present-perfect', 'Present Perfect: Have you ever wondered …?',
         'Have you ever wondered why the sky is blue on a clear day?'),
      GN('i29-passive-basics', 'Majhul nisbat: is scattered',
         'Light with short waves is scattered far more strongly than light with long waves.')],
     [
         tf('Air has a strong blue colour of its own.', 'F',
            'Matnda aksi aytilgan: «the air is almost completely transparent» — havo deyarli shaffof.', 0, ng=True),
         tf('Red light has longer waves than blue light.', 'T',
            '«Red light has the longest waves, while blue and violet light have much shorter ones.»', 1, ng=True),
         tf('Lord Rayleigh discovered this effect by studying sunsets.', 'NG',
            'Matnda faqat «This effect was explained in the nineteenth century by … Lord Rayleigh» deyilgan; u buni qanday yoʻl bilan kashf etgani haqida maʼlumot yoʻq.', 2, ng=True),
         tf('At sunset, sunlight passes through less air than at midday.', 'F',
            'Aksincha: «its light has to travel through much more air» — quyosh past boʻlganda yorugʻlik koʻproq havodan oʻtadi.', 4, ng=True),
         hd(1, ['White light is a mix of colours', 'Why sunsets are red', 'The size of air molecules'], 0,
            '2-xatboshining asosiy gʻoyasi: «Sunlight looks white, but it is really a mixture of all the colours».'),
         ch('Why does the sky look blue from every direction?',
            ['because blue light is scattered all around the sky', 'because the sea reflects blue light into the sky',
             'because the Sun sends out only blue light'], 0,
            '«blue light is bounced around the sky, and it reaches our eyes from every direction». Dengiz bilan aloqasi yoʻq (1-xatboshi).', 2),
         ch('According to the text, why is the sky not violet?',
            ['Violet light has the longest waves.', 'The Sun sends less violet light, and our eyes are more sensitive to blue.',
             'Violet light cannot pass through the air at all.'], 1,
            '4-xatboshida ikki sabab bor: «The Sun sends us less violet light» va «our eyes are much more sensitive to blue».', 3),
         ch('In paragraph 3, the word "scatter" is closest in meaning to …',
            ['send in many different directions', 'make warmer', 'change into another colour'], 0,
            '«scatter some of the light in all directions» — yorugʻlikni har tomonga tarqatish.', 2),
         gap('On the Moon, there is no air, so the sky stays ___ even during the day.', ['black'],
             '«on the Moon, where there is no air at all, the sky stays black even during the day».', 4, 2),
     ])

# 2 ─────────────────────────────────────────────────────────────────────────────
text(B, 'b1-07-bees', 'Asalarilar', "My Grandfather's Bees", 'B1', 'blog', L('Tabiat', 'Nature'),
     'Bu blogda muallif bobosining asalarilari haqida yozadi. Oʻqishdan oldin oʻylab koʻring: '
     'asalarilar asal qilishdan tashqari yana qanday foyda keltiradi?',
     [
         P("Every summer, I spend a few weeks at my grandfather's house in a village in the foothills. "
           "My grandfather has kept bees for more than forty years, and his wooden hives stand in a row at the end of the garden, "
           "among apricot trees. When I was little, I was afraid of the bees. Now I help him, and I have learned that these tiny "
           "insects are far more interesting than I had imagined."),
         P("Most people think of bees as honey makers, but their most important job is pollination. When a bee visits a flower to "
           "collect nectar and pollen, some pollen sticks to its hairy body. Then, when it flies to the next flower, some of this pollen "
           "is left behind. This helps plants to produce fruit and seeds. Many of the fruits and vegetables we eat, such as apples, "
           "cherries and melons, depend on insects like bees. My grandfather always says that a village without bees would soon be "
           "a village without fruit."),
         P("Honey itself is made from nectar, the sweet liquid inside flowers. The bees carry it back to the hive, where they store it "
           "in small wax cells. Then they fan it with their wings until much of the water evaporates and the nectar becomes thick honey. "
           "When a cell is full, they close it with a thin layer of wax. A single bee makes only a tiny amount of honey in its whole life, "
           "so a full jar is the work of thousands of bees."),
         P("My favourite thing to watch is the waggle dance. When a worker bee finds a good place full of flowers, she returns to the "
           "hive and dances on the honeycomb. She moves in a figure-of-eight pattern and shakes her body during the straight part of the "
           "dance. The direction of this straight run shows the other bees which way to fly, using the position of the Sun as a guide. "
           "The longer she waggles, the farther away the flowers are."),
         P("Sadly, bees are in trouble in many parts of the world. Some pesticides that farmers spray on crops can harm or kill them. "
           "When wild meadows are turned into roads, buildings or huge fields of a single crop, bees lose the flowers they need. "
           "Diseases and parasites are another problem. My grandfather never uses strong chemicals in his garden, and he plants flowers "
           "that bloom at different times of the year. If more people did the same, bees would have a much better future."),
     ],
     [G('foothills', 'togʻ etaklari, adirlar'), G('hive', 'ari uyasi, ari qutisi'), G('insect', 'hasharot'),
      G('pollination', 'changlanish, changlatish'), G('pollen', 'gulchang'), G('nectar', 'gul shirasi, nektar'),
      G('stick to', '… ga yopishmoq'), G('depend on', '… ga bogʻliq boʻlmoq'), G('evaporate', 'bugʻlanmoq'),
      G('wax', 'mum'), G('honeycomb', 'ari kataklari, mum katak'), G('pesticide', 'pestitsid, zararkunandalarga qarshi zahar'),
      G('meadow', 'oʻtloq, yaylov'), G('bloom', 'gullamoq')],
     [GN('i08-how-long-for-since', 'Present Perfect + for: has kept … for',
         'My grandfather has kept bees for more than forty years'),
      GN('i26-second-conditional', 'Ikkinchi shart gap: If more people did …, bees would …',
         'If more people did the same, bees would have a much better future.')],
     [
         tf("The writer's grandfather has kept bees for over forty years.", 'T',
            '«My grandfather has kept bees for more than forty years».', 0, ng=True),
         tf('The writer has always enjoyed being near bees.', 'F',
            '«When I was little, I was afraid of the bees» — kichikligida ulardan qoʻrqqan.', 0, ng=True),
         tf('The grandfather sells his honey at a market in the city.', 'NG',
            'Asal qanday tayyorlanishi aytilgan, lekin bobo asalni sotishi yoki bozor haqida hech narsa yoʻq.', 2, ng=True),
         tf('One bee can produce a full jar of honey during its life.', 'F',
            '«A single bee makes only a tiny amount of honey … a full jar is the work of thousands of bees».', 2, ng=True),
         ch('According to the writer, what is the most important job of bees?',
            ['making honey', 'pollination', 'building hives'], 1,
            '«Most people think of bees as honey makers, but their most important job is pollination.»', 1),
         ch('In the waggle dance, what does the length of the waggling tell the other bees?',
            ['how far away the flowers are', 'which flowers smell the best', 'how many bees should fly out'], 0,
            '«The longer she waggles, the farther away the flowers are.» Yoʻnalishni esa toʻgʻri yugurish qismi koʻrsatadi.', 3),
         ch('What is the main idea of the last paragraph?',
            ['Honey is becoming more expensive.', 'Bees face several dangers, but people can help them.',
             "The grandfather's garden is too small for bees."], 1,
            'Xatboshida xavflar sanalgan (pestitsidlar, oʻtloqlarning yoʻqolishi, kasalliklar) va yechim: «If more people did the same…».', 4),
         gap('Bees fan the nectar with their ___ until much of the water evaporates.', ['wings'],
             '«Then they fan it with their wings until much of the water evaporates».', 2, 2),
         gap('The grandfather plants flowers that ___ at different times of the year.', ['bloom', 'flower'],
             '«he plants flowers that bloom at different times of the year».', 4, 2),
     ])

# 3 ─────────────────────────────────────────────────────────────────────────────
text(B, 'b1-08-sleep-memory', 'Uyqu va xotira', 'Sleep and Memory', 'B1', 'dialogue', SCI,
     'Oʻquvchi Jasur va oʻqituvchisi imtihon oldidan uyqu haqida suhbatlashadi. Oʻqishdan oldin oʻylab koʻring: '
     'imtihon oldidan tun boʻyi oʻqish foydalimi?',
     [
         P("Jasur: Ms Rahimova, I've got a big biology test on Friday, so I'm planning to stay up all night on Thursday and study. "
           "Do you think that's a good idea? Ms Rahimova: Honestly, Jasur, I don't. Many students believe that more hours of study "
           "always mean better results, but if you give up sleep, you may remember less, not more."),
         P("Jasur: Really? But how can sleeping help me remember? My brain is switched off when I'm asleep. Ms Rahimova: That's a "
           "common mistake. Your body rests, but your brain stays very busy. Scientists have found that during sleep, the brain goes "
           "over the things you learned during the day. It strengthens the important memories and makes them more stable, so they "
           "are less likely to be forgotten."),
         P("Jasur: So sleep is like pressing the save button on a computer? Ms Rahimova: That's a nice way to put it. New information "
           "is quite fragile at first. While you sleep, it is moved into longer-term storage and connected to things you already know. "
           "Researchers call this process memory consolidation. It happens in different stages of sleep, so a full night is better "
           "than a short nap."),
         P("Jasur: What happens if I don't sleep at all? Ms Rahimova: Then your brain doesn't get that chance. On top of that, after "
           "a sleepless night most people find it harder to concentrate, they react more slowly and they make more careless mistakes. "
           "You might know the answer to a question and still not be able to remember it in the exam."),
         P("Jasur: OK, but I really haven't studied much yet. What should I do instead? Ms Rahimova: Start today. Study a little "
           "every evening, test yourself without looking at your notes, and then go to bed at a sensible time. If you review the key "
           "points the next morning, you'll notice how much you remember."),
         P("Jasur: That sounds easier than staying up all night, to be honest. Ms Rahimova: It is, and it works better too. You'd "
           "never charge your phone for only ten minutes before a long trip, would you? Your brain needs proper time to recharge as "
           "well. Good luck on Friday, and sleep well on Thursday!"),
     ],
     [G('stay up', 'uxlamay oʻtirmoq, kech yotmoq'), G('give up', 'voz kechmoq'), G('switch off', 'oʻchmoq, oʻchirmoq'),
      G('go over', 'qayta koʻrib chiqmoq'), G('strengthen', 'mustahkamlamoq, kuchaytirmoq'), G('stable', 'barqaror, mustahkam'),
      G('fragile', 'moʻrt, nozik'), G('storage', 'saqlash joyi, xotira ombori'), G('consolidation', 'mustahkamlanish'),
      G('nap', 'qisqa uyqu (kunduzgi)'), G('concentrate', 'diqqatni jamlamoq'), G('careless', 'eʼtiborsiz, beparvo'),
      G('sensible', 'oqilona, maʼqul'), G('recharge', 'quvvat yigʻmoq, qayta zaryadlanmoq')],
     [GN('i25-if-i-do-if-i-did', 'Birinchi shart gap: If you review …, you\'ll notice …',
         "If you review the key points the next morning, you'll notice how much you remember."),
      GN('i29-passive-basics', 'Majhul nisbat: to be forgotten, is moved',
         'they are less likely to be forgotten')],
     [
         tf('Jasur has a history test on Friday.', 'F',
            'Jasur: «a big biology test on Friday» — tarix emas, biologiya.', 0, ng=True),
         tf('According to the teacher, the brain is very active during sleep.', 'T',
            '«Your body rests, but your brain stays very busy.»', 1, ng=True),
         tf('Ms Rahimova used to stay up all night before her own exams.', 'NG',
            'Oʻqituvchi oʻzining talabalik yillari haqida hech narsa aytmaydi — matnda maʼlumot yoʻq.', 0, ng=True),
         tf('The teacher says a short nap is just as good as a full night of sleep.', 'F',
            'Aksincha: «a full night is better than a short nap».', 2, ng=True),
         hd(1, ['The busy brain at night', 'Why biology is difficult', 'A plan for Friday'], 0,
            '2-xatboshi: tana dam oladi, miya esa uyquda band — kun davomida oʻrganilganlarni qayta koʻradi.'),
         ch('What does Jasur mean when he compares sleep to "pressing the save button"?',
            ['Sleep helps to keep new information safely in memory.', 'Sleep deletes information that is not important.',
             'Computers need rest just like people.'], 0,
            'Oʻqituvchi tasdiqlaydi: uyquda yangi maʼlumot «is moved into longer-term storage» — xotirada saqlanadi.', 2),
         ch('Which problem after a sleepless night is NOT mentioned by the teacher?',
            ['finding it hard to concentrate', 'reacting more slowly', 'feeling hungry all day'], 2,
            '4-xatboshida faqat «harder to concentrate», «react more slowly», «careless mistakes» aytilgan; ochlik haqida gap yoʻq.', 3),
         ch("What is the teacher's main advice to Jasur?",
            ['Study all night only before very hard tests.', 'Study a little every day and get enough sleep.',
             'Study only on the morning of the test.'], 1,
            '«Study a little every evening … and then go to bed at a sensible time.»', 4),
         gap('Researchers call the process of storing new memories during sleep memory ___.', ['consolidation'],
             '«Researchers call this process memory consolidation.»', 2, 2),
     ])

# 4 ─────────────────────────────────────────────────────────────────────────────
text(B, 'b1-09-groundwater', 'Yer osti suvlari', 'Water Under Our Feet', 'B1', 'article', L('Atrof-muhit', 'Environment'),
     'Bu maqola yer osti suvlari, quduqlar va qadimiy korizlar haqida. Oʻqishdan oldin oʻylab koʻring: '
     'quduqdagi suv qayerdan keladi?',
     [
         P("When we think of fresh water, we usually picture rivers, lakes and mountain snow. However, a huge amount of the world's "
           "fresh water is hidden under our feet. It is called groundwater, and in many dry regions, including large parts of Central "
           "Asia, people have depended on it for thousands of years."),
         P("Groundwater begins as rain or melting snow. Some of this water runs off into rivers, and some evaporates, but a part of it "
           "slowly soaks into the ground. It moves down through the soil and fills the tiny spaces between grains of sand and gravel, as "
           "well as cracks in rock. A layer of rock or sand that holds a lot of water and lets it flow is called an aquifer. Contrary to "
           "what many people imagine, most groundwater is not stored in underground lakes but in these small spaces, a bit like water "
           "in a sponge."),
         P("To reach this water, people dig or drill wells. In the past, wells were dug by hand and water was lifted with a bucket. "
           "Today, electric pumps can bring up water from much deeper aquifers. In Central Asia and neighbouring regions, people also "
           "built an ingenious system called the kariz. A kariz is an underground canal that carries water from the foothills to "
           "villages and fields. Because the water flows gently downhill by gravity, no pump is needed. A line of vertical shafts, which "
           "workers used to dig the tunnel and to remove soil, can often be seen on the surface. And because the water travels "
           "underground, less of it is lost to evaporation in the hot summer."),
         P("Groundwater is valuable, but it is not endless. Rain can refill an aquifer, but this may take many years, and for some deep "
           "aquifers it takes thousands of years. If water is pumped out faster than nature can replace it, the water table, the top "
           "level of groundwater, falls. Old wells dry up, and farmers have to drill deeper and deeper, which costs more money and energy. "
           "In some places, the ground has even sunk because so much water has been removed from beneath it."),
         P("Groundwater can also be polluted by chemicals from farms, factories and rubbish. Once this happens, cleaning it is very "
           "difficult. For this reason, experts say that we should use groundwater carefully, water crops in more efficient ways, such "
           "as drip irrigation, and protect the land above aquifers. Water that we cannot see still needs our care."),
     ],
     [G('picture', 'koʻz oldiga keltirmoq, tasavvur qilmoq'), G('groundwater', 'yer osti suvi'), G('soak into', '… ga singmoq'),
      G('grain', 'donacha, zarra'), G('gravel', 'shagʻal'), G('crack', 'yoriq, darz'), G('aquifer', 'suvli qatlam, akvifer'),
      G('sponge', 'shimgich, gubka'), G('drill', 'burgʻulamoq'), G('ingenious', 'mohirona oʻylab topilgan, zukko'),
      G('gravity', 'tortishish kuchi'), G('shaft', 'vertikal quduq, shaxta'), G('water table', 'yer osti suvi sathi'),
      G('drip irrigation', 'tomchilatib sugʻorish')],
     [GN('i29-passive-basics', 'Majhul nisbat: were dug, was lifted',
         'wells were dug by hand and water was lifted with a bucket'),
      GN('i55-non-defining', 'Ajratuvchi ergash gap: …, which workers used …, …',
         'A line of vertical shafts, which workers used to dig the tunnel and to remove soil, can often be seen on the surface.')],
     [
         tf('Most groundwater is stored in large underground lakes.', 'F',
            '«most groundwater is not stored in underground lakes but in these small spaces».', 1, ng=True),
         tf('A kariz does not need a pump because the water flows downhill.', 'T',
            '«Because the water flows gently downhill by gravity, no pump is needed.»', 2, ng=True),
         tf('The first kariz in Central Asia was built about a thousand years ago.', 'NG',
            'Korizlar qurilgani aytilgan, lekin birinchisi qachon qurilgani haqida matnda maʼlumot yoʻq.', 2, ng=True),
         tf('Refilling some deep aquifers can take thousands of years.', 'T',
            '«for some deep aquifers it takes thousands of years».', 3, ng=True),
         ch('What is an aquifer?',
            ['a deep well dug by hand', 'a layer of rock or sand that holds water and lets it flow', 'an underground lake'], 1,
            '«A layer of rock or sand that holds a lot of water and lets it flow is called an aquifer.»', 1),
         ch('According to the text, why is less water lost from a kariz in hot summers?',
            ['because the water travels underground', 'because the water moves very fast', 'because the canal is cleaned often'], 0,
            '«because the water travels underground, less of it is lost to evaporation».', 2),
         ch('What happens when water is pumped out faster than nature can replace it?',
            ['The water table rises.', 'The water table falls and old wells may dry up.', 'The groundwater becomes cleaner.'], 1,
            '«the water table … falls. Old wells dry up».', 3),
         hd(4, ['Pollution and protection', 'How wells are dug', 'Why rain falls'], 0,
            'Oxirgi xatboshi: yer osti suvi ifloslanishi va uni qanday asrash kerakligi haqida.'),
         gap('Experts suggest watering crops in more efficient ways, such as ___.', ['drip irrigation'],
             '«water crops in more efficient ways, such as drip irrigation».', 4, 2),
     ])

# 5 ─────────────────────────────────────────────────────────────────────────────
text(B, 'b1-10-solar', 'Quyosh energiyasi', 'Power from the Sun', 'B1', 'article', L('Texnologiya', 'Technology'),
     'Bu maqola quyosh panellari qanday ishlashi, ularning afzalliklari va kamchiliklari haqida. Oʻqishdan oldin oʻylab koʻring: '
     'quyosh paneli kechasi ishlaydimi?',
     [
         P("The Sun sends a huge amount of energy to the Earth every day, far more than people need. For a long time, people could only "
           "use a little of this energy directly, for example to dry fruit or to warm water. Today, solar panels allow us to turn "
           "sunlight straight into electricity, and they have become a common sight on roofs and in fields around the world."),
         P("How does a solar panel work? A panel is made of many small units called solar cells. Most of them are made from silicon, "
           "the same material that is used in computer chips. When light hits a cell, its energy knocks tiny particles called electrons "
           "loose from their atoms. The cell is designed so that these electrons can only move in one direction, and moving electrons are "
           "exactly what an electric current is. Wires collect the current, and a device called an inverter changes it into the kind of "
           "electricity that is used in our homes."),
         P("Solar power has many advantages. Once a panel has been installed, the sunlight it uses is free. Panels have no moving parts, "
           "so they are quiet and need little maintenance, and they do not produce smoke or harmful gases while they work. They are "
           "especially useful in sunny countries like Uzbekistan, where clear skies are common for much of the year. A panel on the roof "
           "of a village house or a school can provide electricity even far from the main power lines."),
         P("However, solar energy also has limits. Panels produce no electricity at night, and they produce much less on cloudy days. "
           "Dust can cover them and block the light, so in dry, windy places they need to be cleaned regularly. Surprisingly, very hot "
           "weather also reduces their efficiency a little, so a cool, bright spring day can be better for a panel than a very hot summer "
           "afternoon."),
         P("The biggest challenge is that people need electricity when the Sun is not shining. One solution is to store energy in "
           "batteries during the day and use it in the evening. Batteries are becoming cheaper and better, but they are still expensive, "
           "so many power systems combine solar energy with other sources, such as wind, water or gas. If engineers continue to improve "
           "panels and batteries, sunshine could become one of the most important sources of energy in the future."),
     ],
     [G('directly', 'bevosita, toʻgʻridan-toʻgʻri'), G('solar panel', 'quyosh paneli'), G('silicon', 'kremniy'),
      G('particle', 'zarracha'), G('knock loose', 'urib ajratib chiqarmoq'), G('current', 'elektr toki'),
      G('device', 'qurilma'), G('install', 'oʻrnatmoq'), G('maintenance', 'texnik xizmat, taʼmirlash'),
      G('harmful', 'zararli'), G('efficiency', 'samaradorlik, foydali ish koeffitsienti'), G('store', 'saqlamoq, toʻplab qoʻymoq'),
      G('combine', 'birlashtirmoq, qoʻshib ishlatmoq'), G('source', 'manba')],
     [GN('i30-passive-tenses', 'Majhul nisbat (Present Perfect): has been installed',
         'Once a panel has been installed, the sunlight it uses is free.'),
      GN('i53-who-which-that', 'Aniqlovchi ergash gap: that is used …',
         'the same material that is used in computer chips')],
     [
         tf('Most solar cells are made from silicon.', 'T',
            '«Most of them are made from silicon».', 1, ng=True),
         tf('Solar panels are noisy because they have many moving parts.', 'F',
            '«Panels have no moving parts, so they are quiet».', 2, ng=True),
         tf('Solar panels work best on the hottest days of summer.', 'F',
            '«very hot weather also reduces their efficiency a little» — salqin, yorugʻ bahor kuni yaxshiroq boʻlishi mumkin.', 3, ng=True),
         tf('Every school in Uzbekistan already has solar panels on its roof.', 'NG',
            'Matnda faqat panel maktab tomida ham elektr berishi «mumkin»ligi aytilgan; barcha maktablarda bor-yoʻqligi haqida maʼlumot yoʻq.', 2, ng=True),
         ch('What does an inverter do?',
            ['It changes the current into the kind of electricity used in homes.', 'It cleans dust from the panels.',
             'It stores energy for the night.'], 0,
            '«a device called an inverter changes it into the kind of electricity that is used in our homes».', 1),
         ch('Why do panels in dry, windy places need regular cleaning?',
            ['because rain damages them', 'because dust can block the light', 'because the wires get too hot'], 1,
            '«Dust can cover them and block the light, so in dry, windy places they need to be cleaned regularly.»', 3),
         ch("What is the writer's opinion about the future of solar energy?",
            ['It will never be useful because there is no sun at night.',
             'It could become very important if panels and batteries keep improving.',
             'It will soon replace all other sources of energy.'], 1,
            '«If engineers continue to improve panels and batteries, sunshine could become one of the most important sources».', 4),
         hd(3, ['When panels work less well', 'How electrons move', 'Free electricity for schools'], 0,
            '4-xatboshi quyosh energiyasining cheklovlari haqida: kecha, bulut, chang, issiq.'),
         gap('In the evening, people can use energy that was stored in ___ during the day.', ['batteries'],
             '«store energy in batteries during the day and use it in the evening».', 4, 2),
     ])
