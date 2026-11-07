"""A1 · 2-boʻlim: Kundalik hayot (5 ta matn)"""
from lib import *

B = 'a1'
DAY = L('Kundalik hayot', 'Daily life')

text(B, 'a1-06-morning', 'Mening kunim', 'My Day', 'A1', 'story', DAY,
     'Bekzod oddiy bir kunini tasvirlaydi. Oʻqishdan oldin oʻylab koʻring: siz ertalab soat nechada turasiz?',
     [
         P("My name is Bekzod. I live in Fergana. On weekdays, I get up at half past six. I wash my face and get dressed. "
           "Then I have breakfast with my family. We usually eat bread and eggs and drink green tea.",
           "Mening ismim Bekzod. Men Fargʻonada yashayman. Ish kunlari soat olti yarimda turaman. Yuzimni yuvaman va kiyinaman. "
           "Keyin oilam bilan nonushta qilaman. Biz odatda non va tuxum yeymiz, koʻk choy ichamiz."),
         P("School starts at eight o'clock. I go to school by bus. It takes twenty minutes. I have six lessons every day. "
           "I never sleep in class!",
           "Maktab soat sakkizda boshlanadi. Men maktabga avtobusda boraman. Yoʻlga yigirma daqiqa ketadi. Har kuni oltita darsim bor. "
           "Men darsda hech qachon uxlamayman!"),
         P("I come home at two. After lunch, I do my homework. In the evening, I sometimes help my father in the garden. "
           "We have dinner at seven. I go to bed at ten.",
           "Uyga soat ikkida kelaman. Tushlikdan keyin uy vazifamni bajaraman. Kechqurun baʼzan otamga bogʻda yordam beraman. "
           "Soat yettida kechki ovqat yeymiz. Soat oʻnda uxlashga yotaman."),
     ],
     [G('get up', 'oʻrnidan turmoq'), G('wash', 'yuvmoq'), G('get dressed', 'kiyinmoq'), G('breakfast', 'nonushta'),
      G('usually', 'odatda'), G('lesson', 'dars'), G('never', 'hech qachon'), G('homework', 'uy vazifasi'),
      G('sometimes', 'baʼzan'), G('garden', 'bogʻ, tomorqa'), G('go to bed', 'uxlashga yotmoq')],
     [GN('b19-my-day', 'Present Simple: kundalik ishlar', 'I get up at half past six.'),
      GN('b24-frequency', 'usually, sometimes, never', 'We usually eat bread and eggs')],
     [
         tf('Bekzod lives in Tashkent.', 'F', 'U Fargʻonada yashaydi: «I live in Fergana.»', 0),
         ch('What time does Bekzod get up on weekdays?', ['at six', 'at half past six', 'at seven'], 1,
            '«On weekdays, I get up at half past six.» — half past six = olti yarim (6:30).', 0),
         tf('Bekzod drinks green tea at breakfast.', 'T', 'Nonushtada: «We usually eat bread and eggs and drink green tea.»', 0),
         ch('How does Bekzod go to school?', ['on foot', 'by car', 'by bus'], 2, '«I go to school by bus.»', 1),
         gap("School starts at ___ o'clock.", ['eight', '8'], 'Maktab soat sakkizda boshlanadi: «School starts at eight».', 1),
         tf('Bekzod does his homework before lunch.', 'F', 'Tushlikdan keyin: «After lunch, I do my homework.»', 2),
         gap('Bekzod goes to bed at ___.', ['ten', '10'], '«I go to bed at ten.» Soat yettida esa kechki ovqat yeyishadi.', 2),
     ])

