"""C1 · 5-boʻlim: Adabiyot va biografiya (Literature and biography)"""
from lib import *

B = 'c1'


# ---------------------------------------------------------------- 21: Abdulla Qodiriy
text(B, 'c1-21-qodiriy', 'Abdulla Qodiriy', 'Abdulla Qodiriy and the Birth of the Uzbek Novel', 'C1', 'exam',
     L('Adabiyot', 'Literature'),
     'Biografik-akademik matn: oʻzbek romanchiligining asoschisi Abdulla Qodiriy hayoti va ijodi. Topshiriqlar: '
     'True/False/Not Given, test savollari (muallif maqsadi, asosiy fikr) va gap toʻldirish. Taxminan 20 daqiqa ajrating: '
     'avval matnni tez koʻrib chiqib har bir xatboshining mavzusini belgilang, keyin TFNG savollarida sanalar va '
     '«first», «only», «of his own free will» kabi soʻzlarga alohida eʼtibor bering — aynan ular javobni hal qiladi.',
     [
         P("Few writers occupy a position in their national literature comparable to the one Abdulla Qodiriy holds in "
           "Uzbek letters. Born in Tashkent in 1894, he lived through one of the most turbulent periods in the history of "
           "Central Asia, witnessing the final decades of Russian imperial administration, the upheavals of revolution "
           "and civil war, and the consolidation of Soviet power. His reputation rests chiefly on a single book, Oʻtkan "
           "kunlar, usually rendered in English as Days Gone By, which is widely regarded as the first Uzbek novel. Yet to "
           "treat him simply as the author of one celebrated work would be to underestimate both the range of his writing "
           "and the extent of his influence."),
         P("Qodiriy came of age at a time when educated circles in Turkestan were engaged in intense debate about how "
           "their society should respond to modernity. Reform-minded intellectuals, often referred to as the Jadids, "
           "argued for new methods of schooling, a revitalised press and a literature capable of addressing contemporary "
           "problems. Qodiriy, who had received both a traditional education and some schooling of a more modern kind, is "
           "generally associated with this current of thought. His early career was devoted largely to journalism, and he "
           "became known for satirical sketches in which the pretensions of officials and the absurdities of everyday "
           "life were exposed with considerable wit."),
         P("Days Gone By first appeared in instalments in the early 1920s before being published as a complete book in "
           "the middle of the decade. Set in the mid-nineteenth century, principally in Tashkent and Margilan, the novel "
           "follows the love of Otabek, a young Tashkent merchant, for Kumush, a girl from Margilan. Their happiness, "
           "however, is repeatedly threatened, not only by the intrigues of rivals but by the social conventions of the "
           "day. Pressed by his family into a second marriage, Otabek finds himself trapped in a household where jealousy "
           "eventually leads to tragedy. Around this private drama the author weaves a wider picture of a society weakened "
           "by factional feuds and corrupt officials, a society that, the novel implies, contributed to its own decline."),
         P("What made the novel so striking to its first readers was less its plot than its manner. Much earlier prose "
           "in the region, critics have observed, had tended towards didactic tales and ornate, formulaic description, "
           "whereas Qodiriy offered characters with recognisable inner lives, whose motives were revealed gradually "
           "through dialogue and action. His language, too, marked a departure: rather than relying on the elevated "
           "vocabulary of classical literature, he drew extensively on the spoken Uzbek of his time, giving his narrative "
           "an immediacy that readers had seldom encountered on the page. It is this combination of psychological depth "
           "and vernacular vitality that critics most often cite when explaining why the book has never lost its "
           "readership."),
         P("Qodiriy's second novel, Mehrobdan chayon, which may be translated as The Scorpion from the Altar, appeared "
           "towards the end of the 1920s. Set in the Kokand Khanate, it is again built around a love story, but its "
           "satirical edge is sharper. The title itself points to the novel's central concern: hypocrisy concealed behind "
           "a façade of piety and authority. Through its portrait of scheming courtiers and self-serving clerics, the book "
           "develops the critique of power that had been present in his earlier work, while confirming his mastery of the "
           "historical novel as a vehicle for reflecting on the present."),
         P("His career was cut short in the most brutal manner. During the wave of mass repression that swept the Soviet "
           "Union in the late 1930s, Qodiriy was arrested, and in 1938 he was executed, sharing the fate of many other "
           "prominent Uzbek writers and thinkers of his generation. For a considerable time afterwards, his name could "
           "scarcely be mentioned in public, and his books were removed from circulation. Only after Stalin's death was he "
           "officially rehabilitated, and it was not until later still that his novels gradually regained the place they "
           "now occupy in schools and libraries."),
         P("Qodiriy's legacy is visible throughout modern Uzbek prose. Later novelists who turned to the past in order to "
           "explore questions of identity, morality and national memory worked, consciously or not, within a tradition he "
           "had established. Days Gone By has been adapted for stage and screen, and its characters remain familiar to a "
           "wide public. Perhaps the most telling measure of his achievement, however, is that readers continue to "
           "approach his work not as a historical curiosity but as living literature, finding in its portrayal of love, "
           "ambition and social pressure concerns that remain recognisably their own."),
     ],
     [G('turbulent', 'notinch, toʻlqinli (davr)'), G('upheaval', 'gʻalayon, keskin oʻzgarish'),
      G('consolidation', 'mustahkamlanish'), G('underestimate', 'yetarlicha baholamaslik'),
      G('came of age', 'voyaga yetdi, (shaxs sifatida) shakllandi'), G('revitalise', 'jonlantirmoq, yangi hayot bagʻishlamoq'),
      G('pretension', 'daʼvogarlik, oʻzini katta tutish'), G('instalment', 'qism (davomli nashrda)'),
      G('intrigue', 'fitna, igʻvo'), G('factional feud', 'guruhlar oʻrtasidagi adovat'),
      G('didactic', 'pand-nasihatli, ibratomuz'), G('ornate', 'bezakli, dabdabali'),
      G('vernacular', 'xalq soʻzlashuv tili'), G('façade', 'tashqi koʻrinish, niqob'),
      G('piety', 'taqvodorlik'), G('scheming', 'fitnachi, makkor'),
      G('rehabilitate', 'oqlamoq (siyosiy jihatdan)'), G('legacy', 'meros')],
     [GN('c16-reporting-passive', 'Majhul nisbatda baho: is widely regarded as',
         'which is widely regarded as the first Uzbek novel'),
      GN('c57-cleft-sentences', 'Taʼkidli gap: It is … that',
         'It is this combination of psychological depth and vernacular vitality that critics most often cite')],
     [
         tf('Qodiriy was born in a city that is also one of the main settings of Days Gone By.', 'T',
            'A: «Born in Tashkent in 1894»; C: roman «principally in Tashkent and Margilan» da kechadi. Ikki maʼlumotni bogʻlab xulosa chiqariladi.', 2, ng=True),
         tf('Qodiriy studied abroad before beginning his career as a journalist.', 'NG',
            'B xatboshida u anʼanaviy va zamonaviyroq taʼlim olgani aytilgan, lekin chet elda oʻqigani haqida hech narsa yoʻq.', 1),
         tf('Days Gone By was originally released as a single complete volume.', 'F',
            '«first appeared in instalments in the early 1920s before being published as a complete book» — avval qismlarga boʻlib chop etilgan.', 2, ng=True),
         tf('Otabek enters his second marriage of his own free will.', 'F',
            '«Pressed by his family into a second marriage» — oila bosimi bilan, oʻz xohishi bilan emas.', 2, ng=True),
         tf('The novel suggests that internal divisions played a part in the decline of the society it depicts.', 'T',
            '«a society weakened by factional feuds … contributed to its own decline» — «internal divisions» = «factional feuds».', 2, ng=True),
         tf('Mehrobdan chayon sold more copies than Days Gone By in the 1920s.', 'NG',
            'Ikkinchi roman mavzusi va uslubi tasvirlangan, ammo sotuv yoki tiraj haqida maʼlumot yoʻq.', 4),
         tf('Qodiriy was officially rehabilitated while Stalin was still alive.', 'F',
            '«Only after Stalin\'s death was he officially rehabilitated» — Stalin vafotidan keyin.', 5, ng=True),
         ch('What is the writer\'s main purpose in the final sentence of paragraph A?',
            ['to suggest that Days Gone By has been overrated',
             'to indicate that Qodiriy\'s importance goes beyond one famous novel',
             'to explain why Qodiriy wrote so little',
             'to compare Qodiriy with writers from other countries'], 1,
            '«to treat him simply as the author of one celebrated work would be to underestimate both the range of his writing and the extent of his influence» — matn uning boshqa asarlari va taʼsirini ham koʻrib chiqadi.', 0),
         ch('According to paragraph D, what most distinguished Qodiriy\'s novel from earlier prose?',
            ['its unusually dramatic and complicated plot',
             'its use of the elevated vocabulary of classical literature',
             'its psychologically convincing characters and use of everyday speech',
             'its clear moral lessons for young readers'], 2,
            '«characters with recognisable inner lives» va «drew extensively on the spoken Uzbek of his time». Klassik leksika — aksincha, undan voz kechgan; syujet esa «less its plot than its manner».', 3),
         ch('According to the writer, what does the title Mehrobdan chayon point to?',
            ['the danger of foreign invasion',
             'dishonesty hidden behind religious and political respectability',
             'the cruelty of family conventions',
             'the decline of trade in the Kokand Khanate'], 1,
            '«hypocrisy concealed behind a façade of piety and authority» — «hypocrisy» = dishonesty, «piety and authority» = religious and political respectability.', 4),
         ch('What does the writer consider the strongest evidence of Qodiriy\'s achievement?',
            ['the adaptation of his novel for stage and screen',
             'the number of later novelists who imitated him',
             'the fact that readers still find his work personally relevant',
             'the inclusion of his books in school programmes'], 2,
            '«Perhaps the most telling measure of his achievement … is that readers continue to approach his work … as living literature». Boshqa variantlar tilga olingan, lekin «eng muhim oʻlchov» sifatida emas.', 6),
         gap('Before he became a novelist, Qodiriy was known for ___ that mocked the pretensions of officials.',
             'satirical sketches', '«he became known for satirical sketches in which the pretensions of officials … were exposed».', 1, 2),
         gap('Instead of classical vocabulary, Qodiriy drew on the ___ of his time.', 'spoken Uzbek',
             '«he drew extensively on the spoken Uzbek of his time».', 3, 2),
         gap('In the novel, ___ within Otabek\'s household finally results in tragedy.', 'jealousy',
             '«a household where jealousy eventually leads to tragedy» — «results in» = «leads to».', 2, 2),
     ])


