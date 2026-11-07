"""C1 · 3-boʻlim: Psixologiya (IELTS Academic darajasidagi oʻqish testlari)"""
from lib import *

B = 'c1'
TAG = L('Psixologiya', 'Psychology')


# ---------------------------------------------------------------- 11
H11 = ['Why knowing about errors is not enough to prevent them',
       'Two contrasting styles of mental processing',
       'How an arbitrary starting point distorts estimates',
       'When memorability is mistaken for frequency',
       'Why shortcuts deserve a fairer assessment',
       'The circumstances in which experience produces reliable instincts',
       'The brain regions responsible for rational thought',
       'How advertisers exploit consumers\' fears']

text(B, 'c1-11-decisions', 'Qaror qabul qilish', 'Shortcuts of the Mind', 'C1', 'exam', TAG,
     'Akademik matn: inson qanday qaror qabul qilishi, «evristika» deb ataluvchi aqliy qisqa yoʻllar va ular keltirib '
     'chiqaradigan xatolar haqida. Topshiriqlar: Matching headings, True/False/Not Given, boʻshliq toʻldirish va test '
     'savollari. Taxminan 20 daqiqa ajrating. Maslahat: sarlavhalarni moslashda har bir xatboshining birinchi va oxirgi '
     'gapiga eʼtibor bering — asosiy fikr koʻpincha shu yerda boʻladi; matndagi bitta soʻzga oʻxshash sarlavha koʻpincha tuzoq.',
     [
         P("For much of the twentieth century, many economic models rested on a convenient assumption: that people weigh "
           "the available options carefully and choose whatever best serves their interests. Psychologists who studied real "
           "decisions, however, began to document a rather different picture. Rather than calculating every possibility, "
           "people appear to rely heavily on heuristics, mental shortcuts that allow a judgement to be reached quickly and "
           "with little effort. These shortcuts are often remarkably effective, yet under certain conditions they produce "
           "systematic and predictable errors, which researchers have come to call cognitive biases."),
         P("A useful, if simplified, way of thinking about this research distinguishes between two modes of thought. The "
           "first is fast, automatic and largely effortless; it is the mode that allows an experienced driver to brake before "
           "consciously noticing a hazard, or a reader to grasp the meaning of a familiar word instantly. The second is slow, "
           "deliberate and demanding, and it is called upon when we solve an unfamiliar problem or check an argument step by "
           "step. It should be stressed that these are descriptions of styles of processing rather than two physical systems "
           "located in separate parts of the brain. Most everyday judgements are handled by the fast mode, and the slower one "
           "frequently accepts its conclusions without serious scrutiny."),
         P("One of the most thoroughly documented biases is anchoring. When people are asked to estimate an uncertain "
           "quantity, an initial number, even one that is obviously irrelevant, tends to pull their answer towards it. In one "
           "well-known demonstration, participants watched what appeared to be a random number produced by a spinning wheel "
           "before estimating a quantity entirely unrelated to it; those who had seen a higher number generally gave higher "
           "estimates. Outside the laboratory, the same tendency may explain why the first offer in a negotiation so often "
           "shapes the final agreement, and why a reduced price looks attractive mainly in comparison with the original "
           "figure printed beside it."),
         P("A second shortcut, the availability heuristic, involves judging how frequent or likely an event is by how easily "
           "examples come to mind. Since memorable events are often genuinely common, this rule of thumb frequently works. "
           "The difficulty is that ease of recall is also influenced by how vivid, recent or emotionally charged an event is. "
           "Dramatic incidents such as plane crashes or shark attacks receive extensive media coverage and are easy to "
           "picture, so people may overestimate their likelihood while underestimating less spectacular but considerably "
           "more common risks. Judgements of risk, in other words, can reflect the news agenda as much as the underlying "
           "reality."),
         P("Perhaps the most consequential finding concerns the asymmetry between losses and gains. A loss, it seems, is "
           "generally felt more intensely than a gain of the same size, a tendency known as loss aversion. This helps to "
           "explain why many people decline a bet on the toss of a coin that offers an equal chance of winning or losing the "
           "same amount of money, even though such a bet is, in purely financial terms, perfectly fair. Closely related is "
           "the framing effect: the same option may be accepted when it is described in terms of what can be gained but "
           "rejected when it is presented in terms of what might be lost."),
         P("It would be a mistake, however, to conclude that human judgement is simply defective. Some researchers have "
           "argued that heuristics should be evaluated not against an abstract ideal of rationality but in relation to the "
           "environments in which they are used. From this perspective, a simple rule that ignores much of the available "
           "information can, under conditions of uncertainty, perform as well as or even better than an elaborate "
           "calculation. Biases, then, may be best understood as the occasional price paid for a system that is, for the "
           "most part, fast, economical and surprisingly accurate."),
         P("Under what conditions, then, can intuition be trusted? A considerable degree of consensus has emerged, even among "
           "researchers from rival traditions, that expert intuition is reliable mainly when two conditions are met: the environment must be sufficiently regular to contain learnable "
           "patterns, and the person must have had extensive practice with prompt and accurate feedback. Experienced "
           "firefighters, nurses and chess players often meet these conditions, and their rapid judgements can be "
           "impressively accurate. By contrast, those who make long-term forecasts about political events or financial "
           "markets operate in environments where feedback is delayed and patterns are unstable, and their confidence may "
           "far exceed their actual accuracy. Subjective certainty, in short, is a poor indicator of whether an intuition "
           "deserves to be believed."),
         P("Simply knowing about biases does not appear to make people immune to them. Were awareness alone sufficient, the "
           "researchers who study these effects would presumably be free of them, which does not seem to be the case. More "
           "promising are changes to the way decisions are structured: using checklists, deliberately considering why an "
           "initial judgement might be wrong, or seeking the views of others before committing to a conclusion. Such "
           "procedures cannot remove the shortcuts on which the mind depends, but they can create moments in which the "
           "slower mode of thinking has an opportunity to intervene."),
     ],
     [G('heuristic', 'evristika, aqliy qisqa yoʻl'), G('systematic', 'tizimli, muntazam takrorlanadigan'),
      G('deliberate', 'oʻylab qilingan, ongli'), G('scrutiny', 'sinchkov tekshiruv'),
      G('anchoring', '«langar» effekti — boshlangʻich raqamga bogʻlanib qolish'),
      G('estimate', 'taxmin qilmoq; taxmin'), G('vivid', 'yorqin, jonli'),
      G('overestimate', 'oshirib baholamoq'), G('consequential', 'oqibati katta, muhim'),
      G('asymmetry', 'nosimmetriklik, notenglik'), G('loss aversion', 'yoʻqotishdan qochish moyilligi'),
      G('framing effect', 'taqdim etish (ramka) effekti'), G('elaborate', 'murakkab, puxta ishlangan'),
      G('consensus', 'umumiy kelishuv, yakdil fikr'), G('prompt feedback', 'tezkor qayta aloqa'),
      G('indicator', 'koʻrsatkich, belgi'), G('be immune to', '… taʼsiriga berilmaslik, … dan himoyalangan boʻlmoq'),
      G('intervene', 'aralashmoq, oraga kirmoq')],
     [GN('c50-inverted-conditionals', 'Inversiyali shart gap: Were awareness alone sufficient, …',
         'Were awareness alone sufficient, the researchers who study these effects would presumably be free of them'),
      GN('c39-it-there', 'Kirish «it»: It would be a mistake … to conclude that …',
         'It would be a mistake, however, to conclude that human judgement is simply defective')],
     [
         hd(1, H11, 1, 'Xatboshi B: fikrlashning ikki usuli — tez, avtomatik va sekin, ongli. «The brain regions …» '
                       'chalgʻitadi: matnda aksincha «rather than two physical systems located in separate parts of the brain» deyilgan.'),
         hd(2, H11, 2, 'Xatboshi C: «anchoring» — ahamiyatsiz boshlangʻich raqam ham taxminni oʻziga tortadi '
                       '(«an initial number, even one that is obviously irrelevant, tends to pull their answer towards it»).'),
         hd(3, H11, 3, 'Xatboshi D: hodisaning qanchalik tez-tez boʻlishini uning qanchalik oson esga tushishiga qarab baholash — '
                       '«judging how frequent … by how easily examples come to mind».'),
         hd(5, H11, 4, 'Xatboshi F: evristikalarni «nuqson» deb emas, muhitga nisbatan baholash kerak — '
                       '«It would be a mistake … to conclude that human judgement is simply defective».'),
         hd(6, H11, 5, 'Xatboshi G: intuitsiya qachon ishonchli — muhit muntazam va tezkor qayta aloqa boʻlganda. '
                       '«instincts» = «intuition», «experience» = «extensive practice».'),
         tf('According to the passage, the two modes of thought correspond to separate physical structures in the brain.', 'F',
            'Matnda aksi: «these are descriptions of styles of processing rather than two physical systems located in separate '
            'parts of the brain».', 1, ng=True),
         tf('People may misjudge certain risks partly because of the amount of media attention some events receive.', 'T',
            '«Dramatic incidents … receive extensive media coverage … so people may overestimate their likelihood» — '
            '«misjudge» = «overestimate / underestimate».', 3, ng=True),
         tf('Loss aversion tends to be stronger in older people than in younger people.', 'NG',
            'Loss aversion taʼriflangan, lekin yosh guruhlari solishtirilmagan — matnda bu haqda maʼlumot yoʻq.', 4),
         tf('The writer suggests that expert intuition is reliable in any field where a person has many years of experience.', 'F',
            'Ikki shart kerak: «the environment must be sufficiently regular» va «prompt and accurate feedback». Siyosiy va moliyaviy '
            'prognozlarda tajriba boʻlsa ham intuitsiya ishonchsiz — demak «any field» notoʻgʻri.', 6, ng=True),
         gap('Researchers use the term ___ for the predictable errors that mental shortcuts can sometimes produce.',
             ['cognitive biases', 'biases'],
             '«they produce systematic and predictable errors, which researchers have come to call cognitive biases».', 0, 2),
         gap('Under the framing effect, an option may be rejected if it is described in terms of what might be ___.',
             ['lost'],
             '«rejected when it is presented in terms of what might be lost» — «described» = «presented».', 4, 2),
         ch('What is the writer\'s main purpose in paragraph F?',
            ['To show that heuristics usually lead to serious mistakes',
             'To challenge the view that mental shortcuts are simply a flaw',
             'To argue that elaborate calculations are always preferable',
             'To explain why economists rejected psychological research'], 1,
            'Xatboshi F «It would be a mistake … to conclude that human judgement is simply defective» bilan boshlanadi va '
            'oddiy qoidalar ham yaxshi ishlashi mumkinligini aytadi — yaʼni evristikalarni oqlaydi. Qolgan variantlar matnga zid yoki yoʻq.', 5),
         ch('Why does the writer mention the researchers who study biases in paragraph H?',
            ['To praise their contribution to decision-making',
             'To suggest that they are more biased than other people',
             'To show that awareness of biases does not protect people from them',
             'To recommend that everyone should study psychology'], 2,
            '«Were awareness alone sufficient, the researchers … would presumably be free of them, which does not seem to be the case» — '
            'bilish yetarli emasligini isbotlovchi misol.', 7),
         ch('In paragraph C, the example of the reduced price is used to illustrate that',
            ['shoppers rarely compare prices carefully',
             'an earlier figure can influence how a later one is judged',
             'negotiations usually end in agreement',
             'discounts are generally a form of deception'], 1,
            '«a reduced price looks attractive mainly in comparison with the original figure printed beside it» — bu anchoring '
            'misoli: dastlabki raqam keyingi bahoga taʼsir qiladi.', 2),
     ])