text(B, 'a1-07-bazaar', 'Bozorda', 'At the Bazaar', 'A1', 'dialogue', L('Xarid', 'Shopping'),
     'Malika Chorsu bozorida meva va sabzavot sotib oladi. Oʻqishdan oldin: bozorda narxni inglizcha qanday soʻraysiz?',
     [
         P("Malika: Good morning! I want some apples, please. Seller: Good morning! These red apples are very sweet. "
           "They are 15,000 sum a kilo.",
           "Malika: Xayrli tong! Menga olma kerak edi. Sotuvchi: Xayrli tong! Mana bu qizil olmalar juda shirin. "
           "Ularning kilosi 15 000 soʻm."),
         P("Malika: Good. Two kilos, please. Do you have any grapes? Seller: Sorry, I don't have any grapes today. "
           "But I have some nice pears.",
           "Malika: Yaxshi. Ikki kilo bering, iltimos. Uzumingiz bormi? Sotuvchi: Kechirasiz, bugun uzum yoʻq. "
           "Lekin yaxshi noklarim bor."),
         P("Malika: No, thank you. How much are the tomatoes? Seller: They are 10,000 sum a kilo.",
           "Malika: Yoʻq, rahmat. Pomidor necha pul? Sotuvchi: Kilosi 10 000 soʻm."),
         P("Malika: One kilo, please. How much is that all together? Seller: That is 40,000 sum.",
           "Malika: Bir kilo bering, iltimos. Hammasi boʻlib qancha boʻldi? Sotuvchi: 40 000 soʻm."),
         P("Malika: Here you are. Thank you! Seller: Thank you. Come again!",
           "Malika: Mana, oling. Rahmat! Sotuvchi: Sizga ham rahmat. Yana keling!"),
     ],
     [G('seller', 'sotuvchi'), G('sweet', 'shirin'), G('kilo', 'kilogramm'), G('grapes', 'uzum'), G('pear', 'nok'),
      G('tomato', 'pomidor'), G('How much …?', 'Qancha turadi? Necha pul?'), G('all together', 'hammasi boʻlib'),
      G('Here you are.', 'Mana, oling.'), G('Come again!', 'Yana keling!')],
     [GN('b33-some-any', 'some / any', 'Do you have any grapes?'),
      GN('b31-countable', 'Sanaladigan otlar: apple → apples', 'These red apples are very sweet.')],
     [
         ch('What does Malika ask for first?', ['apples', 'grapes', 'pears'], 0, '«I want some apples, please.»', 0),
         tf('The red apples are sweet.', 'T', 'Sotuvchi aytadi: «These red apples are very sweet.»', 0),
         gap('The apples are ___ sum a kilo.', ['15,000', '15000', '15 000'], '«They are 15,000 sum a kilo.»', 0),
         tf('The seller has grapes today.', 'F', '«Sorry, I don\'t have any grapes today.» — bugun uzum yoʻq.', 1),
         ch('What does the seller offer instead of grapes?', ['tomatoes', 'pears', 'melons'], 1,
            '«But I have some nice pears.» Lekin Malika nok olmaydi.', 1),
         ch('How many kilos of tomatoes does Malika buy?', ['one', 'two', 'three'], 0,
            '«One kilo, please.» Ikki kilo — bu olma.', 3),
         gap('All together, Malika pays ___ sum.', ['40,000', '40000', '40 000'], '«That is 40,000 sum.» — 2 kilo olma 30 000 + 1 kilo pomidor 10 000.', 3),
     ])

text(B, 'a1-08-weekend', 'Dam olish kuni', 'My Weekend', 'A1', 'email', L('Dam olish', 'Free time'),
     'Bu — Nodiraning dugonasi Sevaraga yozgan xati. Oʻqishdan oldin: siz dam olish kunlari nima qilasiz?',
     [
         P("Hi Sevara, How are you? I am in a small village near Samarkand. My grandparents live here, and I visit them "
           "every month. It is very quiet here. There is a big garden with apple trees.",
           "Salom, Sevara! Qalaysan? Men Samarqand yaqinidagi kichik bir qishloqdaman. Bu yerda buvim va bobom yashaydi, "
           "men ularni har oy koʻrgani kelaman. Bu yer juda tinch. Bu yerda olma daraxtlari oʻsadigan katta bogʻ bor."),
         P("On Saturday, my grandfather and I go to the river. He likes fishing, but I don't. I read a book under a tree. "
           "On Sunday morning, my grandmother bakes bread in the tandir. It smells wonderful!",
           "Shanba kuni bobom bilan daryoga boramiz. U baliq tutishni yoqtiradi, men esa yoqtirmayman. Men daraxt tagida kitob oʻqiyman. "
           "Yakshanba kuni ertalab buvim tandirda non yopadi. Uning hidi ajoyib!"),
         P("I can't use the internet here, but I don't mind. I come back to Tashkent on Monday. "
           "Can we meet on Tuesday after school? Write soon! Love, Nodira",
           "Bu yerda internetdan foydalana olmayman, lekin bu meni bezovta qilmaydi. Dushanba kuni Toshkentga qaytaman. "
           "Seshanba kuni darsdan keyin uchrasha olamizmi? Tezroq javob yoz! Mehr bilan, Nodira"),
     ],
     [G('village', 'qishloq'), G('grandparents', 'buvi va bobo'), G('visit', 'koʻrgani bormoq, mehmon boʻlmoq'),
      G('quiet', 'tinch, sokin'), G('river', 'daryo'), G('fishing', 'baliq tutish'), G('under', 'tagida, ostida'),
      G('bake', '(non) yopmoq, pishirmoq'), G('smell', 'hid taratmoq, hidi kelmoq'), G('come back', 'qaytib kelmoq'),
      G('Write soon!', 'Tezroq javob yoz!')],
     [GN('b14-there-is', 'there is / there are', 'There is a big garden with apple trees.'),
      GN('b10-likes-dislikes', 'like + -ing: yoqtirmoq', "He likes fishing, but I don't.")],
     [
         tf('Nodira writes from Tashkent.', 'F', 'U Samarqand yaqinidagi qishloqda: «I am in a small village near Samarkand.»', 0),
         ch('How often does Nodira visit her grandparents?', ['every week', 'every month', 'every year'], 1,
            '«I visit them every month.»', 0),
         tf('Nodira likes fishing.', 'F', 'Baliq tutishni bobosi yoqtiradi, Nodira emas: «He likes fishing, but I don\'t.»', 1),
         gap('Nodira reads a book under a ___.', 'tree', '«I read a book under a tree.»', 1),
         ch('Who bakes bread?', ['Nodira', 'her grandfather', 'her grandmother'], 2,
            '«my grandmother bakes bread in the tandir».', 1),
         tf('Nodira can use the internet in the village.', 'F', '«I can\'t use the internet here».', 2),
         gap('Nodira wants to meet Sevara on ___.', 'Tuesday', '«Can we meet on Tuesday after school?» Dushanba — qaytish kuni.', 2),
     ])

