"""B1 · 1-boʻlim: Shaxsiy hikoyalar (5 ta matn)"""
from lib import *

B = 'b1'

text(B, 'b1-01-study-abroad', 'Chet elda oʻqish', 'My First Months Abroad', 'B1', 'story',
     L('Taʼlim', 'Education'),
     'Nodira ismli talaba chet elda oʻqishning birinchi oylari haqida hikoya qiladi. '
     'Oʻqishdan oldin oʻylab koʻring: uydan uzoqda yashashning eng qiyin tomoni nima deb oʻylaysiz?',
     [
         P("My name is Nodira, and when I received my letter from the university, I was so happy that I cried. "
           "I had dreamed about studying abroad since I was fifteen, and now I was going to study computer science "
           "in a small university town in England. My parents were proud of me, but my mother was also worried. "
           "She asked me who would cook for me. I laughed and told her that I would be fine."),
         P("The first weeks were much harder than I had expected. Although I had studied English for years, people "
           "spoke very fast, and I often could not understand jokes or local expressions. In lectures, I recorded "
           "everything on my phone and listened again in the evening. The food was another problem. Everything seemed "
           "to taste the same, and I missed my mother's plov more than I can say. I even tried to cook it myself, but "
           "without the right rice it was a disaster."),
         P("The hardest part, however, was homesickness. In November, the days became short and grey, and I often sat "
           "alone in my room. I called my family every evening, but after each call I felt even lonelier. One day my "
           "flatmate, a girl from Brazil, knocked on my door and invited me to a meeting of the international students' "
           "club. I did not want to go, but she would not take no for an answer."),
         P("That evening changed everything. I met students from more than twenty countries, and many of them were "
           "having the same problems as me. We started to cook dinner together every Friday. Each week, someone "
           "prepared a dish from their home country. When it was my turn, I made somsa, and everyone asked for the "
           "recipe. For the first time, I felt proud to share my culture instead of just missing it."),
         P("Now I am in my second year, and I have learned a lot, not only about computers. I have learned that it is "
           "normal to feel lost at first and that asking for help is not a weakness. If a friend asked me for advice "
           "before going abroad, I would tell them three things: practise listening, not only speaking; learn to cook "
           "a few simple dishes; and say yes to invitations, even when you would prefer to stay at home."),
     ],
     [G('receive', 'olmoq, qabul qilmoq'), G('abroad', 'chet elda, xorijda'), G('be proud of', '… bilan faxrlanmoq'),
      G('expect', 'kutmoq, taxmin qilmoq'), G('local expressions', 'mahalliy iboralar'), G('lecture', 'maʼruza'),
      G('homesickness', 'uyni (vatanni) sogʻinish'), G('lonely', 'yolgʻiz, tanho'), G('flatmate', 'kvartiradosh'),
      G('take no for an answer', '«yoʻq» javobini qabul qilmoq (koʻpincha inkorda: koʻndirmaguncha qoʻymaslik)'),
      G('turn', 'navbat'), G('recipe', 'retsept, tayyorlash usuli'), G('weakness', 'zaiflik, ojizlik'),
      G('invitation', 'taklif')],
     [GN('i11-past-perfect', 'Past Perfect: had dreamed, had expected',
         'I had dreamed about studying abroad since I was fifteen'),
      GN('i26-second-conditional', 'Ikkinchi shart gap: If a friend asked …, I would tell …',
         'If a friend asked me for advice before going abroad, I would tell them three things')],
     [
         tf('Nodira had wanted to study abroad since she was a teenager.', 'T',
            '«I had dreamed about studying abroad since I was fifteen» — 15 yoshidan beri orzu qilgan.', 0, ng=True),
         tf('From the start, Nodira found it easy to understand people in England.', 'F',
            'Aksincha: «people spoke very fast, and I often could not understand jokes or local expressions».', 1, ng=True),
         tf("Nodira's flatmate was also studying computer science.", 'NG',
            'Kvartiradoshi Braziliyadan ekani aytilgan, lekin u nima oʻqishi haqida maʼlumot yoʻq.', 2, ng=True),
         tf('Nodira phoned her family every evening.', 'T',
            '«I called my family every evening» — har kuni kechqurun qoʻngʻiroq qilgan.', 2, ng=True),
         ch('Why did Nodira record her lectures?',
            ['to send them to her family', 'because she could not always understand fast speech',
             'because her teachers asked her to'], 1,
            '2-xatboshi: odamlar juda tez gapirgan va u ularni har doim ham tushunmagan, shuning uchun «I recorded everything on my phone and listened again in the evening».', 1),
         ch('What does «she would not take no for an answer» mean in paragraph 3?',
            ['She accepted my answer quickly.', 'She insisted that I should come.', 'She did not ask me anything.'], 1,
            'Nodira borishni xohlamagan, lekin kvartiradoshi «yoʻq» javobini qabul qilmagan — yaʼni qatʼiy turib olgan.', 2),
         hd(3, ['A dinner that went wrong', 'Finding people who understood', 'Learning to cook plov'], 1,
            '4-xatboshi: Nodira «many of them were having the same problems as me» — oʻzini tushunadigan odamlarni topgan.'),
         gap('Nodira tried to cook plov, but without the right ___ it was a disaster.', 'rice',
             '«without the right rice it was a disaster».', 1, 2),
         ch('Which piece of advice does Nodira give?',
            ['Speak as much as possible and do not worry about listening.',
             'Practise listening and accept invitations.', 'Stay at home and focus only on studying.'], 1,
            '5-xatboshi: «practise listening, not only speaking … say yes to invitations».', 4),
     ])

