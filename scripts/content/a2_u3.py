"""A2 · 3-boʻlim: Bayramlar va anʼanalar (5 ta matn)"""
from lib import *

B = 'a2'
HOL = L('Bayramlar', 'Holidays')

text(B, 'a2-11-navruz', 'Navroʻz', 'Navruz', 'A2', 'article', HOL,
     'Bu maqola Navroʻz bayrami va uning anʼanalari haqida. Oʻqishdan oldin oʻylab koʻring: sizning oilangiz Navroʻzda nima qiladi?',
     [
         P("Navruz is one of the oldest holidays in Central Asia. People celebrate it on 21 March, at the start of spring. "
           "In Uzbekistan, it is a public holiday, so schools and many offices are closed. For many families, it is the beginning of a new year.",
           "Navroʻz — Markaziy Osiyodagi eng qadimiy bayramlardan biri. Odamlar uni 21-martda, bahor boshlanishida nishonlaydi. "
           "Oʻzbekistonda bu dam olish kuni, shuning uchun maktablar va koʻplab idoralar yopiq boʻladi. Koʻp oilalar uchun bu yangi yilning boshlanishidir."),
         P("Before the holiday, people clean their houses and streets. They plant trees and flowers. Many people buy new clothes. "
           "They want to start the new year with a clean home and a happy heart.",
           "Bayramdan oldin odamlar uylari va koʻchalarini tozalaydi. Ular daraxt va gul ekadi. Koʻpchilik yangi kiyim sotib oladi. "
           "Ular yangi yilni toza uy va quvnoq koʻngil bilan boshlashni xohlaydi."),
         P("The most famous Navruz dish is sumalak. It is made from sprouted wheat. It is cooked in a very big pot for many hours, often all night. "
           "Neighbours and relatives come and stir it in turns. They talk, sing songs and make wishes.",
           "Navroʻzning eng mashhur taomi — sumalak. U undirilgan bugʻdoydan tayyorlanadi. U juda katta qozonda koʻp soat, koʻpincha tun boʻyi pishiriladi. "
           "Qoʻni-qoʻshnilar va qarindoshlar kelib, uni navbat bilan kavlashadi. Ular suhbatlashadi, qoʻshiq aytadi va niyat qiladi."),
         P("On the day of Navruz, people visit their relatives and friends. They also cook halim, a dish of wheat and meat. "
           "In the parks, there are concerts, games and traditional sports.",
           "Navroʻz kuni odamlar qarindosh va doʻstlarinikiga boradi. Ular halim ham pishiradi — bu bugʻdoy va goʻshtdan qilinadigan taom. "
           "Bogʻlarda konsertlar, oʻyinlar va milliy sport musobaqalari boʻladi."),
     ],
     [G('celebrate', 'nishonlamoq'), G('public holiday', 'rasmiy dam olish kuni, bayram'), G('beginning', 'boshlanish'),
      G('plant', 'ekmoq'), G('dish', 'taom; idish'), G('sprouted wheat', 'undirilgan bugʻdoy'), G('pot', 'qozon'),
      G('stir', 'kavlamoq, aralashtirmoq'), G('in turns', 'navbat bilan'), G('make a wish', 'niyat qilmoq'),
      G('relatives', 'qarindoshlar')],
     [GN('e19-passive', 'Majhul nisbat: It is made from …', 'It is made from sprouted wheat.'),
      GN('e49-at-on-in-time', 'Vaqt predloglari: on 21 March, at the start', 'People celebrate it on 21 March')],
     [
         tf('People celebrate Navruz on 21 March.', 'T', '1-xatboshi: «People celebrate it on 21 March».', 0),
         tf('Schools are open on Navruz in Uzbekistan.', 'F',
            'Bu dam olish kuni: «so schools and many offices are closed».', 0),
         ch('What do people do before the holiday?', ['They clean their houses.', 'They cook halim.', 'They go to concerts.'], 0,
            '«Before the holiday, people clean their houses and streets.» Halim va konsertlar — bayram kunining oʻzida.', 1),
         gap('Sumalak is made from sprouted ___.', 'wheat', '«It is made from sprouted wheat.»', 2),
         ch('Why do neighbours and relatives come to the sumalak pot?', ['to buy sumalak', 'to stir it in turns', 'to clean the pot'], 1,
            '«Neighbours and relatives come and stir it in turns.»', 2),
         tf('Sumalak is cooked quickly, in one hour.', 'F', 'U uzoq pishiriladi: «for many hours, often all night» — koʻp soat, koʻpincha tun boʻyi.', 2),
         gap('Halim is a dish of wheat and ___.', 'meat', '«halim, a dish of wheat and meat».', 3),
         ch('Where are there concerts and games?', ['at schools', 'in the parks', 'in offices'], 1,
            '«In the parks, there are concerts, games and traditional sports.»', 3),
     ])

