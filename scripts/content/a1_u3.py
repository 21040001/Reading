"""A1 · 3-boʻlim: Shahrim (5 ta matn)"""
from lib import *

B = 'a1'
CITY = L('Shahar', 'City')

text(B, 'a1-11-metro', 'Toshkent metrosi', 'The Tashkent Metro', 'A1', 'blog', L('Transport', 'Transport'),
     'Bekzod blogida Toshkent metrosi haqida yozadi. Oʻqishdan oldin: siz metroda yurganmisiz? Sizga qaysi bekat yoqadi?',
     [
         P("Hi, I'm Bekzod. I live in Tashkent. Every day I go to college by metro. The metro is fast and cheap. "
           "It is not new. The first line is from 1977.",
           "Salom, men Bekzodman. Men Toshkentda yashayman. Har kuni kollejga metroda boraman. Metro tez va arzon. "
           "U yangi emas. Birinchi liniya 1977-yilda ochilgan."),
         P("Today there are many lines. In the morning the trains are very full, so I always stand.",
           "Hozir metroda koʻplab liniyalar bor. Ertalab poyezdlar juda gavjum boʻladi, shuning uchun men doim tik turaman."),
         P("The stations are very beautiful. My favourite station is Kosmonavtlar. It is blue, and there are pictures of "
           "cosmonauts on the walls. Alisher Navoi station is beautiful too.",
           "Bekatlar juda chiroyli. Mening sevimli bekatim — «Kosmonavtlar». U koʻk rangda, devorlarida "
           "kosmonavtlarning suratlari bor. «Alisher Navoiy» bekati ham chiroyli."),
         P("Tips for visitors: buy a ticket at the station. Don\'t stand near the edge of the platform. "
           "And please give your seat to old people!",
           "Mehmonlar uchun maslahatlar: chiptani bekatda sotib oling. Platforma chetiga yaqin turmang. "
           "Va iltimos, keksalarga joy bering!"),
     ],
     [G('college', 'kollej'), G('fast', 'tez'), G('cheap', 'arzon'), G('line', 'liniya, yoʻnalish'),
      G('full', 'toʻla, gavjum'), G('station', 'bekat'), G('wall', 'devor'), G('visitor', 'mehmon, tashrif buyuruvchi'),
      G('ticket', 'chipta'), G('edge', 'chet, qirra'), G('seat', 'oʻrindiq, joy')],
     [GN('b14-there-is', 'there is / there are', 'Today there are many lines.'),
      GN('b15-around-town', 'Shaharda: go by metro', 'Every day I go to college by metro.')],
     [
         ch('How does Bekzod go to college?', ['by bus', 'by metro', 'by taxi'], 1,
            '«Every day I go to college by metro.»', 0),
         tf('The first metro line is from 1977.', 'T', '«The first line is from 1977.» — birinchi liniya 1977-yilda ochilgan.', 0),
         tf('The metro is slow and expensive.', 'F', 'Aksincha, metro tez va arzon: «The metro is fast and cheap.»', 0),
         tf('In the morning Bekzod always sits on the train.', 'F',
            'Ertalab poyezd gavjum, u doim tik turadi: «so I always stand».', 1),
         ch("What is Bekzod's favourite station?", ['Alisher Navoi', 'Chilonzor', 'Kosmonavtlar'], 2,
            '«My favourite station is Kosmonavtlar.» «Alisher Navoi» ham chiroyli, lekin sevimlisi emas.', 2),
         gap('At Kosmonavtlar there are pictures of ___ on the walls.', 'cosmonauts',
             '«there are pictures of cosmonauts on the walls».', 2, max_words=1),
         gap('Please give your ___ to old people.', 'seat', '«please give your seat to old people!»', 3, max_words=1),
     ])

