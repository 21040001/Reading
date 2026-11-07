"""B2 · 2-boʻlim: True / False / Not Given"""
from lib import *

B = 'b2'

# ---------------------------------------------------------------- b2-06-tea
text(B, 'b2-06-tea', 'Choy tarixi', 'The Story of Tea', 'B2', 'exam',
     L('Madaniyat va tarix', 'Culture and history'),
     'Topshiriq: True / False / Not Given. TFNG savollari odatda matndagi tartib bilan keladi: bitta savolning javobini '
     'topgach, keyingisini shu joydan keyin qidiring. Agar ikki savol orasida javob topilmasa, ehtimol u NOT GIVEN.',
     [
         P("Few drinks have travelled as far as tea. The tea plant is thought to come from south-western China, and "
           "according to Chinese tradition, people there were drinking an infusion of its leaves thousands of years ago, "
           "at first mainly as a medicine rather than for pleasure. Over many centuries, the habit spread across the country, and tea gradually became part of "
           "everyday life, served in homes, at markets and during ceremonies."),
         P("From China, tea moved outwards along trade routes. Merchants carried it by land through Central Asia and by "
           "sea to other parts of Asia. Because the leaves were light and kept well when dried or pressed into blocks, "
           "they were an ideal product for long journeys. In some regions, pressed tea was so valued that it was even "
           "used in place of money. Much later, sea traders brought tea to Europe, where it was at first an expensive "
           "luxury enjoyed only by the wealthy."),
         P("In Central Asia, tea became far more than a drink. In Uzbekistan, green tea is the most common choice, "
           "although black tea is also popular in some places. Tea is offered to every guest, often "
           "before any serious conversation begins, and refusing it may be seen as impolite."),
         P("The traditional place for drinking tea outside the home is the choyxona, or teahouse. Often built near water "
           "and shaded by trees, it has wide raised platforms covered with carpets, where visitors sit, talk and share "
           "food for hours. For many communities, the choyxona has long served as a meeting place where news is "
           "exchanged and local matters are discussed."),
         P("Tea is normally served from a single teapot and shared by everyone at the table. The host pours, usually "
           "filling each small bowl, known as a piyola, only partly, so that the tea stays hot and the host has a reason "
           "to keep returning to the guest. A full bowl, in fact, is sometimes said to be a polite hint that the visitor "
           "should leave. Before serving, many hosts pour tea into a bowl and return it to the pot two or three times. This "
           "custom, called qaytarish, helps the leaves brew evenly and is said to make the flavour stronger."),
         P("Today, tea bags and modern cafes are common in Central Asian cities, and some younger people prefer coffee "
           "in certain situations. Yet the teapot on the table remains a symbol of hospitality, and for many families "
           "no meal feels complete without it."),
     ],
     [G('infusion', 'damlama, qaynoq suvda dimlangan ichimlik'), G('gradually', 'asta-sekin'),
      G('trade route', 'savdo yoʻli'), G('merchant', 'savdogar'), G('pressed', 'presslangan, siqilgan'),
      G('in place of', 'oʻrniga'), G('luxury', 'hashamat, qimmatbaho narsa'), G('the wealthy', 'boylar'),
      G('impolite', 'odobsiz, beadab'), G('platform', 'soʻri, supa'), G('exchange', 'almashmoq'),
      G('hint', 'ishora'), G('brew', 'damlanmoq'), G('evenly', 'bir tekis'), G('hospitality', 'mehmondoʻstlik')],
     [GN('i29-passive-basics', 'Majhul nisbat: is offered, may be seen', 'Tea is offered to every guest'),
      GN('i64-so-that-in-order-to', 'Maqsad: so that', 'so that the tea stays hot')],
     [
         tf('In early China, tea was valued more for its effect on health than for its taste.', 'T',
            '«at first mainly as a medicine rather than for pleasure» — avval dori sifatida, zavq uchun emas.', 0, ng=True),
         tf('Tea was suitable for long-distance trade partly because it did not spoil easily.', 'T',
            '«kept well when dried or pressed into blocks … an ideal product for long journeys» — «kept well» = tez buzilmagan.', 1, ng=True),
         tf('Merchants who carried tea by land earned more than those who transported it by sea.', 'NG',
            'Quruqlik va dengiz yoʻllari tilga olingan, lekin savdogarlarning daromadi solishtirilmagan. '
            'Tuzoq: matndagi soʻzlar (merchants, by land, by sea) bor, ammo daromad haqida maʼlumot yoʻq.', 1),
         tf('When tea first arrived in Europe, it was drunk by people of all social classes.', 'F',
            '«an expensive luxury enjoyed only by the wealthy» — faqat boylar ichgan, hamma emas.', 1, ng=True),
         tf('Black tea is never drunk in Uzbekistan.', 'F',
            '«although black tea is also popular in some places» — baʼzi joylarda qora choy ham mashhur.', 2, ng=True),
         tf('Turning down tea that is offered can be considered rude.', 'T',
            '«refusing it may be seen as impolite» — turning down = refusing, rude = impolite.', 2, ng=True),
         tf('The number of choyxonas in Central Asia has fallen in recent years.', 'NG',
            'Choyxona qanday joy ekani tasvirlangan, lekin ularning soni kamaygani yoki koʻpaygani haqida hech narsa yoʻq. '
            'Oxirgi xatboshidagi «modern cafes» ham choyxonalar soni haqida emas.', 3),
         tf('A host who fills a guest\'s bowl to the top may be suggesting that the visit should end.', 'T',
            '«A full bowl … is sometimes said to be a polite hint that the visitor should leave» — «may be suggesting» ham '
            'ehtiyotkor ifoda.', 4, ng=True),
         gap('In Uzbekistan, tea is drunk from a small bowl called a ___.', 'piyola',
             '«each small bowl, known as a piyola».', 4, 1),
         gap('Pouring tea into a bowl and back into the pot several times is known as ___.', 'qaytarish',
             '«This custom, called qaytarish».', 4, 1),
         ch('Why does the host usually fill the bowl only partly?',
            ['to save tea for other guests', 'to keep the tea hot and have a reason to return to the guest',
             'because the bowls are too small', 'to make the flavour stronger'], 1,
            '«so that the tea stays hot and the host has a reason to keep returning to the guest». '
            '«flavour stronger» qaytarish odatiga tegishli, kosani toʻla quymaslikka emas.', 4),
     ])

