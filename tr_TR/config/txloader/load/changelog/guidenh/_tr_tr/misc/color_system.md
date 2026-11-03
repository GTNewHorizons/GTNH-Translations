---
navigation:
  title: Tam Renk Sistemi
  parent: misc.md
  icon: gregtech:gt.metaitem.02:32415
categories:
    - Miscellaneous Changes
author: Skorched
date: 2026-05-20
---

# Tam Renk Sistemi
Biraz <Color id="GREEN">Renk!</Color> olmadan hayat neye yarar! GTNH artık tamamen yerleşik eksiksiz bir renk sistemine sahip! Bu sistem görevler, tabelalar, örsler, sohbet ve metnin görüntülendiği hemen hemen her yerde çalışır!

## Dahil Olan Özellikler
- 16 klasik rengin tamamı - sadece "\&" ve bir renk kodu yaz!
- RGB onaltılık renkler - 16 milyon rengin herhangi biri
- Degradeler - yumuşak renk geçişleri oluştur
- Gökkuşağı metni - neden olmasın ki?
- Dalgalı metin - animasyonlu zıplayan metin
- Kalın, italik, altı çizili ve daha fazlası - herhangi bir renkle serbestçe birleştirilebilir

# Kullanım
Metninden önce rengi yazman yeterli; başka bir renk kullanana veya `\&r` ile sıfırlayana kadar her şey o renkte olur.
## Vanilya Renkleri:

| Kod | Renk |
| -------------- | --------------- |
| `\&0` | <Color id="BLACK">Siyah</Color> |
| `\&1` | <Color color="#0000AA">Koyu Mavi</Color> |
| `\&2` | <Color color="#00AA00">Koyu Yeşil</Color> |
| `\&3` | <Color color="#00AAAA">Koyu Turkuaz</Color> |
| `\&4` | <Color color="#AA0000">Koyu Kırmızı</Color> |
| `\&5` | <Color color="#AA00AA">Koyu Mor</Color> |
| `\&6` | <Color color="#FFAA00">Altın</Color> |
| `\&7` | <Color color="#AAAAAA">Gri</Color> |
| `\&8` | <Color color="#555555">Koyu Gri</Color> |
| `\&9` | <Color color="#5555FF">Mavi</Color> |
| `\&a` | <Color color="#55FF55">Yeşil</Color> |
| `\&b` | <Color color="#55FFFF">Turkuaz</Color> |
| `\&c` | <Color color="#FF5555">Kırmızı</Color> |
| `\&d` | <Color color="#FF55FF">Açık Mor</Color> |
| `\&e` | <Color color="#FFFF55">Sarı</Color> |
| `\&f` | <Color color="#FFFFFF">Beyaz</Color> |


## Biçimlendirme:
| Kod | Etki |
| -------------- | --------------- |
| `\&l` | __Kalın Metin__ |
| `\&o` | _İtalik Metin_  |
| `\&n` | <u>Altı Çizili Metin</u> |
| `\&m` | ~~Üstü Çizili Metin~~ (Üstü Çizili) |
| `\&k` | Gizemli Metin (Netlik için oluşturulmaz)|
| `\&z` | Dalgalı Metin |
| `\&r` | Normal yazıya sıfırlar|


## RGB Onaltılık Renkler:
16 renk yetmedi mi? Kendi rengini uydur! Geçerli herhangi bir onaltılık kod kullanabilirsin (takılırsan çevrimiçi bir renk seçici kullan)
| Kod | Renk |
| -------------- | --------------- |
| `\&#FF6B4A` | <Color color="#FF6B4A">Mercan Turuncusu</Color> |
| `\&#4ECDC4` | <Color color="#4ECDC4">Yumuşak Turkuaz</Color> |
| `\&#7B68EE` | <Color color="#7B68EE">Levha Mavisi</Color> |
| `\&#FF69B4` | <Color color="#FF69B4">Sıcak Pembe</Color> |


## Degradeler:
`\&g` ve ardından iki geçerli onaltılık renk yazarak belirtilen iki renk arasında bir degrade oluşturulur! Ateş yapmak için `\&g\&#FF0000\&#FFFF00<YourTextHere>` yazmayı dene!

Özel bir degrade türünün kendi özel kodu var! Gökkuşağı efektleri için `\&q` yaz!

