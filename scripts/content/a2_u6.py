"""A2 · 6-boʻlim: Texnologiya (5 ta matn)"""
from lib import *

B = 'a2'
TECH = L('Texnologiya', 'Technology')

text(B, 'a2-26-phone-rules', 'Smartfon qoidalari', 'Phone Rules at School', 'A2', 'notice', TECH,
     'Bu — maktabning telefonlar haqidagi yangi qoidalari toʻgʻrisidagi eʼloni. Oʻqishdan oldin oʻylab koʻring: '
     'sizning maktabingizda darsda telefondan foydalanish mumkinmi?',
     [
         P("Notice for all students of School Number 21, Namangan. From 1 November, our school is going to have "
           "new phone rules. Please read them carefully and share them with your parents.",
           "Namangandagi 21-maktabning barcha oʻquvchilari uchun eʼlon. 1-noyabrdan boshlab maktabimizda telefonlar "
           "boʻyicha yangi qoidalar amal qiladi. Iltimos, ularni diqqat bilan oʻqing va ota-onangizga ham aytib bering."),
         P("During lessons, phones must be switched off and kept in your bags. You mustn't use your phone in the "
           "corridors or in the canteen either. If a teacher sees a phone in a lesson, he or she will take it to the "
           "office. Your parents will have to collect it.",
           "Dars paytida telefonlar oʻchirilgan va sumkangizda boʻlishi shart. Telefoningizdan yoʻlaklarda yoki "
           "oshxonada ham foydalanmasligingiz kerak. Agar oʻqituvchi darsda telefonni koʻrsa, uni idoraga olib ketadi. "
           "Uni ota-onangiz kelib olib ketishi kerak boʻladi."),
         P("You can use your phone before 8:00 and after the last lesson. In an emergency, you can call home from "
           "the school office at any time. You needn't bring a phone to school at all if you don't need one.",
           "Telefoningizdan soat 8:00 gacha va oxirgi darsdan keyin foydalanishingiz mumkin. Favqulodda holatda istalgan "
           "vaqtda maktab idorasidan uyga qoʻngʻiroq qilishingiz mumkin. Agar telefon kerak boʻlmasa, uni maktabga "
           "umuman olib kelmasangiz ham boʻladi."),
         P("Why have we made these rules? Many students have told us that they can't stop checking messages. Some "
           "have become more tired and less active at break. We want breaks to be fun and friendly again, with more "
           "games and real conversations.",
           "Nega bu qoidalarni joriy qildik? Koʻplab oʻquvchilar bizga xabarlarni tekshirishni toʻxtata olmasliklarini "
           "aytishdi. Baʼzilari tanaffusda koʻproq charchaydigan va kamroq harakat qiladigan boʻlib qolgan. Biz "
           "tanaffuslar yana qiziqarli va samimiy, koʻproq oʻyinlar va jonli suhbatlar bilan oʻtishini xohlaymiz."),
         P("Phones are useful, of course. In IT lessons, your teacher might ask you to use one for a project. Then it "
           "will be allowed. Any questions? Talk to Mr Yusupov in Room 14.",
           "Albatta, telefonlar foydali. Informatika darslarida oʻqituvchingiz loyiha uchun telefondan foydalanishni "
           "soʻrashi mumkin. Unda bunga ruxsat beriladi. Savollaringiz bormi? 14-xonadagi Yusupov domlaga murojaat qiling."),
     ],
     [G('notice', 'eʼlon'), G('rule', 'qoida'), G('carefully', 'diqqat bilan'), G('switch off', 'oʻchirmoq'),
      G('corridor', 'yoʻlak, koridor'), G('canteen', 'oshxona (maktab, ishxonada)'), G('collect', 'olib ketmoq; yigʻmoq'),
      G('emergency', 'favqulodda holat'), G('check messages', 'xabarlarni tekshirmoq'), G('tired', 'charchagan'),
      G('break', 'tanaffus'), G('allowed', 'ruxsat etilgan')],
     [GN('e27-must-mustnt-neednt', 'must / mustn\'t / needn\'t', 'You mustn\'t use your phone in the corridors'),
      GN('e54-when-if', 'Birinchi shart gap: If … will', 'If a teacher sees a phone in a lesson, he or she will take it to the office.')],
     [
         tf('The new rules start in November.', 'T', '«From 1 November, our school is going to have new phone rules.»', 0),
         tf('Students can use their phones in the canteen.', 'F',
            'Oshxonada ham mumkin emas: «You mustn\'t use your phone in the corridors or in the canteen either.»', 1),
         ch('What happens if a teacher sees a phone in a lesson?',
            ['The student must leave the lesson.', 'The teacher takes it to the office.', 'The teacher calls the student\'s parents in the lesson.'], 1,
            '«he or she will take it to the office» — telefon idoraga olib ketiladi.', 1),
         tf('Parents have to come to school to get the phone back.', 'T',
            '«Your parents will have to collect it.» — telefonni ota-ona olib ketadi.', 1),
         ch('In an emergency, a student can …',
            ['use their own phone in the lesson', 'call home from the school office', 'go home without asking'], 1,
            '«In an emergency, you can call home from the school office at any time.»', 2),
         gap('Students needn\'t bring a ___ to school if they don\'t need one.', 'phone',
             '«You needn\'t bring a phone to school at all if you don\'t need one.»', 2),
         ch('Why has the school made the new rules?',
            ['Phones are too expensive for many families.', 'Students check messages too much and are less active.',
             'Parents asked the school to make them.'], 1,
            '«they can\'t stop checking messages… more tired and less active at break» — sabab shu.', 3),
         gap('Students with questions should go to Room ___.', ['14', 'fourteen'], '«Talk to Mr Yusupov in Room 14.»', 4),
     ])

