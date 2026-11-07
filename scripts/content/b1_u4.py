"""B1 · 4-boʻlim: Atrof-muhit (Environment)"""
from lib import *

B = 'b1'
TAG = L('Atrof-muhit', 'Environment')

# ---------------------------------------------------------------- 16
text(B, 'b1-16-plastic', 'Plastik muammosi', 'The Plastic Problem', 'B1', 'story', TAG,
     'Bir maktab oʻquvchisi sinfi mahallada plastikka qarshi qanday aksiya oʻtkazganini hikoya qiladi. '
     'Oʻqishdan oldin oʻylab koʻring: sizning oilangiz bir haftada nechta plastik paket ishlatadi?',
     [
         P("Last spring, our biology teacher, Mrs Rakhimova, brought a large bag into the classroom and emptied it onto her desk. "
           "It was full of plastic bottles, bags and food wrappers. “I collected all this in twenty minutes,” she said, "
           "“from the small river behind our school.” Nobody spoke. Most of us had walked past that river every day, "
           "but we had never really looked at it."),
         P("Mrs Rakhimova explained that most plastic does not simply disappear. It can take hundreds of years to break down, "
           "and even then it does not really go away. Instead, it slowly breaks into smaller and smaller pieces called microplastics. "
           "These tiny pieces have been found in rivers, in the sea, in soil and even inside fish and other animals. "
           "“If we keep using plastic like this,” she told us, “the problem will only get bigger.”"),
         P("We decided to do something. Our class started a campaign called “Less Plastic, Cleaner Mahalla”. "
           "First, we cleaned the riverbank on two Saturdays. Parents and neighbours joined us, and by the end we had filled "
           "more than forty bags with rubbish. Then we made posters for the shops near the school and asked people to bring "
           "their own cloth bags when they went shopping."),
         P("Reducing plastic turned out to be harder than cleaning it up. Some shopkeepers were not interested at first. "
           "One of them said that his customers would complain if he stopped giving them free bags. However, when an old woman "
           "from our street started sewing cloth bags from old curtains and selling them cheaply, more and more people began to use them."),
         P("We also learned that reusing things is often better than recycling them. Instead of buying a new bottle of water every day, "
           "most students in our class now bring a metal or glass bottle from home and fill it at school. If everyone in our school did this, "
           "we would save thousands of bottles a year. The river is not perfect yet, but it is cleaner than it used to be, "
           "and we have stopped looking away."),
     ],
     [G('empty', 'boʻshatmoq, toʻkib tashlamoq'), G('wrapper', 'oʻram, qadoq'), G('break down', 'parchalanmoq'),
      G('tiny', 'juda kichik, mitti'), G('soil', 'tuproq'), G('campaign', 'aksiya, kampaniya'),
      G('riverbank', 'daryo qirgʻogʻi'), G('rubbish', 'axlat, chiqindi'), G('turn out', 'boʻlib chiqmoq'),
      G('shopkeeper', 'doʻkondor'), G('complain', 'shikoyat qilmoq'), G('sew', 'tikmoq'),
      G('reuse', 'qayta foydalanmoq'), G('look away', 'koʻz yummoq, eʼtibor bermaslik')],
     [GN('i30-passive-tenses', 'Present Perfect majhul nisbat: have been found',
         'These tiny pieces have been found in rivers'),
      GN('i26-second-conditional', 'Ikkinchi shart gap: If everyone did …, we would …',
         'If everyone in our school did this, we would save thousands of bottles a year.')],
     [
         tf('The teacher collected the rubbish near the school.', 'T',
            '1-xatboshi: «from the small river behind our school» — maktab orqasidagi daryodan.', 0, ng=True),
         tf('According to the teacher, plastic disappears completely after a few years.', 'F',
            '2-xatboshi: «It can take hundreds of years to break down, and even then it does not really go away».', 1, ng=True),
         tf('The class won a prize for their campaign.', 'NG',
            'Matnda mukofot haqida hech narsa aytilmagan — Not Given.', 2, ng=True),
         tf('All the shopkeepers supported the campaign from the beginning.', 'F',
            '4-xatboshi: «Some shopkeepers were not interested at first» — hammasi emas.', 3, ng=True),
         ch('What is the text mainly about?',
            ['how a class tried to reduce plastic in their area', 'how plastic is made in factories',
             'why recycling is the only solution'], 0,
            'Butun hikoya sinfning aksiyasi haqida: daryoni tozalash, plakatlar, mato sumkalar. '
            'Matn qayta ishlashni eng yaxshi yechim demaydi: «reusing things is often better than recycling them».', 2),
         ch('Why did more people start using cloth bags?',
            ['The shops stopped selling plastic bags.', 'A local woman made cheap cloth bags from old curtains.',
             'The teacher gave free bags to everyone.'], 1,
            '4-xatboshi: «an old woman … started sewing cloth bags from old curtains and selling them cheaply, more and more people began to use them».', 3),
         ch('What does the writer think about reusing things?',
            ['It is often better than recycling.', 'It is too difficult for students.', 'It is less useful than cleaning rivers.'], 0,
            '5-xatboshi: «reusing things is often better than recycling them».', 4),
         gap('Very small pieces of broken plastic are called ___.', ['microplastics'],
             '2-xatboshi: «smaller and smaller pieces called microplastics».', 1, 2),
         gap('The students asked shoppers to bring their own ___.', ['cloth bags', 'bags'],
             '3-xatboshi: «asked people to bring their own cloth bags».', 2, 2),
     ])

