"""B1 · 3-boʻlim: Tarix va madaniyat (5 ta matn)"""
from lib import *

B = 'b1'
TAG = L('Tarix va madaniyat', 'History and culture')

# 1 ─────────────────────────────────────────────────────────────── article
text(B, 'b1-11-silk-road', 'Buyuk Ipak yoʻli', 'The Great Silk Road', 'B1', 'article', TAG,
     'Bu maqola Buyuk Ipak yoʻli va u orqali nafaqat mollar, balki gʻoyalar ham tarqalgani haqida. '
     'Oʻqishdan oldin oʻylab koʻring: savdo yoʻllari orqali yana nimalar sayohat qilishi mumkin edi?',
     [
         P("For more than a thousand years, a network of trade routes connected China with the lands around the "
           "Mediterranean Sea. In the 19th century, a German geographer gave it the name the Silk Road, because Chinese "
           "silk was one of the most valuable goods that travelled along it. In fact, it was never a single road. It was "
           "a web of paths across deserts, mountains and grasslands."),
         P("Very few merchants ever travelled the whole way from one end to the other. Instead, goods were passed from "
           "hand to hand. A trader might carry silk from one city to the next, sell it there and buy something else to "
           "take home. Each time the goods changed hands, their price went up. By the time a piece of silk reached Rome "
           "or Constantinople, it had become extremely expensive."),
         P("Cities in Central Asia stood right in the middle of this network, and Samarkand and Bukhara became two of "
           "the most important. Their markets were full of goods from both East and West: silk and porcelain, spices, "
           "glass, horses and precious stones. Local craftsmen and traders grew rich, and the cities were filled with "
           "mosques, madrasas and busy bazaars."),
         P("However, the Silk Road carried much more than goods. Ideas, languages and religions travelled with the "
           "caravans. Buddhism spread from India into China along these routes, and later Islam reached many parts of "
           "Central Asia. Technologies moved too. Papermaking, which had been invented in China, reached Samarkand, and "
           "the city became famous for its paper. From there, the skill slowly spread to the Middle East and Europe."),
         P("Travelling with a caravan was slow and often dangerous. To make the journey safer, rest houses called "
           "caravanserais were built along the main routes, often about a day's journey apart. A typical caravanserai "
           "had a large courtyard where camels and horses could rest, with rooms for travellers around it. Here, "
           "merchants from different countries ate, slept and exchanged news. In Uzbekistan today, you can still see "
           "the remains of some of these buildings."),
     ],
     [G('trade route', 'savdo yoʻli'), G('network', 'tarmoq'), G('valuable', 'qimmatbaho, qadrli'),
      G('goods', 'mollar, tovarlar'), G('merchant', 'savdogar'), G('change hands', 'qoʻldan qoʻlga oʻtmoq, sotilmoq'),
      G('precious stones', 'qimmatbaho toshlar'), G('craftsman', 'hunarmand, usta'), G('spread', 'tarqalmoq'),
      G('invent', 'ixtiro qilmoq'), G('caravan', 'karvon'), G('caravanserai', 'karvonsaroy'),
      G('courtyard', 'hovli'), G('exchange news', 'yangiliklar bilan oʻrtoqlashmoq'), G('remains', 'qoldiqlar, xarobalar')],
     [GN('i11-past-perfect', 'Past Perfect: it had become',
         'By the time a piece of silk reached Rome or Constantinople, it had become extremely expensive.'),
      GN('i55-non-defining', 'Qoʻshimcha maʼlumot beruvchi ergash gap: , which …',
         'Papermaking, which had been invented in China, reached Samarkand')],
     [
         tf('The Silk Road was one long road from China to the Mediterranean.', 'F',
            'Aksincha: «it was never a single road. It was a web of paths» — bu yoʻllar tarmogʻi edi.', 0, ng=True),
         tf('The price of silk rose every time it was sold to a new trader.', 'T',
            '«Each time the goods changed hands, their price went up.»', 1, ng=True),
         tf('Traders in Samarkand had to pay a tax to the ruler of the city.', 'NG',
            'Matnda Samarqand bozorlari haqida gap bor, lekin soliq haqida hech narsa aytilmagan.', 2),
         tf('Islam reached Central Asia before Buddhism reached China.', 'F',
            '«Buddhism spread from India into China … and later Islam reached many parts of Central Asia» — '
            'Islom keyinroq kelgan.', 3, ng=True),
         ch('What is the main idea of paragraph 4?',
            ['Silk was the most expensive product on the road.',
             'The Silk Road spread ideas, religions and technologies, not only goods.',
             'Samarkand produced more paper than any other city.'], 1,
            'Xatboshi «the Silk Road carried much more than goods» deb boshlanadi va gʻoyalar, dinlar, '
            'texnologiyalar haqida gapiradi.', 3),
         ch('In paragraph 2, "the goods changed hands" means that the goods …',
            ['were sold to a new owner', 'were broken during the journey', 'were carried in both hands'], 0,
            'Avvalgi gap: «sell it there and buy something else» — mol yangi egaga sotiladi, shuning uchun narx oshadi.', 1),
         ch('Why were caravanserais built?',
            ['to sell silk to local people', 'to make the journey safer for travellers', 'to teach merchants new languages'], 1,
            '«To make the journey safer, rest houses called caravanserais were built».', 4),
         gap('Papermaking was invented in ___ and later reached Samarkand.', ['China'],
             '«Papermaking, which had been invented in China, reached Samarkand».', 3, 2),
         gap('In a caravanserai, camels and horses rested in a large ___.', ['courtyard'],
             '«a large courtyard where camels and horses could rest».', 4, 2),
     ])

