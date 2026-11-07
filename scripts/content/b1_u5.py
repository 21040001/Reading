"""B1 · 5-boʻlim: Ish dunyosi (5 ta matn)"""
from lib import *

B = 'b1'
WORK = L('Ish dunyosi', 'The world of work')

text(B, 'b1-21-formal-letter', 'Rasmiy xat', 'A Letter of Complaint', 'B1', 'email', WORK,
     'Bu — internet-doʻkonga yozilgan rasmiy shikoyat xati. Oʻqishdan oldin oʻylab koʻring: buyurtmangiz kechiksa, nima qilasiz?',
     [
         P("Dear Sir or Madam, I am writing to complain about order number 40215, which I placed on your website on 3 September. "
           "I ordered a wooden desk and a chair for my son, who has just started secondary school. When I paid for the order, "
           "the website said that it would be delivered within five working days."),
         P("Unfortunately, the delivery did not arrive on time. I have contacted your customer service twice by phone. "
           "The first time, I was told that the desk was still in the warehouse and would be sent the next day. The second time, "
           "nobody could tell me where my order was. I waited at home for two whole days, but no one came."),
         P("The desk finally arrived on 21 September, almost three weeks after I had placed the order. However, when I opened the box, I found that one "
           "of the legs was broken, and the chair was missing. As a result, my son has had to do his homework at the kitchen table "
           "for almost a month."),
         P("I have been a customer of your shop for three years, and until now I have always been satisfied with your service. "
           "That is why this experience has been so disappointing. I understand that delays can happen, but I would have expected "
           "someone to inform me about the problem."),
         P("I would therefore be grateful if you could replace the broken desk and send the missing chair as soon as possible. "
           "I would also like a partial refund of the delivery fee, as the service was clearly not what I had paid for. "
           "I have attached photos of the damaged desk and a copy of my receipt."),
         P("I look forward to hearing from you within seven days. If I do not receive a reply, I will have to take further action. "
           "Yours faithfully, Nodira Karimova"),
     ],
     [G('complain about', '… dan shikoyat qilmoq'), G('place an order', 'buyurtma bermoq'),
      G('deliver', 'yetkazib bermoq'), G('working days', 'ish kunlari'), G('unfortunately', 'afsuski'),
      G('warehouse', 'ombor'), G('missing', 'yetishmayotgan, yoʻq'), G('satisfied', 'mamnun, qoniqqan'),
      G('disappointing', 'hafsalani pir qiladigan, koʻngilni qoldiradigan'), G('inform', 'xabardor qilmoq'), G('replace', 'almashtirib bermoq'),
      G('refund', 'pulni qaytarish'), G('receipt', 'chek, kvitansiya'), G('look forward to', '… ni intiqlik bilan kutmoq')],
     [GN('i33-reported-speech', 'Oʻzlashtirma gap: said that it would …',
         'the website said that it would be delivered within five working days'),
      GN('i05-present-perfect', 'Present Perfect: I have contacted …',
         'I have contacted your customer service twice by phone.')],
     [
         tf('The writer placed the order by phone.', 'F',
            'Buyurtma saytda berilgan: «an order that I placed on your website». Telefon orqali faqat mijozlar xizmatiga qoʻngʻiroq qilgan.', 0, ng=True),
         tf('The writer contacted customer service more than once.', 'T',
            '«I have contacted your customer service twice by phone» — ikki marta.', 1, ng=True),
         tf('The delivery driver apologised when the desk arrived.', 'NG',
            'Haydovchi uzr soʻragani yoki soʻramagani haqida matnda hech narsa yoʻq.', 2, ng=True),
         tf('The writer has bought things from this shop before.', 'T',
            '«I have been a customer of your shop for three years» — uch yildan beri xaridor.', 3, ng=True),
         ch('What is the main purpose of the letter?',
            ['to order some new furniture', 'to complain and ask the company to solve the problem',
             'to thank the company for its service'], 1,
            'Xat «I am writing to complain» bilan boshlanadi va 5-xatboshida aniq talablar bor: almashtirish, stulni yuborish, pulni qaytarish.', 0),
         ch('What does the writer say about delays?',
            ['They are never acceptable.', 'They can happen, but the company should have told her.',
             'They are always the fault of the driver.'], 1,
            '«I understand that delays can happen, but I would have expected someone to inform me» — kechikish boʻlishi mumkin, lekin xabar berish kerak edi.', 3),
         ch('In paragraph 5, a «partial refund» means getting …',
            ['all of the money back', 'some of the money back', 'a new order for free'], 1,
            '«partial» — qisman. Muallif faqat yetkazib berish haqining bir qismini qaytarishni soʻraydi: «a partial refund of the delivery fee».', 4),
         gap('The writer has attached photos of the damaged desk and a copy of her ___.', 'receipt',
             '«a copy of my receipt» — chekning nusxasi.', 4, 2),
         gap('The writer expects a reply within ___.', ['seven days', '7 days'],
             '«I look forward to hearing from you within seven days.»', 5, 2),
     ])

