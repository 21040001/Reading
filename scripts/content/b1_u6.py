"""B1 · 6-boʻlim: Media (5 ta matn)"""
from lib import *

B = 'b1'

# ---------------------------------------------------------------- 26
text(B, 'b1-26-fake-news', 'Yolgʻon yangiliklarni tanish', 'How to Spot False News', 'B1', 'article',
     L('Media savodxonligi', 'Media literacy'),
     'Bu maqola internetdagi yolgʻon yangiliklarni qanday tanish haqida. Oʻqishdan oldin oʻylab koʻring: '
     'siz biror xabarni boshqalarga yuborishdan oldin uni tekshirasizmi?',
     [
         P("Every day, millions of messages, photos and videos are shared online. Many of them are useful, but some are "
           "simply not true. False news can spread very quickly, because people often share a surprising story before they "
           "check it. The good news is that you do not need to be an expert to protect yourself. A few simple questions can "
           "help you decide whether a story deserves your trust."),
         P("First, look at the source. Who has published the story? A well-known newspaper or television channel usually has "
           "editors who check the facts before they publish anything. An unknown website with a strange name, or a message "
           "that was forwarded to you by a friend of a friend, should make you more careful. If you cannot find out who wrote "
           "the story, that is already a warning sign."),
         P("Second, check the date. Sometimes an old story is shared again as if it had just happened. A photo of a flood from "
           "ten years ago, for example, may suddenly appear with a new caption about this week's weather. It is also a good "
           "idea to search for the same news on other websites. If a really important event has taken place, several different "
           "news outlets will be reporting it. If only one website mentions it, you should wait before you believe it."),
         P("Third, pay attention to your feelings. False stories are often written to make readers angry, scared or excited. "
           "Headlines in capital letters with lots of exclamation marks, or words such as shocking and unbelievable, are "
           "designed to make you click and share quickly. When a headline makes you feel very emotional, stop for a moment "
           "and read the whole article calmly."),
         P("Finally, remember that pictures can be edited too. Modern software makes it easy to change a photo or to put a "
           "person into a place where they have never been. Look for strange shadows, unclear edges, or hands and faces that "
           "look unnatural. If you are not sure, it is better not to share the story at all. Each of us can help to stop false "
           "news simply by thinking before we press the share button."),
     ],
     [G('spread', 'tarqalmoq'), G('deserve', 'loyiq boʻlmoq, arzimoq'), G('source', 'manba'),
      G('publish', 'chop etmoq, eʼlon qilmoq'), G('editor', 'muharrir'), G('forward', '(xabarni) boshqaga joʻnatmoq'),
      G('warning sign', 'ogohlantiruvchi belgi'), G('caption', 'rasm ostidagi yozuv'),
      G('news outlet', 'axborot vositasi, yangilik nashri'), G('headline', 'sarlavha'),
      G('be designed to', '… uchun moʻljallangan boʻlmoq'), G('calmly', 'xotirjam, shoshilmasdan'),
      G('edit', 'tahrirlamoq, oʻzgartirmoq'), G('unnatural', 'gʻayritabiiy, sunʼiy')],
     [GN('i29-passive-basics', 'Majhul nisbat: are shared, can be edited',
         'Every day, millions of messages, photos and videos are shared online.'),
      GN('i05-present-perfect', 'Present Perfect: has taken place',
         'If a really important event has taken place')],
     [
         tf('According to the writer, only experts can protect themselves from false news.', 'F',
            'Aksincha: «you do not need to be an expert» — mutaxassis boʻlish shart emas.', 0, ng=True),
         tf('Well-known newspapers usually have people who check facts before publishing.', 'T',
            '«usually has editors who check the facts before they publish anything».', 1, ng=True),
         tf('The writer once worked as an editor at a newspaper.', 'NG',
            'Matnda muharrirlar haqida umumiy gap bor, lekin muallifning oʻzi qayerda ishlagani aytilmagan.', 1),
         tf('If only one website reports an important event, you can believe it immediately.', 'F',
            '«If only one website mentions it, you should wait before you believe it» — kutish kerak.', 2, ng=True),
         ch('What is the main purpose of the article?',
            ['to explain how journalists make false news', 'to give readers simple ways to check a story',
             'to tell readers to stop using the internet'], 1,
            '1-xatboshi: «A few simple questions can help you decide whether a story deserves your trust» — '
            'maqola oddiy tekshirish usullarini beradi.', 0),
         ch('In paragraph 3, the word «outlets» is closest in meaning to …',
            ['shops that sell newspapers', 'organisations that publish news', 'electric sockets in a wall'], 1,
            '«several different news outlets will be reporting it» — bu yerda yangilik tarqatuvchi tashkilotlar nazarda tutilgan.', 2),
         ch('Why do some headlines use capital letters and exclamation marks?',
            ['to make readers click and share quickly', 'to make the text easier to read', 'to show that editors have checked them'], 0,
            '«are designed to make you click and share quickly».', 3),
         gap('If a headline makes you very emotional, you should stop and read the whole article ___.', 'calmly',
             '«stop for a moment and read the whole article calmly».', 3, 2),
         hd(4, ['Checking photos carefully', 'How to take better pictures', 'Why we should never go online'], 0,
            '5-xatboshi tahrirlangan rasmlarni qanday aniqlash haqida: «pictures can be edited too».'),
     ])

