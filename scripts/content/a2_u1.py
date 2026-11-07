"""A2 · 1-boʻlim: Odatlar va oʻzgarishlar (5 ta matn)"""
from lib import *

B = 'a2'
CHG = L('Oʻzgarishlar', 'Changes')

text(B, 'a2-01-then-now', 'Ilgari va hozir', 'Then and Now', 'A2', 'blog', CHG,
     'Sardor blogida bolaligi va hozirgi hayotini solishtiradi. Oʻqishdan oldin: siz bolaligingizdan beri qanday oʻzgardingiz?',
     [
         P("Hi, I'm Sardor, and I'm twenty-two. Today I looked at some old photos from my childhood in Namangan, "
           "and I laughed a lot. I have changed so much! So in this post I want to write about my life then and now.",
           "Salom, men Sardorman, yigirma ikki yoshdaman. Bugun Namangandagi bolaligimdan qolgan eski suratlarni koʻrib, "
           "rosa kuldim. Men juda oʻzgarib ketibman! Shuning uchun bu postda ilgarigi va hozirgi hayotim haqida yozmoqchiman."),
         P("When I was ten, I used to be very shy. I didn't use to talk to new people, and I always stood behind my "
           "mother at weddings. Now I work at a hotel in Samarkand, and I talk to guests from different countries every day.",
           "Oʻn yoshligimda men juda uyatchan edim. Yangi odamlar bilan gaplashmasdim, toʻylarda doim onamning orqasida "
           "turardim. Hozir Samarqanddagi mehmonxonada ishlayman va har kuni turli mamlakatlardan kelgan mehmonlar bilan gaplashaman."),
         P("I also used to hate vegetables. My grandmother cooked delicious soup with carrots and pumpkin, but I never "
           "ate it. Now soup is my favourite food, and I cook it myself on Sundays.",
           "Bundan tashqari, ilgari sabzavotlarni yomon koʻrardim. Buvim sabzi va qovoq solib mazali shoʻrva pishirardi, "
           "lekin men uni hech qachon yemasdim. Hozir shoʻrva — sevimli taomim, yakshanba kunlari uni oʻzim pishiraman."),
         P("Some things are different now, but some things haven't changed. I still love football, and I still play "
           "with my old friends when I go back to Namangan. They are taller now, but we laugh like children.",
           "Baʼzi narsalar hozir boshqacha, lekin baʼzilari oʻzgarmagan. Men hamon futbolni yaxshi koʻraman va Namanganga "
           "qaytganimda eski doʻstlarim bilan hali ham oʻynayman. Endi ularning boʻyi ancha oʻsgan, lekin biz bolalardek kulamiz."),
         P("What about you? What did you use to do as a child? Write in the comments!",
           "Sizchi? Bolaligingizda nima qilardingiz? Izohlarda yozing!"),
     ],
     [G('childhood', 'bolalik'), G('shy', 'uyatchan'), G('wedding', 'toʻy'), G('guest', 'mehmon'),
      G('different', 'turli; boshqacha'), G('hate', 'yomon koʻrmoq'), G('pumpkin', 'qovoq'),
      G('myself', 'oʻzim'), G('still', 'hali ham, hamon'), G('comment', 'izoh, fikr')],
     [GN('e11-used-to', 'used to — ilgari qilardim', 'I used to be very shy.'),
      GN('e13-present-perfect', 'Present Perfect: I have changed', 'I have changed so much!')],
     [
         tf('Sardor looked at old photos from his childhood.', 'T',
            '1-xatboshi: «Today I looked at some old photos from my childhood».', 0),
         tf('As a child, Sardor liked talking to new people.', 'F',
            'U uyatchan boʻlgan: «I didn\'t use to talk to new people».', 1),
         ch('Where does Sardor work now?', ['at a school in Namangan', 'at a hotel in Samarkand', 'at a restaurant in Tashkent'], 1,
            '«Now I work at a hotel in Samarkand».', 1),
         ch('Why does Sardor talk to people from different countries now?',
            ['He works with hotel guests.', 'He studies languages at university.', 'He travels a lot.'], 0,
            'U mehmonxonada ishlaydi: «I talk to guests from different countries every day».', 1),
         tf("Sardor's grandmother made soup with carrots and pumpkin.", 'T',
            '«My grandmother cooked delicious soup with carrots and pumpkin».', 2),
         gap('Now Sardor cooks soup himself on ___.', 'Sundays', '«I cook it myself on Sundays».', 2),
         ch('What is true about Sardor and football?', ['He stopped playing it.', 'He still loves it.', 'He started playing it in Samarkand.'], 1,
            '«I still love football» — still = hali ham.', 3),
         gap('Sardor is ___ years old.', ['twenty-two', '22', 'twenty two'], '«I\'m twenty-two» — u 22 yoshda.', 0),
     ])

