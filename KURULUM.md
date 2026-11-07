# LinguaUz Reading — kurulum

Grammar ile aynı yapı: React Native 0.80.3, yeni mimari, `src/core` ortak çekirdek (seri, günlük hedef, yedek ortak).

## 1. Projeyi oluştur (bir kez)

Grammar klasörünün **yanında** (kısa bir yol seçin):

```powershell
cd C:\Users\abdur\Desktop
npx @react-native-community/cli@19.1.2 init Reading --version 0.80.3
cd Reading
```

## 2. Zip'i aç

Zip'i `Reading` klasörünün içine açın, var olan dosyaların üzerine yazsın (`App.tsx` dahil).
Şablonla gelen `__tests__/App.test.tsx` dosyasını silin.

## 3. Paketler (PowerShell'de tırnaklar şart)

```powershell
npm install "@op-engineering/op-sqlite@14.1.4" "@react-native-async-storage/async-storage@2.2.0" "@react-navigation/native@^7.1.0" "@react-navigation/native-stack@^7.3.0" "@react-navigation/bottom-tabs@^7.4.0" "react-native-safe-area-context@5.6.2" "react-native-screens@4.18.0" "react-native-vector-icons@^10.3.0" "@mhpdev/react-native-speech@1.4.3" "@react-native-documents/picker@10.1.7" "@dr.pogodin/react-native-fs@2.35.1" "@notifee/react-native@9.1.8"
npm install -D "@types/react-native-vector-icons@^6.4.18"
```

## 4. Android ayarları (Grammar'dakinin aynısı)

**`android/app/build.gradle`**
- En üstteki `apply plugin` satırlarının altına:
  ```gradle
  apply from: file("../../node_modules/react-native-vector-icons/fonts.gradle")
  ```
- `dependencies { ... }` içine:
  ```gradle
  implementation("androidx.core:core-splashscreen:1.0.1")
  ```

**`android/build.gradle`**: `buildToolsVersion = "36.0.0"`, `compileSdkVersion = 36`, `targetSdkVersion = 36`

**`android/app/src/main/AndroidManifest.xml`**
- `<application>` içinde `android:theme="@style/AppTheme"` → `android:theme="@style/Theme.App.Starting"`
- `MainActivity`'ye derin bağlantı filtresi (mevcut `MAIN/LAUNCHER` bloğunun **altına**):
  ```xml
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="linguauz-reading" />
  </intent-filter>
  ```
  Deneme: `adb shell am start -W -a android.intent.action.VIEW -d "linguauz-reading://text/a1-01-dilnoza"`

Zip'teki `MainActivity.kt` (paket `com.reading`), `styles.xml`, mor ikonlar ve açılış görseli hazır.
İkonu değiştirmek için: `python scripts/branding/make_icons.py` (renk ve yazı betiğin başında).

## 5. Grammar'a da bir satır (gramer notları için)

Reading'deki «Matndagi grammatika» kartı Grammar'da dersi açar: `linguauz-grammar://topic/<id>`.
Grammar'ın kodu hazır (zip'te `AppNavigator.tsx`). Grammar'ın `AndroidManifest.xml`'ine yukarıdaki
`intent-filter`'ın aynısını `android:scheme="linguauz-grammar"` ile ekleyin.

Paket adları kesinleşince **üç projede de** `src/core/config.ts` → `SUITE_LINKS` içindeki `androidPackage`
değerlerini güncelleyin (uygulama kurulu değilse Play Market sayfası buna göre açılır).

## 6. Çalıştır

```powershell
cd android; .\gradlew clean; cd ..
npx react-native start --reset-cache
# ikinci terminal:
npx react-native run-android
```

## 7. İçerik testi

Yeni metin ekledikten sonra:
```powershell
npm test -- content
```
Seviyeye göre uzunluk, A1–A2'de tarjima, boşluk cevabının metinde geçmesi, Özbekçe `o'` hatası,
gramer notu örneğinin metinden alınması gibi kuralları denetler.

## Notlar

- `src/core/` üç projede de AYNI: birinde değiştirirseniz diğerlerine kopyalayın (bu sürümde `AppKey`'e `speaking`
  ve `SUITE_LINKS`'e `grammar`, `reading` eklendi — üç projenin `config.ts`'i zip'lerde güncel).
- İçerik nasıl yazılır: `docs/ICERIK.md`.