# 2 ─────────────────────────────────────────────────────────────── biography
text(B, 'b1-12-navoi', 'Alisher Navoiy', 'Alisher Navoi', 'B1', 'biography', TAG,
     'Bu matn — Alisher Navoiyning qisqacha tarjimai holi. Oʻqishdan oldin oʻylab koʻring: '
     'Navoiyning qaysi asarlarini bilasiz va nega u bugun ham shunchalik hurmat qilinadi?',
     [
         P("Alisher Navoi is often called the father of Uzbek literature. Almost every city in Uzbekistan has a street, "
           "a park or a school named after him, and his portrait hangs in many libraries and classrooms. But who was "
           "this man, and why is he still so loved more than five hundred years after his death?"),
         P("Alisher was born in 1441 in Herat, a city which is now in Afghanistan. His family was close to the ruling "
           "Timurid family, and as a boy he studied together with Husayn Bayqara, a young prince who became his "
           "lifelong friend. Alisher loved poetry from an early age. According to old stories, he had already learned "
           "many long poems by heart when he was still a child."),
         P("In 1469, Husayn Bayqara became the ruler of Herat and invited his old friend to his court. Navoi served as a "
           "high official, and for a time he was one of the most powerful men in the state. However, he used his wealth "
           "to help others. He paid for the building of schools, hospitals, mosques and bridges, and he supported many "
           "young poets, artists and scholars."),
         P("In Navoi's time, most serious poetry in the region was written in Persian. Navoi wrote in Persian too, but "
           "he believed that his own Turkic language, known today as Chagatai, was just as rich and beautiful. Near the "
           "end of his life, he wrote a book called Muhokamat ul-lughatayn, which means The Judgement of Two Languages. "
           "In it, he compared the two languages and argued that Turkic poets should not be ashamed of writing in their "
           "mother tongue."),
         P("His most famous work is the Khamsa, a collection of five long poems. Earlier poets had written their own "
           "Khamsas in Persian, but Navoi was the first to write a complete one in Turkic. Its stories of love, friendship and "
           "wisdom, such as Farhod and Shirin and Layli and Majnun, are still read and performed today."),
         P("Navoi died in Herat in 1501. Today he is considered the national poet of Uzbekistan. A region and its "
           "capital city, the National Library and the opera theatre in Tashkent all carry his name. If you want to "
           "understand Uzbek culture, a few lines of Navoi are a good place to start."),
     ],
     [G('literature', 'adabiyot'), G('named after', '… nomi bilan atalgan'), G('portrait', 'portret, surat'),
      G('lifelong', 'umrbod'), G('learn by heart', 'yod olmoq'), G('court', 'saroy'),
      G('official', 'amaldor, davlat arbobi'), G('wealth', 'boylik'), G('scholar', 'olim'),
      G('argue', 'isbotlashga harakat qilmoq, daʼvo qilmoq'), G('be ashamed of', '… dan uyalmoq'),
      G('mother tongue', 'ona tili'), G('collection', 'toʻplam'), G('wisdom', 'donolik, hikmat'),
      G('perform', 'sahnalashtirmoq, ijro etmoq')],
     [GN('i11-past-perfect', 'Past Perfect: he had already learned',
         'he had already learned many long poems by heart'),
      GN('i29-passive-basics', 'Majhul nisbat: was written, is considered',
         'most serious poetry in the region was written in Persian')],
     [
         tf('Navoi was born in the city of Herat.', 'T', '«Alisher was born in 1441 in Herat».', 1, ng=True),
         tf('Navoi and Husayn Bayqara met for the first time at the court in 1469.', 'F',
            'Ular bolalikdan tanish: «as a boy he studied together with Husayn Bayqara».', 1, ng=True),
         tf("Navoi's father was also a famous poet.", 'NG',
            'Matnda faqat oilasi temuriylarga yaqin boʻlgani aytilgan; otasi shoir boʻlganmi — maʼlumot yoʻq.', 1),
         tf('Navoi was the first poet in history to write a Khamsa.', 'F',
            '«Earlier poets had written their own Khamsas in Persian» — u turkiy tilda toʻliq «Xamsa» yozgan birinchi shoir, umuman birinchi emas.', 4, ng=True),
         hd(2, ['A powerful man who helped others', 'A childhood in Herat', 'A new language for poetry'], 0,
            '3-xatboshi: Navoiy yuqori lavozimda boʻlgan va boyligini maktab, shifoxona, koʻpriklar qurishga sarflagan.'),
         ch('Why did Navoi write Muhokamat ul-lughatayn?',
            ['to teach Persian to Turkic children',
             'to show that Turkic was as good a language for poetry as Persian',
             'to tell the story of his friendship with Husayn Bayqara'], 1,
            'U ikki tilni solishtirib, turkiy shoirlar ona tilida yozishdan uyalmasligi kerak, deb taʼkidlagan: '
            '«should not be ashamed of writing in their mother tongue».', 3),
         ch('Which sentence best describes Navoi as a statesman?',
            ['He kept his money and lived a quiet life.',
             'He used his position and money to support people and build useful places.',
             'He left the court because he did not like politics.'], 1,
            '«he used his wealth to help others. He paid for the building of schools, hospitals…».', 2),
         gap('Navoi believed his Turkic language was rich and beautiful; today this language is known as ___.', ['Chagatai'],
             '«his own Turkic language, known today as Chagatai».', 3, 2),
         gap('The Khamsa is a collection of five long ___.', ['poems'],
             '«the Khamsa, a collection of five long poems».', 4, 2),
     ])