# ---------------------------------------------------------------- 12
H12 = ['An overlooked figure in plain view',
       'Why moving between activities has a price',
       'Shaping surroundings to protect concentration',
       'The problem lies in the mind, not the hands',
       'False confidence in what we perceive',
       'Why experts never miss important details',
       'Technology that has finally solved distraction',
       'A brief history of attention research']

text(B, 'c1-12-attention', 'Diqqat va chalgʻish', 'The Limits of Attention', 'C1', 'exam', TAG,
     'Akademik matn: diqqatning chegaralari, «multitasking» haqidagi afsona va diqqatni jamlash uchun muhitni '
     'qanday tashkil qilish haqida. Topshiriqlar: Matching headings, True/False/Not Given, boʻshliq toʻldirish '
     '(NO MORE THAN TWO WORDS) va test savollari. Taxminan 20 daqiqa. Maslahat: boʻshliq toʻldirishda avval kerakli '
     'soʻz turkumini (ot, sifat …) aniqlang, soʻng matndagi parafrazani qidiring; javobni matndan aynan koʻchiring.',
     [
         P("At any given moment, the senses deliver far more information than the brain could possibly process in detail. "
           "The hum of traffic, the pressure of a chair, the movement of leaves at the edge of vision: almost all of it "
           "passes unnoticed. Attention is the set of processes by which some of this information is selected for further "
           "analysis while the rest is filtered out. Far from being a weakness, this selectivity is essential, since a mind "
           "that attended equally to everything would be overwhelmed. Its limits, however, have consequences that most "
           "people consistently underestimate."),
         P("Nowhere is this more evident than in the popular belief in multitasking. When people claim to be doing several "
           "things at once, what is usually happening, at least for tasks that require thought, is rapid switching between "
           "them. Laboratory studies of task switching have shown repeatedly that each shift carries a cost: performance "
           "slows, errors become more frequent, and some time is needed to reconfigure the mind for a new set of rules. "
           "Individually these costs are small, but across a working day in which attention is redirected again and again, "
           "they may add up to a substantial loss of efficiency. Paradoxically, people who habitually multitask do not "
           "necessarily become better at it, and some research suggests that they may even be more easily distracted."),
         P("The practical significance of these limits is especially clear on the road. A number of studies have suggested "
           "that holding a telephone conversation while driving impairs performance even when the phone is used hands-free. "
           "This finding appears counter-intuitive only if one assumes that the problem is a manual one. The real "
           "bottleneck, it seems, lies not in the hands but in the mind: a demanding conversation draws on the same limited "
           "capacity that is needed to monitor the road and to respond to unexpected events. Talking to a passenger may be "
           "less risky, possibly because a passenger can see the traffic and tends to fall silent when conditions become "
           "difficult."),
         P("Perhaps the most striking demonstration of attentional limits comes from research on what is known as "
           "inattentional blindness. In a famous experiment, participants watched a short video in which two teams, one "
           "dressed in white and the other in black, passed basketballs among themselves. Viewers were asked to count the "
           "passes made by the team in white. Midway through the clip, a person wearing a gorilla costume walked into the "
           "middle of the scene, paused to face the camera and walked off again. Remarkably, a large proportion of viewers, "
           "absorbed in their counting, failed to notice the gorilla at all, and many were astonished when the clip was "
           "shown to them a second time."),
         P("What makes such findings unsettling is not merely that we miss things, but that we are generally unaware of "
           "missing them. People tend to assume that anything sufficiently unusual would capture their attention, and this "
           "confidence is precisely what the experiment undermines. Expertise offers less protection than might be "
           "expected: in a later study, many radiologists searching lung scans for signs of disease failed to notice an "
           "image of a gorilla that had been inserted into the scans. Such results have implications well beyond the "
           "laboratory, from the reliability of eyewitness testimony to the design of safety-critical work."),
         P("Modern digital environments place these limited resources under constant pressure. Notifications are, in "
           "effect, designed to capture attention, and each one invites a switch with all its associated costs. Even after "
           "an interruption has ended, thoughts about the unfinished task may linger and interfere with whatever comes "
           "next. It has also been suggested that the mere presence of a smartphone on the desk can reduce the mental "
           "capacity available for other work, although attempts to replicate this finding have produced mixed results, "
           "and it should therefore be treated with caution."),
         P("If attention is limited and easily captured, then relying on willpower alone to stay focused is likely to be an "
           "uphill struggle. A more realistic strategy is to design environments in which distraction is less likely to "
           "arise in the first place. At an individual level, this may involve silencing notifications during periods of "
           "concentrated work, keeping only the materials needed for the current task within reach, and grouping similar "
           "activities such as answering messages into dedicated blocks of time. Organisations, too, can contribute by "
           "protecting periods free from meetings and by questioning the expectation that every message deserves an "
           "immediate reply."),
         P("None of this implies that attention is a fixed quantity that can only be rationed. Its selectivity allows us to "
           "follow a single conversation in a crowded room and to become deeply absorbed in a demanding task. The challenge, "
           "rather, is to recognise that what we notice is always a small and partly arbitrary sample of what is there, and "
           "to arrange our surroundings so that the sample includes what matters most."),
     ],
     [G('selectivity', 'tanlab olish xususiyati'), G('overwhelmed', 'haddan tashqari yuklangan, bosib ketilgan'),
      G('underestimate', 'yetarlicha baholamaslik, kam baholamoq'), G('reconfigure', 'qayta sozlamoq'),
      G('substantial', 'salmoqli, katta'), G('impair', 'yomonlashtirmoq, susaytirmoq'),
      G('counter-intuitive', 'kutilmagan, sogʻlom fikrga zid tuyuladigan'), G('bottleneck', 'tor joy, toʻsiq'),
      G('inattentional blindness', 'diqqat boshqa narsaga band boʻlgani uchun koʻrmaslik (eʼtiborsizlik koʻrligi)'), G('absorbed in', '… ga berilib ketgan'),
      G('unsettling', 'bezovta qiluvchi, xavotirga soladigan'), G('undermine', 'putur yetkazmoq, zaiflashtirmoq'),
      G('eyewitness testimony', 'guvohlik koʻrsatmasi'), G('linger', 'saqlanib qolmoq, ketmay turmoq'),
      G('replicate', 'takrorlamoq, natijani qayta olish'), G('uphill struggle', 'mashaqqatli kurash'),
      G('ration', 'tejab taqsimlamoq')],
     [GN('c58-inversion', 'Inversiya: Nowhere is this more evident than …',
         'Nowhere is this more evident than in the popular belief in multitasking'),
      GN('c16-reporting-passive', 'Majhul nisbatda xabar: It has been suggested that …',
         'It has also been suggested that the mere presence of a smartphone on the desk can reduce the mental capacity available for other work')],
     [
         hd(1, H12, 1, 'Xatboshi B: vazifalar orasida almashish har safar «cost» keltiradi — sekinlashuv va xatolar. '
                       '«has a price» = «carries a cost».'),
         hd(2, H12, 3, 'Xatboshi C: hands-free telefon ham xavfli, chunki «The real bottleneck … lies not in the hands but in the mind».'),
         hd(3, H12, 0, 'Xatboshi D: gorilla kostyumidagi odam sahna oʻrtasidan oʻtsa ham koʻpchilik uni sezmagan — '
                       '«overlooked figure in plain view».'),
         hd(4, H12, 4, 'Xatboshi E: biz nimani oʻtkazib yuborganimizni bilmaymiz va hissiyotimizga ortiqcha ishonamiz — '
                       '«this confidence is precisely what the experiment undermines». «Why experts never miss …» xato: '
                       'radiologlar ham gorillani sezmagan.'),
         tf('The writer regards the brain\'s tendency to filter out information as a design flaw.', 'F',
            '«Far from being a weakness, this selectivity is essential» — muallif buni zaruriy xususiyat deb biladi.', 0, ng=True),
         tf('In the video experiment, viewers who failed to see the gorilla also counted the passes less accurately.', 'NG',
            'Matnda faqat koʻpchilik gorillani sezmagani aytilgan; sanash aniqligi haqida hech narsa yoʻq.', 3),
         tf('Thoughts about an interrupted task can continue to affect performance after the interruption is over.', 'T',
            '«Even after an interruption has ended, thoughts about the unfinished task may linger and interfere with whatever comes next».',
            5, ng=True),
         gap('Research on ___ shows that moving from one activity to another slows people down and leads to more errors.',
             ['task switching'],
             '«Laboratory studies of task switching have shown repeatedly that each shift carries a cost: performance slows, errors become more frequent».',
             1, 2),
         gap('Failing to notice an unexpected object because attention is focused elsewhere is known as ___.',
             ['inattentional blindness'],
             '«research on what is known as inattentional blindness» — keyin gorilla tajribasi shu hodisaga misol qilib keltiriladi.', 3, 2),
         gap('Organisations can help by questioning the assumption that each message requires an ___.',
             ['immediate reply'],
             '«questioning the expectation that every message deserves an immediate reply» — «assumption» = «expectation», '
             '«requires» = «deserves».', 6, 2),
         ch('According to paragraph C, why may talking to a passenger be less risky than a phone conversation?',
            ['Passengers usually talk about less demanding subjects.',
             'The driver does not need to hold anything in his or her hands.',
             'A passenger can see the road and may stop talking when it becomes difficult.',
             'Conversations in a car are generally shorter.'], 2,
            '«possibly because a passenger can see the traffic and tends to fall silent when conditions become difficult». '
            'Ikkinchi variant hands-free telefon uchun ham toʻgʻri, demak farqni tushuntirmaydi.', 2),
         ch('How does the writer present the claim about the presence of a smartphone on a desk?',
            ['As a well-established fact', 'As a finding that should be treated cautiously',
             'As a claim that has been completely disproved', 'As the writer\'s own discovery'], 1,
            '«attempts to replicate this finding have produced mixed results, and it should therefore be treated with caution».', 5),
         ch('What is the main point of the final paragraph?',
            ['Attention can be increased through regular training.',
             'People should avoid crowded places when they need to concentrate.',
             'Selective attention is valuable, but we should organise our surroundings so that we notice what matters.',
             'Most of what we notice is unimportant and can be ignored.'], 2,
            'Muallif selektivlik foydali ekanini («allows us to follow a single conversation …») va muhitni shunday tashkil qilish '
            'kerakligini aytadi: «so that the sample includes what matters most».', 7),
     ])