# ---------------------------------------------------------------- 17
text(B, 'b1-17-city-parks', 'Shahar bogʻlari', 'Why Cities Need Parks', 'B1', 'article', TAG,
     'Issiq shaharlarda daraxt va bogʻlar nima uchun muhimligi haqida maqola. '
     'Oʻqishdan oldin oʻylab koʻring: yozda soyali bogʻda havo nega salqinroq tuyuladi?',
     [
         P("On a summer afternoon in Tashkent, Bukhara or Termez, the temperature can rise above forty degrees. "
           "Walking along a wide road with no trees can feel like standing next to an oven. Yet only a few steps away, "
           "in a shady park, the air feels noticeably cooler. This is not your imagination. Scientists have studied this effect "
           "for many years, and it is one of the main reasons why cities in hot countries need more green spaces."),
         P("Cities often become hotter than the countryside around them. Asphalt, concrete and brick absorb heat during the day "
           "and release it slowly at night, so streets stay warm even after sunset. This is known as the urban heat island effect. "
           "Trees help in two ways. Their leaves block sunlight, which keeps the ground below them cool. They also release water "
           "into the air through their leaves, and this cools the air around them, a little like sweat cools the human body."),
         P("Green spaces are also good for our health. Trees can trap some of the dust in the air, which is especially useful "
           "in dry, dusty regions. Researchers have found that people who live near parks tend to walk more and often feel less stressed. "
           "For children, a park may be the only safe place to run, climb and play outside. For older people, it is a place "
           "to meet friends on a bench in the shade."),
         P("In recent years, tree-planting has become a popular activity in many Uzbek cities. Volunteers, students and local "
           "organisations often gather in spring and autumn to plant young trees along streets and in schoolyards. However, experts "
           "warn that planting a tree is only the beginning. A young tree needs to be watered regularly for several years, and it should "
           "be suited to the local climate. Trees that need a lot of water may not survive a long, dry summer."),
         P("Planners also point out that a big park is not the only answer. A row of trees in a courtyard, plants on a roof or "
           "a small garden between apartment blocks can all make a difference to the people who live nearby. If every neighbourhood "
           "looked after its own trees, our cities would become cooler, cleaner and more pleasant places to live."),
     ],
     [G('shady', 'soyali'), G('noticeably', 'sezilarli darajada'), G('absorb', 'yutmoq, singdirmoq'),
      G('release', 'chiqarmoq, ajratmoq'), G('concrete', 'beton'), G('urban heat island', 'shahar «issiqlik oroli»'),
      G('block', 'toʻsmoq'), G('sweat', 'ter'), G('trap', 'ushlab qolmoq'), G('stressed', 'asabiy, zoʻriqqan'),
      G('volunteer', 'koʻngilli'), G('be suited to', '… ga mos boʻlmoq'), G('courtyard', 'hovli'),
      G('pleasant', 'yoqimli')],
     [GN('i29-passive-basics', 'Majhul nisbat: is known as', 'This is known as the urban heat island effect.'),
      GN('i53-who-which-that', 'Nisbiy olmosh: people who live …', 'people who live near parks tend to walk more')],
     [
         tf('Streets in cities can stay warm after the sun goes down.', 'T',
            '2-xatboshi: «streets stay warm even after sunset».', 1, ng=True),
         tf('Trees cool the air only by giving shade.', 'F',
            '2-xatboshi: «Trees help in two ways» — soya berish va barglar orqali havoga suv chiqarish.', 1, ng=True),
         tf('Tashkent has more parks than Bukhara.', 'NG',
            'Matnda shaharlardagi bogʻlar soni solishtirilmagan — Not Given.', 0, ng=True),
         tf('Experts believe that planting a tree is enough to help a city.', 'F',
            '4-xatboshi: «experts warn that planting a tree is only the beginning» — daraxtni yillar davomida sugʻorish kerak.', 3, ng=True),
         hd(1, ['How trees cool a hot city', 'Where to find the best parks', 'The history of Uzbek gardens'], 0,
            '2-xatboshi shahar nega isishi va daraxtlar havoni qanday salqinlatishi haqida: «Trees help in two ways».'),
         ch('In paragraph 3, the word "trap" is closest in meaning to …',
            ['catch and hold', 'produce', 'throw away'], 0,
            '«Trees can trap some of the dust in the air» — daraxtlar changni ushlab qoladi, yaʼni havoni tozalaydi.', 2),
         ch('Why might some young trees die in a long, dry summer?',
            ['They need a lot of water.', 'They are planted in autumn.', 'They grow too close to roads.'], 0,
            '4-xatboshi: «Trees that need a lot of water may not survive a long, dry summer».', 3),
         gap('When a city is hotter than the countryside around it, this is called the urban heat ___ effect.', ['island'],
             '2-xatboshi: «This is known as the urban heat island effect».', 1, 2),
         gap('People who live near parks tend to walk more and feel less ___.', ['stressed'],
             '3-xatboshi: «tend to walk more and often feel less stressed».', 2, 2),
     ])

