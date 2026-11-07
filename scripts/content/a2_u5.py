"""A2 · 5-boʻlim: Sogʻliq va sport (5 ta matn)"""
from lib import *

B = 'a2'
HEALTH = L('Sogʻliq', 'Health')
SPORT = L('Sport', 'Sport')

text(B, 'a2-21-doctor-advice', 'Shifokor maslahati', "The Doctor's Advice", 'A2', 'dialogue', HEALTH,
     'Jasur charchoq va bosh ogʻrigʻidan shikoyat qilib shifokorga boradi. Oʻqishdan oldin oʻylab koʻring: '
     'siz kuniga necha soat uxlaysiz va qancha suv ichasiz?',
     [
         P("Jasur is sixteen years old. Last week he felt tired all the time and often had headaches, "
           "so his mother took him to the local clinic.",
           "Jasur oʻn olti yoshda. Oʻtgan hafta u doim oʻzini charchagan his qildi va tez-tez boshi ogʻridi, "
           "shuning uchun onasi uni mahalladagi poliklinikaga olib bordi."),
         P("Doctor: Hello, Jasur. What's the matter? Jasur: I feel tired every day, and my head hurts in the afternoon. "
           "I can't study well at school.",
           "Shifokor: Salom, Jasur. Nima boʻldi? Jasur: Har kuni charchayman, tushdan keyin boshim ogʻriydi. "
           "Maktabda yaxshi oʻqiy olmayapman."),
         P("Doctor: How many hours do you sleep at night? Jasur: About six hours. I usually play games on my phone until midnight.",
           "Shifokor: Kechasi necha soat uxlaysiz? Jasur: Taxminan olti soat. Odatda yarim tungacha telefonimda oʻyin oʻynayman."),
         P("Doctor: That isn't enough. Teenagers need about eight to ten hours of sleep. You should put your phone away "
           "an hour before bed. How much water do you drink? Jasur: Not much. I usually drink sweet fizzy drinks.",
           "Shifokor: Bu yetarli emas. Oʻsmirlarga taxminan sakkiz-oʻn soat uyqu kerak. Uxlashdan bir soat oldin "
           "telefoningizni olib qoʻyishingiz kerak. Qancha suv ichasiz? Jasur: Koʻp emas. Odatda shirin gazli ichimliklar ichaman."),
         P("Doctor: You should drink more water and eat more fruit and vegetables. You mustn't skip breakfast, and you "
           "should walk or do sport every day. Come back in two weeks if you still have headaches. "
           "Jasur: Thank you, doctor. I'll try.",
           "Shifokor: Koʻproq suv ichishingiz, koʻproq meva va sabzavot yeyishingiz kerak. Nonushtani tashlab ketmasligingiz kerak, "
           "har kuni piyoda yurishingiz yoki sport bilan shugʻullanishingiz lozim. Agar boshingiz hali ham ogʻrisa, "
           "ikki haftadan keyin yana keling. Jasur: Rahmat, doktor. Harakat qilaman."),
     ],
     [G('tired', 'charchagan'), G('headache', 'bosh ogʻrigʻi'), G('clinic', 'poliklinika, shifoxona'),
      G("What's the matter?", 'Nima boʻldi? Nimadan shikoyat qilyapsiz?'), G('hurt', 'ogʻrimoq'),
      G('teenager', 'oʻsmir'), G('enough', 'yetarli'), G('put away', 'olib qoʻymoq, yigʻishtirmoq'),
      G('fizzy drink', 'gazli ichimlik'), G('skip', 'tashlab ketmoq, oʻtkazib yubormoq'),
      G('vegetables', 'sabzavotlar')],
     [GN('e29-should', 'should — maslahat berish', 'You should drink more water'),
      GN('e48-enough-too', 'enough — yetarli', "That isn't enough.")],
     [
         tf('Jasur is sixteen years old.', 'T', '1-xatboshi: «Jasur is sixteen years old.»', 0),
         tf("Jasur's head hurts in the morning.", 'F', 'Boshi tushdan keyin ogʻriydi: «my head hurts in the afternoon».', 1),
         ch('How many hours does Jasur sleep at night?', ['about six', 'about eight', 'about ten'], 0,
            '«About six hours.» Sakkiz-oʻn soat — oʻsmirlarga kerak boʻlgan uyqu.', 2),
         ch('What does Jasur usually do until midnight?', ['He does his homework.', 'He plays games on his phone.', 'He watches TV.'], 1,
            '«I usually play games on my phone until midnight.»', 2),
         tf('The doctor says teenagers need about eight to ten hours of sleep.', 'T',
            '«Teenagers need about eight to ten hours of sleep.»', 3),
         gap('Jasur usually drinks sweet fizzy ___.', 'drinks', '«I usually drink sweet fizzy drinks.»', 3, max_words=1),
         ch('What does the doctor say about breakfast?', ["Jasur mustn't skip it.", 'Jasur should eat it at school.',
                                                         'It is not important.'], 0,
            '«You mustn\'t skip breakfast» — nonushtani tashlab ketmaslik kerak.', 4),
         gap('The doctor tells Jasur to come back in ___ weeks if he still has headaches.', ['two', '2'],
            '«Come back in two weeks if you still have headaches.»', 4, max_words=1),
     ])

