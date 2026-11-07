"""C1 · 6-boʻlim: Toʻliq mashq testlari (IELTS Academic tarzidagi toʻliq oʻqish testlari)"""
from lib import *

B = 'c1'


def intro(topic):
    return (f'Toʻliq mashq testi (C1): {topic} Haqiqiy IELTS Academic imtihonidagidek bitta matnga 14 ta savol beriladi: '
            'Matching headings, True/False/Not Given, summary completion (NO MORE THAN TWO WORDS) va 4 variantli test savollari. '
            'Taxminan 20 daqiqa ajrating. Tavsiya etiladigan tartib: avval 2–3 daqiqada matnga koʻz yugurtirib, har bir xatboshining '
            'asosiy gʻoyasini belgilang va sarlavhalarni moslang; soʻng TFNG savollarini matn tartibida bajaring; keyin xulosadagi '
            'boʻshliqlarni matndagi soʻzlar bilan aynan toʻldiring; test savollarini esa oxiriga qoldiring.')


# ---------------------------------------------------------------- 1-test
H1 = ['A carefully protected natural laboratory', 'Shared traits of the first colonists',
      'Changing the environment for successors', 'The unexpected contribution of wildlife',
      'A quicker recovery where soil survives', 'Questioning a neat, predictable sequence',
      'Why volcanic islands attract visitors', 'How seeds survive long sea journeys',
      'Measuring how quickly lava cools']