text(B, 'a1-09-weather', 'Bugun ob-havo qanday?', "What's the Weather Like Today?", 'A1', 'dialogue', L('Ob-havo', 'Weather'),
     'Aziza Moskvada yashaydigan akasi Jamshid bilan telefonda gaplashadi. Oʻqishdan oldin: bugun sizning shahringizda ob-havo qanday?',
     [
         P("Aziza: Hello, Jamshid! How are you? How is Moscow? Jamshid: Hi, Aziza! I am fine, but it is very cold here. "
           "It is minus ten degrees today, and it is snowing.",
           "Aziza: Salom, Jamshid! Qalaysiz? Moskva qalay? Jamshid: Salom, Aziza! Yaxshiman, lekin bu yer juda sovuq. "
           "Bugun havo minus oʻn daraja, qor yogʻyapti."),
         P("Aziza: Here in Tashkent it is cold too, but it is sunny. It is five degrees. Jamshid: Five degrees? "
           "That is warm for me! What are you wearing?",
           "Aziza: Bu yerda, Toshkentda ham sovuq, lekin quyoshli. Havo besh daraja. Jamshid: Besh daraja? "
           "Men uchun bu iliq-ku! Ustingda nima bor?"),
         P("Aziza: I am wearing a coat and a hat. Jamshid: I am wearing a warm jacket, a scarf and gloves. "
           "I never go out without my gloves in winter.",
           "Aziza: Men palto va shapka kiyib olganman. Jamshid: Men issiq kurtka, sharf va qoʻlqop kiyib olganman. "
           "Qishda hech qachon qoʻlqopsiz koʻchaga chiqmayman."),
         P("Aziza: Be careful! Jamshid: Don't worry. I like the snow. Bye!",
           "Aziza: Ehtiyot boʻling! Jamshid: Xavotir olma. Men qorni yaxshi koʻraman. Xayr!"),
     ],
     [G('cold', 'sovuq'), G('degree', 'daraja'), G('minus', 'minus, noldan past'), G('snow', 'qor; qor yogʻmoq'),
      G('sunny', 'quyoshli'), G('warm', 'iliq; issiq'), G('wear', 'kiymoq, kiyib yurmoq'), G('coat', 'palto'),
      G('scarf', 'sharf'), G('gloves', 'qoʻlqop'), G('be careful', 'ehtiyot boʻlmoq')],
     [GN('b37-talking-weather', 'Ob-havo: it is cold, it is snowing', 'It is minus ten degrees today, and it is snowing.'),
      GN('b35-wearing-now', 'Hozir kiyib turgan narsa: I am wearing', 'I am wearing a coat and a hat.')],
     [
         tf('Jamshid is in Moscow.', 'T', 'Aziza soʻraydi: «How is Moscow?» Jamshid: «it is very cold here».', 0),
         ch('What is the weather like in Moscow today?', ['sunny and warm', 'cold and snowing', 'rainy and windy'], 1,
            '«it is very cold here… and it is snowing».', 0),
         gap('In Moscow, it is minus ___ degrees.', ['ten', '10'], '«It is minus ten degrees today».', 0),
         tf('It is snowing in Tashkent.', 'F', 'Toshkentda sovuq, lekin quyoshli: «it is cold too, but it is sunny».', 1),
         ch('What is Aziza wearing?', ['a coat and a hat', 'a jacket and gloves', 'a scarf and a hat'], 0,
            '«I am wearing a coat and a hat.» Kurtka va qoʻlqop — Jamshidda.', 2),
         tf('Jamshid sometimes goes out without his gloves in winter.', 'F',
            '«I never go out without my gloves in winter.» — never = hech qachon.', 2),
         gap('Jamshid likes the ___.', 'snow', '«Don\'t worry. I like the snow.»', 3),
     ])