text(B, 'a2-22-marathon', 'Marafon', 'My First Marathon', 'A2', 'blog', SPORT,
     'Nilufar birinchi marafoniga tayyorlanyapti va blogida bu haqda yozadi. Oʻqishdan oldin: '
     'siz bir martada qancha masofaga yugura olasiz?',
     [
         P("Hi everyone! My name is Nilufar, and I am a nurse in Tashkent. Two years ago I couldn't run for more than "
           "five minutes. Next month I am going to run my first marathon. A marathon is about 42 kilometres long, "
           "so it is a big challenge for me!",
           "Hammaga salom! Mening ismim Nilufar, men Toshkentda hamshira boʻlib ishlayman. Ikki yil oldin besh daqiqadan "
           "ortiq yugura olmasdim. Kelasi oy birinchi marta marafonda yugurmoqchiman. Marafon taxminan 42 kilometr, "
           "shuning uchun bu men uchun katta sinov!"),
         P("I started slowly. At first, I ran for ten minutes three times a week. Then I ran a little longer every week. "
           "Last spring I finished a ten-kilometre race in the park. I was slower than most runners, but I was very happy.",
           "Men sekin boshladim. Avvaliga haftasiga uch marta oʻn daqiqadan yugurdim. Keyin har hafta biroz uzoqroq yugurdim. "
           "Oʻtgan bahorda bogʻdagi oʻn kilometrlik poygani tugatdim. Koʻpchilik yuguruvchilardan sekinroq edim, "
           "lekin juda xursand boʻldim."),
         P("Now I run five days a week. On Sundays I do a long run of twenty or thirty kilometres. I have to get up "
           "at five o'clock, because the streets are quieter and the air is cooler in the early morning.",
           "Hozir haftasiga besh kun yuguraman. Yakshanba kunlari yigirma-oʻttiz kilometr masofaga uzoq yuguraman. "
           "Soat beshda turishimga toʻgʻri keladi, chunki erta tongda koʻchalar tinchroq, havo esa salqinroq boʻladi."),
         P("Food and rest are important too. I eat more rice, bread and vegetables, and I drink a lot of water. "
           "I sleep eight hours every night. I don't run on Mondays, because my legs need a rest.",
           "Ovqat va dam olish ham muhim. Men koʻproq guruch, non va sabzavot yeyman, koʻp suv ichaman. "
           "Har kecha sakkiz soat uxlayman. Dushanba kunlari yugurmayman, chunki oyoqlarim dam olishi kerak."),
         P("I am a little nervous, but my friends are going to wait for me at the finish line. I don't want to win. "
           "I just want to finish! Wish me luck!",
           "Biroz hayajondaman, lekin doʻstlarim meni marra chizigʻida kutib turishadi. Men gʻolib boʻlishni xohlamayman. "
           "Shunchaki marragacha yetib borishni xohlayman! Menga omad tilang!"),
     ],
     [G('nurse', 'hamshira'), G('challenge', 'sinov, qiyin vazifa'), G('slowly', 'sekin'),
      G('at first', 'avvaliga, dastlab'), G('race', 'poyga'), G('runner', 'yuguruvchi'),
      G('quiet', 'tinch, sokin'), G('rest', 'dam olish; dam olmoq'), G('nervous', 'hayajonlangan, xavotirda'),
      G('finish line', 'marra chizigʻi'), G('Wish me luck!', 'Menga omad tilang!')],
     [GN('e28-have-to', 'have to — majburiyat', "I have to get up at five o'clock"),
      GN('e45-comparatives', 'Qiyosiy daraja: quieter, cooler', 'the streets are quieter and the air is cooler')],
     [
         tf('Nilufar works as a teacher.', 'F', 'U hamshira: «I am a nurse in Tashkent.»', 0),
         gap('A marathon is about ___ kilometres long.', ['42', 'forty-two'],
             '«A marathon is about 42 kilometres long» — aniqrogʻi 42,195 km.', 0, max_words=1),
         tf('Two years ago Nilufar could run for a long time.', 'F',
            '«Two years ago I couldn\'t run for more than five minutes.»', 0),
         ch('What did Nilufar do last spring?', ['She finished a ten-kilometre race.', 'She ran a marathon.',
                                                 'She won a race in the park.'], 0,
            '«Last spring I finished a ten-kilometre race in the park.» Marafon hali oldinda — kelasi oy.', 1),
         tf('In the ten-kilometre race, Nilufar was faster than most runners.', 'F',
            '«I was slower than most runners» — u sekinroq edi.', 1),
         ch('Why does Nilufar run in the early morning?', ['Her work starts at seven.',
                                                          'The streets are quieter and the air is cooler.',
                                                          'Her friends run with her then.'], 1,
            '«because the streets are quieter and the air is cooler in the early morning».', 2),
         gap("Nilufar doesn't run on ___.", 'Mondays', '«I don\'t run on Mondays, because my legs need a rest.»', 3, max_words=1),
         ch("What is Nilufar's goal in the marathon?", ['to win', 'to finish', 'to meet new friends'], 1,
            '«I don\'t want to win. I just want to finish!»', 4),
     ])

