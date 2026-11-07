# Reading — içerik rehberi

## Müfredat

| Kitap | Seviye | Odak | Metin uzunluğu | Soru türleri | Hedef |
|---|---|---|---|---|---|
| Boshlangʻich | A1 | Genel | 60–120 kelime | True/False, çoktan seçmeli, boşluk | 6 bölüm × 5 = 30 |
| Elementar | A2 | Genel | 120–250 | A1 ile aynı (daha uzun metin, geçmiş zaman) | 30 |
| Oʻrta daraja | B1 | Genel | 250–450 | + True/False/**Not Given** | 30 |
| Imtihonga tayyorgarlik | B2 | IELTS / Multilevel | 250–600 | TFNG, matching headings, summary (NO MORE THAN N WORDS), çoktan seçmeli | 30 |
| Yuqori daraja | C1 | IELTS Academic | 600–900 | Hepsi + tam deneme testleri | 30 |

Bölüm ve metin başlıkları `src/features/reading/content/index.ts` içinde (`planned` = henüz yazılmadı, uygulamada «Tez orada» görünür).
Toplam plan: **150 metin**. Hazır: 5 kitabın tamamı (150 metin).

## Bir metin nasıl yazılır

`scripts/content/<seviye>_u<n>.py` dosyasında `text(...)`:

```python
text('a1', 'a1-06-morning', 'Mening kunim', 'My Morning', 'A1', 'story', L('Kundalik hayot', 'Daily life'),
     'Oʻqishdan oldin: siz ertalab nima qilasiz?',            # okumadan önce (Özbekçe)
     [P("English paragraph…", "Özbekçe çevirisi…"), ...],    # A1–A2'de çeviri ZORUNLU
     [G('wake up', 'uygʻonmoq'), ...],                        # lugʻat: en az 5
     [GN('b19-my-day', 'Present Simple: he gets up', 'He gets up at seven.')],  # Grammar dersi + metinden örnek
     [tf('…', 'T', 'izoh', para=0), ch('…?', ['a', 'b', 'c'], 1, 'izoh', 1), gap('… ___ …', 'word', 'izoh', 2)])
```

Sonra: `python scripts/content/a1_u2.py` → `index.ts`'de import + bölümün `texts` listesine ekle (aynı adı `planned`'dan sil) → `npm test -- content`.

### Kurallar
1. **Metinler özgün.** Kitaplardan / sitelerden kopya yok. Sınav kitaplarındaki formatlar taklit edilir, metinleri değil.
2. **Gerçek bilgi doğru olmalı** (tarih, sayı, yer). Emin olunmayan sayı yazılmaz («about a thousand» gibi).
3. Konuların yarısı Özbekistan'dan (şehirler, gelenekler, tarih, doğa), yarısı dünyadan.
4. Seviye dili: A1'de Present Simple, *there is*, *can*; A2'de geçmiş ve gelecek; B1+ serbest.
   Gramer notu, metinde gerçekten geçen yapıyı Grammar'daki derse bağlar (`topicId` = Grammar konu id'si).
5. Her soruda **izoh** (Özbekçe): neden doğru + metnin hangi cümlesinde. `para` = cevabın paragrafı (0'dan).
6. **Not Given** yalnız B1'den itibaren. NG sorusu gerçek dünyada doğru olsa bile metinde yoksa NG'dir —
   kafa karıştırmamak için gerçekte de bilinmeyen / önemsiz bir ayrıntı seçin.
7. Boşluk (gap) cevabı metinde **aynen** geçmeli; sınav tarzında `max_words` verin.
8. Özbekçe metinde `oʻ gʻ` için ʻ (U+02BB), tutuq belgisi için ʼ — düz `'` kullanmayın.
9. İngilizce paragrafta parantez yok (sesli okumada okunur), çift boşluk yok.

### Öğretmen kontrolü
Grammar'daki gibi bir kontrol tablosu (xlsx) metin sayısı arttıkça üretilebilir.
