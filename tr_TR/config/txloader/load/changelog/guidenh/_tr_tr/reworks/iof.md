---
item_ids:
  - gregtech:gt.blockmachines:15564
navigation:
  title: Entegre Cevher Fabrikası
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15564
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-23
---

# Entegre Cevher Fabrikası

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15564"/>
</GameScene>
<Color id="GREEN">Entegre Cevher Fabrikası (IOF)</Color>, tüm cevher işlemeyi tek adımda yapan UHV kademesinde bir multibloktur. Mevcut tüm cevher işleme düzenlerinin tamamen yerini almak, genel verimi artırmak ve lag'i azaltmak için tasarlanmıştır. <Color id="GREEN">IOF</Color>, <ItemLink id="gregtech:gt.blockmachines:14003" /> kısa bir süre sonra açılır; oyuncunun büyük miktarda cevher biriktirmeye başladığı ve hepsini toza işlemenin daha kolay/daha hızlı bir yoluna ihtiyaç duyduğu nokta burasıdır. <Color id="GREEN">IOF</Color> tüm cevher çeşitlerini (Ezilmiş, Temizlenmiş vb.) destekler ve yeterli paralel varsa farklı tarifleri aynı anda bile işleyebilir. Toplam paralel sayısı girdi gücüyle doğrusal olarak ölçeklenir ve üst sınırı yoktur. Yan ürünler, <Color id="GREEN">IOF</Color>'un mevcut moduna göre üretilir. Yedi farklı cevher işleme yolu (eleme, cevher yıkama, kimyasal banyo vb.) için toplam yedi mod vardır.
<br clear="all"/>

> [!NOTE]
> Önceki Entegre Cevher Fabrikası'na göre değişiklikler şunlardır (yeni yapı hariç):
> - Lazer Desteği: Ciddi hız aşırtma için artık Lazer Enerji kapaklarını kabul ediyor
> - Mod Düğmeleri: Mod değiştirme düğmesi artık GUI'de bulunabiliyor
> - Esneklik: Kapak konumu kısıtlamaları büyük ölçüde azaltıldı, yerleştirmede daha fazla esneklik sağlanıyor


## İnşa
<Color id="GREEN">IOF</Color>'un kademeli bileşenleri yoktur. Cam her kademeden olabilir ve makinenin çalışması üzerinde etkisi yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki paslanmaz çelik Makine Gövdesi'nin yerini alabilir. Ciddi verim için <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> kullan.

<ItemLink id="gregtech:gt.blockmachines:32026" /> bileşen parçaları için __KULLANILMADIĞI__ varsayılırsa, bir <Color id="GREEN">IOF</Color> inşa etmek diğer malzemelerin yanı sıra 7.21k nötronyum, 3.89k iridyum, 3.03k kozmik nötronyum, 3.02k naquadria ve 880 Katmankayamsı gerektirir.

### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15564" /> <ItemImage id="gregtech:gt.blockmachines:15564" />
- 462 <ItemLink id="gregtech:gt.blockcasings8:7" /> <ItemImage id="gregtech:gt.blockcasings8:7" />
- 0-163 <ItemLink id="gregtech:gt.blockcasings4:1" /> <ItemImage id="gregtech:gt.blockcasings4:1" />
- 96 <ItemLink id="gregtech:gt.sheetmetal:84" /> <ItemImage id="gregtech:gt.sheetmetal:84" />
- 90 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 23 <ItemLink id="gregtech:gt.blockframes:306" /> <ItemImage id="gregtech:gt.blockframes:306" />
- 7 <ItemLink id="gregtech:gt.blockcasings5:8" /> <ItemImage id="gregtech:gt.blockcasings5:8" />
- 7 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:6" />
- 7 <ItemLink id="gregtech:gt.blockcasings3:10" /> <ItemImage id="gregtech:gt.blockcasings3:10" />
- 7 <ItemLink id="miscutils:miscutils.blockcasings" /> <ItemImage id="miscutils:miscutils.blockcasings" />
- 1 Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">IOF'ler</Color> kasa, sac metal, çerçeve kutusu ve veriyolu/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımına açabilir. Alt katmanı, hemen altına ters çevrilmiş başka bir IOF ile üst üste bindirmek en etkili yöntemdir ve şiddetle önerilir. Ancak enerji kapağını paylaşma; çünkü makine hâlâ paralel kullanılabilirken mümkün olduğunca fazla amper çeker.

## Kullanım
<Color id="GREEN">IOF</Color>, GTNH'deki çeşitleri (Ezilmiş, Temizlenmiş vb.) dahil neredeyse her cevheri işleyebilir. Her cevher sabit 30 EU/t, 2L yağlayıcı ve 200L damıtılmış suya mal olur. Kimyasal banyo için sodyum persülfat gibi başka girdiler içeren tarifler, varsayılan maliyetlere ek olarak bunları yine de gerektirir. İşleme hızı, sağlanan güce ve makinenin moduna bağlıdır.

Aşağıda listelenen yedi farklı cevher işleme yolu için toplam yedi mod vardır. Modlar arasında kontrolcünün GUI'sinden veya kontrolcüye tornavidayla sağ tıklayarak geçiş yap. Taş tozunu otomatik olarak yok etmek için kontrolcüye eğilerek tornavidayla sağ tıkla.
| Mod | Süre | Yol | Maks. Verim |
| --------------- | --------------- | --------------- | --------------- |
| 1 | 30s | Öğütme -> Cevher Yıkayıcı -> Termal Santrifüj -> Öğütme | 357,914 /s |
| 2 | 15s | Öğütme -> Cevher Yıkayıcı -> Öğütme -> Santrifüj | 715,828 /s |
| 3 | 10s | Öğütme -> Öğütme -> Cevher Yıkayıcı | 1,073,742 /s |
| 4 | 20s | Öğütme -> Cevher Yıkayıcı -> Elek | 536,871 /s |
| 5 | 17s | Öğütme -> Kimyasal Banyo -> Öğütme -> Santrifüj| 631,613 /s |
| 6 | 32s | Öğütme -> Kimyasal Banyo -> Termal Santrifüj -> Öğütme | 335,544 /s |
| 7 | 1s | Dövme Çekici -> Dövme Çekici -> Basit Yıkayıcı| 10,737,418 /s |

Tüm cevher işleme tarifleri LV kademesindedir; temel süreler ve güç maliyetleri buradan gelir. <Color id="GREEN">IOF</Color> hiç __hız aşırtma__ yapmaz, ancak sağlanan her 30 EU/t için bir paralel ekler. Paralel sayısında teknik olarak üst sınır yoktur, ancak damıtılmış su üzerindeki maksimum tamsayı sınırı nedeniyle yine de 10,737,418 veya 322,122,540 EU/t'de tavan yapar. Bu, 256A UHV'yi aşmanın makinenin çalışması üzerinde hiçbir etkisi olmadığı ve aynı anda 2B'den fazla damıtılmış su sağlamak için daha fazla ME stoklama Girdi Kapağı eklemenin de yardımcı olmadığı anlamına gelir.