text(B, 'a2-23-breakfast', 'Sogʻlom nonushta', 'A Healthy Breakfast', 'A2', 'email', HEALTH,
     'Dilfuza nonushta qilmaydigan dugonasi Lolaga maslahat yozadi. Oʻqishdan oldin: siz bugun nonushtaga nima yedingiz?',
     [
         P("Hi Lola, Thanks for your email. You said you often feel hungry and tired before lunch. I think I know why. "
           "You told me you never have breakfast! I had the same problem last year.",
           "Salom, Lola! Xating uchun rahmat. Tushlikdan oldin tez-tez qorning ochib, charchab qolishingni yozibsan. "
           "Menimcha, sababini bilaman. Axir menga hech qachon nonushta qilmasligingni aytgansan! Oʻtgan yili menda ham xuddi shu muammo bor edi."),
         P("Our school doctor gave us some good advice. After a long night, your body needs energy. A good breakfast "
           "helps you think better in your morning lessons. If you skip breakfast, you may want sweet snacks later in the day.",
           "Maktabimiz shifokori bizga yaxshi maslahat bergan edi. Uzun tundan keyin tanangga quvvat kerak. Yaxshi nonushta "
           "ertalabki darslarda yaxshiroq fikrlashingga yordam beradi. Agar nonushtani tashlab ketsang, kunning keyingi qismida "
           "shirin gazak yeging kelishi mumkin."),
         P("So what is a healthy breakfast? You don't need much time. My favourite is porridge with milk and some fruit. "
           "On other days I have an egg, some bread and a cucumber. My grandmother always says that a bowl of warm "
           "porridge is better than a plate of biscuits!",
           "Xoʻsh, sogʻlom nonushta qanday boʻladi? Buning uchun koʻp vaqt kerak emas. Mening sevimli nonushtam — sutli boʻtqa va "
           "biroz meva. Boshqa kunlari tuxum, non va bodring yeyman. Buvim doim bir kosa issiq boʻtqa bir likopcha "
           "pechenyedan yaxshiroq, deydi!"),
         P("Try not to eat too much sugar in the morning. Sweet cakes and fizzy drinks give you energy for a short time, "
           "but soon you feel hungry again. A glass of water or a cup of tea without much sugar is a good choice.",
           "Ertalab juda koʻp shakar yemaslikka harakat qil. Shirin pishiriqlar va gazli ichimliklar qisqa vaqtga quvvat beradi, "
           "lekin tez orada yana qorning ochadi. Bir stakan suv yoki kam shakarli bir piyola choy — yaxshi tanlov."),
         P("Why don't you try it for one week? Get up fifteen minutes earlier and eat something healthy. "
           "Then write and tell me how you feel! Love, Dilfuza",
           "Nega bir hafta sinab koʻrmaysan? Oʻn besh daqiqa ertaroq tur va sogʻlom biror narsa ye. "
           "Keyin oʻzingni qanday his qilayotganingni yozib yubor! Mehr bilan, Dilfuza"),
     ],
     [G('hungry', 'och, qorni och'), G('advice', 'maslahat'), G('energy', 'quvvat, energiya'),
      G('skip', 'tashlab ketmoq, oʻtkazib yubormoq'), G('snack', 'gazak, yengil tamaddi'), G('healthy', 'sogʻlom, foydali'),
      G('porridge', 'boʻtqa'), G('bowl', 'kosa'), G('sugar', 'shakar'), G('choice', 'tanlov'),
      G('earlier', 'ertaroq')],
     [GN('e45-comparatives', 'Qiyosiy daraja: better than', 'a bowl of warm porridge is better than a plate of biscuits'),
      GN('e42-much-many', 'much — sanalmaydigan otlar bilan', "You don't need much time.")],
     [
         tf('Lola often feels hungry before lunch.', 'T', '«You said you often feel hungry and tired before lunch.»', 0),
         tf('Dilfuza never had a problem with breakfast.', 'F', '«I had the same problem last year.»', 0),
         ch('Who gave the students advice about breakfast at school?', ['Dilfuza\'s grandmother', 'the school doctor',
                                                                         'the English teacher'], 1,
            '«Our school doctor gave us some good advice.» Buvisi esa boʻtqa haqida gapiradi.', 1),
         ch('What can happen if you skip breakfast?', ['You may want sweet snacks later.', 'You sleep better at night.',
                                                       'You think better in your lessons.'], 0,
            '«If you skip breakfast, you may want sweet snacks later in the day.» Yaxshi fikrlashga esa nonushta yordam beradi.', 1),
         gap("Dilfuza's favourite breakfast is porridge with ___ and some fruit.", 'milk',
             '«My favourite is porridge with milk and some fruit.»', 2, max_words=1),
         tf("Dilfuza's grandmother thinks biscuits are better than porridge.", 'F',
            'Aksincha: «a bowl of warm porridge is better than a plate of biscuits».', 2),
         ch('Which drink does Dilfuza suggest in the morning?', ['a fizzy drink', 'water or tea without much sugar',
                                                                 'sweet juice'], 1,
            '«A glass of water or a cup of tea without much sugar is a good choice.»', 3),
         gap('Dilfuza tells Lola to get up ___ minutes earlier.', ['fifteen', '15'],
             '«Get up fifteen minutes earlier and eat something healthy.»', 4, max_words=1),
     ])

