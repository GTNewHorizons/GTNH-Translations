---
item_ids:
  - gregtech:gt.blockmachines:14050
navigation:
  title: Exo-Foundry
  parent: multis.md
  icon: gregtech:gt.blockmachines:14050
categories:
    - New Multiblocks
author: Skorched
date: 2026-05-25
---

# Exo-Foundry
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:14050" />
</GameScene>
<Color id="GREEN">Exo-Foundry</Color>, sıvı metalleri devasa ölçekte kalıplara döken bir UEV kademesi multibloktur. <Color id="GREEN">Exo-Foundry</Color>, <ItemLink id="gregtech:gt.blockmachines:368" /> <ItemImage id="gregtech:gt.blockmachines:368" /> makinesinin doğrudan yükseltmesidir; çünkü belirgin şekilde daha hızlı çalışır, daha yüksek enerji indirimi sunar ve çok daha fazla paralel işlem yapar. Kesin değerler, takılı modüllerin miktarına ve sayısına göre önemli ölçüde değişir. Toplam yedi modül vardır ve her biri makineye özgü bir bonus verir; ancak yapının kademesine göre yalnızca 2/3/4 yuva bulunur. Modüller tamamen farklı olabilir ya da bonusları üst üste yığmak için aynı modülden birden fazla takılabilir. Ayrıca daha da iyi performans için tek seferlik bonuslar sunan dört modül eşleştirmesi bulunur. 
<br clear="all"/>

## İnşaat:
<Color id="GREEN">Exo-Foundry</Color> üç kademede mevcuttur. Aralarındaki tek yapısal fark manyetik şasi blokları, tek işlevsel fark ise modül yuvası sayısıdır (2/3/4). Veriyolları/kapaklar yapının herhangi bir yerindeki ana <Color id="GREEN">Exo-Foundry</Color> kasasının yerini alabilir. Asgari kasa gereksinimi, toplam 35 kalıp için 25 girişe kadar destekler. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir; ancak <Color id="GREEN">Exo-Foundry</Color>, Aşırı Soğutucu <ItemImage id="gregtech:gt.foundrycasings:9"/> veya Helyo Döküm Takviyesi <ItemImage id="gregtech:gt.foundrycasings:7" /> modülleri olmadan enerji kapağının gerilim kademesinin ötesine hız aşırtma yapamaz. Bakım veya egzoz çıkışı yoktur. Animasyonları kapatmak için kontrolcüye tornavidayla sağ tıkla. Manyetik şasi bloklarının kademesini belirtmek için "chassis" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.
 
Kontrolcünün GUI'sinde hangi modülleri kullanacağını seç, ardından bunları inşa etmek için Multiblok Yapı Hologram Projektörünü kullan. Merkezî kolonun çevresinde halkalar şeklinde görünürler ve istatistikleri kontrolcünün GUI'sindeki "makine bilgilerini göster" bölümünde özetlenir. Sıralamanın makinenin çalışmasına etkisi yoktur. Modülleri seçim menüsünde Shift + sol tıklayarak kaldır, ardından bir <ItemLink id="gregtech:gt.Tool_Vajra" /> <ItemImage id="gregtech:gt.Tool_Vajra" /> veya başka bir aletle fiziksel olarak kır. 
### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:14050" /> <ItemImage id="gregtech:gt.blockmachines:14050" />
- 548 <ItemLink id="gregtech:gt.blockglass1:7" /> <ItemImage id="gregtech:gt.blockglass1:7" />
- 462-486 <ItemLink id="gregtech:gt.foundrycasings" /> <ItemImage id="gregtech:gt.foundrycasings" />
- 281 <ItemLink id="gregtech:gt.foundrycasings:11" /> <ItemImage id="gregtech:gt.foundrycasings:11" />
- 260 _Manyetik Şasi (Kademeli)_ <ItemImage id="gregtech:gt.foundrycasings:1" />
- 224 <ItemLink id="gregtech:gt.blockframes:132" /> <ItemImage id="gregtech:gt.blockframes:132" />
- 196 <ItemLink id="gregtech:gt.foundrycasings:12" /> <ItemImage id="gregtech:gt.foundrycasings:12" />
- 173 <ItemLink id="gregtech:gt.blockcasings11:7" /><ItemImage id="gregtech:gt.blockcasings11:7" />
- 1+ _Enerji Kapağı (herhangi bir ana Exo-Foundry kasası)_ <ItemImage id="gregtech:gt.blockmachines:40" />
- 0+ _Giriş Veriyolu (herhangi bir ana Exo-Foundry kasası)_ <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ _Girdi Kapağı (herhangi bir ana Exo-Foundry kasası)_ <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ _Çıkış Veriyolu (herhangi bir ana Exo-Foundry kasası)_ <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı:
<Color id="GREEN">Exo-Foundry</Color> makineleri kasa, modül bileşeni ve veriyolu/kapak tasarrufu sağlamak için her bir kenarını paylaşabilir. Ancak enerji kapağını paylaşma; çünkü makine hâlâ paralel veya hız aşırtma imkânı varken mümkün olduğunca fazla amper çeker. 

