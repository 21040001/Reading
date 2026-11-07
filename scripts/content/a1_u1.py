"""A1 · 1-boʻlim: Men va oilam (5 ta matn)"""
from lib import *

B = 'a1'
FAM = L('Oila', 'Family')
SCH = L('Maktab', 'School')

text(B, 'a1-01-dilnoza', 'Salom, men Dilnozaman', "Hello, I'm Dilnoza", 'A1', 'story', L('Tanishuv', 'Introductions'),
     'Dilnoza oʻzi haqida gapirib beradi. Oʻqishdan oldin oʻylab koʻring: siz oʻzingizni inglizcha qanday tanishtirasiz?',
     [
         P("Hello! My name is Dilnoza. I am fifteen years old. I am from Uzbekistan. I live in Bukhara with my family.",
           "Salom! Mening ismim Dilnoza. Men oʻn besh yoshdaman. Men Oʻzbekistondanman. Men oilam bilan Buxoroda yashayman."),
         P("I am a student. I go to School Number 12. My favourite subject is English. I also like music. I can play the dutar.",
           "Men oʻquvchiman. Men 12-maktabda oʻqiyman. Mening sevimli fanim — ingliz tili. Men musiqani ham yoqtiraman. Men dutor chala olaman."),
         P("Bukhara is an old and beautiful city. Many tourists come here every year. I want to be a tour guide in the future.",
           "Buxoro — qadimiy va goʻzal shahar. Har yili bu yerga koʻplab sayyohlar keladi. Men kelajakda gid boʻlishni xohlayman."),
     ],
     [G('student', 'oʻquvchi, talaba'), G('subject', 'fan (maktabdagi)'), G('favourite', 'sevimli'), G('also', 'ham'),
      G('old', 'qadimiy; eski; keksa'), G('tourist', 'sayyoh'), G('every year', 'har yili'),
      G('tour guide', 'gid, ekskursiya boshlovchisi'), G('in the future', 'kelajakda')],
     [GN('b03-about-yourself', 'to be: am / is / are', 'I am fifteen years old.'),
      GN('b29-can', 'can — qila olmoq', 'I can play the dutar.')],
     [
         tf('Dilnoza is fifteen years old.', 'T', '1-xatboshi: «I am fifteen years old.»', 0),
         tf('Dilnoza lives in Samarkand.', 'F', 'U Buxoroda yashaydi: «I live in Bukhara».', 0),
         tf('Her favourite subject is music.', 'F', 'Sevimli fani — ingliz tili. Musiqani «ham» yoqtiradi.', 1),
         ch('What can Dilnoza play?', ['the piano', 'the dutar', 'football'], 1, '«I can play the dutar.»', 1),
         ch('What does Dilnoza want to be?', ['a teacher', 'a doctor', 'a tour guide'], 2,
            '«I want to be a tour guide in the future.»', 2),
         gap('Bukhara is an old and ___ city.', 'beautiful', '3-xatboshi: «an old and beautiful city».', 2),
         gap('Many ___ come to Bukhara every year.', 'tourists', 'Har yili koʻplab sayyohlar keladi — tourists.', 2),
     ])

text(B, 'a1-02-family', 'Mening oilam', 'My Family', 'A1', 'story', FAM,
     'Jasur oilasi haqida yozadi. Oʻqishdan oldin: sizning oilangizda necha kishi bor?',
     [
         P("My name is Jasur. There are six people in my family: my father, my mother, my grandmother, my two sisters and me.",
           "Mening ismim Jasur. Oilamizda olti kishi bor: otam, onam, buvim, opam, singlim va men."),
         P("My father is a driver. He drives a bus in Tashkent. My mother is a nurse. She works at a hospital. "
           "My grandmother doesn't work. She cooks very good plov!",
           "Otam haydovchi. U Toshkentda avtobus haydaydi. Onam hamshira. U kasalxonada ishlaydi. "
           "Buvim ishlamaydi. U juda mazali palov pishiradi!"),
         P("My sisters are Madina and Shahzoda. Madina is twenty. She is a student at university. "
           "Shahzoda is eight. She is very funny. We have a cat. Its name is Momiq.",
           "Opamning ismi Madina, singlimniki — Shahzoda. Madina yigirma yoshda. U universitet talabasi. "
           "Shahzoda sakkiz yoshda. U juda kulgili. Bizning mushugimiz bor. Uning ismi Momiq."),
     ],
     [G('people', 'odamlar, kishilar'), G('driver', 'haydovchi'), G('drive', 'haydamoq'), G('nurse', 'hamshira'),
      G('hospital', 'kasalxona'), G('cook', 'ovqat pishirmoq; oshpaz'), G('funny', 'kulgili, quvnoq'),
      G('university', 'universitet')],
     [GN('b14-there-is', 'there is / there are', 'There are six people in my family.'),
      GN('b04-family', 'Egalik: my, his, her, its', 'Its name is Momiq.')],
     [
         tf("There are five people in Jasur's family.", 'F', 'Olti kishi: «There are six people in my family».', 0),
         tf('His father drives a bus.', 'T', '«He drives a bus in Tashkent.»', 1),
         ch('Where does his mother work?', ['at a school', 'at a hospital', 'at a bazaar'], 1,
            'Onasi hamshira: «She works at a hospital.»', 1),
         tf('His grandmother works at a hospital.', 'F', 'Buvisi ishlamaydi: «My grandmother doesn\'t work.»', 1),
         ch('How old is Madina?', ['eight', 'twelve', 'twenty'], 2, '«Madina is twenty.» Sakkiz yoshdagisi — Shahzoda.', 2),
         gap("Jasur's grandmother cooks very good ___.", 'plov', '«She cooks very good plov!»', 1),
         gap("The cat's name is ___.", 'Momiq', '«Its name is Momiq.» — its = uning (hayvon haqida).', 2),
     ])