text(B, 'a2-02-morning-habits', 'Mening ertalabki odatlarim', 'My Morning Habits', 'A2', 'dialogue', L('Kundalik hayot', 'Daily life'),
     'Bu — Nilufar va sinfdoshi Bekzod oʻrtasidagi suhbat. Oʻqishdan oldin: siz ertalab birinchi boʻlib nima qilasiz?',
     [
         P("Nilufar: Bekzod, you always come to class first, and you never look tired. What time do you get up? "
           "Bekzod: I usually get up at half past five. Last year I used to sleep until seven, but I changed my habits.",
           "Nilufar: Bekzod, sen doim sinfga birinchi kelasan va hech qachon charchagan koʻrinmaysan. Soat nechada turasan? "
           "Bekzod: Odatda besh yarimda turaman. Oʻtgan yili yettigacha uxlardim, lekin odatlarimni oʻzgartirdim."),
         P("Nilufar: Half past five! That's really early. What do you do first? Bekzod: First I drink a glass of water. "
           "Then I go running in the park near our house for twenty minutes. My dad comes with me on Saturdays.",
           "Nilufar: Besh yarimda! Bu juda erta-ku. Birinchi nima qilasan? Bekzod: Avval bir stakan suv ichaman. "
           "Keyin uyimiz yaqinidagi bogʻda yigirma daqiqa yuguraman. Shanba kunlari dadam ham men bilan boradi."),
         P("Nilufar: And what do you have for breakfast? Bekzod: My mum makes tea, and we eat bread, eggs and some fruit "
           "together. I don't look at my phone at breakfast. I think breakfast is better without it.",
           "Nilufar: Nonushtaga nima yeysan? Bekzod: Oyim choy damlaydi, biz birga non, tuxum va biroz meva yeymiz. "
           "Nonushta paytida telefonimga qaramayman. Menimcha, nonushta telefonsiz yaxshiroq."),
         P("Nilufar: Why did you change your habits? Bekzod: Last year I was always late, and I felt tired in lessons. "
           "Our sports teacher told me to sleep earlier and move more in the morning. Now I go to bed at ten.",
           "Nilufar: Nega odatlaringni oʻzgartirding? Bekzod: Oʻtgan yili doim kechikardim va darslarda charchagan boʻlardim. "
           "Jismoniy tarbiya oʻqituvchimiz menga ertaroq uxlashni va ertalab koʻproq harakat qilishni maslahat berdi. "
           "Hozir soat oʻnda yotaman."),
         P("Nilufar: Is it difficult? Bekzod: It was difficult in the first week, but now it's easy. I feel healthier, "
           "and my marks are better too.",
           "Nilufar: Qiyinmi? Bekzod: Birinchi haftada qiyin edi, lekin hozir oson. Oʻzimni sogʻlomroq his qilyapman, "
           "baholarim ham yaxshilandi."),
         P("Nilufar: I think I'm going to try it next month! Bekzod: Great idea! We can run in the park together.",
           "Nilufar: Menimcha, kelasi oy men ham sinab koʻraman! Bekzod: Zoʻr fikr! Bogʻda birga yugurishimiz mumkin."),
     ],
     [G('usually', 'odatda'), G('habit', 'odat'), G('tired', 'charchagan'), G('early', 'erta'),
      G('glass', 'stakan'), G('breakfast', 'nonushta'), G('late', 'kechikkan, kech'), G('lesson', 'dars'),
      G('healthy', 'sogʻlom'), G('mark', 'baho'), G('difficult', 'qiyin')],
     [GN('e11-used-to', 'used to — ilgari qilardim', 'Last year I used to sleep until seven'),
      GN('e45-comparatives', 'Qiyosiy daraja: healthier, better', 'I feel healthier, and my marks are better too.')],
     [
         gap('Bekzod usually gets up at half past ___.', ['five', '5'], '«I usually get up at half past five».', 0),
         tf('Last year Bekzod got up later than he does now.', 'T',
            '«Last year I used to sleep until seven» — hozir esa besh yarimda turadi.', 0),
         ch('What does Bekzod do first in the morning?', ['He goes running.', 'He drinks a glass of water.', 'He makes tea.'], 1,
            '«First I drink a glass of water. Then I go running».', 1),
         tf('Bekzod runs in the park with his dad every day.', 'F',
            'Dadasi faqat shanba kunlari boradi: «My dad comes with me on Saturdays».', 1),
         ch('Who makes tea in the morning?', ['Bekzod', 'his dad', 'his mum'], 2, '«My mum makes tea».', 2),
         tf('Bekzod looks at his phone at breakfast.', 'F', '«I don\'t look at my phone at breakfast».', 2),
         ch('Why did Bekzod change his habits?',
            ['He was often late and tired.', 'His mum asked him.', 'He wanted to win a race.'], 0,
            '«Last year I was always late, and I felt tired in lessons».', 3),
         gap('Now Bekzod goes to bed at ___.', ['ten', '10'], '«Now I go to bed at ten».', 3),
     ])