text(B, 'c1-26-test1', '1-test: Kashshof oʻsimliklar', 'Life on Bare Ground: Pioneer Plants and Succession', 'C1', 'exam',
     L('Ekologiya', 'Ecology'), intro('vulqon orollari va tashlab qoʻyilgan yerlarda hayot qanday qayta boshlanishi haqidagi ilmiy matn.'),
     [
         P("When a volcano pours fresh lava across a hillside, or a retreating glacier exposes rock that has been buried for "
           "thousands of years, the result is a landscape almost entirely without life. There is no soil to speak of, no store "
           "of seeds and very little to hold water or nutrients. Yet within a few years such places are rarely completely bare. "
           "A sequence of colonisation begins, and over decades or centuries it may transform the site into grassland, scrub or "
           "forest. Ecologists call this process succession, and they usually distinguish between two forms of it. Primary "
           "succession starts on surfaces that have never supported a community of living things, while secondary succession "
           "follows a disturbance, such as a fire or the abandonment of a field, that removes vegetation but leaves the soil "
           "largely intact."),
         P("Few natural experiments in primary succession have been followed as closely as that offered by Surtsey, an island "
           "that rose from the sea off the southern coast of Iceland during a series of eruptions in the 1960s. From the "
           "beginning, the authorities restricted access to a small number of researchers, so that the arrival of life could be "
           "recorded with minimal human interference. What emerged from decades of observation was a picture of colonisation "
           "that was neither instant nor random. The earliest arrivals were carried by the sea, the wind and birds, and many of "
           "those that landed failed to establish themselves at all. For a long time, survival rather than arrival was the "
           "main obstacle."),
         P("The species that do succeed in such conditions tend to share a recognisable set of characteristics. Pioneer plants "
           "typically produce large numbers of small, light seeds or spores that can travel long distances, and they are able to "
           "tolerate intense sunlight, sharp changes in temperature and a severe shortage of nutrients. Many complete their life "
           "cycle quickly. On bare rock, the first colonists are often not flowering plants at all but lichens, partnerships "
           "between a fungus and an alga or a cyanobacterium, which can cling to surfaces where nothing else can gain a "
           "foothold. Mosses frequently follow, trapping dust and moisture among their tightly packed stems."),
         P("What makes pioneers ecologically significant is not simply that they survive but that they alter their "
           "surroundings. Lichens release acids that slowly break down the rock surface, and as pioneer plants die, their "
           "remains add organic matter to the mineral particles, gradually producing a thin layer of soil capable of holding "
           "water. Some early colonists form partnerships with bacteria that convert nitrogen from the air into a form that "
           "plants can use, which is particularly valuable in nutrient-poor ground. In this way pioneers may prepare the ground "
           "for larger and more demanding species, a process ecologists refer to as facilitation. There is an irony here: by "
           "improving conditions, pioneers often make the site more attractive to competitors that will eventually shade them out."),
         P("Animals can play a surprisingly large part in this story. On Surtsey, researchers observed that plant colonisation "
           "accelerated markedly after seabirds began nesting on the island. The birds not only brought seeds with them but also "
           "enriched the poor volcanic ground with their droppings, and the areas around their colonies developed far denser "
           "vegetation than the rest of the island. Elsewhere, insects, small mammals and birds may disperse seeds and carry "
           "nutrients between habitats, linking a newly forming community to the wider landscape."),
         P("Secondary succession usually proceeds much faster, because the most difficult stage has already been completed. "
           "When a cultivated field is abandoned, the soil retains its structure and nutrients, and it often contains a bank of "
           "dormant seeds. Fast-growing annual weeds commonly appear within the first season, to be followed over subsequent "
           "years by perennial grasses and herbs, then by shrubs and, where the climate allows, by trees. Even so, the return of "
           "a mature woodland may take many decades, and the forest that eventually develops does not necessarily resemble the "
           "one that was cleared."),
         P("For much of the twentieth century, succession was often described as an orderly progression in which each stage "
           "gave way to the next until a stable final community, sometimes called a climax, was reached. Many ecologists now "
           "regard this picture as too tidy. The order in which species happen to arrive can strongly influence what follows, "
           "and some early colonists, rather than preparing the way for others, appear to inhibit them, for instance by forming "
           "dense thickets that later species struggle to penetrate. Repeated disturbances such as storms, fires or grazing may "
           "also reset the process before any final state is reached. Succession, in other words, is better understood as a set "
           "of probabilities than as a fixed script."),
         P("These insights have practical applications. Those attempting to restore land damaged by mining or erosion sometimes "
           "deliberately introduce pioneer species, particularly nitrogen-fixing plants, to speed up soil formation. Such "
           "interventions, however, carry risks. A species chosen for its vigour may spread far beyond the area it was intended "
           "to protect, and in Iceland a lupin introduced to combat erosion has become the subject of considerable debate "
           "because it can overrun native vegetation. Working with succession, it seems, requires an understanding not only of "
           "how pioneers help but also of when they might take over."),
     ],
     [G('retreating glacier', 'chekinayotgan muzlik'), G('colonisation', 'yangi hududni egallash, joylashish'),
      G('succession', 'suksessiya, oʻsimliklar jamoasining izchil almashinuvi'),
      G('disturbance', 'buzilish, tabiiy muvozanatning izdan chiqishi'), G('interference', 'aralashuv'),
      G('establish oneself', 'oʻrnashib olmoq, qaror topmoq'), G('tolerate', 'chidamoq, bardosh bermoq'),
      G('gain a foothold', 'oyoq qoʻyadigan joy topmoq, oʻrnashmoq'), G('organic matter', 'organik modda'),
      G('facilitation', 'yengillashtirish, yoʻl ochib berish'), G('shade out', 'soya solib siqib chiqarmoq'),
      G('accelerate markedly', 'sezilarli darajada tezlashmoq'), G('disperse', 'tarqatmoq, sochmoq'),
      G('dormant', 'uyquda, faol boʻlmagan (urugʻ)'), G('inhibit', 'toʻsqinlik qilmoq, sekinlashtirmoq'),
      G('vigour', 'kuch-quvvat, jadal oʻsish'), G('overrun', 'bosib ketmoq, egallab olmoq')],
     [GN('c57-cleft-sentences', 'Taʼkidli (wh-) gap: What makes … is …',
         'What makes pioneers ecologically significant is not simply that they survive but that they alter their surroundings'),
      GN('c34-participle-clauses', 'Sifatdoshli ergash gap: …, trapping dust and moisture',
         'Mosses frequently follow, trapping dust and moisture among their tightly packed stems')],
     [
         hd(1, H1, 0, 'Xatboshi B: Surtsey oroliga kirish cheklangan — «restricted access to a small number of researchers», '
                      'hayotning paydo boʻlishi «with minimal human interference» kuzatilgan, yaʼni bu tabiiy laboratoriya. '
                      '«How seeds survive long sea journeys» chalgʻitadi: dengiz faqat tashuvchi sifatida tilga olinadi.'),
         hd(2, H1, 1, 'Xatboshi C: kashshof turlarning umumiy belgilari — «share a recognisable set of characteristics»: '
                      'mayda urugʻlar, quyosh va ozuqa tanqisligiga chidamlilik.'),
         hd(3, H1, 2, 'Xatboshi D: kashshoflar atrof-muhitni oʻzgartiradi — «they alter their surroundings», tuproq hosil qiladi '
                      'va keyingi turlarga yoʻl ochadi (facilitation).'),
         hd(5, H1, 4, 'Xatboshi F: ikkilamchi suksessiya tezroq, chunki tuproq saqlanib qolgan — «the soil retains its structure and nutrients».'),
         hd(6, H1, 5, 'Xatboshi G: «orderly progression … climax» tasavvuri «too tidy» deb tanqid qilinadi — tartibli va oldindan '
                      'aytib boʻladigan ketma-ketlik shubha ostiga olinadi.'),
         tf('Primary succession takes place on ground where the soil has survived a disturbance.', 'F',
            'Aksincha: primary succession «starts on surfaces that have never supported a community of living things»; '
            'tuprogʻi saqlangan yer — bu secondary succession.', 0, ng=True),
         tf('Access to Surtsey was limited so that human influence on colonisation would be kept to a minimum.', 'T',
            '«the authorities restricted access … so that the arrival of life could be recorded with minimal human interference» — '
            'limited = restricted, kept to a minimum = minimal.', 1, ng=True),
         tf('Some plant species growing near the seabird colonies on Surtsey are found nowhere else in Iceland.', 'NG',
            'Qushlar koloniyasi atrofida oʻsimliklar zichroq ekani aytilgan («far denser vegetation»), lekin noyob turlar haqida maʼlumot yoʻq.', 4),
         tf('Many ecologists today believe that succession always ends in a stable final community.', 'F',
            '«Many ecologists now regard this picture as too tidy» va jarayon «before any final state is reached» qayta boshlanishi mumkin — '
            'demak, «always» notoʻgʻri.', 6, ng=True),
         gap('Summary: On bare rock, lichens release ___ that slowly break the surface down.', 'acids',
             '«Lichens release acids that slowly break down the rock surface».', 3, 2),
         gap('Summary: The way in which pioneers prepare the ground for larger species is known as ___.', 'facilitation',
             '«a process ecologists refer to as facilitation» — refer to as = is known as.', 3, 2),
         gap('Summary: Abandoned fields recover relatively quickly, partly because the soil often holds a bank of ___.',
             ['dormant seeds', 'seeds'],
             '«it often contains a bank of dormant seeds». Javob 2 soʻzdan oshmasligi kerak.', 5, 2),
         ch('According to paragraph B, what was the main difficulty for living things on Surtsey in the early years?',
            ['reaching the island in the first place', 'surviving once they had arrived',
             'competing with seabirds for space', 'avoiding disturbance by human visitors'], 1,
            '«many of those that landed failed to establish themselves» va «survival rather than arrival was the main obstacle». '
            'Odamlar kirishi cheklangan, shuning uchun D variant notoʻgʻri.', 1),
         ch('Why does the writer mention the lupin introduced in Iceland?',
            ['to show that pioneer species can never be used safely', 'to illustrate a risk of introducing vigorous species',
             'to prove that native plants cannot prevent erosion', 'to give an example of a fully successful restoration project'], 1,
            '«A species chosen for its vigour may spread far beyond the area…» — lupin shu xavfning misoli. «never» haddan tashqari kuchli: '
            'muallif faqat «carry risks» deydi.', 7),
     ])


# ---------------------------------------------------------------- 2-test
H2 = ['From a bold claim to a more modest question', 'Evidence that an effect may be temporary',
      'Describing location without left and right', 'Findings that have proved hard to repeat',
      'Why cause and effect are hard to separate', 'A compromise view of language and mind',
      'A spectrum divided in many ways', 'Why some languages borrow more words than others',
      'The decline of minority languages']