# ---------------------------------------------------------------- 27
text(B, 'b1-27-advertising', 'Reklama siri', 'The Secret of Advertising', 'B1', 'story',
     L('Reklama', 'Advertising'),
     'Bu hikoyada oʻn besh yoshli Malika bir hafta davomida reklamalardagi «hiyla»larni yozib boradi. '
     'Oʻqishdan oldin oʻylab koʻring: siz biror narsani reklama sababli sotib olganmisiz?',
     [
         P("Malika is fifteen, and until last month she had never thought much about advertisements. They were simply there: "
           "on the bus stop near her school, between videos on her phone and on the television in the evening. Then her "
           "teacher, Mr Karimov, gave the class an unusual piece of homework. 'For one week,' he said, 'I want you to collect "
           "adverts and write down every trick you notice.'"),
         P("On the first day, Malika saw a poster for a new sports drink. A famous footballer was holding the bottle and "
           "smiling. 'He probably doesn't even drink it,' she thought. In her notebook she wrote: famous faces. Advertisers use "
           "well-known people because we trust them and want to be like them, so we connect the product with their success."),
         P("The next evening, a television advert for a phone said that the special price was available for three days only. "
           "Her older brother had almost bought a phone the week before for exactly the same reason. Malika realised that a "
           "limited offer makes people hurry. If you have no time to think, you are less likely to ask whether you really need "
           "the thing."),
         P("She also started listening to adverts instead of only watching them. Almost every one had cheerful, catchy music, "
           "and one song stayed in her head for two whole days. Music, she wrote, makes us feel happy, and the advert hopes "
           "that we will remember that feeling when we see the product in a shop."),
         P("The strangest discovery came on her phone. After she had searched for running shoes once, adverts for trainers "
           "appeared everywhere: in her games, on websites and in her social media feed. Malika asked her teacher about it. "
           "He explained that many companies collect information about what we search for and show us adverts that are "
           "targeted at our interests."),
         P("At the end of the week, Malika presented her list to the class. 'I am not saying that all adverts are bad,' she "
           "said. 'Some of them tell us useful things. But now, when I see one, I ask myself what trick it is using.' "
           "Mr Karimov gave her the highest mark in the class."),
     ],
     [G('advertisement', 'reklama (qisqasi: advert)'), G('trick', 'hiyla, nayrang'), G('poster', 'plakat, afisha'),
      G('advertiser', 'reklama beruvchi'), G('connect', 'bogʻlamoq'), G('available', 'mavjud, olish mumkin'),
      G('limited offer', 'cheklangan taklif'), G('hurry', 'shoshilmoq'), G('be likely to', 'ehtimoli bor'),
      G('catchy', 'tez yodda qoladigan (kuy)'), G('discovery', 'kashfiyot, topilma'),
      G('targeted at', '… ga moʻljallangan, yoʻnaltirilgan'), G('feed', 'lenta (ijtimoiy tarmoqda)'),
      G('mark', 'baho')],
     [GN('i11-past-perfect', 'Past Perfect: had searched, had never thought',
         'After she had searched for running shoes once, adverts for trainers appeared everywhere'),
      GN('i29-passive-basics', 'Majhul nisbat: are targeted at',
         'adverts that are targeted at our interests')],
     [
         tf('Mr Karimov asked the students to collect adverts for one week.', 'T',
            '«For one week, I want you to collect adverts».', 0, ng=True),
         tf('The footballer on the poster plays for an Uzbek team.', 'NG',
            'Futbolchi mashhur ekani aytilgan, lekin qaysi jamoada oʻynashi haqida maʼlumot yoʻq.', 1),
         tf('Malika\'s brother bought a phone because of a special price.', 'F',
            '«had almost bought a phone» — «almost» sotib olishiga oz qolgan, lekin olmaganini bildiradi.', 2, ng=True),
         tf('A song from an advert stayed in Malika\'s head for two days.', 'T',
            '«one song stayed in her head for two whole days».', 3, ng=True),
         ch('According to Malika, why do adverts say that an offer is for a short time only?',
            ['to make people hurry and not think too much', 'because the shop will close soon',
             'because the product is old'], 0,
            '«a limited offer makes people hurry. If you have no time to think…».', 2),
         ch('Why did Malika see adverts for trainers everywhere?',
            ['Her brother had bought trainers.', 'She had searched for running shoes.', 'Her teacher had sent them to her.'], 1,
            '«After she had searched for running shoes once, adverts for trainers appeared everywhere».', 4),
         ch('What is Malika\'s final opinion about adverts?',
            ['All adverts are dangerous and should be stopped.',
             'Adverts can be useful, but it is important to notice their tricks.',
             'Only adverts with music are honest.'], 1,
            '«I am not saying that all adverts are bad… But now… I ask myself what trick it is using».', 5),
         gap('Advertisers use famous people because we ___ them and want to be like them.', 'trust',
             '«because we trust them and want to be like them».', 1, 2),
         gap('At the end, Mr Karimov gave Malika the ___ in the class.', 'highest mark',
             '«Mr Karimov gave her the highest mark in the class».', 5, 2),
     ])