text(B, 'a2-03-no-phone', 'Telefonsiz bir hafta', 'A Week Without a Phone', 'A2', 'story', L('Texnologiya', 'Technology'),
     'Madina bir hafta telefonsiz yashab koʻradi. Oʻqishdan oldin: siz bir kun telefonsiz yasha olasizmi?',
     [
         P("Last month, our English teacher gave us a strange task: live for one week without a phone. Most students in "
           "my class laughed, but I decided to try. My name is Madina, and I am sixteen. Before that week, I spent about "
           "five hours a day on my phone.",
           "Oʻtgan oy ingliz tili oʻqituvchimiz bizga gʻalati topshiriq berdi: bir hafta telefonsiz yashash. Sinfimizdagi "
           "koʻp oʻquvchilar kulishdi, lekin men sinab koʻrishga qaror qildim. Mening ismim Madina, oʻn olti yoshdaman. "
           "Oʻsha haftagacha kuniga taxminan besh soatni telefonda oʻtkazardim."),
         P("The first two days were terrible. I didn't know the time, so I was late for school on Monday. In the evenings "
           "I felt bored and lonely. I wanted to check my messages every ten minutes.",
           "Dastlabki ikki kun dahshatli oʻtdi. Soat nechaligini bilmadim, shuning uchun dushanba kuni maktabga kechikdim. "
           "Kechqurunlari zerikdim va oʻzimni yolgʻiz his qildim. Har oʻn daqiqada xabarlarimni tekshirgim kelardi."),
         P("On Wednesday, things got better. I found an old book on my sister's shelf and read it in two days. I also "
           "helped my grandmother in the garden, and she told me funny stories about her school years. I have never "
           "laughed so much with her!",
           "Chorshanba kuni ishlar yaxshilandi. Opamning javonidan eski bir kitob topib, uni ikki kunda oʻqib chiqdim. "
           "Bogʻda buvimga ham yordam berdim, u menga maktab yillari haqida kulgili voqealarni aytib berdi. "
           "U bilan hech qachon bunchalik koʻp kulmagan edim!"),
         P("By the end of the week, I was sleeping better and I wasn't so tired in the morning. I also spent more "
           "time with my family. We talked at dinner instead of looking at our screens.",
           "Hafta oxiriga kelib yaxshiroq uxlay boshladim va ertalab unchalik charchamasdim. Oilam bilan ham koʻproq "
           "vaqt oʻtkaza boshladim. Kechki ovqatda ekranlarga qarash oʻrniga suhbatlashdik."),
         P("Now I have my phone again, but I'm going to use it less. I put it in another room at night, and I read "
           "before bed. It was one of the best weeks of my life.",
           "Hozir telefonim yana oʻzimda, lekin undan kamroq foydalanmoqchiman. Kechasi uni boshqa xonaga qoʻyaman, "
           "uxlashdan oldin kitob oʻqiyman. Bu hayotimdagi eng yaxshi haftalardan biri boʻldi."),
     ],
     [G('strange', 'gʻalati'), G('task', 'topshiriq, vazifa'), G('decide', 'qaror qilmoq'), G('terrible', 'dahshatli'),
      G('bored', 'zerikkan'), G('lonely', 'yolgʻiz, tanho'), G('message', 'xabar'), G('shelf', 'javon, tokcha'),
      G('spend time', 'vaqt oʻtkazmoq'), G('instead of', '…ning oʻrniga'), G('screen', 'ekran'), G('less', 'kamroq')],
     [GN('e15-ever-never', 'Present Perfect + never', 'I have never laughed so much with her!'),
      GN('e22-going-to', 'going to — reja', "I'm going to use it less.")],
     [
         ch('Who gave the students the task?', ['their English teacher', 'their parents', 'the school director'], 0,
            '«our English teacher gave us a strange task».', 0),
         gap('Before the week, Madina spent about ___ hours a day on her phone.', ['five', '5'],
             '«I spent about five hours a day on my phone».', 0),
         tf('Madina was late for school on Monday.', 'T', '«I was late for school on Monday».', 1),
         ch('Why was Madina late for school?', ['She missed the bus.', "She didn't know the time.", 'She was ill.'], 1,
            '«I didn\'t know the time, so I was late» — so = shuning uchun.', 1),
         tf('Madina felt happy and busy in the evenings of the first two days.', 'F',
            '«In the evenings I felt bored and lonely».', 1),
         gap('Madina found an old book on her ___ shelf.', ["sister's", 'sisters', 'sister'], '«on my sister\'s shelf» — opasining javonida.', 2),
         ch('What did her grandmother tell her about?', ['her garden', 'her school years', 'her favourite books'], 1,
            '«she told me funny stories about her school years».', 2),
         tf('Now Madina keeps her phone next to her bed at night.', 'F',
            'Kechasi telefonni boshqa xonaga qoʻyadi: «I put it in another room at night».', 4),
     ])

