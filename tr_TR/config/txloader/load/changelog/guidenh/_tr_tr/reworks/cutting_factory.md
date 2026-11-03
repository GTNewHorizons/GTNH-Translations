---
item_ids:
  - gregtech:gt.blockmachines:15540
navigation:
  title: Endüstriyel Kesim Fabrikası
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15540
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---
# Endüstriyel Kesim Fabrikası

<GameScene wrap="square" align="right">
  <ImportStructure src="../assets/reworks/cutting.snbt"/>
</GameScene>

<Color id="GREEN">Endüstriyel Kesim Fabrikası (ICF)</Color>, çubuk, gofret, blok ve daha fazlasını kesmek için bir IV kademe multibloğudur. <Color id="GREEN">ICF</Color>, tek bloklu kesim makinesinin doğrudan yükseltmesidir çünkü <Color id="BLUE">%450</Color>'ye varan hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="RED">%60</Color>'ını kullanır ve her gerilim kademesi başına <Color id="GREEN">6</Color> paralel sunar. Kesin bonuslar ve enerji kapaklarının maksimum kademesi, kontrolcüdeki testere bıçağının kademesine bağlıdır. Yalnızca bir testere bıçağı gerekir ve dört kademenin hepsinin dayanıklılığı sınırsızdır--makineyi yükseltmek için tek seferlik bir maliyettir. Aşkın metal testere bıçağı <ItemImage id="gregtech:gt.metaitem.01:32105"/> en güçlüsüdür ve normal enerji kapakları yerine bir çok-amperli enerji kapağı kullanma yeteneğini açar. Aynı makine içinde farklı programlanmış devreler ve/veya tüketilmeyen eşyalar kullanmak için <Color id="GREEN">ICF</Color>'de girdi ayrıştırması etkinleştirilmelidir.
<br clear="all"/>

> [!NOTE]
> Multibloğa (yapı dışında) şu değişiklikler yapıldı:
> - Paraleller: Artık Gerilim Kademesinden bağımsız, ancak kullanılan testere bıçaklarına bağlı (maks 6, önceden 4)
> - Hız: Ayrıca testere bıçaklarına bağlı (maks %450, önceden %300)
> - Güç: AYRICA testere bıçaklarına bağlı (min %60, önceden %75)

## Yapım
<Color id="GREEN">ICF</Color>'in kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına bir etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir kasayı değiştirebilir. <Color id="RED">Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı olabilir. Aşkın metal testere bıçağı kullanılıyorsa bir <Color id="GREEN">Çok-Amperli Enerji Kapağı</Color> kullanılabilir. Animasyonları devre dışı bırakmak için kontrolcüye tornavida kullan. Camın kademesini belirtmek üzere "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15540"/><ItemImage id="gregtech:gt.blockmachines:15540"/>
- 10-30 <ItemLink id="miscutils:gtplusplus.blockcasings.2:13"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:13"/>
- 18 <ItemLink id="miscutils:blockFrameGtTantalumCarbide"/><ItemImage id="miscutils:blockFrameGtTantalumCarbide"/>
- 13 <ItemLink id="gregtech:gt.sheetmetal:334"/><ItemImage id="gregtech:gt.sheetmetal:334"/>
- 1+ Enerji Kapağı (herhangi bir çerçeve, kademe testere bıçağıyla sınırlı) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir çerçeve) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir çerçeve) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir çerçeve) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir çerçeve) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir çerçeve) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">ICF</Color>'ler kasa, çerçeve kutusu, cam ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">ICF</Color>, tek bloklu kesim makinesinin doğrudan yükseltmesidir çünkü %450'ye varan hızda çalışır, normalde gereken EU/t'nin yalnızca %60'ını kullanır ve her gerilim kademesi başına 6 paralel sunar. Kesin bonuslar ve enerji kapaklarının maksimum kademesi, kontrolcüdeki testere bıçağının kademesine bağlıdır.

<Color id="GREEN">ICF</Color>'de herhangi bir tarifi çalıştırmak için kontrolcüde bir testere bıçağı gereklidir. Dört kademenin hepsinin dayanıklılığı sınırsızdır--makineyi yükseltmek için tek seferlik bir maliyettir. Kontrolcüde birden fazlasını üst üste koymanın makinenin çalışmasına bir etkisi yoktur. Aşkın metal testere bıçağı en güçlüsüdür ve normal enerji kapakları yerine bir çok-amperli enerji kapağı kullanma yeteneğini açar.

Farklı giriş yollarındaki KATI bileşenlerin, programlanmış devreler veya dilimleyici bıçağı dahil, aynı tarifte kullanılmasını önlemek için <Color id="GREEN">ICF</Color>'de girdi ayrıştırması etkinleştirilmelidir. Bu, çok sayıda giriş yolu olan tek bir <Color id="GREEN">ICF</Color>'in aynı anda birçok farklı programlanmış devreyi destekleyebileceği anlamına gelir. Sadece kesim fabrikası çerçevelerinin minimum sayısının üzerinde kalmayı unutma. SIVI bileşenler, girdi kapağı renklendirilmediği sürece, girdi ayrıştırmasından bağımsız olarak her zaman paylaşılır.