text(B, 'a2-12-wedding', 'Oʻzbek toʻyi', 'An Uzbek Wedding', 'A2', 'story', L('Anʼanalar', 'Traditions'),
     'Kamola akasining toʻyi haqida hikoya qiladi. Oʻqishdan oldin oʻylab koʻring: siz oxirgi marta qachon toʻyda boʻlgansiz?',
     [
         P("My name is Kamola. Last summer, my older brother Sardor got married. In Uzbekistan, a wedding is a big event for the whole family. "
           "We started to prepare two months before the day. My parents invited more than three hundred guests!",
           "Mening ismim Kamola. Oʻtgan yozda akam Sardor uylandi. Oʻzbekistonda toʻy butun oila uchun katta voqea. "
           "Biz toʻydan ikki oy oldin tayyorgarlik koʻrishni boshladik. Ota-onam uch yuzdan ortiq mehmon taklif qildi!"),
         P("My mother and my aunts were very busy. They cleaned the house, bought new dishes and made a lot of sweets. "
           "My father and his friends found a big restaurant for the party. Everybody helped, even my little cousins.",
           "Onam va xolalarim juda band edi. Ular uyni tozalashdi, yangi idishlar sotib olishdi va juda koʻp shirinlik tayyorlashdi. "
           "Otam va uning doʻstlari bazm uchun katta restoran topishdi. Hamma yordam berdi, hatto kichkina amakivachchalarim ham."),
         P("On the morning of the wedding, there was a special plov called nahor oshi. Many men from our neighbourhood came to it. "
           "They ate plov early in the morning and gave their good wishes to my brother.",
           "Toʻy kuni ertalab nahor oshi deb ataladigan maxsus osh boʻldi. Unga mahallamizdan koʻplab erkaklar keldi. "
           "Ular erta tongda osh yeyishdi va akamga ezgu tilaklarini bildirishdi."),
         P("In the evening, the main party started at the restaurant. The bride wore a beautiful white dress. There was live music, "
           "and everybody danced for hours. The tables were full of fruit, salads and delicious food.",
           "Kechqurun asosiy bazm restoranda boshlandi. Kelin chiroyli oq libos kiygan edi. Jonli musiqa yangradi, "
           "hamma soatlab raqsga tushdi. Dasturxonlar meva, salatlar va mazali taomlarga toʻla edi."),
         P("It was a long and tiring day, but I was very happy. Now I have a sister-in-law, and our family is bigger!",
           "Bu uzoq va charchatadigan kun boʻldi, lekin men juda xursand edim. Endi mening kelinoyim bor, oilamiz esa kattaroq boʻldi!"),
     ],
     [G('got married', 'turmush qurdi, uylandi (get married)'), G('whole', 'butun'), G('prepare', 'tayyorlanmoq, tayyorlamoq'),
      G('invite', 'taklif qilmoq'), G('guest', 'mehmon'), G('busy', 'band'), G('neighbourhood', 'mahalla'),
      G('wishes', 'tilaklar'), G('bride', 'kelin'), G('live music', 'jonli musiqa'), G('tiring', 'charchatadigan'),
      G('sister-in-law', 'kelinoyi; yanga')],
     [GN('e06-past-regular', 'Past Simple: -ed bilan (invited, started)', 'My parents invited more than three hundred guests'),
      GN('e07-past-irregular', 'Past Simple: notoʻgʻri feʼllar (wear → wore)', 'The bride wore a beautiful white dress.')],
     [
         tf('Sardor got married last summer.', 'T', '«Last summer, my older brother Sardor got married.»', 0),
         ch('When did the family start to prepare?', ['two weeks before the day', 'two months before the day', 'one year before the day'], 1,
            '«We started to prepare two months before the day.»', 0),
         gap('The parents invited more than three ___ guests.', 'hundred', '«more than three hundred guests».', 0),
         tf('Only Kamola\'s mother prepared for the wedding.', 'F',
            'Hamma yordam berdi: «Everybody helped, even my little cousins.»', 1),
         ch('What is nahor oshi?', ['a wedding dress', 'a morning plov', 'a kind of music'], 1,
            '«On the morning of the wedding, there was a special plov called nahor oshi.»', 2),
         tf('The main party was in the morning.', 'F', 'Asosiy bazm kechqurun: «In the evening, the main party started».', 3),
         gap('The bride wore a beautiful ___ dress.', 'white', '«The bride wore a beautiful white dress.»', 3),
         ch('How did Kamola feel at the end of the day?', ['tired but happy', 'sad and bored', 'angry'], 0,
            '«It was a long and tiring day, but I was very happy.»', 4),
     ])

