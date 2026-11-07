"""A2 · 4-boʻlim: Ish va oʻqish (5 ta matn)"""
from lib import *

B = 'a2'
WORK = L('Ish va oʻqish', 'Work and study')

text(B, 'a2-16-job-ad', 'Ish eʼloni', 'Summer Job at a Café', 'A2', 'notice', WORK,
     'Samarqanddagi kafe yozga ishchi qidirmoqda. Oʻqishdan oldin oʻylab koʻring: ish eʼlonida qanday maʼlumotlar boʻlishi kerak?',
     [
         P("Bahor Café in Samarkand is looking for two waiters for the summer. The café is near the Registan, "
           "so a lot of tourists come here every day. The job starts on 1 June and finishes on 31 August.",
           "Samarqanddagi «Bahor» kafesi yozga ikkita ofitsiant qidirmoqda. Kafe Registon yaqinida joylashgan, "
           "shuning uchun bu yerga har kuni koʻplab sayyohlar keladi. Ish 1-iyunda boshlanib, 31-avgustda tugaydi."),
         P("You have to be eighteen or older. You must be friendly and polite. You need to speak some English, "
           "because many of our guests are from other countries. You don't need any experience. "
           "We will teach you everything in your first week.",
           "Siz 18 yoki undan katta yoshda boʻlishingiz shart. Siz xushmuomala va odobli boʻlishingiz kerak. "
           "Biroz inglizcha gapira olishingiz lozim, chunki mehmonlarimizning koʻpchiligi boshqa davlatlardan. "
           "Tajriba talab qilinmaydi. Birinchi haftada sizga hamma narsani oʻrgatamiz."),
         P("You will work five days a week, from ten in the morning to six in the evening. The pay is 4,000,000 sum a month. "
           "You can also keep your tips. Lunch is free for all our workers.",
           "Haftasiga besh kun, ertalab soat oʻndan kechqurun soat oltigacha ishlaysiz. Maosh oyiga 4 000 000 soʻm. "
           "Choychaqalar ham sizda qoladi. Barcha xodimlarimiz uchun tushlik bepul."),
         P("Would you like to join our team? Please send a short letter about yourself to the café manager, Mr Rustamov. "
           "Write about the languages you speak and why you want this job. The last day to apply is 20 May.",
           "Jamoamizga qoʻshilishni xohlaysizmi? Iltimos, oʻzingiz haqingizda qisqa xatni kafe menejeri janob Rustamovga yuboring. "
           "Qaysi tillarni bilishingiz va nima uchun bu ishni xohlashingiz haqida yozing. Ariza topshirishning oxirgi kuni — 20-may."),
         P("We are going to invite the best people for an interview at the end of May. Good luck!",
           "Eng munosib nomzodlarni may oyi oxirida suhbatga taklif qilamiz. Omad!"),
     ],
     [G('waiter', 'ofitsiant'), G('polite', 'odobli, xushmuomala'), G('guest', 'mehmon'),
      G('experience', 'tajriba'), G('pay', 'maosh, ish haqi'), G('tip', 'choychaqa'),
      G('worker', 'ishchi, xodim'), G('join', 'qoʻshilmoq'), G('team', 'jamoa'),
      G('manager', 'menejer, rahbar'), G('apply', 'ariza topshirmoq'), G('interview', 'suhbat (ishga qabul)')],
     [GN('e28-have-to', 'have to — majburiyat (shart)', 'You have to be eighteen or older.'),
      GN('e27-must-mustnt-neednt', 'must — shart, kerak', 'You must be friendly and polite.')],
     [
         tf('The café needs workers for the whole year.', 'F',
            'Faqat yozga: «for the summer… starts on 1 June and finishes on 31 August».', 0),
         tf('You need experience to get this job.', 'F', 'Tajriba shart emas: «You don\'t need any experience.»', 1),
         ch('Why do the workers need to speak some English?',
            ['because the manager is English', 'because many guests are from other countries', 'because the menu is only in English'], 1,
            '«because many of our guests are from other countries» — mehmonlarning koʻpi chet elliklar.', 1),
         ch('How many days a week will the waiters work?', ['four', 'five', 'six'], 1,
            '«You will work five days a week».', 2),
         tf('Workers have to pay for their lunch.', 'F', 'Tushlik bepul: «Lunch is free for all our workers.»', 2),
         gap('The workers can also keep their ___.', 'tips', '«You can also keep your tips.»', 2),
         gap('The last day to apply is ___ May.', ['20', 'twenty', '20th', 'twentieth'],
            '«The last day to apply is 20 May.»', 3),
         ch('What is going to happen at the end of May?',
            ['The café is going to close.', 'Some people are going to have an interview.', 'The summer job is going to start.'], 1,
            '«We are going to invite the best people for an interview at the end of May.» Ish esa 1-iyunda boshlanadi.', 4),
     ])

