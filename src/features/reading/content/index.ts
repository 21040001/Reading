/**
 * İçerik kataloğu: kitaplar (seviyeler) → bölümler → metinler.
 * Yeni metin eklemek:
 *   1. scripts/content/<seviye>_u<n>.py içinde text(...) yazın, çalıştırın → data/<kitap>/<id>.json
 *   2. Aşağıda import edip TEXT_LIST'e ve ilgili bölümün `texts` listesine ekleyin
 *      (aynı adı `planned` listesinden silin).
 */
import type { Book, ReadingText } from './types';

import a1_01 from './data/a1/a1-01-dilnoza.json';
import a1_02 from './data/a1/a1-02-family.json';
import a1_03 from './data/a1/a1-03-flat.json';
import a1_04 from './data/a1/a1-04-friend.json';
import a1_05 from './data/a1/a1-05-trip.json';
import a1_06 from './data/a1/a1-06-morning.json';
import a1_07 from './data/a1/a1-07-bazaar.json';
import a1_08 from './data/a1/a1-08-weekend.json';
import a1_09 from './data/a1/a1-09-weather.json';
import a1_10 from './data/a1/a1-10-food.json';
import a1_11 from './data/a1/a1-11-metro.json';
import a1_12 from './data/a1/a1-12-library.json';
import a1_13 from './data/a1/a1-13-neighbour.json';
import a1_14 from './data/a1/a1-14-post.json';
import a1_15 from './data/a1/a1-15-park.json';
import a1_16 from './data/a1/a1-16-football.json';
import a1_17 from './data/a1/a1-17-cinema.json';
import a1_18 from './data/a1/a1-18-hobby.json';
import a1_19 from './data/a1/a1-19-birthday.json';
import a1_20 from './data/a1/a1-20-apps.json';
import a1_21 from './data/a1/a1-21-train.json';
import a1_22 from './data/a1/a1-22-hotel.json';
import a1_23 from './data/a1/a1-23-charvak.json';
import a1_24 from './data/a1/a1-24-letter.json';
import a1_25 from './data/a1/a1-25-lost-bag.json';
import a1_26 from './data/a1/a1-26-grandma.json';
import a1_27 from './data/a1/a1-27-doctor.json';
import a1_28 from './data/a1/a1-28-chef.json';
import a1_29 from './data/a1/a1-29-coach.json';
import a1_30 from './data/a1/a1-30-new-student.json';
import a2_01 from './data/a2/a2-01-then-now.json';
import a2_02 from './data/a2/a2-02-morning-habits.json';
import a2_03 from './data/a2/a2-03-no-phone.json';
import a2_04 from './data/a2/a2-04-new-school.json';
import a2_05 from './data/a2/a2-05-grandpa.json';
import a2_06 from './data/a2/a2-06-unforgettable.json';
import a2_07 from './data/a2/a2-07-rain-trip.json';
import a2_08 from './data/a2/a2-08-lost-key.json';
import a2_09 from './data/a2/a2-09-first-job.json';
import a2_10 from './data/a2/a2-10-old-tale.json';
import a2_11 from './data/a2/a2-11-navruz.json';
import a2_12 from './data/a2/a2-12-wedding.json';
import a2_13 from './data/a2/a2-13-hayit.json';
import a2_14 from './data/a2/a2-14-new-year.json';
import a2_15 from './data/a2/a2-15-world-holidays.json';
import a2_16 from './data/a2/a2-16-job-ad.json';
import a2_17 from './data/a2/a2-17-university.json';
import a2_18 from './data/a2/a2-18-summer-job.json';
import a2_19 from './data/a2/a2-19-online-course.json';
import a2_20 from './data/a2/a2-20-interview.json';
import a2_21 from './data/a2/a2-21-doctor-advice.json';
import a2_22 from './data/a2/a2-22-marathon.json';
import a2_23 from './data/a2/a2-23-breakfast.json';
import a2_24 from './data/a2/a2-24-sleep.json';
import a2_25 from './data/a2/a2-25-kurash.json';
import a2_26 from './data/a2/a2-26-phone-rules.json';
import a2_27 from './data/a2/a2-27-online-shopping.json';
import a2_28 from './data/a2/a2-28-robot-vacuum.json';
import a2_29 from './data/a2/a2-29-social-media.json';
import a2_30 from './data/a2/a2-30-future-city.json';
import b1_01 from './data/b1/b1-01-study-abroad.json';
import b1_02 from './data/b1/b1-02-mountain.json';
import b1_03 from './data/b1/b1-03-two-languages.json';
import b1_04 from './data/b1/b1-04-career-change.json';
import b1_05 from './data/b1/b1-05-volunteer.json';
import b1_06 from './data/b1/b1-06-blue-sky.json';
import b1_07 from './data/b1/b1-07-bees.json';
import b1_08 from './data/b1/b1-08-sleep-memory.json';
import b1_09 from './data/b1/b1-09-groundwater.json';
import b1_10 from './data/b1/b1-10-solar.json';
import b1_11 from './data/b1/b1-11-silk-road.json';
import b1_12 from './data/b1/b1-12-navoi.json';
import b1_13 from './data/b1/b1-13-ibn-sino.json';
import b1_14 from './data/b1/b1-14-khiva.json';
import b1_15 from './data/b1/b1-15-suzani.json';
import b1_16 from './data/b1/b1-16-plastic.json';
import b1_17 from './data/b1/b1-17-city-parks.json';
import b1_18 from './data/b1/b1-18-saving-water.json';
import b1_19 from './data/b1/b1-19-snow-leopard.json';
import b1_20 from './data/b1/b1-20-climate-farming.json';
import b1_21 from './data/b1/b1-21-formal-letter.json';
import b1_22 from './data/b1/b1-22-cv.json';
import b1_23 from './data/b1/b1-23-remote-work.json';
import b1_24 from './data/b1/b1-24-startup.json';
import b1_25 from './data/b1/b1-25-workplace.json';
import b1_26 from './data/b1/b1-26-fake-news.json';
import b1_27 from './data/b1/b1-27-advertising.json';
import b1_28 from './data/b1/b1-28-podcasts.json';
import b1_29 from './data/b1/b1-29-film-review.json';
import b1_30 from './data/b1/b1-30-screen-time.json';
import b2_01 from './data/b2/b2-01-aral.json';
import b2_02 from './data/b2/b2-02-ulugh-beg.json';
import b2_03 from './data/b2/b2-03-silkworm.json';
import b2_04 from './data/b2/b2-04-online-learning.json';
import b2_05 from './data/b2/b2-05-city-transport.json';
import b2_06 from './data/b2/b2-06-tea.json';
import b2_07 from './data/b2/b2-07-bilingual-brain.json';
import b2_08 from './data/b2/b2-08-desert-plants.json';
import b2_09 from './data/b2/b2-09-food-waste.json';
import b2_10 from './data/b2/b2-10-city-noise.json';
import b2_11 from './data/b2/b2-11-cotton.json';
import b2_12 from './data/b2/b2-12-museums.json';
import b2_13 from './data/b2/b2-13-insomnia.json';
import b2_14 from './data/b2/b2-14-architecture.json';
import b2_15 from './data/b2/b2-15-ai-work.json';
import b2_16 from './data/b2/b2-16-sardoba.json';
import b2_17 from './data/b2/b2-17-honey.json';
import b2_18 from './data/b2/b2-18-cycling-cities.json';
import b2_19 from './data/b2/b2-19-language-learning.json';
import b2_20 from './data/b2/b2-20-earthquakes.json';
import b2_21 from './data/b2/b2-21-homework.json';
import b2_22 from './data/b2/b2-22-tourism.json';
import b2_23 from './data/b2/b2-23-teens-social.json';
import b2_24 from './data/b2/b2-24-city-village.json';
import b2_25 from './data/b2/b2-25-books-screens.json';
import b2_26 from './data/b2/b2-26-test1.json';
import b2_27 from './data/b2/b2-27-test2.json';
import b2_28 from './data/b2/b2-28-test3.json';
import b2_29 from './data/b2/b2-29-test4.json';
import b2_30 from './data/b2/b2-30-test5.json';