text(B, 'a2-04-new-school', 'Yangi maktab', 'A New School', 'A2', 'email', L('Maktab', 'School'),
     'Aziz yangi maktabi haqida xolavachchasi Layloga xat yozadi. Oʻqishdan oldin: yangi joyda birinchi kun sizga qanday boʻlgan?',
     [
         P("Hi Laylo, How are you? Sorry for my late answer. We moved to Andijan three weeks ago because my dad got a new "
           "job here, and I started at a new school. I've been very busy!",
           "Salom, Laylo! Qalaysan? Kech javob berganim uchun uzr. Dadam bu yerda yangi ish topgani uchun uch hafta oldin "
           "Andijonga koʻchib keldik va men yangi maktabda oʻqiy boshladim. Juda band boʻlib qoldim!"),
         P("My new school is bigger than my old school in Jizzakh. It has three floors, a big library and a modern "
           "computer room. But the classes are larger too. There are thirty-two students in my class, and at first I "
           "didn't know anyone.",
           "Yangi maktabim Jizzaxdagi eski maktabimdan kattaroq. Unda uch qavat, katta kutubxona va zamonaviy kompyuter "
           "xonasi bor. Lekin sinflar ham kattaroq. Sinfimda oʻttiz ikki oʻquvchi bor, avvaliga hech kimni tanimasdim."),
         P("The first day was hard. I couldn't find the chemistry room, and I sat alone at lunch. But on the second day, "
           "a boy called Doniyor asked me to play football with his friends after school. Now we walk home together "
           "every day.",
           "Birinchi kun qiyin boʻldi. Kimyo xonasini topa olmadim, tushlikda yolgʻiz oʻtirdim. Lekin ikkinchi kuni "
           "Doniyor ismli bola meni darsdan keyin doʻstlari bilan futbol oʻynashga chaqirdi. Endi har kuni uyga birga qaytamiz."),
         P("The lessons are more difficult here, especially maths. I have to do a lot of homework, and I've already had "
           "two tests. I got a good mark in English, but my maths test wasn't great.",
           "Bu yerda darslar qiyinroq, ayniqsa matematika. Koʻp uy vazifasi bajarishim kerak, allaqachon ikkita nazorat "
           "ishi yozdim. Ingliz tilidan yaxshi baho oldim, lekin matematikadan nazorat ishim unchalik yaxshi boʻlmadi."),
         P("Next month our school is going to have a sports festival, and I'm going to run in the 400-metre race. Wish me "
           "luck! Write soon and tell me about your school. Your cousin, Aziz",
           "Kelasi oy maktabimizda sport bayrami boʻladi, men 400 metrga yugurish musobaqasida qatnashaman. Menga omad tila! "
           "Tezroq yoz, maktabing haqida aytib ber. Xolavachchang Aziz"),
     ],
     [G('move', 'koʻchmoq'), G('floor', 'qavat'), G('library', 'kutubxona'), G('modern', 'zamonaviy'),
      G('at first', 'avvaliga, dastlab'), G('alone', 'yolgʻiz'), G('together', 'birga'), G('especially', 'ayniqsa'),
      G('homework', 'uy vazifasi'), G('test', 'nazorat ishi, test'), G('race', 'poyga, yugurish musobaqasi'), G('luck', 'omad')],
     [GN('e45-comparatives', 'Qiyosiy daraja: bigger than', 'My new school is bigger than my old school in Jizzakh.'),
      GN('e28-have-to', 'have to — majbur boʻlmoq', 'I have to do a lot of homework')],
     [
         ch("Why did Aziz's family move to Andijan?", ['His dad got a new job.', 'His grandparents live there.', 'He wanted a better school.'], 0,
            '«because my dad got a new job here».', 0),
         gap("Aziz's family moved to Andijan ___ weeks ago.", ['three', '3'], '«We moved to Andijan three weeks ago».', 0),
         tf("Aziz's old school was in Jizzakh.", 'T', '«my old school in Jizzakh».', 1),
         tf("Aziz's new school is smaller than his old one.", 'F', 'Yangi maktab kattaroq: «bigger than my old school».', 1),
         gap("There are ___ students in Aziz's class.", ['thirty-two', '32', 'thirty two'],
             '«There are thirty-two students in my class».', 1),
         ch('How did Aziz meet Doniyor?',
            ['They sat together at lunch.', 'Doniyor invited him to play football.', 'They were in the same chemistry class.'], 1,
            '«a boy called Doniyor asked me to play football with his friends». Tushlikda Aziz yolgʻiz oʻtirgan.', 2),
         tf('Aziz got a good mark in his maths test.', 'F', '«my maths test wasn\'t great». Yaxshi baho — ingliz tilidan.', 3),
         ch('What is Aziz going to do next month?', ['take a maths test', 'run in a race', 'visit Laylo'], 1,
            '«I\'m going to run in the 400-metre race».', 4),
     ])