# Modüller:
<Color id="GREEN">Exo-Foundry</Color> modülsüzken <Color id="RED">%150</Color> hızda çalışır ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına <Color id="BLUE">16</Color> paralel sunar. Ayrıca Helyo Döküm Takviyesi <ItemImage id="gregtech:gt.foundrycasings:7" /> modülü olmadan UIV+ tariflerini çalıştıramaz. Bu haliyle tam hızdaki <Color id="RED">Kütle Katılaştırıcı</Color>'dan daha yavaş, daha verimsiz ve daha kısıtlayıcıdır; ancak bunlar makinenin yalnızca temel istatistikleridir ve takılan her modülle belirgin şekilde iyileşir. Paralelleri belirleyen etkin gerilim, hız aşırtmalarda olduğu gibi enerji kapağının kademesiyle sınırlanmaz; ancak amper sayısından bağımsız olarak birden fazla enerji kapağı bulunmalıdır. 

Aşağıdaki tabloda "SCB", <Color id="BLUE">Süper Yoğun Döküm Havuzu</Color> modüllerini; "SCB+" ise eşleştirme bonuslarına sahip aynı modülü ifade eder. Her ikisi de bu bölümün ilerleyen kısmında açıklanacaktır.
### Paraleller:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |------------- |
| Temel | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |
| 1 SCB | 28 | 56 | 84 | 112 | 140 | 168 | 196 | 224 | 252 | 280 | 308 | 336 | 364 | 392 | 420 |
| 2 SCB | 40 | 80 | 120 | 160 | 200 | 240 | 280 | 320 | 360 | 400 | 440 | 480 | 520 | 560 | 600 |
| 1 SCB+ | 34 | 68 | 102 | 136 | 170 | 204 | 238 | 272 | 306 | 340 | 374 | 408 | 442 | 476 | 510 |
| 2 SCB+ | 46 | 92 | 138 | 184 | 230 | 276 | 322 | 368 | 414 | 460 | 506 | 552 | 598 | 644 | 690 |

Toplam yedi modül ve yapının kademesine göre 2/3/4 modül yuvası vardır. Hangi modülleri kullanacağını kontrolcünün GUI'sinde seç. Modüller tamamen farklı olabilir ya da bonusları üst üste yığmak için aynı modülden birden fazla takılabilir. Tek istisnalar Aşırı Soğutucu <ItemImage id="gregtech:gt.foundrycasings:9" />, Bilinçli Hız Aşırtıcı <ItemImage id="gregtech:gt.foundrycasings:5" /> ve Evrensel Çökertici <ItemImage id="gregtech:gt.foundrycasings:4" /> modülleridir; hepsi <Color id="GREEN">Exo-Foundry</Color> başına 1 ile sınırlıdır.

Helyo Döküm Takviyesi <ItemImage id="gregtech:gt.foundrycasings:7" /> ve Bilinçli Hız Aşırtma <ItemImage id="gregtech:gt.foundrycasings:5" /> modüllerinin ikisi de makinenin hız aşırtma faktörünü artırır; bu, her hız aşırtmada hız bonusunu doğrudan yükselten özgün bir mekaniktir. Örneğin kusurlu bir hız aşırtma 2 kat hız için 4 kat güç tüketir; ancak hız aşırtma faktörünü 0.35 artırmak, Exo-Foundry'nin 4 kat güç karşılığında bunun yerine 2.35 kat hız sunmasını sağlar. 