text(B, 'b1-02-mountain', 'Chimyon togʻlarida bir kun', 'A Day in the Chimgan Mountains', 'B1', 'blog',
     L('Sayohat', 'Travel'),
     'Bu blogda muallif doʻstlari bilan Toshkent yaqinidagi Chimyon togʻlariga qilgan piyoda sayohati haqida yozadi. '
     'Oʻqishdan oldin oʻylab koʻring: togʻga chiqish uchun nimalarni olib borish kerak?',
     [
         P("Last Saturday, my friends and I finally did something we had planned for months: a hike in the Chimgan "
           "mountains. Chimgan is in the Tashkent region, less than two hours by car from the city, so it is a popular "
           "place for weekend trips. In winter, people go there to ski, but we wanted to see the mountains in late "
           "spring, when the slopes are green and covered with wild flowers."),
         P("We left Tashkent at six in the morning, because our guide, Bekzod, had warned us that the afternoon sun "
           "could be very strong. We started walking from the Beldersay area, where there are ski lifts. The path went "
           "up slowly at first, through small trees and fields of red poppies. Bekzod told us to walk at our own speed "
           "and to drink water often, even if we did not feel thirsty."),
         P("After about two hours, the path became steep and rocky, and I started to regret my heavy backpack. I had "
           "packed far too many things, including a big book that I never opened. My friend Laylo, who goes hiking "
           "almost every month, had brought only water, some bread, dried apricots and a warm jacket. She laughed at "
           "me, but she also carried my book for the last part of the climb."),
         P("When we reached the ridge, I forgot about my tired legs. Below us, we could see the valley, the small "
           "villages and, further away, the bright blue water of the Charvak reservoir. It was windy and much colder "
           "than in the city, so we were glad that Bekzod had made us bring jackets. We did not climb to the top of "
           "Big Chimgan, which is over three thousand metres high. Bekzod said that it should only be attempted by "
           "experienced hikers."),
         P("If you are planning a similar trip, here is my advice. Go with someone who knows the mountains well, start "
           "early, and check the weather before you leave, because it can change quickly. Wear good shoes, and pack "
           "light. And please take your rubbish home with you: the mountains are beautiful because people have looked "
           "after them. I am already planning my next hike, and this time my backpack will be much lighter!"),
     ],
     [G('hike', 'piyoda sayohat (togʻda, tabiatda)'), G('slope', 'qiyalik, yonbagʻir'),
      G('guide', 'yoʻlboshlovchi, gid'), G('warn', 'ogohlantirmoq'), G('thirsty', 'chanqagan'),
      G('steep', 'tik'), G('regret', 'afsuslanmoq, pushaymon boʻlmoq'), G('backpack', 'ryukzak, orqa sumka'),
      G('ridge', 'togʻ tizmasi, qir'), G('valley', 'vodiy'), G('reservoir', 'suv ombori'),
      G('attempt', 'urinib koʻrmoq, harakat qilmoq'), G('experienced', 'tajribali'), G('rubbish', 'axlat, chiqindi')],
     [GN('i55-non-defining', 'Qoʻshimcha maʼlumot beruvchi ergash gap: Laylo, who …',
         'My friend Laylo, who goes hiking almost every month, had brought only water'),
      GN('i30-passive-tenses', 'Modal + majhul nisbat: should be attempted',
         'it should only be attempted by experienced hikers')],
     [
         tf('It takes less than two hours to drive from Tashkent to Chimgan.', 'T',
            '«less than two hours by car from the city».', 0, ng=True),
         tf('The group started their hike in the afternoon.', 'F',
            'Ular ertalab soat oltida yoʻlga chiqqan: «We left Tashkent at six in the morning».', 1, ng=True),
         tf('Laylo had been to Chimgan many times before this trip.', 'NG',
            '«goes hiking almost every month» deyilgan, lekin aynan Chimyonga necha marta borgani aytilmagan.', 2, ng=True),
         tf('The writer read the book during the trip.', 'F',
            'Muallif kitobni ochmagan ham: «a big book that I never opened».', 2, ng=True),
         ch('Why did the group leave Tashkent early in the morning?',
            ['to avoid the strong afternoon sun', 'to see the ski lifts working', 'to meet Laylo in Beldersay'], 0,
            'Gid ogohlantirgan: «the afternoon sun could be very strong».', 1),
         ch('In paragraph 3, «regret» is closest in meaning to …',
            ['feel sorry about', 'feel proud of', 'forget about'], 0,
            'Ryukzak ogʻir boʻlgani uchun muallif uni olganidan afsuslangan — «regret» = afsuslanmoq.', 2),
         ch('Why did the group not climb to the top of Big Chimgan?',
            ['The weather was too bad.', 'Their guide said it was only for experienced hikers.',
             'The path to the top was closed.'], 1,
            '«Bekzod said that it should only be attempted by experienced hikers».', 3),
         gap('Laylo brought water, some bread, dried ___ and a warm jacket.', 'apricots',
             '«had brought only water, some bread, dried apricots and a warm jacket».', 2, 2),
         gap('From the ridge, the writer could see the bright blue water of the Charvak ___.', 'reservoir',
             '«the bright blue water of the Charvak reservoir».', 3, 2),
     ])

