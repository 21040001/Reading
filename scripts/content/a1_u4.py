"""A1 · 4-boʻlim: Boʻsh vaqt (5 ta matn)"""
from lib import *

B = 'a1'

text(B, 'a1-16-football', 'Futbol jamoamiz', 'Our Football Team', 'A1', 'story', L('Sport', 'Sports'),
     'Otabek oʻz futbol jamoasi haqida gapirib beradi. Oʻqishdan oldin oʻylab koʻring: siz qaysi sportni yoqtirasiz?',
     [
         P("My name is Otabek. I am twelve years old. I love football. I play in a team at a sports school in Tashkent. "
           "Our team is called Yulduz.",
           "Mening ismim Otabek. Men oʻn ikki yoshdaman. Men futbolni juda yaxshi koʻraman. Men Toshkentdagi sport maktabida "
           "bir jamoada oʻynayman. Jamoamizning nomi «Yulduz»."),
         P("We train three times a week, on Monday, Wednesday and Friday. Our coach is Mr Rustamov. He is kind but strict. "
           "We run, pass the ball and play short games.",
           "Biz haftasiga uch marta — dushanba, chorshanba va juma kunlari mashq qilamiz. Murabbiyimiz — Rustamov. "
           "U mehribon, lekin talabchan. Biz yuguramiz, toʻp oshiramiz va qisqa oʻyinlar oʻynaymiz."),
         P("I am a goalkeeper. I am tall and I can jump high. My friend Sardor is our captain. He can run very fast.",
           "Men darvozabonman. Men baland boʻyliman va baland sakray olaman. Doʻstim Sardor — jamoamiz sardori. "
           "U juda tez yugura oladi."),
         P("On Sunday we have a big match against a team from Yunusobod. I am a little nervous, but I am happy too. "
           "Come and watch us!",
           "Yakshanba kuni bizda Yunusoboddagi jamoaga qarshi katta oʻyin bor. Men biroz hayajondaman, lekin xursandman ham. "
           "Kelib bizni tomosha qiling!"),
     ],
     [G('team', 'jamoa'), G('train', 'mashq qilmoq'), G('coach', 'murabbiy'), G('strict', 'talabchan, qattiqqoʻl'),
      G('pass the ball', 'toʻp oshirmoq'), G('goalkeeper', 'darvozabon'), G('jump', 'sakramoq'),
      G('captain', 'sardor, kapitan'), G('match', 'oʻyin, uchrashuv (sportda)'), G('against', 'qarshi'),
      G('nervous', 'hayajonlangan, xavotirli')],
     [GN('b40-sports', 'Sport soʻzlari: team, coach, match', 'Our coach is Mr Rustamov.'),
      GN('b29-can', 'can — qila olmoq', 'He can run very fast.')],
     [
         tf('Otabek is twelve years old.', 'T', '1-xatboshi: «I am twelve years old.»', 0),
         ch('How often does the team train?', ['once a week', 'three times a week', 'every day'], 1,
            '«We train three times a week» — dushanba, chorshanba va juma.', 1),
         tf('The coach is never strict.', 'F', 'Murabbiy talabchan: «He is kind but strict.»', 1),
         ch('What does Otabek do in the team?', ['He is the captain.', 'He is the goalkeeper.', 'He is the coach.'], 1,
            '«I am a goalkeeper.» Jamoa sardori (captain) esa — Sardor.', 2),
         gap('Sardor is the team ___.', 'captain', '«My friend Sardor is our captain.»', 2),
         tf('Sardor can run very fast.', 'T', '«He can run very fast.» — he = Sardor.', 2),
         gap('On Sunday, the team plays against a team from ___.', 'Yunusobod',
             '«a big match against a team from Yunusobod».', 3),
     ])