# ---------------------------------------------------------------- 28
text(B, 'b1-28-podcasts', 'Podkastlar', 'Podcasts', 'B1', 'blog',
     L('Audio va taʼlim', 'Audio and learning'),
     'Ingliz tilini oʻrganayotgan talaba Jasur oʻz blogida podkastlar haqida yozadi. '
     'Oʻqishdan oldin oʻylab koʻring: siz biror marta podkast tinglaganmisiz?',
     [
         P("Hi everyone, and welcome back to my blog about learning English. Today I want to write about something that has "
           "changed the way I study: podcasts. A year ago, I did not even know what a podcast was. Now I listen to at least "
           "one every day, usually on my way to university."),
         P("For anyone who is new to them, a podcast is a series of audio programmes that you can download or stream on your "
           "phone. Some podcasts are like radio shows, with one host talking about the news. Others are conversations between "
           "two or three people, and some tell long stories in many episodes. There are podcasts about almost everything: "
           "history, football, cooking, science and, of course, languages."),
         P("Why are they so popular? I think the main reason is freedom. You cannot read a book while you are driving or "
           "washing the dishes, but you can listen to a podcast. My mother, who never had time for reading, now listens to "
           "programmes about health while she cooks dinner. People also like the personal feeling of podcasts. When you have "
           "listened to the same hosts for months, they start to feel like friends."),
         P("For English learners, podcasts are a gift. When I started, I chose a podcast made especially for learners. The "
           "hosts spoke slowly and explained difficult words, and every episode came with a transcript, so I could read the "
           "text after listening. If I had started with a normal podcast for native speakers, I would probably have given up "
           "after one week."),
         P("Here is my advice. Choose a topic you really enjoy, because then you will listen more often. Start with short "
           "episodes of ten or fifteen minutes. Listen to each episode twice: the first time for the general idea, the second "
           "time for details. And do not worry if you do not understand everything. My listening has improved more this year "
           "than in three years of school lessons, and I am sure yours can too."),
     ],
     [G('on my way to', '… ga ketayotib, yoʻlda'), G('series', 'turkum, seriya'), G('download', 'yuklab olmoq'),
      G('stream', 'onlayn (yuklamasdan) tinglamoq/koʻrmoq'), G('host', 'boshlovchi'), G('episode', 'son, qism'),
      G('freedom', 'erkinlik'), G('personal', 'shaxsiy, samimiy'), G('gift', 'sovgʻa; katta foyda'),
      G('transcript', 'yozma matn (aytilganlarning)'), G('native speaker', 'ona tili sifatida gapiruvchi'),
      G('give up', 'tashlab qoʻymoq, voz kechmoq'), G('advice', 'maslahat'), G('improve', 'yaxshilanmoq')],
     [GN('i27-third-conditional', 'Uchinchi shart gap: If I had started…, I would have…',
         'If I had started with a normal podcast for native speakers, I would probably have given up after one week.'),
      GN('i05-present-perfect', 'Present Perfect: has changed, has improved',
         'something that has changed the way I study')],
     [
         tf('The writer has listened to podcasts for many years.', 'F',
            '«A year ago, I did not even know what a podcast was» — bir yil oldin podkastni bilmagan ham.', 0, ng=True),
         tf('The writer usually listens to podcasts while travelling to university.', 'T',
            '«usually on my way to university».', 0, ng=True),
         tf('The writer\'s favourite podcast is about football.', 'NG',
            'Futbol faqat mavzular roʻyxatida tilga olingan; muallifning eng yaxshi koʻrgan podkasti aytilmagan.', 1),
         tf('The first podcast the writer used had a transcript for every episode.', 'T',
            '«every episode came with a transcript».', 3, ng=True),
         ch('According to the writer, what is the main reason why podcasts are popular?',
            ['They cost nothing.', 'You can listen while doing other things.', 'They are shorter than radio shows.'], 1,
            '«the main reason is freedom. You cannot read a book while you are driving… but you can listen to a podcast».', 2),
         ch('What does the writer mean when saying that hosts «start to feel like friends»?',
            ['Listeners often meet the hosts in real life.', 'Listeners feel close to hosts they hear regularly.',
             'The hosts are the writer\'s classmates.'], 1,
            '«When you have listened to the same hosts for months» — oylab tinglagach, ular yaqin kishidek tuyuladi.', 2),
         ch('Why does the writer suggest listening to each episode twice?',
            ['to understand the general idea first and then the details', 'to learn the episode by heart',
             'because the episodes are very short'], 0,
            '«the first time for the general idea, the second time for details».', 4),
         gap('The writer advises beginners to start with short ___.', 'episodes',
             '«Start with short episodes of ten or fifteen minutes».', 4, 2),
         hd(1, ['What a podcast is', 'How to record your own podcast', 'The history of radio'], 0,
            '2-xatboshi podkast nima ekanini tushuntiradi: «a podcast is a series of audio programmes…».'),
     ])