import c1_01 from './data/c1/c1-01-microbiome.json';
import c1_02 from './data/c1/c1-02-memory.json';
import c1_03 from './data/c1/c1-03-quantum.json';
import c1_04 from './data/c1/c1-04-deep-ocean.json';
import c1_05 from './data/c1/c1-05-placebo.json';
import c1_06 from './data/c1/c1-06-remittances.json';
import c1_07 from './data/c1/c1-07-urbanisation.json';
import c1_08 from './data/c1/c1-08-four-day-week.json';
import c1_09 from './data/c1/c1-09-cooperatives.json';
import c1_10 from './data/c1/c1-10-inequality.json';
import c1_11 from './data/c1/c1-11-decisions.json';
import c1_12 from './data/c1/c1-12-attention.json';
import c1_13 from './data/c1/c1-13-empathy.json';
import c1_14 from './data/c1/c1-14-motivation.json';
import c1_15 from './data/c1/c1-15-conformity.json';
import c1_16 from './data/c1/c1-16-free-museums.json';
import c1_17 from './data/c1/c1-17-automation.json';
import c1_18 from './data/c1/c1-18-language-identity.json';
import c1_19 from './data/c1/c1-19-sport-money.json';
import c1_20 from './data/c1/c1-20-university-rankings.json';
import c1_21 from './data/c1/c1-21-qodiriy.json';
import c1_22 from './data/c1/c1-22-translation.json';
import c1_23 from './data/c1/c1-23-fairy-tales.json';
import c1_24 from './data/c1/c1-24-babur.json';
import c1_25 from './data/c1/c1-25-history-reading.json';
import c1_26 from './data/c1/c1-26-test1.json';
import c1_27 from './data/c1/c1-27-test2.json';
import c1_28 from './data/c1/c1-28-test3.json';
import c1_29 from './data/c1/c1-29-test4.json';
import c1_30 from './data/c1/c1-30-test5.json';
export const TEXT_LIST = [
  a1_01, a1_02, a1_03, a1_04, a1_05,
  a1_06, a1_07, a1_08, a1_09, a1_10, a1_11, a1_12, a1_13, a1_14, a1_15, a1_16, a1_17, a1_18, a1_19, a1_20, a1_21, a1_22, a1_23, a1_24, a1_25, a1_26, a1_27, a1_28, a1_29, a1_30,
  a2_01, a2_02, a2_03, a2_04, a2_05, a2_06, a2_07, a2_08, a2_09, a2_10, a2_11, a2_12, a2_13, a2_14, a2_15, a2_16, a2_17, a2_18, a2_19, a2_20, a2_21, a2_22, a2_23, a2_24, a2_25, a2_26, a2_27, a2_28, a2_29, a2_30,
  b1_01, b1_02, b1_03, b1_04, b1_05, b1_06, b1_07, b1_08, b1_09, b1_10, b1_11, b1_12, b1_13, b1_14, b1_15, b1_16, b1_17, b1_18, b1_19, b1_20, b1_21, b1_22, b1_23, b1_24, b1_25, b1_26, b1_27, b1_28, b1_29, b1_30,
  b2_01, b2_02, b2_03, b2_04, b2_05, b2_06, b2_07, b2_08, b2_09, b2_10, b2_11, b2_12, b2_13, b2_14, b2_15, b2_16, b2_17, b2_18, b2_19, b2_20, b2_21, b2_22, b2_23, b2_24, b2_25, b2_26, b2_27, b2_28, b2_29, b2_30,
  c1_01, c1_02, c1_03, c1_04, c1_05, c1_06, c1_07, c1_08, c1_09, c1_10, c1_11, c1_12, c1_13, c1_14, c1_15, c1_16, c1_17, c1_18, c1_19, c1_20, c1_21, c1_22, c1_23, c1_24, c1_25, c1_26, c1_27, c1_28, c1_29, c1_30,
] as ReadingText[];

