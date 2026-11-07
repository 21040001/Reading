"""A2 · 2-boʻlim: Oʻtmishdan hikoyalar (5 ta matn)"""
from lib import *

B = 'a2'
PAST = L('Oʻtmishdan hikoyalar', 'Stories from the past')

text(B, 'a2-06-unforgettable', 'Unutilmas kun', 'An Unforgettable Day', 'A2', 'blog', L('Oila', 'Family'),
     'Bu — Kamolaning blogi: u bobosining tugʻilgan kunida boʻlgan voqeani hikoya qiladi. Oʻqishdan oldin oʻylab koʻring: '
     'sizning hayotingizda unutilmas kun boʻlganmi?',
     [
         P("Hello, readers! My name is Kamola, and today I want to tell you about an unforgettable day. It was last April, "
           "and it was my grandfather's eightieth birthday. All our relatives came to his house in Namangan.",
           "Salom, oʻquvchilar! Mening ismim Kamola, bugun sizlarga bir unutilmas kun haqida aytib bermoqchiman. Bu oʻtgan aprel "
           "oyida, bobomning sakson yoshga toʻlgan kunida boʻlgan edi. Barcha qarindoshlarimiz uning Namangandagi uyiga yigʻildi."),
         P("We started early in the morning. My mother and my aunts cooked plov in a huge kazan, and my cousins and I put tables "
           "and chairs in the garden. By the afternoon, there were more than sixty guests. Everyone was happy and noisy.",
           "Biz erta tongdan ishga kirishdik. Onam va xolalarim katta qozonda palov damlashdi, men esa amakivachchalarim bilan "
           "bogʻga stol va stullar qoʻydik. Tushdan keyin mehmonlar soni oltmishdan oshdi. Hamma xursand edi, atrof shovqinli edi."),
         P("But one person was not there: my uncle Rustam. He was in South Korea for work, and the last time we saw him was "
           "five years ago. When the guests sang songs for Grandfather, he smiled, but his eyes were sad.",
           "Lekin bir kishi yoʻq edi — Rustam amakim. U Janubiy Koreyada ishlardi, biz uni oxirgi marta besh yil oldin koʻrgan edik. "
           "Mehmonlar bobomga qoʻshiq aytganda, u jilmaydi, lekin koʻzlarida gʻam bor edi."),
         P("Then, while Grandfather was cutting the cake, the gate opened slowly. A tall man came in with a big bag. "
           "It was Uncle Rustam! Grandfather dropped the knife and ran to his son. For a moment nobody spoke. "
           "Then everybody started to cry and laugh at the same time.",
           "Keyin, bobom tortni kesayotganda, darvoza sekin ochildi. Katta sumka koʻtargan baland boʻyli bir kishi kirib keldi. "
           "Bu Rustam amakim edi! Bobom pichoqni tushirib yubordi va oʻgʻliga qarab yugurdi. Bir lahza hech kim gapirmadi. "
           "Soʻng hamma bir vaqtning oʻzida ham yigʻlab, ham kula boshladi."),
         P("Later, Uncle Rustam explained everything. He wanted to surprise his father, so he didn't tell anyone about his trip. "
           "I will never forget Grandfather's face that evening. Do you have an unforgettable day? Write about it in the comments!",
           "Keyinroq Rustam amakim hammasini tushuntirdi. U otasini hayron qoldirmoqchi edi, shuning uchun safari haqida hech kimga "
           "aytmagan ekan. Bobomning oʻsha oqshomdagi yuzini hech qachon unutmayman. Sizning ham unutilmas kuningiz bormi? "
           "Bu haqda izohlarda yozing!"),
     ],
     [G('unforgettable', 'unutilmas'), G('relatives', 'qarindoshlar'), G('huge', 'juda katta, ulkan'),
      G('cousin', 'amakivachcha, xolavachcha'), G('guest', 'mehmon'), G('noisy', 'shovqinli'),
      G('gate', 'darvoza'), G('drop', 'tushirib yubormoq'), G('at the same time', 'bir vaqtning oʻzida'),
      G('explain', 'tushuntirmoq'), G('surprise', 'hayron qoldirmoq; kutilmagan sovgʻa')],
     [GN('e09-past-continuous', 'Past Continuous: while … was cutting', 'while Grandfather was cutting the cake, the gate opened slowly.'),
      GN('e53-and-but-so-because', 'so — shuning uchun', "He wanted to surprise his father, so he didn't tell anyone about his trip.")],
     [
         tf("The birthday party was at the grandfather's house in Namangan.", 'T',
            '«All our relatives came to his house in Namangan.»', 0),
         ch('How old was the grandfather?', ['seventy', 'eighty', 'sixty'], 1,
            '«my grandfather\'s eightieth birthday» — eightieth = saksoninchi. Oltmish — mehmonlar soni.', 0),
         tf('Kamola and her cousins cooked the plov.', 'F',
            'Palovni onasi va xolalari pishirdi: «My mother and my aunts cooked plov». Kamola stol va stullarni qoʻydi.', 1),
         gap('By the afternoon, there were more than ___ guests.', ['sixty', '60'], '«there were more than sixty guests».', 1),
         ch('Where was Uncle Rustam before the party?', ['in Russia', 'in South Korea', 'in Tashkent'], 1,
            '«He was in South Korea for work».', 2),
         ch('What was Grandfather doing when the gate opened?', ['singing songs', 'cutting the cake', 'eating plov'], 1,
            '«while Grandfather was cutting the cake, the gate opened slowly».', 3),
         tf('Grandfather walked slowly to his son.', 'F', 'U yugurdi: «Grandfather dropped the knife and ran to his son.» '
            'Sekin ochilgan narsa — darvoza.', 3),
         ch("Why didn't Uncle Rustam tell anyone about his trip?",
            ['He wanted to surprise his father.', 'He forgot to call.', 'His phone was broken.'], 0,
            '«He wanted to surprise his father, so he didn\'t tell anyone about his trip.»', 4),
     ])