text(B, 'a2-27-online-shopping', 'Onlayn xarid', 'Shopping Online', 'A2', 'email', TECH,
     'Kamola amakivachchasiga birinchi onlayn xaridi haqida xat yozadi. Oʻqishdan oldin: siz internet orqali '
     'biror narsa sotib olganmisiz?',
     [
         P("Hi Shahnoza, how are you? I have some news. Last week I bought a jacket online for the first time! I used a "
           "shopping app on my phone. It was easier than I thought.",
           "Salom, Shahnoza, qalaysan? Bir yangilik bor. Oʻtgan hafta birinchi marta internet orqali kurtka sotib oldim! "
           "Telefonimdagi xarid ilovasidan foydalandim. Bu men oʻylagandan osonroq boʻldi."),
         P("In the app, you can see thousands of clothes, and the prices are often lower than in the shops in "
           "Samarkand. I found a warm green jacket for 280,000 sum. At the market, the same jacket costs 350,000. "
           "The delivery took only three days, and the courier brought it to our door.",
           "Ilovada minglab kiyimlarni koʻrish mumkin, narxlar esa koʻpincha Samarqanddagi doʻkonlardagidan arzonroq. "
           "Men 280 000 soʻmga issiq yashil kurtka topdim. Bozorda xuddi shu kurtka 350 000 soʻm turadi. Yetkazib berish "
           "atigi uch kun oldi, kuryer uni eshigimizgacha olib keldi."),
         P("But not everything was perfect. The jacket in the photo looked darker. Also, my brother has had a bad "
           "experience. He paid for headphones on an unknown website, and they never arrived. He has lost his money.",
           "Lekin hammasi ham mukammal emas edi. Rasmdagi kurtka toʻqroq koʻringan edi. Bundan tashqari, akamning yomon "
           "tajribasi boʻlgan. U notanish bir saytda quloqchinlar uchun pul toʻlagan, ular esa hech qachon kelmadi. "
           "U pulidan ayrildi."),
         P("So here are my tips. Only use apps or sites that you know well. Read the comments from other buyers. "
           "Never send your card number or SMS codes in a message. If something is much cheaper than everywhere else, "
           "it might be a trick.",
           "Xullas, mana mening maslahatlarim. Faqat yaxshi biladigan ilova yoki saytlardan foydalan. Boshqa xaridorlarning "
           "izohlarini oʻqi. Hech qachon karta raqamingni yoki SMS-kodlarni xabarda yuborma. Agar biror narsa boshqa joylardagidan ancha arzon "
           "boʻlsa, bu aldov boʻlishi mumkin."),
         P("Are you going to try online shopping? Write back soon! Love, Kamola",
           "Sen ham onlayn xarid qilib koʻrmoqchimisan? Tezroq javob yoz! Mehr bilan, Kamola"),
     ],
     [G('online', 'internet orqali, onlayn'), G('app', 'ilova (dastur)'), G('price', 'narx'), G('lower', 'pastroq, arzonroq'),
      G('delivery', 'yetkazib berish'), G('courier', 'kuryer'), G('perfect', 'mukammal, benuqson'),
      G('experience', 'tajriba'), G('headphones', 'quloqchinlar'), G('arrive', 'yetib kelmoq'),
      G('buyer', 'xaridor'), G('trick', 'aldov, hiyla')],
     [GN('e45-comparatives', 'Qiyosiy daraja: lower than, easier than', 'the prices are often lower than in the shops'),
      GN('e13-present-perfect', 'Present Perfect: has lost', 'He has lost his money.')],
     [
         tf('Kamola bought her jacket in a shop in Samarkand.', 'F',
            'U kurtkani ilova orqali olgan: «I used a shopping app on my phone.»', 0),
         ch('How much did Kamola pay for the jacket?', ['350,000 sum', '280,000 sum', '300,000 sum'], 1,
            '«I found a warm green jacket for 280,000 sum.» 350 000 — bozordagi narx.', 1),
         gap('The jacket arrived after ___ days.', ['three', '3'], '«The delivery took only three days».', 1),
         tf('The jacket looked exactly the same as in the photo.', 'F', '«The jacket in the photo looked darker.»', 2),
         ch('What happened to Kamola\'s brother?',
            ['His headphones never arrived.', 'He got the wrong headphones.', 'He got his money back.'], 0,
            '«they never arrived. He has lost his money.»', 2),
         tf('Kamola thinks it is safe to send your card number in a message.', 'F',
            '«Never send your card number or SMS codes in a message.»', 3),
         ch('According to Kamola, a very cheap price …', ['is always a good chance', 'might be a trick', 'means the item is old'], 1,
            '«If something is much cheaper than everywhere else, it might be a trick.»', 3),
         gap('Read the comments from other ___.', 'buyers', '«Read the comments from other buyers.»', 3),
     ])