# ---------------------------------------------------------------- 13
YNNG = ('Fikr-mulohaza matni (opinion essay): muallif empatiyaning foydasi va chegaralari haqida oʻz pozitsiyasini bildiradi. '
        'Bu yerda True/False/Not Given savollari aslida YES / NO / NOT GIVEN vazifasini bajaradi: TRUE = muallif shu fikrda (YES), '
        'FALSE = muallif aksini aytadi (NO), NOT GIVEN = muallifning bu haqdagi fikri nomaʼlum. Shuningdek, Matching headings, '
        'boʻshliq toʻldirish va test savollari bor. Taxminan 20 daqiqa. Maslahat: «I would argue», «I do not intend», '
        '«None of this is to deny» kabi iboralarni belgilab boring — muallif pozitsiyasi aynan shu yerda koʻrinadi.')

H13 = ['A single word covering two different abilities',
       'A narrow beam that favours the familiar',
       'The toll on those who care for others',
       'Caring without sharing the pain',
       'Why empathy should be taught to every child',
       'The inherited basis of empathy',
       'Empathy as the main cause of conflict']

text(B, 'c1-13-empathy', 'Empatiya', 'The Limits of Empathy', 'C1', 'exam', TAG, YNNG,
     [
         P("Empathy enjoys an almost unrivalled reputation. Politicians call for more of it, educators design programmes to "
           "cultivate it, and its absence is often treated as the root of cruelty and indifference. It is difficult to object "
           "to such enthusiasm, and I do not intend to argue that empathy is worthless. I do want to suggest, however, that "
           "the word conceals important distinctions, and that once these are recognised, empathy begins to look like a "
           "less dependable moral guide than its admirers assume."),
         P("Psychologists commonly distinguish between two capacities that the single word tends to blur. Cognitive empathy "
           "is the ability to understand what another person is thinking or feeling, to grasp a situation from their point "
           "of view. Emotional empathy, by contrast, involves actually sharing that feeling, so that another person's "
           "distress produces a corresponding distress in oneself. The two do not necessarily go together. A skilled "
           "negotiator or, more troublingly, a manipulative fraudster may read other people's emotions with great accuracy "
           "while remaining entirely unmoved by them; conversely, someone may be overwhelmed by another's pain without "
           "understanding its causes."),
         P("None of this is to deny that empathy has real value. Understanding others' perspectives makes cooperation, "
           "teaching and the resolution of conflict possible, and feeling moved by another person's suffering can prompt "
           "acts of genuine kindness. In close relationships, the sense of being understood is widely regarded as one of the "
           "foundations of trust. The difficulty arises when empathy, and emotional empathy in particular, is asked to serve "
           "as the basis of moral judgement on a larger scale."),
         P("Here its limitations become apparent. Empathy behaves much like a spotlight: it illuminates whoever happens to "
           "fall within its beam and leaves everyone else in darkness. Research on what has been called the identifiable "
           "victim effect suggests that people are often more willing to help a single named individual whose story they "
           "know than a large group whose suffering is described only in statistical terms. Moreover, empathy appears to "
           "flow more readily towards those who resemble us, whether in appearance, nationality or opinions, and less "
           "readily towards strangers or members of groups we regard as different. A moral guide that is so easily steered "
           "by familiarity and vividness can hardly be described as impartial."),
         P("There is also a cost to the empathiser. Those who work in caring professions such as nursing, medicine and social "
           "work are exposed daily to suffering, and if they were to share fully in every patient's distress, the result "
           "would probably be exhaustion rather than better care. The condition often described as compassion fatigue may, "
           "some researchers have suggested, be more accurately termed empathic distress, since it seems to arise from "
           "absorbing others' pain rather than from caring about them."),
         P("This distinction points towards an alternative. Compassion, as the term is increasingly used by researchers, "
           "refers to feelings of warmth and concern for another person, combined with a motivation to help, without the "
           "requirement to mirror their suffering. Some studies of brief training programmes have reported that practising "
           "compassion was associated with more positive feelings, whereas training focused on sharing others' pain tended "
           "to increase negative ones. These findings come from relatively small samples and should be interpreted "
           "cautiously, yet they are consistent with the intuition that one can care deeply about another person without "
           "being consumed by their distress."),
         P("What this suggests, I would argue, is that sound moral reasoning draws on three elements rather than one. "
           "Cognitive empathy helps us to understand what others actually need; compassion supplies the motivation to act; "
           "and deliberate reflection on fairness corrects for the narrowness of the spotlight. It is this third element "
           "that allows us to ask whether people who have not caught our attention, distant strangers among them, deserve "
           "our concern just as much as those who have."),
         P("To question empathy is not to recommend coldness. Rather, it is to acknowledge that a capacity which may well "
           "have developed to strengthen bonds within close communities may need supplementing when we make decisions that "
           "affect many people we will never meet. Feeling with others is valuable; caring for them wisely may require "
           "something more."),
     ],
     [G('unrivalled', 'tengsiz, raqibsiz'), G('cultivate', 'tarbiyalamoq, rivojlantirmoq'),
      G('indifference', 'befarqlik'), G('conceal', 'yashirmoq, berkitmoq'),
      G('blur', 'xiralashtirmoq, farqini yoʻqotmoq'), G('corresponding', 'mos keladigan, tegishli'),
      G('manipulative', 'manipulyatsiya qiluvchi, ayyor'), G('unmoved', 'taʼsirlanmagan, befarq'),
      G('conversely', 'aksincha, teskari holda'), G('illuminate', 'yoritmoq'),
      G('resemble', '… ga oʻxshamoq'), G('impartial', 'xolis, betaraf'),
      G('exhaustion', 'holdan toyish, charchoq'), G('compassion', 'shafqat, mehr-hamdardlik'),
      G('mirror', 'aks ettirmoq, takrorlamoq'), G('be consumed by', '… ga butunlay berilib ketmoq, yutilmoq'),
      G('supplement', 'toʻldirmoq, qoʻshimcha qilmoq')],
     [GN('c57-cleft-sentences', 'Cleft gaplar: What this suggests … is that …; It is this third element that …',
         'It is this third element that allows us to ask'),
      GN('c36-whoever-whatever', '«whoever» bilan ergash gap: it illuminates whoever happens to …',
         'it illuminates whoever happens to fall within its beam')],
     [
         hd(1, H13, 0, 'Xatboshi B: «empathy» soʻzi ikki xil qobiliyatni — cognitive va emotional empathy — qamrab oladi: '
                       '«two capacities that the single word tends to blur».'),
         hd(3, H13, 1, 'Xatboshi D: empatiya «spotlight» kabi faqat nur tushgan joyni yoritadi va oʻzimizga oʻxshaganlarga '
                       'koʻproq yoʻnaladi — «narrow beam that favours the familiar».'),
         hd(4, H13, 2, 'Xatboshi E: gʻamxoʻrlik kasblaridagilar uchun narx — «There is also a cost to the empathiser», '
                       '«exhaustion». «toll» = zarar, yoʻqotish.'),
         hd(5, H13, 3, 'Xatboshi F: compassion — gʻamxoʻrlik va yordam istagi, lekin azobni «mirror» qilmasdan. '
                       '«without the requirement to mirror their suffering».'),
         tf('Empathy has no genuine value.', 'F',
            'NO: «I do not intend to argue that empathy is worthless» va «None of this is to deny that empathy has real value».', 0, ng=True),
         tf('Cognitive and emotional empathy always occur together.', 'F',
            'NO: «The two do not necessarily go together» — firibgar misoli buni koʻrsatadi.', 1, ng=True),
         tf('Moral decisions that affect large groups should not be based mainly on emotional empathy.', 'T',
            'YES: «The difficulty arises when … emotional empathy in particular, is asked to serve as the basis of moral judgement '
            'on a larger scale», keyin esa uning xolis emasligi isbotlanadi.', 2, ng=True),
         tf('Empathy training programmes in schools should be made compulsory.', 'NG',
            'NOT GIVEN: kirish qismida pedagoglar empatiyani rivojlantirish dasturlarini tuzishi aytilgan, lekin muallif ularni '
            'majburiy qilish haqida hech qanday fikr bildirmaydi.', 0),
         gap('People are often more generous towards one named person than towards many victims described in ___ terms.',
             ['statistical'],
             '«a large group whose suffering is described only in statistical terms».', 3, 2),
         gap("According to some researchers, the exhaustion experienced by carers comes from absorbing others' pain rather than from ___ them.",
             ['caring about'],
             "«since it seems to arise from absorbing others' pain rather than from caring about them».", 4, 2),
         ch('What does the writer use the example of the fraudster to show?',
            ['That most people misunderstand the emotions of others',
             'That understanding someone\'s feelings does not guarantee concern for them',
             'That emotional empathy is more dangerous than cognitive empathy',
             'That negotiators should be trained in empathy'], 1,
            'Firibgar boshqalarning his-tuygʻularini aniq oʻqiydi «while remaining entirely unmoved by them» — yaʼni cognitive '
            'empathy bor, lekin gʻamxoʻrlik yoʻq.', 1),
         ch('How does the writer regard the findings on compassion training?',
            ['As conclusive proof that compassion is superior',
             'As irrelevant to the argument',
             'As encouraging but limited because of small samples',
             'As contradicting the idea of empathic distress'], 2,
            '«These findings come from relatively small samples and should be interpreted cautiously, yet they are consistent with …» — '
            'ehtiyotkor, lekin ijobiy baho.', 5),
         ch('Which of the following best describes the writer\'s overall position in the final paragraph?',
            ['Empathy should be replaced by strict rules.',
             'Empathy is harmful and should be discouraged.',
             'Empathy is valuable but not sufficient on its own for wise decisions.',
             'Empathy is only useful within close communities.'], 2,
            '«To question empathy is not to recommend coldness … Feeling with others is valuable; caring for them wisely may require '
            'something more».', 7),
     ])