text(B, 'c1-27-test2', '2-test: Til va fikrlash', 'Does Language Shape the Way We Think?', 'C1', 'exam',
     L('Tilshunoslik', 'Linguistics'), intro('til fikrlashga taʼsir qiladimi degan savol — rang va makon haqidagi tadqiqotlar.'),
     [
         P("It is a claim that appears regularly in popular articles and conversations: speakers of different languages, we "
           "are told, see the world in fundamentally different ways. One language is said to lack a word for a particular "
           "emotion, so its speakers supposedly cannot feel it; another is said to have dozens of words for snow, implying that "
           "its speakers perceive winter landscapes in ways outsiders never could. Such stories are appealing, but many of them "
           "are exaggerated or simply inaccurate. The serious question behind them is nevertheless a genuine one, and it has "
           "occupied linguists, psychologists and philosophers for more than a century: does the language we speak influence "
           "the way we think, and if so, how far?"),
         P("The idea is often referred to as linguistic relativity, and in its strongest form it holds that language "
           "determines thought, so that concepts absent from a language are effectively unavailable to its speakers. This "
           "version, associated in particular with American linguists of the first half of the twentieth century, attracted considerable "
           "attention but proved difficult to support. Speakers routinely understand ideas for which their language has no "
           "single word, and translation, although imperfect, is clearly possible. By the middle of the century, many "
           "researchers had turned towards the view that human thought rests on shared foundations, and the strong hypothesis "
           "fell largely out of favour. Interest later returned in a more modest form: the question became not whether "
           "language imprisons thought but whether it nudges it in particular directions."),
         P("Colour has long been a favourite testing ground, because the physical spectrum is continuous while languages divide "
           "it in strikingly different ways. Some languages have only a handful of basic colour terms, whereas others have a "
           "dozen or more. Influential cross-cultural surveys in the second half of the twentieth century suggested that this "
           "variation is not unlimited, since the ways in which languages divide the spectrum appear to follow broad "
           "regularities. Later work has questioned how strict these patterns are, but the debate shows why colour vocabulary "
           "offers a convenient point at which language and perception can be compared."),
         P("One frequently discussed line of research concerns Russian, which treats lighter and darker blue as two distinct "
           "basic colours rather than shades of a single one. In laboratory tasks, Russian speakers have been found to "
           "distinguish two blues slightly faster when the shades fall on different sides of this linguistic boundary, an "
           "advantage not shown by English speakers. Interestingly, the effect has been reported to weaken when participants "
           "are simultaneously asked to perform a verbal task, which occupies the language system. Results of this kind suggest "
           "that language may influence perception in the moment, rather than permanently reshaping what people are able to "
           "see. The differences, it should be stressed, are measured in fractions of a second."),
         P("Spatial language provides perhaps the most striking evidence. Speakers of English and Uzbek habitually describe "
           "locations relative to their own bodies, saying that a cup is to the left of a plate. Some communities, however, "
           "including speakers of certain Aboriginal languages in Australia, rely largely on fixed compass directions, so that "
           "the cup might be described as north of the plate regardless of where the speaker is facing. Researchers have "
           "reported that such speakers tend to keep track of their orientation with remarkable accuracy, and that in "
           "non-verbal tasks they are inclined to reproduce arrangements according to compass directions rather than left and "
           "right. Critics point out, though, that the habit of attending to direction may arise from the landscape and culture "
           "as much as from language itself."),
         P("Grammar has been investigated too. In languages with grammatical gender, nouns meaning bridge or key are classed as "
           "masculine or feminine, and some studies suggested that speakers describe objects in ways that echo their "
           "grammatical gender. Subsequent attempts to repeat these findings, however, have produced mixed results. Uzbek offers "
           "an interesting contrast, since, like other Turkic languages, it has no grammatical gender and uses the single "
           "pronoun u for both he and she. Whether this affects how its speakers think about gender remains an open question, "
           "and it would be unwise to draw conclusions without careful evidence."),
         P("Part of the difficulty is methodological. Language is inseparable from the culture in which it is used, so it is "
           "rarely possible to show that a difference in thinking stems from language rather than from education, environment "
           "or everyday practices. Nor is the direction of influence always clear: a community may develop a rich vocabulary "
           "for something precisely because it already pays close attention to it. Studies with bilingual speakers, who "
           "sometimes respond differently depending on the language in which a task is presented, offer one way around this "
           "problem, although they introduce complications of their own."),
         P("Where, then, does the evidence leave us? Most researchers now reject the notion that language is a prison which "
           "confines thought. At the same time, few would claim that it has no influence whatsoever. A widely held middle "
           "position is that each language makes certain distinctions obligatory or habitual, and that its speakers "
           "consequently become practised at noticing them. Language, on this view, functions less like a pair of tinted "
           "glasses that colours everything we see than like a set of well-worn paths, which we follow most easily but are "
           "not forced to take."),
     ],
     [G('exaggerated', 'boʻrttirilgan, oshirib yuborilgan'), G('linguistic relativity', 'lingvistik nisbiylik'),
      G('determine', 'belgilamoq, hal qilmoq'), G('fall out of favour', 'eʼtibordan qolmoq, obroʻsini yoʻqotmoq'),
      G('nudge', 'sekin turtmoq, ozgina yoʻnaltirmoq'), G('strikingly', 'yaqqol, hayratlanarli darajada'),
      G('regularity', 'qonuniyat, muntazamlik'), G('distinguish', 'farqlamoq'), G('simultaneously', 'bir vaqtning oʻzida'),
      G('habitually', 'odatiy ravishda'), G('orientation', 'yoʻnalishni bilish, moʻljal'),
      G('subsequent', 'keyingi, undan soʻnggi'), G('inseparable from', '… dan ajralmas'), G('stem from', '… dan kelib chiqmoq'),
      G('obligatory', 'majburiy'), G('confine', 'cheklamoq, qamab qoʻymoq'), G('whatsoever', 'hech qanday, mutlaqo')],
     [GN('c14-complex-passive', 'Murakkab majhul nisbat: is said to lack / have been found to distinguish',
         'One language is said to lack a word for a particular emotion'),
      GN('c58-inversion', 'Inversiya: Nor is the direction … clear',
         'Nor is the direction of influence always clear')],
     [
         hd(1, H2, 0, 'Xatboshi B: «language determines thought» degan kuchli daʼvo qoʻllab-quvvatlanmadi va keyin «in a more modest form» '
                      'qaytdi — dadil daʼvodan kamtarroq savolga oʻtish.'),
         hd(3, H2, 1, 'Xatboshi D: ogʻzaki topshiriq bajarilganda effekt zaiflashadi — til idrokka «in the moment» taʼsir qiladi, '
                      '«rather than permanently» — yaʼni effekt vaqtinchalik boʻlishi mumkin.'),
         hd(4, H2, 2, 'Xatboshi E: baʼzi jamoalar chap-oʻng oʻrniga «fixed compass directions» dan foydalanadi.'),
         hd(6, H2, 4, 'Xatboshi G: farq tildanmi yoki madaniyatdanmi — ajratish qiyin; «Nor is the direction of influence always clear» — '
                      'sabab va oqibatni ajratish muammosi.'),
         hd(7, H2, 5, 'Xatboshi H: «A widely held middle position» — til fikrni qamamaydi, lekin taʼsirsiz ham emas; bu murosali qarash.'),
         tf('The writer suggests that most popular stories about language and thought are entirely accurate.', 'F',
            '«many of them are exaggerated or simply inaccurate» — muallif bunga qarama-qarshi fikrda.', 0, ng=True),
         tf('One reason the strong form of linguistic relativity lost support is that translation between languages is possible.', 'T',
            '«proved difficult to support. … translation, although imperfect, is clearly possible» — bu dalil kuchli versiyaga qarshi.', 1, ng=True),
         tf('The Russian speakers in the experiments were also faster at distinguishing shades of green.', 'NG',
            'Matnda faqat koʻk rang tuslari haqida gap boradi; yashil rang haqida hech narsa aytilmagan.', 3),
         tf('Speakers who rely on compass directions are less accurate at tracking their orientation than other speakers.', 'F',
            '«such speakers tend to keep track of their orientation with remarkable accuracy» — aksincha, juda aniq.', 4, ng=True),
         gap('Summary: Russian treats lighter and darker blue as two separate ___ rather than shades of one colour.',
             ['basic colours', 'basic colors', 'colours', 'colors'],
             '«treats lighter and darker blue as two distinct basic colours rather than shades of a single one».', 3, 2),
         gap('Summary: The Russian speakers\' advantage weakened when they had to carry out a ___ at the same time.',
             ['verbal task'], '«asked to perform a verbal task» — simultaneously = at the same time.', 3, 2),
         gap('Summary: Uzbek has no grammatical gender and uses one ___ to refer to both men and women.', 'pronoun',
             '«uses the single pronoun u for both he and she».', 5, 2),
         ch('What does the writer say about studies with bilingual speakers?',
            ['They have completely solved the methodological problem.', 'They offer a partial solution but raise new difficulties.',
             'They prove that culture has no effect on thinking.', 'They show that bilingual people think more clearly.'], 1,
            '«offer one way around this problem, although they introduce complications of their own» — qisman yechim, lekin yangi qiyinchiliklar.', 6),
         ch('What is the purpose of the comparison with well-worn paths in the final paragraph?',
            ['to argue that language completely controls perception', 'to suggest that language guides thinking without restricting it',
             'to show that languages gradually change over time', 'to explain why some people learn languages more easily'], 1,
            '«which we follow most easily but are not forced to take» — til yoʻnaltiradi, lekin majburlamaydi. '
            '«tinted glasses» oʻxshatishi esa rad etiladi.', 7),
     ])


