"""A1 · 6-boʻlim: Odamlar va kasblar (5 ta matn)"""
from lib import *

B = 'a1'
JOBS = L('Kasblar', 'Jobs')

text(B, 'a1-26-grandma', 'Buvim', 'My Grandmother', 'A1', 'story', L('Oila', 'Family'),
     'Gulnora buvisi haqida hikoya qiladi. Oʻqishdan oldin oʻylab koʻring: buvingiz yoki bobongiz har kuni nima qiladi?',
     [
         P("My name is Gulnora. This is my grandmother, Saodat. She is seventy years old. "
           "She has got short grey hair and kind brown eyes. She always wears a white scarf and glasses.",
           "Mening ismim Gulnora. Bu — buvim, Saodat. U yetmish yoshda. Uning sochi kalta va oqargan, "
           "koʻzlari mehribon va jigarrang. U doim oq roʻmol oʻraydi va koʻzoynak taqadi."),
         P("My grandmother is a retired teacher. She doesn't work now, but she is always busy. "
           "She gets up at six every morning and makes tea for the family. She often makes somsa on Sundays.",
           "Buvim nafaqadagi oʻqituvchi. U hozir ishlamaydi, lekin doim band. "
           "U har kuni ertalab soat oltida turadi va oila uchun choy damlaydi. Yakshanba kunlari u tez-tez somsa pishiradi."),
         P("Fifty years ago, Grandma could run very fast. Now she can't run, but she walks in the park every evening. "
           "Her doctor says she should walk every day.",
           "Ellik yil oldin buvim juda tez yugura olardi. Hozir u yugura olmaydi, lekin har oqshom bogʻda sayr qiladi. "
           "Shifokori unga har kuni piyoda yurish kerakligini aytadi."),
         P("I love my grandmother. She tells me old stories and helps me with my homework.",
           "Men buvimni juda yaxshi koʻraman. U menga qadimiy hikoyalar aytib beradi va uy vazifamda yordam beradi."),
     ],
     [G('grey hair', 'oq (oqargan) soch'), G('kind', 'mehribon'), G('scarf', 'roʻmol'), G('glasses', 'koʻzoynak'),
      G('retired', 'nafaqadagi'), G('busy', 'band'), G('get up', 'oʻrnidan turmoq'), G('ago', 'oldin (… yil oldin)'),
      G('fast', 'tez'), G('should', 'kerak, … gani maʼqul (maslahat)'), G('story', 'hikoya, ertak')],
     [GN('b46-have-got', 'have got / has got — bor', 'She has got short grey hair and kind brown eyes.'),
      GN('b41-can-could', 'could — oʻtmishda qila olardi', 'Fifty years ago, Grandma could run very fast.')],
     [
         tf('Saodat is seventy years old.', 'T', '1-xatboshi: «She is seventy years old.»', 0),
         ch('What does Grandma always wear?', ['a white scarf', 'a blue hat', 'a red dress'], 0,
            '«She always wears a white scarf and glasses.»', 0),
         tf('Grandma works at a school now.', 'F', 'U nafaqada: «She doesn\'t work now».', 1),
         gap('Grandma often makes ___ on Sundays.', 'somsa', '«She often makes somsa on Sundays.»', 1),
         tf('Grandma can run very fast now.', 'F',
            'Ellik yil oldin tez yugura olardi, hozir esa: «Now she can\'t run».', 2),
         gap('Her doctor says she should ___ every day.', 'walk', '«Her doctor says she should walk every day.»', 2),
         ch('What does Grandma help Gulnora with?', ['her homework', 'her cooking', 'her music'], 0,
            '«She … helps me with my homework.»', 3),
     ])