## Süper Yoğun Döküm Havuzları <ItemImage id="gregtech:gt.foundrycasings:8"/>
SCB modülü (UEV), temel gerilim kademesi başına 16 paralelin üzerine 12 paralel daha ekler ve asgari kasa sayısını 36 düşürür. Bu, gerilim kademesi başına toplam 28 paralel ve toplam 35 kalıp için 61 girişe yetecek alan demektir. Exo-Foundry başına SCB modülü sayısında bir sınır yoktur. SCB'yi Akıcı Dökümcüler modülüyle eşleştirmek, gerilim kademesi başına +6 paralel ve +%75 hız sağlayan tek seferlik bir bonus olan Optimum Üretim'i açar. 

### Gereksinimler:
- 64 <ItemLink id="gregtech:gt.foundrycasings:8" /> <ItemImage id="gregtech:gt.foundrycasings:8" />
- 64 <ItemLink id="gregtech:gt.blockcasings10:13" /> <ItemImage id="gregtech:gt.blockcasings10:13" />
- 36 <ItemLink id="gregtech:gt.foundrycasings" /> <ItemImage id="gregtech:gt.foundrycasings" />
- 32 <ItemLink id="gregtech:gt.blockcasings10:14" /> <ItemImage id="gregtech:gt.blockcasings10:14" />
- 30 <ItemLink id="gregtech:gt.blockframes:75" /> <ItemImage id="gregtech:gt.blockframes:75" />
- 8 <ItemLink id="bartworks:bw.werkstoffblockscasing.01:10109"/> <ItemImage id="bartworks:bw.werkstoffblockscasing.01:10109"/>
- 8 <ItemLink id="gregtech:bw.sheetmetal:10109" /> <ItemImage id="gregtech:bw.sheetmetal:10109" />
- 6 <ItemLink id="gregtech:gt.sheetmetal:75" /> <ItemImage id="gregtech:gt.sheetmetal:75" />
- 4 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:10109"/> <ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:10109"/>

## Proto-Volt Dengeleyici <ItemImage id="gregtech:gt.foundrycasings:6" />
PVS modülü (UEV), tariflerin temel EU/t maliyetinden %10 düşer ve sonucu 0.8 ile çarpar; aşağıdaki denklemde görebilirsin. Bu, bir PVS ile %28, iki PVS ile %49 EU/t indirimi demektir. Bunun, tarif süresi değişmediği için Exo-Foundry'nin hızını artırmadığını unutma. Toplamsal bonus Helyo Döküm Takviyesi modülüyle, çarpan bonusu ise Evrensel Çökertici modülüyle üst üste biner. Exo-Foundry başına PVS modülü sayısında bir sınır yoktur. PVS'yi Bilinçli Hız Aşırtıcı modülüyle eşleştirmek, -%50 EU/t ve +0.1 hız aşırtma faktörü sağlayan tek seferlik bir bonus olan Harmonik Verimlilik'i açar. 
<Latex formula="\text{EU/t} = (100\% - \sum \text{AddBonus}) \times \prod \text{MultBonus}"/>

| Modüller   | Güç Tüketimi (EU/t)    |
|--------------- | --------------- |
| 1 PVS   | $$(100\% - 10\%) \times 0.8 = 72\%$$   |
| 2 PVS   | $$(100\% - 20\%) \times 0.8^2 = 51\%$$   |
| 1 PVS+   | $$(100\% - 60\%) \times 0.8 = 32\%$$   |
| 2 PVS+   | $$(100\% - 70\%) \times 0.8^2 = 19\%$$   |

### Gereksinimler:
- 64 <ItemLink id="gregtech:gt.foundrycasings:6" /><ItemImage id="gregtech:gt.foundrycasings:6" />
- 32 <ItemLink id="gregtech:gt.blockframes:73" /><ItemImage id="gregtech:gt.blockframes:73" />
- 28 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2:3" /> <ItemImage id="miscutils:gtplusplus.blockspecialcasings.2:3"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:112" /><ItemImage id="gregtech:gt.sheetmetal:112"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:391" /><ItemImage id="gregtech:gt.sheetmetal:391"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:69" /><ItemImage id="gregtech:gt.sheetmetal:69"/>
- 4 <ItemLink id="gregtech:gt.sheetmetal:112" /><ItemImage id="gregtech:gt.sheetmetal:112"/>
- 4 <ItemLink id="gregtech:gt.blockcasings11:5" /><ItemImage id="gregtech:gt.blockcasings11:5" />

