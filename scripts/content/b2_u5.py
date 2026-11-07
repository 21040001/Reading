"""B2 · 5-boʻlim: Multiple choice va fikr (muallif fikri, maqsad, xulosa chiqarish)"""
from lib import *

B = 'b2'

YNG = (' Ikkinchi qism: True / False / Not Given — bu matnda TRUE = muallif shu fikrga qoʻshiladi (YES), '
       'FALSE = muallif fikri bunga zid (NO), NOT GIVEN = muallif bu haqda oʻz fikrini bildirmagan.')

# ---------------------------------------------------------------- 1. Homework
text(B, 'b2-21-homework', 'Uy vazifasi kerakmi?', 'Is Homework Necessary?', 'B2', 'exam',
     L('Taʼlim', 'Education'),
     'Topshiriq: Multiple choice (muallif fikri). Muallifning oʻz fikrini u keltirgan boshqalarning fikridan ajrating: '
     '«supporters argue», «critics point out» — bu boshqalar; «In my view», «I believe» — muallifning oʻzi. '
     'Savolda «the writer» soʻzi boʻlsa, javobni aynan shu jumlalardan qidiring.' + YNG,
     [
         P("Few topics divide parents, teachers and pupils as reliably as homework. For some families, the evening routine "
           "of exercise books spread across the kitchen table is a sign of a serious education. For others, it is a source "
           "of tears, arguments and lost sleep. In recent years, some schools have reduced homework or abandoned it "
           "altogether in the early grades, while others have increased it. Which side is right?"),
         P("Supporters of homework make a reasonable case. Learning, they argue, does not stop when the bell rings. A skill "
           "that is practised only in the classroom is easily forgotten, and short, regular practice at home helps new "
           "knowledge to settle. Homework is also said to build habits that matter later in life: planning time, working "
           "without supervision and taking responsibility for one's own progress."),
         P("Critics, however, point out that these benefits depend heavily on the kind of task and the age of the child. A "
           "young pupil copying out the same sentence twenty times is not developing independence; the child is simply learning "
           "to dislike school. Moreover, homework assumes that every child goes home to a quiet room and an adult who can "
           "help. Many do not. A child who looks after younger brothers and sisters, or whose parents work late, may be "
           "punished for circumstances that have nothing to do with effort."),
         P("In my view, both sides are partly right, and the real question is not whether homework should exist but what it "
           "should look like. The best homework I have seen is short, has a clear purpose and could not easily be done in "
           "class: reading a chapter of a novel, interviewing a grandparent about the past, or measuring the shadows in the "
           "yard at different times of day. Such tasks connect school with the world outside it. Pages of repetitive "
           "exercises, on the other hand, mostly measure how patient a family is."),
         P("Teachers also deserve some sympathy. Under pressure to cover a long curriculum, many feel that homework is the "
           "only way to finish the programme on time. Yet if a topic has been taught too quickly for pupils to understand "
           "it, sending it home rarely solves the problem; it simply moves the difficulty from the teacher to the parents."),
         P("Abolishing homework completely would probably be a mistake, especially for older students preparing for "
           "important examinations, who genuinely need time for independent revision. But schools would do well to ask "
           "themselves a simple question before setting any task: what will a child learn from this that they could not "
           "learn in the classroom? If there is no good answer, the evening might be better spent on reading, sport or "
           "simply rest."),
     ],
     [G('divide', '(fikrlarni) ikkiga boʻlmoq'), G('reliably', 'har doim, ishonchli tarzda'), G('routine', 'kundalik tartib'),
      G('abandon', 'voz kechmoq, tashlamoq'), G('settle', 'oʻrnashmoq, mustahkamlanmoq'),
      G('supervision', 'nazorat'), G('independence', 'mustaqillik'), G('circumstances', 'sharoit, vaziyat'),
      G('purpose', 'maqsad'), G('repetitive', 'takroriy, bir xil'), G('sympathy', 'hamdardlik'),
      G('curriculum', 'oʻquv dasturi'), G('abolish', 'bekor qilmoq'), G('genuinely', 'chindan ham'),
      G('revision', 'takrorlash (imtihonga)')],
     [GN('i31-it-is-said', 'is said to: …ligi aytiladi', 'Homework is also said to build habits that matter later in life'),
      GN('c61-linking-adverbials', 'Bogʻlovchi soʻzlar: Moreover', 'Moreover, homework assumes that every child goes home to a quiet room')],
     [
         ch("What is the writer's main argument?",
            ['Homework should be abolished in all schools.',
             'Homework should be better designed rather than removed.',
             'Teachers do not give pupils enough homework.',
             'Parents should spend more time helping with homework.'], 1,
            '4-xatboshi: «the real question is not whether homework should exist but what it should look like». Muallif '
            'bekor qilishga qarshi (6-xatboshi: «would probably be a mistake»), lekin koʻproq vazifa ham talab qilmaydi.', 3),
         ch('What is the main purpose of paragraph C?',
            ['to explain why homework can be unfair to some children',
             'to describe a typical evening in a family home',
             'to show that homework builds independence'], 0,
            'C xatboshi tanqidchilar fikri: uyda tinch xona va yordam beradigan kattalar hammada yoʻq. «builds independence» — '
            'bu B xatboshidagi tarafdorlar fikri.', 2),
         ch('What does the writer mean by «Pages of repetitive exercises … mostly measure how patient a family is»?',
            ['Such homework tests the family\'s endurance more than the child\'s learning.',
             'Families should be more patient with their children.',
             'Repetitive exercises are a good way to test character.'], 0,
            'Muallif bunday vazifani tanqid qiladi: u bilimni emas, oilaning sabrini «oʻlchaydi». Bu kinoya — maqtov emas.', 3),
         ch("What is the writer's attitude towards teachers in paragraph E?",
            ['completely hostile', 'understanding, but critical of one common practice',
             'unconcerned', 'full of admiration for their methods'], 1,
            '«Teachers also deserve some sympathy» — tushunadi; lekin «sending it home rarely solves the problem» — '
            'shoshib oʻtilgan mavzuni uyga berish odatini tanqid qiladi.', 4),
         ch('Which task would the writer most probably approve of?',
            ['copying a list of spelling words ten times',
             'finishing fifty sums from the textbook',
             'asking an older neighbour how the town has changed and reporting back',
             'rewriting the day\'s lesson notes neatly'], 2,
            'Muallif yoqtirgan misollar: «interviewing a grandparent about the past» — maktabni tashqi dunyo bilan bogʻlaydi. '
            'Qolganlari «repetitive exercises».', 3),
         ch('Which statement would the writer most likely agree with?',
            ['The value of homework depends on the purpose of the task.',
             'Homework is useful only for young children.',
             'Pupils who do not finish homework are lazy.'], 0,
            '«short, has a clear purpose» va 6-xatboshidagi savol: «what will a child learn from this…?». Kichik bolalar '
            'haqida muallif aksincha, katta oʻquvchilarga vazifa kerak deydi.', 5),
         tf('Good homework tasks link what is learned at school with life outside it.', 'T',
            'TRUE (muallif qoʻshiladi): «Such tasks connect school with the world outside it» — muallif buni yaxshi vazifa '
            'sifatida keltiradi.', 3, ng=True),
         tf('Long sets of repetitive exercises are the most useful kind of homework.', 'F',
            'FALSE: muallif ularni tanqid qiladi — «mostly measure how patient a family is».', 3, ng=True),
         tf('Teachers who set homework do not care about their pupils.', 'F',
            'FALSE: «Teachers also deserve some sympathy» — muallif ularni dasturni tugatish bosimi ostida deb tushunadi.', 4,
            ng=True),
         tf('Homework should be checked by the teacher on the same day it is handed in.', 'NG',
            'NOT GIVEN: vazifani tekshirish haqida muallif hech qanday fikr bildirmagan.', 4),
     ])