# ---------------------------------------------------------------- b2-07-bilingual-brain
text(B, 'b2-07-bilingual-brain', 'Ikki tilli miya', 'The Bilingual Brain', 'B2', 'exam',
     L('Fan va til', 'Science and language'),
     'Topshiriq: True / False / Not Given. FALSE va NOT GIVEN farqini shunday tekshiring: matnda gapga zid jumlani '
     'barmogʻingiz bilan koʻrsata olasizmi? Koʻrsata olsangiz — FALSE; bunday jumla umuman boʻlmasa — NOT GIVEN.',
     [
         P("For much of the twentieth century, many parents and teachers worried that learning two languages in early "
           "childhood might confuse children or slow down their development. Today, most specialists reject this view. "
           "Children who grow up with two languages sometimes mix words from both in a single sentence, but this is "
           "generally regarded as a normal stage rather than a sign of a problem."),
         P("One question that has long interested researchers is how bilingual people keep their languages apart. "
           "Studies suggest that both languages remain active in the mind even when only one of them is being used. "
           "A bilingual speaker reading in English, for example, may unconsciously activate similar words in her other "
           "language. Many researchers believe that, for a person to speak fluently, the brain has to select one language "
           "and hold back the other, a process that happens so quickly that the speaker rarely notices it."),
         P("Switching between languages, then, is not a sign of weakness. Many bilinguals change language in the middle "
           "of a conversation, depending on the topic or the person they are talking to. Linguists point out that this "
           "kind of switching usually follows regular patterns and often requires considerable skill. Speakers may switch to express an idea that feels more natural in one "
           "language, or to show that they belong to a particular group."),
         P("Because bilinguals constantly practise controlling two languages, some scientists have proposed that they may "
           "develop stronger executive control, the set of mental abilities that help us focus attention, ignore "
           "distractions and move between tasks. Early experiments appeared to support this idea, and it quickly became "
           "popular in newspapers and magazines. It was an attractive idea, since it suggested that an everyday "
           "experience could have hidden benefits for the mind."),
         P("However, the picture has since become less clear. Several later studies, often with larger groups of "
           "participants, failed to find the same advantage, and some researchers now argue that the effect is small or "
           "may not exist at all. Others reply that bilingualism takes many forms and that results may depend on how "
           "often people use each language. The debate is far from settled."),
         P("What is not disputed is that knowing two languages brings practical and cultural benefits, from wider career "
           "opportunities to closer contact with family and community. Whether or not it also trains the brain, for a "
           "large part of the world's population, living with two languages is simply ordinary life."),
     ],
     [G('confuse', 'chalkashtirmoq'), G('reject', 'rad etmoq'), G('regard as', '… deb hisoblamoq'),
      G('remain', 'qolmoq'), G('unconsciously', 'ongsiz ravishda'), G('fluently', 'ravon'),
      G('hold back', 'tiyib turmoq, bosib turmoq'), G('considerable', 'katta, salmoqli'),
      G('propose', 'taklif qilmoq, ilgari surmoq'), G('executive control', 'ijro nazorati (diqqatni boshqarish)'),
      G('distraction', 'chalgʻituvchi narsa'), G('participant', 'ishtirokchi'), G('advantage', 'ustunlik'),
      G('settled', 'hal qilingan'), G('dispute', 'bahslashmoq, shubha ostiga olmoq')],
     [GN('c09-probability-deduction', 'Ehtimollik: may develop, may not exist', 'the effect is small or may not exist at all'),
      GN('i30-passive-tenses', 'Majhul nisbat: is being used', 'even when only one of them is being used')],
     [
         tf('In the past, it was widely believed that growing up with two languages could harm a child.', 'T',
            '«many parents and teachers worried that learning two languages … might confuse children or slow down their '
            'development» — harm = confuse / slow down.', 0, ng=True),
         tf('Children who mix two languages in one sentence are now thought to have a language disorder.', 'F',
            '«regarded as a normal stage rather than a sign of a problem» — muammo belgisi emas, normal bosqich.', 0, ng=True),
         tf('Bilingual children usually learn to read earlier than other children.', 'NG',
            'Matnda oʻqishni qachon oʻrganish haqida hech narsa yoʻq. Bunday daʼvo na tasdiqlangan, na rad etilgan.', 0),
         tf('When a bilingual person uses one language, the other one is completely switched off.', 'F',
            '«both languages remain active in the mind even when only one of them is being used».', 1, ng=True),
         tf('Bilingual speakers are normally aware of the effort of suppressing one of their languages.', 'F',
            '«a process that happens so quickly that the speaker rarely notices it» — odatda sezmaydi.', 1, ng=True),
         tf('The choice of language in a conversation can depend on who the listener is.', 'T',
            '«depending on the topic or the person they are talking to».', 2, ng=True),
         tf('The first experiments on executive control in bilinguals were carried out with elderly people.', 'NG',
            '«Early experiments» haqida faqat ular gʻoyani qoʻllab-quvvatlagani aytilgan; ishtirokchilar yoshi haqida maʼlumot yoʻq.', 3),
         tf('Some researchers think that how often bilinguals use each language may affect the results.', 'T',
            '«results may depend on how often people use each language».', 4, ng=True),
         gap('The mental abilities that help us focus and move between tasks are called ___.', 'executive control',
             '«executive control, the set of mental abilities that help us focus attention …».', 3, 2),
         gap('According to linguists, switching languages usually follows regular ___.', 'patterns',
             '«this kind of switching usually follows regular patterns».', 2, 1),
         ch('What is the writer\'s view of the idea that bilingualism improves executive control?',
            ['It has been clearly proved by later studies.', 'It is still uncertain and being debated.',
             'It was invented by newspapers and magazines.', 'It has been completely rejected by scientists.'], 1,
            '«The debate is far from settled» — hali hal boʻlmagan. Gazetalar gʻoyani faqat ommalashtirgan, '
            'oʻylab topmagan; «some researchers» rad etadi, lekin hammasi emas.', 4),
     ])