# ---------------------------------------------------------------- 3-test
H3 = ['Seasonal floods and a contested theory of power', 'Traces of a once-cultivated landscape',
      'Why old channels are hard to find and to date', 'The chemistry behind a slow decline',
      'Disputed evidence from ancient crop records', 'Several reasons for leaving the land',
      'Ancient problems with present-day relevance', 'The engineering of the first great dams',
      'Trade between Khorezm and Mesopotamia']

text(B, 'c1-28-test3', '3-test: Qadimgi irrigatsiya', 'Water, Salt and Civilisation', 'C1', 'exam',
     L('Tarix va arxeologiya', 'History and archaeology'),
     intro('Mesopotamiya va Xorazmdagi qadimgi sugʻorish tizimlari hamda tuproq shoʻrlanishi haqidagi matn.'),
     [
         P("Long before modern dams and pumps, farmers in some of the driest regions of the ancient world learned to move "
           "water from rivers to fields on a remarkable scale. In the floodplains of the Tigris and Euphrates, and along the "
           "lower course of the Amu Darya in Central Asia, irrigation made it possible to grow crops where rainfall alone would "
           "never have sustained them. The surplus food that resulted supported towns, specialised crafts and, eventually, "
           "complex states. Yet the same technology that underpinned these societies also carried a hidden cost, one that "
           "unfolded so slowly that it may have been barely perceptible to any single generation."),
         P("Southern Mesopotamia presented farmers with both an opportunity and a challenge. The soils were fertile and the "
           "rivers abundant, but rainfall was insufficient for reliable farming, and the annual floods tended to arrive in "
           "spring, when winter crops were nearing harvest, rather than when water was most needed. Farmers therefore built "
           "canals to distribute water, along with embankments to protect fields from unwanted floods. A once-influential "
           "theory held that the need to manage such systems gave rise to powerful centralised governments. Archaeological "
           "evidence has since complicated this picture, suggesting that many early canals were modest in scale and could have "
           "been maintained by local communities long before large states appeared."),
         P("In ancient Khorezm, on the lower Amu Darya south of the Aral Sea, irrigation likewise shaped human settlement for "
           "many centuries. Archaeologists have traced networks of canals across areas that are now desert, some of them "
           "stretching for many kilometres, along with the remains of fortified settlements whose walls still stand in parts of "
           "present-day Karakalpakstan and the Khorezm region. The origins of irrigated farming there are generally placed at "
           "least as early as the first millennium BC, although precise dates remain debated. What is clear is that the "
           "landscape once supported far more cultivation than its current appearance would suggest."),
         P("Studying ancient canals poses particular problems. A canal is essentially a ditch, and once abandoned it fills with "
           "wind-blown sand and silt, becoming almost invisible at ground level. A long-running Soviet archaeological "
           "expedition in Khorezm, begun in the late 1930s, came to make extensive use of aerial photography, which revealed the lines of former "
           "channels as faint marks on the surface; today, satellite imagery serves a similar purpose. Dating, however, remains "
           "difficult. Canals were frequently cleaned, deepened and redirected over centuries, so a single channel may contain "
           "layers from very different periods, and pottery found nearby does not necessarily indicate when the water was flowing."),
         P("The hidden cost mentioned earlier is salinisation, the gradual accumulation of salts in the soil. All river water "
           "carries small quantities of dissolved salts. When it is spread over fields in a hot, dry climate, much of the water "
           "evaporates or is taken up by plants, while the salts remain behind. Over-irrigation creates a further danger: if "
           "more water is applied than can drain away, the water table rises, and once it comes close to the surface, "
           "groundwater is drawn upwards and evaporates, leaving a white crust of salt. Without adequate drainage, land that has "
           "been cultivated for generations can gradually lose its fertility."),
         P("Whether salinisation contributed to the decline of particular ancient societies is a matter of continuing debate. "
           "Some scholars, drawing on ancient texts from southern Mesopotamia, have argued that over a period of centuries "
           "farmers grew less wheat and more barley, a crop known to be more tolerant of salt, and that recorded yields fell. "
           "Others have cautioned that the written evidence is fragmentary and open to different interpretations, and that "
           "changes in crop choice may also reflect economic or dietary preferences. Most specialists would probably accept that "
           "salinity was a real and recurring problem, while doubting that it alone can explain the rise and fall of cities."),
         P("In Khorezm, too, the abandonment of irrigated land seems to have had several causes. The Amu Darya has shifted its "
           "course more than once over the centuries, leaving some canal heads without water, and periods of warfare and "
           "political instability may have disrupted the collective labour that maintenance required. Salinity probably played "
           "a part in some areas. Disentangling these factors is difficult, not least because the archaeological record seldom "
           "reveals why people left, only that they did."),
         P("These ancient experiences are of more than historical interest. Large parts of Central Asia today face serious "
           "problems of soil salinity, linked to the extensive irrigation developed during the twentieth century and to "
           "inadequate drainage. Modern engineers can measure salt levels and install drainage systems that ancient farmers "
           "lacked, yet the underlying chemistry is unchanged. Not only do the canals of Khorezm and Mesopotamia testify to "
           "human ingenuity, but they also remind us that a system which works well for decades may still be unsustainable "
           "over centuries."),
     ],
     [G('floodplain', 'daryo qayiri, toshqin tekisligi'), G('sustain', 'ushlab turmoq, taʼminlamoq'),
      G('surplus', 'ortiqcha mahsulot'), G('underpin', 'asos boʻlmoq, tayanch boʻlmoq'),
      G('perceptible', 'sezilarli, payqash mumkin boʻlgan'), G('embankment', 'damba, qirgʻoq uyumi'),
      G('give rise to / gave rise to', 'yuzaga keltirmoq, sabab boʻlmoq'), G('fortified', 'mustahkamlangan, qalʼa devori bilan oʻralgan'),
      G('silt', 'loyqa, il'), G('aerial photography', 'havodan suratga olish'),
      G('salinisation', 'shoʻrlanish'), G('accumulation', 'toʻplanish'), G('water table', 'yer osti suvlari sathi'),
      G('fragmentary', 'parcha-parcha, toʻliq boʻlmagan'), G('recurring', 'takrorlanib turadigan'),
      G('disentangle', 'ajratib olmoq, chigalini yechmoq'), G('ingenuity', 'zukkolik, ixtirochilik'),
      G('unsustainable', 'uzoq davom ettirib boʻlmaydigan, barqaror boʻlmagan')],
     [GN('c58-inversion', 'Inversiya: Not only do … but … also',
         'Not only do the canals of Khorezm and Mesopotamia testify to human ingenuity'),
      GN('c60-nominalisation', 'Nominalizatsiya: the gradual accumulation of salts',
         'the gradual accumulation of salts in the soil')],
     [
         hd(2, H3, 1, 'Xatboshi C: hozir choʻl boʻlgan joylarda kanallar va qalʼalar izlari — «the landscape once supported far more '
                      'cultivation than its current appearance would suggest».'),
         hd(3, H3, 2, 'Xatboshi D: tashlab ketilgan kanal qum bilan toʻlib koʻrinmay qoladi, sanasini aniqlash esa «remains difficult».'),
         hd(4, H3, 3, 'Xatboshi E: shoʻrlanish mexanizmi — bugʻlanish, tuzlarning qolishi, yer osti suvi koʻtarilishi; asta-sekin hosildorlik yoʻqoladi.'),
         hd(5, H3, 4, 'Xatboshi F: bugʻdoy oʻrniga arpa ekilgani haqidagi yozma maʼlumotlar bahsli — «fragmentary and open to different interpretations».'),
         hd(6, H3, 5, 'Xatboshi G: Xorazmda yerlar tashlab ketilishining bir necha sababi — daryo oʻzanining oʻzgarishi, urushlar, shoʻrlanish. '
                      '«Trade between Khorezm and Mesopotamia» chalgʻitadi: savdo haqida gap yoʻq.'),
         tf('In southern Mesopotamia, the annual floods usually came at the time when crops most needed water.', 'F',
            'Toshqinlar bahorda, hosil yigʻishga yaqin kelgan — «rather than when water was most needed».', 1, ng=True),
         tf('Archaeological evidence suggests that some early canals may have been managed without large states.', 'T',
            '«could have been maintained by local communities long before large states appeared».', 1, ng=True),
         tf('The Soviet expedition in Khorezm discovered more canals than any later archaeological project.', 'NG',
            'Ekspeditsiya aerofotosuratdan foydalangani aytilgan, lekin topilgan kanallar sonini keyingi loyihalar bilan solishtirish yoʻq.', 3),
         tf('Barley is described as more able to cope with salty soil than wheat.', 'T',
            '«barley, a crop known to be more tolerant of salt» — more tolerant = more able to cope with.', 5, ng=True),
         gap('Summary: Once abandoned, a canal fills with wind-blown sand and ___, and becomes almost invisible.', 'silt',
             '«it fills with wind-blown sand and silt, becoming almost invisible at ground level».', 3, 2),
         gap('Summary: When too much water is applied to fields, the ___ rises towards the surface.', 'water table',
             '«if more water is applied than can drain away, the water table rises».', 4, 2),
         gap('Summary: As groundwater evaporates, it leaves a white ___ of salt on the land.', 'crust',
             '«leaving a white crust of salt».', 4, 2),
         ch('According to paragraph D, why can pottery found near a canal be misleading?',
            ['It is usually too damaged to identify.', 'It may not show when the canal actually carried water.',
             'It was often brought from distant regions.', 'It is always older than the canal itself.'], 1,
            '«pottery found nearby does not necessarily indicate when the water was flowing».', 3),
         ch('What is the writer\'s main point in the final paragraph?',
            ['Modern engineering has fully solved the problem of salinity.',
             'A system that succeeds for decades may still fail in the long term.',
             'Ancient canals were more efficient than modern ones.',
             'Central Asia should return to traditional methods of irrigation.'], 1,
            '«a system which works well for decades may still be unsustainable over centuries». Muhandislar tuz darajasini oʻlchay oladi, '
            'lekin «the underlying chemistry is unchanged» — muammo toʻliq hal boʻlgani aytilmaydi.', 7),
     ])


