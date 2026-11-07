"""C1 · 1-boʻlim: Fan va tadqiqot (IELTS Academic darajasidagi ilmiy-ommabop matnlar)"""
from lib import *

B = 'c1'


def C(prompt, options, pos, explain, para):
    """options[0] — toʻgʻri javob; uni pos oʻringa qoʻyadi."""
    o = options[1:]
    o.insert(pos, options[0])
    return ch(prompt, o, pos, explain, para)

# ---------------------------------------------------------------- 1. Mikrobiom
H1 = ['Products and promises that outpace the evidence',
      'New tools that exposed a hidden variety',
      'How bacteria cause most common infections',
      'A long-standing view shown to be only part of the story',
      "Training and protecting the body's defences",
      'A promising link that remains unproven',
      'Replacing antibiotics with beneficial microbes',
      'Breaking down what the body cannot',
      'Everyday choices and medical treatments that reshape the community']

text(B, 'c1-01-microbiome', 'Mikrobiom', 'The Gut Microbiome', 'C1', 'exam',
     L('Biologiya va tibbiyot', 'Biology and medicine'),
     'IELTS Academic uslubidagi ilmiy-ommabop matn: ichakdagi mikroorganizmlar va ularning hazm, immunitet hamda '
     'ruhiy salomatlik bilan bogʻliqligi. Asosiy topshiriq — Matching headings: har bir xatboshining umumiy gʻoyasini '
     'aniqlang, bitta mos soʻzga aldanmang (sarlavhalar roʻyxatida ortiqcha variantlar bor). Taxminan 20 daqiqa ajrating: '
     'avval sarlavhalarni, soʻng TFNG, boʻshliq va test savollarini bajaring.',
     [
         P("For most of the twentieth century, bacteria were regarded primarily as agents of disease, invisible enemies to be "
           "eliminated with disinfectants and antibiotics. That view, while understandable, now appears strikingly incomplete. "
           "The human gut alone is home to a vast community of microorganisms, including bacteria, archaea, fungi and viruses, "
           "collectively known as the gut microbiota, while the term microbiome is often used for this community together with "
           "its genes. Far from being passive passengers, these organisms seem to participate in many of the processes on which "
           "human health depends. It was once widely claimed that microbial cells outnumber human cells by ten to one; more "
           "careful calculations have since suggested that the two figures are roughly comparable, but even this revised "
           "estimate implies a population of tens of trillions."),
         P("Part of the reason this world remained hidden for so long is methodological. Many gut microbes live in an "
           "environment without oxygen and have proved extremely difficult to grow in the laboratory, so traditional "
           "techniques, which relied on culturing organisms in a dish, captured only a fraction of them. The turning point came "
           "with the falling cost of DNA sequencing. Rather than attempting to grow each species, researchers can now extract "
           "genetic material directly from a sample, typically stool, and identify the organisms present by their genetic "
           "signatures. This shift has revealed a diversity far greater than earlier methods had suggested, along with "
           "considerable variation from one person to another."),
         P("Among the best-established functions of the microbiota is its contribution to digestion. Human enzymes are unable "
           "to break down many of the complex carbohydrates found in plant foods, collectively referred to as dietary fibre. "
           "Gut bacteria, by contrast, possess a remarkable repertoire of enzymes capable of fermenting these compounds. The "
           "products of this fermentation include short-chain fatty acids, which serve as an important source of energy for the "
           "cells lining the colon and appear to influence processes well beyond the gut. Certain bacteria also synthesise "
           "vitamins, notably vitamin K and several B vitamins, although the extent to which the body relies on this microbial "
           "supply is still debated."),
         P("Equally significant is the relationship between microbes and the immune system. Experiments with animals raised in "
           "completely sterile conditions, so-called germ-free animals, have shown that without exposure to microbes the immune "
           "system develops abnormally, with some of its components remaining underdeveloped. The resident community appears to "
           "act as a kind of training partner, helping the immune system learn to distinguish between harmless and dangerous "
           "organisms. Moreover, by occupying available space and consuming nutrients, established bacteria make it harder for "
           "disease-causing species to gain a foothold, a phenomenon known as colonisation resistance."),
         P("What shapes this community? Diet is among the most powerful influences. Studies have repeatedly associated diets "
           "rich in a wide variety of plant foods with a more diverse microbiota, whereas diets dominated by highly processed "
           "food tend to be linked with lower diversity, although diversity alone is no guarantee of health. Antibiotics exert "
           "a more abrupt effect. Because many of these drugs cannot distinguish between harmful and beneficial bacteria, a "
           "single course can substantially reduce microbial diversity. In many people the community largely recovers within "
           "weeks or months, yet some species may fail to return. One well-documented consequence of such disruption is that it "
           "can allow opportunistic pathogens to flourish, which is one reason doctors are urged to prescribe antibiotics only "
           "when they are genuinely needed."),
         P("The most intriguing and most controversial claims concern the brain. The gut and the brain communicate through "
           "several routes, including the vagus nerve, hormones and immune signals, and microbes produce substances that could, "
           "at least in principle, enter this conversation. In animal studies, altering the microbiota has been shown to change "
           "behaviours associated with anxiety. In humans, however, the picture is far less clear. Differences in gut bacteria "
           "have been observed in people with depression and other conditions, but such associations do not establish "
           "causation: illness may alter diet, sleep and medication, which in turn reshape the microbiota. It is therefore "
           "premature to conclude that changing one's gut bacteria can treat mental illness, and researchers generally describe "
           "this as an emerging rather than a settled area of research."),
         P("Such caution sits uneasily with the commercial enthusiasm surrounding the topic. Products promising to restore or "
           "optimise the microbiome are widely marketed, yet for many of them the supporting evidence remains limited, and the "
           "effects of probiotics appear to depend heavily on the specific strain and the condition in question. Part of the "
           "difficulty is that scientists have not agreed on what a healthy microbiome looks like; two healthy people may host "
           "strikingly different communities. Nevertheless, few researchers doubt that the field will continue to transform our "
           "understanding of the body. Not only has it challenged the image of bacteria as enemies, but it has also suggested "
           "that a human being might be better understood as an ecosystem than as a solitary organism."),
     ],
     [G('regard as', '… deb hisoblamoq'), G('strikingly', 'yaqqol, hayratlanarli darajada'),
      G('passive', 'sust, faol boʻlmagan'), G('methodological', 'uslubiy, metodologik'),
      G('culture', '(mikroblarni) laboratoriyada oʻstirmoq'), G('turning point', 'burilish nuqtasi'),
      G('repertoire', 'toʻplam, imkoniyatlar majmui'), G('ferment', 'bijgʻitmoq, achitmoq'),
      G('synthesise', 'sintez qilmoq, hosil qilmoq'), G('sterile', 'steril, mikrobsiz'),
      G('gain a foothold', 'oʻrnashib olmoq, joy egallamoq'), G('abrupt', 'keskin, toʻsatdan'),
      G('opportunistic pathogen', 'qulay vaziyatda kasallik qoʻzgʻatuvchi mikrob'),
      G('flourish', 'gullab-yashnamoq, koʻpayib ketmoq'), G('establish causation', 'sabab-oqibat bogʻliqligini isbotlamoq'),
      G('premature', 'barvaqt, shoshilinch'), G('sit uneasily with', '… bilan yaxshi chiqishmaslik, ziddiyatda boʻlmoq'),
      G('solitary', 'yakka, yolgʻiz')],
     [GN('c58-inversion', 'Inversiya: Not only has it challenged …',
         'Not only has it challenged the image of bacteria as enemies'),
      GN('c16-reporting-passive', 'Xabar beruvchi majhul nisbat: It was once widely claimed that …',
         'It was once widely claimed that microbial cells outnumber human cells by ten to one')],
     [
         hd(0, H1, 3, 'A xatboshi: bakteriyalar uzoq vaqt faqat «agents of disease» deb qaralgan, endi bu qarash «strikingly '
                      'incomplete» — yaʼni eski tasavvur hikoyaning faqat bir qismi. «How bacteria cause most common infections» '
                      'chalgʻitadi: kasallik faqat eski qarash sifatida tilga olinadi.'),
         hd(1, H1, 1, 'B xatboshi: mikroblarni oʻstirish qiyin boʻlgan, DNK sekvenlash arzonlashgach «revealed a diversity far '
                      'greater» — yangi vositalar yashirin xilma-xillikni ochib bergan.'),
         hd(2, H1, 7, 'C xatboshi: «Human enzymes are unable to break down … dietary fibre», bakteriyalar esa uni bijgʻitadi — '
                      'organizm oʻzi parchalay olmaydigan narsani parchalash.'),
         hd(3, H1, 4, 'D xatboshi: mikroblar immunitetni «training partner» sifatida oʻrgatadi va zararli turlarning oʻrnashishiga '
                      'yoʻl qoʻymaydi — oʻrgatish va himoya qilish.'),
         hd(4, H1, 8, 'E xatboshi: ovqatlanish (kundalik tanlov) va antibiotiklar (tibbiy davolash) mikroblar jamoasini '
                      'oʻzgartiradi. «Replacing antibiotics…» matnda yoʻq.'),
         hd(5, H1, 5, 'F xatboshi: ichak va miya bogʻliqligi qiziqarli, lekin «associations do not establish causation», '
                      '«emerging rather than a settled area» — istiqbolli, ammo isbotlanmagan bogʻliqlik.'),
         hd(6, H1, 0, 'G xatboshi: mahsulotlar keng reklama qilinadi, lekin «the supporting evidence remains limited» — '
                      'vaʼdalar dalillardan oldinga oʻtib ketgan.'),
         tf('Recent calculations confirm that microbial cells outnumber human cells by about ten to one.', 'F',
            'Matnda: oʻndan birga nisbat «once widely claimed», ammo «more careful calculations» ikki son «roughly comparable» '
            'ekanini koʻrsatgan — gap matnga zid.', 0, ng=True),
         tf('Short-chain fatty acids are produced in larger quantities from fruit than from cereals.', 'NG',
            'Matn qisqa zanjirli yogʻ kislotalari bijgʻish mahsuloti ekanini aytadi, lekin meva va donni solishtirmaydi.', 2),
         tf('Animals raised without any exposure to microbes develop immune systems that are not entirely normal.', 'T',
            '«without exposure to microbes the immune system develops abnormally» — «not entirely normal» bu fikrning '
            'parafrazi.', 3, ng=True),
         gap('Instead of growing each species, researchers now extract ___ directly from a sample.', 'genetic material',
             '«researchers can now extract genetic material directly from a sample». Javob ikki soʻz.', 1, 2),
         gap('The way established bacteria make it difficult for harmful species to settle is known as ___.',
             ['colonisation resistance', 'colonization resistance'],
             '«make it harder for disease-causing species to gain a foothold, a phenomenon known as colonisation resistance».',
             3, 2),
         C('Why does the writer mention that illness may alter diet, sleep and medication?',
            ['To explain why an observed link may not show that bacteria cause the illness',
             'To recommend lifestyle changes for people with depression',
             'To show that animal studies of the microbiota are unreliable',
             'To argue that the vagus nerve is the main route between gut and brain'], 2,
            'Bu gapdan oldin «such associations do not establish causation» deyilgan: kasallikning oʻzi mikrobiotani '
            'oʻzgartirishi mumkin, yaʼni sabab-oqibat teskari boʻlishi ham mumkin.', 5),
         C('What does the writer suggest about probiotics?',
            ['Their effects vary according to the particular strain and condition',
             'They have been proven to restore a healthy microbiome',
             'They are more effective than antibiotics',
             'They work equally well for everyone'], 1,
            '«the effects of probiotics appear to depend heavily on the specific strain and the condition in question».', 6),
     ])