# 3 ─────────────────────────────────────────────────────────────── dialogue
text(B, 'b1-13-ibn-sino', 'Ibn Sino', 'Ibn Sino: A Visit to Afshona', 'B1', 'dialogue', TAG,
     'Bu dialogda gid Afshona qishlogʻida sayyohlarga, jumladan maktab oʻquvchisi Jasurga, Ibn Sino haqida hikoya qiladi. '
     'Oʻqishdan oldin oʻylab koʻring: Ibn Sino qaysi sohalarda mashhur boʻlgan?',
     [
         P("Guide: Welcome to Afshona, everyone. Ibn Sino, who is known in Europe as Avicenna, was born in this village "
           "near Bukhara around the year 980. At that time, Bukhara was the capital of the Samanid state and a great centre of "
           "learning. Jasur: Did he go to school in Bukhara, then?"),
         P("Guide: Yes, his family moved to Bukhara when he was a child. He was an amazingly fast learner. By the age of "
           "about ten, he had learned the whole Quran by heart, and then he studied logic, mathematics and philosophy. "
           "When he became interested in medicine, he found it quite easy. Jasur: Easy? Medicine is the hardest "
           "subject I can imagine!"),
         P("Guide: Many people would agree with you. But Ibn Sino was already treating patients when he was still a "
           "teenager. Once, the ruler of Bukhara became seriously ill, and the young doctor was invited to help him. "
           "The ruler recovered, and as a reward Ibn Sino was allowed to use the royal library. Jasur: That sounds like "
           "a better prize than gold!"),
         P("Guide: He thought so too, and he spent many hours reading there. Later, political problems forced him to "
           "leave Bukhara, and he spent the rest of his life moving from city to city, first in Khorezm and later in Persia. He worked as a "
           "doctor and adviser to different rulers, and he never stopped writing, even while he was travelling. "
           "Jasur: How many books did he write?"),
         P("Guide: Historians are not sure of the exact number, but there were a lot, on subjects from astronomy to "
           "music. His most famous work is The Canon of Medicine. It brought together the knowledge of earlier doctors "
           "and his own experience. It was translated into Latin and used in European universities for centuries. "
           "Jasur: If I wrote a book like that, I would be very proud!"),
         P("Guide: I'm sure he was proud of it. Today, his name can be seen on hospitals, schools and streets all over "
           "Uzbekistan. Now, let's go inside and look at the exhibition. Jasur: Great! Who knows, maybe I'll become a "
           "doctor too."),
     ],
     [G('be known as', '… nomi bilan tanilgan'), G('centre of learning', 'ilm markazi'), G('fast learner', 'tez oʻrganadigan odam'),
      G('learn by heart', 'yod olmoq'), G('treat patients', 'bemorlarni davolamoq'), G('seriously ill', 'ogʻir kasal'),
      G('recover', 'tuzalmoq, sogʻaymoq'), G('reward', 'mukofot'), G('royal', 'shohona, podshohga tegishli'),
      G('force', 'majbur qilmoq'), G('adviser', 'maslahatchi'), G('exact', 'aniq'),
      G('translate', 'tarjima qilmoq'), G('exhibition', 'koʻrgazma')],
     [GN('i26-second-conditional', 'Ikkinchi tur shart gap: If I wrote …, I would …',
         'If I wrote a book like that, I would be very proud!'),
      GN('i30-passive-tenses', 'Majhul nisbat: was invited, was allowed, was translated',
         'It was translated into Latin and used in European universities for centuries.')],
     [
         tf('Ibn Sino was born in the city of Bukhara.', 'F',
            'U Buxoro yaqinidagi qishloqda tugʻilgan: «was born in this village near Bukhara», oilasi keyin Buxoroga koʻchgan.', 0, ng=True),
         tf('Jasur thinks that medicine is an easy subject.', 'F',
            'Jasur aksincha deydi: «Medicine is the hardest subject I can imagine!»', 1, ng=True),
         tf("Ibn Sino's father worked as a doctor.", 'NG',
            'Matnda faqat oilasi Buxoroga koʻchgani aytilgan; otasining kasbi haqida maʼlumot yoʻq.', 1),
         tf('The Canon of Medicine was studied in European universities.', 'T',
            '«It was translated into Latin and used in European universities for centuries.»', 4, ng=True),
         ch('Why was Ibn Sino allowed to use the royal library?',
            ['He had bought many books for it.', 'He had helped the ill ruler to recover.',
             'He was the son of the librarian.'], 1,
            '«The ruler recovered, and as a reward Ibn Sino was allowed to use the royal library.»', 2),
         ch('Why did Ibn Sino leave Bukhara?',
            ['because of political problems', 'because he wanted to study in Europe', 'because the library was closed'], 0,
            '«political problems forced him to leave Bukhara».', 3),
         ch('What does the guide say about the number of books Ibn Sino wrote?',
            ['He wrote only one important book.', 'Nobody knows exactly how many he wrote.',
             'He wrote exactly one hundred books.'], 1,
            '«Historians are not sure of the exact number, but there were a lot».', 4),
         gap('In Europe, Ibn Sino is known as ___.', ['Avicenna'],
             '«Ibn Sino, who is known in Europe as Avicenna».', 0, 2),
         gap('The Canon of Medicine was translated into ___.', ['Latin'],
             '«It was translated into Latin».', 4, 2),
     ])