text(B, 'a1-03-flat', 'Bizning kvartiramiz', 'Our Flat', 'A1', 'story', L('Uy', 'Home'),
     'Bir bola uyini tasvirlaydi. Oʻqishdan oldin: sizning xonangizda nimalar bor?',
     [
         P("We live in a flat in Chilonzor. It is on the fourth floor. The building has a lift, but it is often broken!",
           "Biz Chilonzordagi kvartirada yashaymiz. U toʻrtinchi qavatda. Binoda lift bor, lekin u tez-tez buzilib qoladi!"),
         P("Our flat has three rooms, a kitchen and a bathroom. The living room is big. There is a sofa, a TV and a big carpet "
           "on the floor. My grandmother's room is next to the kitchen.",
           "Kvartiramizda uchta xona, oshxona va hammom bor. Mehmonxona katta. U yerda divan, televizor va polda katta gilam bor. "
           "Buvimning xonasi oshxonaning yonida."),
         P("My room is small, but I love it. There is a bed, a desk and a bookshelf. My computer is on the desk. "
           "From my window I can see a park.",
           "Mening xonam kichkina, lekin men uni yaxshi koʻraman. Unda karavot, yozuv stoli va kitob javoni bor. "
           "Kompyuterim stol ustida. Derazamdan bogʻni koʻra olaman."),
     ],
     [G('flat', 'kvartira'), G('floor', 'qavat; pol'), G('building', 'bino'), G('often', 'tez-tez, koʻpincha'),
      G('broken', 'buzilgan, singan'), G('living room', 'mehmonxona (uydagi xona)'), G('carpet', 'gilam'),
      G('next to', 'yonida'), G('desk', 'yozuv stoli'), G('bookshelf', 'kitob javoni'), G('window', 'deraza')],
     [GN('b14-there-is', 'there is / there are', 'There is a bed, a desk and a bookshelf.'),
      GN('b16-prepositions-place', 'Joy predloglari: on, next to', 'My computer is on the desk.')],
     [
         tf('The family lives in a house.', 'F', 'Ular kvartirada yashaydi: «We live in a flat».', 0),
         ch('Which floor is the flat on?', ['the second', 'the fourth', 'the fifth'], 1, '«It is on the fourth floor.»', 0),
         tf('The lift always works.', 'F', 'Lift tez-tez buziladi: «it is often broken».', 0),
         ch('What is on the floor in the living room?', ['a carpet', 'a bed', 'a desk'], 0,
            '«a big carpet on the floor» — bu yerda floor = pol.', 1),
         tf("The grandmother's room is next to the bathroom.", 'F', 'Buvining xonasi oshxona yonida: «next to the kitchen».', 1),
         gap('The computer is on the ___.', 'desk', '«My computer is on the desk.»', 2),
         gap('From the window you can see a ___.', 'park', '«From my window I can see a park.»', 2),
     ])