# ---------------------------------------------------------------- 2. Xotira
text(B, 'c1-02-memory', 'Xotiraning ishonchsizligi', 'The Unreliable Memory', 'C1', 'exam',
     L('Psixologiya', 'Psychology'),
     'Ilmiy-ommabop matn: xotira videoyozuv emas, balki har safar qayta tiklanadigan jarayon; soxta xotiralar va guvohlar '
     'koʻrsatmasi. Asosiy topshiriq — True / False / Not Given. FALSE uchun matnda aniq zid gap boʻlishi kerak; agar matn '
     'shunchaki bu haqda gapirmasa — NOT GIVEN. «most», «all», «fully» kabi soʻzlarga alohida eʼtibor bering. '
     'Taxminan 20 daqiqa ajrating.',
     [
         P("Most people, if asked to describe how memory works, reach for a technological metaphor. Remembering, they assume, "
           "is rather like replaying a video: the original experience has been recorded somewhere in the brain, and recalling "
           "it is simply a matter of pressing play. The metaphor is intuitive and deeply rooted, and it shapes everything from "
           "the way we argue about the past with relatives to the weight that courts have traditionally attached to eyewitness "
           "testimony. Decades of psychological research, however, suggest that it is fundamentally misleading."),
         P("According to the view that now dominates the field, memory is reconstructive rather than reproductive. What is "
           "stored is not a complete record but a set of fragments, and each act of remembering involves assembling those "
           "fragments into a coherent account. Gaps are filled, often without our awareness, with information drawn from "
           "general knowledge, expectations and later experience. Someone recalling a visit to a restaurant, for instance, may "
           "remember a waiter bringing the bill simply because that is what usually happens in restaurants. Some researchers "
           "have further proposed that a memory becomes temporarily unstable each time it is retrieved and must then be stored "
           "again, which would offer an opportunity for it to be altered in the process, although the details of this "
           "mechanism remain under investigation."),
         P("Among the most influential demonstrations of this malleability is a series of experiments conducted in the 1970s. "
           "Participants watched short films of traffic accidents and were then asked questions about what they had seen. The "
           "crucial manipulation lay in a single verb. Some participants were asked how fast the cars were going when they hit "
           "each other; others heard the same question with the word smashed instead. Those who heard the more violent verb "
           "tended to give higher estimates of speed. Strikingly, when participants were questioned again a week later, those "
           "who had heard the word smashed were more likely to report having seen broken glass, even though the film had shown "
           "none. A subtle change in wording, in other words, appeared not merely to bias an answer but to alter the memory "
           "itself."),
         P("Later research went considerably further, showing that it is possible to create memories of entire events that "
           "never occurred. In studies of this kind, participants are presented with descriptions of several childhood "
           "episodes, supposedly supplied by family members, one of which has been invented. After repeated attempts to "
           "remember, a minority of participants come to report at least partial memories of the fictitious event, sometimes "
           "elaborating it with sensory details. Such findings do not imply that all memories are unreliable, nor that people "
           "can be persuaded to remember anything at all; rather, they reveal that the subjective experience of remembering is "
           "not, in itself, proof that an event took place."),
         P("Perhaps the most counterintuitive finding concerns the relationship between confidence and accuracy. It might be "
           "supposed that vivid, emotionally charged memories would be especially reliable. Yet when researchers have asked "
           "people to describe where they were on hearing news of a major public event, and then questioned them again months "
           "or years later, the accounts have frequently changed in significant ways, while the confidence with which they were "
           "reported has remained high. Confidence, it seems, can grow with each retelling, even as the details drift further "
           "from what actually happened."),
         P("Nowhere are the consequences of these findings more serious than in the criminal justice system. Cases in which "
           "convicted people were later cleared by DNA evidence have shown that mistaken identification by eyewitnesses "
           "contributed to a large proportion of those wrongful convictions. Crucially, most of the witnesses involved were not "
           "lying; they were sincerely reporting what they believed they remembered. In response, psychologists have "
           "recommended a number of reforms: identification procedures run by an officer who does not know which person is the "
           "suspect, the recording of a witness's confidence at the moment of the first identification, and interview "
           "techniques that avoid leading questions. Several jurisdictions have adopted some of these practices, though their "
           "implementation remains uneven."),
         P("It would be tempting to conclude from all this that human memory is simply defective. Many researchers, however, "
           "argue the opposite. A system that stored every experience in exhaustive detail would be costly and, arguably, less "
           "useful than one that extracts general patterns and discards specifics. The same flexibility that allows memories to "
           "be distorted also enables us to generalise from experience, to imagine alternatives and to plan for the future by "
           "recombining elements of the past. Seen in this light, the fallibility of memory is less a design flaw than the price "
           "of a mind built for prediction rather than for archiving."),
     ],
     [G('metaphor', 'metafora, koʻchma oʻxshatish'), G('deeply rooted', 'chuqur ildiz otgan'),
      G('testimony', 'koʻrsatma, guvohlik'), G('reconstructive', 'qayta tiklovchi, qayta quruvchi'),
      G('coherent', 'izchil, mantiqan bogʻlangan'), G('retrieve', '(xotiradan) chiqarib olmoq, eslamoq'),
      G('malleability', 'oʻzgaruvchanlik, yumshoqlik (shakl olish qobiliyati)'), G('manipulation', '(tajribada) ataylab oʻzgartirilgan omil'),
      G('fictitious', 'toʻqima, oʻylab topilgan'), G('elaborate', 'tafsilotlar bilan boyitmoq'),
      G('counterintuitive', 'sezgiga zid, kutilmagan'), G('emotionally charged', 'kuchli hissiyotli'),
      G('wrongful conviction', 'nohaq hukm qilinish'), G('leading question', 'yoʻnaltiruvchi (javobni ichiga olgan) savol'),
      G('jurisdiction', 'yurisdiksiya, sud hokimiyati hududi'), G('exhaustive', 'toʻliq, har tomonlama'),
      G('fallibility', 'xatoga moyillik')],
     [GN('c58-inversion', 'Inkor maʼnoli ravishdan keyin inversiya: Nowhere are …',
         'Nowhere are the consequences of these findings more serious than in the criminal justice system'),
      GN('c34-participle-clauses', 'Sifatdoshli ergash gap: Seen in this light, …',
         'Seen in this light, the fallibility of memory is less a design flaw than the price of a mind built for prediction')],
     [
         tf('Most people compare memory to a form of recording technology.', 'T',
            '«Most people … reach for a technological metaphor», yaʼni xotirani videoni qayta qoʻyishga oʻxshatadi.', 0,
            ng=True),
         tf('According to the reconstructive view, the brain keeps a complete record of each experience.', 'F',
            'Matnda aksi: «What is stored is not a complete record but a set of fragments».', 1, ng=True),
         tf('Scientists have fully explained how a retrieved memory is stored again.', 'F',
            '«the details of this mechanism remain under investigation» — toʻliq tushuntirilmagan.', 1, ng=True),
         tf('The films shown to participants in the traffic experiments included broken glass.', 'F',
            '«even though the film had shown none» — filmda singan oyna boʻlmagan.', 2, ng=True),
         tf('The researchers later repeated the traffic experiments with children and obtained similar results.', 'NG',
            'Matnda tajribaning bolalar bilan takrorlangani haqida hech narsa yoʻq.', 2),
         tf('In studies of invented childhood events, most participants came to remember the false event.', 'F',
            '«a minority of participants» — koʻpchilik emas, ozchilik.', 3, ng=True),
         tf('The studies of memories of major public events were all carried out in a single country.', 'NG',
            'Matn bu tadqiqotlarda hikoyalar oʻzgargani, ishonch esa yuqori qolganini aytadi, lekin ular qaysi yoki nechta '
            'mamlakatda oʻtkazilgani haqida hech narsa demaydi.', 4),
         tf('Most eyewitnesses in the wrongful conviction cases were deliberately giving false evidence.', 'F',
            '«most of the witnesses involved were not lying; they were sincerely reporting…» — ataylab emas.', 5, ng=True),
         tf('The writer believes that the flexibility of memory brings advantages as well as costs.', 'T',
            '«The same flexibility that allows memories to be distorted also enables us to generalise … plan for the future».',
            6, ng=True),
         gap('Psychologists recommend that identification procedures be run by an officer who does not know who the ___ is.',
             'suspect', '«run by an officer who does not know which person is the suspect».', 5, 2),
         gap('A witness should have their confidence recorded at the moment of the ___.', 'first identification',
             '«the recording of a witness\'s confidence at the moment of the first identification».', 5, 2),
         gap('Interview techniques should avoid ___.', ['leading questions'],
             '«interview techniques that avoid leading questions».', 5, 2),
         C('What is the main purpose of the first paragraph?',
            ['To introduce a common belief that the rest of the passage challenges',
             'To explain how video recording technology works',
             'To criticise courts for relying on eyewitnesses',
             'To describe typical arguments between family members'], 3,
            'Xatboshi xotira haqidagi keng tarqalgan «video» tasavvurini taqdim etadi va oxirida «fundamentally misleading» '
            'deydi — matnning qolgan qismi shuni rad etadi.', 0),
         C('In the final paragraph, the writer suggests that memory distortion is best seen as',
            ['a side effect of abilities that are useful',
             'a defect that technology may one day correct',
             'a problem that affects only emotional memories',
             'evidence that memory evolved mainly for storage'], 1,
            '«less a design flaw than the price of a mind built for prediction» — buzilish foydali qobiliyatlarning '
            '«narxi», yaʼni yon taʼsiri.', 6),
     ])