## Akıcı Dökümcüler <ItemImage id="gregtech:gt.foundrycasings:10" />
SC modülü (UEV), Exo-Foundry'nin temel hızına %150 daha ekler; yani temel %150 hızın üzerine çıkar, aşağıdaki denklemde görüldüğü gibi. Bu, bir SC ile toplam %300, iki SC ile %450 hız demektir. Toplamsal bonus Helyo Döküm Takviyesi modülüyle üst üste biner; Evrensel Çökertici modülünün çarpan bonusu ise sonrasında uygulanır. Exo-Foundry başına SC modülü sayısında bir sınır yoktur. SC'yi Süper Yoğun Döküm Havuzları modülüyle eşleştirmek, gerilim kademesi başına +6 paralel ve +%75 hız sağlayan tek seferlik bir bonus olan Optimum Üretim'i açar. 
<Latex formula="(150\% + \sum \text{AddBonus}) \times \prod \text{MultBonus}" />

| Modüller   | Hız    |
|--------------- | --------------- |
| 1 SC   | $$(150\% + 150\%) \times 1 = 300\%$$   |
| 2 SC   | $$(150\% + 300\%) \times 1 = 450\%$$   |
| 1 SC+   | $$(150\% + 225\%) \times 1 = 375\%$$   |
| 2 SC+   | $$(150\% + 375\%) \times 1 = 525\%$$   |

### Gereksinimler:
- 64 <ItemLink id="gregtech:gt.foundrycasings:10" /><ItemImage id="gregtech:gt.foundrycasings:10" />
- 28 <ItemLink id="gregtech:gt.blockframes:974" /><ItemImage id="gregtech:gt.blockframes:974" />
- 24 <ItemLink id="gregtech:gt.blockframes:329" /><ItemImage id="gregtech:gt.blockframes:329" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:974" /><ItemImage id="gregtech:gt.sheetmetal:974" />
- 12 <ItemLink id="miscutils:gtplusplus.blockcasings.5:3" /><ItemImage id="miscutils:gtplusplus.blockcasings.5:3" />
- 12 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:13" /><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:13" />

## Aşırı Soğutucu <ItemImage id="gregtech:gt.foundrycasings:9" />
HC modülü (UIV), makine çalışırken soğutucu tüketerek azami hız aşırtma sayısını enerji kapağının gerilim kademesinin ötesine taşır. Soğutucuyu Exo-Foundry'ye DEĞİL, modülün kendisindeki girdi kapağına ver. Ek hız aşırtma sayısı, aşağıdaki tabloda görüldüğü gibi verilen soğutucunun türüne bağlıdır. Exo-Foundry başına 1 HC modülü sınırı vardır. HC'yi Evrensel Çökertici modülüyle eşleştirmek, Eternity'nin 3 ek hız aşırtmaya kadar soğutucu olarak kullanılmasını sağlayan, güç tüketimini 2 katına ve hızı 2 katına çıkaran tek seferlik bir bonus olan Gerçekleşen Potansiyel'i açar. 
| Soğutucu | Oran | Hız Aşırtma |
| --------------- | --------------- | --------------- |
| Süper Soğutucu | 100 L/s | +1 |
| Uzayzaman | 50 L/s | +2 |
| Eternity* | 25 L/s | +3 |

### Gereksinimler:
- 64 <ItemLink id="gregtech:gt.sheetmetal:389" /> <ItemImage id="gregtech:gt.sheetmetal:389" />
- 48 <ItemLink id="gregtech:gt.blockframes:394" /><ItemImage id="gregtech:gt.blockframes:394" />
- 36 <ItemLink id="gregtech:gt.foundrycasings:9" /><ItemImage id="gregtech:gt.foundrycasings:9"/>
- 20 <ItemLink id="gregtech:gt.blockcasings8:14" /> <ItemImage id="gregtech:gt.blockcasings8:14" />
- 19 <ItemLink id="miscutils:gtplusplus.blockcasings.3:10"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:10" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:985" /><ItemImage id="gregtech:gt.sheetmetal:985"/>
- 1 Girdi Kapağı (herhangi bir kriyojenik kasa) <ItemImage id="gregtech:gt.blockmachines:70" />