text(B, 'a2-17-university', 'Universitetga hujjat topshirish', 'Applying to University', 'A2', 'email', WORK,
     'Talaba Kamola universitetga hujjat topshirmoqchi boʻlgan amakivachchasiga maslahat yozadi. '
     'Oʻqishdan oldin: siz qaysi fanni oʻqishni xohlaysiz va nima uchun?',
     [
         P("Hi Nodira, Thank you for your message. You asked me about applying to university, so I would like to tell you "
           "about my experience. I applied two years ago, and now I am a student at a university in Tashkent.",
           "Salom, Nodira! Xating uchun rahmat. Sen mendan universitetga hujjat topshirish haqida soʻragan eding, "
           "shuning uchun oʻz tajribam haqida aytib bermoqchiman. Men ikki yil oldin hujjat topshirganman, hozir esa Toshkentdagi universitetda talabaman."),
         P("First, you have to choose your subject. Don't choose it only because your friends like it. "
           "Think about your future job. I chose economics because I have always liked maths.",
           "Avvalo, yoʻnalishingni tanlashing kerak. Uni faqat doʻstlaringga yoqqani uchun tanlama. "
           "Kelajakdagi kasbing haqida oʻyla. Men iqtisodiyotni tanladim, chunki matematikani doim yaxshi koʻrganman."),
         P("Then you need to prepare your documents. Every university has its own rules, so read its website carefully. "
           "Often they ask for a copy of your passport, your school certificate and some photos. "
           "Check the dates, because you mustn't be late!",
           "Keyin hujjatlaringni tayyorlashing kerak. Har bir universitetning oʻz qoidalari bor, shuning uchun uning saytini diqqat bilan oʻqi. "
           "Koʻpincha pasport nusxasi, maktab attestati va bir nechta surat soʻrashadi. "
           "Sanalarni tekshir, chunki kechikmasliging kerak!"),
         P("The entrance exam was the hardest part for me. I studied for six months. I did a lot of practice tests "
           "and went to extra lessons on Saturdays. Have you started studying yet?",
           "Men uchun eng qiyini kirish imtihoni boʻldi. Olti oy tayyorlandim. Koʻp sinov testlarini yechdim "
           "va shanba kunlari qoʻshimcha darslarga bordim. Sen tayyorlanishni boshladingmi?"),
         P("Don't worry too much. You are a clever girl, and I am sure you will do well. "
           "Write to me if you have any questions. Love, Kamola",
           "Ortiqcha xavotir olma. Sen aqlli qizsan, yaxshi natija koʻrsatishingga ishonaman. "
           "Savollaring boʻlsa, menga yoz. Mehr bilan, Kamola"),
     ],
     [G('apply', 'hujjat topshirmoq, ariza bermoq'), G('subject', 'fan; yoʻnalish'), G('economics', 'iqtisodiyot'),
      G('prepare', 'tayyorlamoq'), G('document', 'hujjat'), G('rule', 'qoida'), G('carefully', 'diqqat bilan'),
      G('copy', 'nusxa'), G('certificate', 'attestat, guvohnoma'), G('entrance exam', 'kirish imtihoni'),
      G('practice test', 'sinov (mashq) testi'), G('worry', 'xavotir olmoq')],
     [GN('e28-have-to', 'have to — kerak, majbur', 'you have to choose your subject'),
      GN('e14-just-already-yet', 'Present Perfect: yet (soʻroqda)', 'Have you started studying yet?')],
     [
         tf('Kamola is a university student now.', 'T', '«now I am a student at a university in Tashkent».', 0),
         ch('Why did Kamola choose economics?',
            ['because her friends chose it', 'because she has always liked maths', 'because her parents told her to'], 1,
            '«I chose economics because I have always liked maths.»', 1),
         tf('Kamola thinks you should choose a subject because your friends like it.', 'F',
            'Aksincha: «Don\'t choose it only because your friends like it.»', 1),
         ch('Why should Nodira read the university website carefully?',
            ['because every university has its own rules', 'because the website has practice tests', 'because Kamola works there'], 0,
            '«Every university has its own rules, so read its website carefully.»', 2),
         gap('Kamola studied for the entrance exam for ___ months.', ['six', '6'], '«I studied for six months.»', 3),
         tf('Kamola went to extra lessons on Sundays.', 'F', 'Shanba kunlari: «went to extra lessons on Saturdays».', 3),
         ch('Which part was the hardest for Kamola?', ['choosing a subject', 'the entrance exam', 'preparing the photos'], 1,
            '«The entrance exam was the hardest part for me.»', 3),
         gap('Kamola is sure that Nodira will do ___.', 'well', '«I am sure you will do well.»', 4),
     ])