text(B, 'a1-12-library', 'Kutubxonada', 'At the Library', 'A1', 'dialogue', CITY,
     'Bu — kutubxonadagi suhbat. Malika kutubxonachi bilan gaplashadi. Oʻqishdan oldin: kutubxonaga borish uchun sizga nima kerak?',
     [
         P("Malika: Good afternoon! Can I get a library card, please? "
           "Librarian: Yes, of course. Write your name and address here, please.",
           "Malika: Xayrli kun! Kutubxona kartasini olsam boʻladimi? "
           "Kutubxonachi: Ha, albatta. Iltimos, ismingiz va manzilingizni shu yerga yozing."),
         P("Malika: Thank you. Where are the English books? Librarian: They are on the second floor, next to the computers.",
           "Malika: Rahmat. Ingliz tilidagi kitoblar qayerda? Kutubxonachi: Ular ikkinchi qavatda, kompyuterlarning yonida."),
         P("Malika: Can I take three books? Librarian: Yes, you can. You can keep them for two weeks.",
           "Malika: Uchta kitob olsam boʻladimi? Kutubxonachi: Ha, mumkin. Ularni ikki hafta saqlashingiz mumkin."),
         P("Malika: Is the library open on Sunday? Librarian: No, it isn\'t. We are open from Monday to Saturday.",
           "Malika: Kutubxona yakshanba kuni ochiqmi? Kutubxonachi: Yoʻq, ochiq emas. Biz dushanbadan shanbagacha ishlaymiz."),
         P("Malika: And can I use the computers? Librarian: Yes, but please be quiet!",
           "Malika: Kompyuterlardan ham foydalansam boʻladimi? Kutubxonachi: Ha, lekin iltimos, jim boʻling!"),
     ],
     [G('library card', 'kutubxona kartasi'), G('librarian', 'kutubxonachi'), G('address', 'manzil'),
      G('floor', 'qavat'), G('next to', 'yonida'), G('keep', 'saqlamoq, oʻzida olib turmoq'), G('week', 'hafta'),
      G('open', 'ochiq'), G('use', 'foydalanmoq'), G('quiet', 'jim, sokin')],
     [GN('b29-can', 'Can I …? — ruxsat soʻrash', 'Can I take three books?'),
      GN('b16-prepositions-place', 'Joy predloglari: on, next to', 'They are on the second floor, next to the computers.')],
     [
         ch('What does Malika want first?', ['a library card', 'a computer', 'a newspaper'], 0,
            '«Can I get a library card, please?»', 0),
         gap('Malika writes her name and ___.', 'address', '«Write your name and address here, please.»', 0, max_words=1),
         ch('Where are the English books?', ['on the first floor', 'on the second floor', 'on the third floor'], 1,
            '«They are on the second floor, next to the computers.»', 1),
         tf('Malika can take three books.', 'T', 'Kutubxonachi: «Yes, you can.»', 2),
         ch('How long can Malika keep the books?', ['one week', 'two weeks', 'three weeks'], 1,
            '«You can keep them for two weeks.» Uch — kitoblar soni.', 2),
         tf('The library is open on Sunday.', 'F', 'Yakshanba kuni yopiq: «No, it isn\'t.» — «from Monday to Saturday».', 3),
         tf('Malika can use the computers.', 'T', '«Yes, but please be quiet!» — foydalanish mumkin, faqat jim boʻlish kerak.', 4),
     ])