# ---------------------------------------------------------------- 22: Tarjima sanʼati
text(B, 'c1-22-translation', 'Tarjima sanʼati', 'The Art of Translation', 'C1', 'exam',
     L('Til va adabiyot', 'Language and literature'),
     'Fikr-mulohaza (opinion) matni: tarjimonlik sanʼati, aniqlik va ravonlik, «tarjima qilib boʻlmaydigan» soʻzlar, '
     'sheʼr va hazil tarjimasi. Bu matnda T/F/NG savollari YES / NO / NOT GIVEN maʼnosida: T = muallif shunday fikrda, '
     'F = muallif buning aksini aytadi, NG = muallifning fikri berilmagan. Taxminan 20 daqiqa: muallif oʻz fikrini '
     'bildiradigan joylarni («In my view», «I find», «I suspect») belgilab oling — YES/NO savollarining kaliti shu yerda.',
     [
         P("Translators are fond of describing their work as building bridges between cultures, and the metaphor is an "
           "attractive one. It suggests a solid structure across which meaning passes intact from one bank to the other. "
           "Yet anyone who has attempted to translate a demanding text knows that the reality is rather less tidy. Meaning "
           "does not simply cross over; it has to be reconstructed, and at every stage the translator must make choices "
           "that no dictionary can make for them. An old Italian pun equates the translator with a traitor, and while the "
           "charge is unfair, it captures an uncomfortable truth: every translation involves some loss, and the question "
           "is never whether to sacrifice something but what."),
         P("The oldest debate in the field concerns the competing demands of fidelity and fluency. Since antiquity, "
           "commentators have argued over whether a translator should follow the original word for word or render its "
           "sense in whatever form sounds most natural in the target language. A strictly literal version may preserve "
           "the structure of the source but often reads awkwardly, while a highly fluent one may read beautifully yet "
           "quietly erase everything that made the original distinctive. In my view, neither extreme deserves to be "
           "treated as a virtue. A good translation should read as though it had been written with care in its new "
           "language, while still allowing the reader to sense that it came from somewhere else."),
         P("Much is made of so-called untranslatable words, and lists of them circulate widely as evidence that some "
           "ideas exist in one language alone. Consider the Uzbek word hashar, which refers to the custom of neighbours "
           "gathering voluntarily to help with a shared task such as building a house or cleaning a street. English can "
           "offer community work or voluntary labour, but neither phrase conveys the sense of reciprocity and celebration "
           "that usually accompanies the practice. Nevertheless, it would be misleading to conclude that such words "
           "cannot be translated at all. Their meaning can almost always be explained; what is lost is the economy with "
           "which a single word carries an entire cluster of associations."),
         P("Poetry presents these difficulties in their most acute form, because in verse the sound of a line is "
           "inseparable from its sense. Classical Uzbek poetry, much of it composed in the quantitative metre known as "
           "aruz, relies on patterns of long and short syllables that English, with its stress-based rhythms, cannot "
           "reproduce. A translator must therefore decide whether to imitate the rhyme scheme at the cost of accuracy, "
           "abandon form in favour of meaning, or seek some compromise between the two. Each option produces a different "
           "poem, and readers who know only one version should remember that they are encountering an interpretation "
           "rather than the original itself."),
         P("Humour is perhaps even more treacherous. Jokes that depend on wordplay rarely survive the journey intact, "
           "since a pun is by definition tied to the accidents of a particular language. Humour that arises from "
           "situations, by contrast, often travels surprisingly well. The anecdotes about Afandi, the folk trickster "
           "familiar across much of the Turkic and Persian-speaking world, tend to work in English precisely because their "
           "comedy lies in the logic of the situation rather than in the words. Where a joke relies on shared cultural "
           "knowledge, however, the translator faces an unenviable choice between adding an explanation, which kills the "
           "joke, and substituting a local equivalent, which changes it."),
         P("Despite the decisive role they play, translators have traditionally been expected to remain unseen. Their "
           "names are frequently omitted from book covers, and reviewers often praise a novel's style without "
           "acknowledging that the sentences they admire were written by someone other than the author. One scholar has "
           "memorably described this situation as the translator's invisibility, arguing that the ideal of a perfectly "
           "smooth translation conceals the labour behind it. I find this argument persuasive. Readers would arguably be "
           "better served if translators were credited prominently and allowed to explain, in a preface or afterword, the "
           "principles that guided their decisions."),
         P("None of this is cause for despair. Translation is imperfect in the same way that all reading is imperfect: "
           "every reader brings their own experience to a text and takes away something slightly different. Far from "
           "being a regrettable necessity, translation is one of the main ways in which literatures renew themselves, "
           "since encounters with foreign works have repeatedly introduced new forms and ideas into national traditions. "
           "Machine translation may increasingly handle routine documents, but rendering a novel or a poem will, I "
           "suspect, continue to require human judgement for some time to come."),
     ],
     [G('intact', 'butunligicha, shikastlanmagan'), G('reconstruct', 'qayta qurmoq, qayta tiklamoq'),
      G('equate with', '… bilan tenglashtirmoq'), G('fidelity', 'asliyatga sodiqlik'),
      G('fluency', 'ravonlik'), G('render', 'ifodalamoq, tarjima qilmoq'),
      G('erase', 'oʻchirib tashlamoq'), G('distinctive', 'oʻziga xos'),
      G('reciprocity', 'oʻzaro yordam, bir-biriga javob qaytarish'), G('cluster of associations', 'bir toʻda maʼno-bogʻlanishlar'),
      G('acute', 'keskin, oʻtkir'), G('inseparable from', '… dan ajralmas'),
      G('treacherous', 'xavfli, aldamchi'), G('unenviable', 'havas qilib boʻlmaydigan, ogʻir'),
      G('omit', 'tushirib qoldirmoq'), G('acknowledge', 'tan olmoq, eʼtirof etmoq'),
      G('prominently', 'koʻzga tashlanadigan qilib'), G('regrettable', 'afsuslanarli')],
     [GN('c46-contrast-concession', 'Toʻsiqsiz ergash gap: while … (garchi … boʻlsa-da)',
         'while the charge is unfair, it captures an uncomfortable truth'),
      GN('c38-ellipsis', 'Ellipsis: takrorni tushirib qoldirish (… but what)',
         'the question is never whether to sacrifice something but what')],
     [
         tf('The writer believes the image of a bridge accurately reflects what translators do.', 'F',
            'NO: «the reality is rather less tidy. Meaning does not simply cross over; it has to be reconstructed» — muallif metaforani yetarli deb hisoblamaydi.', 0, ng=True),
         tf('The writer accepts that some loss is unavoidable in any translation.', 'T',
            'YES: «every translation involves some loss» — muallif buni «uncomfortable truth» deb tan oladi.', 0, ng=True),
         tf('According to the writer, a good translation should hide every trace of its foreign origin.', 'F',
            'NO: «while still allowing the reader to sense that it came from somewhere else» — begonalikni butunlay yashirmaslik kerak.', 1, ng=True),
         tf('The writer thinks that most lists of untranslatable words are compiled by professional translators.', 'NG',
            'NOT GIVEN: roʻyxatlar keng tarqalgani aytilgan, lekin ularni kim tuzishi haqida muallif fikri yoʻq.', 2),
         tf('The writer considers humour based on situations easier to translate than humour based on wordplay.', 'T',
            'YES: wordplay «rarely survive the journey intact», situational humour esa «often travels surprisingly well».', 4, ng=True),
         tf('The writer argues that translators of literature should be paid more than they currently are.', 'NG',
            'NOT GIVEN: muallif tarjimonlar nomi koʻrsatilishi va soʻzboshi yozishini taklif qiladi, ammo haq toʻlash haqida gapirmaydi.', 5),
         tf('The writer is confident that machines will soon translate novels as well as humans do.', 'F',
            'NO: «rendering a novel or a poem will, I suspect, continue to require human judgement for some time to come».', 6, ng=True),
         ch('What is the writer\'s main point about the word hashar?',
            ['It has no meaning that an English speaker could understand.',
             'Its meaning can be explained, but not as concisely as in Uzbek.',
             'It proves that Uzbek is richer in vocabulary than English.',
             'Translators should always leave it in its original form.'], 1,
            '«Their meaning can almost always be explained; what is lost is the economy with which a single word carries an entire cluster of associations» — «economy» = qisqalik, ixchamlik.', 2),
         ch('Why does the writer mention the metre known as aruz?',
            ['to show that classical Uzbek poetry has no rhyme',
             'to give an example of a formal feature that English cannot reproduce',
             'to argue that poetry should be translated as prose',
             'to explain why Uzbek readers prefer classical poetry'], 1,
            '«relies on patterns of long and short syllables that English, with its stress-based rhythms, cannot reproduce» — sheʼriy shakl tarjimada saqlanmasligiga misol.', 3),
         ch('In paragraph E, what does the phrase "which kills the joke" refer to?',
            ['adding an explanation', 'substituting a local equivalent',
             'relying on wordplay', 'shared cultural knowledge'], 0,
            '«adding an explanation, which kills the joke» — «which» oʻzidan oldingi iboraga ishora qiladi. Mahalliy muqobil esa hazilni «changes», yaʼni oʻzgartiradi.', 4),
         ch('What does the writer recommend in paragraph F?',
            ['Reviewers should stop commenting on the style of translated novels.',
             'Translations should be as smooth as possible so that readers forget the translator.',
             'Translators should be given visible credit and a chance to explain their approach.',
             'Publishers should print the original text alongside the translation.'], 2,
            '«translators were credited prominently and allowed to explain, in a preface or afterword, the principles that guided their decisions».', 5),
         gap('A strictly literal translation may keep the structure of the source but often reads ___.', 'awkwardly',
             '«A strictly literal version may preserve the structure of the source but often reads awkwardly».', 1, 2),
         gap('English phrases such as community work fail to convey the sense of ___ and celebration that hashar involves.',
             'reciprocity', '«neither phrase conveys the sense of reciprocity and celebration».', 2, 2),
         gap('One scholar has called the hidden position of translators the translator\'s ___.', 'invisibility',
             '«One scholar has memorably described this situation as the translator\'s invisibility».', 5, 2),
     ])