text(B, 'a2-13-hayit', 'Hayit', 'Hayit', 'A2', 'blog', HOL,
     'Aziza oʻz blogida oilasi Hayitni qanday oʻtkazishini yozadi. Oʻqishdan oldin oʻylab koʻring: bayram kunlari kimlarnikiga borasiz?',
     [
         P("Hi everyone! My name is Aziza, and today I want to write about Hayit. In Uzbekistan, there are two Hayit holidays every year. "
           "Ramazon Hayiti is at the end of Ramadan, the month of fasting. Qurbon Hayiti comes later in the year. Both days are public holidays.",
           "Hammaga salom! Mening ismim Aziza, bugun Hayit haqida yozmoqchiman. Oʻzbekistonda har yili ikkita hayit bayrami boʻladi. "
           "Ramazon hayiti roʻza oyi boʻlgan Ramazonning oxirida keladi. Qurbon hayiti esa yilning keyinroq qismida keladi. Ikkala kun ham dam olish kuni."),
         P("The day before Hayit, my mother and grandmother are always busy in the kitchen. They make sweets, fried pastries and plov. "
           "I help them, and my brother cleans the yard. Our home smells of fresh bread and sweets.",
           "Hayitdan bir kun oldin onam va buvim doim oshxonada band boʻlishadi. Ular shirinliklar, yogʻda pishirilgan pishiriqlar va osh tayyorlashadi. "
           "Men ularga yordam beraman, akam esa hovlini tozalaydi. Uyimizdan yangi non va shirinliklarning hidi kelib turadi."),
         P("On the morning of Hayit, we wear our best clothes. Then we visit our relatives and neighbours. "
           "Children greet the elders, and the elders give them sweets or a little money. We also visit old people who live alone.",
           "Hayit kuni ertalab biz eng yaxshi kiyimlarimizni kiyamiz. Keyin qarindoshlarimiz va qoʻshnilarimiznikiga boramiz. "
           "Bolalar kattalar bilan salomlashib, ularni bayram bilan tabriklaydi, kattalar esa ularga shirinlik yoki ozgina pul beradi. Biz yolgʻiz yashaydigan keksalarni ham yoʻqlaymiz."),
         P("Hayit is also a time to help people in need. Many families share food with poor neighbours. "
           "My grandfather says this is the most important part of the holiday.",
           "Hayit — muhtojlarga yordam berish vaqti hamdir. Koʻp oilalar kambagʻal qoʻshnilari bilan taom baham koʻradi. "
           "Bobomning aytishicha, bu bayramning eng muhim qismi."),
         P("What do you do on holidays? Write in the comments!",
           "Siz bayramlarda nima qilasiz? Izohlarda yozing!"),
     ],
     [G('fasting', 'roʻza tutish'), G('both', 'ikkalasi ham'), G('busy', 'band'), G('fried pastries', 'yogʻda pishirilgan pishiriqlar (masalan, bugʻirsoq)'),
      G('yard', 'hovli'), G('smell of', '… hidi kelmoq'), G('greet', 'salomlashmoq'), G('elders', 'kattalar, yoshi ulugʻlar'),
      G('alone', 'yolgʻiz'), G('people in need', 'muhtojlar'), G('share', 'baham koʻrmoq, boʻlishmoq')],
     [GN('e43-all-every-both', 'both — ikkalasi ham', 'Both days are public holidays.'),
      GN('e46-superlatives', 'Orttirma daraja: the most important', 'this is the most important part of the holiday')],
     [
         tf('There are two Hayit holidays every year in Uzbekistan.', 'T',
            '«In Uzbekistan, there are two Hayit holidays every year.»', 0),
         ch('When is Ramazon Hayiti?', ['at the start of Ramadan', 'at the end of Ramadan', 'on 21 March'], 1,
            '«Ramazon Hayiti is at the end of Ramadan».', 0),
         tf('Aziza\'s brother cooks plov the day before Hayit.', 'F',
            'Akasi hovlini tozalaydi: «my brother cleans the yard». Oshni onasi va buvisi tayyorlaydi.', 1),
         gap('On the morning of Hayit, the family wears their best ___.', 'clothes', '«we wear our best clothes».', 2),
         ch('What do the elders give to children?', ['books', 'sweets or a little money', 'new clothes'], 1,
            '«the elders give them sweets or a little money».', 2),
         tf('The family visits old people who live alone.', 'T', '«We also visit old people who live alone.»', 2),
         gap('Many families share ___ with poor neighbours.', 'food', '«Many families share food with poor neighbours.»', 3),
         ch('What is the most important part of the holiday for the grandfather?',
            ['eating sweets', 'wearing new clothes', 'helping people in need'], 2,
            'Bobosi muhtojlarga yordamni nazarda tutadi: «this is the most important part of the holiday».', 3),
     ])