text(B, 'a2-07-rain-trip', 'Yomgʻirdagi sayohat', 'A Trip in the Rain', 'A2', 'dialogue', PAST,
     'Nilufar va Sherzod dam olish kunlari haqida gaplashadi. Oʻqishdan oldin: yomgʻir sizning rejalaringizni hech buzganmi?',
     [
         P("Nilufar: Hi, Sherzod! How was your weekend? Did you go to Charvak Lake? "
           "Sherzod: Yes, we did, but it wasn't a perfect trip. It rained almost all day!",
           "Nilufar: Salom, Sherzod! Dam olish kunlaring qanday oʻtdi? Chorvoqqa bordingmi? "
           "Sherzod: Ha, bordik, lekin sayohat unchalik yaxshi boʻlmadi. Deyarli kun boʻyi yomgʻir yogʻdi!"),
         P("Nilufar: Oh no! What happened? Sherzod: We left Tashkent early in the morning. The sky was blue, so we didn't take "
           "umbrellas or warm clothes. But when we arrived at the lake, it started to rain heavily.",
           "Nilufar: Voy! Nima boʻldi? Sherzod: Toshkentdan erta tongda chiqdik. Osmon moviy edi, shuning uchun soyabon ham, "
           "issiq kiyim ham olmadik. Lekin koʻl boʻyiga yetib kelganimizda, kuchli yomgʻir yogʻa boshladi."),
         P("Nilufar: Did you go back home? Sherzod: No, we didn't. My father found a small teahouse near the water. "
           "We sat there for three hours. We drank hot tea and ate samsa while the rain was falling outside.",
           "Nilufar: Uyga qaytdinglarmi? Sherzod: Yoʻq, qaytmadik. Otam suv yaqinida kichkina choyxona topdi. "
           "Biz u yerda uch soat oʻtirdik. Tashqarida yomgʻir yogʻayotganda issiq choy ichib, somsa yedik."),
         P("Nilufar: That sounds boring. Sherzod: Actually, it wasn't! An old man at the next table told us funny stories "
           "about the mountains. My little sister laughed so much that she forgot about the rain.",
           "Nilufar: Zerikarli boʻlgan boʻlsa kerak. Sherzod: Aslida, unday emas! Qoʻshni stoldagi bir chol bizga togʻlar haqida "
           "kulgili hikoyalar aytib berdi. Singlim shunchalik koʻp kuldiki, yomgʻirni ham unutib qoʻydi."),
         P("Nilufar: And did you swim in the end? Sherzod: No, the water was too cold. But in the evening the rain stopped, "
           "and we saw a beautiful rainbow over the lake. I took lots of photos. I'll show you!",
           "Nilufar: Oxiri choʻmildinglarmi? Sherzod: Yoʻq, suv juda sovuq edi. Lekin kechqurun yomgʻir toʻxtadi va "
           "koʻl ustida chiroyli kamalakni koʻrdik. Koʻp rasmga oldim. Senga koʻrsataman!"),
     ],
     [G('perfect', 'mukammal, aʼlo'), G('rain', 'yomgʻir; yomgʻir yogʻmoq'), G('umbrella', 'soyabon'),
      G('arrive', 'yetib kelmoq'), G('heavily', 'kuchli, qattiq'), G('teahouse', 'choyxona'),
      G('boring', 'zerikarli'), G('funny', 'kulgili'), G('laugh', 'kulmoq'), G('rainbow', 'kamalak'),
      G('take photos', 'rasmga olmoq')],
     [GN('e08-past-negative-question', 'Oʻtgan zamon: soʻroq va inkor', 'Did you go back home?'),
      GN('e10-continuous-or-simple-past', 'Past Simple va Past Continuous birga', 'We drank hot tea and ate samsa while the rain was falling outside.')],
     [
         tf("It rained for most of the day on Sherzod's trip.", 'T', 'Sherzod: «It rained almost all day!»', 0),
         ch("Why didn't the family take umbrellas?", ['The sky was blue.', 'They forgot them in the car.', "They didn't have any."], 0,
            '«The sky was blue, so we didn\'t take umbrellas or warm clothes.»', 1),
         ch('What happened when they arrived at the lake?', ['The rain stopped.', 'It started to rain heavily.', 'They saw a rainbow.'], 1,
            '«when we arrived at the lake, it started to rain heavily». Yomgʻir faqat kechqurun toʻxtadi.', 1),
         tf('The family went back home because of the rain.', 'F', '«Did you go back home?» — «No, we didn\'t.»', 2),
         gap('The family sat in the teahouse for ___ hours.', ['three', '3'], '«We sat there for three hours.»', 2),
         ch('Who told funny stories?', ["Sherzod's father", 'an old man', "Sherzod's sister"], 1,
            '«An old man at the next table told us funny stories». Singlisi esa kuldi.', 3),
         tf('Sherzod swam in the lake in the evening.', 'F', 'Ular choʻmilmadi: «No, the water was too cold.»', 4),
         gap('In the evening, they saw a beautiful ___ over the lake.', 'rainbow',
             '«we saw a beautiful rainbow over the lake».', 4),
     ])