# ---------------------------------------------------------------- 29
text(B, 'b1-29-film-review', 'Kino tanqidi', 'Film Review: The Last Apricot Tree', 'B1', 'article',
     L('Kino', 'Cinema'),
     'Bu — toʻqima (oʻylab topilgan) oʻzbek filmi haqidagi taqriz. Oʻqishdan oldin oʻylab koʻring: '
     'filmni koʻrishga borishdan oldin siz uning haqida fikr-mulohazalarni oʻqiysizmi?',
     [
         P("The Last Apricot Tree, the second feature film by the young director Dilafruz Tojimurodova, arrived in cinemas this "
           "month, and it is already one of the most talked-about Uzbek films of the year. I went to see it with low "
           "expectations, because family dramas often feel too sweet. I was wrong. This is a warm, funny and sometimes "
           "painful film that stayed with me long after I had left the cinema."),
         P("The story is simple. Bekzod, a twelve-year-old boy from Tashkent who spends most of his time on his phone, is "
           "sent to his grandfather's village in the Fergana Valley for the summer. At first he is bored and angry. There is "
           "no internet, and his grandfather, Rustam ota, gets up at five every morning to work in his old apricot garden. "
           "Then Bekzod learns that a businessman wants to buy the garden and build a hotel on it."),
         P("What makes the film special is the relationship between the boy and the old man. Rustam ota is played by a "
           "veteran actor who says very little, but his face tells us everything. In one wonderful scene, he teaches Bekzod "
           "how to dry apricots on the roof, and neither of them speaks for almost two minutes. The young actor who plays "
           "Bekzod is also natural and believable, which is rare for a child in his first role."),
         P("The film is also beautiful to look at. The camera loves the valley: the morning light on the mountains, the "
           "green rows of trees, the busy local bazaar. You can almost smell the fruit. The music, played mostly on "
           "traditional instruments, is used carefully and never feels too loud."),
         P("However, the film is not perfect. The middle part is too slow, and a few scenes with the businessman feel like a "
           "cartoon. I also guessed the ending about half an hour before it came, although I will not tell you what it is. "
           "Even so, I would recommend The Last Apricot Tree to anyone who has ever spent a summer with their grandparents. "
           "I give it four stars out of five."),
     ],
     [G('feature film', 'badiiy film'), G('director', 'rejissyor'), G('expectations', 'kutilmalar, umidlar'),
      G('drama', 'drama (janr)'), G('painful', 'ogʻriqli, alamli'), G('be bored', 'zerikmoq'),
      G('relationship', 'munosabat'), G('veteran', 'tajribali, faxriy'), G('scene', 'sahna, lavha'),
      G('believable', 'ishonarli, hayotiy'), G('role', 'rol'), G('row', 'qator'),
      G('guess', 'taxmin qilmoq, topmoq'), G('recommend', 'tavsiya qilmoq')],
     [GN('i53-who-which-that', 'Nisbiy gap: who spends…',
         'a twelve-year-old boy from Tashkent who spends most of his time on his phone'),
      GN('i29-passive-basics', 'Majhul nisbat: is played by, is sent to',
         'Rustam ota is played by a veteran actor')],
     [
         tf('Before seeing the film, the reviewer expected to enjoy it very much.', 'F',
            '«I went to see it with low expectations» — kutilmalari past boʻlgan.', 0, ng=True),
         tf('The businessman in the film wants to build a hotel on the garden.', 'T',
            '«a businessman wants to buy the garden and build a hotel on it».', 1, ng=True),
         tf('The boy who plays Bekzod has acted in many films before.', 'F',
            '«a child in his first role» — bu uning birinchi roli.', 2, ng=True),
         tf('Dilafruz Tojimurodova also wrote the music for the film.', 'NG',
            'Musiqa haqida «played mostly on traditional instruments» deyilgan, kim yozgani aytilmagan.', 3),
         ch('What does the reviewer like most about the film?',
            ['the relationship between the boy and his grandfather', 'the scenes with the businessman',
             'the surprising ending'], 0,
            '«What makes the film special is the relationship between the boy and the old man».', 2),
         ch('In paragraph 3, the word «believable» means …',
            ['realistic and easy to believe', 'very famous', 'difficult to understand'], 0,
            '«natural and believable» — tabiiy va ishonarli, yaʼni hayotiy oʻynagan.', 2),
         ch('What is one criticism the reviewer makes?',
            ['The music is too loud.', 'The middle part is too slow.', 'The valley does not look beautiful.'], 1,
            '«However, the film is not perfect. The middle part is too slow». Musiqa esa «never feels too loud».', 4),
         gap('In one scene, Rustam ota teaches Bekzod how to dry apricots on the ___.', 'roof',
             '«how to dry apricots on the roof».', 2, 2),
         gap('The reviewer gives the film four ___ out of five.', 'stars',
             '«I give it four stars out of five».', 4, 2),
     ])