# ---------------------------------------------------------------- b2-08-desert-plants
text(B, 'b2-08-desert-plants', 'Choʻl oʻsimliklari', 'Plants of the Desert', 'B2', 'exam',
     L('Tabiat', 'Nature'),
     'Topshiriq: True / False / Not Given. Savoldagi «cheklovchi» soʻzlarga eʼtibor bering: all, only, never, always, most. '
     'Matnda «some» deyilib, qolganlari boshqacha ekani ham koʻrsatilgan boʻlsa, savoldagi «all» FALSE boʻladi; '
     'boshqalar haqida hech narsa deyilmagan boʻlsa — NOT GIVEN.',
     [
         P("Deserts are among the harshest environments on Earth. Rain is rare and unpredictable, summer temperatures can "
           "be extreme, and the soil is often sandy or salty. Yet many plants not only survive in such conditions but "
           "thrive, thanks to adaptations that have developed over a very long time. Broadly, these plants face three challenges: finding water, keeping it and protecting it."),
         P("One of the most common strategies is to reach water that other plants cannot. Some desert shrubs send their "
           "roots deep underground, sometimes many metres down, until they find moisture far below the surface. Others "
           "take the opposite approach, spreading a wide network of shallow roots just beneath the ground so that they "
           "can absorb rain quickly before it evaporates."),
         P("Leaves present a particular problem, because plants lose water through them. Many desert species therefore "
           "have very small leaves, or almost none at all, and carry out much of their photosynthesis in green stems "
           "instead. Leaves that do exist are often covered with a waxy layer that slows the loss of water, and some "
           "plants close the tiny openings on their leaves during the hottest part of the day."),
         P("Another group of plants stores water when it is available. Cacti, which are native to the Americas, are the "
           "best-known example: their thick, fleshy stems can hold large amounts of water, which the plant uses slowly "
           "during dry periods. Sharp spines, rather than ordinary leaves, help to protect this precious supply from "
           "thirsty animals. Their roots, by contrast, are usually shallow and spread widely, ready to catch even light rain."),
         P("In the Kyzylkum desert, which lies mainly in Uzbekistan and Kazakhstan, two plants are particularly well adapted. The saxaul, a "
           "small tree with very hard wood, has tiny scale-like leaves and long roots, which allow it to grow on shifting "
           "sand. Because its roots bind the sand together, it has been planted to slow the movement of dunes. Its wood burns slowly and has traditionally been used as fuel. Tamarisk, "
           "a shrub with feathery branches and pink flowers, can tolerate salty soil and is common along rivers and dry riverbeds."),
         P("Some desert plants avoid drought altogether. Their seeds can lie in the soil for long periods, sometimes for "
           "years, waiting for enough rain. When a heavy shower finally arrives, they germinate, grow, flower and produce "
           "new seeds within a few weeks, before the ground dries out again. After a rare wet spring, a desert that "
           "looked empty can suddenly be covered in flowers."),
     ],
     [G('harsh', 'ogʻir, qattiq'), G('unpredictable', 'oldindan aytib boʻlmaydigan'), G('thrive', 'yaxshi oʻsmoq, gullab-yashnamoq'),
      G('adaptation', 'moslashuv'), G('shrub', 'buta'), G('moisture', 'namlik'), G('shallow', 'sayoz, chuqur boʻlmagan'),
      G('absorb', 'shimmoq'), G('evaporate', 'bugʻlanmoq'), G('waxy', 'mumsimon'), G('fleshy', 'etdor, sersuv'),
      G('spine', 'tikan'), G('shifting', 'koʻchib yuradigan'), G('bind', 'bogʻlab turmoq'),
      G('saxaul', 'saksovul'), G('tamarisk', 'yulgʻun'), G('tolerate', 'chidamoq'), G('germinate', 'unib chiqmoq')],
     [GN('i55-non-defining', 'Qoʻshimcha aniqlovchi ergash gap: which are …', 'Cacti, which are native to the Americas, are the best-known example'),
      GN('c46-contrast-concession', 'Qarama-qarshilik: by contrast', 'Their roots, by contrast, are usually shallow')],
     [
         tf('Rain in the desert is both infrequent and difficult to forecast.', 'T',
            '«Rain is rare and unpredictable» — infrequent = rare, difficult to forecast = unpredictable.', 0, ng=True),
         tf('All desert plants depend on deep roots to find water.', 'F',
            '«Some … send their roots deep … Others … shallow roots» — hammasi emas, baʼzilari sayoz ildizli.', 1, ng=True),
         tf('Shallow roots help some plants collect rainwater before it disappears into the air.', 'T',
            '«absorb rain quickly before it evaporates» — evaporate = havoga bugʻlanib ketmoq.', 1, ng=True),
         tf('Desert plants that have leaves have no way of reducing the water lost through them.', 'F',
            '«covered with a waxy layer that slows the loss of water» va «close the tiny openings … during the hottest part '
            'of the day» — suv yoʻqotishni kamaytirish usullari bor.', 2, ng=True),
         tf('The spines of cacti contain a substance that is poisonous to animals.', 'NG',
            'Tikanlar suvni hayvonlardan himoya qiladi, deyilgan; zahar haqida hech narsa yoʻq.', 3),
         tf('Saxaul was first planted on sand dunes by foreign scientists.', 'NG',
            '«it has been planted to slow the movement of dunes» — kim va qachon birinchi ekkani aytilmagan.', 4),
         tf('Tamarisk is unable to grow in soil that contains salt.', 'F',
            '«can tolerate salty soil» — shoʻr tuproqqa chidaydi.', 4, ng=True),
         tf('The seeds of some desert plants can survive in the ground for several years.', 'T',
            '«Their seeds can lie in the soil for long periods, sometimes for years».', 5, ng=True),
         gap('Desert leaves are often protected by a ___ layer that reduces water loss.', 'waxy',
             '«covered with a waxy layer that slows the loss of water».', 2, 1),
         gap('The saxaul has tiny ___ leaves.', ['scale-like'],
             '«has tiny scale-like leaves».', 4, 1),
         ch('What is the main point of the last paragraph?',
            ['Desert flowers last for many months.', 'Some plants survive drought by waiting as seeds for rain.',
             'Heavy showers often destroy desert plants.', 'Deserts are completely empty in spring.'], 1,
            '«Some desert plants avoid drought altogether … seeds … waiting for enough rain». Gullar bir necha hafta '
            'ichida paydo boʻladi, oylab emas; choʻl faqat «looked empty» — boʻsh koʻringan.', 5),
     ])

