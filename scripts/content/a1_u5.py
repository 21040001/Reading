"""A1 · 5-boʻlim: Sayohat (5 ta matn)"""
from lib import *

B = 'a1'

text(B, 'a1-21-train', 'Samarqandga poyezdda', 'To Samarkand by Train', 'A1', 'story', L('Poyezd', 'Train'),
     'Dilshod va Kamola tezyurar poyezdda Samarqandga boradi. Oʻqishdan oldin: siz qachon poyezdda yurgansiz?',
     [
         P("It is Saturday morning. Dilshod and his sister Kamola are at the train station in Tashkent. "
           "They have two tickets for the Afrosiyob. It is a fast train.",
           "Shanba kuni ertalab. Dilshod va uning singlisi Kamola Toshkentdagi temir yoʻl vokzalida. "
           "Ularda «Afrosiyob»ga ikkita chipta bor. Bu — tezyurar poyezd."),
         P("The train leaves at eight o'clock. Their seats are next to a big window. The trip is about two hours. "
           "Kamola reads a book, and Dilshod looks at the fields and small villages.",
           "Poyezd soat sakkizda joʻnaydi. Ularning oʻrindiqlari katta derazaning yonida. Yoʻl taxminan ikki soat davom etadi. "
           "Kamola kitob oʻqiydi, Dilshod esa dalalar va kichik qishloqlarga qaraydi."),
         P("There is a small café on the train. Dilshod would like a cup of tea. "
           "Kamola would like some water and a sandwich.",
           "Poyezdda kichik kafe bor. Dilshod bir piyola choy ichmoqchi. "
           "Kamola esa suv va sendvich olmoqchi."),
         P("In Samarkand, their uncle Jahongir is at the station. He says, \"Welcome to Samarkand!\" "
           "Tomorrow they want to see the Registan.",
           "Samarqandda vokzalda ularni amakisi Jahongir kutib turibdi. U: «Samarqandga xush kelibsizlar!» — deydi. "
           "Ertaga ular Registonni koʻrmoqchi."),
     ],
     [G('train station', 'temir yoʻl vokzali'), G('ticket', 'chipta'), G('fast', 'tez, tezyurar'),
      G('leave', 'joʻnab ketmoq'), G('seat', 'oʻrindiq'), G('trip', 'safar, yoʻl'), G('about', 'taxminan'),
      G('field', 'dala'), G('village', 'qishloq'), G('would like', '… xohlamoq (xushmuomala)'),
      G('uncle', 'amaki, togʻa')],
     [GN('b20-telling-time', "Vaqt: at eight o'clock", "The train leaves at eight o'clock."),
      GN('b44-would-like', 'would like — xohlamoq', 'Dilshod would like a cup of tea.')],
     [
         tf('Dilshod and Kamola are at the station on Saturday morning.', 'T',
            '1-xatboshi: «It is Saturday morning… are at the train station».', 0),
         tf('The Afrosiyob is a slow train.', 'F', 'Bu tezyurar poyezd: «It is a fast train.»', 0),
         ch('When does the train leave?', ["at seven o'clock", "at eight o'clock", "at ten o'clock"], 1,
            "«The train leaves at eight o'clock.»", 1),
         ch('What does Kamola do on the train?', ['She reads a book.', 'She sleeps.', 'She plays a game.'], 0,
            '«Kamola reads a book» — dalalarga Dilshod qaraydi.', 1),
         gap('The trip is about two ___.', 'hours', '«The trip is about two hours.»', 1),
         ch('What would Dilshod like?', ['some water', 'a sandwich', 'a cup of tea'], 2,
            '«Dilshod would like a cup of tea.» Suv va sendvichni Kamola xohlaydi.', 2),
         tf('Their uncle Jahongir is at the station in Samarkand.', 'T',
            '«In Samarkand, their uncle Jahongir is at the station.»', 3),
     ])