export const TEXTS: Record<string, ReadingText> = Object.fromEntries(TEXT_LIST.map(t => [t.id, t]));

const p = (uz: string, en?: string) => ({ uz, en });

export const BOOKS: Book[] = [
  {
    id: 'a1',
    level: 'A1',
    focus: 'general',
    color: 'success',
    title: p('Boshlangʻich', 'Beginner'),
    subtitle: p('Qisqa va sodda matnlar (60–120 soʻz), har bir xatboshining tarjimasi bilan', 'Short, simple texts with a translation of every paragraph'),
    units: [
      {
        id: 'a1-u1',
        title: p('Men va oilam', 'Me and my family'),
        texts: ['a1-01-dilnoza', 'a1-02-family', 'a1-03-flat', 'a1-04-friend', 'a1-05-trip'],
      },
      {
        id: 'a1-u2',
        title: p('Kundalik hayot', 'Daily life'),
        texts: ['a1-06-morning', 'a1-07-bazaar', 'a1-08-weekend', 'a1-09-weather', 'a1-10-food'],
      },
      {
        id: 'a1-u3',
        title: p('Shahrim', 'My city'),
        texts: ['a1-11-metro', 'a1-12-library', 'a1-13-neighbour', 'a1-14-post', 'a1-15-park'],
      },
      {
        id: 'a1-u4',
        title: p('Boʻsh vaqt', 'Free time'),
        texts: ['a1-16-football', 'a1-17-cinema', 'a1-18-hobby', 'a1-19-birthday', 'a1-20-apps'],
      },
      {
        id: 'a1-u5',
        title: p('Sayohat', 'Travel'),
        texts: ['a1-21-train', 'a1-22-hotel', 'a1-23-charvak', 'a1-24-letter', 'a1-25-lost-bag'],
      },
      {
        id: 'a1-u6',
        title: p('Odamlar va kasblar', 'People and jobs'),
        texts: ['a1-26-grandma', 'a1-27-doctor', 'a1-28-chef', 'a1-29-coach', 'a1-30-new-student'],
      },
    ],
  },
  {
    id: 'a2',
    level: 'A2',
    focus: 'general',
    color: 'primary',
    title: p('Elementar', 'Elementary'),
    subtitle: p('Hikoyalar, xatlar va eʼlonlar (120–250 soʻz); oʻtgan va kelasi zamon', 'Stories, emails and notices; past and future'),
    units: [
      { id: 'a2-u1', title: p('Odatlar va oʻzgarishlar', 'Habits and changes'), texts: ['a2-01-then-now', 'a2-02-morning-habits', 'a2-03-no-phone', 'a2-04-new-school', 'a2-05-grandpa'] },
      { id: 'a2-u2', title: p('Oʻtmishdan hikoyalar', 'Stories from the past'), texts: ['a2-06-unforgettable', 'a2-07-rain-trip', 'a2-08-lost-key', 'a2-09-first-job', 'a2-10-old-tale'] },
      { id: 'a2-u3', title: p('Bayramlar va anʼanalar', 'Holidays and traditions'), texts: ['a2-11-navruz', 'a2-12-wedding', 'a2-13-hayit', 'a2-14-new-year', 'a2-15-world-holidays'] },
      { id: 'a2-u4', title: p('Ish va oʻqish', 'Work and study'), texts: ['a2-16-job-ad', 'a2-17-university', 'a2-18-summer-job', 'a2-19-online-course', 'a2-20-interview'] },
      { id: 'a2-u5', title: p('Sogʻliq va sport', 'Health and sport'), texts: ['a2-21-doctor-advice', 'a2-22-marathon', 'a2-23-breakfast', 'a2-24-sleep', 'a2-25-kurash'] },
      { id: 'a2-u6', title: p('Texnologiya', 'Technology'), texts: ['a2-26-phone-rules', 'a2-27-online-shopping', 'a2-28-robot-vacuum', 'a2-29-social-media', 'a2-30-future-city'] },
    ],
  },
  {
    id: 'b1',
    level: 'B1',
    focus: 'general',
    color: 'warning',
    title: p('Oʻrta daraja', 'Intermediate'),
    subtitle: p('Maqolalar, blog va biografiyalar (250–450 soʻz); True / False / Not Given bilan tanishuv', 'Articles, blogs and biographies; first True / False / Not Given tasks'),
    units: [
      { id: 'b1-u1', title: p('Shaxsiy hikoyalar', 'Personal stories'), texts: ['b1-01-study-abroad', 'b1-02-mountain', 'b1-03-two-languages', 'b1-04-career-change', 'b1-05-volunteer'] },
      { id: 'b1-u2', title: p('Ilm-fan sodda tilda', 'Science made simple'), texts: ['b1-06-blue-sky', 'b1-07-bees', 'b1-08-sleep-memory', 'b1-09-groundwater', 'b1-10-solar'] },
      { id: 'b1-u3', title: p('Tarix va madaniyat', 'History and culture'), texts: ['b1-11-silk-road', 'b1-12-navoi', 'b1-13-ibn-sino', 'b1-14-khiva', 'b1-15-suzani'] },
      { id: 'b1-u4', title: p('Atrof-muhit', 'Environment'), texts: ['b1-16-plastic', 'b1-17-city-parks', 'b1-18-saving-water', 'b1-19-snow-leopard', 'b1-20-climate-farming'] },
      { id: 'b1-u5', title: p('Ish dunyosi', 'The world of work'), texts: ['b1-21-formal-letter', 'b1-22-cv', 'b1-23-remote-work', 'b1-24-startup', 'b1-25-workplace'] },
      { id: 'b1-u6', title: p('Media', 'Media'), texts: ['b1-26-fake-news', 'b1-27-advertising', 'b1-28-podcasts', 'b1-29-film-review', 'b1-30-screen-time'] },
    ],
  },
  {
    id: 'b2',
    level: 'B2',
    focus: 'exam',
    color: 'danger',
    title: p('Imtihonga tayyorgarlik', 'Exam preparation'),
    subtitle: p('IELTS va Milliy sertifikat (Multilevel) tarzidagi topshiriqlar, 250–600 soʻz', 'IELTS- and Multilevel-style tasks'),
    units: [
      {
        id: 'b2-u1',
        title: p('Topshiriq turlari bilan tanishuv', 'Meet the task types'),
        texts: ['b2-01-aral', 'b2-02-ulugh-beg', 'b2-03-silkworm', 'b2-04-online-learning', 'b2-05-city-transport'],
      },
      { id: 'b2-u2', title: p('True / False / Not Given', 'True / False / Not Given'), texts: ['b2-06-tea', 'b2-07-bilingual-brain', 'b2-08-desert-plants', 'b2-09-food-waste', 'b2-10-city-noise'] },
      { id: 'b2-u3', title: p('Matching headings', 'Matching headings'), texts: ['b2-11-cotton', 'b2-12-museums', 'b2-13-insomnia', 'b2-14-architecture', 'b2-15-ai-work'] },
      { id: 'b2-u4', title: p('Summary va gap completion', 'Summary and sentence completion'), texts: ['b2-16-sardoba', 'b2-17-honey', 'b2-18-cycling-cities', 'b2-19-language-learning', 'b2-20-earthquakes'] },
      { id: 'b2-u5', title: p('Multiple choice va fikr', 'Multiple choice and opinion'), texts: ['b2-21-homework', 'b2-22-tourism', 'b2-23-teens-social', 'b2-24-city-village', 'b2-25-books-screens'] },
      { id: 'b2-u6', title: p('Toʻliq mashq testlari', 'Practice tests'), texts: ['b2-26-test1', 'b2-27-test2', 'b2-28-test3', 'b2-29-test4', 'b2-30-test5'] },
    ],
  },
  {
    id: 'c1',
    level: 'C1',
    focus: 'exam',
    color: 'primary',
    title: p('Yuqori daraja', 'Advanced'),
    subtitle: p('Akademik va publitsistik matnlar (600–900 soʻz), IELTS Academic darajasi', 'Academic and opinion texts, IELTS Academic level'),
    units: [
      { id: 'c1-u1', title: p('Fan va tadqiqot', 'Science and research'), texts: ['c1-01-microbiome', 'c1-02-memory', 'c1-03-quantum', 'c1-04-deep-ocean', 'c1-05-placebo'] },
      { id: 'c1-u2', title: p('Iqtisod va jamiyat', 'Economy and society'), texts: ['c1-06-remittances', 'c1-07-urbanisation', 'c1-08-four-day-week', 'c1-09-cooperatives', 'c1-10-inequality'] },
      { id: 'c1-u3', title: p('Psixologiya', 'Psychology'), texts: ['c1-11-decisions', 'c1-12-attention', 'c1-13-empathy', 'c1-14-motivation', 'c1-15-conformity'] },
      { id: 'c1-u4', title: p('Fikr va munozara', 'Opinion and debate'), texts: ['c1-16-free-museums', 'c1-17-automation', 'c1-18-language-identity', 'c1-19-sport-money', 'c1-20-university-rankings'] },
      { id: 'c1-u5', title: p('Adabiyot va biografiya', 'Literature and biography'), texts: ['c1-21-qodiriy', 'c1-22-translation', 'c1-23-fairy-tales', 'c1-24-babur', 'c1-25-history-reading'] },
      { id: 'c1-u6', title: p('Toʻliq mashq testlari', 'Practice tests'), texts: ['c1-26-test1', 'c1-27-test2', 'c1-28-test3', 'c1-29-test4', 'c1-30-test5'] },
    ],
  },
];