text(B, 'a1-17-cinema', 'Kino kechasi', 'Movie Night', 'A1', 'dialogue', L('Kino', 'Cinema'),
     'Zarina va Malika shanba kuni kinoga borishni rejalashtirmoqda. Oʻqishdan oldin: siz kinoga kim bilan borasiz?',
     [
         P("Zarina: Hi, Malika! Are you free on Saturday evening? Malika: Yes, I am. Why?",
           "Zarina: Salom, Malika! Shanba kuni kechqurun boʻshmisan? Malika: Ha, boʻshman. Nima edi?"),
         P("Zarina: Let's go to the cinema! There is a new cartoon about a little camel. "
           "Malika: Great idea! I love cartoons. What time does it start?",
           "Zarina: Yur, kinoga boraylik! Kichkina tuyacha haqida yangi multfilm chiqibdi. "
           "Malika: Zoʻr fikr! Men multfilmlarni juda yaxshi koʻraman. U soat nechada boshlanadi?"),
         P("Zarina: It starts at 7 o'clock. A ticket costs 40,000 sum. "
           "Malika: OK. Would you like to eat something first?",
           "Zarina: Soat 7 da boshlanadi. Bitta chipta 40 000 soʻm turadi. "
           "Malika: Mayli. Avval biror narsa yeyishni xohlaysanmi?"),
         P("Zarina: Yes! There is a nice cafe near the cinema. Let's meet there at 6 o'clock.",
           "Zarina: Ha! Kinoteatr yaqinida yaxshi kafe bor. Oʻsha yerda soat 6 da uchrashaylik."),
         P("Malika: Perfect. Can my brother come too? He is nine. Zarina: Of course! See you on Saturday!",
           "Malika: Ajoyib. Ukam ham kelsa boʻladimi? U toʻqqiz yoshda. Zarina: Albatta! Shanba kuni koʻrishguncha!"),
     ],
     [G('free', 'boʻsh (vaqti bor)'), G('evening', 'kechqurun'), G('cinema', 'kinoteatr, kino'),
      G('cartoon', 'multfilm'), G('camel', 'tuya'), G('start', 'boshlanmoq'), G('ticket', 'chipta'),
      G('would you like', '… ni xohlaysizmi?'), G('cafe', 'kafe'), G('near', 'yaqinida'), G('of course', 'albatta')],
     [GN('b39-suggestions', "Taklif: Let's …", "Let's go to the cinema!"),
      GN('b44-would-like', 'would like — xohlamoq', 'Would you like to eat something first?')],
     [
         tf('Malika is free on Saturday evening.', 'T', 'Zarina soʻraydi, Malika javob beradi: «Yes, I am.»', 0),
         ch('What film do the girls want to see?', ['an action film', 'a cartoon', 'a comedy'], 1,
            '«There is a new cartoon about a little camel.»', 1),
         gap("The film starts at ___ o'clock.", ['7', 'seven'],
             '3-xatboshi: «It starts at 7 o\'clock.» Soat 6 — kafedagi uchrashuv vaqti.', 2),
         ch('How much is a ticket?', ['40,000 sum', '14,000 sum', '4,000 sum'], 0,
            '«A ticket costs 40,000 sum.»', 2),
         tf("The girls meet at the cafe at 7 o'clock.", 'F',
            "Ular kafeda soat 6 da uchrashadi: «Let's meet there at 6 o'clock.» Soat 7 da film boshlanadi.", 3),
         gap('There is a nice ___ near the cinema.', 'cafe', '«There is a nice cafe near the cinema.»', 3),
         ch('Who can come with the girls too?', ["Malika's sister", "Zarina's mother", "Malika's brother"], 2,
            'Malika soʻraydi: «Can my brother come too?» Zarina: «Of course!»', 4),
     ])