text(B, 'a2-08-lost-key', 'Yoʻqolgan kalit', 'The Lost Key', 'A2', 'story', PAST,
     'Bu — kalitini yoʻqotib qoʻygan Bobur haqidagi hikoya. Oʻqishdan oldin: siz biror narsani yoʻqotib, keyin kutilmagan joydan topganmisiz?',
     [
         P("Last Tuesday, Bobur came home from school at two o'clock. He was hungry and tired. His parents were at work, "
           "so the flat was empty. He put his hand in his pocket, but the key wasn't there!",
           "Oʻtgan seshanba kuni Bobur maktabdan soat ikkida uyga keldi. U och va charchagan edi. Ota-onasi ishda edi, "
           "shuning uchun kvartirada hech kim yoʻq edi. U qoʻlini choʻntagiga soldi, lekin kalit yoʻq edi!"),
         P("Bobur looked in his bag carefully. He took out all his books and notebooks, but he couldn't find the key. "
           "Then he walked back to school slowly and looked at the ground all the way. He didn't find anything.",
           "Bobur sumkasini diqqat bilan koʻzdan kechirdi. Barcha kitob va daftarlarini chiqardi, lekin kalitni topa olmadi. "
           "Keyin u maktabga sekin qaytib bordi va butun yoʻl boʻyi yerga qarab ketdi. Hech narsa topmadi."),
         P("When he came back, his neighbour, Aunt Hamida, was sitting on a bench near the building. 'You look worried, Bobur,' "
           "she said. He told her about the key. 'Come and have some tea. Your mother comes home at six,' she said.",
           "U qaytib kelganda, qoʻshnisi Hamida xola bino yonidagi skameykada oʻtirgan edi. «Xavotirda koʻrinasan, Bobur», — dedi u. "
           "Bobur unga kalit haqida aytib berdi. «Yur, choy ichamiz. Onang soat oltida keladi», — dedi xola."),
         P("Bobur drank tea and ate some bread with jam. While he was eating, Aunt Hamida's grandson, Doniyor, ran into the kitchen. "
           "'Grandma, look! I found a key on the stairs this morning!' he shouted. It was Bobur's key with a small red football on it.",
           "Bobur choy ichib, murabbo bilan non yedi. U ovqatlanayotganda Hamida xolaning nevarasi Doniyor oshxonaga yugurib kirdi. "
           "«Buvi, qarang! Bugun ertalab zinadan kalit topib oldim!» — deb qichqirdi u. Bu Boburning kaliti edi, unda kichkina qizil "
           "futbol toʻpi osilgan edi."),
         P("Bobur laughed. Now he remembered: in the morning he was in a hurry, so he locked the door quickly and dropped the key. "
           "He thanked Doniyor and gave him a chocolate. Now Bobur always keeps his key on a string around his neck.",
           "Bobur kulib yubordi. Endi esladi: ertalab u shoshayotgan edi, shuning uchun eshikni tez qulflab, kalitni tushirib qoldirgan. "
           "U Doniyorga rahmat aytdi va unga shokolad berdi. Endi Bobur kalitini doim boʻyniga ipga taqib yuradi."),
     ],
     [G('hungry', 'och (qorni och)'), G('empty', 'boʻsh'), G('pocket', 'choʻntak'), G('carefully', 'diqqat bilan, ehtiyotlab'),
      G('ground', 'yer (oyoq ostidagi)'), G('neighbour', 'qoʻshni'), G('bench', 'skameyka, oʻrindiq'), G('worried', 'xavotirli'),
      G('stairs', 'zina'), G('be in a hurry', 'shoshilmoq'), G('lock', 'qulflamoq'), G('string', 'ip')],
     [GN('e09-past-continuous', 'Past Continuous: while he was eating', "While he was eating, Aunt Hamida's grandson, Doniyor, ran into the kitchen."),
      GN('e44-adjectives-adverbs', 'Ravish: careful → carefully', 'Bobur looked in his bag carefully.')],
     [
         tf("Bobur's parents were at home when he came back from school.", 'F',
            'Ular ishda edi: «His parents were at work, so the flat was empty.»', 0),
         ch('What did Bobur do first?', ['He looked in his bag.', 'He went to Aunt Hamida.', 'He walked back to school.'], 0,
            'Avval sumkasini koʻrdi: «Bobur looked in his bag carefully.» Keyin («Then») maktabga qaytdi.', 1),
         tf('Bobur found the key on the way to school.', 'F', '«He didn\'t find anything.»', 1),
         gap('Aunt Hamida was sitting on a ___ near the building.', 'bench', '«Aunt Hamida, was sitting on a bench near the building».', 2),
         ch("When does Bobur's mother come home?", ['at two', 'at six', 'at seven'], 1,
            '«Your mother comes home at six». Soat ikkida Bobur maktabdan kelgan.', 2),
         ch('Who found the key?', ['Aunt Hamida', "Bobur's mother", 'Doniyor'], 2,
            'Doniyor: «I found a key on the stairs this morning!»', 3),
         gap('There was a small red ___ on the key.', 'football', '«Bobur\'s key with a small red football on it».', 3),
         ch('Why did Bobur drop the key?', ['He was in a hurry.', 'He was playing football.', 'His bag was open.'], 0,
            '«in the morning he was in a hurry, so he locked the door quickly and dropped the key».', 4),
     ])