# ---------------------------------------------------------------- 23: Ertaklar
H3 = ['Why written collections replaced storytellers', 'Cleverness prized alongside virtue',
      'Lessons about society that go unspoken', 'A wise fool who deflates the powerful',
      'Proof that tales reduce childhood anxiety', 'Facing danger from a position of safety',
      'Familiar figures of a regional tradition', 'A story that changes with every telling',
      'Reasons for an enduring appeal']

text(B, 'c1-23-fairy-tales', 'Ertaklar nimani oʻrgatadi', 'What Fairy Tales Teach', 'C1', 'exam',
     L('Folklor', 'Folklore'),
     'Akademik matn: xalq ertaklarining vazifalari, ogʻzaki anʼana va Markaziy Osiyo ertaklari. Asosiy topshiriq — '
     'Matching headings: B–H xatboshilari uchun 9 ta sarlavhadan mosini tanlang (2 tasi ortiqcha; A xatboshisi uchun savol yoʻq). '
     'Taxminan 20 daqiqa: har bir xatboshining birinchi va oxirgi gapini diqqat bilan oʻqing, asosiy gʻoyani '
     'oʻz soʻzingiz bilan ifodalang, soʻngra sarlavhani tanlang. Matndagi soʻz bilan bir xil soʻz qatnashgan sarlavha '
     'koʻpincha tuzoq boʻladi.',
     [
         P("Folk tales are often dismissed as entertainment for small children, stories to be told at bedtime and "
           "forgotten by adolescence. Folklorists, anthropologists and psychologists have long taken a different view. "
           "For them, the tales that communities pass down across generations constitute a remarkably rich archive of "
           "collective experience, recording what societies feared, valued and hoped for. To ask what fairy tales teach is "
           "therefore to ask how cultures have educated their young before, and alongside, any formal system of "
           "schooling."),
         P("The most obvious function of such stories is moral instruction. Kindness is rewarded and cruelty punished; "
           "the generous hero receives help from unexpected quarters, while the greedy brother returns home empty-handed. "
           "A well-known Uzbek tale contrasts a hardworking girl with her idle stepsister, and the fortune of each mirrors "
           "the way she has behaved. Yet the moral universe of folk tales is less straightforward than this suggests. "
           "Tricksters frequently prosper through deception, and cunning is celebrated at least as often as honesty. What "
           "the tales seem to value above all is resourcefulness, the capacity to survive in a world that is rarely fair."),
         P("A second function concerns fear. Fairy tales are full of menace: giants and monsters, wicked stepmothers, "
           "dark forests and abandoned children. It might seem strange to expose young listeners to such material, but one "
           "influential line of thought holds that this is precisely the point. By presenting terrifying situations within "
           "a reassuring framework, in which the danger is eventually overcome, tales may allow children to confront their "
           "anxieties at a safe distance. Critics have objected that this argument is difficult to test and has sometimes "
           "been overstated, yet the observation that children often request the most frightening stories again and again "
           "lends it a certain plausibility."),
         P("Tales also transmit social norms, frequently in ways their tellers would not have articulated. Stories "
           "reinforce expectations about hospitality, obedience to parents and respect for elders, and they often reflect "
           "assumptions about the roles considered appropriate for men and women. In this respect they are not neutral. A "
           "tale in which the heroine's only reward is marriage to a prince carries an implicit message about what a "
           "girl's life should aim at. It is partly for this reason that many contemporary writers have produced revised "
           "versions in which familiar plots are reworked to reflect different values."),
         P("Crucially, folk tales were for most of their history oral rather than written, and this shaped them "
           "profoundly. A storyteller would adapt a tale to the audience in front of them, lengthening a passage that drew "
           "laughter, omitting an episode unsuitable for the occasion, or substituting local landmarks for distant ones. "
           "As a result, there is rarely a single authentic version of any tale. Folklorists have compiled extensive "
           "catalogues of tale types, demonstrating that remarkably similar plots appear in regions separated by thousands "
           "of kilometres. Whether such similarities reflect migration, trade or simply common human concerns remains a "
           "subject of debate."),
         P("The tales of Central Asia display many features found elsewhere, alongside elements distinctly their own. "
           "Devs, monstrous beings of enormous strength, threaten heroes, while peris, beautiful supernatural figures, may "
           "help or hinder them. The youngest of three brothers, dismissed by his elders as foolish, often proves the most "
           "capable. Animals speak, horses carry their riders across impossible distances, and journeys frequently involve "
           "tests of patience and loyalty. Traditionally, such tales were told during long winter evenings, when families "
           "gathered and skilled storytellers could hold an audience for hours."),
         P("No figure in the region's humorous tradition is better known than Afandi, the character known in other "
           "countries as Nasreddin Hodja. Anecdotes about him circulate from Turkey and the Balkans to Central Asia and "
           "beyond, and several places claim him as their own. In Uzbek tradition he is often associated with Bukhara. "
           "Afandi is at once fool and sage: he may ride his donkey backwards or appear to misunderstand a simple question, "
           "yet his apparent foolishness repeatedly exposes the vanity of rulers, the greed of judges and the pomposity of "
           "the learned. His stories teach, in short, that wisdom does not always look the way authority expects."),
         P("Why, then, do such tales endure in an age of screens and streaming? Part of the answer may lie in their "
           "flexibility. Because they were never fixed, they lend themselves to endless retelling in new media, from "
           "animated films to picture books. More fundamentally, the questions they address, how to behave, how to face "
           "danger and how to find one's place among others, have not been resolved by technological change. As long as "
           "those questions remain, it seems likely that people will continue to answer them, at least in part, through "
           "stories."),
     ],
     [G('dismiss as', '… deb eʼtiborsiz qoldirmoq'), G('constitute', 'tashkil etmoq, … boʻlmoq'),
      G('archive', 'arxiv, xazina'), G('from unexpected quarters', 'kutilmagan tomondan'),
      G('prosper', 'gullab-yashnamoq, muvaffaqiyat qozonmoq'), G('cunning', 'ayyorlik, makr'),
      G('resourcefulness', 'topqirlik, uddaburonlik'), G('menace', 'xavf, tahdid'),
      G('plausibility', 'ishonarlilik, haqiqatga yaqinlik'), G('articulate', 'aniq ifodalamoq'),
      G('implicit', 'yashirin, bilvosita'), G('profoundly', 'chuqur, tubdan'),
      G('authentic', 'asl, haqiqiy'), G('hinder', 'toʻsqinlik qilmoq'),
      G('sage', 'donishmand'), G('vanity', 'kibr, shuhratparastlik'),
      G('pomposity', 'dimogʻdorlik, oʻzini katta tutish'), G('endure', 'saqlanib qolmoq, yashab qolmoq')],
     [GN('c34-participle-clauses', 'Sifatdosh oborot (-ed): dismissed by his elders as foolish',
         'The youngest of three brothers, dismissed by his elders as foolish, often proves the most capable'),
      GN('c33-relative-advanced', 'Predlogli nisbiy gap: in which',
         'within a reassuring framework, in which the danger is eventually overcome')],
     [
         hd(1, H3, 1, 'Xatboshi B: ertaklar yaxshilikni mukofotlaydi, lekin «cunning is celebrated at least as often as honesty» — '
                      'ayyorlik/topqirlik ezgulik bilan teng qadrlanadi.'),
         hd(2, H3, 5, 'Xatboshi C: qoʻrqinchli voqealar «within a reassuring framework» beriladi — bola xavfga «at a safe distance» duch keladi. '
                      '«Proof that tales reduce childhood anxiety» — tuzoq: matnda bu gʻoyani «difficult to test» deyilgan, isbot yoʻq.'),
         hd(3, H3, 2, 'Xatboshi D: ertaklar ijtimoiy meʼyorlarni «in ways their tellers would not have articulated» — ochiq aytilmagan holda yetkazadi; «implicit message».'),
         hd(4, H3, 7, 'Xatboshi E: ertakchi har safar ertakni tinglovchiga moslab oʻzgartirgan — «there is rarely a single authentic version». '
                      '«Why written collections replaced storytellers» — tuzoq: yozma toʻplamlar haqida gap yoʻq.'),
         hd(5, H3, 6, 'Xatboshi F: Markaziy Osiyo ertaklarining tanish qahramonlari — devlar, parilar, kenja aka-uka, gapiradigan hayvonlar.'),
         hd(6, H3, 3, 'Xatboshi G: Afandi — «at once fool and sage», hukmdorlar, qozilar va olimlarning kibrini fosh qiladi.'),
         hd(7, H3, 8, 'Xatboshi H: «Why, then, do such tales endure …?» — moslashuvchanlik va abadiy savollar ertaklarning uzoq yashashiga sabab.'),
         tf('According to the writer, folk tales consistently reward honesty rather than cunning.', 'F',
            '«Tricksters frequently prosper through deception, and cunning is celebrated at least as often as honesty» — doimo halollik ustun emas.', 1, ng=True),
         tf('Children tend to avoid frightening stories once they have heard them.', 'F',
            '«children often request the most frightening stories again and again» — aksincha, qayta-qayta soʻraydi.', 2, ng=True),
         tf('Most Afandi anecdotes were first written down in Bukhara.', 'NG',
            'Afandi oʻzbek anʼanasida Buxoro bilan bogʻlanishi aytilgan, lekin latifalar qayerda birinchi yozib olingani haqida maʼlumot yoʻq.', 6),
         ch('What does the writer suggest about tales in which the heroine is rewarded only with marriage?',
            ['They were invented by contemporary writers.',
             'They quietly promote a particular view of what girls should aspire to.',
             'They are the most popular type of tale among children.',
             'They show that folk tales are morally neutral.'], 1,
            '«carries an implicit message about what a girl\'s life should aim at»; «In this respect they are not neutral» — shuning uchun D variant notoʻgʻri.', 3),
         ch('According to paragraph E, why is there rarely a single authentic version of a tale?',
            ['because folklorists have changed the tales when cataloguing them',
             'because tellers adapted each tale to their listeners and circumstances',
             'because tales were translated many times as they travelled',
             'because similar plots were invented independently in different regions'], 1,
            '«A storyteller would adapt a tale to the audience … As a result, there is rarely a single authentic version» — «As a result» sababni koʻrsatadi.', 4),
         gap('Folklorists\' catalogues show that similar plots appear in regions separated by thousands of ___.',
             ['kilometres', 'kilometers'],
             '«remarkably similar plots appear in regions separated by thousands of kilometres».', 4, 2),
     ])