text(B, 'a1-18-hobby', 'Mening xobbim', 'My Hobby', 'A1', 'blog', L('Xobbi', 'Hobbies'),
     'Bu — Kamolaning blogi. U sevimli mashgʻuloti haqida yozadi. Oʻqishdan oldin: sizning xobbingiz nima?',
     [
         P("Hi, everyone! I'm Kamola, and this is my blog. I am fourteen and I live in Samarkand. "
           "Today I want to tell you about my hobby. My hobby is drawing.",
           "Hammaga salom! Men Kamolaman, bu esa mening blogim. Men oʻn toʻrt yoshdaman va Samarqandda yashayman. "
           "Bugun sizga xobbim haqida aytib bermoqchiman. Mening xobbim — rasm chizish."),
         P("I draw every day after school. I usually draw people, cats and old buildings. "
           "Samarkand has many beautiful buildings, so I never get bored!",
           "Men har kuni darsdan keyin rasm chizaman. Odatda odamlar, mushuklar va qadimiy binolarni chizaman. "
           "Samarqandda goʻzal binolar koʻp, shuning uchun hech qachon zerikmayman!"),
         P("I have a big box of pencils and a small sketchbook. I always carry my sketchbook in my bag. "
           "On Saturdays I go to an art club. Our teacher is very friendly.",
           "Menda bir katta quti qalam va kichkina eskiz daftari bor. Eskiz daftarimni doim sumkamda olib yuraman. "
           "Shanba kunlari rasm toʻgaragiga boraman. Oʻqituvchimiz juda samimiy."),
         P("I also like reading and playing chess with my grandfather, but drawing is my favourite. "
           "What is your hobby? Write in the comments!",
           "Men kitob oʻqishni va bobom bilan shaxmat oʻynashni ham yoqtiraman, lekin eng sevimli mashgʻulotim — rasm chizish. "
           "Sizning xobbingiz nima? Izohlarda yozing!"),
     ],
     [G('hobby', 'xobbi, sevimli mashgʻulot'), G('draw', 'rasm chizmoq'), G('usually', 'odatda'),
      G('get bored', 'zerikmoq'), G('pencil', 'qalam'), G('sketchbook', 'eskiz daftari, rasm daftari'),
      G('carry', 'olib yurmoq'), G('art club', 'rasm toʻgaragi'), G('friendly', 'samimiy, xushmuomala'),
      G('chess', 'shaxmat'), G('comments', 'izohlar (internetda)')],
     [GN('b08-like-ing', 'like + -ing', 'I also like reading and playing chess with my grandfather'),
      GN('b42-hobbies-vocab', 'Xobbi haqida: My hobby is …', 'My hobby is drawing.')],
     [
         tf('Kamola lives in Samarkand.', 'T', '1-xatboshi: «I live in Samarkand.»', 0),
         ch("What is Kamola's favourite hobby?", ['reading', 'drawing', 'playing chess'], 1,
            '«My hobby is drawing.» Kitob va shaxmatni ham yoqtiradi, lekin «drawing is my favourite».', 0),
         ch('When does Kamola draw?', ['every day after school', 'only on Saturdays', 'only at night'], 0,
            '«I draw every day after school.»', 1),
         gap('Kamola usually draws people, cats and old ___.', 'buildings',
             '«I usually draw people, cats and old buildings.»', 1),
         tf('Kamola often gets bored.', 'F', 'Samarqandda goʻzal binolar koʻp: «so I never get bored!»', 1),
         gap('Kamola always carries her ___ in her bag.', 'sketchbook',
             '«I always carry my sketchbook in my bag.»', 2),
         tf('Kamola plays chess with her grandfather.', 'T',
            '«I also like reading and playing chess with my grandfather».', 3),
     ])

text(B, 'a1-19-birthday', 'Tugʻilgan kun taklifnomasi', 'A Birthday Invitation', 'A1', 'email',
     L('Bayramlar', 'Celebrations'),
     'Bu — Nilufarning dugonasiga yozgan xati. Oʻqishdan oldin: taklifnomada qanday maʼlumotlar boʻladi?',
     [
         P("Hi Aziza, how are you? I have good news. My birthday is on Saturday, 20 May, "
           "and I would like to invite you to my party!",
           "Salom, Aziza! Qalaysan? Menda yaxshi xabar bor. Mening tugʻilgan kunim 20-may, shanba kuni, "
           "va seni bazmimga taklif qilmoqchiman!"),
         P("The party is at our house in Yunusobod. It starts at 4 o'clock in the afternoon and finishes at 8. "
           "Our address is 12 Lola Street.",
           "Bazm Yunusoboddagi uyimizda boʻladi. U tushdan keyin soat 4 da boshlanib, 8 da tugaydi. "
           "Manzilimiz: Lola koʻchasi, 12-uy."),
         P("There is a big birthday cake and plov for everyone. We can play games and dance in the garden. "
           "My cousin Bekzod can play the guitar.",
           "Hamma uchun katta tugʻilgan kun torti va palov boʻladi. Biz bogʻda oʻyinlar oʻynashimiz va raqsga tushishimiz mumkin. "
           "Amakivachcham Bekzod gitara chala oladi."),
         P("Please don't bring a big present. A card is fine! Can you come? Please write back by Thursday. Love, Nilufar",
           "Iltimos, katta sovgʻa olib kelma. Bitta otkritka ham yetarli! Kela olasanmi? Iltimos, payshanbagacha javob yoz. "
           "Mehr bilan, Nilufar"),
     ],
     [G('good news', 'yaxshi xabar'), G('birthday', 'tugʻilgan kun'), G('invite', 'taklif qilmoq'),
      G('party', 'bazm, ziyofat'), G('afternoon', 'tushdan keyin, kunduzi'), G('finish', 'tugamoq'),
      G('address', 'manzil'), G('cake', 'tort'), G('cousin', 'amakivachcha, xolavachcha'),
      G('present', 'sovgʻa'), G('write back', 'javob yozmoq')],
     [GN('b44-would-like', 'would like — xohlamoq', 'I would like to invite you to my party!'),
      GN('b23-days-dates', 'Sanalar: on Saturday, 20 May', 'My birthday is on Saturday, 20 May')],
     [
         ch("When is Nilufar's birthday?", ['on Thursday, 20 May', 'on Saturday, 20 May', 'on Saturday, 12 May'], 1,
            '«My birthday is on Saturday, 20 May». Payshanba — javob berish muddati, 12 — uy raqami.', 0),
         tf('The party is at a cafe.', 'F', 'Bazm uyda boʻladi: «The party is at our house in Yunusobod.»', 1),
         ch('What time does the party start?', ["at 4 o'clock", "at 8 o'clock", "at 12 o'clock"], 0,
            '«It starts at 4… and finishes at 8.» Soat 8 da bazm tugaydi.', 1),
         gap("Nilufar's address is 12 ___ Street.", 'Lola', '«Our address is 12 Lola Street.»', 1),
         tf('There is a cake at the party.', 'T', '«There is a big birthday cake and plov for everyone.»', 2),
         gap('Bekzod can play the ___.', 'guitar', '«My cousin Bekzod can play the guitar.»', 2),
         tf('Aziza must bring a big present.', 'F', 'Nilufar yozadi: «Please don’t bring a big present. A card is fine!»', 3),
     ])