# ---------------------------------------------------------------- 2. Tourism
text(B, 'b2-22-tourism', 'Turizm: foyda va zarar', 'Tourism: Gift or Burden?', 'B2', 'exam',
     L('Jamiyat va iqtisod', 'Society and economy'),
     'Topshiriq: Multiple choice (asosiy gʻoya va maqsad). Ikki tomonni koʻrsatadigan matnda muallifning xulosasi '
     'odatda oxirgi xatboshida boʻladi — avval birinchi va oxirgi xatboshini diqqat bilan oʻqing. «however», «yet», '
     '«none of this means» kabi soʻzlardan keyin fikr burilishiga eʼtibor bering.' + YNG,
     [
         P("For many cities, tourism looks like an obvious gift. Visitors arrive, spend money and leave, and the local economy "
           "grows. In Uzbekistan, the historic centres of Samarkand, Bukhara and Khiva have welcomed growing numbers of "
           "foreign and domestic travellers in recent years, and new hotels, cafés and guesthouses have opened to serve them. "
           "Yet experience from popular destinations around the world suggests that the gift comes with conditions."),
         P("The benefits are real and should not be underestimated. Tourism creates jobs not only in hotels and restaurants "
           "but also for drivers, guides, craftspeople and the farmers who supply food. A potter or a carpet weaver who once "
           "sold only to neighbours may now find buyers from the other side of the world. Income from visitors can also pay "
           "for the restoration of old buildings that might otherwise fall into ruin."),
         P("Tourism can even help to keep traditions alive. When travellers show interest in a local craft, young people are "
           "more likely to see it as a career rather than an old-fashioned hobby. In this sense, the attention of outsiders "
           "can strengthen a community's pride in its own culture. Skills that might have disappeared within a generation are, in some places, being passed on once again."),
         P("The problems, however, tend to appear gradually, which makes them easy to ignore. In some famous European cities, "
           "residents complain that the historic centre has turned into a kind of museum: the shops sell souvenirs instead "
           "of bread, rents rise beyond what local families can afford, and narrow streets are crowded from morning till "
           "night. Old buildings, too, can suffer when thousands of feet walk across the same stones every day."),
         P("There is also a quieter danger, which might be called the loss of authenticity. When a tradition is performed "
           "mainly for visitors, it can slowly change to match what tourists expect to see. A wedding dance shortened to five "
           "minutes for a hotel stage is still beautiful, but it is no longer quite the same thing."),
         P("None of this means that tourism should be discouraged. It means that it needs to be planned. Limiting the number "
           "of large tour groups at the busiest sites, encouraging visitors to explore less famous towns, and making sure that "
           "local people share in the income are all measures that destinations have tried. The aim should be a city that "
           "welcomes guests without ceasing to be a home for those who live there."),
     ],
     [G('obvious', 'aniq, ravshan'), G('destination', 'manzil (sayohat)'), G('underestimate', 'yetarlicha baholamaslik'),
      G('craftspeople', 'hunarmandlar'), G('supply', 'yetkazib bermoq'), G('restoration', 'taʼmirlash, tiklash'),
      G('fall into ruin', 'vayron boʻlmoq'), G('strengthen', 'mustahkamlamoq'), G('resident', 'doimiy aholi'),
      G('souvenir', 'esdalik buyum'), G('afford', '(pulga) qurbi yetmoq'), G('authenticity', 'asllik, haqiqiylik'),
      G('perform', 'ijro etmoq'), G('discourage', 'toʻsqinlik qilmoq, ragʻbatlantirmaslik'), G('cease', 'toʻxtamoq')],
     [GN('i30-passive-tenses', 'Modal + majhul: should not be underestimated', 'The benefits are real and should not be underestimated.'),
      GN('i56-ing-ed-clauses', '-ed qoʻshimchali ergash qism: shortened to …', 'A wedding dance shortened to five minutes for a hotel stage is still beautiful')],
     [
         ch('What is the main purpose of the passage?',
            ['to persuade readers to visit Samarkand, Bukhara and Khiva',
             'to argue that tourism brings real benefits but must be carefully managed',
             'to show that tourism destroys historic cities',
             'to compare Uzbek cities with European ones'], 1,
            'Foyda (B, C) va zarar (D, E) koʻrsatiladi, xulosa F da: «None of this means that tourism should be discouraged. '
            'It means that it needs to be planned.»', 5),
         ch('What does the writer mean by «the gift comes with conditions»?',
            ['Visitors must follow strict local rules.',
             'The advantages of tourism bring problems that have to be dealt with.',
             'Cities have to pay to attract tourists.'], 1,
            '«Gift» = turizm foydasi; «conditions» — keyingi xatboshilarda tasvirlangan muammolar. Qoidalar yoki pul '
            'toʻlash haqida gap yoʻq.', 0),
         ch('Why does the writer include paragraph C?',
            ['to show a cultural benefit of tourism that is less obvious than money',
             'to criticise young people for losing interest in crafts',
             'to explain how traditions change to please tourists'], 0,
            'C: turistlarning qiziqishi yoshlarni hunarga qaytaradi va «pride in its own culture»ni kuchaytiradi. '
            'Anʼanalarning oʻzgarishi — E xatboshidagi xavf.', 2),
         ch('In paragraph D, «the historic centre has turned into a kind of museum» suggests that the centre',
            ['contains many interesting museums',
             'is very well protected and preserved',
             'no longer meets the everyday needs of the people who live there'], 2,
            'Keyingi tafsilotlar: non oʻrniga suvenir, ijara qimmat, koʻchalar gavjum — aholi uchun yashash joyi emas, '
            'tomosha joyiga aylangan.', 3),
         ch('What can be inferred from the example of the wedding dance?',
            ['Performances for tourists are usually of poor quality.',
             'A tradition shown to visitors may lose part of its original character.',
             'Hotels should not organise cultural shows.'], 1,
            '«still beautiful, but … no longer quite the same thing» — sifat yomon emas, lekin asl koʻrinishi oʻzgaradi.', 4),
         ch("Which best describes the writer's overall attitude to tourism?",
            ['enthusiastic and uncritical', 'cautiously positive', 'strongly opposed', 'uninterested'], 1,
            'Foydani tan oladi («should not be underestimated»), lekin rejalashtirishni talab qiladi — ehtiyotkor ijobiy munosabat.', 5),
         ch('Which statement would the writer most likely agree with?',
            ['Local people should receive a fair share of the money tourism brings.',
             'Visitors should only be allowed to see the most famous sites.',
             'Large tour groups should be banned everywhere.'], 0,
            '«making sure that local people share in the income». Muallif aksincha kamroq mashhur shaharlarni tavsiya qiladi; '
            'guruhlarni taqiqlash emas, faqat «limiting… at the busiest sites».', 5),
         tf('Only people who work in hotels gain from tourism.', 'F',
            'FALSE: «not only in hotels and restaurants but also for drivers, guides, craftspeople and the farmers».', 1, ng=True),
         tf('Interest from visitors can make young people value traditional crafts more.', 'T',
            'TRUE (muallif qoʻshiladi): «young people are more likely to see it as a career rather than an old-fashioned hobby».', 2,
            ng=True),
         tf('The problems caused by tourism are usually noticed straight away.', 'F',
            'FALSE: «tend to appear gradually, which makes them easy to ignore».', 3, ng=True),
         tf('Foreign tourists are more welcome in historic cities than domestic ones.', 'NG',
            'NOT GIVEN: chet ellik va mahalliy sayyohlar faqat tilga olingan; muallif ularni solishtirmaydi.', 0),
     ])