text(B, 'a2-24-sleep', 'Uyqu nega muhim?', 'Why Is Sleep Important?', 'A2', 'article', HEALTH,
     'Bu maqola uyqu tanamiz va miyamiz uchun nima uchun kerakligini tushuntiradi. Oʻqishdan oldin: '
     'siz yaxshi uxlamasangiz, ertasi kuni oʻzingizni qanday his qilasiz?',
     [
         P("Why do we sleep? Scientists still have many questions, but they agree on one thing: sleep is very important "
           "for our health. We spend about one third of our lives asleep!",
           "Biz nega uxlaymiz? Olimlarda hali ham koʻp savollar bor, lekin ular bir narsada hamfikr: uyqu sogʻligʻimiz uchun "
           "juda muhim. Biz umrimizning taxminan uchdan bir qismini uyquda oʻtkazamiz!"),
         P("While we sleep, the body rests and repairs itself. The brain is busy too. It sorts the things that we learned "
           "during the day and helps us remember them. That is why a good night's sleep before an exam is better than "
           "studying all night.",
           "Biz uxlayotganimizda tana dam oladi va oʻzini tiklaydi. Miya ham band boʻladi. U kun davomida oʻrgangan "
           "narsalarimizni tartibga soladi va ularni eslab qolishimizga yordam beradi. Shuning uchun imtihondan oldin "
           "yaxshilab uxlash tun boʻyi oʻqishdan yaxshiroq."),
         P("How much sleep do we need? Most adults need seven to nine hours. Children and teenagers need more, because "
           "their bodies are still growing. For example, teenagers need about eight to ten hours a night. But many "
           "teenagers sleep only six or seven hours on school nights.",
           "Bizga qancha uyqu kerak? Koʻpchilik kattalarga yetti-toʻqqiz soat kerak. Bolalar va oʻsmirlarga koʻproq kerak, "
           "chunki ularning tanasi hali oʻsyapti. Masalan, oʻsmirlarga bir kechada taxminan sakkiz-oʻn soat uyqu kerak. "
           "Lekin koʻp oʻsmirlar ertasi kuni dars bor kechalari atigi olti-yetti soat uxlaydi."),
         P("What happens if we don't sleep enough? We feel tired and get angry more easily, and it is harder to concentrate. "
           "Over a long time, too little sleep can also make people ill more often.",
           "Agar yetarlicha uxlamasak, nima boʻladi? Charchaymiz, tezroq jahlimiz chiqadi va diqqatni jamlash qiyinroq boʻladi. "
           "Uzoq vaqt davomida kam uxlash odamlarning tez-tez kasal boʻlishiga ham sabab boʻlishi mumkin."),
         P("Here are some simple tips. Go to bed and get up at the same time every day. Don't drink tea or coffee in the "
           "evening. Keep your bedroom dark and quiet, and put your phone away at least half an hour before bed.",
           "Mana bir nechta oddiy maslahat. Har kuni bir xil vaqtda yoting va turing. Kechqurun choy yoki qahva ichmang. "
           "Yotoq xonangizni qorongʻi va tinch tuting, telefoningizni esa uxlashdan kamida yarim soat oldin olib qoʻying."),
     ],
     [G('health', 'sogʻliq'), G('spend', '(vaqt) oʻtkazmoq'), G('asleep', 'uxlayotgan, uyquda'),
      G('repair', 'tuzatmoq, tiklamoq'), G('brain', 'miya'), G('remember', 'eslab qolmoq'),
      G('adult', 'katta yoshli odam'), G('grow', 'oʻsmoq'), G('concentrate', 'diqqatni jamlamoq'),
      G('ill', 'kasal'), G('tip', 'maslahat'), G('dark', 'qorongʻi')],
     [GN('e48-enough-too', 'enough / too — yetarli / haddan ortiq', "What happens if we don't sleep enough?"),
      GN('e55-who-which-that', 'that — aniqlovchi ergash gap', 'the things that we learned during the day')],
     [
         tf('Scientists know everything about sleep.', 'F', '«Scientists still have many questions» — hali savollar koʻp.', 0),
         gap('We spend about one ___ of our lives asleep.', 'third',
             '«We spend about one third of our lives asleep!» — uchdan bir qism.', 0, max_words=1),
         ch('What does the brain do while we sleep?', ['It stops working.', 'It helps us remember what we learned.',
                                                       'It grows bigger.'], 1,
            '«It sorts the things that we learned during the day and helps us remember them.»', 1),
         tf('The text says it is better to study all night before an exam.', 'F',
            'Aksincha: «a good night\'s sleep before an exam is better than studying all night».', 1),
         ch('How much sleep do most adults need?', ['five to six hours', 'seven to nine hours', 'ten to twelve hours'], 1,
            '«Most adults need seven to nine hours.»', 2),
         tf('Teenagers need more sleep than adults.', 'T',
            '«Children and teenagers need more, because their bodies are still growing.»', 2),
         gap('Without enough sleep, it is harder to ___.', 'concentrate',
             '«it is harder to concentrate» — diqqatni jamlash qiyinroq.', 3, max_words=1),
         ch('Which tip is in the text?', ['Drink tea in the evening.', 'Keep your bedroom dark and quiet.',
                                          'Use your phone in bed.'], 1,
            '«Keep your bedroom dark and quiet». Kechqurun choy ichmaslik, telefonni esa olib qoʻyish kerak.', 4),
     ])