text(B, 'a2-28-robot-vacuum', 'Robot-changyutgich', 'The Robot Vacuum', 'A2', 'story', TECH,
     'Farruxning oilasi uyga robot-changyutgich olib keladi. Buvisi esa unga ishonmaydi. Oʻqishdan oldin: '
     'sizningcha, robotlar uy ishlarini odamlardan yaxshiroq bajara oladimi?',
     [
         P("Last month, Farrukh's family in Jizzakh bought a robot vacuum cleaner. It is round and flat, and it "
           "moves around the house by itself. Farrukh's little sister Zarina called it Pishak, because it is grey "
           "like a cat.",
           "Oʻtgan oy Jizzaxdagi Farruxning oilasi robot-changyutgich sotib oldi. U yumaloq va yassi boʻlib, uy boʻylab "
           "oʻzi harakatlanadi. Farruxning singlisi Zarina unga Pishak deb ism qoʻydi, chunki u mushukka oʻxshab kulrang."),
         P('At first, Grandma didn\'t trust the robot. "This machine will never clean better than me," she said. '
           'But every morning at nine, the robot cleaned the floors while the family were at work and school. When '
           'it finished, it went back to its charger.',
           "Avvaliga buvi robotga ishonmadi. «Bu mashina hech qachon mendan yaxshiroq tozalay olmaydi», dedi u. "
           "Lekin har kuni ertalab soat toʻqqizda, oila ishda va maktabda boʻlganida, robot pollarni tozalardi. "
           "Ishini tugatgach, quvvatlagichiga qaytib borardi."),
         P("There have been some problems too. One day, the robot ate one of Zarina's socks and stopped. Another "
           "time, it got stuck under the sofa for two hours. And it can't go up the stairs to the bedrooms.",
           "Baʼzi muammolar ham boʻldi. Bir kuni robot Zarinaning paypogʻini yutib yubordi va toʻxtab qoldi. Yana bir "
           "safar u ikki soat divan tagida tiqilib qoldi. Bundan tashqari, u zinadan yotoq xonalariga chiqa olmaydi."),
         P('Now Grandma likes Pishak more than anyone expected. She has learned to start it with the app on her '
           'phone. "It is quieter than the old vacuum cleaner," she says, "and I have more time for my garden." But '
           'she still cleans the corners herself, because the robot misses them.',
           "Endi buvi Pishakni hech kim kutmaganidan ham koʻproq yaxshi koʻradi. U telefonidagi ilova orqali uni ishga "
           "tushirishni oʻrganib oldi. «U eski changyutgichdan jimroq, — deydi u, — tomorqamga ham koʻproq vaqtim qoladi». "
           "Lekin burchaklarni hali ham oʻzi tozalaydi, chunki robot ularni tozalamay oʻtib ketadi."),
     ],
     [G('vacuum cleaner', 'changyutgich'), G('round', 'yumaloq'), G('flat', 'yassi'), G('by itself', 'oʻzi, mustaqil'),
      G('trust', 'ishonmoq'), G('charger', 'quvvatlagich'), G('stuck', 'tiqilib qolgan (get stuck — tiqilib qolmoq)'), G('stairs', 'zina'),
      G('expect', 'kutmoq (umid qilmoq)'), G('quiet', 'jim, shovqinsiz'), G('corner', 'burchak'),
      G('miss', 'oʻtkazib yubormoq')],
     [GN('e23-will', 'will — kelajak haqida fikr', 'This machine will never clean better than me.'),
      GN('e45-comparatives', 'Qiyosiy daraja: quieter than', 'It is quieter than the old vacuum cleaner')],
     [
         tf('The robot is called Pishak because it is grey like a cat.', 'T', '«called it Pishak, because it is grey like a cat».', 0),
         ch('Who gave the robot its name?', ['Farrukh', 'Zarina', 'Grandma'], 1,
            '«Farrukh\'s little sister Zarina called it Pishak».', 0),
         tf('At first, Grandma liked the robot very much.', 'F', '«At first, Grandma didn\'t trust the robot.»', 1),
         gap('Every morning at ___, the robot cleaned the floors.', ['nine', '9'], '«every morning at nine, the robot cleaned the floors».', 1),
         ch('Why did the robot stop one day?', ['Its battery was empty.', 'It ate a sock.', 'Grandma switched it off.'], 1,
            '«the robot ate one of Zarina\'s socks and stopped».', 2),
         tf('The robot can clean the bedrooms upstairs.', 'F',
            '«it can\'t go up the stairs to the bedrooms» — yuqoridagi yotoq xonalariga chiqa olmaydi.', 2),
         ch('What does Grandma do with her free time now?', ['She watches TV.', 'She works in her garden.', 'She cooks plov.'], 1,
            '«I have more time for my garden» — boʻsh vaqtini tomorqaga sarflaydi.', 3),
         ch('Why does Grandma still clean the corners?', ['She doesn\'t understand the app.', 'The robot misses them.', 'The robot is too loud.'], 1,
            '«because the robot misses them».', 3),
     ])