# ---------------------------------------------------------------- 4-test
H4 = ['A common mistake reveals two separate problems', 'Where the energy of a sound wave goes',
      'Turning sound into a little warmth', 'The particular challenge of deep sounds',
      'Weight, airtightness and separate layers', 'Devices tuned to a narrow range',
      'Aiming for balance rather than silence', 'Why modern buildings are noisier than old ones',
      'The effects of urban noise on health']

text(B, 'c1-29-test4', '4-test: Tovush yutuvchi materiallar', 'Absorbing the Noise: How Acoustic Materials Work', 'C1', 'exam',
     L('Fizika va arxitektura', 'Physics and architecture'),
     intro('tovushni yutuvchi va izolyatsiya qiluvchi materiallar qanday ishlashi haqidagi ilmiy-texnik matn.'),
     [
         P("Anyone who has tried to quieten a noisy flat by fixing soft foam panels to the walls is likely to have been "
           "disappointed. The panels may make the room itself sound less echoey, but the neighbour's television remains "
           "stubbornly audible. This common experience points to a distinction that lies at the heart of architectural "
           "acoustics and is frequently misunderstood. Controlling sound within a space and preventing sound from passing "
           "between spaces are different problems, and they are solved by materials that work in fundamentally different ways."),
         P("Sound is a pressure wave travelling through the air, and when it strikes a surface, its energy is divided in three "
           "ways. Part of it is reflected back into the room, part is absorbed by the material, and part passes through to the "
           "other side. Hard, smooth surfaces such as concrete, glass and tiles reflect most of the energy that reaches them, "
           "which is why empty rooms with bare walls tend to sound harsh. Sound absorption refers to reducing the reflected "
           "portion and thus improving conditions inside a room, whereas sound insulation is concerned with limiting the "
           "portion that is transmitted."),
         P("The most familiar absorbers are porous materials, including mineral wool, open-cell foam and heavy fabrics. Their "
           "effectiveness depends on a network of tiny interconnected air spaces. As a sound wave enters the material, it forces "
           "air to move back and forth through these narrow passages, and friction between the moving air and the fibres "
           "converts some of the sound energy into heat. The amount of heat produced is minute, far too small to be felt, but "
           "the cumulative effect on the reflected sound can be considerable. It follows that a porous absorber whose surface is "
           "sealed, for example by a thick coat of paint, may lose much of its effectiveness, since air can no longer enter it freely."),
         P("Porous absorbers have an important limitation, however. They work best at middle and high frequencies, whose "
           "wavelengths are relatively short. Low-frequency sounds, such as the hum of machinery or the bass in music, have "
           "wavelengths that can be several metres long, and to absorb them effectively, a porous layer generally needs to be "
           "very thick. Designers sometimes compensate by mounting panels at a distance from the wall, because the air gap "
           "behind the material allows it to work over a broader range of frequencies. Even so, deep bass remains among the "
           "hardest sounds to control."),
         P("Insulation relies on quite different principles. To stop sound passing from one room to another, a barrier should "
           "above all be heavy and airtight. A massive wall is harder for a pressure wave to set into vibration, and the less "
           "it vibrates, the less sound it radiates on the other side. Increasing mass brings diminishing returns, though, so "
           "builders often use a further technique: dividing a wall into two layers that are not rigidly connected, with "
           "absorbent material in the cavity between them. Equally important is the elimination of gaps, since even a small "
           "opening around a door or pipe can allow a surprising amount of sound to leak through."),
         P("A third category, resonant absorbers, is designed specifically to deal with the low frequencies that porous "
           "materials struggle with. One type consists of a thin panel mounted over an enclosed air space; the panel vibrates "
           "most strongly at a particular frequency and loses energy as it does so. Another, known as a Helmholtz resonator, "
           "works on the same principle as the note produced by blowing across the neck of a bottle: the air in the neck "
           "oscillates against the cushion of air inside, absorbing energy most efficiently around one frequency. Because such "
           "devices are tuned to a narrow range, they are typically used to solve a specific problem rather than to treat a "
           "room in general. Interestingly, a Roman writer on architecture described bronze vessels placed in theatres to "
           "modify their sound, although how effective such devices actually were is uncertain."),
         P("Getting the acoustics of a room right is rarely a matter of maximising absorption. A space that absorbs too much "
           "sounds unnaturally dead, and speech and music lose their liveliness. Concert halls require a degree of "
           "reverberation, the persistence of sound after its source has stopped, while classrooms and offices need much less, "
           "because excessive reverberation blurs the consonants on which the intelligibility of speech depends. It is this "
           "balance, rather than the elimination of echoes, that acoustic designers aim to achieve, and it explains why the "
           "same material may be ideal in one setting and inappropriate in another."),
         P("Similar principles are increasingly applied on the scale of whole cities. Barriers along busy roads block the "
           "direct path between traffic and nearby homes, and some road surfaces are made porous so that they absorb part of "
           "the noise generated by tyres. Trees and shrubs, by contrast, tend to reduce traffic noise only modestly unless they "
           "are planted in deep belts, although they may make an environment feel quieter. Researchers are also exploring "
           "engineered structures, sometimes called acoustic metamaterials, which might control sound in ways that ordinary "
           "materials cannot, though most remain at an experimental stage."),
     ],
     [G('stubbornly', 'oʻjarlik bilan, qaysarlarcha'), G('audible', 'eshitiladigan'),
      G('porous', 'gʻovak, teshikchali'), G('interconnected', 'oʻzaro bogʻlangan'), G('friction', 'ishqalanish'),
      G('minute', 'juda kichik, arzimas'), G('cumulative', 'jamlangan, yigʻilib boradigan'),
      G('compensate', 'oʻrnini toʻldirmoq'), G('airtight', 'havo oʻtkazmaydigan, germetik'),
      G('diminishing returns', 'kamayib boruvchi samara'), G('cavity', 'boʻshliq'),
      G('resonant', 'rezonansli'), G('oscillate', 'tebranmoq'), G('reverberation', 'reverberatsiya, tovushning sekin soʻnishi'),
      G('intelligibility', 'tushunarlilik, aniq eshitilish'), G('modestly', 'ozgina, kamtarona darajada'),
      G('experimental stage', 'tajriba bosqichi')],
     [GN('c57-cleft-sentences', 'Taʼkidli gap: It is … that …',
         'It is this balance, rather than the elimination of echoes, that acoustic designers aim to achieve'),
      GN('c43-comparison-advanced', 'Murakkab qiyoslash: the less …, the less …',
         'the less it vibrates, the less sound it radiates on the other side')],
     [
         hd(1, H4, 1, 'Xatboshi B: tovush energiyasi uch yoʻlga boʻlinadi — «reflected … absorbed … passes through».'),
         hd(2, H4, 2, 'Xatboshi C: gʻovak materialda ishqalanish tovush energiyasining bir qismini issiqlikka aylantiradi — '
                      '«converts some of the sound energy into heat», issiqlik esa «minute».'),
         hd(4, H4, 4, 'Xatboshi E: izolyatsiya — devor «heavy and airtight» boʻlishi, ikki qatlam va tirqishlarni yoʻqotish.'),
         hd(6, H4, 6, 'Xatboshi G: maqsad maksimal yutish emas, muvozanat — «It is this balance, rather than the elimination of echoes». '
                      '«Why modern buildings are noisier» chalgʻitadi: bu haqda gap yoʻq.'),
         tf('Fixing soft foam panels to the walls is an effective way to stop a neighbour\'s television being heard.', 'F',
            '«the neighbour\'s television remains stubbornly audible» — panellar faqat xona ichidagi aks-sadoni kamaytiradi.', 0, ng=True),
         tf('Rooms with bare walls tend to sound harsh because hard surfaces reflect most of the sound energy.', 'T',
            '«reflect most of the energy that reaches them, which is why empty rooms with bare walls tend to sound harsh».', 1, ng=True),
         tf('Mineral wool absorbs high frequencies more effectively than open-cell foam.', 'NG',
            'Ikkalasi ham gʻovak material sifatida sanab oʻtilgan, lekin ular bir-biri bilan solishtirilmagan.', 2),
         tf('Covering a porous absorber with thick paint may make it less effective.', 'T',
            '«a porous absorber whose surface is sealed, for example by a thick coat of paint, may lose much of its effectiveness».', 2, ng=True),
         tf('Trees and shrubs usually reduce traffic noise substantially, even when planted in narrow rows.', 'F',
            '«reduce traffic noise only modestly unless they are planted in deep belts» — substantially emas, modestly.', 7, ng=True),
         gap('Summary: Low-frequency sounds have wavelengths that may be several ___ long.', ['metres', 'meters'],
             '«have wavelengths that can be several metres long».', 3, 2),
         gap('Summary: Panels are sometimes mounted away from the wall, because the ___ behind them lets them work over more frequencies.',
             'air gap', '«the air gap behind the material allows it to work over a broader range of frequencies».', 3, 2),
         gap('Summary: In classrooms, excessive reverberation blurs the ___ that make speech understandable.', 'consonants',
             '«excessive reverberation blurs the consonants on which the intelligibility of speech depends».', 6, 2),
         ch('Why does the writer mention blowing across the neck of a bottle?',
            ['to explain the principle behind one type of resonant absorber', 'to show that glass reflects most sound',
             'to describe a device used in ancient theatres', 'to illustrate how porous materials absorb sound'], 0,
            '«known as a Helmholtz resonator, works on the same principle as the note produced by blowing across the neck of a bottle». '
            'Qadimgi teatrlar haqida esa bronza idishlar tilga olinadi.', 5),
         ch('What does the writer say about acoustic metamaterials?',
            ['They have already replaced roadside barriers in many cities.', 'Most of them are still being tested.',
             'They are less effective than trees and shrubs.', 'They work only at high frequencies.'], 1,
            '«though most remain at an experimental stage» — koʻpchiligi hali sinov bosqichida.', 7),
     ])