# ---------------------------------------------------------------- 14
H14 = ['An experiment in which a prize reduced enthusiasm',
       'Three needs that underlie lasting motivation',
       'When outside pressure becomes personal commitment',
       'Defining two sources of motivation',
       'A more complicated pattern than first assumed',
       'Why money is the most effective incentive',
       'The decline of volunteering in modern society',
       'How young children learn to draw']

text(B, 'c1-14-motivation', 'Motivatsiya', 'What Drives Us', 'C1', 'exam', TAG,
     'Akademik matn: ichki va tashqi motivatsiya, mukofot qiziqishni qanday susaytirishi mumkinligi va '
     '«self-determination theory» haqida. Topshiriqlar: Matching headings, True/False/Not Given, boʻshliq toʻldirish va '
     'test savollari, jumladan «reference» savoli (olmosh nimaga ishora qilishini topish). Taxminan 20 daqiqa. '
     'Maslahat: olmosh soʻralganda oldingi gapni oʻqing — ishora qilingan ot odatda yaqin joyda turadi.',
     [
         P("Why do people spend hours on activities that earn them nothing? Amateur musicians practise scales late into the "
           "evening, volunteers maintain hiking trails at weekends, and countless contributors write and correct entries in "
           "online encyclopedias without payment or public credit. Such behaviour sits uneasily with the assumption, common "
           "in both economics and everyday management, that people work chiefly in response to rewards and punishments. "
           "Psychologists have long sought to account for it by distinguishing between two broad kinds of motivation."),
         P("Intrinsic motivation refers to doing something because it is inherently interesting or satisfying: the activity "
           "is, in effect, its own reward. Extrinsic motivation, by contrast, refers to doing something in order to obtain an "
           "outcome that is separable from the activity itself, whether a salary, a grade, praise or the avoidance of a "
           "penalty. Most real activities involve a mixture of the two, and neither is automatically superior. Nevertheless, "
           "the distinction has proved valuable, not least because it draws attention to the possibility that the two forms "
           "of motivation may interact in unexpected ways."),
         P("The most provocative evidence for such interaction comes from research on what is called the overjustification "
           "effect. In a classic study conducted in the early 1970s, nursery-school children who already showed an interest "
           "in drawing were divided into groups. Some were told in advance that they would receive a certificate for "
           "drawing, others received the same reward unexpectedly, and others received nothing. When the children were "
           "later observed during free play, those who had expected and received the reward spent less time drawing than "
           "the other children did. The reward, it seemed, had transformed an enjoyable pastime into something done for a "
           "prize."),
         P("Subsequent research has shown that the picture is considerably more nuanced than the most dramatic "
           "interpretations suggest. Rewards appear most likely to undermine interest when they are expected, tangible and "
           "dependent simply on doing the task, and when the activity was enjoyable to begin with. Verbal feedback that "
           "conveys information about competence, by contrast, may sustain or even enhance interest, and rewards for tasks "
           "that people find tedious are unlikely to destroy an enthusiasm that never existed. Reviews combining the results "
           "of many studies have reached somewhat different conclusions about the size and generality of the effect, and the "
           "debate has not been entirely resolved."),
         P("Why should a reward ever reduce interest? One influential answer is offered by self-determination theory, which "
           "has been developed over several decades. According to this framework, people have three basic psychological "
           "needs: autonomy, the sense that one's actions are self-endorsed rather than imposed; competence, the experience "
           "of acting effectively; and relatedness, the feeling of being connected to and cared for by others. Rewards and "
           "other external pressures are thought to undermine intrinsic motivation chiefly when they are experienced as "
           "controlling, since they then shift the perceived reason for acting from within the person to outside."),
         P("The implications for schools and workplaces are considerable. Environments that rely heavily on surveillance, "
           "deadlines imposed without explanation and rewards made contingent on narrow targets risk producing compliance "
           "rather than engagement. Teachers and managers who offer meaningful choices, explain the reasons behind requests "
           "and acknowledge the perspectives of those they supervise are, according to this research, more likely to foster "
           "lasting motivation. This does not mean abandoning structure; rather, it means providing structure in a way that "
           "supports, instead of overriding, a person's sense of agency."),
         P("It would be misleading, however, to present extrinsic motivation as inherently harmful. Self-determination theory "
           "itself describes a continuum along which externally prompted behaviour can gradually become internalised. A "
           "student who initially revises only to pass an examination may come to value the subject for its own sake, or at "
           "least to recognise its personal importance; a nurse who follows hygiene procedures because they are required "
           "may, over time, follow them because she understands why they matter. Such internalised motivation, though not "
           "strictly intrinsic, appears to be far more durable than behaviour sustained only by external pressure."),
         P("Rewards, in short, are neither a universal solution nor an inevitable threat. Their effect depends on what they "
           "communicate: whether they are perceived as an attempt to control or as recognition of genuine achievement. Those "
           "who wish to motivate others might therefore do well to ask not only what incentives to offer, but whether the "
           "conditions they create allow people to feel capable, connected and, above all, the authors of their own actions."),
     ],
     [G('sit uneasily with', '… ga yaxshi mos kelmaslik, ziddek tuyulmoq'), G('inherently', 'tabiatan, oʻz-oʻzidan'),
      G('separable', 'ajratib boʻladigan'), G('superior', 'ustun, afzal'),
      G('provocative', 'bahs uygʻotuvchi, oʻylantiradigan'), G('pastime', 'ermak, boʻsh vaqt mashgʻuloti'),
      G('nuanced', 'nozik farqlarga ega, murakkab'), G('tangible', 'moddiy, qoʻl bilan ushlab boʻladigan'),
      G('tedious', 'zerikarli, bir xil'), G('autonomy', 'mustaqillik, avtonomiya'),
      G('self-endorsed', 'oʻzi maʼqullagan, ichki rozilik bilan'), G('contingent on', '… ga bogʻliq, … sharti bilan'),
      G('compliance', 'boʻysunish, talabni bajarish'), G('foster', 'rivojlantirmoq, qoʻllab-quvvatlamoq'),
      G('override', 'bosib ketmoq, ustidan oʻtmoq'), G('internalise', 'oʻzlashtirmoq, ichki qadriyatga aylantirmoq'),
      G('durable', 'barqaror, uzoq davom etadigan'), G('incentive', 'ragʻbat, ragʻbatlantiruvchi omil')],
     [GN('c14-complex-passive', 'Murakkab majhul: are thought to undermine',
         'Rewards and other external pressures are thought to undermine intrinsic motivation chiefly when they are experienced as controlling'),
      GN('c46-contrast-concession', 'Toʻsiqsiz ergash (qisqargan): though not strictly intrinsic',
         'Such internalised motivation, though not strictly intrinsic, appears to be far more durable')],
     [
         hd(1, H14, 3, 'Xatboshi B: intrinsic va extrinsic motivatsiyaning taʼriflari beriladi — «Defining two sources of motivation».'),
         hd(2, H14, 0, 'Xatboshi C: sertifikat kutgan bolalar keyin kamroq rasm chizgan — mukofot qiziqishni pasaytirgan. '
                       '«How young children learn to draw» tuzoq: «drawing» soʻzi bor, lekin asosiy fikr emas.'),
         hd(3, H14, 4, 'Xatboshi D: «the picture is considerably more nuanced than the most dramatic interpretations suggest» — '
                       'manzara dastlab oʻylangandan murakkabroq.'),
         hd(6, H14, 2, 'Xatboshi G: tashqi turtki bilan boshlangan xatti-harakat asta-sekin ichki qadriyatga aylanishi — '
                       '«externally prompted behaviour can gradually become internalised».'),
         tf('In the classic study, children who received a reward unexpectedly drew less afterwards than children who had been promised one.', 'F',
            'Matnga koʻra kamroq chizganlar aynan mukofotni oldindan kutganlar edi: «those who had expected and received the reward '
            'spent less time drawing than the other children did».', 2, ng=True),
         tf('The certificates in the classic study were chosen by the children\'s parents.', 'NG',
            'Sertifikat haqida faqat u mukofot boʻlgani aytilgan; uni kim tanlagani haqida maʼlumot yoʻq.', 2),
         tf('Researchers now fully agree on how large and widespread the overjustification effect is.', 'F',
            '«Reviews … have reached somewhat different conclusions about the size and generality of the effect, and the debate has not '
            'been entirely resolved».', 3, ng=True),
         tf('According to self-determination theory, rewards are most damaging to interest when people experience them as controlling.', 'T',
            '«are thought to undermine intrinsic motivation chiefly when they are experienced as controlling» — «damaging» = «undermine».',
            4, ng=True),
         gap('Verbal feedback that gives information about ___ may help to maintain people\'s interest.',
             ['competence'],
             '«Verbal feedback that conveys information about competence … may sustain or even enhance interest» — «maintain» = «sustain».',
             3, 2),
         gap('Environments built on surveillance and narrow targets may result in ___ rather than genuine engagement.',
             ['compliance'],
             '«risk producing compliance rather than engagement».', 5, 2),
         gap('Self-determination theory describes a ___ along which behaviour first prompted from outside can become internalised.',
             ['continuum'],
             '«describes a continuum along which externally prompted behaviour can gradually become internalised».', 6, 2),
         ch('Why does the writer mention amateur musicians and volunteers in paragraph A?',
            ['To show that unpaid work is becoming more common',
             'To illustrate behaviour that is difficult to explain by rewards alone',
             'To argue that economists have ignored music',
             'To prove that people dislike being paid'], 1,
            'Bu misollardan keyin: «Such behaviour sits uneasily with the assumption … that people work chiefly in response to rewards '
            'and punishments».', 0),
         ch('What does the writer say about structure in schools and workplaces?',
            ['It should be removed to increase freedom.',
             'It matters less than rewards.',
             'It should be provided in a way that supports people\'s sense of agency.',
             'It is the main cause of low motivation.'], 2,
            '«This does not mean abandoning structure; rather, it means providing structure in a way that supports … a person\'s sense of agency».', 5),
         ch('In paragraph H, the word «Their» in «Their effect depends on what they communicate» refers to',
            ['people', 'rewards', 'actions', 'conditions'], 1,
            'Oldingi gap: «Rewards, in short, are neither a universal solution nor an inevitable threat» — «Their» = rewards.', 7),
     ])