text(B, 'a2-29-social-media', 'Ijtimoiy tarmoqlar', 'A Week Without Social Networks', 'A2', 'blog', TECH,
     'Diyor bir hafta ijtimoiy tarmoqlarsiz yashab koʻrdi va bu haqda blog yozdi. Oʻqishdan oldin: '
     'siz kuniga ijtimoiy tarmoqlarda qancha vaqt oʻtkazasiz?',
     [
         P("Hi, I'm Diyor. I'm sixteen and I live in Karshi. Last month I checked how much time I spend on social "
           "networks. The answer was four hours a day! So I decided to try a week without them.",
           "Salom, men Diyorman. Oʻn olti yoshdaman va Qarshida yashayman. Oʻtgan oy ijtimoiy tarmoqlarda qancha vaqt "
           "oʻtkazishimni tekshirib koʻrdim. Javob — kuniga toʻrt soat! Shuning uchun bir hafta ularsiz yashab koʻrishga qaror qildim."),
         P("The first two days were difficult. I wanted to check my phone every five minutes. I was worried that I "
           "might miss something important. But by Wednesday, I felt calmer. I slept better and finished a book for "
           "the first time in a year.",
           "Dastlabki ikki kun qiyin boʻldi. Har besh daqiqada telefonimni tekshirgim kelardi. Biror muhim narsani "
           "oʻtkazib yuborishim mumkinligidan xavotirlanardim. Lekin chorshanbaga kelib oʻzimni xotirjamroq his qildim. "
           "Yaxshiroq uxladim va bir yil ichida birinchi marta kitobni oxirigacha oʻqidim."),
         P("Of course, social networks have good sides too. My cousin studies in Tashkent, and we chat every day. "
           "I have learned a lot of English from videos. My older sister sells her handmade bags online.",
           "Albatta, ijtimoiy tarmoqlarning yaxshi tomonlari ham bor. Amakivachcham Toshkentda oʻqiydi, biz har kuni "
           "yozishamiz. Videolardan koʻp inglizcha soʻz va iboralarni oʻrgandim. Opam esa qoʻlda tikkan sumkalarini "
           "internet orqali sotadi."),
         P("But there are dangers. Some people use fake names, and some posts are not true. My advice is simple: "
           "don't share your address or the name of your school with strangers, and use a strong password. If someone "
           "is unkind to you online, tell an adult you trust.",
           "Lekin xavflar ham bor. Baʼzi odamlar soxta ismlardan foydalanadi, baʼzi postlar esa haqiqat emas. "
           "Maslahatim oddiy: manzilingizni yoki maktabingiz nomini notanish odamlarga aytmang va kuchli paroldan "
           "foydalaning. Agar kimdir internetda sizga yomon munosabatda boʻlsa, oʻzingiz ishonadigan kattalarga ayting."),
         P("I'm going to keep using social networks, but only for one hour a day. Will it be easy? Probably not. "
           "I'll tell you next month!",
           "Men ijtimoiy tarmoqlardan foydalanishda davom etaman, lekin kuniga faqat bir soat. Bu oson boʻladimi? "
           "Ehtimol, yoʻq. Keyingi oy sizlarga aytib beraman!"),
     ],
     [G('social network', 'ijtimoiy tarmoq'), G('decide', 'qaror qilmoq'), G('be worried', 'xavotirlanmoq'),
      G('calm', 'xotirjam, tinch'), G('chat', 'yozishmoq, suhbatlashmoq'), G('handmade', 'qoʻlda yasalgan'),
      G('danger', 'xavf'), G('fake', 'soxta'), G('post', 'post, eʼlon qilingan yozuv'), G('stranger', 'notanish odam'),
      G('password', 'parol'), G('unkind', 'qoʻpol, mehrsiz')],
     [GN('e25-might-may', 'might — ehtimol', 'I was worried that I might miss something important.'),
      GN('e22-going-to', 'going to — reja', 'I\'m going to keep using social networks')],
     [
         tf('Before his experiment, Diyor spent four hours a day on social networks.', 'T',
            '«The answer was four hours a day!»', 0),
         tf('The first days without social networks were easy for Diyor.', 'F', '«The first two days were difficult.»', 1),
         ch('What changed by Wednesday?', ['He felt calmer and slept better.', 'He bought a new phone.', 'He started a new blog.'], 0,
            '«by Wednesday, I felt calmer. I slept better…»', 1),
         gap('Diyor finished a ___ for the first time in a year.', 'book', '«finished a book for the first time in a year».', 1),
         ch('How does Diyor\'s sister use the internet?', ['She teaches English.', 'She sells handmade bags.', 'She studies in Tashkent.'], 1,
            '«My older sister sells her handmade bags online.» Toshkentda esa amakivachchasi oʻqiydi.', 2),
         tf('Diyor thinks that everything on social networks is true.', 'F', '«some posts are not true».', 3),
         ch('If someone is unkind to you online, Diyor says you should …',
            ['answer them in the same way', 'tell an adult you trust', 'give them your password'], 1,
            '«If someone is unkind to you online, tell an adult you trust.»', 3),
         ch('What is Diyor\'s plan now?', ['to stop using social networks completely', 'to use them for one hour a day',
                                          'to use them only at the weekend'], 1,
            '«I\'m going to keep using social networks, but only for one hour a day.»', 4),
     ])

