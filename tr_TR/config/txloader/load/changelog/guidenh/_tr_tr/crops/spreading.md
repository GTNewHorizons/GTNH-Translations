---
navigation:
  title: Ekin Yayılımı
  parent: crops.md
  icon: cropsnh:cropSticks
categories:
    - crops
author: Skorched
date: 2026-05-21
---

# Ekin Yayılımı
> [!NOTE]
> Bu sayfa, [Ekin Temelleri](basics.md) sayfasını zaten okuduğunu veya ekinlerin ve istatistiklerinin temellerine aşina olduğunu varsayar
Diyelim ki istediğin ekine sahipsin. Tek bir ekin muhtemelen yeterli olmayacaktır, ancak bir ekin alanı elde etmek için ekinlerinin istatistiklerini yüzlerce kez yeniden ayarlamak zahmetli olurdu! Buna yardımcı olmak için <Color id="GREEN">Ekin Yayılımı</Color>'ndan yararlanabiliriz.

Pekâlâ çocuklar, öğretmen gitti, hadi videoyu açalım!
<GameScene width="420" height="280" zoom={2.5} interactive={true}>
  <ImportStructure src="../assets/crops/spreading.snbt" />
  <ImportPonder src="../assets/crops/spreading.json" />
</GameScene>

# Açıklamalar:
Videoyu izlemek istemeyenler veya daha fazla ayrıntıya ihtiyaç duyanlar için işte ders kitabı sürümü:

## Yayılım
Bir ekini yaymak için, yanında çapraz bir Ekin Çubuğu (aynı yere iki kez yerleştirilmiş) olmalı ve altında hedef ekin için geçerli bir toprak bloğu bulunmalıdır. Ekinin bir alt toprak gereksinimi varsa, yeni ekinin hedef bloğunda da bu gereksinim olmalıdır. Bu gereksinimleri NEI'nin "Ekinler" sayfasında bulabilirsin:
<RecipeFor id="minecraft:log" input="cropsnh:genericSeed" float="left" wrap="square"/>
Ekin bu bitişik ekin çubuklarında büyüyebiliyorsa, kendini çoğaltarak diğer ekin çubuğu grubuna yayılmaya çalışacaktır.

Yeni ekinin istatistikleri gübrelenmemişse (-2:+4), gübrelenmişse (+0:+4) aralığında olacaktır. Böylece, gübrelenmiş topraktan oluşan yönetilen bir alanda tek bir ekinle başlarsan, yeterli zamanla MAX istatistikli (31/31/31) bir ekin elde etmen garanti olur.
<br clear="all" />
## Yabani Otlar
Toprak Weed-Ex <ItemImage id="cropsnh:weedEX" /> ile işlenmediği sürece, yabani otlar çiftlenmiş olsun olmasın <Color id="RED">***HER***</Color> ekin çubuğunda her zaman büyümeye çalışır. Yabani otlar baş belasıdır; çünkü onlar da yayılarak ekin alanını yiyip bitirir ve ... gibi başka sorunlara yol açar.

## Hastalık
Eski uygulamanın aksine, yabani otlar diğer ekinleri **yok etmez**, bunun yerine onları <Color id="RED">hasta</Color> eder. Hasta ekinler ürün veremez ve <Color id="GREEN">Bitki İlacı</Color> <ItemImage id="cropsnh:plantCure" /> kullanılarak iyileştirilmelidir.