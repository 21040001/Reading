"""B2 · 1-boʻlim: Imtihon formatlari bilan tanishuv (IELTS / Multilevel tarzidagi topshiriqlar)"""
from lib import *

B = 'b2'

TFNG_INTRO = ('Topshiriq: True / False / Not Given. TRUE — matn shuni aytadi; FALSE — matn buning aksini aytadi; '
              'NOT GIVEN — matnda bu haqda maʼlumot yoʻq. Oʻz bilimingizga emas, faqat matnga tayaning!')

text(B, 'b2-01-aral', 'Orol dengizi qaytadimi?', 'The Aral Sea: Can a Lost Sea Return?', 'B2', 'exam',
     L('Atrof-muhit', 'Environment'), TFNG_INTRO,
     [
         P("In 1960, the Aral Sea was the fourth-largest lake in the world. Fishing villages lined its shores, and the "
           "port of Muynak, in Karakalpakstan, sent fish to every corner of the Soviet Union. Today, visitors to "
           "Muynak find rusting ships sitting on sand, many kilometres from the nearest water."),
         P("The cause of the disaster is well known. From the 1960s, water from the region's two great rivers, the Amu Darya "
           "and the Syr Darya, was diverted to irrigate huge cotton fields. With far less fresh water flowing in, the sea began "
           "to shrink and its water became saltier. By the late 1980s, it had split into two separate parts."),
         P("The consequences went far beyond the loss of fish. As the water disappeared, it left behind a new desert, now often "
           "called the Aralkum. Strong winds lift salt and dust from the dry seabed and carry them hundreds of kilometres, "
           "damaging crops and, according to doctors in the region, contributing to breathing problems."),
         P("Yet the story is not entirely hopeless. In 2005, Kazakhstan completed a dam that separates the small northern part "
           "of the sea from the south. Water levels behind the dam rose, the water became less salty, and fish returned. "
           "Some local fishermen have gone back to work."),
         P("Recovering the much larger southern part is a different challenge. Instead of trying to bring the water back, "
           "Uzbekistan has focused on planting drought-resistant plants such as saxaul on the dry seabed. Their roots hold "
           "the soil in place and reduce dust storms. Scientists say this will not restore the sea, but it may make the region "
           "a healthier place to live."),
     ],
     [G('line the shores', 'qirgʻoq boʻylab joylashmoq'), G('rusting', 'zanglayotgan'), G('divert', '(suvni) boshqa tomonga burmoq'),
      G('irrigate', 'sugʻormoq'), G('shrink', 'kichraymoq, qisqarmoq'), G('split', 'boʻlinmoq'),
      G('consequence', 'oqibat'), G('seabed', 'dengiz tubi'), G('contribute to', '… ga sabab boʻlmoq, hissa qoʻshmoq'),
      G('dam', 'toʻgʻon'), G('drought-resistant', 'qurgʻoqchilikka chidamli'), G('saxaul', 'saksovul'),
      G('restore', 'tiklamoq')],
     [GN('i11-past-perfect', 'Past Perfect: had split', 'By the late 1980s, it had split into two separate parts.'),
      GN('i29-passive-basics', 'Majhul nisbat: was diverted', 'Water … was diverted to irrigate huge cotton fields.')],
     [
         tf('The Aral Sea was once among the five largest lakes in the world.', 'T',
            '«the fourth-largest lake in the world» — toʻrtinchi, demak beshtalikda.', 0),
         tf('Muynak is still an important fishing port today.', 'F',
            'Bugun kemalar qum ustida, suv kilometrlab uzoqda — port emas.', 0),
         tf('Water used for cotton farming would otherwise have flowed into the sea.', 'T',
            'Daryolar suvi paxta dalalariga burilgani uchun dengizga kamroq suv kelgan (2-xatboshi).', 1),
         tf('In the 1980s, the Soviet government made a plan to save the sea.', 'NG',
            'Matnda hukumat rejasi haqida hech narsa aytilmagan — Not Given.', 1),
         tf('Dust from the dry seabed affects places far away from the sea.', 'T',
            '«carry them hundreds of kilometres» — yuzlab kilometrga yetadi.', 2),
         tf('Kazakhstan paid for the dam without any help from other countries.', 'NG',
            'Toʻgʻonni Qozogʻiston qurgani aytilgan, kim pul toʻlagani haqida maʼlumot yoʻq.', 3),
         tf('After 2005, fish disappeared again from the northern part of the sea.', 'F',
            'Aksincha: «fish returned» — baliqlar qaytgan.', 3),
         hd(2, ['Effects beyond fishing', 'A plan from the government', 'Life in Muynak today'], 0,
            '3-xatboshi baliqdan tashqari oqibatlar haqida: yangi choʻl, chang, sogʻliq.'),
         gap('Uzbekistan is planting drought-resistant plants such as ___ on the dry seabed.', 'saxaul',
             '5-xatboshi: «plants such as saxaul».', 4, 1),
         gap('The roots of these plants help to reduce ___.', ['dust storms', 'dust'],
             '«Their roots hold the soil in place and reduce dust storms.»', 4, 2),
         gap('Scientists believe that the planting will not ___ the sea.', ['restore', 'bring back'],
             '«this will not restore the sea» — dengizni tiklamaydi, lekin hududni sogʻlomroq qiladi.', 4, 2),
     ])