# ---------------------------------------------------------------- 24: Mirzo Bobur
text(B, 'c1-24-babur', 'Mirzo Bobur', 'Babur: Conqueror and Memoirist', 'C1', 'exam',
     L('Tarix va adabiyot', 'History and literature'),
     'Biografik matn: Zahiriddin Muhammad Bobur — hukmdor, «Boburnoma» muallifi va shoir. Topshiriqlar: True/False/Not Given, '
     'test savollari (ishora, maqsad, xulosa) va gap toʻldirish (NO MORE THAN TWO WORDS). Taxminan 20 daqiqa: sanalar va '
     'joy nomlarini (Andijon, Samarqand, Kobul, Panipat, Agra) matnda belgilab oling — savollarning koʻpi aynan shu '
     'tayanch nuqtalar atrofida tuzilgan.',
     [
         P("Many rulers have founded empires, and a good number have commissioned flattering chronicles of their deeds. "
           "Rarely, however, has a ruler left behind a personal account as candid as the one written by Zahiriddin "
           "Muhammad Babur, the prince from the Fergana Valley who became the founder of the Mughal dynasty in India. His "
           "life story is remarkable in itself, a sequence of reversals in which kingdoms were won and lost with "
           "bewildering speed. What has secured his lasting reputation, though, is not only what he did but the way he "
           "wrote about it."),
         P("Babur was born in Andijan in 1483, the son of Umar Shaikh Mirza, who ruled the small principality of Fergana. "
           "Through his father he was descended from Amir Temur, and through his mother from Genghis Khan, a double lineage "
           "that conferred enormous prestige but also fuelled ambitions that his modest territory could hardly sustain. "
           "When his father died in an accident in 1494, Babur inherited the throne while still a boy of about eleven, "
           "surrounded by relatives and advisers whose loyalty could not be taken for granted."),
         P("The years that followed were dominated by a struggle for Samarkand, the former capital of Temur, whose "
           "possession represented for any Timurid prince the ultimate symbol of legitimacy. Babur captured the city more "
           "than once, yet on each occasion he proved unable to hold it. The decisive challenge came from Muhammad Shaybani "
           "Khan, whose forces were consolidating their power across the region. Driven out of Samarkand and eventually "
           "deprived of Fergana as well, Babur spent a period as a ruler without a realm, moving from place to place with a "
           "dwindling band of followers."),
         P("His fortunes changed in 1504, when he seized Kabul. The city gave him a secure base, and for two decades he "
           "ruled there, all the while looking for an opportunity to restore his position in Central Asia. A final attempt "
           "to retake Samarkand, made with the support of the Safavid Shah of Iran, briefly succeeded but ended in failure. "
           "Gradually, Babur's attention turned south-east, towards the wealthy lands of northern India, into which he led "
           "a series of expeditions."),
         P("In 1526, at Panipat, north of Delhi, his army confronted the forces of Ibrahim Lodi, the Sultan of Delhi, an "
           "army generally believed to have been far larger than his own. Babur's victory is often attributed to his "
           "skilful use of field fortifications and gunpowder weapons, which were still relatively uncommon on Indian "
           "battlefields. The battle laid the foundation of what became known as the Mughal Empire. Babur himself did not "
           "live long enough to consolidate it: he died in Agra in 1530, and his remains were later taken to Kabul, in "
           "keeping with his wishes. His descendants, however, would rule much of the subcontinent for generations, "
           "presiding over a culture of extraordinary richness."),
         P("It is the Boburnoma, known in English as the Baburnama, that gives Babur a place in literary as well as "
           "political history. Written in Chagatai Turkic, the literary language of the Timurid world, the memoir records "
           "his campaigns, but it does so with a frankness that is rare in royal writing. Babur admits defeats, errors of "
           "judgement and moments of despair, and he comments shrewdly, and sometimes harshly, on the character of allies "
           "and enemies alike. Equally striking is his curiosity. He describes the landscapes, fruits, birds and customs of "
           "Fergana, Kabul and India with the eye of a naturalist, and he is not above complaining that his new Indian "
           "domains lacked the melons and grapes of his homeland. The work was later translated into Persian at the court "
           "of his grandson Akbar, which helped it reach a wider audience."),
         P("Babur was also an accomplished poet. He composed ghazals and rubais in Turkic, and he is often ranked among the "
           "most significant poets to have written in Chagatai after Alisher Navoi. Many of his verses express longing for "
           "the homeland he had been forced to leave, a theme that lends them particular resonance for readers in "
           "Uzbekistan today. Soldier, ruler, memoirist and poet, Babur defies easy categorisation, and it is perhaps this "
           "very complexity that continues to draw readers to his work five centuries after it was written."),
     ],
     [G('commission', 'buyurtma bermoq'), G('flattering', 'xushomadgoʻy, maqtovli'),
      G('candid', 'ochiq-oydin, samimiy'), G('reversal', 'keskin burilish, omadsizlik'),
      G('bewildering', 'hayratlanarli, aqlni shoshiradigan'), G('principality', 'kichik davlat, beklik'),
      G('lineage', 'nasl-nasab'), G('confer prestige', 'obroʻ bagʻishlamoq'),
      G('legitimacy', 'qonuniylik, hokimiyat huquqi'), G('deprive of', '… dan mahrum qilmoq'),
      G('realm', 'saltanat, mamlakat'), G('dwindling', 'kamayib borayotgan'),
      G('attribute to', '… ga nisbat bermoq, … bilan izohlamoq'), G('in keeping with', '… ga muvofiq'),
      G('frankness', 'ochiqlik, toʻgʻrisoʻzlik'), G('shrewdly', 'zukkolik bilan, oʻtkir nigoh bilan'),
      G('resonance', 'aks-sado, taʼsirchanlik'), G('defies categorisation', 'biror toifaga sigʻmaydi')],
     [GN('c58-inversion', 'Inversiya: Rarely has a ruler …',
         'Rarely, however, has a ruler left behind a personal account as candid as the one written by Zahiriddin Muhammad Babur'),
      GN('c34-participle-clauses', 'Sifatdosh oborot: Driven out of …, Babur spent …',
         'Driven out of Samarkand and eventually deprived of Fergana as well, Babur spent a period as a ruler without a realm')],
     [
         tf('Babur\'s family background gave him prestige but also encouraged ambitions beyond his resources.', 'T',
            '«a double lineage that conferred enormous prestige but also fuelled ambitions that his modest territory could hardly sustain» — paraphrase.', 1, ng=True),
         tf('Babur became ruler of Fergana as an adult.', 'F',
            '«Babur inherited the throne while still a boy of about eleven».', 1, ng=True),
         tf('Babur\'s final attempt on Samarkand, made with Safavid support, achieved no success at all.', 'F',
            '«briefly succeeded but ended in failure» — qisqa muddat muvaffaqiyat boʻlgan, demak «no success at all» notoʻgʻri.', 3, ng=True),
         tf('Babur was buried permanently in Agra, where he died.', 'F',
            '«he died in Agra in 1530, and his remains were later taken to Kabul, in keeping with his wishes».', 4, ng=True),
         tf('The Persian translation of the memoir was produced during Babur\'s lifetime.', 'F',
            '«later translated into Persian at the court of his grandson Akbar» — nabirasi davrida, Bobur vafotidan keyin.', 5, ng=True),
         tf('Babur learned to write poetry from a famous poet at his father\'s court.', 'NG',
            'G xatboshida Bobur shoir boʻlgani va Navoiydan keyingi yirik shoirlar qatorida turishi aytilgan, ammo kimdan oʻrgangani haqida maʼlumot yoʻq.', 6),
         ch('In paragraph A, the writer suggests that Babur\'s lasting reputation depends mainly on',
            ['the size of the empire he founded',
             'the flattering chronicles written about him',
             'both his achievements and the way he recorded them',
             'the speed with which he won his kingdoms'], 2,
            '«What has secured his lasting reputation … is not only what he did but the way he wrote about it».', 0),
         ch('In paragraph B, the phrase "a double lineage" refers to Babur\'s descent from',
            ['Umar Shaikh Mirza and the rulers of Fergana', 'Amir Temur and Genghis Khan',
             'two branches of the Timurid family in Samarkand', 'his father and his advisers'], 1,
            '«Through his father he was descended from Amir Temur, and through his mother from Genghis Khan, a double lineage …» — ikki tomonlama nasab.', 1),
         ch('Why was Samarkand so important to Babur?',
            ['It was the richest trading city in the region.',
             'Controlling it confirmed a Timurid prince\'s right to rule.',
             'It was the city where he had been born.',
             'It provided a safe base for his expeditions to India.'], 1,
            '«whose possession represented for any Timurid prince the ultimate symbol of legitimacy» — «legitimacy» = hokimiyatga qonuniy huquq. Tugʻilgan joyi — Andijon; xavfsiz baza — Kobul.', 2),
         ch('Why does the writer mention Babur\'s complaint about melons and grapes?',
            ['to show that Indian agriculture was poorly developed',
             'to illustrate the personal and unguarded tone of his observations',
             'to explain why he decided to return to Kabul',
             'to criticise his attitude towards the people of India'], 1,
            'Bu misol «frankness» va «curiosity» haqidagi fikrni tasdiqlaydi; «he is not above complaining» — u hatto mayda shaxsiy noroziliklarini ham yashirmaydi.', 5),
         gap('After 1504, Kabul provided Babur with a secure ___.', 'base',
             '«The city gave him a secure base».', 3, 2),
         gap('At Panipat, Babur made skilful use of field fortifications and ___ weapons.', 'gunpowder',
             '«his skilful use of field fortifications and gunpowder weapons».', 4, 2),
         gap('The Boburnoma was written in ___, the literary language of the Timurid world.', ['Chagatai Turkic', 'Chagatai'],
             '«Written in Chagatai Turkic, the literary language of the Timurid world».', 5, 2),
         gap('Many of Babur\'s poems express ___ for the homeland he had lost.', 'longing',
             '«Many of his verses express longing for the homeland he had been forced to leave».', 6, 2),
     ])