# 4 ─────────────────────────────────────────────────────────────── blog
text(B, 'b1-14-khiva', 'Xiva — ochiq osmon ostidagi muzey', 'Khiva: A Museum Under the Open Sky', 'B1', 'blog', TAG,
     'Bu — Xivaga borgan sayyohning blogidagi yozuv. Oʻqishdan oldin oʻylab koʻring: '
     'nega Xivani «ochiq osmon ostidagi muzey» deb atashadi?',
     [
         P("Day 3 of my trip around Uzbekistan, and I think I have found my favourite place. After a long drive across "
           "the desert from Bukhara, we arrived in Khiva late in the afternoon. The sun was going down, and the old city "
           "walls were glowing orange. I had seen photos before, of course, but nothing had prepared me for how "
           "beautiful it looked in real life."),
         P("The old part of Khiva is called Itchan Kala, which means the inner town. It is surrounded by thick mud-brick "
           "walls, and you enter it through one of four gates. Inside, there are almost no modern buildings, just narrow "
           "streets, madrasas, mosques, minarets and palaces. In 1990, Itchan Kala became the first place in Uzbekistan "
           "to be added to the UNESCO World Heritage List. Walking around, I could easily see why people call Khiva a "
           "museum under the open sky."),
         P("The first thing I noticed was a short, wide tower covered in blue and green tiles. This is Kalta Minor, "
           "which means the short minaret. Our guide told us that the khan had planned it to be much taller, but he had "
           "died before it was finished, and the work was never completed. Even unfinished, it has become a symbol of "
           "the city."),
         P("The next morning, I visited the Juma Mosque. From the outside it looks quite simple, but inside there is a "
           "huge hall with more than two hundred carved wooden columns. Light comes in through openings in the roof, "
           "and the hall feels calm and cool, even on a hot day. I sat there for twenty minutes without saying a word."),
         P("In the evening, I climbed the Islam Khoja Minaret, the tallest in Khiva. The stairs were dark and steep, so "
           "I had to hold the wall all the way up. But the view from the top was worth it: the whole old town lay below "
           "me, with its domes and towers, and the flat land stretched to the horizon."),
         P("My advice? If you go to Khiva, stay at least two nights. Explore early in the morning or late in the "
           "afternoon, when it is cooler and there are fewer tourists. And wear comfortable shoes, because you will "
           "walk a lot!"),
     ],
     [G('glow', 'nur taratmoq, tovlanmoq'), G('prepare somebody for', 'kimnidir … ga tayyorlamoq'),
      G('surrounded by', '… bilan oʻralgan'), G('mud-brick', 'xom gʻisht, paxsa'), G('gate', 'darvoza'),
      G('World Heritage List', 'Jahon merosi roʻyxati'), G('tile', 'koshin, sopol plitka'), G('unfinished', 'tugallanmagan'),
      G('symbol', 'ramz'), G('carved', 'oʻymakor, oʻyib ishlangan'), G('column', 'ustun'),
      G('steep', 'tik'), G('be worth it', 'arzimoq, bunga arziydi'), G('horizon', 'ufq')],
     [GN('i33-reported-speech', 'Koʻchirma gap: told us that … had planned',
         'Our guide told us that the khan had planned it to be much taller'),
      GN('i25-if-i-do-if-i-did', 'Shart gap: If you go …, stay …',
         'If you go to Khiva, stay at least two nights.')],
     [
         tf('The writer travelled to Khiva from Bukhara.', 'T',
            '«After a long drive across the desert from Bukhara, we arrived in Khiva».', 0, ng=True),
         tf('There are five gates in the walls of Itchan Kala.', 'F',
            '«you enter it through one of four gates» — toʻrtta darvoza.', 1, ng=True),
         tf('The writer had to pay to climb the Islam Khoja Minaret.', 'NG',
            'Muallif minoraga chiqqanini aytadi, lekin buning uchun pul toʻlagan-toʻlamagani yozilmagan.', 4),
         tf('Work on Kalta Minor continued after the khan died.', 'F',
            '«he had died before it was finished, and the work was never completed».', 2, ng=True),
         ch('Why is Kalta Minor so short?',
            ['The khan wanted a small minaret.', 'It was never finished because the khan died.',
             'The top fell down in an earthquake.'], 1,
            '«the khan had planned it to be much taller, but he had died before it was finished».', 2),
         ch('How did the writer feel inside the Juma Mosque?',
            ['bored and tired', 'calm and quiet', 'nervous because it was dark'], 1,
            '«the hall feels calm and cool» va «I sat there for twenty minutes without saying a word».', 3),
         ch('Why does the writer suggest exploring early or late in the day?',
            ['because the museums are free then', 'because it is cooler and less crowded',
             'because the light is better for photos'], 1,
            '«when it is cooler and there are fewer tourists».', 5),
         gap('The name Itchan Kala means the ___.', ['inner town'],
             '«Itchan Kala, which means the inner town».', 1, 2),
         gap('The stairs of the Islam Khoja Minaret were dark and ___.', ['steep'],
             '«The stairs were dark and steep».', 4, 2),
     ])