# ---------------------------------------------------------------- 3. Teenagers and social media
text(B, 'b2-23-teens-social', 'Ijtimoiy tarmoqlar va oʻsmirlar', 'Teenagers and Social Media', 'B2', 'exam',
     L('Texnologiya va jamiyat', 'Technology and society'),
     'Topshiriq: Multiple choice (iboraning matndagi maʼnosi). Iboraning soʻzma-soʻz maʼnosini tanlashga shoshilmang: '
     'oldingi va keyingi jumlani qayta oʻqing, soʻng har bir variantni iboraning oʻrniga qoʻyib koʻring — '
     'qaysi biri bilan jumla mantiqli boʻlsa, oʻsha javob.' + YNG,
     [
         P("Few inventions have entered teenage life as quickly as social media. In a single generation, the phone has become "
           "a diary, a meeting place and a stage. Parents who grew up writing letters or waiting by the home telephone often "
           "watch their children's constant scrolling with a mixture of confusion and alarm. But is their worry justified?"),
         P("Many psychologists believe there are genuine reasons for concern. Platforms are designed to hold attention, and the "
           "endless stream of photos, short videos and notifications can make it hard to put the phone down. Late-night use is "
           "widely thought to reduce sleep, which in turn affects mood and concentration at school. Perhaps most worrying is "
           "comparison: teenagers see carefully edited images of their peers' lives and may conclude that everyone else is "
           "happier, more attractive or more successful."),
         P("Cruelty, too, has moved online. Unkind remarks that once stayed in the school yard can now follow a young person "
           "home and be seen by hundreds of people. Because the attacker is often hidden behind a screen, it may be harder "
           "for adults to notice what is happening. Some teenagers, it seems, prefer to suffer in silence rather than tell an "
           "adult, perhaps fearing that their phones will be taken away."),
         P("And yet the picture is not entirely dark. For a teenager who feels isolated, perhaps because of an unusual hobby or "
           "a difficult situation at home, an online community can offer friendship and understanding that are hard to find "
           "nearby. Young people use social networks to organise volunteering, to share their music and drawings, and to learn "
           "skills that their schools do not teach. For many, staying in touch with relatives who have moved abroad would be "
           "far more difficult without them."),
         P("Researchers are increasingly cautious about simple conclusions. How a teenager uses social media seems to matter "
           "more than how many hours they spend on it. Chatting with real friends or creating something is likely to have "
           "very different effects from passively scrolling through strangers' photographs late at night."),
         P("If this is correct, banning phones entirely may be less useful than teaching young people to use them wisely. "
           "Agreeing on phone-free times, such as meals and the hour before sleep, talking openly about what children see "
           "online, and setting a good example are approaches that many families find helpful. After all, adults are not "
           "always the best models of healthy screen habits themselves."),
     ],
     [G('scroll', '(ekranni) varaqlamoq'), G('alarm', 'xavotir'), G('justified', 'asosli'),
      G('genuine', 'haqiqiy, chin'), G('notification', 'bildirishnoma'), G('concentration', 'diqqatni jamlash'),
      G('edited', 'tahrirlangan'), G('peer', 'tengdosh'), G('cruelty', 'shafqatsizlik'),
      G('isolated', 'yolgʻiz, ajralib qolgan'), G('volunteering', 'koʻngillilik'), G('cautious', 'ehtiyotkor'),
      G('conclusion', 'xulosa'), G('passively', 'sust, faol boʻlmagan holda'), G('approach', 'yondashuv')],
     [GN('i31-it-is-said', 'is thought to: …deb hisoblanadi', 'Late-night use is widely thought to reduce sleep'),
      GN('c09-probability-deduction', 'Ehtimollik: is likely to', 'is likely to have very different effects')],
     [
         ch('What is the main idea of the passage?',
            ['Social media is mainly harmful to teenagers.',
             'The effects of social media depend largely on how it is used.',
             'Parents should ban phones at home.',
             'Teenagers use social media less than adults think.'], 1,
            '«How a teenager uses social media seems to matter more than how many hours they spend on it.» Taqiqlash '
            'haqida muallif aksincha: «may be less useful».', 4),
         ch('What does the writer mean when saying the phone has become «a diary, a meeting place and a stage»?',
            ['Teenagers use phones mainly to write about their day.',
             'The phone now serves many personal and social purposes for teenagers.',
             'Teenagers want to become actors.'], 1,
            'Uch metafora: shaxsiy yozuvlar, doʻstlar bilan uchrashish, oʻzini koʻrsatish — telefon koʻp vazifani bajaradi. '
            'Soʻzma-soʻz maʼno emas.', 0),
         ch('Why does the writer mention parents who grew up «writing letters or waiting by the home telephone»?',
            ['to explain why many parents find their children\'s habits hard to understand',
             'to show that older forms of communication were better',
             'to suggest that parents should write more letters'], 0,
            'Ular boshqacha muhitda katta boʻlgani uchun «confusion and alarm» his qiladi. Muallif eski usullarni maqtamaydi.', 0),
         ch('According to paragraph C, why might online cruelty be hard for adults to notice?',
            ['because it happens only at school',
             'because the person responsible is often not visible',
             'because teenagers enjoy it'], 1,
            '«the attacker is often hidden behind a screen». Aksincha, endi u maktabdan tashqariga ham chiqadi.', 2),
         ch('What is the purpose of paragraph D?',
            ['to present the positive side of social media',
             'to warn about strangers online',
             'to describe problems at home'], 0,
            '«And yet the picture is not entirely dark» — burilish: doʻstlik, koʻngillilik, ijod, qarindoshlar bilan aloqa.', 3),
         ch('What does the final sentence of the passage suggest?',
            ['Adults use phones less than teenagers.',
             'Parents should also think about their own screen habits.',
             'Teenagers should teach adults how to use phones.'], 1,
            '«adults are not always the best models» — ota-onalar ham oʻz odatlariga qarashi kerak; «setting a good example» bilan bogʻliq.', 5),
         ch('Which statement would the writer most likely agree with?',
            ['An hour spent chatting with close friends is probably different in effect from an hour of scrolling strangers\' photos at night.',
             'The total number of hours online is the only thing that matters.',
             'All online communities are dangerous for young people.'], 0,
            '«Chatting with real friends … is likely to have very different effects from passively scrolling».', 4),
         tf('Parents\' worries about social media have no basis at all.', 'F',
            'FALSE: muallif psixologlar fikrini keltiradi («genuine reasons for concern») va oʻzi ham «Perhaps most worrying '
            'is comparison» deydi; D xatboshidagi «the picture is not entirely dark» ham salbiy tomon borligini tan oladi.', 1,
            ng=True),
         tf('An online community can help a lonely teenager find understanding.', 'T',
            'TRUE (muallif qoʻshiladi): «an online community can offer friendship and understanding that are hard to find nearby».', 3,
            ng=True),
         tf('The amount of time spent online is the most important factor.', 'F',
            'FALSE: qanday foydalanish «seems to matter more than how many hours».', 4, ng=True),
         tf('Schools should teach a separate subject about social media.', 'NG',
            'NOT GIVEN: muallif oilalardagi yondashuvlar haqida yozadi; maktabda alohida fan haqida fikr yoʻq.', 5),
     ])