text(B, 'a2-05-grandpa', 'Bobomning yoshligi', "My Grandfather's Youth", 'A2', 'biography', L('Oila tarixi', 'Family history'),
     'Nevara bobosining yoshligi haqida yozadi. Oʻqishdan oldin: bobongiz yoki buvingiz yoshligida qanday yashagan?',
     [
         P("My grandfather, Rustam, is seventy-eight years old. He was born in a small village near Kokand. Last weekend "
           "I asked him about his youth, and he talked for two hours. Here is his story.",
           "Bobom Rustam yetmish sakkiz yoshda. U Qoʻqon yaqinidagi kichik qishloqda tugʻilgan. Oʻtgan dam olish kuni "
           "undan yoshligi haqida soʻradim, u ikki soat gapirib berdi. Mana uning hikoyasi."),
         P("When he was a boy, life was much harder than today. There was no television in the village, and only a few "
           "families had a radio. My grandfather had to walk five kilometres to school every morning, even in winter.",
           "U bolaligida hayot bugungidan ancha ogʻir edi. Qishloqda televizor yoʻq edi, faqat bir nechta oilada radio bor edi. "
           "Bobom har kuni ertalab, hatto qishda ham, maktabga besh kilometr piyoda borishi kerak edi."),
         P("After school, he used to help his father with the sheep. In summer, he and his friends swam in the river and "
           "climbed apricot trees. They didn't have many toys, but they made balls from old cloth and played until dark.",
           "Darsdan keyin u otasiga qoʻylarni boqishda yordam berardi. Yozda doʻstlari bilan daryoda suzib, oʻrik "
           "daraxtlariga chiqishardi. Ularning oʻyinchoqlari koʻp emas edi, lekin eski matodan toʻp yasab, qorongʻi "
           "tushguncha oʻynashardi."),
         P("At eighteen, he moved to Tashkent and studied to be an engineer. He worked at a factory for almost forty "
           "years and built machines. He met my grandmother at the factory, and he says she was the best worker there.",
           "Oʻn sakkiz yoshida u Toshkentga koʻchib bordi va muhandislikka oʻqidi. U qariyb qirq yil zavodda ishlab, "
           "mashinalar yasadi. Buvim bilan oʻsha zavodda tanishgan va uning aytishicha, buvim u yerdagi eng yaxshi ishchi boʻlgan."),
         P("Today my grandfather lives with us. He still gets up early and walks in the park every morning. I think his "
           "life was harder than mine, but he was happy. I'm going to write his story in a notebook so I never forget it.",
           "Hozir bobom biz bilan yashaydi. U hali ham erta turadi va har kuni ertalab bogʻda sayr qiladi. Menimcha, uning "
           "hayoti menikidan ogʻirroq boʻlgan, lekin u baxtli edi. Uning hikoyasini hech qachon unutmaslik uchun daftarga yozib qoʻymoqchiman."),
     ],
     [G('youth', 'yoshlik'), G('be born', 'tugʻilmoq'), G('village', 'qishloq'), G('even', 'hatto'),
      G('sheep', 'qoʻy'), G('climb', 'chiqmoq, tirmashmoq'), G('apricot', 'oʻrik'), G('cloth', 'mato, latta'),
      G('engineer', 'muhandis'), G('factory', 'zavod, fabrika'), G('notebook', 'daftar'), G('forget', 'unutmoq')],
     [GN('e28-have-to', 'had to — majbur edi', 'My grandfather had to walk five kilometres to school every morning'),
      GN('e11-used-to', 'used to — ilgari qilardi', 'After school, he used to help his father with the sheep.')],
     [
         gap('Rustam is ___ years old.', ['seventy-eight', '78', 'seventy eight'], '«is seventy-eight years old».', 0),
         tf('Rustam was born in Tashkent.', 'F', 'U Qoʻqon yaqinidagi qishloqda tugʻilgan: «born in a small village near Kokand».', 0),
         ch('How did Rustam go to school?', ['by bus', 'on foot', 'by horse'], 1,
            '«had to walk five kilometres to school» — piyoda borgan.', 1),
         tf('Every family in the village had a radio.', 'F', '«only a few families had a radio».', 1),
         ch('What did the children make their balls from?', ['old cloth', 'apricots', 'paper'], 0,
            '«they made balls from old cloth».', 2),
         tf('Rustam met his wife at the factory.', 'T', '«He met my grandmother at the factory».', 3),
         gap('Rustam worked at a factory for almost ___ years.', ['forty', '40'], '«He worked at a factory for almost forty years».', 3),
         ch('Why is the writer going to write the story in a notebook?',
            ['for a school project', 'so the story is never forgotten', 'because the grandfather asked for it'], 1,
            '«I\'m going to write his story in a notebook so I never forget it».', 4),
     ])