# ---------------------------------------------------------------- 18
text(B, 'b1-18-saving-water', 'Suvni tejash', 'Every Drop Counts', 'B1', 'dialogue', TAG,
     'Dilnoza qishloqda fermer togʻasi Akmal bilan suvni qanday tejash haqida suhbatlashadi. '
     'Oʻqishdan oldin oʻylab koʻring: uyingizda suv qayerda behuda sarflanadi?',
     [
         P("Dilnoza: Uncle Akmal, why are there black pipes lying along every row of your tomatoes? I don't remember them from last summer. "
           "Akmal: That's my new drip irrigation system. In the past, we used to flood the whole field with water from the canal. "
           "Now these thin pipes carry water straight to the roots of each plant, drop by drop."),
         P("Dilnoza: Does it really make such a big difference? "
           "Akmal: It does. When you flood a field in July, a lot of the water evaporates in the sun or runs off to places where nothing grows. "
           "With drip irrigation, much less is wasted. I have used less water this year, and my tomatoes have grown better than ever, "
           "because the soil doesn't get too wet or too dry."),
         P("Dilnoza: So why doesn't everyone in the village use it? "
           "Akmal: Setting it up costs money, and you have to keep the pipes clean, or they get blocked. Some farmers here are still "
           "waiting to see if it works. My neighbour said he would try it next year if my harvest was good."),
         P("Dilnoza: We don't have a field in Tashkent, but my teacher says families waste a lot of water too. "
           "Akmal: Your teacher is right. A dripping tap or a leaking toilet can waste a surprising amount of water, and it is usually "
           "easy to fix. Your aunt noticed that our kitchen tap had been dripping for weeks, so we finally changed the washer. "
           "It took ten minutes."),
         P("Dilnoza: What else can we do at home? "
           "Akmal: Turn off the tap while you brush your teeth. Wash fruit in a bowl instead of under running water, and give that water "
           "to the plants afterwards. Water the garden early in the morning or in the evening, when it is cooler. In a dry region like ours, "
           "every bucket matters."),
         P("Dilnoza: I'm going to write a list and put it on our fridge as soon as I get home. "
           "Akmal: Good idea. And check under the kitchen sink while you're at it. Small leaks are very easy to miss."),
     ],
     [G('pipe', 'quvur'), G('drip irrigation', 'tomchilatib sugʻorish'), G('flood', 'suv bostirmoq'),
      G('canal', 'kanal, ariq'), G('evaporate', 'bugʻlanmoq'), G('run off', 'oqib ketmoq'),
      G('waste', 'isrof qilmoq, behuda sarflamoq'), G('set up', 'oʻrnatmoq'), G('blocked', 'tiqilib qolgan'),
      G('harvest', 'hosil'), G('tap', 'jumrak'), G('leak', 'oqish, sizib chiqish'), G('washer', 'qistirma, prokladka'),
      G('bucket', 'chelak')],
     [GN('i12-used-to-would', 'Used to: oʻtmishdagi odat', 'we used to flood the whole field with water from the canal'),
      GN('i33-reported-speech', 'Koʻchirma gap: said he would …',
         'My neighbour said he would try it next year if my harvest was good.')],
     [
         tf('Akmal has always used drip irrigation on his farm.', 'F',
            '1-xatboshi: «In the past, we used to flood the whole field» — ilgari dalani suvga bostirgan, tizim yangi.', 0, ng=True),
         tf('Drip irrigation has helped Akmal use less water.', 'T',
            '2-xatboshi: «I have used less water this year».', 1, ng=True),
         tf('Akmal sells his tomatoes at a market in Tashkent.', 'NG',
            'Pomidorlar qayerda sotilishi haqida matnda hech narsa yoʻq — Not Given.', 1, ng=True),
         tf('Fixing the kitchen tap took a long time.', 'F',
            '4-xatboshi: «It took ten minutes» — juda tez.', 3, ng=True),
         ch('According to Akmal, why is flooding a field less effective?',
            ['Much of the water evaporates or runs off.', 'The water from the canal is too dirty.', 'The tomatoes grow too quickly.'], 0,
            '2-xatboshi: «a lot of the water evaporates in the sun or runs off to places where nothing grows».', 1),
         ch('Why are some farmers not using drip irrigation yet?',
            ['It costs money and they want to see if it works.', 'It is not allowed in their village.', 'Their fields are too small.'], 0,
            '3-xatboshi: «Setting it up costs money» va «Some farmers here are still waiting to see if it works».', 2),
         ch('What does Akmal mean by "every bucket matters"?',
            ['Even small amounts of water are important.', 'People should buy more buckets.', 'Water should always be carried by hand.'], 0,
            '5-xatboshi: quruq hududda har bir chelak suv ham muhim, yaʼni ozgina suvni ham tejash kerak.', 4),
         gap('In drip irrigation, thin pipes carry water straight to the ___ of each plant.', ['roots'],
             '1-xatboshi: «carry water straight to the roots of each plant».', 0, 2),
         gap('Akmal advises watering the garden early in the morning or in the ___.', ['evening', 'the evening'],
             '5-xatboshi: «Water the garden early in the morning or in the evening, when it is cooler».', 4, 2),
     ])