text(B, 'a2-18-summer-job', 'Yozgi ish', 'A Summer Job at the Bakery', 'A2', 'story', WORK,
     'Sardor yozda novvoyxonada ishlaydi. Oʻqishdan oldin: siz yozgi taʼtilda ishlab koʻrganmisiz?',
     [
         P("Last summer, Sardor was seventeen. He wanted to buy a new laptop, but his parents couldn't give him the money. "
           "So he decided to find a summer job.",
           "Oʻtgan yozda Sardor oʻn yetti yoshda edi. U yangi noutbuk sotib olmoqchi edi, lekin ota-onasi unga pul bera olmadi. "
           "Shuning uchun u yozgi ish topishga qaror qildi."),
         P("His neighbour, Mr Hamidov, has a small bakery in Bukhara. He needed a helper, and Sardor got the job. "
           "He had to start work at five o'clock in the morning, because people buy fresh bread very early.",
           "Qoʻshnisi Hamidovning Buxoroda kichik novvoyxonasi bor. Unga yordamchi kerak edi va Sardor shu ishga kirdi. "
           "U ishni ertalab soat beshda boshlashi kerak edi, chunki odamlar yangi nonni juda erta sotib olishadi."),
         P("The first week was difficult. Sardor was always tired, and once he burned forty loaves of bread! "
           "Mr Hamidov wasn't angry. He just laughed and said, \"Be more careful next time.\"",
           "Birinchi hafta qiyin boʻldi. Sardor doim charchagan edi, bir safar esa qirqta nonni kuydirib qoʻydi! "
           "Hamidovning jahli chiqmadi. U shunchaki kuldi va: «Keyingi safar ehtiyotkorroq boʻl», — dedi."),
         P("Slowly, Sardor learned a lot. He could make dough, use the big oven and talk to customers. "
           "By the end of August, he had enough money for his laptop.",
           "Asta-sekin Sardor koʻp narsani oʻrgandi. U xamir qora olar, katta tandirdan foydalana olar va xaridorlar bilan gaplasha olardi. "
           "Avgust oxiriga kelib, noutbuk uchun yetarli pulga ega boʻldi."),
         P("Now Sardor is back at school, but he still visits the bakery on Sundays. He says that the job taught him two things: "
           "to get up early and to work hard. Next summer, he is going to work there again.",
           "Hozir Sardor yana maktabda oʻqiyapti, lekin yakshanba kunlari hamon novvoyxonaga boradi. Uning aytishicha, bu ish unga ikki narsani oʻrgatdi: "
           "erta turishni va qattiq mehnat qilishni. Kelasi yozda u yana oʻsha yerda ishlamoqchi."),
     ],
     [G('decide', 'qaror qilmoq'), G('neighbour', 'qoʻshni'), G('bakery', 'novvoyxona'), G('helper', 'yordamchi'),
      G('fresh', 'yangi, yangi uzilgan/pishgan'), G('tired', 'charchagan'), G('burn', 'kuydirmoq'),
      G('loaf / loaves', 'bir dona non / nonlar'), G('careful', 'ehtiyotkor'), G('dough', 'xamir'),
      G('oven', 'tandir, pech'), G('customer', 'xaridor, mijoz')],
     [GN('e28-have-to', 'had to — oʻtgan zamonda majburiyat', "He had to start work at five o'clock in the morning"),
      GN('e22-going-to', 'going to — reja', 'he is going to work there again')],
     [
         ch('Why did Sardor look for a summer job?',
            ['He wanted to buy a laptop.', 'He wanted to leave school.', 'His teacher asked him to.'], 0,
            '«He wanted to buy a new laptop, but his parents couldn\'t give him the money.»', 0),
         tf('Sardor started work very early in the morning.', 'T', '«He had to start work at five o\'clock in the morning».', 1),
         ch('Why did Sardor have to start work so early?',
            ['because it is very hot in the afternoon', 'because people buy fresh bread very early', 'because he had lessons later'], 1,
            '«because people buy fresh bread very early».', 1),
         gap('Once Sardor burned ___ loaves of bread.', ['forty', '40'], '«once he burned forty loaves of bread!»', 2),
         tf('Mr Hamidov was angry about the burned bread.', 'F', '«Mr Hamidov wasn\'t angry. He just laughed».', 2),
         tf('Sardor earned enough money for the laptop.', 'T',
            '«By the end of August, he had enough money for his laptop.»', 3),
         gap('Now Sardor visits the bakery on ___.', 'Sundays', '«he still visits the bakery on Sundays».', 4),
         ch('What is Sardor going to do next summer?',
            ['travel to Tashkent', 'work at the bakery again', 'open his own bakery'], 1,
            '«Next summer, he is going to work there again.»', 4),
     ])