# ---------------------------------------------------------------- 5-test
H5 = ['Confidence in science is real but uneven', 'A discredited assumption about ignorance',
      'Trust depends on more than information', 'A temptation to hide doubt',
      'The hidden costs of overconfidence', 'Ordinary people as data collectors',
      'Making volunteer records reliable', 'Why scientists receive less praise than doctors',
      'Teaching science more effectively in schools']

text(B, 'c1-30-test5', '5-test: Ilm-fan va jamoatchilik', 'Science, Trust and the Public', 'C1', 'exam',
     L('Fan va jamiyat', 'Science and society'),
     intro('jamiyatning ilm-fanga ishonchi, noaniqlikni tushuntirish va fuqarolik ilmi loyihalari haqidagi matn.'),
     [
         P("Scientific knowledge shapes decisions in almost every area of modern life, from the medicines people take to the "
           "policies governments adopt on energy, food and the environment. It might be expected, therefore, that the "
           "relationship between scientists and the wider public would be a settled one. In reality, it is complex and at times "
           "uneasy. Surveys conducted in many countries generally suggest that scientists are among the more trusted groups in "
           "society, yet that trust is far from uniform. It can vary considerably between countries and social groups, and it "
           "tends to be weakest on issues that have become entangled with political or moral disputes."),
         P("For a long time, a widespread assumption among scientists and policymakers was that public scepticism stemmed "
           "largely from a lack of knowledge. If people only understood the facts, the reasoning went, they would accept the "
           "conclusions that experts had reached. This approach, which critics later labelled the deficit model, led to "
           "campaigns aimed at filling gaps in public understanding. Research on science communication has cast considerable "
           "doubt on it. Greater scientific knowledge does not reliably lead to greater acceptance, and on some contested "
           "issues, people with more knowledge appear to be more, not less, divided along the lines of their existing beliefs."),
         P("One explanation is that people evaluate scientific claims not in isolation but in the light of their values, their "
           "identities and their confidence in the institutions involved. A message may be rejected less because of its content "
           "than because of who delivers it, or because accepting it seems to imply changes that people regard as threatening "
           "to their way of life. Trust, in this sense, is not simply a judgement about whether a piece of information is "
           "accurate. It also reflects whether people believe that those providing it are competent, honest and acting in the "
           "public interest."),
         P("These insights bear directly on one of the most difficult questions in science communication: how to talk about "
           "uncertainty. Almost all scientific findings come with a degree of uncertainty, and much research consists precisely "
           "of estimating how large it is. Communicators, however, have often feared that acknowledging uncertainty would make "
           "science appear weak, give ammunition to critics or leave the public confused about what to do. As a result, "
           "findings have sometimes been presented with greater confidence than the evidence warranted."),
         P("Such caution may be misplaced. Some experimental research suggests that openly communicating uncertainty, for "
           "example by giving a range rather than a single figure, reduces trust only slightly, if at all, provided that it is "
           "done clearly. Overstated certainty, by contrast, carries a risk of its own: when confident advice later has to be "
           "revised, as new evidence inevitably emerges, the change can appear to be a reversal or even a sign of incompetence. "
           "Had the provisional nature of early advice been explained from the outset, many observers argue, later revisions "
           "might have been accepted as a normal part of the scientific process rather than as evidence of failure."),
         P("Alongside these debates, a different kind of relationship between science and the public has been expanding. In "
           "citizen science projects, members of the public contribute directly to research, most often by collecting or "
           "classifying data. Birdwatching offers some of the best-known examples. In one bird count in North America, which "
           "has been running for more than a century, volunteers record the birds they see within defined areas on a single day "
           "during a set period each winter, and similar counts take place in many other countries. More recently, online "
           "platforms have allowed thousands of people to help classify images of animals, plants or distant galaxies from "
           "their own homes."),
         P("Such projects can gather information on a scale that professional researchers could never achieve alone, covering "
           "wide areas over many years. Their value, however, depends on the quality of the data. Volunteers vary in skill, and "
           "they tend to survey places that are convenient or attractive rather than a representative sample of the landscape. "
           "Project organisers address these problems through standardised methods, training, checks on unusual records and "
           "statistical techniques that take account of differences in observer effort and experience. Used carefully, citizen "
           "science data have contributed to research on matters such as changes in the distribution of bird species."),
         P("Advocates also hope that participation will strengthen public understanding of how science works, including its "
           "routines of checking, revising and quantifying uncertainty. Whether it does so is harder to establish, since "
           "volunteers are often people who were already interested in science. There are ethical questions too, concerning "
           "how volunteers are credited and whether projects serve their interests as well as those of researchers. "
           "Nevertheless, citizen science illustrates a broader shift in thinking: the public is increasingly seen not merely "
           "as an audience to be informed but as a potential partner in the production of knowledge."),
     ],
     [G('uniform', 'bir xil, yagona'), G('entangled with', '… bilan chirmashib ketgan'),
      G('scepticism', 'shubhali munosabat, skeptitsizm'), G('cast doubt on', '… ni shubha ostiga qoʻymoq'),
      G('contested', 'bahsli, munozarali'), G('in isolation', 'alohida holda, boshqalardan ajratib'),
      G('competent', 'malakali, layoqatli'), G('acknowledge', 'tan olmoq'),
      G('ammunition', 'qarshi dalil, «oʻq-dori»'), G('warrant', 'asoslamoq, oqlamoq'), G('misplaced', 'oʻrinsiz, asossiz'),
      G('overstated', 'boʻrttirilgan'), G('provisional', 'vaqtinchalik, dastlabki'), G('from the outset', 'boshidanoq'),
      G('representative sample', 'reprezentativ (vakillik qiluvchi) tanlanma'), G('advocate', 'tarafdor, himoyachi'),
      G('credit', 'hissasini tan olmoq, muallif sifatida koʻrsatmoq')],
     [GN('c50-inverted-conditionals', 'Inversiyali shart gap: Had … been explained, … might have been',
         'Had the provisional nature of early advice been explained from the outset'),
      GN('c34-participle-clauses', 'Sifatdoshli ergash gap: Used carefully, …',
         'Used carefully, citizen science data have contributed to research')],
     [
         hd(1, H5, 1, 'Xatboshi B: «deficit model» — shubha bilim yetishmasligidan degan taxmin; tadqiqotlar «cast considerable doubt on it». '
                      '«Teaching science more effectively in schools» chalgʻitadi: maktab taʼlimi haqida gap yoʻq.'),
         hd(2, H5, 2, 'Xatboshi C: ishonch faqat maʼlumot toʻgʻriligiga emas, qadriyatlar, oʻzlik va institutlarga ham bogʻliq — '
                      '«Trust … is not simply a judgement about whether a piece of information is accurate».'),
         hd(3, H5, 3, 'Xatboshi D: muloqotchilar noaniqlikni tan olishdan qoʻrqqan va natijalarni haddan ortiq ishonch bilan berishgan — '
                      'shubhani yashirish vasvasasi.'),
         hd(4, H5, 4, 'Xatboshi E: haddan tashqari ishonch xavfli — maslahat oʻzgarsa, «a sign of incompetence» kabi koʻrinadi.'),
         hd(6, H5, 6, 'Xatboshi G: koʻngillilar maʼlumotlari sifati muammosi va yechimlar — «standardised methods, training, checks…».'),
         tf('According to the writer, trust in scientists is the same across different social groups.', 'F',
            '«trust is far from uniform. It can vary considerably between countries and social groups».', 0, ng=True),
         tf('The term deficit model was introduced by people who supported this approach.', 'F',
            '«which critics later labelled the deficit model» — atamani tarafdorlar emas, tanqidchilar qoʻllagan.', 1, ng=True),
         tf('Scientific findings have sometimes been presented as more certain than the evidence justified.', 'T',
            '«findings have sometimes been presented with greater confidence than the evidence warranted» — warranted = justified.', 3, ng=True),
         tf('Volunteers in the North American bird count must pass a written identification test.', 'NG',
            'Koʻngillilar qushlarni qayd etishi aytilgan, lekin ular uchun imtihon haqida maʼlumot yoʻq.', 5),
         gap('Summary: Some research suggests that giving a ___ instead of a single figure reduces trust only slightly, if at all.',
             'range', '«by giving a range rather than a single figure, reduces trust only slightly, if at all».', 4, 2),
         gap('Summary: Volunteers often survey convenient places instead of a ___ sample of the landscape.', 'representative',
             '«rather than a representative sample of the landscape».', 6, 2),
         gap('Summary: Statistical techniques take into account differences in observer ___ and experience.', 'effort',
             '«take account of differences in observer effort and experience».', 6, 2),
         ch('Why, according to the writer, is it hard to show that citizen science improves understanding of science?',
            ['Volunteers are rarely asked about their views.', 'Participants are often already interested in science.',
             'Most projects are too short to have any effect.', 'Researchers refuse to use volunteers\' data.'], 1,
            '«Whether it does so is harder to establish, since volunteers are often people who were already interested in science».', 7),
         ch('Which statement best reflects the shift in thinking described in the final paragraph?',
            ['The public should simply receive information from experts.',
             'The public is increasingly regarded as a possible partner in research.',
             'Members of the public cannot provide useful scientific data.',
             'Public interest in science has declined in recent years.'], 1,
            '«not merely as an audience to be informed but as a potential partner in the production of knowledge».', 7),
     ])