text(B, 'a2-09-first-job', 'Birinchi ish kunim', 'My First Day at Work', 'A2', 'email', L('Ish', 'Work'),
     'Bu — Sevinchning dugonasi Madinaga yozgan xati. U Xivadagi mehmonxonadagi birinchi ish kuni haqida yozadi. '
     'Oʻqishdan oldin: birinchi ish kuni odam qanday his qiladi deb oʻylaysiz?',
     [
         P("Hi Madina, How are you? I have big news. Yesterday was my first day at work! I got a summer job at a small family "
           "hotel in Khiva. I work at the reception desk because I can speak English.",
           "Salom, Madina! Qalaysan? Katta yangiligim bor. Kecha mening birinchi ish kunim edi! Xivadagi kichik oilaviy mehmonxonada "
           "yozgi ish topdim. Ingliz tilida gapira olganim uchun qabulxonada ishlayman."),
         P("I woke up at six because I was very nervous. I arrived at the hotel at half past seven. The owner, Mr Yusupov, "
           "showed me the rooms and explained my job to me. I answer the phone, give keys to guests and help tourists with information.",
           "Juda hayajonlanganim uchun soat oltida uygʻondim. Mehmonxonaga yetti yarimda yetib keldim. Mehmonxona egasi Yusupov "
           "menga xonalarni koʻrsatdi va ishimni tushuntirdi. Men telefonga javob beraman, mehmonlarga kalit beraman va "
           "sayyohlarga maʼlumot berib yordam beraman."),
         P("At first, everything went badly. At nine o'clock, a French couple arrived. I gave them the wrong key, and they "
           "walked into a room with another guest in it! I felt terrible. I said sorry many times, and luckily they only laughed.",
           "Avvaliga hammasi yomon ketdi. Soat toʻqqizda fransuz er-xotin keldi. Men ularga notoʻgʻri kalit berdim va ular "
           "ichida boshqa mehmon bor xonaga kirib qolishdi! Oʻzimni juda yomon his qildim. Koʻp marta kechirim soʻradim, "
           "baxtimga ular faqat kulishdi."),
         P("After lunch, things got better. A family from Australia asked me about the old city. I told them about Itchan Kala "
           "and its minarets, and I spoke English slowly and clearly. They thanked me and gave me a small koala toy as a present!",
           "Tushlikdan keyin ishlar yaxshilandi. Avstraliyalik bir oila mendan eski shahar haqida soʻradi. Men ularga Ichan qalʼa "
           "va uning minoralari haqida aytib berdim, inglizcha sekin va aniq gapirdim. Ular menga rahmat aytishdi va sovgʻa "
           "sifatida kichkina koala oʻyinchogʻini berishdi!"),
         P("I came home at five. I was really tired, but happy. Mr Yusupov said I did a good job on my first day. "
           "Write soon and tell me about your summer! Love, Sevinch",
           "Uyga soat beshda keldim. Juda charchagan edim, lekin xursand edim. Yusupov birinchi kunimda yaxshi ishlaganimni aytdi. "
           "Tezroq javob yoz va yozgi taʼtiling qanday oʻtayotganini aytib ber! Mehr bilan, Sevinch"),
     ],
     [G('summer job', 'yozgi ish'), G('reception desk', 'qabulxona (mehmonxonada)'), G('nervous', 'hayajonlangan, asabiy'),
      G('owner', 'egasi, xoʻjayin'), G('guest', 'mehmon'), G('couple', 'er-xotin, juftlik'), G('wrong', 'notoʻgʻri'),
      G('terrible', 'dahshatli, juda yomon'), G('luckily', 'baxtiga, yaxshiyamki'), G('minaret', 'minora'),
      G('clearly', 'aniq, tushunarli'), G('present', 'sovgʻa')],
     [GN('e07-past-irregular', 'Notoʻgʻri feʼllar: give → gave', 'I gave them the wrong key'),
      GN('e44-adjectives-adverbs', 'Ravishlar: slowly, clearly', 'I spoke English slowly and clearly.')],
     [
         tf("Sevinch's job is at a big hotel in Bukhara.", 'F',
            'Mehmonxona kichik va Xivada: «a small family hotel in Khiva».', 0),
         ch('Why does Sevinch work at the reception desk?',
            ['because she can speak English', 'because she lives near the hotel', 'because she knows the owner'], 0,
            '«I work at the reception desk because I can speak English.»', 0),
         gap('Sevinch woke up at ___ because she was nervous.', ['six', '6'],
             '«I woke up at six because I was very nervous.» Mehmonxonaga esa yetti yarimda keldi.', 1),
         tf('Mr Yusupov showed Sevinch the rooms.', 'T', '«The owner, Mr Yusupov, showed me the rooms».', 1),
         ch('What mistake did Sevinch make?',
            ['She gave guests the wrong key.', 'She was late for work.', 'She forgot to answer the phone.'], 0,
            '«I gave them the wrong key».', 2),
         tf('The French couple were very angry.', 'F', 'Ular jahl qilmadi: «luckily they only laughed».', 2),
         ch('When did things get better?', ['before nine o\'clock', 'after lunch', 'in the evening'], 1,
            '«After lunch, things got better.»', 3),
         gap('The Australian family gave Sevinch a small koala ___.', 'toy', '«gave me a small koala toy as a present».', 3),
     ])