text(B, 'a2-19-online-course', 'Onlayn kurs', 'An Online Course', 'A2', 'dialogue', WORK,
     'Malika va Bobur onlayn kurs haqida gaplashishadi. Oʻqishdan oldin: siz internet orqali biror narsa oʻrganganmisiz?',
     [
         P("Bobur: Malika, you look tired. Are you OK? Malika: I'm fine, thanks. I've just finished a lesson for my online course. "
           "I'm learning web design.",
           "Bobur: Malika, charchagan koʻrinasan. Yaxshimisan? Malika: Yaxshiman, rahmat. Hozirgina onlayn kursimdagi darsni tugatdim. "
           "Men veb-dizaynni oʻrganyapman."),
         P("Bobur: Online? Is it difficult to study without a teacher? Malika: There is a teacher, but she lives in Tashkent "
           "and I live in Namangan. We meet in a video lesson every Tuesday. The other lessons are short videos, "
           "so I can watch them at any time.",
           "Bobur: Onlayn? Oʻqituvchisiz oʻqish qiyin emasmi? Malika: Oʻqituvchi bor, lekin u Toshkentda yashaydi, "
           "men esa Namanganda. Har seshanba video darsda uchrashamiz. Qolgan darslar qisqa videolar, "
           "shuning uchun ularni xohlagan vaqtda koʻra olaman."),
         P("Bobur: How long is the course? Malika: Three months. I have already finished the first month, "
           "and I've made my first simple website. It was for my aunt's flower shop!",
           "Bobur: Kurs qancha davom etadi? Malika: Uch oy. Birinchi oyni allaqachon tugatdim "
           "va birinchi oddiy saytimni yaratdim. U xolamning gul doʻkoni uchun edi!"),
         P("Bobur: That's great. Is it expensive? Malika: Not very. It costs 300,000 sum a month. But you have to be very organised. "
           "Nobody checks if you watch the videos. Last week I was lazy, and I haven't done my homework yet.",
           "Bobur: Zoʻr-ku. Qimmatmi? Malika: Unchalik emas. Oyiga 300 000 soʻm turadi. Lekin juda tartibli boʻlishing kerak. "
           "Videolarni koʻryapsanmi-yoʻqmi, hech kim tekshirmaydi. Oʻtgan hafta dangasalik qildim va uy vazifamni hali bajarmadim."),
         P("Bobur: Maybe I should try a course too. I'd like to learn photography. "
           "Malika: Good idea! I'll send you the link to the website after dinner.",
           "Bobur: Balki men ham biror kursni sinab koʻrarman. Fotografiyani oʻrganmoqchiman. "
           "Malika: Yaxshi fikr! Kechki ovqatdan keyin senga sayt havolasini yuboraman."),
     ],
     [G('online course', 'onlayn kurs'), G('web design', 'veb-dizayn'), G('without', '…siz, …dan holi'),
      G('at any time', 'xohlagan vaqtda'), G('simple', 'oddiy'), G('website', 'veb-sayt'),
      G('expensive', 'qimmat'), G('organised', 'tartibli, uyushgan'), G('check', 'tekshirmoq'),
      G('lazy', 'dangasa'), G('photography', 'fotografiya, suratga olish'), G('link', 'havola')],
     [GN('e14-just-already-yet', 'just / already / yet', 'I have already finished the first month'),
      GN('e30-would-like', 'would like — xohlamoq (muloyim)', "I'd like to learn photography.")],
     [
         tf('Malika has just finished a lesson.', 'T', '«I\'ve just finished a lesson for my online course.»', 0),
         ch('What is Malika learning?', ['photography', 'web design', 'English'], 1,
            '«I\'m learning web design.» Fotografiyani esa Bobur oʻrganmoqchi.', 0),
         tf('Malika and her teacher live in the same city.', 'F',
            'Oʻqituvchi Toshkentda, Malika Namanganda: «she lives in Tashkent and I live in Namangan».', 1),
         ch('Why can Malika watch most of the lessons at any time?',
            ['because they are short videos', 'because her teacher is always online', 'because she doesn\'t go to work'], 0,
            '«The other lessons are short videos, so I can watch them at any time.»', 1),
         gap("Malika made her first website for her aunt's ___ shop.", 'flower', '«It was for my aunt\'s flower shop!»', 2),
         gap('The course costs ___ sum a month.', ['300,000', '300 000', '300000'], '«It costs 300,000 sum a month.»', 3),
         tf('Malika has done all her homework.', 'F', '«I haven\'t done my homework yet.» — hali bajarmagan.', 3),
         ch('What would Bobur like to learn?', ['web design', 'cooking', 'photography'], 2,
            '«I\'d like to learn photography.»', 4),
     ])