text(B, 'b1-22-cv', 'Rezyume qanday yoziladi', 'How to Write a CV', 'B1', 'article', WORK,
     'Bu maqolada yaxshi rezyume yozish boʻyicha maslahatlar berilgan. Oʻqishdan oldin oʻylab koʻring: rezyumeda qanday boʻlimlar boʻlishi kerak?',
     [
         P("Your CV is often the first thing an employer learns about you. Employers who receive a lot of applications usually "
           "look at each CV only briefly at first, so yours needs to make a good impression quickly. Here are some tips that will "
           "help you write a CV that gets noticed."),
         P("A good CV usually has a few clear sections. At the top, write your name and contact details: your phone number, your "
           "email address and the city where you live. Next, add a short personal profile of two or three sentences that describes "
           "who you are and what you are looking for. After that come your work experience and your education, with the most recent "
           "first. Finally, list your skills, such as languages and computer programs you can use."),
         P("Keep it short. For most young people, one page is enough, and even experienced workers rarely need more than two. "
           "Use bullet points instead of long paragraphs, and choose a simple, clear font. A CV that is full of decoration may look "
           "creative, but it is often harder to read."),
         P("One of the most common mistakes is sending exactly the same CV to every company. Before you apply, read the job "
           "advertisement carefully and find out which skills the employer is looking for. Then change your CV so that these skills "
           "are easy to see. If a job asks for teamwork, for example, mention the volunteer project where you worked with a group "
           "of other students."),
         P("Before you send it, check your CV carefully for spelling and grammar mistakes. It is a good idea to ask a friend or a "
           "teacher to read it too, because it is easy to miss your own errors. Most importantly, be honest. If you say that you "
           "speak fluent German but you have only studied it for a few months, the truth will come out at the interview, and you "
           "will lose the employer's trust."),
         P("Writing a good CV takes time, but it is time well spent. Remember that the aim of a CV is not to get you the job. "
           "Its aim is to get you an interview, where you can show the employer who you really are."),
     ],
     [G('employer', 'ish beruvchi'), G('application', 'ariza'), G('make a good impression', 'yaxshi taassurot qoldirmoq'),
      G('contact details', 'aloqa maʼlumotlari'), G('personal profile', 'oʻzingiz haqingizda qisqa maʼlumot'),
      G('experience', 'tajriba'), G('skill', 'koʻnikma, malaka'), G('bullet point', 'roʻyxat belgisi, nuqtali band'),
      G('font', 'shrift'), G('job advertisement', 'ish eʼloni'), G('volunteer', 'koʻngilli'),
      G('spelling', 'imlo'), G('fluent', 'erkin, ravon'), G('trust', 'ishonch')],
     [GN('i64-so-that-in-order-to', 'Maqsad: so that …', 'change your CV so that these skills are easy to see'),
      GN('i54-whose-whom-where', 'Nisbiy gap: where', 'the volunteer project where you worked with a group of other students')],
     [
         tf('The writer says the personal profile should be very long.', 'F',
            'Profil qisqa boʻlishi kerak: «a short personal profile of two or three sentences».', 1, ng=True),
         tf('The writer advises including a photo on your CV.', 'NG',
            'Matnda rasm haqida hech narsa aytilmagan — Not Given.', 1, ng=True),
         tf('Experienced workers often need a CV of more than two pages.', 'F',
            '«even experienced workers rarely need more than two» — kamdan-kam hollarda.', 2, ng=True),
         tf('Other people may notice mistakes that you have missed.', 'T',
            '«ask a friend or a teacher to read it too, because it is easy to miss your own errors».', 4, ng=True),
         hd(2, ['Short and simple', 'Creative designs win', 'Your contact details'], 0,
            '3-xatboshi qisqalik va soddalik haqida: «Keep it short», «a simple, clear font». Bezakli dizayn esa tavsiya qilinmaydi.'),
         ch('Why should you change your CV for each job?',
            ['because employers prefer long CVs', 'so that the skills the employer needs are easy to see',
             'because companies do not accept the same CV twice'], 1,
            '«change your CV so that these skills are easy to see».', 3),
         ch('According to the writer, what is the main aim of a CV?',
            ['to get you the job', 'to get you an interview', 'to show how creative you are'], 1,
            '«the aim of a CV is not to get you the job. Its aim is to get you an interview».', 5),
         gap('Work experience and education should be listed with the most ___ first.', 'recent',
             '«with the most recent first» — eng oxirgisi birinchi.', 1, 2),
         gap('If you are not honest, you will lose the employer\'s ___.', 'trust',
             '«you will lose the employer\'s trust» — ish beruvchining ishonchini yoʻqotasiz.', 4, 2),
     ])