# ---------------------------------------------------------------- b2-09-food-waste
text(B, 'b2-09-food-waste', 'Ovqat isrofi', 'Wasted Food', 'B2', 'exam',
     L('Jamiyat va atrof-muhit', 'Society and environment'),
     'Topshiriq: True / False / Not Given. Sabab-natija tuzogʻidan ehtiyot boʻling: savolda matndagi ikki fakt toʻgʻri '
     'boʻlishi mumkin, lekin ular orasidagi «because» bogʻlanishi notoʻgʻri koʻrsatilgan. Faqat faktlarni emas, '
     'sababni ham matn bilan solishtiring.',
     [
         P("A large share of the food produced around the world is never eaten. It is lost or thrown away at almost every "
           "stage between the farm and the plate, and when this happens, the water, energy, land and labour used to "
           "produce it are wasted as well. Food that rots in landfill sites also releases methane, a powerful "
           "greenhouse gas."),
         P("Some of the loss occurs before food even leaves the farm. Crops may be damaged by pests or bad weather, or "
           "simply left unharvested when market prices are too low to cover the cost of picking them. Some produce is also damaged during harvesting or packing. In places where "
           "roads and storage facilities are poor, fruit and vegetables can spoil on the way to market, especially in "
           "hot climates without refrigeration."),
         P("Supermarkets contribute in other ways. Many shops reject produce that is the wrong shape or size, even though "
           "it is perfectly safe to eat, because they believe customers will not buy it. Special offers that encourage "
           "people to buy more than they need may simply move waste from the shop to the home. Confusion about date "
           "labels adds to the problem: a best-before date refers to quality rather than safety, yet many people throw "
           "food away as soon as this date has passed."),
         P("In wealthier countries, households are thought to be responsible for a significant part of all food waste. "
           "People buy too much, forget what is in the fridge, cook larger portions than they can eat, or throw away "
           "leftovers. Because each family wastes only a little at a time, the problem is easy to overlook, but across a "
           "whole country the amounts are considerable."),
         P("A number of solutions are being tried. Food banks collect surplus food from shops, restaurants and producers "
           "and pass it on to people in need. Some cities have introduced separate collection of food scraps, which can "
           "be composted and returned to the soil as fertiliser. In some places, shops now sell imperfect vegetables at "
           "lower prices instead of rejecting them. Restaurants, too, can cut waste by offering smaller portions."),
         P("Experts generally agree that preventing waste is better than dealing with it afterwards. Simple habits, such "
           "as planning meals, writing a shopping list and storing food properly, can make a real difference. In many "
           "traditional cultures, including that of Uzbekistan, where bread is treated with great respect and should never "
           "be thrown away, wasting food has long been considered wrong."),
     ],
     [G('share', 'ulush'), G('labour', 'mehnat'), G('landfill', 'chiqindixona'), G('release', 'chiqarmoq, ajratmoq'),
      G('pest', 'zararkunanda'), G('unharvested', 'yigʻib olinmagan'), G('spoil', 'buzilmoq, aynimoq'),
      G('refrigeration', 'sovutish'), G('reject', 'rad etmoq, qabul qilmaslik'), G('produce', 'meva-sabzavot; ishlab chiqarmoq'),
      G('leftovers', 'ortib qolgan ovqat'), G('overlook', 'eʼtibordan chetda qoldirmoq'), G('surplus', 'ortiqcha'),
      G('compost', 'kompost qilmoq (chiritib oʻgʻitga aylantirmoq)'), G('fertiliser', 'oʻgʻit')],
     [GN('i31-it-is-said', 'Majhul: are thought to be', 'households are thought to be responsible for a significant part'),
      GN('i61-although-despite', 'even though / yet', 'even though it is perfectly safe to eat')],
     [
         tf('When food is wasted, the resources used to produce it are lost too.', 'T',
            '«the water, energy, land and labour used to produce it are wasted as well».', 0, ng=True),
         tf('Farmers sometimes leave crops in the fields because picking them would cost more than they could earn.', 'T',
            '«left unharvested when market prices are too low to cover the cost of picking them».', 1, ng=True),
         tf('Food is more likely to spoil during transport in cold countries than in hot ones.', 'F',
            '«especially in hot climates without refrigeration» — aksincha, issiq iqlimda.', 1, ng=True),
         tf('Supermarkets refuse oddly shaped produce because it is unsafe to eat.', 'F',
            'Sabab-natija tuzogʻi: «even though it is perfectly safe to eat, because they believe customers will not buy it» — '
            'sabab xavfsizlik emas, xaridorlar olmaydi degan fikr.', 2, ng=True),
         tf('Most customers would happily buy misshapen vegetables if shops offered them.', 'NG',
            'Matnda faqat doʻkonlar nima deb oʻylashi aytilgan; xaridorlarning haqiqiy fikri haqida maʼlumot yoʻq.', 2),
         tf('Food that has passed its best-before date is dangerous to eat.', 'F',
            '«a best-before date refers to quality rather than safety» — xavfsizlik haqida emas.', 2, ng=True),
         tf('Household food waste is easy to miss because each family throws away small amounts at a time.', 'T',
            '«Because each family wastes only a little at a time, the problem is easy to overlook».', 3, ng=True),
         tf('Restaurants that offer smaller portions have attracted more customers.', 'NG',
            'Restoranlar kichikroq porsiya bilan isrofni kamaytirishi mumkinligi aytilgan, lekin mijozlar soni haqida '
            'hech narsa yoʻq.', 4),
         gap('Rotting food in landfill sites produces a greenhouse gas called ___.', 'methane',
             '«releases methane, a powerful greenhouse gas».', 0, 1),
         gap('Composted food scraps can be returned to the soil as ___.', ['fertiliser', 'fertilizer'],
             '«composted and returned to the soil as fertiliser».', 4, 1),
         ch('What does the writer suggest in the final paragraph?',
            ['Food banks are the best answer to food waste.', 'Avoiding waste in the first place is the most effective approach.',
             'Traditional cultures waste more food than modern ones.', 'Shopping lists are rarely useful.'], 1,
            '«preventing waste is better than dealing with it afterwards». Food banks oldingi xatboshida, '
            'eng yaxshi yechim deb aytilmagan; anʼanaviy madaniyatlar aksincha isrofni yomon deb biladi.', 5),
     ])