text(B, 'a2-20-interview', 'Ish suhbatidan keyin', 'After the Interview', 'A2', 'blog', WORK,
     'Zarina birinchi ish suhbatidan keyin blogiga yozadi. Oʻqishdan oldin: ish suhbatida qanday savollar berilishi mumkin?',
     [
         P("Today I had my first job interview! I want to be a tour guide, and a small travel company in Samarkand "
           "needs a new guide for English-speaking tourists. The interview was at ten o'clock this morning.",
           "Bugun birinchi ish suhbatimga bordim! Men gid boʻlishni xohlayman, Samarqanddagi kichik sayyohlik kompaniyasiga esa "
           "ingliz tilida soʻzlashuvchi sayyohlar uchun yangi gid kerak. Suhbat bugun ertalab soat oʻnda boʻldi."),
         P("I was very nervous. I woke up at six and I couldn't eat breakfast. I put on my best white shirt and took a taxi, "
           "because I didn't want to be late. I arrived twenty minutes early.",
           "Juda hayajonlandim. Soat oltida uygʻondim va nonushta qila olmadim. Eng yaxshi oq koʻylagimni kiydim va taksiga oʻtirdim, "
           "chunki kechikishni istamadim. Yigirma daqiqa erta yetib keldim."),
         P("There were two people at the interview: the manager and an older guide. First, they asked me questions in Uzbek. "
           "Then the guide started to speak English, and I had to tell them about the Registan. "
           "I think I did it well, because they smiled a lot.",
           "Suhbatda ikki kishi bor edi: menejer va yoshi kattaroq bir gid. Avval ular menga oʻzbek tilida savollar berishdi. "
           "Keyin gid inglizcha gapira boshladi va men ularga Registon haqida gapirib berishim kerak edi. "
           "Menimcha, yaxshi uddaladim, chunki ular koʻp jilmayishdi."),
         P("They also asked me a difficult question: \"What will you do if a tourist gets lost?\" I answered, \"I will phone "
           "the tourist and wait at the meeting place.\" I'm not sure it was the best answer.",
           "Ular yana bir qiyin savol ham berishdi: «Agar sayyoh adashib qolsa, nima qilasiz?» Men: «Sayyohga qoʻngʻiroq qilaman "
           "va uchrashuv joyida kutaman», — deb javob berdim. Bu eng yaxshi javob boʻldimi, bilmayman."),
         P("The manager said, \"We are going to call you on Friday.\" I haven't heard anything yet, of course, "
           "but I feel hopeful. If I get the job, I will start in June. Wish me luck!",
           "Menejer: «Juma kuni sizga qoʻngʻiroq qilamiz», — dedi. Albatta, hali hech narsa eshitmadim, "
           "lekin umidim bor. Agar ishga olishsa, iyunda ish boshlayman. Menga omad tilang!"),
     ],
     [G('job interview', 'ish suhbati'), G('tour guide', 'gid'), G('travel company', 'sayyohlik kompaniyasi'),
      G('nervous', 'hayajonlangan, asabiy'), G('put on', 'kiymoq'), G('arrive', 'yetib kelmoq'),
      G('manager', 'menejer, rahbar'), G('smile', 'jilmaymoq'), G('get lost', 'adashib qolmoq'),
      G('meeting place', 'uchrashuv joyi'), G('hopeful', 'umidvor'), G('wish', 'tilamoq')],
     [GN('e54-when-if', 'if + Present Simple, … will', 'If I get the job, I will start in June.'),
      GN('e22-going-to', 'going to — reja', 'We are going to call you on Friday.')],
     [
         tf('Zarina wants to work as a tour guide.', 'T', '«I want to be a tour guide».', 0),
         tf('The interview was in the afternoon.', 'F', 'Ertalab: «The interview was at ten o\'clock this morning.»', 0),
         ch('Why did Zarina take a taxi?',
            ['because it was raining', 'because she didn\'t want to be late', 'because the company paid for it'], 1,
            '«took a taxi, because I didn\'t want to be late».', 1),
         gap('Zarina arrived ___ minutes early.', ['twenty', '20'], '«I arrived twenty minutes early.»', 1),
         ch('Why does Zarina think she spoke well about the Registan?',
            ['because the manager told her so', 'because they smiled a lot', 'because they gave her the job'], 1,
            '«I think I did it well, because they smiled a lot.»', 2),
         tf('Zarina is sure that her answer about the lost tourist was the best.', 'F',
            '«I\'m not sure it was the best answer.»', 3),
         ch('When is the company going to call Zarina?', ['on Monday', 'on Friday', 'in June'], 1,
            '«We are going to call you on Friday.» Iyun — ish boshlanadigan oy.', 4),
         gap('If Zarina gets the job, she will start in ___.', 'June', '«If I get the job, I will start in June.»', 4),
     ])