## Helyo Döküm Takviyesi <ItemImage id="gregtech:gt.foundrycasings:7" />
HR modülü (UIV), Exo-Foundry için UIV+ tariflerinin kilidini açar. Buna hipojen, eternity, universium veya Magmadde içeren tüm sıvı katılaştırıcı tarifleri ile aşkın düzeyde güçlendirilmiş borosilikat cam ve Hawking radyasyonu yeniden hizalama odak camı dahildir. Exo-Foundry başına HR modülü sayısında bir sınır yoktur. HR'yi kendisiyle eşleştirmek, aşağıdaki tabloda görüldüğü gibi toplam HR modülü sayısına bağlı olarak ölçeklenen bir bonus olan Süper Kararlı Çekirdek'i açar. 

| Modüller   | Bonuslar    |
|--------------- | --------------- |
| $$\geq$$ 1 HR   | UIV+ Tariflerini Açar   |
| $$\geq$$ 2 HR   | HR başına +%75 Hız   |
| $$\geq$$ 3 HR  | HR başına gerilim kademesi başına +6 Paralel, 0.1 Hız Aşırtma Faktörü   |
| 4 HR   | +2 Hız Aşırtma   |

### Gereksinimler:
- 32 <ItemLink id="tectech:gt.godforgecasing:3" /><ItemImage id="tectech:gt.godforgecasing:3" />
- 24 <ItemLink id="gregtech:gt.blockframes:147" /><ItemImage id="gregtech:gt.blockframes:147" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:588" /><ItemImage id="gregtech:gt.sheetmetal:588" />
- 16 <ItemLink id="tectech:tile.spatiallyTranscendentGravitationalLens" /> <ItemImage id="tectech:tile.spatiallyTranscendentGravitationalLens"/>
- 12 <ItemLink id="gregtech:gt.foundrycasings:7" /><ItemImage id="gregtech:gt.foundrycasings:7" />
- 12 <ItemLink id="gregtech:gt.blockframes:581"/><ItemImage id="gregtech:gt.blockframes:582"/>
- 12 <ItemLink id="gregtech:gt.blockframes:149"/><ItemImage id="gregtech:gt.blockframes:149"/>
- 12 <ItemLink id="gregtech:gt.blockframes:148"/><ItemImage id="gregtech:gt.blockframes:148"/>
- 12 <ItemLink id="gregtech:gt.blockframes:588"/><ItemImage id="gregtech:gt.blockframes:588"/>

## Bilinçli Hız Aşırtıcı <ItemImage id="gregtech:gt.foundrycasings:5"/>
SO modülü (UMV), makinenin hız aşırtma faktörünü 0.35 artırır. Yani aşağıdaki tabloda görüldüğü gibi her kusurlu hız aşırtma ek %35 hız sağlar. Exo-Foundry başına 1 SO modülü sınırı vardır. SO'yu Proto-Volt Dengeleyici modülüyle eşleştirmek, -%50 EU/t ve +0.1 hız aşırtma faktörü sağlayan tek seferlik bir bonus olan Harmonik Verimlilik'i açar. 
| Hız | 1 OC | 2 OC | 3 OC | 4 OC | 5 OC |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |
| Temel | 200% | 400% | 800% | 1,600% | 3,200% |
| $$\geq$$ 3 HR | 210% | 441% | 926% | 1,945% | 4,084% |
| 1 SO | 235% | 552% | 1,298% | 3,050% | 7,167% |
| 1 SO+ | 245% | 600% | 1,471% | 3,603% | 8,827% |

### Gereksinimler:
- 72 <ItemLink id="GoodGenerator:magneticFluxCasing"/><ItemImage id="GoodGenerator:magneticFluxCasing"/>
- 48 <ItemLink id="GoodGenerator:gravityStabilizationCasing"/><ItemImage id="GoodGenerator:gravityStabilizationCasing"/>
- 40 <ItemLink id="gregtech:gt.foundrycasings:5"/><ItemImage id="gregtech:gt.foundrycasings:5"/>
- 36 <ItemLink id="GoodGenerator:antimatterContainmentCasing"/><ItemImage id="GoodGenerator:antimatterContainmentCasing"/>
- 24 <ItemLink id="gregtech:gt.foundrycasings:1"/> <ItemImage id="gregtech:gt.foundrycasings:1"/>
- 16 <ItemLink id="gregtech:gt.blockframes:327"/> <ItemImage id="gregtech:gt.blockframes:327"/>