# 5 ─────────────────────────────────────────────────────────────── story
text(B, 'b1-15-suzani', 'Soʻzana', "My Grandmother's Suzani", 'B1', 'story', TAG,
     'Bu hikoyada bir qiz buvisining soʻzanasi va bu hunarning sirlari haqida soʻzlaydi. '
     'Oʻqishdan oldin oʻylab koʻring: sizning uyingizda soʻzana bormi va unda qanday naqshlar bor?',
     [
         P("When I was twelve, my grandmother opened an old wooden chest in her room and took out something I had never "
           "seen before. It was a huge piece of cotton cloth, almost as big as my bed, covered in red and pink flowers. "
           "'This is a suzani,' she said. 'I made it for my wedding more than fifty years ago.'"),
         P("Grandmother explained that the word suzani comes from a Persian word for needle. In the past, a girl's "
           "mother and grandmother started embroidering suzanis when she was still a little child. They were part of "
           "her dowry, the things a bride brought with her to her new home. Because a family often prepared several of "
           "them, the work could take years. Sometimes the cloth was cut into long strips, and different women "
           "embroidered different strips at the same time. Later, the pieces were sewn together."),
         P("I looked more closely at Grandmother's suzani. In the centre there was a large round shape like a sun, and "
           "around it were flowers, leaves and small red fruits. 'Those are pomegranates,' she said. 'They have many "
           "seeds, so people believed they would bring a big, happy family.' Every pattern had a meaning, and many of "
           "them were wishes for the young bride."),
         P("She also told me that suzanis from different places look different. Those from Nurata often have delicate "
           "flowers spread across a light background, while the ones from Samarkand usually have large, bold shapes in "
           "deep red. People who know a lot about suzanis can often guess where one was made just by looking at its "
           "patterns."),
         P("Grandmother's generation used to hang suzanis on the walls and spread them on beds, especially on special "
           "days like weddings. Today, many suzanis are made in workshops and sold to tourists, and some old ones are "
           "kept in museums around the world. But in many families, the tradition is still alive at home."),
         P("Last year, Grandmother gave me a needle and some coloured thread and showed me my first stitches. My flowers "
           "are still a little crooked, and I have finished only one small corner. 'Don't worry,' she said, smiling. "
           "'If you keep practising, your suzani will be ready long before your wedding.'"),
     ],
     [G('chest', 'sandiq'), G('cloth', 'mato'), G('needle', 'igna'), G('embroider', 'kashta tikmoq'),
      G('dowry', 'sep'), G('bride', 'kelin'), G('strip', 'uzun boʻlak, tasma'), G('sew together', 'bir-biriga tikib ulamoq'),
      G('pomegranate', 'anor'), G('pattern', 'naqsh'), G('delicate', 'nozik'), G('bold', 'yirik va koʻzga tashlanadigan, yorqin'),
      G('thread', 'ip'), G('stitch', 'chok, tikish qadami'), G('crooked', 'qiyshiq')],
     [GN('i12-used-to-would', 'used to: oʻtmishdagi odat',
         "Grandmother's generation used to hang suzanis on the walls"),
      GN('i29-passive-basics', 'Majhul nisbat: were sewn, are made',
         'Later, the pieces were sewn together.')],
     [
         tf("The grandmother made her suzani for her own wedding.", 'T',
            '«I made it for my wedding more than fifty years ago.»', 0, ng=True),
         tf('In the past, each suzani was always made by only one woman.', 'F',
            '«different women embroidered different strips at the same time» — bir nechta ayol ishlagan.', 1, ng=True),
         tf('The grandmother learned to embroider from her own mother.', 'NG',
            'Buvi kimdan oʻrgangani matnda aytilmagan.', 1),
         tf('The writer has already finished her own suzani.', 'F',
            '«I have finished only one small corner» — hali tugamagan.', 5, ng=True),
         ch('According to the grandmother, why were pomegranates embroidered on suzanis?',
            ['because they were the bride\'s favourite fruit', 'because they were a wish for a big, happy family',
             'because red thread was cheap'], 1,
            '«They have many seeds, so people believed they would bring a big, happy family.»', 2),
         ch('What is paragraph 4 mainly about?',
            ['how to choose a good suzani in a shop', 'how suzanis from different regions differ',
             'why young people do not like suzanis'], 1,
            '«suzanis from different places look different» — Nurota va Samarqand uslublari solishtiriladi.', 3),
         ch('In the last paragraph, "crooked" flowers are flowers that …',
            ['are not straight or neat', 'are too big', 'have the wrong colour'], 0,
            'Qiz endi oʻrganmoqda, gullari «still a little crooked» — hali tekis chiqmaydi, buvisi esa uni ruhlantiradi.', 5),
         gap('The word suzani comes from a Persian word for ___.', ['needle'],
             '«the word suzani comes from a Persian word for needle».', 1, 2),
         gap('Suzanis from Samarkand usually have large, bold shapes in deep ___.', ['red'],
             '«the ones from Samarkand usually have large, bold shapes in deep red».', 3, 2),
     ])