# ---------------------------------------------------------------- 3. Kvant kompyuterlar
text(B, 'c1-03-quantum', 'Kvant kompyuterlar', 'Quantum Computers: Beyond the Hype', 'C1', 'exam',
     L('Fan va texnologiya', 'Science and technology'),
     'Ilmiy-ommabop matn: bit va kubit, superpozitsiya, chalkashlik (entanglement), xatolarni tuzatish muammosi. Asosiy '
     'topshiriq — koʻp variantli test: muallifning maqsadi, munosabati va soʻz maʼnosini kontekstdan topish. Avval savolni '
     'oʻqing, matndan kerakli joyni toping, keyin har bir variantni matn bilan solishtiring — eng «aqlli» koʻringan emas, '
     'matn tasdiqlaydigan variantni tanlang. Taxminan 20 daqiqa ajrating.',
     [
         P("Few areas of technology attract as much breathless commentary as quantum computing. Headlines regularly announce "
           "that a new machine will revolutionise medicine, break every code or render conventional computers obsolete. Such "
           "claims tend to obscure both what makes the field genuinely remarkable and why progress has been slower than the "
           "excitement implies. Understanding either requires a brief look at how quantum computers differ from the machines we "
           "already use."),
         P("An ordinary computer processes information in bits, each of which is always in one of two definite states, "
           "conventionally written as 0 and 1. A quantum computer instead uses qubits, which can exist in a superposition of "
           "these two states. It is often said that a qubit is therefore 0 and 1 at the same time, but this popular description "
           "can mislead. More precisely, the state of a qubit is described by two numbers, known as amplitudes, which determine "
           "the probability of obtaining 0 or 1 when the qubit is measured. Measurement always produces a single definite "
           "result, and in doing so it destroys the superposition. A quantum computer cannot, therefore, simply try every "
           "possible answer at once and read them all out."),
         P("A second key ingredient is entanglement. When qubits become entangled, their states can no longer be described "
           "independently of one another: measuring one qubit gives information about the outcome of measuring the other, "
           "however far apart they may be. The correlations involved are stronger than any that could arise between ordinary "
           "objects, a fact that has been confirmed in numerous experiments. Contrary to a widespread misconception, though, "
           "entanglement cannot be used to send messages faster than light, because the result of each individual measurement "
           "remains random."),
         P("Where, then, does the potential advantage come from? The answer lies in the way amplitudes combine. Unlike "
           "probabilities, amplitudes can be negative or even complex numbers, so they can reinforce or cancel one another, much as waves do. A "
           "well-designed quantum algorithm choreographs this interference so that paths leading to wrong answers tend to "
           "cancel out while those leading to the right answer are amplified. Only certain problems possess the mathematical "
           "structure that makes such choreography possible. The best-known example is finding the prime factors of very large "
           "numbers, a task believed to be extremely difficult for conventional machines; another, which many researchers "
           "regard as more promising in the near term, is simulating the behaviour of molecules and materials, which are "
           "themselves governed by quantum mechanics. For a great many everyday tasks, by contrast, there is no reason to "
           "expect a quantum computer to be faster."),
         P("The principal obstacle is fragility. Qubits must be isolated from their surroundings with extraordinary care, "
           "since any unwanted interaction with heat, vibration or stray electromagnetic fields can disturb their delicate "
           "state, a process known as decoherence. Depending on the technology, qubits may be built from tiny superconducting "
           "circuits cooled to a fraction of a degree above absolute zero, from individual charged atoms held in place by "
           "electromagnetic fields, or from particles of light. Each approach has its own strengths, yet all of them suffer "
           "from errors at rates far higher than those tolerated in conventional electronics."),
         P("In ordinary computers, errors can be handled with a simple strategy: store several copies of each bit and, if one "
           "copy differs, trust the majority. Quantum mechanics rules out this approach in its straightforward form. A "
           "fundamental principle prevents an unknown quantum state from being copied, and checking a qubit directly would "
           "destroy the very superposition one wishes to protect. Quantum error correction gets round these constraints by "
           "spreading the information of one logical qubit across many physical qubits and measuring only carefully chosen "
           "collective properties, which reveal whether an error has occurred without revealing the stored information itself. "
           "The cost is considerable. Estimates vary with the hardware and the error rates achieved, but a single reliable "
           "logical qubit may require hundreds or even thousands of physical ones, and useful calculations would need many "
           "logical qubits."),
         P("None of this means that the field is overhyped in its entirety. Researchers have made steady progress in reducing "
           "error rates and have demonstrated the basic principles of error correction experimentally. What it does mean is "
           "that expectations should be calibrated. Quantum computers are unlikely ever to replace laptops or phones; they are "
           "better thought of as specialised instruments for a narrow but potentially important class of problems. Nor is it "
           "clear when machines powerful enough to outperform conventional computers on practically useful tasks will become "
           "available. Prudently, cryptographers are not waiting to find out: new encryption methods designed to resist quantum "
           "attack are already being developed and standardised, precisely because sensitive data intercepted today could, in "
           "principle, be decrypted in the future."),
     ],
     [G('breathless', 'hayajonli, haddan tashqari shov-shuvli'), G('render obsolete', 'eskirgan holga keltirmoq'),
      G('obscure', 'xiralashtirmoq, yashirmoq'), G('superposition', 'superpozitsiya (holatlarning ustma-ust kelishi)'),
      G('definite', 'aniq, muayyan'), G('entanglement', 'chalkashlik (kvant bogʻlanish)'),
      G('misconception', 'notoʻgʻri tasavvur'), G('reinforce', 'kuchaytirmoq'),
      G('interference', 'interferensiya (toʻlqinlarning qoʻshilishi)'), G('amplify', 'kuchaytirmoq'),
      G('fragility', 'moʻrtlik, nozik holat'), G('stray', 'tasodifiy, adashgan'),
      G('rule out', 'istisno qilmoq, imkonsiz qilmoq'), G('get round', '(qiyinchilikni) aylanib oʻtmoq'),
      G('calibrate', 'moslab sozlamoq, toʻgʻrilamoq'), G('prudently', 'oqilona, ehtiyotkorlik bilan'),
      G('intercept', 'yoʻlda tutib olmoq')],
     [GN('c58-inversion', 'Nor dan keyin inversiya: Nor is it clear when …',
         'Nor is it clear when machines powerful enough to outperform conventional computers on practically useful tasks '
         'will become available'),
      GN('c16-reporting-passive', 'Xabar beruvchi majhul nisbat: It is often said that …',
         'It is often said that a qubit is therefore 0 and 1 at the same time')],
     [
         C('According to paragraph B, why is it misleading to say that a qubit is 0 and 1 at the same time?',
            ['Measurement always gives one result, so all possible answers cannot be read out at once',
             'A qubit can in fact only hold the value 0',
             'Amplitudes cannot be measured with current technology',
             'Ordinary bits can also exist in a superposition'], 2,
            '«Measurement always produces a single definite result … cannot … simply try every possible answer at once and '
            'read them all out».', 1),
         C('What does the writer say about entanglement and communication?',
            ['It cannot be used to send messages faster than light because individual results are random',
             'It allows instant communication, but only over short distances',
             'Its effects have not yet been confirmed by experiment',
             'It produces weaker correlations than those between ordinary objects'], 3,
            '«entanglement cannot be used to send messages faster than light, because the result of each individual '
            'measurement remains random». Tajribalar tasdiqlagan, korrelyatsiyalar esa kuchliroq — boshqa variantlar zid.', 2),
         C('The word "choreographs" in paragraph D suggests that a quantum algorithm',
            ['carefully arranges how amplitudes combine',
             'randomly tests many possible answers',
             'copies amplitudes into several qubits',
             'measures each qubit many times'], 0,
            'Raqs xoreografiyasi kabi — har bir harakat oldindan rejalashtiriladi: notoʻgʻri yoʻllar bir-birini yoʻqqa chiqaradi, '
            'toʻgʻrisi kuchayadi. Bu tasodifiy sinash emas.', 3),
         C('Which application do many researchers regard as more promising in the near term?',
            ['Simulating molecules and materials', 'Factoring very large numbers',
             'Replacing laptops and phones', 'Sending secret messages'], 2,
            '«another, which many researchers regard as more promising in the near term, is simulating the behaviour of '
            'molecules and materials».', 3),
         C('Why can the ordinary method of error correction not simply be applied to qubits?',
            ['Unknown quantum states cannot be copied, and checking them directly destroys the superposition',
             'Qubits make too few errors to need correction',
             'Majority voting is too slow for quantum machines',
             'Physical qubits cannot be grouped together'], 1,
            '«A fundamental principle prevents an unknown quantum state from being copied, and checking a qubit directly would '
            'destroy the very superposition».', 5),
         C("What is the writer's overall attitude to quantum computing?",
            ['Cautiously positive: real progress has been made, but expectations should be realistic',
             'Dismissive: the whole field is overhyped',
             'Enthusiastic: quantum computers will soon replace conventional ones',
             'Neutral: the writer avoids expressing any view'], 3,
            '«None of this means that the field is overhyped in its entirety… expectations should be calibrated» — '
            'ijobiy, lekin ehtiyotkor munosabat.', 6),
         tf('Measuring a qubit leaves its superposition unchanged.', 'F',
            '«in doing so it destroys the superposition» — oʻzgarmasdan qolmaydi.', 1, ng=True),
         tf('Quantum computers are expected to be faster than conventional computers at most everyday tasks.', 'F',
            '«For a great many everyday tasks … there is no reason to expect a quantum computer to be faster».', 3, ng=True),
         tf('Error rates have fallen at the same speed for every type of qubit.', 'NG',
            'Matnda xatolar kamayayotgani («steady progress in reducing error rates») aytilgan, lekin turli kubit turlari '
            'solishtirilmagan.', 6),
         tf('Some encryption methods intended to withstand quantum computers are already being developed.', 'T',
            '«new encryption methods designed to resist quantum attack are already being developed».', 6, ng=True),
         gap('Unwanted interaction with the surroundings disturbs a qubit in a process called ___.', 'decoherence',
             '«can disturb their delicate state, a process known as decoherence».', 4, 2),
         gap('Error correction spreads the information of one ___ across many physical qubits.', 'logical qubit',
             '«spreading the information of one logical qubit across many physical qubits».', 5, 2),
         gap('Like waves, amplitudes can reinforce or ___ one another.', 'cancel',
             '«they can reinforce or cancel one another, much as waves do».', 3, 2),
     ])