# ---------------------------------------------------------------- 19
text(B, 'b1-19-snow-leopard', 'Qor qoplonlari', 'Ghosts of the Mountains', 'B1', 'article', TAG,
     'Baland togʻlarda yashaydigan noyob mushuk — qor qoploni (irbis) haqida maqola. '
     'Oʻqishdan oldin oʻylab koʻring: nima uchun bu hayvonni koʻrish juda qiyin deb oʻylaysiz?',
     [
         P("High in the mountains of Central Asia, where winters are long and the air is thin, lives one of the most mysterious "
           "animals in the world: the snow leopard. Its thick grey fur with dark spots helps it hide among the rocks and snow so well "
           "that people who have lived in the mountains all their lives may never see one. That is why it is sometimes called "
           "the ghost of the mountains."),
         P("The snow leopard is well adapted to its cold, steep home. Its wide paws work like snowshoes, so it does not sink into "
           "deep snow. Its tail is very long and thick. It helps the cat keep its balance on narrow rocks, and when the animal rests, "
           "it can wrap the tail around its body and face to stay warm. Unlike lions and tigers, snow leopards cannot roar."),
         P("Snow leopards live in the high mountains of several Asian countries, from the Himalayas to Mongolia. In Uzbekistan, "
           "they have been recorded in mountain areas such as the Gissar and Chatkal ranges, where some of the land is protected "
           "as nature reserves. They mainly hunt wild goats and sheep, for example the Siberian ibex, and they usually live and hunt alone."),
         P("Because the animals are so rare and shy, scientists rarely study them face to face. Instead, they use camera traps. "
           "These are small cameras that are fixed to rocks or trees and take a photo automatically when an animal walks past. "
           "Every snow leopard has its own pattern of spots, so researchers can tell individual cats apart. Photos like these have "
           "helped scientists learn where the cats travel and how many may live in an area."),
         P("Snow leopards face serious threats. Some are killed illegally by poachers who want their beautiful fur or their bones. "
           "When people hunt too many wild goats and sheep, the leopards lose their natural food, and hungry cats may attack farm animals. "
           "Herders may then kill them to protect their flocks. Climate change could also affect their mountain habitat in the future."),
         P("Protecting the snow leopard means protecting the whole mountain world. Rangers patrol nature reserves to stop poaching, "
           "and conservation groups work with local communities, for example by helping herders build safer shelters for their animals "
           "at night. If these efforts continue, people may still be able to see this rare cat, even if only in a camera trap photo, "
           "many years from now."),
     ],
     [G('mysterious', 'sirli'), G('hide', 'yashirinmoq'), G('be adapted to', '… ga moslashgan boʻlmoq'),
      G('steep', 'tik, qiya'), G('paw', 'panja'), G('sink', 'botib ketmoq'), G('wrap', 'oʻramoq'),
      G('range', 'togʻ tizmasi'), G('camera trap', 'fotoqopqon, avtomatik kamera'), G('tell apart', 'farqlamoq, ajrata olmoq'),
      G('poacher', 'brakoner, noqonuniy ovchi'), G('herder', 'choʻpon, podachi'), G('flock', 'suruv, poda'),
      G('habitat', 'yashash muhiti')],
     [GN('i54-whose-whom-where', 'Nisbiy soʻz: where', 'High in the mountains of Central Asia, where winters are long and the air is thin'),
      GN('i30-passive-tenses', 'Present Perfect majhul nisbat: have been recorded',
         'they have been recorded in mountain areas such as the Gissar and Chatkal ranges')],
     [
         tf('Even people who live in the mountains may never see a snow leopard.', 'T',
            '1-xatboshi: «people who have lived in the mountains all their lives may never see one».', 0, ng=True),
         tf('Snow leopards can roar like lions and tigers.', 'F',
            '2-xatboshi: «Unlike lions and tigers, snow leopards cannot roar».', 1, ng=True),
         tf('Snow leopards in Uzbekistan are bigger than those in Mongolia.', 'NG',
            'Matnda turli mamlakatlardagi qoplonlarning kattaligi solishtirilmagan — Not Given.', 2, ng=True),
         tf('Snow leopards usually hunt in groups.', 'F',
            '3-xatboshi: «they usually live and hunt alone» — yolgʻiz ov qiladi.', 2, ng=True),
         gap('The snow leopard is sometimes called the ___ of the mountains.', ['ghost'],
             '1-xatboshi: «it is sometimes called the ghost of the mountains».', 0, 2),
         gap('Its wide paws work like ___, so it does not sink into deep snow.', ['snowshoes'],
             '2-xatboshi: «Its wide paws work like snowshoes».', 1, 2),
         ch('How can researchers tell individual snow leopards apart?',
            ['Each cat has its own pattern of spots.', 'Each cat has a different tail length.', 'Each cat wears a number.'], 0,
            '4-xatboshi: «Every snow leopard has its own pattern of spots, so researchers can tell individual cats apart».', 3),
         ch('According to the text, why may herders kill snow leopards?',
            ['to sell their fur', 'to protect their flocks', 'because the cats attack people'], 1,
            '5-xatboshi: «Herders may then kill them to protect their flocks». Moʻyna uchun esa brakonerlar oʻldiradi.', 4),
         hd(4, ['Dangers for the snow leopard', 'How snow leopards hunt', 'A new nature reserve'], 0,
            '5-xatboshi tahdidlar haqida: «Snow leopards face serious threats» — brakonerlik, oziqning kamayishi, iqlim oʻzgarishi.'),
     ])