# ---------------------------------------------------------------- 30
text(B, 'b1-30-screen-time', 'Ekran vaqti', 'Screen Time', 'B1', 'dialogue',
     L('Raqamli hayot', 'Digital life'),
     'Bu suhbatda bir oila telefon va ekranlardan foydalanish qoidalarini muhokama qiladi. '
     'Oʻqishdan oldin oʻylab koʻring: sizning uyingizda telefon uchun qoidalar bormi?',
     [
         P("Gulnora: Aziz, it is almost midnight and I can still see light under your door. Have you been on your phone all "
           "evening? Aziz: Not all evening, Mum. I finished my homework first, and then I was just watching a few videos. "
           "Everyone in my class does it."),
         P("Gulnora: That is exactly what worries me. You were very tired this morning, and your teacher told me that you had "
           "fallen asleep in class last week. Doctors say that using a bright screen late at night can make it harder to fall "
           "asleep. Aziz: But I need my phone. We talk about homework in our class group, and I use it to learn English too."),
         P("Akmal: You are both right, in a way. Screens are not bad in themselves. Aziz learns a lot online, and I use a "
           "computer for work all day. The problem starts when we cannot stop. Gulnora: And it is not only about sleep. Have "
           "you noticed that he cannot read a book for ten minutes without checking his messages? Many teachers say that "
           "constant notifications make it difficult to concentrate."),
         P("Aziz: But Dad checks his phone at dinner all the time! Akmal: That is true, and I am not proud of it. So perhaps "
           "we need rules for the whole family, not only for you. If we all agreed on some rules, it would be fairer. "
           "What do you think?"),
         P("Gulnora: All right. First, no phones at the dinner table, for anyone. Second, all phones stay in the kitchen after "
           "ten o'clock at night. Aziz: And on Saturdays, can I play games for longer if I have finished my homework? "
           "Akmal: Yes, as long as you also spend some time outside. We could go cycling together on Sunday mornings."),
         P("Aziz: Fine. But if Dad breaks a rule, he has to wash the dishes for a week. Gulnora: Agreed! Let's try it for a "
           "month and then talk again about what works and what does not."),
     ],
     [G('almost', 'deyarli'), G('worry', 'xavotirga solmoq, tashvishlantirmoq'), G('fall asleep', 'uxlab qolmoq'),
      G('bright', 'yorqin'), G('in a way', 'maʼlum maʼnoda'), G('in themselves', 'oʻz-oʻzidan, aslida'),
      G('constant', 'doimiy, toʻxtovsiz'), G('notification', 'bildirishnoma'), G('concentrate', 'diqqatni jamlamoq'),
      G('be proud of', '… bilan faxrlanmoq'), G('agree on', '… ga kelishmoq'), G('fair', 'adolatli'),
      G('as long as', '… sharti bilan, faqat … boʻlsa'), G('break a rule', 'qoidani buzmoq')],
     [GN('i26-second-conditional', 'Ikkinchi shart gap: If we agreed…, it would be…',
         'If we all agreed on some rules, it would be fairer.'),
      GN('i62-unless-as-long-as', 'as long as — shart bilan',
         'as long as you also spend some time outside')],
     [
         tf('Aziz did his homework before he started watching videos.', 'T',
            '«I finished my homework first, and then I was just watching a few videos».', 0, ng=True),
         tf('Aziz has never fallen asleep at school.', 'F',
            'Oʻqituvchi aytgan: «you had fallen asleep in class last week».', 1, ng=True),
         tf('Akmal thinks that screens are bad in themselves.', 'F',
            'Akmal aksini aytadi: «Screens are not bad in themselves».', 2, ng=True),
         tf('Aziz has his own laptop.', 'NG',
            'Aziz telefon ishlatishi aytilgan; uning shaxsiy noutbuki bor-yoʻqligi haqida maʼlumot yoʻq.', 2),
         ch('Which sentence best describes Akmal\'s opinion about screens?',
            ['Screens should not be used at home at all.',
             'Screens are useful, but the problem is when we cannot stop using them.',
             'Teenagers need more time on their phones.'], 1,
            '«Screens are not bad in themselves… The problem starts when we cannot stop».', 2),
         ch('Why does Akmal suggest rules for the whole family?',
            ['because Aziz asked for them', 'because he also uses his phone too much at dinner',
             'because the school told him to'], 1,
            'Aziz: «Dad checks his phone at dinner all the time!» Akmal: «That is true… So perhaps we need rules for the whole family».', 3),
         ch('What will happen if Aziz\'s father breaks a rule?',
            ['He will lose his phone for a week.', 'He will wash the dishes for a week.', 'He will cook dinner on Sunday.'], 1,
            '«if Dad breaks a rule, he has to wash the dishes for a week».', 5),
         gap('After ten o\'clock at night, all phones stay in the ___.', 'kitchen',
             '«all phones stay in the kitchen after ten o\'clock at night».', 4, 2),
         gap('Aziz can play games for longer on Saturdays as long as he also spends some time ___.', 'outside',
             '«as long as you also spend some time outside».', 4, 2),
     ])