text(B, 'b1-03-two-languages', 'Ikki tilda oʻsish', 'Growing Up with Two Languages', 'B1', 'dialogue',
     L('Til va oila', 'Language and family'),
     'Maktab radiosida boshlovchi Madina ikki tilda — oʻzbek va rus tillarida soʻzlashib oʻsgan oʻquvchi Temur bilan suhbatlashadi. '
     'Oʻqishdan oldin oʻylab koʻring: bolalikdan ikki tilni bilishning qanday foydasi bor?',
     [
         P("Madina: Today on our school radio we are talking to Timur, a tenth-grade student who grew up with two "
           "languages. Timur, which languages do you speak at home? "
           "Timur: Both Uzbek and Russian. My father's family is Uzbek, and my mother grew up in a Russian-speaking "
           "family in Tashkent. When I was born, my parents decided that each of them would speak to me only in their "
           "own language. So my father always spoke Uzbek to me, and my mother always spoke Russian."),
         P("Madina: Did that ever confuse you? "
           "Timur: My parents say that I mixed the two languages a lot when I was three or four. I used to start a "
           "sentence in Uzbek and finish it in Russian. They were a bit worried, but our doctor told them that this was "
           "normal for children who learn two languages and that it usually happens less as they grow older. She was right. By the "
           "time I started school, I could keep the languages apart."),
         P("Madina: What is the best thing about being bilingual? "
           "Timur: For me, it is that I can talk to everyone in my family. My grandmother on my father's side lives in a "
           "village near Andijan and speaks only Uzbek, while my mother's parents prefer Russian. At family "
           "celebrations, I often translate jokes from one side of the table to the other. Some jokes are impossible to "
           "translate, but people laugh anyway!"),
         P("Madina: Have there been any difficulties? "
           "Timur: Yes. For a few years, my Uzbek writing was weaker than my Russian, because I had read more books in "
           "Russian. When I was in the sixth grade, I got a bad mark for an Uzbek essay, and I felt really embarrassed. "
           "After that, my father and I started reading Uzbek stories together every weekend. Now I write well in both "
           "languages, and I am learning English as my third language."),
         P("Madina: What would you say to parents who want to raise bilingual children? "
           "Timur: Be patient and be consistent. Children need to hear each language every day, in real conversations, "
           "not only in lessons. And never make a child feel ashamed of mixing languages. If my parents had laughed at "
           "me when I was small, I might have stopped speaking one of the languages completely."),
     ],
     [G('bilingual', 'ikki tilli, ikki tilda soʻzlashuvchi'), G('decide', 'qaror qilmoq'),
      G('confuse', 'chalkashtirmoq, adashtirmoq'), G('mix', 'aralashtirmoq'),
      G('keep apart', 'bir-biridan ajratib turmoq'), G('prefer', 'afzal koʻrmoq'),
      G('celebration', 'bayram, tantana'), G('translate', 'tarjima qilmoq'), G('impossible', 'imkonsiz'),
      G('mark', 'baho'), G('embarrassed', 'xijolat boʻlgan, uyalgan'), G('raise', '(bolani) tarbiyalamoq, oʻstirmoq'),
      G('consistent', 'izchil, bir xil tartibda'), G('ashamed', 'uyalgan, sharmanda boʻlgan')],
     [GN('i12-used-to-would', 'used to: oʻtmishdagi odat',
         'I used to start a sentence in Uzbek and finish it in Russian'),
      GN('i27-third-conditional', 'Uchinchi shart gap: If … had laughed, I might have stopped',
         'If my parents had laughed at me when I was small, I might have stopped speaking one of the languages completely')],
     [
         tf("Timur's mother grew up in a Russian-speaking family.", 'T',
            '«my mother grew up in a Russian-speaking family in Tashkent».', 0, ng=True),
         tf('When Timur was a baby, each parent spoke both languages to him.', 'F',
            'Har biri faqat oʻz tilida gapirgan: «each of them would speak to me only in their own language».', 0, ng=True),
         tf("Timur's mother can speak Uzbek well.", 'NG',
            'Onasi Timurga rus tilida gapirgani aytilgan, lekin u oʻzbek tilini bilish-bilmasligi haqida maʼlumot yoʻq.', 0, ng=True),
         tf('Timur had stopped mixing the two languages before he started school.', 'T',
            '«By the time I started school, I could keep the languages apart».', 1, ng=True),
         ch('In paragraph 2, «keep the languages apart» means …',
            ['use each language separately, without mixing', 'forget one of the languages', 'speak only one language at school'], 0,
            'Avval tillarni aralashtirgan, keyin esa ularni ajrata olgan — yaʼni aralashtirmasdan ishlatgan.', 1),
         gap('At family celebrations, Timur often translates ___ from one side of the table to the other.', 'jokes',
             '«I often translate jokes from one side of the table to the other».', 2, 2),
         ch("Why was Timur's Uzbek writing weaker for a few years?",
            ['He had read more books in Russian.', 'His Uzbek teacher was very strict.', 'Nobody spoke Uzbek at home.'], 0,
            '«because I had read more books in Russian».', 3),
         gap('After the bad mark, Timur and his father read Uzbek stories together every ___.', 'weekend',
             '«my father and I started reading Uzbek stories together every weekend».', 3, 2),
         ch("What is the main idea of Timur's advice to parents?",
            ['Send children to language lessons as early as possible.',
             'Use both languages every day, be patient and do not shame children for mixing.',
             'Speak only one language at home to avoid confusion.'], 1,
            '5-xatboshi: «Be patient and be consistent … every day, in real conversations … never make a child feel ashamed».', 4),
     ])

