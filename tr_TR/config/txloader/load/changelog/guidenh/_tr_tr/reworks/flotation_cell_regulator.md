---
item_ids:
  - gregtech:gt.blockmachines:15560
navigation:
  title: Flotasyon Hücresi Regülatörü
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15560
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Flotasyon Hücresi Regülatörü

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15560"/>
</GameScene>
<Color id="GREEN">Flotasyon Hücresi Regülatörü (FCR)</Color>, öğütülmüş cevher, çam yağı ve etil ksantat tozundan metal köpükleri üretmek için kullanılan LuV kademe bir multibloktur. Metal köpükler daha sonra nadir metal bileşikleri için bir vakum fırınına veya Utupu-Tanuri'ye <ItemImage id="gregtech:gt.blockmachines:995"/> verilir. <Color id="GREEN">FCR</Color> yalnızca tek bir malzeme tipini işleyebilir çünkü makine kendisini kalıcı olarak çalıştırdığı ilk tarife kilitler, ancak kusursuz overclock'larıyla iyi ölçeklenir.
<br clear="all"/>

> [!NOTE]
> Bu multiblokun yalnızca yapısı değişti, mekanikleri aynı kaldı

## Yapım
<Color id="GREEN">FCR</Color> kademeli bileşenlere sahip değildir. Yollar/kapaklar yapının alt katmanındaki herhangi bir inconel güçlendirilmiş kasayı değiştirebilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapı kurulduğunda su bedavaya oluşturulur ve bu yüzden elle yerleştirilmesine gerek YOKTUR. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15560"/><ItemImage id="gregtech:gt.blockmachines:15560"/>
- 90-121 <ItemLink id="miscutils:gtplusplus.blockcasings.3:1"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:1"/>
- 31 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:9"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:9"/>
- 20 <ItemLink id="miscutils:blockFrameGtStaballoy"/><ItemImage id="miscutils:blockFrameGtStaballoy"/>
- 8 <ItemLink id="miscutils:blockFrameGtInconel690"/><ItemImage id="miscutils:blockFrameGtInconel690"/>
- 1+ Enerji Kapağı (herhangi bir alt kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir alt kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir alt kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir alt kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (herhangi bir alt kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">FCR</Color>'lar kasa, çerçeve kutusu ve yol/kapaktan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağı paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">FCR</Color> yalnızca öğütülmüş cevher, çam yağı ve etil ksantat tozundan metal köpükleri üretmek için kullanılır. Metal köpükler daha sonra nadir metal bileşikleri için bir vakum fırınına veya Utupu-Tanuri'ye verilir. Çam yağı ve etil ksantat tozunun ikisi de ExxonMobil Kimya Tesisi'nde <ItemImage id="gregtech:gt.blockmachines:998"/> üretilir. Tarifleri çakışmaz, bu yüzden aynı tesiste üretilebilirler. Sfalerit köpüğü indiyum tozu için çok değerlidir, monazit köpüğü lantan/lutesyum tozu için çok değerlidir ve netherrack köpüğü Netherit Hattı'nda zorunludur.

<Color id="GREEN">FCR</Color> yalnızca tek bir malzeme tipini işleyebilir çünkü makine kendisini kalıcı olarak çalıştırdığı ilk tarife kilitler. Kontrolcüyü kırmak bile onu sıfırlamaz. Bu davranış, herhangi bir baskı gerektirmemesi dışında Devre Montaj Hattı <ItemImage id="gregtech:gt.blockmachines:12735"/> ile benzerdir. 