HEAD_INTRO = ('Topshiriq: Matching headings. Har bir xatboshi uchun eng mos sarlavhani tanlang. Avval xatboshining asosiy '
              'gʻoyasini bitta jumlada oʻzingizga ayting, keyin sarlavhalarni oʻqing. Bitta soʻz mos kelgani yetarli emas!')

HEADINGS = ['A rediscovery', 'A ruler who preferred science', 'Bigger meant more accurate',
            'A lasting scientific achievement', 'The end of a great project', 'Teaching astronomy to children']

text(B, 'b2-02-ulugh-beg', 'Ulugʻbek rasadxonasi', "Ulugh Beg's Observatory", 'B2', 'exam',
     L('Tarix va fan', 'History and science'), HEAD_INTRO,
     [
         P("In the 1420s, the governor of Samarkand did something unusual for a ruler: he built a scientific institution. Mirzo "
           "Ulugh Beg, the grandson of Amir Temur, was more interested in the stars than in war. On a hill outside the city, "
           "he constructed an observatory that was one of the most advanced in the world at that time."),
         P("The heart of the building was an enormous instrument, a curved structure cut partly into the rock, with a radius "
           "of around forty metres. Using it, astronomers could measure the position of the Sun and other celestial bodies with "
           "remarkable accuracy. Because there were no telescopes yet, size was the key to precision: the bigger the instrument, "
           "the smaller the errors."),
         P("The most famous result of this work was a star catalogue listing the positions of about a thousand stars. It was "
           "the most accurate star catalogue made since ancient times, and scholars continued to study it for centuries. Ulugh Beg and "
           "his team also calculated the length of the year with an error of only about a minute."),
         P("Sadly, the observatory did not survive its creator for long. After Ulugh Beg was killed in 1449, the building was "
           "abandoned and gradually destroyed. For more than four centuries, its exact location was forgotten."),
         P("In 1908, the archaeologist Vasily Vyatkin found the remains of the great instrument underground. Today, visitors to "
           "Samarkand can walk down into the surviving part of it and visit a small museum nearby, which tells the story of a "
           "ruler who chose science."),
     ],
     [G('ruler', 'hukmdor'), G('institution', 'muassasa'), G('observatory', 'rasadxona'), G('enormous', 'ulkan'),
      G('curved', 'egri, yoysimon'), G('radius', 'radius'), G('accuracy / precision', 'aniqlik'),
      G('catalogue', 'katalog, roʻyxat'), G('scholar', 'olim'), G('survive', 'saqlanib qolmoq; omon qolmoq'),
      G('abandon', 'tashlab ketmoq'), G('gradually', 'asta-sekin'), G('remains', 'qoldiqlar')],
     [GN('i60-the-more', 'the bigger …, the smaller …', 'the bigger the instrument, the smaller the errors'),
      GN('i30-passive-tenses', 'Majhul nisbat: was killed, was abandoned', 'the building was abandoned and gradually destroyed')],
     [
         hd(0, HEADINGS, 1, 'Xatboshi A: Ulugʻbek urushdan koʻra yulduzlarga qiziqqan hukmdor.'),
         hd(1, HEADINGS, 2, 'Xatboshi B: asbob qancha katta boʻlsa, xato shuncha kam.'),
         hd(2, HEADINGS, 3, 'Xatboshi C: yulduzlar katalogi asrlar davomida oʻrganilgan — ahamiyatini yoʻqotmagan yutuq.'),
         hd(3, HEADINGS, 4, 'Xatboshi D: Ulugʻbek oʻlimidan keyin rasadxona tashlab ketilgan va buzilgan.'),
         hd(4, HEADINGS, 0, 'Xatboshi E: 1908-yilda Vyatkin qoldiqlarni topgan — qayta kashfiyot.'),
         ch('Why was the main instrument so large?',
            ['to impress visitors to Samarkand', 'because a larger instrument gave more accurate results',
             'because it had to be cut into the rock'], 1,
            '«size was the key to precision: the bigger the instrument, the smaller the errors».', 1),
         tf('Ulugh Beg used telescopes to observe the stars.', 'F', '«there were no telescopes yet» — teleskop hali yoʻq edi.', 1, ng=True),
         tf("Ulugh Beg's team included more than a hundred astronomers.", 'NG',
            'Matnda «his team» deyilgan, lekin necha kishi ekani aytilmagan.', 2),
         ch('What happened after Ulugh Beg died?',
            ['The observatory was moved to Bukhara.', 'The building was left and slowly destroyed.',
             'His students built a new observatory.'], 1, '«the building was abandoned and gradually destroyed».', 3),
         gap('Near the remains of the instrument, visitors can also see a small ___.', 'museum',
             '«visit a small museum nearby».', 4, 1),
     ])