# ---------------------------------------------------------------- 25: Kitobxonlik tarixi
text(B, 'c1-25-history-reading', 'Kitobxonlik tarixi', 'A Short History of Reading', 'C1', 'exam',
     L('Madaniyat tarixi', 'Cultural history'),
     'Akademik matn: ovoz chiqarib oʻqishdan ichida oʻqishgacha, kitob bosish, ommaviy savodxonlik va ekrandan oʻqish. '
     'Asosiy topshiriq — Summary completion (NO MORE THAN TWO WORDS): xulosadagi boʻshliqlarni matndagi soʻzlar bilan aynan '
     'toʻldiring. Taxminan 20 daqiqa: avval xulosani oʻqib, har bir boʻshliqqa qanday soʻz turkumi (ot, sifat) kerakligini '
     'aniqlang, soʻngra matnda sinonim va parafrazlarni qidiring — xulosa gaplari matn tartibida keladi.',
     [
         P("Reading is so deeply embedded in modern life that it is easy to assume it has always been practised in much "
           "the same way. Historians of the book have shown, however, that the act itself has undergone a series of "
           "profound transformations. Who read, what they read, how they held and handled texts, and even whether they read "
           "aloud or in silence have all varied considerably across time and place. Recognising these changes can help to "
           "place current anxieties about reading in a longer perspective."),
         P("For much of antiquity, reading appears to have been a predominantly oral activity. Greek and Latin texts were "
           "often written without spaces between words, a practice that made it difficult to decipher a line without "
           "sounding it out. Reading was also frequently social: a literate person might read to a household, and wealthy "
           "Romans sometimes employed slaves to read aloud to them. Scholars have cautioned against exaggerating this "
           "picture, since there is evidence that silent reading was not unknown in the ancient world. Nevertheless, the "
           "voice seems to have been far more central to the experience of a text than it is for most readers today."),
         P("A frequently cited passage in the Confessions of Augustine, written around the end of the fourth century, "
           "records his surprise at observing Ambrose, the bishop of Milan, reading with his eyes moving over the page while "
           "his voice remained silent. Whether this reaction reflects genuine rarity or merely Augustine's interest in the "
           "bishop's personal habits is disputed. What is clearer is that, over the course of the Middle Ages, scribes "
           "increasingly separated words and introduced punctuation, changes that are thought to have made silent reading "
           "easier. Private reading, in turn, opened the way for more personal and reflective engagement with texts."),
         P("The introduction of printing with movable type in Europe in the mid-fifteenth century, associated above all "
           "with Johannes Gutenberg in Mainz, transformed the economics of the written word, although similar techniques "
           "had been developed considerably earlier in East Asia. Books that had once been copied laboriously by hand could "
           "now be produced in hundreds of identical copies, and prices gradually fell. Printing also encouraged the "
           "standardisation of spelling and texts, since large numbers of readers could now consult exactly the same "
           "edition. It would be wrong, however, to imagine that printing immediately created a mass reading public; for "
           "several centuries, literacy remained confined largely to a minority."),
         P("Mass literacy is, in most societies, a relatively recent achievement. In parts of Europe and North America, "
           "the nineteenth century brought compulsory schooling, cheap newspapers and public libraries, and by the early "
           "twentieth century the ability to read had become an expectation rather than a privilege in many countries. "
           "This expansion was not universally welcomed. Already in the eighteenth century, some commentators had warned of "
           "a reading mania, fearing that novels would overheat the imagination of young readers, particularly women, and "
           "distract them from their duties. Such warnings now seem quaint, but they reveal a recurring pattern in which new "
           "forms of reading provoke moral concern."),
         P("The latest transformation is the move to screens. Reading online tends to be fragmented: readers skim, follow "
           "links and switch between texts, often while receiving notifications. A number of studies comparing "
           "comprehension on paper and on screen have found a modest advantage for paper, particularly for long or complex "
           "texts, though the results are not entirely consistent and may change as readers grow more accustomed to digital "
           "formats. Some researchers have suggested that the habit of skimming may gradually erode the capacity for "
           "sustained, deep reading, while others argue that readers can learn to switch deliberately between modes."),
         P("Seen in historical perspective, the present moment is less unprecedented than it may appear. Each major shift, "
           "from voice to silence, from manuscript to print and from elite to mass readership, prompted fears that something "
           "valuable was being lost, and each was accompanied by real gains as well as real costs. The lesson is perhaps not "
           "that worries about screens are misplaced, but that the kind of reading a society values must be deliberately "
           "cultivated rather than taken for granted."),
     ],
     [G('embedded', 'singib ketgan, chuqur oʻrnashgan'), G('undergo', 'boshdan kechirmoq'),
      G('predominantly', 'asosan, koʻproq'), G('decipher', 'oʻqib tushunmoq, sirini ochmoq'),
      G('caution against', '… dan ogohlantirmoq'), G('scribe', 'kotib, xattot-koʻchiruvchi'),
      G('engagement with', '… bilan chuqur ishlash, muloqot'), G('movable type', 'koʻchma harf (bosmaxonada)'),
      G('laboriously', 'mashaqqat bilan'), G('standardisation', 'bir xillashtirish, standartlashtirish'),
      G('confined to', '… bilan cheklangan'), G('compulsory', 'majburiy'),
      G('quaint', 'gʻalati-eskicha, kulgili koʻrinadigan'), G('fragmented', 'parchalangan, uzuq-yuluq'),
      G('skim', 'koʻz yugurtirib oʻqimoq'), G('erode', 'asta-sekin yemirmoq'),
      G('unprecedented', 'misli koʻrilmagan'), G('cultivate', 'tarbiyalamoq, rivojlantirmoq')],
     [GN('c14-complex-passive', 'Murakkab majhul nisbat: are thought to have made',
         'changes that are thought to have made silent reading easier'),
      GN('c60-nominalisation', 'Nominalizatsiya: The introduction of printing …',
         'The introduction of printing with movable type in Europe in the mid-fifteenth century')],
     [
         gap('Summary: In antiquity, Greek and Latin texts were often written without ___ between words, which made reading aloud almost necessary.',
             'spaces', '«often written without spaces between words, a practice that made it difficult to decipher a line without sounding it out».', 1, 2),
         gap('Summary: Reading was often a social activity, and wealthy Romans sometimes had ___ read to them.',
             'slaves', '«wealthy Romans sometimes employed slaves to read aloud to them».', 1, 2),
         gap('Summary: During the Middle Ages, scribes separated words and added ___, which probably made silent reading easier.',
             'punctuation', '«scribes increasingly separated words and introduced punctuation» — «added» = «introduced».', 2, 2),
         gap('Summary: Printing reduced the price of books and encouraged the ___ of spelling and texts.',
             ['standardisation', 'standardization'],
             '«Printing also encouraged the standardisation of spelling and texts».', 3, 2),
         gap('Summary: In the nineteenth century, compulsory schooling, cheap newspapers and ___ helped to spread literacy.',
             'public libraries', '«the nineteenth century brought compulsory schooling, cheap newspapers and public libraries».', 4, 2),
         gap('Summary: Even earlier, some critics had warned of a ___ that might overheat the imagination of the young.',
             'reading mania', '«some commentators had warned of a reading mania, fearing that novels would overheat the imagination».', 4, 2),
         tf('Historians agree that silent reading was completely unknown in the ancient world.', 'F',
            '«there is evidence that silent reading was not unknown in the ancient world» — butunlay nomaʼlum boʻlmagan.', 1, ng=True),
         tf('Augustine himself preferred reading aloud to reading silently.', 'NG',
            "Matnda Avgustinning Ambroziyni koʻrib hayron boʻlgani aytilgan, lekin uning oʻzi qanday oʻqishni afzal koʻrgani haqida maʼlumot yoʻq.", 2),
         tf('Printing with movable type was developed in Europe before anywhere else.', 'F',
            '«similar techniques had been developed considerably earlier in East Asia».', 3, ng=True),
         tf('The arrival of printing did not immediately make reading a widespread skill.', 'T',
            '«It would be wrong … to imagine that printing immediately created a mass reading public; for several centuries, literacy remained confined largely to a minority».', 3, ng=True),
         ch('Why does the writer mention eighteenth-century warnings about a reading mania?',
            ['to prove that novels were harmful to young readers',
             'to show that new forms of reading have repeatedly caused moral anxiety',
             'to explain why women were discouraged from going to school',
             'to argue that modern concerns about screens are foolish'], 1,
            '«they reveal a recurring pattern in which new forms of reading provoke moral concern». D variant notoʻgʻri: G xatboshida muallif ekran haqidagi xavotirlar «misplaced» emas deydi.', 4),
         ch('According to paragraph F, what do researchers disagree about?',
            ['whether people read more on screens than on paper',
             'whether skimming gradually weakens deep reading or can be managed by readers',
             'whether notifications should be switched off while reading',
             'whether long texts should be published only on paper'], 1,
            '«Some researchers have suggested that the habit of skimming may gradually erode the capacity for sustained, deep reading, while others argue that readers can learn to switch deliberately between modes».', 5),
         ch('What is the writer\'s main conclusion?',
            ['Concerns about reading on screens are completely unjustified.',
             'Every change in reading has brought only losses.',
             'The kind of reading a society values needs to be actively developed.',
             'Society should return to reading printed books only.'], 2,
            '«the kind of reading a society values must be deliberately cultivated rather than taken for granted». Har bir oʻzgarish «real gains as well as real costs» olib kelgan — B variant notoʻgʻri.', 6),
     ])