text(B, 'a2-30-future-city', 'Kelajak shahri', 'The City of the Future', 'A2', 'article', TECH,
     'Bu maqolada 2050-yildagi shaharlar qanday boʻlishi mumkinligi haqida soʻz boradi. Oʻqishdan oldin: '
     'sizningcha, 2050-yilga kelib shahringiz qanday oʻzgaradi?',
     [
         P("What will our cities look like in 2050? Engineers and students in Uzbekistan are already sharing their "
           "ideas. Here are some of them.",
           "2050-yilda shaharlarimiz qanday koʻrinishda boʻladi? Oʻzbekistondagi muhandislar va talabalar hozirdanoq "
           "oʻz gʻoyalari bilan oʻrtoqlashmoqda. Mana ulardan baʼzilari."),
         P("First, transport will be cleaner. Most buses and cars will be electric, and some of them will drive "
           "themselves. Streets might be quieter than they are today. Small drones may deliver letters and medicine.",
           "Birinchidan, transport tozaroq boʻladi. Avtobus va mashinalarning aksariyati elektr bilan yuradi, ularning "
           "baʼzilari esa haydovchisiz harakatlanadi. Koʻchalar bugungidan jimroq boʻlishi mumkin. Kichik dronlar xat va "
           "dori-darmonlarni yetkazib berishi mumkin."),
         P("Second, buildings will be smarter. Houses will produce their own energy from the sun. This is good news "
           "for sunny cities like Termez and Bukhara. Lights and air conditioners will switch off when nobody is in "
           "the room. If we save energy, we will pay less for it.",
           "Ikkinchidan, binolar aqlliroq boʻladi. Uylar oʻz energiyasini quyoshdan ishlab chiqaradi. Bu Termiz va Buxoro "
           "kabi quyoshli shaharlar uchun yaxshi xabar. Xonada hech kim boʻlmasa, chiroqlar va konditsionerlar oʻchib "
           "qoladi. Agar energiyani tejasak, unga kamroq pul toʻlaymiz."),
         P("But a future city might have problems too. Robots may do many jobs, so some people will need to learn "
           "new skills. If everything is online, computer crime will be a bigger danger. Some older people might find "
           "the new technology difficult.",
           "Lekin kelajak shahrida muammolar ham boʻlishi mumkin. Koʻp ishlarni robotlar bajarishi mumkin, shuning uchun "
           "baʼzi odamlar yangi koʻnikmalarni oʻrganishiga toʻgʻri keladi. Agar hamma narsa internetda boʻlsa, kompyuter "
           "jinoyatlari kattaroq xavfga aylanadi. Baʼzi keksa odamlarga yangi texnologiyalar qiyin boʻlishi mumkin."),
         P('Nodira Rashidova, a young architect from Tashkent, says: "The future city must be green, not only smart. '
           'We need more parks, more trees and more places to walk."',
           "Toshkentlik yosh meʼmor Nodira Rashidova shunday deydi: «Kelajak shahri faqat aqlli emas, balki yashil ham "
           "boʻlishi kerak. Bizga koʻproq bogʻlar, koʻproq daraxtlar va sayr qilish uchun koʻproq joylar kerak»."),
     ],
     [G('engineer', 'muhandis'), G('electric', 'elektr bilan ishlaydigan'), G('drone', 'dron, uchuvchisiz apparat'),
      G('deliver', 'yetkazib bermoq'), G('medicine', 'dori'), G('produce', 'ishlab chiqarmoq'), G('energy', 'energiya, quvvat'),
      G('air conditioner', 'konditsioner'), G('save', 'tejamoq'), G('skill', 'koʻnikma, mahorat'),
      G('crime', 'jinoyat'), G('architect', 'meʼmor, arxitektor')],
     [GN('e23-will', 'will — kelajak haqida bashorat', 'Most buses and cars will be electric'),
      GN('e54-when-if', 'Birinchi shart gap: If … will', 'If we save energy, we will pay less for it.')],
     [
         tf('The article says most cars in 2050 will be electric.', 'T', '«Most buses and cars will be electric».', 1),
         ch('What might drones do in the future?', ['build houses', 'deliver letters and medicine', 'clean the streets'], 1,
            '«Small drones may deliver letters and medicine.»', 1),
         gap('Houses will produce their own energy from the ___.', 'sun', '«Houses will produce their own energy from the sun.»', 2),
         ch('Why does the article mention Termez and Bukhara?', ['They are very sunny.', 'They have many robots.', 'They are the biggest cities.'], 0,
            '«good news for sunny cities like Termez and Bukhara» — ular quyoshli shaharlar.', 2),
         tf('In future buildings, lights will stay on when the room is empty.', 'F',
            '«Lights and air conditioners will switch off when nobody is in the room.»', 2),
         ch('Why will some people need to learn new skills?', ['Because schools will close.', 'Because robots may do many jobs.',
                                                               'Because cars will drive themselves.'], 1,
            '«Robots may do many jobs, so some people will need to learn new skills.»', 3),
         tf('The article says the new technology will be easy for everybody.', 'F',
            '«Some older people might find the new technology difficult.»', 3),
         gap('Nodira Rashidova is a young ___ from Tashkent.', 'architect', '«Nodira Rashidova, a young architect from Tashkent».', 4),
     ])