text(B, 'a2-14-new-year', 'Yangi yil', 'New Year', 'A2', 'email', HOL,
     'Dilshod chet ellik doʻsti Tomga Yangi yil rejalari haqida xat yozadi. Oʻqishdan oldin oʻylab koʻring: siz Yangi yilni qayerda kutib olasiz?',
     [
         P("Hi Tom, Thanks for your email. You asked about New Year in Uzbekistan. It is a very popular holiday here, "
           "and 1 January is a day off. Children love it because they get presents.",
           "Salom, Tom! Xating uchun rahmat. Sen Oʻzbekistondagi Yangi yil haqida soʻragan eding. Bu yerda u juda mashhur bayram, "
           "1-yanvar esa dam olish kuni. Bolalar uni yaxshi koʻradi, chunki ular sovgʻa oladi."),
         P("On 31 December, we are going to celebrate at my grandparents' house. My mother and my aunt are going to cook a lot of food. "
           "We always have a big family dinner with salads, meat and fruit. At midnight, everybody is going to say Happy New Year to each other.",
           "31-dekabrda biz bobom va buvimnikida bayram qilamiz. Onam va xolam juda koʻp ovqat pishirishadi. "
           "Bizda doim salatlar, goʻsht va mevalar bilan toʻla katta dasturxon boʻladi. Yarim tunda hamma bir-birini Yangi yil bilan tabriklaydi."),
         P("Before the holiday, the streets in Tashkent look beautiful. There are big New Year trees and bright lights in the squares. "
           "At midnight, there are fireworks in the sky.",
           "Bayramdan oldin Toshkent koʻchalari chiroyli koʻrinadi. Maydonlarda katta archalar va yorqin chiroqlar boʻladi. "
           "Yarim tunda osmonda mushaklar otiladi."),
         P("I am going to give my little sister a toy and my parents a photo book. I hope they will give me a new phone! "
           "What are your plans for New Year? Write soon, Dilshod",
           "Men singlimga oʻyinchoq, ota-onamga esa fotoalbom sovgʻa qilmoqchiman. Umid qilamanki, ular menga yangi telefon sovgʻa qilishadi! "
           "Sening Yangi yil rejalaring qanday? Tezroq javob yoz. Dilshod"),
     ],
     [G('popular', 'mashhur, ommabop'), G('day off', 'dam olish kuni'), G('present', 'sovgʻa'),
      G('grandparents', 'buvi va bobo'), G('midnight', 'yarim tun'), G('each other', 'bir-birini'),
      G('New Year tree', 'archa (Yangi yil archasi)'), G('bright', 'yorqin'), G('square', 'maydon'),
      G('fireworks', 'mushak, feyerverk'), G('toy', 'oʻyinchoq'), G('plans', 'rejalar')],
     [GN('e22-going-to', 'be going to — reja va niyat', 'My mother and my aunt are going to cook a lot of food.'),
      GN('e49-at-on-in-time', 'Vaqt predloglari: on 31 December, at midnight', 'At midnight, there are fireworks in the sky.')],
     [
         tf('1 January is a day off in Uzbekistan.', 'T', '«1 January is a day off».', 0),
         ch('Why do children love New Year?', ['They get presents.', 'They go to school.', 'They cook food.'], 0,
            '«Children love it because they get presents.»', 0),
         ch('Where is Dilshod\'s family going to celebrate?', ['at a restaurant', 'at a friend\'s house', 'at his grandparents\' house'], 2,
            '«we are going to celebrate at my grandparents\' house».', 1),
         tf('Dilshod is going to cook the food.', 'F',
            'Ovqatni onasi va xolasi pishiradi: «My mother and my aunt are going to cook a lot of food.»', 1),
         gap('There are big New Year trees and bright lights in the ___.', 'squares',
            '«There are big New Year trees and bright lights in the squares.»', 2),
         tf('There are fireworks at midnight.', 'T', '«At midnight, there are fireworks in the sky.»', 2),
         gap('Dilshod is going to give his little sister a ___.', 'toy', '«I am going to give my little sister a toy».', 3),
         ch('What does Dilshod hope to get?', ['a toy', 'a photo book', 'a new phone'], 2,
            '«I hope they will give me a new phone!» Fotoalbomni u ota-onasiga beradi.', 3),
     ])