# ---------------------------------------------------------------- b2-10-city-noise
text(B, 'b2-10-city-noise', 'Shaharlar shovqini', 'The Noise of the City', 'B2', 'exam',
     L('Shahar hayoti va sogʻliq', 'City life and health'),
     'Topshiriq: True / False / Not Given. Ehtiyotkor soʻzlarga qarang: matnda «may», «some studies suggest», '
     '«possible» kabi soʻzlar boʻlsa, savoldagi qatʼiy daʼvo («proved», «always», «causes») koʻpincha FALSE boʻladi.',
     [
         P("For most people who live in cities, noise is so constant that they hardly notice it: traffic, building work, "
           "aircraft overhead, music from neighbouring flats. Yet noise is increasingly treated as a form of pollution, "
           "alongside dirty air and water, and many health organisations now regard it as a genuine environmental "
           "problem rather than a mere annoyance. Unlike smoke, however, noise leaves no visible trace, which may be one reason why it "
           "was ignored for so long."),
         P("One of the clearest concerns is sleep. Even when people do not wake up, loud sounds at night can disturb the "
           "quality of their sleep, and those who live near busy roads or airports often report feeling tired during the "
           "day. Over time, poor sleep may affect concentration, mood and general well-being. Children and older people may be especially sensitive to these effects."),
         P("Researchers have also linked long-term exposure to noise with stress. Unwanted sound can trigger the body's "
           "stress response, raising the heart rate even while a person is asleep. Some studies suggest a possible "
           "connection between constant traffic noise and heart problems, although scientists point out that other "
           "factors, such as diet and the air pollution that often accompanies traffic, make such a link difficult to prove."),
         P("Cities have responded in different ways. Some have created quiet zones, areas such as parks or residential "
           "streets where noisy activities are restricted, and have introduced rules limiting building work at night. In many places, residents can also report excessive noise to local authorities. "
           "Maps showing the noise levels of different streets can help planners decide where new schools and hospitals "
           "should be placed."),
         P("Physical solutions are also widely used. Walls along motorways reflect or absorb sound before it reaches nearby "
           "homes. Trees and bushes are often planted for the same purpose, but a narrow row of trees reduces noise less "
           "than many people imagine. Wide, dense belts of vegetation work better, and greenery can also make a place "
           "feel calmer, which may change how loud it seems."),
         P("Since much traffic noise comes from tyres rolling on the road, engineers have developed quieter road surfaces "
           "that contain more air spaces to absorb some of the sound. Their disadvantage is that they may wear out faster "
           "and need replacing more often. Electric vehicles are quieter at low speeds, but at higher speeds tyre noise "
           "dominates, so they alone will not solve the problem."),
     ],
     [G('constant', 'doimiy'), G('overhead', 'tepada, bosh ustida'), G('increasingly', 'tobora koʻproq'),
      G('genuine', 'haqiqiy, jiddiy'), G('annoyance', 'gʻashga tegadigan narsa'), G('disturb', 'buzmoq, bezovta qilmoq'),
      G('well-being', 'farovonlik, umumiy holat'), G('exposure', 'taʼsirida boʻlish'), G('trigger', 'qoʻzgʻatmoq'),
      G('accompany', 'hamroh boʻlmoq, birga kelmoq'), G('restrict', 'cheklamoq'), G('reflect', 'qaytarmoq (aks ettirmoq)'),
      G('dense', 'zich, qalin'), G('wear out', 'yeyilmoq, eskirmoq'), G('dominate', 'ustun boʻlmoq')],
     [GN('c44-adjective-patterns', 'Sifat + to-infinitive: difficult to prove', 'make such a link difficult to prove'),
      GN('i56-ing-ed-clauses', '-ing qoʻshimchali ibora: showing …', 'Maps showing the noise levels of different streets')],
     [
         tf('Many city residents are barely aware of the noise around them.', 'T',
            '«noise is so constant that they hardly notice it» — barely aware = hardly notice, deyarli sezmaydi.', 0, ng=True),
         tf('Noise is now regarded as a more serious problem than air pollution.', 'NG',
            '«alongside dirty air and water» — yonma-yon, teng qatorda; qaysi biri jiddiyroq ekani taqqoslanmagan.', 0),
         tf('Noise at night only harms sleep if it actually wakes people up.', 'F',
            '«Even when people do not wake up, loud sounds at night can disturb the quality of their sleep».', 1, ng=True),
         tf('Scientists have proved that traffic noise causes heart disease.', 'F',
            '«Some studies suggest a possible connection … make such a link difficult to prove» — isbotlanmagan.', 2, ng=True),
         tf('Quiet zones were first introduced in European cities.', 'NG',
            'Quiet zones tasvirlangan, lekin qayerda birinchi paydo boʻlgani aytilmagan.', 3),
         tf('Noise maps can be helpful when choosing locations for new hospitals.', 'T',
            '«Maps showing the noise levels … can help planners decide where new schools and hospitals should be placed».', 3, ng=True),
         tf('A single narrow line of trees is a very effective barrier against noise.', 'F',
            '«a narrow row of trees reduces noise less than many people imagine».', 4, ng=True),
         tf('Most cities have already replaced their ordinary roads with quieter surfaces.', 'NG',
            'Muhandislar jim yoʻl qoplamalarini ishlab chiqqani va ularning kamchiligi aytilgan, lekin qancha shahar '
            'ulardan foydalanishi haqida maʼlumot yoʻq.', 5),
         gap('Unwanted sound can activate the body\'s ___, even during sleep.', 'stress response',
             '«trigger the body\'s stress response, raising the heart rate even while a person is asleep».', 2, 2),
         gap('Quieter road surfaces contain more ___ that absorb some of the sound.', 'air spaces',
             '«quieter road surfaces that contain more air spaces to absorb some of the sound».', 5, 2),
         ch('Why will electric vehicles alone not solve the problem of traffic noise?',
            ['They are louder than ordinary cars at low speeds.', 'At higher speeds, most noise comes from the tyres.',
             'They wear out road surfaces faster.', 'There are too few of them in cities.'], 1,
            '«at higher speeds tyre noise dominates». Past tezlikda ular aksincha jimroq; yoʻlni tez yeyish '
            'jim yoʻl qoplamalariga tegishli; soni haqida gap yoʻq.', 5),
     ])