text(B, 'b1-23-remote-work', 'Masofaviy ish', 'Working from Home', 'B1', 'blog', WORK,
     'Bu blogda bir dizayner uydan ishlash tajribasi haqida yozadi. Oʻqishdan oldin oʻylab koʻring: siz uydan ishlashni yoki ofisda ishlashni afzal koʻrasizmi?',
     [
         P("Two years ago, the small design company where I work decided that most of us could work from home. At first, I was "
           "delighted. I would no longer have to spend an hour on a crowded bus every morning, and I could start work in comfortable "
           "clothes with a cup of tea next to my laptop. Now, after two years, I want to share what I have learned."),
         P("Let me start with the good things. Without the journey, I have gained about two hours every day, and I use some of this "
           "time to go for a walk or cook proper meals. I can also concentrate better. In the office, colleagues often stopped by my "
           "desk to chat, and it was hard to focus on difficult tasks. At home, I can work for long periods without interruptions."),
         P("However, working from home has its problems too. The biggest one for me has been loneliness. Some days I don't speak to "
           "anyone except through a screen. I used to have lunch with my colleagues every day, and I miss those conversations more "
           "than I expected. It is also harder to ask a quick question, because you have to write a message and wait for an answer."),
         P("Another problem is that work and home life can mix together. During my first months, I often answered emails late in "
           "the evening and even at weekends. My sister once told me that I was always at work, even when I was sitting at dinner "
           "with the family. After a while, I felt tired all the time."),
         P("Since then, I have made a few rules for myself. I start and finish work at the same time every day, and I close my laptop "
           "when I finish. I have turned a corner of my bedroom into a small office, so I don't work on the sofa any more. Twice a "
           "week, I work from a café near my house just to be around other people. My company has also started to organise a team "
           "meeting in the office every Friday."),
         P("So, would I go back to the office full-time? Probably not. But if someone asked me for advice, I would say that remote "
           "work is not for everyone. If you need people around you, a mix of home and office might suit you better."),
     ],
     [G('work from home', 'uydan ishlamoq'), G('delighted', 'juda xursand'), G('crowded', 'odam gavjum'),
      G('gain', 'qoʻlga kiritmoq, orttirmoq'), G('concentrate / focus', 'diqqatni jamlamoq'), G('chat', 'gaplashmoq, suhbatlashmoq'),
      G('interruption', 'xalaqit, uzilish'), G('loneliness', 'yolgʻizlik'), G('miss', 'sogʻinmoq'),
      G('mix', 'aralashmoq; aralashma'), G('turn something into', '… ni … ga aylantirmoq'), G('organise', 'tashkil qilmoq'),
      G('full-time', 'toʻliq (har kuni), toʻliq ish kuni'), G('suit', 'mos kelmoq')],
     [GN('i12-used-to-would', 'used to: oʻtmishdagi odat', 'I used to have lunch with my colleagues every day'),
      GN('i26-second-conditional', 'Ikkinchi shart gap: if … asked, I would say',
         'if someone asked me for advice, I would say that remote work is not for everyone')],
     [
         tf('The writer used to travel to work by bus.', 'T',
            '«I would no longer have to spend an hour on a crowded bus every morning» — avval avtobusda yurgan.', 0, ng=True),
         tf('The writer found it easier to concentrate in the office.', 'F',
            'Aksincha: «I can also concentrate better» uyda; ofisda «it was hard to focus».', 1, ng=True),
         tf('The writer misses talking to colleagues over lunch.', 'T',
            '«I used to have lunch with my colleagues every day, and I miss those conversations».', 2, ng=True),
         tf('The writer\'s company is planning to close its office.', 'NG',
            'Kompaniya juma kunlari ofisda yigʻilish oʻtkazadi, lekin ofisni yopish rejasi haqida hech narsa aytilmagan.', 4, ng=True),
         ch('What has been the biggest problem of working from home for the writer?',
            ['noise at home', 'feeling lonely', 'a slow internet connection'], 1,
            '«The biggest one for me has been loneliness.»', 2),
         ch('Why does the writer sometimes work in a café?',
            ['because the internet at home is slow', 'to be around other people', 'because the company pays for it'], 1,
            '«I work from a café near my house just to be around other people».', 4),
         ch('What is the writer\'s opinion about remote work?',
            ['Everyone should work from home.', 'It suits some people but not others.',
             'Offices are always better.'], 1,
            '«remote work is not for everyone» — hammaga ham mos emas; baʼzilarga aralash variant yaxshiroq.', 5),
         gap('Without the journey, the writer has gained about ___ every day.', ['two hours', '2 hours'],
             '«I have gained about two hours every day».', 1, 2),
         gap('The writer has turned a corner of the ___ into a small office.', 'bedroom',
             '«I have turned a corner of my bedroom into a small office».', 4, 2),
     ])