text(B, 'a1-10-food', 'Sevimli taomim', 'My Favourite Food', 'A1', 'blog', L('Taomlar', 'Food'),
     'Bu — Sardorning ovqat haqidagi blogi. Oʻqishdan oldin: sizning sevimli taomingiz qaysi?',
     [
         P("Hello, everyone! Welcome to my food blog. My name is Sardor, and I am from Samarkand. "
           "Today I want to write about my favourite food. It is plov!",
           "Hammaga salom! Ovqat haqidagi blogimga xush kelibsiz. Mening ismim Sardor, men samarqandlikman. "
           "Bugun sevimli taomim haqida yozmoqchiman. Bu — palov!"),
         P("We make plov with rice, meat, carrots and onions. My father always cooks it in a big kazan. "
           "There is a lot of oil in it, so it is not very healthy, but it is delicious!",
           "Biz palovni guruch, goʻsht, sabzi va piyozdan tayyorlaymiz. Otam uni doim katta qozonda pishiradi. "
           "Unda yogʻ koʻp, shuning uchun u unchalik foydali emas, lekin juda mazali!"),
         P("We usually eat plov on Sundays. My mother makes a fresh salad with tomatoes and onions. "
           "We drink green tea with it. I never eat sweets after plov. I am always full!",
           "Biz odatda yakshanba kunlari palov yeymiz. Onam pomidor va piyozdan yangi salat qiladi. "
           "Palov bilan koʻk choy ichamiz. Palovdan keyin hech qachon shirinlik yemayman. Doim toʻyib qolaman!"),
         P("What is your favourite food? Write in the comments!",
           "Sizning sevimli taomingiz qaysi? Izohlarda yozing!"),
     ],
     [G('favourite', 'sevimli'), G('rice', 'guruch'), G('meat', 'goʻsht'), G('carrot', 'sabzi'), G('onion', 'piyoz'),
      G('oil', 'yogʻ (oʻsimlik yogʻi)'), G('healthy', 'sogʻlom, foydali'), G('delicious', 'mazali'),
      G('fresh', 'yangi, toza'), G('sweets', 'shirinliklar'), G('full', 'toʻq'), G('comments', 'izohlar')],
     [GN('b30-food-drink', 'Taom va ichimliklar', 'We make plov with rice, meat, carrots and onions.'),
      GN('b31-countable', 'Sanalmaydigan otlar: a lot of oil', 'There is a lot of oil in it')],
     [
         tf('Sardor is from Bukhara.', 'F', 'U Samarqanddan: «I am from Samarkand».', 0),
         ch("What is Sardor's favourite food?", ['shashlik', 'plov', 'manti'], 1, '«my favourite food. It is plov!»', 0),
         ch('Who cooks the plov?', ['Sardor', 'his mother', 'his father'], 2, '«My father always cooks it in a big kazan.»', 1),
         gap("Sardor's father cooks plov in a big ___.", ['kazan', 'qozon'], '«in a big kazan» — kazan = qozon.', 1),
         tf('Sardor says plov is very healthy.', 'F', '«it is not very healthy, but it is delicious!»', 1),
         gap('The family usually eats plov on ___.', ['Sundays', 'Sunday'], '«We usually eat plov on Sundays.»', 2),
         tf('The family drinks green tea with plov.', 'T', '«We drink green tea with it.»', 2),
     ])