text(B, 'a1-13-neighbour', 'Yangi qoʻshni', 'A New Neighbour', 'A1', 'email', L('Qoʻshnilar', 'Neighbours'),
     'Nodira dugonasi Zarinaga elektron xat yozadi. Oʻqishdan oldin: qoʻshnilaringizni taniysizmi? Ular qanday odamlar?',
     [
         P("Hi Zarina, How are you? I have news. We have a new neighbour! Her name is Saida. "
           "She lives in the flat next to ours. She is from Fergana.",
           "Salom, Zarina! Qalaysan? Yangilik bor. Bizning yangi qoʻshnimiz bor! Uning ismi Saida. "
           "U bizning yonimizdagi kvartirada yashaydi. U Fargʻonadan."),
         P("Saida is a doctor at the children's hospital. She is kind and friendly. She has a little son. "
           "His name is Amir, and he is four. He loves cats.",
           "Saida bolalar kasalxonasida shifokor. U mehribon va xushmuomala. Uning kichkina oʻgʻli bor. "
           "Uning ismi Amir, u toʻrt yoshda. U mushuklarni yaxshi koʻradi."),
         P("Every evening, Amir plays with my cat Laylo in the yard. Saida often comes to our home for tea. "
           "My mother likes her very much.",
           "Har kuni kechqurun Amir mening mushugim Laylo bilan hovlida oʻynaydi. Saida tez-tez bizga choyga keladi. "
           "Onam uni juda yaxshi koʻradi."),
         P("Come to my house on Saturday. You can meet them! Love, Nodira",
           "Shanba kuni uyimga kel. Ular bilan tanishishing mumkin! Mehr bilan, Nodira"),
     ],
     [G('news', 'yangilik'), G('neighbour', 'qoʻshni'), G('next to', 'yonida'), G('doctor', 'shifokor'),
      G('kind', 'mehribon'), G('friendly', 'xushmuomala, doʻstona'), G('son', 'oʻgʻil'), G('yard', 'hovli'),
      G('often', 'tez-tez'), G('meet', 'tanishmoq, uchrashmoq')],
     [GN('b06-jobs', 'Kasblar: She is a doctor', "Saida is a doctor at the children's hospital."),
      GN('b24-frequency', 'every evening, often', 'Saida often comes to our home for tea.')],
     [
         tf('Saida lives next to Nodira.', 'T', '«She lives in the flat next to ours.»', 0),
         ch('Where is Saida from?', ['Tashkent', 'Fergana', 'Bukhara'], 1, '«She is from Fergana.»', 0),
         ch("What is Saida's job?", ['a teacher', 'a nurse', 'a doctor'], 2,
            '«Saida is a doctor at the childrenʼs hospital.»', 1),
         tf('Amir is six years old.', 'F', 'Amir toʻrt yoshda: «he is four».', 1),
         gap('Amir plays with the cat in the ___.', 'yard', '«Amir plays with my cat Laylo in the yard».', 2, max_words=1),
         tf("Nodira's mother doesn\'t like Saida.", 'F', 'Aksincha: «My mother likes her very much.»', 2),
         ch('When can Zarina meet Saida and Amir?', ['on Saturday', 'on Sunday', 'every evening'], 0,
            '«Come to my house on Saturday. You can meet them!»', 3),
     ])

text(B, 'a1-14-post', 'Pochtada', 'At the Post Office', 'A1', 'notice', CITY,
     'Bu — pochta boʻlimidagi eʼlon. Oʻqishdan oldin: pochtada nimalar qilish mumkin? Ish vaqti va qoidalarga eʼtibor bering.',
     [
         P("Welcome to the Chilonzor Post Office! We are open from Monday to Saturday, from 9 a.m. to 6 p.m. "
           "We are closed on Sunday.",
           "Chilonzor pochta boʻlimiga xush kelibsiz! Biz dushanbadan shanbagacha, ertalab soat 9 dan kechki 6 gacha ishlaymiz. "
           "Yakshanba kuni yopiqmiz."),
         P("Here you can send letters and parcels to all cities in Uzbekistan and to other countries. "
           "You can also buy stamps, envelopes and postcards.",
           "Bu yerda Oʻzbekistonning barcha shaharlariga va boshqa mamlakatlarga xat va posilka yuborishingiz mumkin. "
           "Shuningdek, marka, konvert va otkritka sotib olishingiz mumkin."),
         P("Do you want to send a parcel? Please write the address clearly. Don\'t put food or water in your parcel. "
           "Take big parcels to Window 3.",
           "Posilka yubormoqchimisiz? Iltimos, manzilni aniq yozing. Posilkangizga oziq-ovqat yoki suv solmang. "
           "Katta posilkalarni 3-darchaga olib boring."),
         P("Do you have a question? Ask our staff at Window 1. Please wait in line. Thank you!",
           "Savolingiz bormi? 1-darchadagi xodimlarimizdan soʻrang. Iltimos, navbatda turing. Rahmat!"),
     ],
     [G('post office', 'pochta boʻlimi'), G('closed', 'yopiq'), G('send', 'yubormoq'), G('letter', 'xat'),
      G('parcel', 'posilka'), G('stamp', 'marka'), G('envelope', 'konvert'), G('postcard', 'otkritka'),
      G('clearly', 'aniq, tushunarli'), G('staff', 'xodimlar'), G('wait in line', 'navbatda turmoq')],
     [GN('b23-days-dates', 'from Monday to Saturday', 'We are open from Monday to Saturday'),
      GN('b29-can', 'can — qila olmoq', 'You can also buy stamps, envelopes and postcards.')],
     [
         tf('The post office is open on Sunday.', 'F', '«We are closed on Sunday.»', 0),
         ch('What time does the post office close?', ['at 5 p.m.', 'at 6 p.m.', 'at 9 p.m.'], 1,
            '«from 9 a.m. to 6 p.m.» — soat 6 da yopiladi.', 0),
         tf('You can send letters to other countries.', 'T',
            '«you can send letters and parcels to all cities in Uzbekistan and to other countries».', 1),
         gap('You can also buy stamps, ___ and postcards.', 'envelopes',
             '«You can also buy stamps, envelopes and postcards.»', 1, max_words=1),
         tf('You can put food in your parcel.', 'F', '«Don\'t put food or water in your parcel.» — mumkin emas.', 2),
         ch('Where do you take a big parcel?', ['to Window 1', 'to Window 2', 'to Window 3'], 2,
            '«Take big parcels to Window 3.» 1-darcha — savollar uchun.', 2),
         ch('Where can you ask a question?', ['at Window 1', 'at Window 3', 'on the phone'], 0,
            '«Ask our staff at Window 1.»', 3),
     ])