text(B, 'b1-04-career-change', 'Kasbni oʻzgartirish', 'From Numbers to Bread', 'B1', 'biography',
     L('Ish va kasb', 'Work and careers'),
     'Bu matn 35 yoshida buxgalterlikdan novvoylikka oʻtgan ayol haqida. '
     'Oʻqishdan oldin oʻylab koʻring: kattaroq yoshda kasbni oʻzgartirish oson deb oʻylaysizmi?',
     [
         P("For twelve years, Shahlo Karimova worked as an accountant in a large office in Namangan. She had a good "
           "salary, a comfortable chair and a computer full of numbers. Her family was proud of her stable job. But "
           "every evening, when she came home, she did the one thing that really made her happy: she baked. Cakes, "
           "bread, biscuits with walnuts: her kitchen always smelled of something warm."),
         P("For a long time, baking was only a hobby. Friends and neighbours often ordered cakes for birthdays, and "
           "Shahlo never asked them to pay much. Then, in the year she turned thirty-five, her company was reorganised "
           "and her department was closed. She was offered a similar job in another city, but it would have meant "
           "leaving her children with her parents for most of the week."),
         P("Shahlo remembers that this was the moment when she had to make a decision. Her husband encouraged her to "
           "try baking professionally, but her mother was less sure. She told Shahlo that a bakery was a risky business "
           "and that an accountant should know this better than anyone. Shahlo agreed that it was risky. However, she "
           "also knew that if she did not try, she would always wonder what might have happened."),
         P("She started small. She rented a tiny room near a busy market, bought a second-hand oven and got up at four "
           "every morning to bake. Her experience as an accountant turned out to be very useful: she knew exactly how "
           "much each loaf cost to make, and she kept careful records of every sale. In the first six months, she earned "
           "less than she had earned in the office. More than once, she wanted to give up."),
         P("Today, three years later, Shahlo's bakery employs five people, and customers queue outside on Friday "
           "mornings for her walnut bread. She works longer hours than before, but she says that she is much happier. "
           "When young people ask her for advice, she tells them that it is never too late to change direction. They do "
           "not have to throw away their old skills, she explains. They just have to find a new place to use them."),
     ],
     [G('accountant', 'buxgalter, hisobchi'), G('salary', 'maosh, oylik'), G('stable', 'barqaror, ishonchli'),
      G('order', 'buyurtma bermoq'), G('reorganise', 'qayta tashkil qilmoq'), G('department', 'boʻlim'),
      G('encourage', 'ruhlantirmoq, ragʻbatlantirmoq'), G('risky', 'tavakkalli, xavfli'),
      G('wonder', 'oʻylanib qolmoq, qiziqmoq'), G('rent', 'ijaraga olmoq'), G('second-hand', 'ishlatilgan, eski'),
      G('records', 'hisob yozuvlari'), G('give up', 'taslim boʻlmoq, voz kechmoq'),
      G('queue', 'navbatda turmoq'), G('employ', 'ishga olmoq, ish bilan taʼminlamoq')],
     [GN('i30-passive-tenses', 'Majhul nisbat: was reorganised, was closed',
         'her company was reorganised and her department was closed'),
      GN('i33-reported-speech', 'Koʻchirma gap: She told Shahlo that …',
         'She told Shahlo that a bakery was a risky business')],
     [
         tf('Shahlo worked as an accountant for more than ten years.', 'T',
            '«For twelve years, Shahlo Karimova worked as an accountant» — 12 yil.', 0, ng=True),
         tf('Before she opened her bakery, people paid Shahlo a lot of money for her cakes.', 'F',
            'Aksincha: «Shahlo never asked them to pay much».', 1, ng=True),
         tf("Shahlo's husband had his own business.", 'NG',
            'Eri uni ruhlantirgani aytilgan, lekin uning ishi haqida hech narsa yoʻq.', 2, ng=True),
         tf("Shahlo's mother supported her plan from the beginning.", 'F',
            'Onasi ikkilangan: «her mother was less sure» va biznesni «risky» degan.', 2, ng=True),
         ch('Why did Shahlo not accept the job in another city?',
            ['The salary was too low.', 'She would have had to leave her children for most of the week.',
             'She did not want to work as an accountant any more.'], 1,
            '«it would have meant leaving her children with her parents for most of the week».', 1),
         ch('How did her experience as an accountant help her?',
            ['She knew the costs and kept careful records.', 'Her old company gave her money.',
             'Her old colleagues became her first customers.'], 0,
            '«she knew exactly how much each loaf cost to make, and she kept careful records of every sale».', 3),
         gap('Shahlo rented a tiny room and bought a ___ oven.', ['second-hand', 'second hand'],
             '«bought a second-hand oven».', 3, 2),
         hd(4, ['Success after a difficult start', 'Why the bakery closed', 'Her first day at the market'], 0,
            '5-xatboshi: uch yildan keyin besh kishi ishlaydi, mijozlar navbatda turadi — qiyin boshlanishdan keyingi muvaffaqiyat.'),
         gap('On Friday mornings, customers queue outside for her walnut ___.', 'bread',
             '«customers queue outside on Friday mornings for her walnut bread».', 4, 2),
     ])