text(B, 'b1-24-startup', 'Startap hikoyasi', 'A Startup Story', 'B1', 'story', WORK,
     'Bu hikoya fermerlar mahsulotini shaharga yetkazib beradigan kichik startap haqida. Oʻqishdan oldin oʻylab koʻring: yangi biznes boshlaganda qanday qiyinchiliklar boʻlishi mumkin?',
     [
         P("Three years ago, Malika and her friend Bekzod were both working in offices in Tashkent. Malika's parents grew fruit and "
           "vegetables in a village in the Fergana Valley, and every summer she heard the same complaint: traders paid farmers very "
           "low prices, while people in the city paid a lot for the same tomatoes. Malika wondered if there was a way to connect "
           "farmers directly with customers."),
         P("The idea was simple. Customers would order a box of fresh seasonal fruit and vegetables online, and the box would be "
           "delivered to their door within a day of being picked. Bekzod, who had studied programming, built a basic website in his "
           "free time. They borrowed a small van from Malika's uncle and started with twelve customers, most of whom were their own "
           "friends and colleagues."),
         P("The first months were exciting but exhausting. They both kept their office jobs, so they packed boxes late at night and "
           "delivered them at weekends. Then, in their first summer, the van broke down on a hot day, and a whole load of strawberries "
           "was ruined before it reached the city. They lost money and several customers. Bekzod admits that he nearly gave up. "
           "\"If Malika hadn't been so stubborn, I would have stopped,\" he says."),
         P("Instead of giving up, they learned from their mistakes. They invested in a second-hand refrigerated van, and they started "
           "to plan their routes more carefully so that the fruit spent less time on the road. They also began to send customers a "
           "short message with the name of the farmer who had grown their vegetables. Customers loved this personal touch, and many "
           "of them told their friends."),
         P("Today, the business works with around forty farming families and delivers several hundred boxes a week. Malika and Bekzod "
           "have left their office jobs and employ eight people. Farmers receive better prices than they did from traders, and "
           "customers know exactly where their food comes from."),
         P("Their advice to young people who want to start a business is practical: start small, listen to your customers, and do "
           "not be afraid of failure. \"Every problem taught us something,\" says Malika. \"The broken van was the best lesson we "
           "ever had.\""),
     ],
     [G('complaint', 'shikoyat'), G('trader', 'savdogar, vositachi (chayqovchi)'), G('connect', 'bogʻlamoq'),
      G('seasonal', 'mavsumiy'), G('borrow', 'qarzga olmoq'), G('exhausting', 'juda charchatadigan'),
      G('break down / broke down', 'buzilib qolmoq'), G('ruin', 'buzmoq, yaroqsiz qilmoq'),
      G('give up / gave up', 'taslim boʻlmoq, voz kechmoq'), G('stubborn', 'qaysar, oʻjar'),
      G('invest in', '… ga sarmoya kiritmoq'), G('second-hand', 'ishlatilgan'),
      G('refrigerated', 'sovutgichli'), G('employ', 'ishga olmoq')],
     [GN('i27-third-conditional', 'Uchinchi shart gap: If … hadn\'t been …, I would have …',
         "If Malika hadn't been so stubborn, I would have stopped"),
      GN('i11-past-perfect', 'Past Perfect: who had grown', 'the name of the farmer who had grown their vegetables')],
     [
         tf('Malika\'s parents were farmers.', 'T',
            '«Malika\'s parents grew fruit and vegetables in a village in the Fergana Valley».', 0, ng=True),
         tf('Bekzod built the website as part of his office job.', 'F',
            'U saytni boʻsh vaqtida qilgan: «built a basic website in his free time».', 1, ng=True),
         tf('In the first months, Malika and Bekzod worked on the business full-time.', 'F',
            '«They both kept their office jobs» — ofisdagi ishlarini tashlamagan.', 2, ng=True),
         tf('They borrowed money from a bank to buy the refrigerated van.', 'NG',
            'Furgon sotib olingani aytilgan, lekin pul qayerdan olingani haqida maʼlumot yoʻq.', 3, ng=True),
         ch('Why did Malika want to start the business?',
            ['She wanted to leave Tashkent.', 'Farmers got low prices while city customers paid a lot.',
             'Her uncle asked her to sell his van.'], 1,
            '«traders paid farmers very low prices, while people in the city paid a lot for the same tomatoes».', 0),
         ch('When Bekzod says Malika was «stubborn», he means that she …',
            ['did not want to give up', 'was often angry with him', 'did not listen to customers'], 0,
            'Bekzod deyarli taslim boʻlgan, lekin Malika qaysar boʻlgani uchun davom etishgan: «If Malika hadn\'t been so stubborn, I would have stopped».', 2),
         hd(3, ['Learning from mistakes', 'A difficult summer', 'Advice for young people'], 0,
            '4-xatboshi «they learned from their mistakes» bilan boshlanadi: yangi furgon, yaxshi yoʻnalishlar, mijozlarga xabar.'),
         gap('Each box was delivered within a day of being ___.', 'picked',
             '«delivered to their door within a day of being picked».', 1, 2),
         gap('Today, Malika and Bekzod employ ___ people.', ['eight', '8'],
             '«have left their office jobs and employ eight people».', 4, 2),
     ])