text(B, 'a1-15-park', 'Bogʻda sayr', 'A Walk in the Park', 'A1', 'story', L('Dam olish', 'Free time'),
     'Sardor bobosi bilan bogʻda sayr qiladi. Oʻqishdan oldin: siz dam olish kunlari qayerda sayr qilasiz?',
     [
         P("My name is Sardor. I live in Namangan, the city of flowers. Every Sunday morning, I walk in the park "
           "with my grandfather. The park is near our house. It is big and green.",
           "Mening ismim Sardor. Men gullar shahri Namanganda yashayman. Har yakshanba ertalab bobom bilan bogʻda sayr qilaman. "
           "Bogʻ uyimiz yaqinida. U katta va yam-yashil."),
         P("There are tall trees, flowers and a small lake. There are ducks on the lake. We always bring bread for them.",
           "U yerda baland daraxtlar, gullar va kichik koʻl bor. Koʻlda oʻrdaklar bor. Biz ularga doim non olib boramiz."),
         P("My grandfather likes chess. Old men play chess under the trees. He often plays with his friend Hamid aka. "
           "I watch them and learn.",
           "Bobom shaxmatni yaxshi koʻradi. Keksalar daraxtlar tagida shaxmat oʻynashadi. U tez-tez doʻsti Hamid aka bilan oʻynaydi. "
           "Men ularni tomosha qilaman va oʻrganaman."),
         P("After the game, we buy ice cream and sit on a bench. Then Grandfather says, \"Let's go home! "
           "A walk is good for you.\"",
           "Oʻyindan keyin biz muzqaymoq sotib olamiz va oʻrindiqda oʻtiramiz. Keyin bobom aytadi: «Qani, uyga ketdik! "
           "Sayr sogʻliq uchun foydali.»"),
     ],
     [G('flower', 'gul'), G('walk', 'sayr qilmoq; sayr'), G('grandfather', 'bobo'), G('near', 'yaqinida'),
      G('tree', 'daraxt'), G('lake', 'koʻl'), G('duck', 'oʻrdak'), G('chess', 'shaxmat'), G('under', 'tagida, ostida'),
      G('ice cream', 'muzqaymoq'), G('bench', 'oʻrindiq, skameyka')],
     [GN('b14-there-is', 'there is / there are', 'There are ducks on the lake.'),
      GN('b39-suggestions', "Taklif: Letʼs …", "Let's go home!")],
     [
         tf('Sardor walks in the park every Sunday morning.', 'T',
            '«Every Sunday morning, I walk in the park with my grandfather.»', 0),
         tf('The park is far from their house.', 'F', '«The park is near our house.»', 0),
         ch('What is on the lake?', ['boats', 'ducks', 'fish'], 1, '«There are ducks on the lake.»', 1),
         gap('Sardor and his grandfather always bring ___ for the ducks.', 'bread',
             '«We always bring bread for them.»', 1, max_words=1),
         ch('What game does the grandfather like?', ['football', 'chess', 'cards'], 1, '«My grandfather likes chess.»', 2),
         tf('Sardor plays chess with Hamid aka.', 'F',
            'Hamid aka bilan bobosi oʻynaydi, Sardor esa tomosha qiladi: «I watch them and learn.»', 2),
         ch('What do they do after the game?', ['They go home.', 'They buy ice cream.', 'They feed the ducks.'], 1,
            '«After the game, we buy ice cream and sit on a bench.»', 3),
     ])