text(B, 'a2-25-kurash', 'Kurash', 'Kurash', 'A2', 'article', SPORT,
     'Kurash — oʻzbek xalqining qadimiy milliy sporti. Oʻqishdan oldin: siz kurash bellashuvini koʻrganmisiz? '
     'Uning qanday qoidalarini bilasiz?',
     [
         P("Kurash is a traditional Uzbek form of wrestling. It is very old, and for hundreds of years people in Uzbekistan "
           "have enjoyed it at weddings, holidays and village festivals. In Uzbek, the word kurash simply means wrestling.",
           "Kurash — oʻzbeklarning anʼanaviy milliy olishuv turi. U juda qadimiy va yuzlab yillardan beri Oʻzbekistonda odamlar uni "
           "toʻylarda, bayramlarda va qishloq sayllarida tomosha qilib keladi. Oʻzbek tilida «kurash» soʻzi shunchaki "
           "olishuv, bellashuv degani."),
         P("In kurash, the two wrestlers stand during the whole fight. Each wrestler wears a jacket and a belt. "
           "In competitions, one wrestler usually wears a green jacket and the other wears a blue one. They hold each "
           "other's belts or jackets and try to throw the other person onto their back.",
           "Kurashda ikki kurashchi butun bellashuv davomida tik turadi. Har bir kurashchi yaktak kiyib, belbogʻ bogʻlaydi. "
           "Musobaqalarda odatda bir kurashchi yashil, ikkinchisi esa koʻk yaktak kiyadi. Ular bir-birining belbogʻi yoki "
           "yaktagidan ushlab, raqibini chalqancha yiqitishga harakat qiladi."),
         P("Kurash has some important rules. Wrestlers mustn't fight on the ground, and they mustn't hold their "
           "opponent's legs. Respect is very important too. Before and after the fight, the wrestlers greet each other politely.",
           "Kurashning muhim qoidalari bor. Kurashchilar yerda olishmasligi kerak va raqibining oyogʻidan ushlamasligi kerak. "
           "Hurmat ham juda muhim. Bellashuvdan oldin va keyin kurashchilar bir-biriga hurmat bilan salom beradi."),
         P("Today kurash is not only an Uzbek sport. People practise it in many countries around the world, and it has "
           "been part of big Asian competitions. Many young Uzbek wrestlers dream of winning international medals.",
           "Bugun kurash faqat oʻzbek sporti emas. Odamlar u bilan dunyoning koʻplab mamlakatlarida shugʻullanadi, "
           "u katta Osiyo musobaqalari dasturiga ham kiritilgan. Koʻplab yosh oʻzbek kurashchilari xalqaro medallar "
           "yutishni orzu qiladi."),
         P("Kurash is a good sport for young people. It makes your body strong and teaches you to be patient and respect "
           "other people. Many boys and girls in Uzbekistan train in sports clubs after school.",
           "Kurash yoshlar uchun yaxshi sport turi. U tanangizni baquvvat qiladi, sabrli boʻlishga va boshqalarni hurmat "
           "qilishga oʻrgatadi. Oʻzbekistonda koʻplab oʻgʻil va qizlar darsdan keyin sport toʻgaraklarida shugʻullanadi."),
     ],
     [G('traditional', 'anʼanaviy'), G('wrestling', 'kurash, olishuv'), G('wedding', 'toʻy'),
      G('wrestler', 'kurashchi, polvon'), G('jacket', 'yaktak, kurtka'), G('belt', 'belbogʻ'),
      G('throw', 'otmoq, yiqitmoq'), G('rule', 'qoida'), G('opponent', 'raqib'), G('respect', 'hurmat; hurmat qilmoq'),
      G('practise', 'shugʻullanmoq, mashq qilmoq'), G('patient', 'sabrli')],
     [GN('e16-for-since', 'for — davomiylik (Present Perfect bilan)',
         'for hundreds of years people in Uzbekistan have enjoyed it'),
      GN('e27-must-mustnt-neednt', 'mustn\'t — taqiq', "Wrestlers mustn't fight on the ground")],
     [
         tf('Kurash is a new sport from Europe.', 'F', '«Kurash is a traditional Uzbek form of wrestling. It is very old».', 0),
         gap('In Uzbek, the word kurash simply means ___.', 'wrestling',
             '«In Uzbek, the word kurash simply means wrestling.»', 0, max_words=1),
         ch('What does each wrestler wear?', ['a jacket and a belt', 'only shorts', 'a helmet'], 0,
            '«Each wrestler wears a jacket and a belt.»', 1),
         tf('In kurash, wrestlers stand during the whole fight.', 'T',
            '«the two wrestlers stand during the whole fight».', 1),
         ch('Which of these is NOT allowed in kurash?', ["holding the opponent's jacket", "holding the opponent's legs",
                                                         "holding the opponent's belt"], 1,
            '«they mustn\'t hold their opponent\'s legs». Belbogʻ va yaktakdan ushlash mumkin.', 2),
         tf('Wrestlers greet each other only after the fight.', 'F',
            'Oldin ham, keyin ham: «Before and after the fight, the wrestlers greet each other politely.»', 2),
         ch('Where do people practise kurash today?', ['only in Uzbekistan', 'only in villages',
                                                       'in many countries around the world'], 2,
            '«People practise it in many countries around the world».', 3),
         gap('Kurash teaches you to be ___ and respect other people.', 'patient',
             '«teaches you to be patient and respect other people».', 4, max_words=1),
     ])