text(B, 'a1-04-friend', 'Eng yaqin doʻstim', 'My Best Friend', 'A1', 'story', L('Doʻstlar', 'Friends'),
     'Aziz eng yaqin doʻsti Temur haqida yozadi. Oʻqishdan oldin: doʻstingiz qanday odam?',
     [
         P("My name is Aziz. My best friend is Timur. We are in the same class. Timur is tall and thin. He has short black hair and brown eyes. "
           "He always wears a blue cap.",
           "Mening ismim Aziz. Eng yaqin doʻstim — Temur. Biz bir sinfda oʻqiymiz. Temur baland boʻyli va ozgʻin. Uning sochi kalta va qora, "
           "koʻzlari jigarrang. U doim koʻk kepka kiyib yuradi."),
         P("Timur is very good at maths, but he isn't good at English. I help him with his English homework, "
           "and he helps me with maths.",
           "Temur matematikani juda yaxshi biladi, lekin ingliz tilini yaxshi bilmaydi. Men unga ingliz tili uy vazifasida "
           "yordam beraman, u esa menga matematikada yordam beradi."),
         P("After school, we often play football in the park. At the weekend, we sometimes go to the cinema. "
           "Timur likes action films, and I like comedies.",
           "Darsdan keyin biz tez-tez bogʻda futbol oʻynaymiz. Dam olish kunlari baʼzan kinoga boramiz. "
           "Temur jangari filmlarni yoqtiradi, men esa komediyalarni."),
     ],
     [G('best friend', 'eng yaqin doʻst'), G('same', 'bir xil; bitta'), G('tall', 'baland boʻyli'), G('thin', 'ozgʻin'),
      G('cap', 'kepka'), G('be good at', '… ni yaxshi bilmoq, … ga usta boʻlmoq'), G('homework', 'uy vazifasi'),
      G('at the weekend', 'dam olish kunlari'), G('sometimes', 'baʼzan'), G('action film', 'jangari film'),
      G('comedy', 'komediya')],
     [GN('b45-appearance', 'Tashqi koʻrinish: He has short black hair', 'He has short black hair and brown eyes.'),
      GN('b24-frequency', 'always, often, sometimes', 'We often play football in the park.')],
     [
         tf('Timur and Aziz are in the same class.', 'T', '«We are in the same class.»', 0),
         ch('What does Timur always wear?', ['a blue cap', 'a red T-shirt', 'glasses'], 0, '«He always wears a blue cap.»', 0),
         tf('Timur is good at English.', 'F', '«he isn\'t good at English» — ingliz tilini yaxshi bilmaydi.', 1),
         ch('Who helps Timur with his English homework?', ['his teacher', 'Aziz', 'his brother'], 1,
            '«My name is Aziz… I help him with his English homework» — yordam beradigan Aziz.', 1),
         tf('The boys often play football after school.', 'T', '«After school, we often play football in the park.»', 2),
         gap('At the weekend, the boys sometimes go to the ___.', 'cinema', '«we sometimes go to the cinema».', 2),
         ch('What films does Timur like?', ['comedies', 'cartoons', 'action films'], 2,
            'Temur — jangari filmlar; komediyalarni Aziz yoqtiradi.', 2),
     ])

text(B, 'a1-05-trip', 'Muzeyga sayohat', 'School Trip to the Museum', 'A1', 'notice', SCH,
     'Bu — maktabdagi eʼlon. Eʼlonlarda vaqt, joy va narx muhim. Oʻqiyotganda raqamlarga eʼtibor bering.',
     [
         P("School trip for Class 7B! On Friday, 14 March, we go to the History Museum in Tashkent.",
           "7B sinfi uchun maktab sayohati! 14-mart, juma kuni biz Toshkentdagi Tarix muzeyiga boramiz."),
         P("The bus leaves the school at 8:30 in the morning. Please come to school at 8:15. Don't be late! "
           "We come back at 3 o'clock.",
           "Avtobus maktabdan ertalab soat 8:30 da joʻnaydi. Iltimos, maktabga 8:15 da keling. Kechikmang! "
           "Soat 3 da qaytamiz."),
         P("The ticket costs 20,000 sum. Bring your lunch and a bottle of water. You can't eat in the museum, "
           "but there is a small park next to it.",
           "Chipta 20 000 soʻm turadi. Tushlik va bir shisha suv olib keling. Muzey ichida ovqatlanish mumkin emas, "
           "lekin uning yonida kichik bogʻ bor."),
         P("Please give this paper to your parents. They must sign it. Bring it back to Ms Karimova by Wednesday.",
           "Iltimos, bu qogʻozni ota-onangizga bering. Ular uni imzolashi kerak. Uni chorshanbagacha oʻqituvchi Karimovaga qaytaring."),
     ],
     [G('trip', 'sayohat, ekskursiya'), G('museum', 'muzey'), G('leave', 'joʻnab ketmoq'), G('late', 'kech; kechikkan'),
      G('come back', 'qaytib kelmoq'), G('cost', '(narxi) … turmoq'), G('bring', 'olib kelmoq'),
      G('bottle', 'shisha (idish)'), G('sign', 'imzolamoq'), G('parents', 'ota-ona'), G('by Wednesday', 'chorshanbagacha')],
     [GN('b20-telling-time', 'Vaqt: at 8:30, at 3 o\'clock', 'The bus leaves the school at 8:30.'),
      GN('b48-health', 'must — majburiyat', 'They must sign it.')],
     [
         ch('When is the trip?', ['on Wednesday', 'on Friday', 'on Monday'], 1, '«On Friday, 14 March». Chorshanba — qogʻozni qaytarish kuni.', 0),
         tf('Students must come to school at 8:30.', 'F', 'Kelish vaqti 8:15; 8:30 da avtobus joʻnaydi.', 1),
         tf('The class comes back at 3 o\'clock.', 'T', '«We come back at 3 o\'clock.»', 1),
         ch('How much is the ticket?', ['20,000 sum', '2,000 sum', 'It is free.'], 0, '«The ticket costs 20,000 sum.»', 2),
         tf('Students can eat their lunch in the museum.', 'F', '«You can\'t eat in the museum» — yonidagi bogʻda yeyish mumkin.', 2),
         ch('Who must sign the paper?', ['the teacher', "the students' parents", 'the museum'], 1,
            '«Please give this paper to your parents. They must sign it.»', 3),
         gap('Students give the paper back to Ms ___.', 'Karimova', '«Bring it back to Ms Karimova by Wednesday.»', 3),
     ])