text(B, 'a1-22-hotel', 'Mehmonxonada', 'At the Hotel', 'A1', 'dialogue', L('Mehmonxona', 'Hotel'),
     'Bu — mehmonxona qabulxonasidagi suhbat. Oʻqishdan oldin: mehmonxonaga kelganda qanday savollar berasiz?',
     [
         P("Receptionist: Good evening! Welcome to our hotel. Can I help you? "
           "Kamola: Good evening. My name is Kamola Rahimova. I have a room for two nights.",
           "Administrator: Xayrli kech! Mehmonxonamizga xush kelibsiz. Sizga yordam bera olamanmi? "
           "Kamola: Xayrli kech. Mening ismim Kamola Rahimova. Menga ikki kechaga xona band qilingan."),
         P("Receptionist: Yes, Ms Rahimova. Your room is 205. It is on the second floor. Here is your key.",
           "Administrator: Ha, Rahimova xonim. Sizning xonangiz — 205. U ikkinchi qavatda. Mana kalitingiz."),
         P("Kamola: Thank you. Is there a lift? Receptionist: Yes, there is. It is next to the stairs.",
           "Kamola: Rahmat. Lift bormi? Administrator: Ha, bor. U zinapoyaning yonida."),
         P("Kamola: What time is breakfast? Receptionist: Breakfast is from seven to ten in the restaurant.",
           "Kamola: Nonushta soat nechada? Administrator: Nonushta restoranda soat yettidan oʻngacha."),
         P("Kamola: Can I use the wifi? Receptionist: Yes, of course. The password is on this card. "
           "Have a nice evening!",
           "Kamola: Wi-Fiʼdan foydalansam boʻladimi? Administrator: Ha, albatta. Parol mana shu kartochkada. "
           "Kechingiz xayrli oʻtsin!"),
     ],
     [G('receptionist', 'administrator (qabulxonada)'), G('welcome', 'xush kelibsiz'), G('night', 'kecha, tun'),
      G('floor', 'qavat'), G('key', 'kalit'), G('lift', 'lift'), G('stairs', 'zinapoya'),
      G('breakfast', 'nonushta'), G('password', 'parol'), G('of course', 'albatta')],
     [GN('b17-short-answers', 'Qisqa javoblar: Yes, there is.', 'Yes, there is.'),
      GN('b29-can', 'Can I …? — ruxsat soʻrash', 'Can I use the wifi?')],
     [
         tf('Kamola has a room for two nights.', 'T', '«I have a room for two nights.»', 0),
         ch('Which floor is the room on?', ['the first', 'the second', 'the third'], 1,
            '«It is on the second floor.»', 1),
         gap('Kamola\'s room number is ___.', '205', '«Your room is 205.»', 1),
         tf('There is no lift in the hotel.', 'F', 'Lift bor: «Yes, there is. It is next to the stairs.»', 2),
         ch('Where is the lift?', ['next to the restaurant', 'next to the stairs', 'next to room 205'], 1,
            '«It is next to the stairs.»', 2),
         ch('When is breakfast?', ['from six to nine', 'from seven to ten', 'from eight to eleven'], 1,
            '«Breakfast is from seven to ten in the restaurant.»', 3),
         gap('The wifi password is on a ___.', 'card', '«The password is on this card.»', 4),
     ])