text(B, 'a2-15-world-holidays', 'Boshqa mamlakatlarda bayramlar', 'Holidays Around the World', 'A2', 'dialogue',
     L('Dunyo', 'The world'),
     'Ingliz tili darsida oʻqituvchi va oʻquvchilar boshqa mamlakatlarning bayramlari haqida gaplashadi. Oʻqishdan oldin oʻylab koʻring: siz qaysi xorijiy bayramlarni bilasiz?',
     [
         P("Ms Rahimova: Today we are talking about holidays in other countries. Sardor, what do you know about Chinese New Year? "
           "Sardor: It is the biggest holiday in China. The date changes every year because it follows the lunar calendar.",
           "Rahimova xonim: Bugun boshqa mamlakatlardagi bayramlar haqida gaplashamiz. Sardor, Xitoy Yangi yili haqida nimalarni bilasan? "
           "Sardor: Bu Xitoydagi eng katta bayram. Uning sanasi har yili oʻzgaradi, chunki u oy taqvimiga asoslanadi."),
         P("Ms Rahimova: That's right. It usually comes in January or February. How do people decorate their homes? "
           "Sardor: They use a lot of red, because red is a lucky colour. Children often get money in red envelopes.",
           "Rahimova xonim: Toʻgʻri. U odatda yanvar yoki fevralga toʻgʻri keladi. Odamlar uylarini qanday bezaydi? "
           "Sardor: Ular qizil rangdan koʻp foydalanadi, chunki qizil — omadli rang. Bolalar koʻpincha qizil konvertlarda pul oladi."),
         P("Ms Rahimova: Very good. Laylo, can you tell us about Diwali? "
           "Laylo: Yes. Diwali is the festival of lights in India. People light small lamps and candles in their homes, and they wear new clothes and share sweets.",
           "Rahimova xonim: Juda yaxshi. Laylo, bizga Divali haqida aytib bera olasanmi? "
           "Laylo: Ha. Divali — Hindistondagi chiroqlar bayrami. Odamlar uylarida kichik chiroqlar va shamlar yoqadi, yangi kiyim kiyadi va shirinliklar ulashadi."),
         P("Ms Rahimova: Excellent. And what about Thanksgiving? "
           "Laylo: It is a holiday in the USA. It is on the fourth Thursday of November. Families have a big dinner together, and they often eat turkey.",
           "Rahimova xonim: Ajoyib. Minnatdorchilik kuni-chi? "
           "Laylo: Bu AQShdagi bayram. U noyabrning toʻrtinchi payshanbasida nishonlanadi. Oilalar katta kechki ovqatga yigʻiladi va koʻpincha kurka goʻshti yeyishadi."),
         P("Ms Rahimova: Great. So every country has its own holidays, but people everywhere enjoy them with their families.",
           "Rahimova xonim: Zoʻr. Demak, har bir mamlakatning oʻz bayramlari bor, lekin hamma joyda odamlar bayramlarni oilasi bilan birga quvonib nishonlaydi."),
     ],
     [G('lunar calendar', 'oy taqvimi'), G('decorate', 'bezamoq'), G('lucky', 'omadli'), G('envelope', 'konvert'),
      G('festival', 'bayram, festival'), G('light', 'yoqmoq; chiroq, yorugʻlik'), G('lamp', 'chiroq'), G('candle', 'sham'),
      G('Thanksgiving', 'Minnatdorchilik kuni (AQSh bayrami)'), G('turkey', 'kurka'), G('own', 'oʻz, shaxsiy')],
     [GN('e46-superlatives', 'Orttirma daraja: the biggest', 'It is the biggest holiday in China.'),
      GN('e53-and-but-so-because', 'because — chunki', 'They use a lot of red, because red is a lucky colour.')],
     [
         tf('Chinese New Year is on the same date every year.', 'F',
            'Sana har yili oʻzgaradi: «The date changes every year because it follows the lunar calendar.»', 0),
         ch('When does Chinese New Year usually come?', ['in January or February', 'in March', 'in November'], 0,
            '«It usually comes in January or February.»', 1),
         ch('Why do people in China use a lot of red?', ['It is cheap.', 'It is a lucky colour.', 'It is the colour of winter.'], 1,
            '«because red is a lucky colour».', 1),
         gap('Children often get money in red ___.', 'envelopes', '«Children often get money in red envelopes.»', 1),
         tf('Diwali is the festival of lights in India.', 'T', '«Diwali is the festival of lights in India.»', 2),
         gap('During Diwali, people light small lamps and ___ in their homes.', 'candles',
            '«People light small lamps and candles in their homes».', 2),
         tf('Thanksgiving is in December.', 'F', 'U noyabrda: «It is on the fourth Thursday of November.»', 3),
         ch('What do American families often eat at Thanksgiving?', ['plov', 'turkey', 'sumalak'], 1,
            '«Families have a big dinner together, and they often eat turkey.»', 3),
     ])