text(B, 'a2-10-old-tale', 'Qushlar va quduq', 'The Birds and the Well', 'A2', 'story', L('Ertaklar', 'Tales'),
     'Bu — qadimgi qishloq, ochkoʻz savdogar va zukko qiz haqidagi ertak. Oʻqishdan oldin: odamlar uchun suv nega bunchalik qadrli?',
     [
         P("Long ago, in a small village near the mountains, there was only one well. It belonged to a rich and greedy merchant "
           "called Bahrom. Every summer, the river dried up, so the villagers had to buy water from him. He asked for one "
           "silver coin for each jug.",
           "Qadim zamonda togʻlar yaqinidagi kichik bir qishloqda faqat bitta quduq bor ekan. U Bahrom ismli boy va ochkoʻz "
           "savdogarga tegishli ekan. Har yozda daryo qurib qolar, shuning uchun qishloq ahli suvni undan sotib olishga majbur "
           "boʻlar ekan. U har bir koʻza suv uchun bitta kumush tanga soʻrar ekan."),
         P("A poor girl called Oysha lived in the village with her old grandmother. They had no money, and they were often "
           "thirsty. One summer, Oysha noticed something strange. Every morning, small birds flew to the hill behind the village, "
           "and an hour later they came back with wet feathers.",
           "Qishloqda Oysha ismli kambagʻal qiz keksa buvisi bilan yashar ekan. Ularning puli yoʻq, koʻpincha chanqab yurishar ekan. "
           "Bir yozda Oysha gʻalati bir narsani payqabdi. Har kuni ertalab kichkina qushlar qishloq ortidagi tepalikka uchib ketar, "
           "bir soatdan keyin esa patlari hoʻl boʻlib qaytar ekan."),
         P("The next day, Oysha followed the birds. She climbed between the rocks. Suddenly she heard a quiet "
           "sound. It was water! A small, clean spring was coming out of the ground under an old tree.",
           "Ertasi kuni Oysha qushlarning ortidan ergashibdi. U qoyalar orasidan yuqoriga chiqibdi. Birdan u sokin bir "
           "tovushni eshitibdi. Bu suv edi! Keksa daraxt tagidan kichkina, toza buloq otilib chiqayotgan ekan."),
         P("Oysha ran back and told everyone. The merchant laughed loudly. 'Birds can't find water for people!' he said. "
           "But the villagers went with Oysha to the hill. For ten days they worked hard and dug a long channel, and soon cold "
           "water ran into the village square.",
           "Oysha orqasiga yugurib qaytibdi va hammaga aytibdi. Savdogar baland ovozda kulibdi. «Qushlar odamlarga suv topib "
           "berolmaydi!» — debdi u. Lekin qishloq ahli Oysha bilan tepalikka boribdi. Oʻn kun davomida ular qattiq mehnat qilib, "
           "uzun ariq qazishibdi va tez orada qishloq maydoniga salqin suv oqib kelibdi."),
         P("Nobody bought water from Bahrom after that. At first he was angry, but then he felt ashamed. He opened his well "
           "to everyone for free. And the old people still say: 'Water belongs to everyone, like the sky.'",
           "Shundan keyin hech kim Bahromdan suv sotib olmabdi. Avvaliga u jahli chiqibdi, keyin esa uyalibdi. U qudugʻini hamma "
           "uchun tekin ochib qoʻyibdi. Keksalar hozir ham shunday deyishadi: «Suv osmon kabi hammaniki»."),
     ],
     [G('well', 'quduq'), G('belong to', 'tegishli boʻlmoq'), G('greedy', 'ochkoʻz'), G('merchant', 'savdogar'),
      G('dry up / dried up', 'qurib qolmoq'), G('jug', 'koʻza'), G('thirsty', 'chanqagan'), G('notice', 'payqamoq, sezib qolmoq'),
      G('feather', 'pat'), G('spring', 'buloq'), G('channel', 'ariq, kanal'), G('ashamed', 'uyalgan')],
     [GN('e53-and-but-so-because', 'so — shuning uchun', 'Every summer, the river dried up, so the villagers had to buy water from him.'),
      GN('e07-past-irregular', 'Notoʻgʻri feʼllar: fly → flew, come → came', 'small birds flew to the hill behind the village')],
     [
         tf('There were many wells in the village.', 'F', 'Faqat bitta quduq bor edi: «there was only one well».', 0),
         ch('Why did the villagers have to buy water from Bahrom?',
            ['The river dried up every summer.', 'The river water was dirty.', 'The king told them to.'], 0,
            '«Every summer, the river dried up, so the villagers had to buy water from him.»', 0),
         gap('Bahrom asked for one silver coin for each ___.', 'jug', '«He asked for one silver coin for each jug.»', 0),
         ch('What did Oysha notice about the birds?',
            ['They came back with wet feathers.', "They sang in the merchant's garden.", 'They never came back.'], 0,
            '«an hour later they came back with wet feathers».', 1),
         ch('What did Oysha do after she found the spring?',
            ['She ran back and told everyone.', 'She sold the water to Bahrom.', 'She stayed on the hill for ten days.'], 0,
            '«Oysha ran back and told everyone.» Oʻn kun — qishloq ahli ariq qazigan vaqt.', 3),
         tf('The merchant believed Oysha at first.', 'F', 'U kuldi: «Birds can\'t find water for people!»', 3),
         gap('The villagers worked for ___ days to dig the channel.', ['ten', '10'],
             '«For ten days they worked hard and dug a long channel».', 3),
         tf('In the end, Bahrom opened his well to everyone for free.', 'T',
            '«He opened his well to everyone for free.»', 4),
     ])