text(B, 'b1-05-volunteer', 'Koʻngilli boʻlish', 'My Summer as a Volunteer', 'B1', 'email',
     L('Jamiyat', 'Community'),
     'Jasur doʻsti Azizaga yozda kutubxonada koʻngilli boʻlib ishlagani haqida xat yozadi. '
     'Oʻqishdan oldin oʻylab koʻring: siz qayerda koʻngilli boʻlib yordam bera olardingiz?',
     [
         P("Hi Aziza, I am sorry I have not written for so long, but I have been really busy this summer, and for a good "
           "reason! You know that I had planned to spend the holidays playing football and sleeping late. Well, that plan "
           "changed in June, when our neighbour, who works at the district library, told me that they were looking for "
           "volunteers for a summer reading club for children."),
         P("At first I was not sure. I had never worked with children, and I thought it would be boring. But my mother "
           "said that it would look good on my university applications, so I agreed to try it for one week. That was two "
           "months ago, and I am still going there three mornings a week!"),
         P("The club is for children aged seven to ten. Most of them can read, but they do not enjoy it. My job is to "
           "read stories aloud to them, help them choose books and organise small games. Last week we made masks of "
           "the characters from a fairy tale, and the children acted out the story for their parents. One shy boy, "
           "Sanjar, who had hardly said a word in July, played the wolf and was brilliant. I was so proud of him."),
         P("I have learned a lot too. I have become much more patient, and I have discovered that I am good at "
           "explaining things. I have also realised that volunteering is not only about helping others. The children "
           "have taught me to enjoy simple things, and the other volunteers have become good friends."),
         P("The club needs more volunteers in September, when the children go back to school and the club meets only on "
           "Saturdays. You should join us! You love books more than anyone I know, and I am sure the children would love "
           "you. If you are interested, write back and I will give you the librarian's phone number. Hope to hear from "
           "you soon. Best wishes, Jasur"),
     ],
     [G('volunteer', 'koʻngilli; koʻngilli boʻlib ishlamoq'), G('district', 'tuman'),
      G('application', 'ariza (oʻqishga, ishga)'), G('aloud', 'ovoz chiqarib'), G('organise', 'tashkil qilmoq'),
      G('character', 'qahramon, personaj'), G('fairy tale', 'ertak'), G('act out', 'sahnalashtirmoq, rolda ijro etmoq'),
      G('shy', 'uyatchan, tortinchoq'), G('hardly', 'deyarli … emas'), G('brilliant', 'ajoyib, zoʻr'),
      G('patient', 'sabrli'), G('realise', 'anglamoq, tushunib yetmoq'), G('librarian', 'kutubxonachi')],
     [GN('i05-present-perfect', 'Present Perfect: have become, have discovered',
         'I have become much more patient, and I have discovered that I am good at explaining things'),
      GN('i20-should-ought-better', 'Maslahat: should', 'You should join us!')],
     [
         tf('Jasur had planned to spend his summer holidays as a volunteer.', 'F',
            'Uning rejasi boshqa edi: «playing football and sleeping late».', 0, ng=True),
         tf('Jasur now goes to the library three mornings a week.', 'T',
            '«I am still going there three mornings a week!»', 1, ng=True),
         tf('Most of the other volunteers are university students.', 'NG',
            'Boshqa koʻngillilar doʻst boʻlgani aytilgan, lekin ular kimligi haqida maʼlumot yoʻq.', 3, ng=True),
         tf('In September, the club will meet only on Saturdays.', 'T',
            '«the club meets only on Saturdays» — sentyabrda, bolalar maktabga qaytganda.', 4, ng=True),
         ch('Why did Jasur agree to try volunteering?',
            ['He had always loved working with children.', 'His mother said it would help his university applications.',
             'The library offered to pay him.'], 1,
            '«my mother said that it would look good on my university applications, so I agreed».', 1),
         gap('The reading club is for children aged seven to ___.', ['ten', '10'],
             '«The club is for children aged seven to ten».', 2, 2),
         ch('What does Jasur say about Sanjar?',
            ['He was quiet at first but played the wolf very well.', 'He could not read at all.',
             'He was the loudest child in the club.'], 0,
            '«who had hardly said a word in July, played the wolf and was brilliant».', 2),
         gap('Jasur has discovered that he is good at ___.', ['explaining things', 'explaining'],
             '«I have discovered that I am good at explaining things».', 3, 2),
         ch('What is the main purpose of the last paragraph?',
            ['to invite Aziza to become a volunteer', 'to ask Aziza for some books',
             'to say sorry for not writing'], 0,
            '«You should join us!» va kutubxonachining raqamini berishni taklif qiladi — Azizani koʻngillilikka chaqiradi.', 4),
     ])