text(B, 'a1-27-doctor', 'Shifokorning bir kuni', "A Day in a Doctor's Life", 'A1', 'blog', JOBS,
     'Bu — bolalar shifokorining blogi. Oʻqishdan oldin: shifokorlar sogʻliq uchun qanday maslahatlar beradi?',
     [
         P("Hi, I'm Rustam. I am a doctor at a children's hospital in Samarkand. I love my job, but it is not easy.",
           "Salom, men Rustamman. Men Samarqanddagi bolalar kasalxonasida shifokorman. Men ishimni yaxshi koʻraman, lekin u oson emas."),
         P("I usually get up at half past five. I start work at seven. Every morning I see about twenty children. "
           "Some children have got a cold, and some have got a stomachache.",
           "Men odatda soat besh yarimda turaman. Ishni soat yettida boshlayman. Har kuni ertalab yigirmatacha bolani qabul qilaman. "
           "Baʼzi bolalar shamollagan, baʼzilarining esa qorni ogʻriydi."),
         P("Children are often scared of doctors. So I always smile and tell a funny joke. Then they aren't scared.",
           "Bolalar koʻpincha shifokorlardan qoʻrqishadi. Shuning uchun men doim jilmayaman va kulgili hazil aytaman. "
           "Shunda ular qoʻrqmaydi."),
         P("Here is my advice for you. You should wash your hands before every meal. "
           "You must sleep nine or ten hours, and you shouldn't eat too many sweets!",
           "Mana sizga maslahatim. Har safar ovqatdan oldin qoʻlingizni yuvishingiz kerak. "
           "Toʻqqiz-oʻn soat uxlashingiz shart, shirinliklarni esa juda koʻp yemasligingiz kerak!"),
     ],
     [G('hospital', 'kasalxona'), G('easy', 'oson'), G('usually', 'odatda'), G('a cold', 'shamollash'),
      G('stomachache', 'qorin ogʻrigʻi'), G('scared', 'qoʻrqqan'), G('smile', 'jilmaymoq'), G('joke', 'hazil'),
      G('advice', 'maslahat'), G('wash', 'yuvmoq'), G('sweets', 'shirinliklar')],
     [GN('b48-health', 'should / must — sogʻliq uchun maslahat', 'You should wash your hands before every meal.'),
      GN('b24-frequency', 'usually, often, always', 'I usually get up at half past five.')],
     [
         ch('Where does Rustam work?', ['at a school', "at a children's hospital", 'at a pharmacy'], 1,
            '«I am a doctor at a children\'s hospital in Samarkand.»', 0),
         tf('Rustam thinks his job is easy.', 'F', 'U ishini yaxshi koʻradi, lekin: «it is not easy».', 0),
         ch('What time does Rustam get up?', ['at half past five', 'at seven', 'at six'], 0,
            '«I usually get up at half past five.» Soat yettida u ishni boshlaydi.', 1),
         gap('Rustam starts work at ___.', ['seven', '7'], '«I start work at seven.»', 1),
         tf('All the children have got a cold.', 'F',
            'Hammasi emas: «Some children have got a cold, and some have got a stomachache.»', 1),
         ch('What does Rustam do for scared children?', ['He gives them sweets.', 'He smiles and tells a joke.',
                                                         'He calls their parents.'], 1,
            '«So I always smile and tell a funny joke.»', 2),
         gap('You should wash your ___ before every meal.', 'hands',
             '«You should wash your hands before every meal.»', 3),
     ])