# ---------------------------------------------------------------- 20
text(B, 'b1-20-climate-farming', 'Iqlim va qishloq xoʻjaligi', 'A Letter from the Farm', 'B1', 'email', TAG,
     'Fermer ota universitetda oʻqiyotgan oʻgʻliga issiq yoz va suv tanqisligi haqida xat yozadi. '
     'Oʻqishdan oldin oʻylab koʻring: havo isib borsa, dehqonlar nimalarni oʻzgartirishi kerak?',
     [
         P("Dear Farrukh, thank you for your message and the photos from your university. Your mother says you have been studying hard, "
           "and we are both very proud of you. You asked me how the farm is doing this year, so I will tell you honestly: "
           "it has been the most difficult summer I can remember."),
         P("When I was your age, the hottest days of July felt like an exception. Now we seem to have weeks of extreme heat almost "
           "every summer, and the heat starts earlier in the year. The canal that waters our fields also carried less water this year "
           "than it used to. By August, the water was arriving only every few days, and the melons on the lower field had dried up "
           "before they were ready."),
         P("But I don't want you to think we are giving up. Your uncle and I have decided to change the way we farm. We have planted "
           "part of the land with sorghum, which needs less water than many other crops and can survive long dry periods. After the "
           "wheat harvest, we sowed mung beans, which grow quickly and are good for the soil. We have also started covering the soil "
           "between the plants with straw. It keeps the ground cooler and stops the water from evaporating so fast."),
         P("We are also working at different times. In June and July, we start in the fields before sunrise and rest in the hottest "
           "hours of the afternoon. Karim aka from the next village laughed at us at first, but last week he came and asked us how "
           "the straw method works. Next spring, I would like to plant a few rows of pistachio trees. They can handle heat and dry soil well, "
           "although they take several years to produce a harvest."),
         P("This is where you come in, my son. You are learning things at university that I never had the chance to learn. When you "
           "come home for the winter holidays, I want you to look at our fields and tell me what else we could do. If my grandfather "
           "saw how we farm today, he would not believe his eyes, but I think he would understand that we must change with the weather. "
           "Take care of yourself. Your father"),
     ],
     [G('exception', 'istisno'), G('extreme', 'haddan tashqari, keskin'), G('canal', 'kanal, ariq'),
      G('dry up', 'qurib qolmoq'), G('give up / giving up', 'taslim boʻlmoq, voz kechmoq'), G('crop', 'ekin'),
      G('sorghum', 'joʻxori'), G('survive', 'omon qolmoq, chidamoq'), G('sow', 'ekmoq, urugʻ sepmoq'),
      G('mung beans', 'mosh'), G('straw', 'somon'), G('evaporate', 'bugʻlanmoq'),
      G('handle', 'chidamoq, uddalamoq'), G('harvest', 'hosil')],
     [GN('i11-past-perfect', 'Past Perfect: had dried up',
         'the melons on the lower field had dried up before they were ready'),
      GN('i55-non-defining', 'Aniqlamaydigan nisbiy ergash gap: , which …',
         'sorghum, which needs less water than many other crops')],
     [
         tf('Farrukh is studying at a university.', 'T',
            '1-xatboshi: «the photos from your university» va 5-xatboshi: «You are learning things at university».', 0, ng=True),
         tf('The canal carried more water this year than in the past.', 'F',
            '2-xatboshi: «carried less water this year than it used to».', 1, ng=True),
         tf("Farrukh's mother also works on the farm.", 'NG',
            'Onasi faqat «Your mother says you have been studying hard» jumlasida tilga olinadi; u fermada ishlaydimi — maʼlumot yoʻq — Not Given.', 0, ng=True),
         tf('Karim aka liked the family\'s new methods from the very beginning.', 'F',
            '4-xatboshi: «Karim aka … laughed at us at first» — avvaliga kulgan, keyin qiziqib qolgan.', 3, ng=True),
         ch('Why did the family plant sorghum?',
            ['It needs less water and can survive dry periods.', 'It sells for a very high price.', 'Farrukh recommended it.'], 0,
            '3-xatboshi: «sorghum, which needs less water than many other crops and can survive long dry periods».', 2),
         ch('In paragraph 4, the word "handle" is closest in meaning to …',
            ['deal with', 'avoid', 'produce'], 0,
            '«They can handle heat and dry soil well» — issiq va quruq tuproqqa yaxshi chidaydi, yaʼni uddalaydi.', 3),
         ch('What is the main purpose of the email?',
            ["to explain how the farm is changing and ask for Farrukh's ideas", 'to ask Farrukh to leave university and come home',
             'to complain about the neighbours'], 0,
            'Ota fermadagi oʻzgarishlarni tushuntiradi va oxirida: «tell me what else we could do» — oʻgʻlining fikrini soʻraydi.', 4),
         gap('The family covers the soil between the plants with ___.', ['straw'],
             '3-xatboshi: «covering the soil between the plants with straw».', 2, 2),
         gap('In June and July, the family starts work in the fields before ___.', ['sunrise'],
             '4-xatboshi: «we start in the fields before sunrise».', 3, 2),
     ])