# ---------------------------------------------------------------- 4. Okean tubi
text(B, 'c1-04-deep-ocean', 'Okean tubi', 'The Deep Ocean', 'C1', 'exam',
     L('Yer va okean', 'Earth and ocean'),
     'Ilmiy-ommabop matn: okean tubi qanchalik kam oʻrganilgan, gidrotermal manbalar, xemosintez va chuqur dengizda '
     'qazib olish boʻyicha bahs. Asosiy topshiriq — Summary completion: qisqacha bayondagi boʻshliqlarni matndagi aynan '
     'soʻzlar bilan toʻldiring (soʻz soni chegarasiga rioya qiling). Bayon parafraz qilingan, shuning uchun avval kerakli '
     'xatboshini toping, soʻng grammatik jihatdan mos soʻzni ajrating. Taxminan 20 daqiqa ajrating.',
     [
         P("It is often remarked that humanity knows more about the surface of the Moon than about the floor of its own oceans. "
           "Like many memorable claims, this one is an oversimplification, but it contains a significant truth. Satellites can "
           "estimate the shape of the entire seabed indirectly, by measuring tiny variations in the height of the sea surface, "
           "yet the maps produced in this way are coarse and capable of revealing only large features. Detailed mapping "
           "requires ships equipped with sonar, which builds up a picture from the echoes of sound pulses, and recent estimates "
           "suggest that only around a quarter of the seafloor has been surveyed in this way. Direct observation of the deep "
           "sea, whether by human visitors or by cameras, covers a far smaller fraction still."),
         P("The reasons are largely physical. Sunlight fades rapidly with depth, and below roughly a thousand metres the ocean "
           "is in permanent darkness apart from light produced by living organisms. Temperatures in most of the deep sea hover "
           "only a few degrees above freezing. Most formidable of all is pressure, which increases by approximately one "
           "atmosphere for every ten metres of descent. At the bottom of the deepest trenches, more than ten kilometres down, "
           "the pressure exceeds a thousand times that at the surface. Vehicles capable of withstanding such conditions are "
           "expensive to build and operate, which is why much exploration today relies on remotely operated and autonomous "
           "machines rather than on crewed submersibles."),
         P("Precisely because it is so difficult to reach, the deep sea has continued to overturn scientific assumptions. In "
           "1977, researchers exploring a volcanic ridge in the eastern Pacific near the Galápagos Islands came upon something "
           "few had anticipated: dense communities of animals clustered around hydrothermal vents. At such vents, seawater seeps "
           "into the crust, is heated by underlying magma and re-emerges laden with dissolved minerals. The emerging fluid can "
           "exceed 350 degrees Celsius, yet it does not boil, because the immense pressure raises its boiling point. Where it "
           "meets the cold surrounding water, the minerals precipitate, in some cases building tall chimneys that release dark, "
           "smoke-like plumes."),
         P("The discovery was remarkable not only for the abundance of life but for its source of energy. Almost every "
           "ecosystem on the surface ultimately depends on photosynthesis, the capture of energy from sunlight. Around the "
           "vents, by contrast, the foundation of the food web consists of microbes that obtain energy from chemical reactions, "
           "for example by oxidising hydrogen sulphide dissolved in the vent fluid, a process known as chemosynthesis. Some vent "
           "animals have formed intimate partnerships with these microbes. Giant tubeworms, for instance, lack a mouth and "
           "digestive system as adults and instead house vast numbers of chemosynthetic bacteria within their bodies, which "
           "supply them with nourishment. Such findings have encouraged speculation that life on Earth may have originated in "
           "comparable environments and that similar habitats might exist on icy moons elsewhere in the solar system, although "
           "both ideas remain hypotheses."),
         P("Beyond the vents, the deep seafloor hosts a diversity of life that scientists are only beginning to catalogue. "
           "Expeditions to poorly studied regions routinely return with species new to science. Many deep-sea organisms grow "
           "slowly, reproduce late and live for remarkably long periods; some deep-sea corals are thought to be hundreds or "
           "even thousands of years old. These characteristics, which are adaptations to a cold environment with scarce food, "
           "also mean that populations may take a very long time to recover from disturbance."),
         P("It is against this background that the debate over deep-sea mining has unfolded. On vast, flat abyssal plains, the "
           "seabed is scattered with potato-sized lumps known as polymetallic nodules, which contain metals such as nickel, "
           "cobalt, manganese and copper. Supporters of mining argue that these metals are needed in growing quantities for "
           "batteries and other technologies associated with the transition to cleaner energy, and that collecting nodules from "
           "the seafloor might avoid some of the environmental and social harms associated with mining on land, such as "
           "deforestation and the displacement of communities."),
         P("Critics counter that too little is known about deep-sea ecosystems to judge the risks responsibly. Nodules form "
           "extremely slowly, over millions of years, and many organisms live attached to them or depend on them, so their "
           "removal would be effectively permanent on any human timescale. Mining machines would also stir up plumes of "
           "sediment that could spread over wide areas. Small-scale disturbance experiments conducted decades ago have left "
           "tracks on the seabed that remain visible, and the affected communities have not fully recovered. For these reasons, "
           "a number of governments and scientists have called for a pause until more research has been done, while the "
           "international body responsible for regulating mining on the seabed beyond national jurisdiction has continued to "
           "negotiate rules."),
         P("Both sides, then, appeal to environmental concerns, which is part of what makes the dispute so difficult to "
           "resolve. What seems clear is that decisions about the deep sea will be made under considerable uncertainty, and "
           "that the gaps in our knowledge, once merely a curiosity, have become a matter of practical consequence."),
     ],
     [G('oversimplification', 'haddan tashqari soddalashtirish'), G('coarse', 'dagʻal, aniqligi past'),
      G('formidable', 'jiddiy, qoʻrqinchli darajada kuchli'), G('withstand', 'bardosh bermoq'),
      G('submersible', 'suv osti apparati'), G('overturn', 'agʻdarmoq, rad etmoq'),
      G('seep', 'sizib oʻtmoq'), G('laden with', '… bilan toʻla, yuklangan'),
      G('precipitate', 'choʻkma hosil qilmoq'), G('abundance', 'moʻllik, koʻplik'),
      G('intimate partnership', 'yaqin hamkorlik (simbioz)'), G('speculation', 'taxmin, faraz'),
      G('scarce', 'kam, tanqis'), G('abyssal plain', 'okean tubidagi tekislik'),
      G('displacement', 'majburan koʻchirilish'), G('counter', 'eʼtiroz bildirmoq, javoban aytmoq'),
      G('stir up', 'koʻtarib yubormoq, loyqalatmoq'), G('beyond national jurisdiction', 'davlatlar yurisdiksiyasidan tashqarida')],
     [GN('c59-fronting-emphasis', 'Taʼkid uchun oldinga chiqarish: Most formidable of all is pressure',
         'Most formidable of all is pressure'),
      GN('c57-cleft-sentences', 'Ajratuvchi (cleft) gap: It is against this background that …',
         'It is against this background that the debate over deep-sea mining has unfolded')],
     [
         gap('In 1977, scientists exploring a volcanic ridge found dense animal communities around hydrothermal ___.', 'vents',
             '«came upon … dense communities of animals clustered around hydrothermal vents».', 2, 2),
         gap('The hot vent fluid does not boil because the immense ___ raises its boiling point.', 'pressure',
             '«it does not boil, because the immense pressure raises its boiling point».', 2, 2),
         gap('Instead of relying on sunlight, the vent food web is based on a process called ___.', 'chemosynthesis',
             '«microbes that obtain energy from chemical reactions … a process known as chemosynthesis».', 3, 2),
         gap('Adult giant tubeworms have no mouth and are fed by ___ living inside their bodies.', 'chemosynthetic bacteria',
             '«house vast numbers of chemosynthetic bacteria within their bodies, which supply them with nourishment».', 3, 2),
         gap('Abyssal plains are covered with ___, which contain metals such as nickel and cobalt.', 'polymetallic nodules',
             '«potato-sized lumps known as polymetallic nodules, which contain metals such as nickel, cobalt…».', 5, 2),
         gap('Critics warn that mining machines would create ___ of sediment that could travel far.', 'plumes',
             '«Mining machines would also stir up plumes of sediment that could spread over wide areas».', 6, 2),
         tf('Satellite measurements can show small features of the seabed in detail.', 'F',
            '«the maps produced in this way are coarse and capable of revealing only large features».', 0, ng=True),
         tf('Machines without people on board play a major part in deep-sea exploration today.', 'T',
            '«much exploration today relies on remotely operated and autonomous machines rather than on crewed submersibles».',
            1, ng=True),
         tf('The researchers who found the first vents in 1977 were searching for new species of fish.', 'NG',
            'Matnda ular vulqon tizmasini oʻrganayotgani aytilgan; baliqning yangi turlarini qidirgani haqida maʼlumot yoʻq.', 2),
         tf('Polymetallic nodules can form again within a few decades of being removed.', 'F',
            '«Nodules form extremely slowly, over millions of years» — bir necha oʻn yil emas.', 6, ng=True),
         C('What is the writer\'s view of the claim that we know more about the Moon than about the ocean floor?',
            ['It exaggerates, but it reflects a real gap in our knowledge',
             'It is completely accurate',
             'It is a myth with no basis in fact',
             'It applies only to shallow coastal waters'], 2,
            '«this one is an oversimplification, but it contains a significant truth» — mubolagʻa, lekin haqiqat ulushi bor.', 0),
         C('Why does the writer mention deforestation and the displacement of communities?',
            ['To give examples of harms that supporters say seabed mining might avoid',
             'To show that mining on land is no longer necessary',
             'To argue that deep-sea mining causes the same problems',
             'To explain why metal prices are rising'], 0,
            'Bular «harms associated with mining on land» misollari; tarafdorlar nodul yigʻish shu zararlarning bir qismidan '
            'qochish imkonini beradi deydi.', 5),
         C('What point does the writer make in the final paragraph?',
            ['Both supporters and opponents of mining use environmental arguments',
             'Mining should begin as soon as possible',
             'The international rules are already complete',
             'Scientific curiosity is the only reason to study the deep sea'], 1,
            '«Both sides, then, appeal to environmental concerns» — ikkala tomon ham ekologik dalillarga tayanadi.', 7),
     ])