text(B, 'a1-28-chef', 'Oshpaz', 'The Chef', 'A1', 'dialogue', JOBS,
     'Maktab gazetasi uchun Malika oshpaz Bekzod bilan suhbatlashadi. Oʻqishdan oldin: oshpazning ishi oson deb oʻylaysizmi?',
     [
         P("Malika: Hello, Bekzod! What is your job? Bekzod: I am a chef. I work in a big restaurant in Tashkent.",
           "Malika: Salom, Bekzod! Kasbingiz nima? Bekzod: Men oshpazman. Toshkentdagi katta restoranda ishlayman."),
         P("Malika: What do you cook? Bekzod: I cook Uzbek food, like plov, lagman and shashlik. "
           "Our plov is very popular. Every day we cook plov for two hundred people.",
           "Malika: Nima pishirasiz? Bekzod: Men oʻzbek taomlarini pishiraman: palov, lagʻmon, shashlik. "
           "Bizning palovimiz juda mashhur. Har kuni ikki yuz kishiga palov pishiramiz."),
         P("Malika: Is your job hard? Bekzod: Yes, sometimes. I work twelve hours a day, and the kitchen is very hot. "
           "But I love my job.",
           "Malika: Ishingiz ogʻirmi? Bekzod: Ha, baʼzan. Kuniga oʻn ikki soat ishlayman, oshxona esa juda issiq. "
           "Lekin men ishimni yaxshi koʻraman."),
         P("Malika: Do you cook at home too? Bekzod: Never! At home my wife cooks. "
           "She makes the best mastava in the world.",
           "Malika: Uyda ham ovqat pishirasizmi? Bekzod: Hech qachon! Uyda xotinim ovqat pishiradi. "
           "U dunyodagi eng mazali mastavani tayyorlaydi."),
     ],
     [G('chef', 'oshpaz'), G('restaurant', 'restoran'), G('popular', 'mashhur'), G('hundred', 'yuz (100)'),
      G('hard', 'ogʻir, qiyin'), G('sometimes', 'baʼzan'), G('kitchen', 'oshxona'), G('hot', 'issiq'),
      G('never', 'hech qachon'), G('wife', 'xotin, rafiqa'), G('the best', 'eng yaxshi, eng mazali')],
     [GN('b06-jobs', 'Kasb haqida soʻrash: What is your job?', 'What is your job? … I am a chef.'),
      GN('b07-a-an', 'a / an — kasb oldidan', 'I am a chef.')],
     [
         tf('Bekzod works in a small cafe.', 'F', 'U katta restoranda ishlaydi: «I work in a big restaurant in Tashkent.»', 0),
         ch("Which food is very popular in Bekzod's restaurant?", ['lagman', 'plov', 'shashlik'], 1,
            '«Our plov is very popular.»', 1),
         gap('Every day they cook plov for two ___ people.', 'hundred',
             '«Every day we cook plov for two hundred people.»', 1),
         ch('How many hours does Bekzod work a day?', ['eight', 'ten', 'twelve'], 2,
            '«I work twelve hours a day».', 2),
         gap('The kitchen is very ___.', 'hot', '«the kitchen is very hot».', 2),
         tf('Bekzod cooks at home every day.', 'F', 'Uyda u hech qachon pishirmaydi: «Never! At home my wife cooks.»', 3),
         ch('Who cooks at home?', ['Bekzod', 'his wife', 'his mother'], 1, '«At home my wife cooks.»', 3),
     ])

text(B, 'a1-29-coach', 'Suzish murabbiyi','The Swimming Coach', 'A1', 'biography', JOBS,
     'Bu — suzish murabbiyi Feruza haqida qisqa tarjimai hol. Oʻqishdan oldin: sizning sevimli sport turingiz qaysi?',
     [
         P("Feruza Aliyeva is a swimming coach. She is thirty-five years old and she lives in Namangan. "
           "She works at the city sports centre.",
           "Feruza Aliyeva — suzish murabbiyi. U oʻttiz besh yoshda va Namanganda yashaydi. "
           "U shahar sport markazida ishlaydi."),
         P("Feruza loves water. At the age of seven, she could swim very well. Now she has got forty students. "
           "They are from six to sixty years old!",
           "Feruza suvni yaxshi koʻradi. Yetti yoshidayoq u juda yaxshi suza olardi. Hozir uning qirqta shogirdi bor. "
           "Ular olti yoshdan oltmish yoshgacha!"),
         P("Feruza's day starts early. She gets up at five and runs in the park. Her first lesson is at seven. "
           "She has lunch at one and finishes work at six.",
           "Feruzaning kuni erta boshlanadi. U soat beshda turadi va bogʻda yuguradi. Birinchi darsi soat yettida. "
           "U soat birda tushlik qiladi va ishni soat oltida tugatadi."),
         P("Feruza is a kind but strict coach. She always tells her students: never swim alone, "
           "and always drink water after a lesson.",
           "Feruza mehribon, lekin talabchan murabbiy. U shogirdlariga doim aytadi: hech qachon yolgʻiz suzmang "
           "va darsdan keyin doim suv iching."),
     ],
     [G('coach', 'murabbiy'), G('swimming', 'suzish'), G('sports centre', 'sport markazi'), G('student', 'shogird, oʻquvchi'),
      G('early', 'erta'), G('lesson', 'dars, mashgʻulot'), G('lunch', 'tushlik'), G('finish', 'tugatmoq'),
      G('strict', 'talabchan, qattiqqoʻl'), G('alone', 'yolgʻiz')],
     [GN('b41-can-could', 'could — oʻtmishda qila olardi', 'At the age of seven, she could swim very well.'),
      GN('b19-my-day', 'Present Simple: she gets up', 'She gets up at five and runs in the park.')],
     [
         ch('Where does Feruza live?', ['in Namangan', 'in Tashkent', 'in Fergana'], 0,
            '«she lives in Namangan».', 0),
         tf('Feruza works at a school.', 'F', 'U sport markazida ishlaydi: «She works at the city sports centre.»', 0),
         gap('At the age of ___, Feruza could swim very well.', ['seven', '7'],
             '«At the age of seven, she could swim very well.»', 1),
         ch('How many students has Feruza got?', ['thirty-five', 'forty', 'sixty'], 1,
            '«Now she has got forty students.» Oʻttiz besh — uning yoshi.', 1),
         tf('Feruza runs in the park in the morning.', 'T', '«She gets up at five and runs in the park.»', 2),
         gap('Feruza finishes work at ___.', ['six', '6'], '«She has lunch at one and finishes work at six.»', 2),
         tf('Feruza says her students can swim alone.', 'F', 'Aksincha: «never swim alone».', 3),
     ])