text(B, 'a1-20-apps', 'Telefonimdagi ilovalar', 'The Apps on My Phone', 'A1', 'story', L('Texnologiya', 'Technology'),
     'Sardor telefonidagi ilovalar haqida gapirib beradi. Oʻqishdan oldin: siz har kuni qaysi ilovalardan foydalanasiz?',
     [
         P("My name is Sardor. I am sixteen. I have a phone, and there are many apps on it. "
           "But I use only four apps a lot.",
           "Mening ismim Sardor. Men oʻn olti yoshdaman. Mening telefonim bor va unda koʻp ilovalar bor. "
           "Lekin men faqat toʻrtta ilovadan koʻp foydalanaman."),
         P("First, I have a music app. I listen to Uzbek and English songs on the bus every morning. "
           "Second, I have a dictionary app. It helps me with new English words.",
           "Birinchisi — musiqa ilovasi. Men har kuni ertalab avtobusda oʻzbekcha va inglizcha qoʻshiqlar tinglayman. "
           "Ikkinchisi — lugʻat ilovasi. U menga yangi inglizcha soʻzlarni oʻrganishda yordam beradi."),
         P("Third, I have a map app. When my family goes to a new place, it shows us the way. "
           "Fourth, I have a game app, but I only play for thirty minutes a day.",
           "Uchinchisi — xarita ilovasi. Oilam yangi joyga borganda, u bizga yoʻlni koʻrsatadi. "
           "Toʻrtinchisi — oʻyin ilovasi, lekin men kuniga faqat oʻttiz daqiqa oʻynayman."),
         P("At dinner my family doesn't use phones. We put them in a box and talk about our day. I like that too!",
           "Kechki ovqat paytida oilamiz telefonlardan foydalanmaydi. Biz ularni qutiga solib qoʻyamiz va kunimiz haqida "
           "gaplashamiz. Bu menga ham yoqadi!"),
     ],
     [G('app', 'ilova'), G('use', 'foydalanmoq, ishlatmoq'), G('listen to', '… ni tinglamoq'), G('song', 'qoʻshiq'),
      G('dictionary', 'lugʻat'), G('word', 'soʻz'), G('map', 'xarita'), G('show the way', 'yoʻl koʻrsatmoq'),
      G('minute', 'daqiqa'), G('dinner', 'kechki ovqat'), G('talk about', '… haqida gaplashmoq')],
     [GN('b28-technology', 'Texnologiya: phone, app', 'I have a phone, and there are many apps on it.'),
      GN('b26-music-media', 'Musiqa: listen to songs', 'I listen to Uzbek and English songs on the bus every morning.')],
     [
         tf('There are only four apps on Sardor\'s phone.', 'F',
            'Telefonida koʻp ilova bor: «there are many apps on it». U faqat toʻrttasidan koʻp foydalanadi.', 0),
         ch('Where does Sardor listen to music?', ['at school', 'on the bus', 'at dinner'], 1,
            '«I listen to Uzbek and English songs on the bus every morning.»', 1),
         gap('The dictionary app helps Sardor with new English ___.', 'words',
             '«It helps me with new English words.»', 1),
         ch('Which app shows the family the way?', ['the map app', 'the music app', 'the game app'], 0,
            '«I have a map app… it shows us the way.»', 2),
         tf('Sardor plays games for three hours a day.', 'F', 'Faqat oʻttiz daqiqa: «I only play for thirty minutes a day.»', 2),
         gap('At dinner, the family puts their phones in a ___.', 'box', '«We put them in a box and talk about our day.»', 3),
         tf("Sardor doesn't like dinner without phones.", 'F', 'Unga bu yoqadi: «I like that too!»', 3),
     ])