text(B, 'a1-23-charvak', 'Chorvoq boʻyida', 'At Charvak Lake', 'A1', 'blog', L('Tabiat', 'Nature'),
     'Jahongir blogida Chorvoqdagi dam olish haqida yozadi. Oʻqishdan oldin: siz dam olish kunlari qayerga borishni yoqtirasiz?',
     [
         P("Hi, everyone! This weekend my family and I are at Charvak. It is a big lake in the mountains near Tashkent. "
           "The water is blue and very clean.",
           "Hammaga salom! Bu dam olish kunlari men oilam bilan Chorvoqdaman. Bu — Toshkent yaqinidagi togʻlarda joylashgan katta koʻl. "
           "Suvi moviy va juda toza."),
         P("Today the weather is sunny and hot. My little brother is swimming now, and my father is sitting in the shade. "
           "My mother is making tea.",
           "Bugun havo quyoshli va issiq. Ukam hozir suzyapti, otam esa soyada oʻtiribdi. "
           "Onam choy damlayapti."),
         P("There are a lot of hotels and small cafés here. In summer, many people come from Tashkent. "
           "You can swim, ride a boat or walk in the mountains.",
           "Bu yerda koʻplab mehmonxonalar va kichik kafelar bor. Yozda Toshkentdan koʻp odamlar keladi. "
           "Bu yerda suzish, qayiqda sayr qilish yoki togʻlarda piyoda sayr qilish mumkin."),
         P("In the evening it is cool, so I wear a jacket. I love Charvak! I would like to come here again next summer.",
           "Kechqurun salqin boʻladi, shuning uchun kurtka kiyaman. Men Chorvoqni yaxshi koʻraman! "
           "Kelasi yozda bu yerga yana kelishni xohlayman."),
     ],
     [G('lake', 'koʻl'), G('mountain', 'togʻ'), G('near', 'yaqinida'), G('clean', 'toza'),
      G('sunny', 'quyoshli'), G('swim', 'suzmoq'), G('shade', 'soya'), G('ride a boat', 'qayiqda sayr qilmoq'),
      G('cool', 'salqin'), G('jacket', 'kurtka'), G('again', 'yana')],
     [GN('b36-weather-vocab', 'Ob-havo: sunny, hot, cool', 'Today the weather is sunny and hot.'),
      GN('b29-can', 'can — mumkinlik', 'You can swim, ride a boat or walk in the mountains.')],
     [
         tf('Charvak is a big lake in the mountains.', 'T', '«It is a big lake in the mountains near Tashkent.»', 0),
         tf('The water in the lake is dirty.', 'F', 'Suv toza: «The water is blue and very clean.»', 0),
         ch('What is the weather like today?', ['cold and rainy', 'sunny and hot', 'cloudy and cool'], 1,
            '«Today the weather is sunny and hot.»', 1),
         ch('Who is swimming now?', ['his father', 'his mother', 'his little brother'], 2,
            '«My little brother is swimming now».', 1),
         gap('His father is sitting in the ___.', 'shade', '«my father is sitting in the shade».', 1),
         tf('You can ride a boat at Charvak.', 'T', '«You can swim, ride a boat or walk in the mountains.»', 2),
         ch('Why does Jahongir wear a jacket in the evening?', ['It is cool.', 'It is rainy.', 'It is hot.'], 0,
            '«In the evening it is cool, so I wear a jacket.»', 3),
     ])

text(B, 'a1-24-letter', 'Doʻstimga xat', 'A Letter to My Friend', 'A1', 'email', L('Xat', 'Letter'),
     'Kamola Xivadan dugonasi Layloga xat yozadi. Oʻqishdan oldin: siz Xiva haqida nimalarni bilasiz?',
     [
         P("Dear Laylo, how are you? I am in Khiva with my parents! I am sitting in a small café now, and I am writing to you.",
           "Qadrli Laylo, qalaysan? Men ota-onam bilan Xivadaman! Hozir kichkina kafeda oʻtiribman va senga xat yozyapman."),
         P("Khiva is an old city. There are high walls around the old part of the city. "
           "Inside, there are mosques, madrasas and a lot of little shops.",
           "Xiva — qadimiy shahar. Shaharning eski qismi atrofida baland devorlar bor. "
           "Ichkarida masjidlar, madrasalar va juda koʻp kichkina doʻkonlar bor."),
         P("The weather is very hot, so I wear a hat every day. The food is great. "
           "I like the green noodles here. They are called shivit oshi.",
           "Havo juda issiq, shuning uchun har kuni shlyapa kiyaman. Ovqatlar zoʻr. "
           "Menga bu yerdagi yashil ugra yoqadi. Uning nomi — shivit oshi."),
         P("We go home on Sunday. I would like to show you my photos. See you soon! Love, Kamola",
           "Biz yakshanba kuni uyga qaytamiz. Senga suratlarimni koʻrsatmoqchiman. Tez orada koʻrishguncha! Mehr bilan, Kamola"),
     ],
     [G('dear', 'qadrli, aziz (xat boshida)'), G('parents', 'ota-ona'), G('wall', 'devor'),
      G('around', 'atrofida'), G('mosque', 'masjid'), G('inside', 'ichkarida'), G('hat', 'shlyapa, qalpoq'),
      G('noodles', 'ugra, lagʻmon'), G('show', 'koʻrsatmoq'), G('photo', 'surat'), G('See you soon!', 'Tez orada koʻrishguncha!')],
     [GN('b14-there-is', 'there is / there are', 'There are high walls around the old part of the city.'),
      GN('b44-would-like', 'would like to … — … ni xohlamoq', 'I would like to show you my photos.')],
     [
         tf('Kamola is in Khiva with her friends.', 'F', 'U ota-onasi bilan: «I am in Khiva with my parents!»', 0),
         ch('Where is Kamola now?', ['in a hotel room', 'in a small café', 'in a mosque'], 1,
            '«I am sitting in a small café now».', 0),
         gap('There are high ___ around the old part of the city.', 'walls',
            '«There are high walls around the old part of the city.»', 1),
         tf('There are a lot of little shops in the old city.', 'T',
            '«Inside, there are mosques, madrasas and a lot of little shops.»', 1),
         ch('Why does Kamola wear a hat?', ['It is very hot.', 'It is cold.', 'It is windy.'], 0,
            '«The weather is very hot, so I wear a hat every day.»', 2),
         gap('Kamola likes the green ___ in Khiva.', 'noodles', '«I like the green noodles here.»', 2),
         ch('When does the family go home?', ['on Friday', 'on Saturday', 'on Sunday'], 2,
            '«We go home on Sunday.»', 3),
     ])