# ---------------------------------------------------------------- 15
H15 = ['A simple task with a hidden twist',
       'Factors that weakened or strengthened yielding',
       'Two motives for going along with others',
       'Results that depend on when and where',
       'A neglected aspect of a famous study',
       'How a persistent few can shift opinion',
       'Why conformity has disappeared from modern societies',
       'The danger of trusting one\'s own eyes']

text(B, 'c1-15-conformity', 'Guruh bosimi', 'The Pressure to Conform', 'C1', 'exam', TAG,
     'Akademik matn: konformizm — guruhga moslashish, Asch tajribalari, ularning turli mamlakat va davrlarda takrorlanishi '
     'hamda ozchilik taʼsiri haqida. Topshiriqlar: Matching headings, True/False/Not Given, boʻshliq toʻldirish va test '
     'savollari. Taxminan 20 daqiqa. Maslahat: «some», «many», «the majority», «never» kabi miqdor soʻzlariga alohida eʼtibor '
     'bering — TFNG savollarida javob koʻpincha aynan shularga bogʻliq.',
     [
         P("Human beings are profoundly social animals, and much of what we believe and do is shaped, often without our "
           "noticing, by the people around us. Psychologists use the term conformity to describe the tendency to adjust "
           "one's behaviour or judgements so that they match those of a group. In many situations this tendency is entirely "
           "sensible: following local customs, queuing in an orderly manner or adopting the vocabulary of a new workplace "
           "all make social life smoother. The question that has fascinated researchers is how far it extends, and in "
           "particular whether people will conform even when the group is plainly wrong."),
         P("The best-known attempt to answer this question was a series of experiments conducted in the United States in the "
           "early 1950s by the psychologist Solomon Asch. Participants were told that they were taking part in a study of "
           "visual perception. Seated with a group of other people, they were shown a single standard line together with "
           "three comparison lines and asked to state aloud which of the comparison lines matched the standard in length. "
           "The task was so straightforward that people judging alone almost never made mistakes. Unknown to the genuine "
           "participant, however, all the other members of the group were working with the experimenter, and on certain "
           "trials they unanimously gave the same obviously incorrect answer. The participant, seated so as to respond near "
           "the end, was thus confronted with a clear choice between the evidence of his own eyes and the verdict of the "
           "majority."),
         P("The results have been widely cited, and sometimes exaggerated. A substantial proportion of participants went "
           "along with the incorrect majority on at least some trials, and some yielded repeatedly. Yet the majority of "
           "responses overall remained correct, and a considerable number of participants never conformed at all. Asch also "
           "varied the conditions in revealing ways. When just one other group member departed from the majority and gave "
           "the correct answer, conformity fell sharply. When participants were allowed to write down their answers rather "
           "than announce them publicly, it also declined. Enlarging the unanimous majority raised conformity at first, but "
           "beyond a fairly small group, adding further members appeared to make little difference."),
         P("Researchers have generally distinguished two reasons why people conform. Normative influence reflects the desire "
           "to be accepted and to avoid the discomfort of standing out; it is consistent with the finding that conformity "
           "diminishes when answers are given in private. Informational influence, by contrast, arises when people treat the "
           "behaviour of others as evidence about what is true, particularly when a situation is ambiguous. Interestingly, "
           "when Asch questioned his participants afterwards, some reported that they had begun to doubt their own "
           "judgement, suggesting that even in an apparently unambiguous task the two forms of influence may operate "
           "together."),
         P("Later attempts to repeat the procedure have produced results that vary considerably across time and place. One "
           "study carried out with British students around 1980 found very little conformity, leading its authors to "
           "suggest that Asch's findings might reflect the particular climate of 1950s America. A large review combining "
           "studies from many countries suggested that conformity tended to be higher in societies that place greater "
           "emphasis on collective goals than on individual independence, and that in the United States it appeared to have "
           "declined since the original experiments. Such comparisons must be interpreted with care, however, since "
           "participants, procedures and even the meaning of agreeing with others may differ from one setting to another: "
           "what looks like weakness in one culture may be understood as tact or sensitivity in another."),
         P("It is also worth recalling that Asch himself did not regard his findings simply as evidence of human weakness. He "
           "appears to have been at least as interested in the participants who resisted the group as in those who yielded, "
           "and some scholars have argued that textbook accounts, by concentrating on conformity, have presented a "
           "one-sided picture of his work."),
         P("If majorities can sway individuals, can a minority ever change the majority? Research begun in Europe in the late "
           "1960s suggests that it can, provided that the minority is consistent. In one well-known experiment, participants "
           "were shown a series of blue slides; when a small number of confederates consistently described the slides as "
           "green, some participants also began to call them green, whereas an inconsistent minority had little effect. "
           "Minority influence of this kind tends to operate more slowly than majority pressure and often produces private "
           "reconsideration rather than immediate public agreement."),
         P("Taken together, this body of research suggests that conformity is neither a simple flaw nor a fixed trait. It is "
           "a response to social circumstances, one that can be strengthened by unanimity and public scrutiny and weakened "
           "by a single dissenting voice. Few findings are more encouraging than this last one, for it implies that the "
           "willingness of one person to speak honestly may make it considerably easier for others to do the same."),
     ],
     [G('profoundly', 'chuqur, juda kuchli darajada'), G('conformity', 'konformizm, guruhga moslashish'),
      G('plainly', 'aniq-ravshan, ochiq-oydin'), G('unanimously', 'yakdillik bilan, bir ovozdan'),
      G('be confronted with', '… ga roʻpara boʻlmoq, duch kelmoq'), G('verdict', 'hukm, qaror'),
      G('exaggerate', 'boʻrttirmoq, oshirib yubormoq'), G('yield', 'yon bermoq, boʻysunmoq'),
      G('diminish', 'kamaymoq, susaymoq'), G('ambiguous', 'noaniq, ikki maʼnoli'),
      G('emphasis on', '… ga urgʻu, eʼtibor'), G('tact', 'odob-nazokat, ehtiyotkorlik'),
      G('one-sided', 'bir tomonlama'), G('sway', 'taʼsir qilib fikrini oʻzgartirmoq'),
      G('confederate', 'tajribachining yashirin yordamchisi'), G('dissenting', 'norozi, boshqacha fikrdagi'),
      G('scrutiny', 'nazorat, sinchkov kuzatuv')],
     [GN('c34-participle-clauses', 'Sifatdosh oborot: Seated with a group of other people, …',
         'Seated with a group of other people, they were shown a single standard line'),
      GN('c51-supposing-provided', 'Shart bogʻlovchisi: provided that …',
         'it can, provided that the minority is consistent')],
     [
         hd(1, H15, 0, 'Xatboshi B: chiziqlarni solishtirish oson vazifa, lekin boshqa ishtirokchilar yashirincha tajribachi bilan '
                       'ishlagan — «hidden twist». «The danger of trusting one\'s own eyes» tuzoq: matn bunday xulosa qilmaydi.'),
         hd(3, H15, 2, 'Xatboshi D: konformizmning ikki sababi — normative va informational influence. «motives» = «reasons».'),
         hd(4, H15, 3, 'Xatboshi E: takroriy tadqiqotlar natijalari «vary considerably across time and place».'),
         hd(6, H15, 5, 'Xatboshi G: izchil ozchilik koʻpchilik fikriga taʼsir qila oladi — «provided that the minority is consistent». '
                       '«persistent» = «consistent».'),
         tf('In Asch\'s experiments, people who judged the lines on their own rarely made errors.', 'T',
            '«The task was so straightforward that people judging alone almost never made mistakes» — «rarely» = «almost never».', 1, ng=True),
         tf('Most of the answers given by participants in Asch\'s experiments were wrong.', 'F',
            '«Yet the majority of responses overall remained correct».', 2, ng=True),
         tf('Participants who had conformed felt embarrassed when the true purpose of the study was explained to them.', 'NG',
            'Asch ishtirokchilarni keyin soʻroq qilgani va baʼzilari oʻz fikriga shubha qilgani aytilgan, lekin ularning uyalgani '
            'haqida maʼlumot yoʻq.', 3),
         tf('In the slide experiment, an inconsistent minority was just as influential as a consistent one.', 'F',
            '«whereas an inconsistent minority had little effect».', 6, ng=True),
         gap('In one variation, conformity fell when participants were allowed to ___ their answers instead of saying them aloud.',
             ['write down'],
             '«When participants were allowed to write down their answers rather than announce them publicly, it also declined».', 2, 2),
         gap('When people treat the behaviour of others as evidence about what is true, this is known as ___ influence.',
             ['informational'],
             '«Informational influence, by contrast, arises when people treat the behaviour of others as evidence about what is true».', 3, 2),
         ch('What does the writer say about comparisons of conformity between cultures?',
            ['They prove that some nations are weaker than others.',
             'They should be interpreted cautiously because settings and meanings differ.',
             'They show that conformity is the same everywhere.',
             'They are less reliable than Asch\'s original experiments.'], 1,
            '«Such comparisons must be interpreted with care … since participants, procedures and even the meaning of agreeing with '
            'others may differ».', 4),
         ch('According to paragraph F, some scholars believe that textbook accounts of Asch\'s work',
            ['have exaggerated the number of participants',
             'have focused too much on conformity and too little on resistance',
             'have ignored the role of the experimenter',
             'have misreported the dates of the experiments'], 1,
            '«textbook accounts, by concentrating on conformity, have presented a one-sided picture of his work»; Asch esa '
            '«at least as interested in the participants who resisted».', 5),
         ch('Why does the writer find the final finding encouraging?',
            ['It shows that majorities are usually right.',
             'It suggests that one honest voice can make it easier for others to resist pressure.',
             'It proves that conformity is a fixed trait.',
             'It means that public scrutiny always reduces conformity.'], 1,
            '«the willingness of one person to speak honestly may make it considerably easier for others to do the same». '
            'Toʻrtinchi variant xato: matnda public scrutiny konformizmni kuchaytiradi deyilgan.', 7),
     ])