# ---------------------------------------------------------------- 4. City or village
text(B, 'b2-24-city-village', 'Shahar yoki qishloq?', 'City or Village?', 'B2', 'exam',
     L('Turmush tarzi', 'Lifestyle'),
     'Topshiriq: Multiple choice («muallif nimaga qoʻshiladi?»). Haddan tashqari keskin variantlarni («always», «never», '
     '«everyone», «only») birinchi boʻlib chiqarib tashlang — muvozanatli matn muallifi kamdan-kam mutlaq fikr aytadi. '
     'Qolgan variantlarni oxirgi xatboshidagi xulosa bilan solishtiring.' + YNG,
     [
         P("Every year, large numbers of young people leave their villages for the city, and in many countries, including "
           "Uzbekistan, the capital and regional centres continue to grow. At the same time, a smaller but noticeable group is "
           "moving in the opposite direction: city families buying old houses in the countryside, or people who work online "
           "deciding they no longer need to live near an office. So which is the better place to live? I would argue that the "
           "question itself is slightly misleading."),
         P("The attractions of the city are easy to list. Universities, hospitals, theatres and a wide choice of jobs are "
           "concentrated there, and for an ambitious young person this concentration of opportunity can be decisive. Cities "
           "also offer a certain freedom. In a large population, it is easier to find people who share your interests, and "
           "nobody pays much attention to how you dress or whom you spend time with."),
         P("That same anonymity, however, has a cost. Many city dwellers admit that they hardly know their neighbours, and "
           "loneliness can exist even in the busiest streets. Add traffic, noise, polluted air in winter and the high price of "
           "flats, and it is not surprising that some people begin to dream of a quieter life."),
         P("The village offers precisely what the city lacks: space, fresh air, home-grown fruit and a community in which "
           "people look after one another. When someone falls ill or a family celebrates a wedding, neighbours appear without "
           "being asked. For children, a yard, a garden and the freedom to play outside can be worth more than any shopping "
           "centre."),
         P("Rural life, though, is rarely as idyllic as it looks from a car window. Work can be hard to find and is often poorly "
           "paid. Schools and clinics may be far away, and young people with specialised ambitions may have to leave anyway. "
           "The close community that supports you can also watch you closely, and not everyone enjoys having their private "
           "decisions discussed by the whole street."),
         P("Perhaps, then, the honest answer is that the right place depends on the stage of life a person has reached. A "
           "student hungry for experience and a retired couple who want peace are looking for different things. As transport "
           "improves and more work can be done remotely, the choice may become less permanent than it was for our "
           "grandparents, who often spent their whole lives in one place. The aim should be to make both cities and villages "
           "better places to live, so that people can move because they want to, not because they have to."),
     ],
     [G('misleading', 'chalgʻituvchi'), G('concentrated', 'bir joyga toʻplangan'), G('ambitious', 'intiluvchan, katta maqsadli'),
      G('decisive', 'hal qiluvchi'), G('anonymity', 'notanishlik, hech kim tanimasligi'), G('dweller', 'aholi, yashovchi'),
      G('loneliness', 'yolgʻizlik'), G('polluted', 'ifloslangan'), G('precisely', 'aynan'),
      G('rural', 'qishloqqa oid'), G('idyllic', 'osoyishta va goʻzal, orzudagidek'), G('specialised', 'maxsus, ixtisoslashgan'),
      G('remotely', 'masofadan'), G('permanent', 'doimiy')],
     [GN('i54-whose-whom-where', 'whom: kim bilan', 'how you dress or whom you spend time with'),
      GN('i64-so-that-in-order-to', 'so that: …sin deb', 'so that people can move because they want to')],
     [
         ch("What is the writer's main point?",
            ['City life is better for most people.',
             'Villages offer a healthier way of life than cities.',
             'The best place to live depends on a person\'s stage of life.',
             'People should stop moving from villages to cities.'], 2,
            'Xulosa F da: «the right place depends on the stage of life a person has reached».', 5),
         ch('Why does the writer call the question «slightly misleading»?',
            ['because there is no single answer that suits everyone',
             'because most people have already chosen the city',
             'because the facts about migration are not clear'], 0,
            'Savol «qaysi biri yaxshiroq» deb bitta javob kutadi, muallif esa oxirida javob odamga bogʻliq deydi.', 0),
         ch('What is the purpose of paragraph C?',
            ['to describe the history of cities',
             'to show that a feature praised in paragraph B also has disadvantages',
             'to explain why flats are expensive'], 1,
            '«That same anonymity, however, has a cost» — B dagi erkinlik (hech kim eʼtibor bermaydi) yolgʻizlikka olib keladi.', 2),
         ch('What does «as idyllic as it looks from a car window» suggest?',
            ['Village life seems more perfect to outsiders than it really is.',
             'The countryside is best seen while travelling.',
             'Villages have very bad roads.'], 0,
            'Oʻtib ketayotgan odamga qishloq goʻzal koʻrinadi, lekin keyin muammolar sanaladi: ish yoʻq, maktab uzoq.', 4),
         ch('What can be inferred from paragraph E about privacy in a village?',
            ['It is better protected than in a city.',
             'It may be limited because neighbours know a lot about each other.',
             'It is not important to village people.'], 1,
            '«The close community … can also watch you closely» — yaqin jamoa shaxsiy hayotni ham kuzatadi.', 4),
         ch('Which statement would the writer most likely agree with?',
            ['Everyone should live in a village when they retire.',
             'Both cities and villages need to be improved.',
             'Young people should never leave their villages.'], 1,
            '«The aim should be to make both cities and villages better places to live». Boshqa variantlar juda keskin.', 5),
         tf('A big city makes it easier to meet people with the same interests.', 'T',
            'TRUE (muallif qoʻshiladi): «it is easier to find people who share your interests».', 1, ng=True),
         tf('Living in a busy city protects people from loneliness.', 'F',
            'FALSE: «loneliness can exist even in the busiest streets».', 2, ng=True),
         tf('Most city families who move to the countryside later regret it.', 'NG',
            'NOT GIVEN: qishloqqa koʻchayotganlar tilga olingan, lekin ular afsuslanishi haqida muallif hech narsa demaydi.', 0),
         tf('Young people with special career goals can always fulfil them in a village.', 'F',
            'FALSE: «young people with specialised ambitions may have to leave anyway».', 4, ng=True),
     ])