text(B, 'a1-25-lost-bag', 'Yoʻqolgan sumka', 'Lost Bag', 'A1', 'notice', L('Eʼlon', 'Notice'),
     'Bu — bozordagi eʼlon. Oʻqishdan oldin: sumkangizda odatda nimalar boʻladi?',
     [
         P("LOST BAG. My name is Kamola, and I can't find my bag. I think it is at Chorsu Bazaar, near the bread stalls.",
           "SUMKA YOʻQOLDI. Mening ismim Kamola, men sumkamni topa olmayapman. "
           "Menimcha, u Chorsu bozorida, non rastalari yaqinida."),
         P("It is a small brown bag. There is a black phone, a blue notebook and my keys in it. There is no money in it.",
           "Bu — kichkina jigarrang sumka. Uning ichida qora telefon, koʻk daftar va kalitlarim bor. Ichida pul yoʻq."),
         P("The notebook is very important to me. My English homework and my poems are in it.",
           "Daftar men uchun juda muhim. Unda ingliz tili uy vazifam va sheʼrlarim bor."),
         P("Can you help me? My phone is in the bag, so please call my brother Jahongir. His number is below. Thank you!",
           "Menga yordam bera olasizmi? Telefonim sumkada, shuning uchun iltimos, akam Jahongirga qoʻngʻiroq qiling. "
           "Uning raqami pastda. Rahmat!"),
     ],
     [G('lost', 'yoʻqolgan'), G('help', 'yordam bermoq'), G('near', 'yaqinida'), G('bread', 'non'),
      G('brown', 'jigarrang'), G('notebook', 'daftar'), G('key', 'kalit'), G('money', 'pul'),
      G('important', 'muhim'), G('poem', 'sheʼr'), G('below', 'pastda, quyida')],
     [GN('b14-there-is', 'there is / there is no', 'There is no money in it.'),
      GN('b29-can', 'Can you …? — iltimos', 'Can you help me?')],
     [
         ch('Where does Kamola think her bag is?', ['at the train station', 'at Chorsu Bazaar', 'at school'], 1,
            '«I think it is at Chorsu Bazaar, near the bread stalls.»', 0),
         ch('What colour is the bag?', ['black', 'blue', 'brown'], 2,
            '«It is a small brown bag.» Qora — telefon, koʻk — daftar.', 1),
         tf('There is a phone in the bag.', 'T', '«There is a black phone… in it.»', 1),
         tf('There is a lot of money in the bag.', 'F', 'Pul yoʻq: «There is no money in it.»', 1),
         gap('Her English homework and her ___ are in the notebook.', 'poems',
            '«My English homework and my poems are in it.»', 2),
         tf('The notebook is not important to Kamola.', 'F', 'Daftar muhim: «The notebook is very important to me.»', 2),
         ch('Who should people call?', ['Kamola', 'her brother Jahongir', 'the police'], 1,
            '«please call my brother Jahongir».', 3),
     ])