text(B, 'a1-30-new-student', 'Sinfimizdagi yangi oʻquvchi', 'A New Student in Our Class', 'A1', 'email',
     L('Maktab', 'School'),
     'Nilufar dugonasi Azizaga elektron xat yozadi. Oʻqishdan oldin: sinfingizga boshqa davlatdan oʻquvchi kelsa, unga qanday yordam berasiz?',
     [
         P("Hi Aziza, how are you? I have got some news. We have got a new student in our class! "
           "His name is Min-jun, and he is from Seoul, South Korea. His father works in Tashkent now.",
           "Salom, Aziza! Qalaysan? Menda bir yangilik bor. Sinfimizga yangi oʻquvchi keldi! "
           "Uning ismi Min-jun, u Janubiy Koreyaning Seul shahridan. Uning otasi hozir Toshkentda ishlaydi."),
         P("Min-jun is twelve, like me. He is short and he has got black hair and glasses. He is very friendly. "
           "He can speak Korean and English, but he can't speak Uzbek yet.",
           "Min-jun ham men kabi oʻn ikki yoshda. U past boʻyli, sochi qora va koʻzoynak taqadi. U juda samimiy. "
           "U koreys va ingliz tillarida gapira oladi, lekin hali oʻzbekcha gapira olmaydi."),
         P("In the lessons, he sits next to me. I help him with Uzbek words, and he helps me with English. "
           "He is very good at maths and art.",
           "Darslarda u mening yonimda oʻtiradi. Men unga oʻzbekcha soʻzlarda yordam beraman, u esa menga ingliz tilida yordam beradi. "
           "U matematika va tasviriy sanʼatni juda yaxshi biladi."),
         P("Min-jun loves Uzbek food. His favourite is plov! Can you come to our school next week? "
           "You can meet him. Write soon! Nilufar",
           "Min-jun oʻzbek taomlarini juda yaxshi koʻradi. Uning eng sevimlisi — palov! Kelasi hafta maktabimizga kela olasanmi? "
           "U bilan tanishasan. Tezroq javob yoz! Nilufar"),
     ],
     [G('news', 'yangilik'), G('new', 'yangi'), G('short', 'past boʻyli'), G('friendly', 'samimiy, doʻstona'),
      G('speak', 'gapirmoq'), G('yet', 'hali (inkorda)'), G('next to', 'yonida'), G('be good at', '… ni yaxshi bilmoq'),
      G('favourite', 'sevimli'), G('meet', 'tanishmoq, uchrashmoq')],
     [GN('b02-countries', 'Qayerdan: he is from …', 'His name is Min-jun, and he is from Seoul, South Korea.'),
      GN('b29-can', 'can / can’t — qila olmoq / qila olmaslik',
         "He can speak Korean and English, but he can't speak Uzbek yet.")],
     [
         tf('The new student is from Japan.', 'F', 'U Koreyadan: «he is from Seoul, South Korea».', 0),
         ch('Why is Min-jun in Tashkent?', ['His father works there.', 'He likes plov.', 'His grandmother lives there.'], 0,
            '«His father works in Tashkent now.»', 0),
         tf('Min-jun is twelve years old.', 'T', '«Min-jun is twelve, like me.»', 1),
         ch("Which language can't Min-jun speak?", ['Korean', 'English', 'Uzbek'], 2,
            '«he can\'t speak Uzbek yet».', 1),
         gap('In the lessons, Min-jun sits ___ to Nilufar.', 'next', '«In the lessons, he sits next to me.»', 2),
         ch('What is Min-jun good at?', ['maths and art', 'music and sport', 'Uzbek and history'], 0,
            '«He is very good at maths and art.»', 2),
         gap("Min-jun's favourite Uzbek food is ___.", 'plov', '«His favourite is plov!»', 3),
     ])