text(B, 'b1-25-workplace', 'Ish joyida muloqot', 'A Misunderstanding at Work', 'B1', 'dialogue', WORK,
     'Ikki hamkasb — Dilnoza va Timur — hisobot muddati boʻyicha tushunmovchilikni muhokama qiladi. Oʻqishdan oldin oʻylab koʻring: ishda yoki oʻqishda sizda ham shunday holat boʻlganmi?',
     [
         P("Dilnoza: Timur, have you got a minute? The manager asked me this morning why the sales report wasn't ready yesterday. "
           "I thought you were working on it. Timur: Yesterday? I'm sorry, but I was sure the deadline was Friday. That's what I "
           "understood from your email last week."),
         P("Dilnoza: Really? Let me check. Here it is. I wrote that you should send the report by the end of the week, ideally "
           "before the meeting with the regional team. That meeting was on Wednesday, so I meant Wednesday. Timur: I see. But for "
           "me, the end of the week means Friday. I didn't know when the meeting was, because I wasn't invited to it."),
         P("Dilnoza: You're right, I should have written the exact date. I'm afraid I assumed everyone knew about the meeting. "
           "Timur: And I should have asked you if I wasn't sure. To be honest, I noticed the word ideally, but I didn't think it "
           "was important."),
         P("Dilnoza: Well, it's not a disaster. The manager wasn't angry, just a bit surprised. How much of the report have you "
           "finished? Timur: Most of it. I only need to add the figures from the Samarkand office. If they send them today, I can "
           "finish it by tomorrow lunchtime."),
         P("Dilnoza: That's great. I'll call Samarkand myself and ask them to hurry. And I'll explain to the manager that it was my "
           "mistake, not yours. Timur: Thanks, that's kind of you. Maybe we could agree on something for the future? When there is "
           "a deadline, let's always write the day and the date."),
         P("Dilnoza: Good idea. And if something isn't clear, we ask each other straight away, even if the question seems silly. "
           "Timur: Agreed. I'll send you the report as soon as it's ready, and next time I'll put the deadline in my calendar the "
           "moment I get the email."),
     ],
     [G('have you got a minute?', 'bir daqiqangiz bormi?'), G('deadline', 'muddat, oxirgi sana'),
      G('ideally', 'eng yaxshisi, iloji boʻlsa'), G('regional', 'hududiy, viloyat (boʻlimi)'), G('invite', 'taklif qilmoq'),
      G('I\'m afraid', 'afsuski (muloyim ohangda)'), G('assume', 'oʻzicha deb oʻylamoq, taxmin qilmoq'),
      G('to be honest', 'rostini aytsam'), G('disaster', 'falokat, ofat'), G('figures', 'raqamlar, koʻrsatkichlar'),
      G('hurry', 'shoshilmoq'), G('agree on', '… ga kelishmoq'), G('straight away', 'darhol'), G('silly', 'arzimas, ahmoqona')],
     [GN('i23-should-have-neednt-have', 'should have + V3: oʻtmishdagi xato', 'I should have written the exact date.'),
      GN('i16-future-time-clauses', 'Kelasi zamon payt ergash gapi: as soon as', "I'll send you the report as soon as it's ready")],
     [
         tf('Timur thought the deadline was Friday.', 'T',
            '«I was sure the deadline was Friday».', 0, ng=True),
         tf('Timur has worked in the company for less than a year.', 'NG',
            'Timur qancha vaqtdan beri ishlashi haqida dialogda hech narsa aytilmagan.', 0, ng=True),
         tf('Timur had been invited to the meeting with the regional team.', 'F',
            '«I wasn\'t invited to it» — uni yigʻilishga taklif qilishmagan.', 1, ng=True),
         tf('The manager was very angry about the late report.', 'F',
            '«The manager wasn\'t angry, just a bit surprised».', 3, ng=True),
         ch('What was the main cause of the misunderstanding?',
            ['Timur forgot about the report.', 'The email did not give an exact date.',
             'The manager changed the deadline.'], 1,
            'Dilnoza tan oladi: «I should have written the exact date» — emailda aniq sana yoʻq edi.', 2),
         ch('What does Dilnoza offer to do?',
            ['finish the report herself', 'tell the manager that the mistake was hers', 'move the meeting to Friday'], 1,
            '«I\'ll explain to the manager that it was my mistake, not yours».', 4),
         ch('In the last paragraph, «straight away» means …',
            ['immediately', 'in a straight line', 'after some time'], 0,
            'Tushunarsiz narsa boʻlsa, «darhol» soʻrashga kelishishadi: «we ask each other straight away».', 5),
         gap('Timur still needs to add the ___ from the Samarkand office.', 'figures',
             '«I only need to add the figures from the Samarkand office».', 3, 2),
         gap('In future, they will always write the day and the ___ of a deadline.', 'date',
             '«let\'s always write the day and the date».', 4, 2),
     ])