# ---------------------------------------------------------------- 5. Books and screens
text(B, 'b2-25-books-screens', 'Kitob va ekran', 'Paper or Screen?', 'B2', 'exam',
     L('Oʻqish va madaniyat', 'Reading and culture'),
     'Topshiriq: Multiple choice (muallif munosabati). Ehtiyotkor soʻzlarga eʼtibor bering: «may», «perhaps», «suspect», '
     '«is still debated». Agar matnda shunday soʻzlar boʻlsa, «the writer is certain» yoki «it has been proven» '
     'degan variant notoʻgʻri boʻladi.' + YNG,
     [
         P("Not long ago, it was widely predicted that the printed book would soon disappear. Screens were becoming cheaper and "
           "lighter, a single device could hold an entire library, and newspapers were moving online. Yet paper books have "
           "proved surprisingly stubborn. Bookshops still exist, and many readers who spend all day in front of a screen say "
           "that, in the evening, they prefer to hold something made of paper."),
         P("Digital reading certainly has advantages that are difficult to argue with. A student in a small town can open texts "
           "that would once have required a trip to a big library. Font sizes can be enlarged for people with weak eyesight, "
           "unfamiliar words can be looked up with a single touch, and a dozen novels weigh no more than one. For travellers "
           "and for people with little space at home, these are not small benefits."),
         P("Some researchers and teachers, however, suspect that the medium affects the way we read. On a screen, many people "
           "tend to skim: their eyes jump down the page in search of key words, a habit encouraged by years of reading short "
           "messages and web pages. This may be perfectly adequate for checking the news, but it is less suited to a long "
           "argument or a complex novel, where the meaning builds up slowly."),
         P("There may also be something about the physical object itself. With a paper book, readers can feel how far they have "
           "come and how much remains, and some say they remember where on a page a particular sentence appeared. These small "
           "clues may help the mind to build a kind of map of the text. Whether this really improves understanding is still "
           "debated, and the answer may differ from one reader to another."),
         P("It would be a mistake, though, to turn this into a battle between good paper and bad screens. Much depends on the "
           "reader's intention and habits. A person who reads slowly and attentively on a tablet, with notifications switched "
           "off, is probably reading better than someone who flicks distractedly through a printed magazine. The device does "
           "not decide everything; the reader does."),
         P("For learners, including those preparing for exams, a sensible approach might combine both. Screens are excellent for "
           "finding material and for quick reference, while longer or more difficult texts may be worth printing, or at least "
           "reading without interruptions. What matters most, in the end, is not the surface on which words appear but the "
           "attention we bring to them."),
     ],
     [G('predict', 'bashorat qilmoq'), G('stubborn', 'oʻjar, bardoshli'), G('device', 'qurilma'),
      G('enlarge', 'kattalashtirmoq'), G('eyesight', 'koʻrish qobiliyati'), G('medium', 'vosita, muhit'),
      G('skim', 'yuzaki koʻz yugurtirmoq'), G('adequate', 'yetarli'), G('complex', 'murakkab'),
      G('physical', 'jismoniy, moddiy'), G('clue', 'belgi, ishora'), G('debate', 'munozara qilmoq'),
      G('attentively', 'diqqat bilan'), G('distractedly', 'chalgʻigan holda'), G('interruption', 'uzilish, xalaqit'),
      G('reference', 'maʼlumot uchun qarash')],
     [GN('i31-it-is-said', 'it was predicted that: …deb bashorat qilingan', 'it was widely predicted that the printed book would soon disappear'),
      GN('c57-cleft-sentences', 'What … is …: urgʻuli gap', 'What matters most, in the end, is not the surface on which words appear')],
     [
         ch('What is the main idea of the passage?',
            ['Paper books are always better than screens.',
             'Printed books will soon disappear.',
             'How attentively we read matters more than whether we use paper or a screen.',
             'Students should stop using digital texts.'], 2,
            'Xulosa: «What matters most … is not the surface … but the attention we bring to them».', 5),
         ch('What is the purpose of paragraph A?',
            ['to show that a prediction about printed books has not come true',
             'to describe the history of newspapers',
             'to argue that screens are too expensive'], 0,
            '«it was widely predicted that the printed book would soon disappear. Yet paper books have proved surprisingly stubborn».', 0),
         ch('In paragraph A, «paper books have proved surprisingly stubborn» means that they',
            ['are difficult to open and read',
             'have continued to survive despite expectations',
             'refuse to change their design'], 1,
            '«Stubborn» bu yerda — yoʻqolmay, saqlanib qolgan: kitob doʻkonlari hali bor.', 0),
         ch('Why does the writer mention «short messages and web pages» in paragraph C?',
            ['to suggest where the habit of skimming may come from',
             'to show that people read more than before',
             'to recommend reading the news online'], 0,
            '«a habit encouraged by years of reading short messages and web pages» — skimming odati shu yerdan.', 2),
         ch("What is the writer's attitude to the idea that paper helps readers build «a kind of map of the text»?",
            ['fully convinced', 'open to it, but not certain', 'completely dismissive'], 1,
            '«may help», «is still debated», «may differ from one reader to another» — muallif inkor ham etmaydi, '
            'ishonch bilan ham aytmaydi.', 3),
         ch('What can be inferred from paragraph E?',
            ['Tablets are designed for careless readers.',
             'A careful reader using a tablet may understand more than a careless reader of paper.',
             'Printed magazines are not worth reading.'], 1,
            '«reads slowly and attentively on a tablet … is probably reading better than someone who flicks distractedly through '
            'a printed magazine».', 4),
         ch('Which piece of advice would the writer most likely give to an exam candidate?',
            ['Use only paper books when preparing.',
             'Use screens to find material, but read difficult texts without interruptions.',
             'Skim every text quickly to save time.'], 1,
            '«Screens are excellent for finding material … longer or more difficult texts may be worth printing, or at least '
            'reading without interruptions».', 5),
         tf('Digital books are useful for people who have limited space at home.', 'T',
            'TRUE (muallif qoʻshiladi): «For travellers and for people with little space at home, these are not small benefits».', 1,
            ng=True),
         tf('Skimming is never an acceptable way of reading.', 'F',
            'FALSE: «This may be perfectly adequate for checking the news».', 2, ng=True),
         tf('It has been proven that paper books improve understanding for every reader.', 'F',
            'FALSE: «is still debated, and the answer may differ from one reader to another».', 3, ng=True),
         tf('Over several years, an electronic reader costs less than buying printed books.', 'NG',
            'NOT GIVEN: ekranlar arzonlashgani aytilgan, lekin uzoq muddatdagi xarajatni muallif solishtirmaydi.', 0),
     ])