export const getText = (id: string): ReadingText | undefined => TEXTS[id];
export const getBook = (id: string): Book | undefined => BOOKS.find(b => b.id === id);

/** Kitobdagi tayyor matnlar (tartib bilan) */
export const bookTexts = (book: Book): ReadingText[] =>
  book.units.flatMap(u => u.texts.map(id => TEXTS[id]).filter((t): t is ReadingText => !!t));

export const bookTextCount = (book: Book) => bookTexts(book).length;
export const bookPlannedCount = (book: Book) =>
  book.units.reduce((n, u) => n + u.texts.length + (u.planned?.length ?? 0), 0);

export const allTexts = (): ReadingText[] => BOOKS.flatMap(bookTexts);

/** Metnin kitobi va bölüm içindeki yeri */
export function textLocation(id: string): { book: Book; unitIndex: number; index: number } | null {
  for (const book of BOOKS) {
    for (let ui = 0; ui < book.units.length; ui++) {
      const i = book.units[ui].texts.indexOf(id);
      if (i >= 0) {
        return { book, unitIndex: ui, index: i };
      }
    }
  }
  return null;
}

export const wordCount = (t: ReadingText) => t.paragraphs.reduce((n, p) => n + p.en.split(/\s+/).filter(Boolean).length, 0);
/** Okuma süresi (dakika): A1–A2 ~60, B1 ~90, B2+ ~120 kelime/dk */
export const readingMinutes = (t: ReadingText) => {
  const wpm = t.level === 'A1' || t.level === 'A2' ? 60 : t.level === 'B1' ? 90 : 120;
  return Math.max(1, Math.round(wordCount(t) / wpm));
};