## Evrensel Çökertici <ItemImage id="gregtech:gt.foundrycasings:4"/>
UC modülü (UXV), güç tüketimini 4 katına, hızı 2 katına çıkarır ve asgari kasa sayısını 20 artırır. Bu pratikte zorunlu bir kusurlu hız aşırtma gibidir ve toplam 35 kalıp için yalnızca 5 girişlik alan bırakır. Exo-Foundry başına 1 UC modülü sınırı vardır. UC'yi Aşırı Soğutucu modülüyle eşleştirmek, Eternity'nin 3 ek hız aşırtmaya kadar soğutucu olarak kullanılmasını sağlayan, güç tüketimini 2 katına ve hızı 2 katına çıkaran tek seferlik bir bonus olan Gerçekleşen Potansiyel'i açar. 

### Gereksinimler:
- 72 <ItemLink id="tectech:gt.blockcasingsBA0:11"/> <ItemImage id="tectech:gt.blockcasingsBA0:11"/>
- 48 <ItemLink id="tectech:gt.blockcasingsBA0:10"/><ItemImage id="tectech:gt.blockcasingsBA0:10"/>
- 40 <ItemLink id="gregtech:gt.blockframes:583" /> <ItemImage id="gregtech:gt.blockframes:583" />
- 28 <ItemLink id="gregtech:gt.blockmetal9:6"/><ItemImage id="gregtech:gt.blockmetal9:6"/>
- 28 <ItemLink id="gregtech:gt.blockmetal9:7"/><ItemImage id="gregtech:gt.blockmetal9:7"/>
- 16 <ItemLink id="gregtech:gt.blockframes:139"/><ItemImage id="gregtech:gt.blockframes:139"/>
- 8 <ItemLink id="gregtech:gt.blockframes:585"/><ItemImage id="gregtech:gt.blockframes:585"/>
- 8 <ItemLink id="gregtech:gt.blockframes:586"/><ItemImage id="gregtech:gt.blockframes:586"/>
- 4 <ItemLink id="gregtech:gt.foundrycasings:4"/><ItemImage id="gregtech:gt.foundrycasings:4"/>
- 4 <ItemLink id="gregtech:gt.blockmetal9:13"/><ItemImage id="gregtech:gt.blockmetal9:13"/>

## Eşleştirmeler
Exo-Foundry'ye ek bonuslar sağlayan dört özgün modül eşleştirmesi vardır. Bunların hepsi yukarıdaki modül alt bölümlerinde anlatıldı; burada referans için özetlenmiştir. Her modülden iki tane olsa bile bu bonuslar yalnızca bir kez uygulanır. Örneğin iki ECB ve iki SC'ye sahip olmak Optimum Üretim'den gelen bonusu İKİYE KATLAMAZ. 

- Optimum Üretim: Süper Yoğun Döküm Havuzu + Akıcı Döküm - gerilim kademesi başına +6 Paralel, +%75 Hız
- Harmonik Verimlilik: Proto-Volt Dengeleyici + Bilinçli Hız Aşırtıcı - -%50 EU/t, +0.1 Hız Aşırtma Faktörü
- Süper Kararlı Çekirdek: Helyo Döküm Takviyesi + Helyo Döküm Takviyesi - HR miktarına göre değişir (Özel bölüme bak)
- Gerçekleşen Potansiyel: Evrensel Çökertici + Aşırı Soğutucu - Eternity Soğutucusunu Açar, x2 EU/t, x2 Hız

## Optimal Kurulumlar
Pek çok olası modül kombinasyonu vardır ve hangilerinin en etkili olduğu tam olarak belli değildir. Aralarında karar vermene yardımcı olmak için aşağıdaki tablolar, oyunun farklı aşamalarında öne çıkan birkaç kombinasyonu karşılaştırır. Kapak alanları yalnızca bir enerji kapağı varsayar ve göreli işlem hacimleri, N'nin tarifin üzerindeki gerilim kademesi sayısı olduğu aşağıdaki denklemle hesaplanır.
<Latex formula="\text{Throughput} = \text{Parallels} \times \text{Speed} \times (\text{OC Factor})^N \times 2^{\text{Bonus OC}}" />

UIV+ tariflerini çalıştırmak için en az bir HR modülü gerekir; ancak en optimal kurulumlarda bu her zaman bulunmaz. Bu yüzden en az iki Exo-Foundry'ye sahip olman ve tarifleri gerilim kademelerine göre ayırman önerilir. 

Her gerilim kademesine özel optimal kurulumlar için [Wiki Sayfası!](https://wiki.gtnewhorizons.com/wiki/Exo-Foundry) bağlantısının alt bölümlerine bak.