# ---------------------------------------------------------------- 5. Platsebo
H5 = ['A standard method that revealed a puzzle',
      'When expectations cause harm',
      'Reasons for improvement that have nothing to do with the placebo itself',
      'Evidence that placebos can cure serious disease',
      'Why misleading patients is hard to justify',
      'How expectation and learning affect the body',
      'Honesty that may still help',
      'The setting and style of treatment']

text(B, 'c1-05-placebo', 'Platsebo effekti', 'The Placebo Effect', 'C1', 'exam',
     L('Tibbiyot', 'Medicine'),
     'Ilmiy-ommabop matn: platsebo va nocebo effektlari, kutish omili, tibbiyot etikasi va «ochiq platsebo» tadqiqotlari. '
     'Aralash topshiriqlar: Matching headings, True/False/Not Given, test va boʻshliq toʻldirish — haqiqiy imtihondagi '
     'kabi. Sarlavhalardan boshlang (matnning tuzilishini tushunib olasiz), keyin qolgan savollarga oʻting. '
     'Taxminan 20 daqiqa ajrating.',
     [
         P("In a typical clinical trial, a new drug is compared not only with no treatment but with a placebo: a tablet, "
           "injection or procedure that looks identical to the real thing but contains no active ingredient. If patients "
           "receiving the drug improve more than those receiving the placebo, the difference can reasonably be attributed to "
           "the drug. This design has become a cornerstone of modern medicine. Yet it has also drawn attention to a curious "
           "fact. Patients in the placebo group frequently improve too, sometimes to a striking degree, and explaining why has "
           "occupied researchers for decades."),
         P("Not all of this improvement, however, reflects a genuine placebo effect. Many conditions fluctuate or resolve on "
           "their own, so some patients would have recovered regardless of what they were given. A statistical phenomenon "
           "known as regression to the mean also plays a part: people tend to seek treatment, or to enrol in trials, when their "
           "symptoms are at their worst, and symptoms that are unusually severe are likely to be less severe on a later "
           "occasion simply by chance. Participants may also report feeling better because they wish to please the researchers. "
           "Disentangling these influences requires trials that include a third group receiving no treatment at all, and when "
           "such comparisons have been made, the true placebo effect has often proved smaller than the raw figures implied."),
         P("Where genuine placebo effects do occur, expectation appears to be central. When patients anticipate relief, the "
           "brain may alter the way it processes signals from the body. Research on pain has been particularly revealing. In "
           "some experiments, the pain relief produced by a placebo was reduced by a drug that blocks the action of opioids, "
           "suggesting that the placebo had triggered the release of the body's own pain-relieving chemicals. Learning also "
           "seems to contribute: a person who has repeatedly experienced relief after taking a particular pill may come to "
           "respond to the pill itself. It is worth stressing, though, that placebo effects are most consistently observed for "
           "subjective symptoms such as pain, nausea and fatigue. There is little evidence that a placebo can shrink a tumour "
           "or cure an infection."),
         P("Context, too, seems to matter. Some studies have suggested that the same inactive substance can produce stronger "
           "effects when it is given by injection rather than as a tablet, when it is described as expensive, or when it is "
           "delivered by a clinician who is warm and attentive. Results of this kind should be interpreted cautiously, since "
           "individual studies are often small, but they hint that the ritual of treatment, and not merely its chemical "
           "content, can influence how patients feel."),
         P("The same mechanisms can also work in the opposite direction. The nocebo effect refers to the harmful consequences "
           "of negative expectations. In clinical trials, participants who receive a placebo commonly report side effects, "
           "often resembling those listed for the active drug they believe they may be taking. Patients who have read long "
           "lists of possible side effects may be more likely to experience them. This poses a genuine dilemma for doctors, who "
           "are obliged to inform patients of risks but who may, by the manner in which they do so, inadvertently contribute to "
           "the very symptoms they describe."),
         P("Deliberately exploiting placebo effects in ordinary medical practice raises serious ethical questions. Giving a "
           "patient an inert pill while claiming that it is an active medicine involves deception, which is difficult to "
           "reconcile with the principle of informed consent and could erode trust if discovered. Surveys in several countries "
           "have nonetheless indicated that a proportion of doctors sometimes prescribe treatments they do not expect to have a "
           "specific effect on the condition, such as vitamins, partly for their psychological value."),
         P("An intriguing possible way out of this dilemma is the open-label placebo, in which patients are told explicitly "
           "that they are receiving a pill with no active ingredient, often along with an explanation of how placebo effects "
           "may work. Small trials in conditions such as irritable bowel syndrome and chronic back pain have reported "
           "improvements in symptoms among those taking such pills. Were these results to be confirmed in larger and more "
           "rigorous studies, they would suggest that deception is not essential to the placebo response. For now, though, "
           "caution is warranted: the trials have mostly been modest in size, the outcomes were largely self-reported, and it "
           "is inherently difficult to design an appropriate comparison for a treatment whose nature the patient already "
           "knows. Whatever their ultimate verdict, such studies underline a broader lesson, namely that the experience of "
           "being cared for may itself be part of how treatment works."),
     ],
     [G('attribute to', '… ga nisbat bermoq, … ning natijasi deb bilmoq'), G('cornerstone', 'asos, tamal toshi'),
      G('fluctuate', 'oʻzgarib turmoq, tebranmoq'), G('regression to the mean', 'oʻrtachaga qaytish (statistik hodisa)'),
      G('enrol', 'roʻyxatdan oʻtmoq, qatnashmoq'), G('disentangle', 'ajratib olmoq, chigalini yechmoq'),
      G('anticipate', 'kutmoq, oldindan sezmoq'), G('trigger', 'qoʻzgʻatmoq, ishga tushirmoq'),
      G('subjective', 'subyektiv, shaxsiy his-tuygʻuga asoslangan'), G('attentive', 'eʼtiborli'),
      G('inadvertently', 'bilmagan holda, beixtiyor'), G('inert', 'nofaol, taʼsirsiz'),
      G('reconcile with', '… bilan muvofiqlashtirmoq'), G('informed consent', 'xabardor qilingan rozilik'),
      G('erode trust', 'ishonchni yemirmoq'), G('rigorous', 'qatʼiy, puxta'),
      G('warranted', 'oʻrinli, asosli'), G('verdict', 'xulosa, hukm')],
     [GN('c50-inverted-conditionals', 'Inversiyali shart gap: Were these results to be confirmed …',
         'Were these results to be confirmed in larger and more rigorous studies, they would suggest that deception is not '
         'essential to the placebo response'),
      GN('c33-relative-advanced', 'Murakkab nisbiy gap: a treatment whose nature …',
         'a treatment whose nature the patient already knows')],
     [
         hd(1, H5, 2, 'B xatboshi: platsebo guruhidagi yaxshilanishning bir qismi kasallikning oʻz-oʻzidan oʻtishi, '
                      '«regression to the mean» va tadqiqotchilarni xursand qilish istagi bilan bogʻliq — platsebodan '
                      'mustaqil sabablar.'),
         hd(3, H5, 7, 'D xatboshi: inyeksiya yoki tabletka, «expensive», «warm and attentive» shifokor — davolanish muhiti '
                      'va uslubi («the ritual of treatment») taʼsir qiladi.'),
         hd(5, H5, 4, 'F xatboshi: bemorni aldash «difficult to reconcile with the principle of informed consent» — nega '
                      'bunday aldashni oqlash qiyin.'),
         tf('Some patients in placebo groups would have got better without receiving anything.', 'T',
            '«some patients would have recovered regardless of what they were given».', 1, ng=True),
         tf('Placebos have been shown to shrink tumours in some patients.', 'F',
            '«There is little evidence that a placebo can shrink a tumour» — isbotlangan emas.', 2, ng=True),
         tf('Patients who experience nocebo effects are usually older than average.', 'NG',
            'Matnda nocebo effektini boshdan kechiradiganlarning yoshi haqida hech narsa aytilmagan.', 4),
         tf('In open-label placebo studies, patients know that their pill contains no active ingredient.', 'T',
            '«patients are told explicitly that they are receiving a pill with no active ingredient».', 6, ng=True),
         C('Why do some trials include a third group that receives no treatment?',
            ['To separate the true placebo effect from other causes of improvement',
             'To make the trial larger and therefore cheaper',
             'To test whether patients wish to please the researchers',
             'To find out which drug has the fewest side effects'], 3,
            '«Disentangling these influences requires trials that include a third group receiving no treatment» — '
            'haqiqiy platsebo effektini boshqa omillardan ajratish uchun.', 1),
         C('What dilemma does the writer describe in paragraph E?',
            ['Informing patients about side effects may itself help to cause them',
             'Patients refuse to take placebos once they know about them',
             'Doctors are not allowed to tell patients about risks',
             'Active drugs and placebos cause exactly the same side effects'], 2,
            'Shifokorlar xavflar haqida aytishga majbur, lekin «inadvertently contribute to the very symptoms they describe».', 4),
         C("What is the writer's attitude to research on open-label placebos?",
            ['Interested, but cautious about how strong the evidence is',
             'Convinced that it proves deception is unnecessary',
             'Dismissive, because the trials were badly designed',
             'Uninterested, since it concerns only rare conditions'], 1,
            '«An intriguing possible way out» — qiziqish; «For now, though, caution is warranted» — ehtiyotkorlik.', 6),
         gap('People often enrol in trials when their symptoms are at their worst, which produces an effect called '
             'regression to the ___.', 'mean',
             '«A statistical phenomenon known as regression to the mean… when their symptoms are at their worst».', 1, 2),
         gap('In some pain experiments, a drug that blocks the action of ___ reduced the relief produced by a placebo.',
             'opioids', '«reduced by a drug that blocks the action of opioids».', 2, 2),
         gap('Placebo effects are most consistently seen for ___ such as pain, nausea and fatigue.', 'subjective symptoms',
             '«most consistently observed for subjective symptoms such as pain, nausea and fatigue».', 2, 2),
     ])
