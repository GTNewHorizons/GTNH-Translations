---
item_ids:
  - gregtech:gt.blockmachines:15538
navigation:
  title: Büyük Termal Rafineri
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15538
categories:
    - Yapı Revizyonları
author: Skorched
date: 2026-05-23
---

# Büyük Termal Rafineri

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15538"/>
</GameScene>
<Color id="GREEN">Büyük Termal Rafineri (LTR)</Color>, ezilmiş cevherleri rafine etmek ve tükenmiş yakıt çubuklarını geri dönüştürmek için EV kademesinde bir multibloktur. <Color id="GREEN">LTR</Color>, tek blok termal santrifüjden doğrudan bir yükseltmedir; çünkü %<Color id="RED">320</Color>'ye varan hızda çalışır, normalde gereken EU/t'nin yalnızca %<Color id="BLUE">39</Color>'u kadarını kullanır ve voltaj kademesi başına <Color color="#ed6401">8</Color> paralel ile solenoid kademesi başına 2 paralel sunar. Ayrıca her Isıtma Bobini kademesi %5 hız bonusu (toplamalı) ve %5 EU/t indirimi (çarpımsal) verir. 

<br clear="all"/>

> [!NOTE]
> Yeni yapı dışında, multiblokta aşağıdaki değişiklikler yapılmıştır:
> - Kademeli Bobinler: kademe başına %5 toplamalı hız bonusu, kademe başına %5 çarpımsal güç azaltımı
> - Kademeli Solenoidler: solenoid kademesi başına 2 paralel

## Yapım
<Color id="GREEN">LTR</Color> iki kademeli bileşenden oluşur. <Color id="RED">Isıtma Bobinleri</Color> makinenin hız bonusunu ve enerji indirimini artırır. <Color id="BLUE">Solenoidler</Color> paralel sayısını artırır. Cam herhangi bir kademede olabilir ve makinenin çalışması üzerinde etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki termal işlem kasasının yerine geçebilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı kullanılabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan ve bu bileşenlerin kademesini belirtmek için "coil", "solenoid" ve "glass" alt kanallarını ver. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15538" /> <ItemImage id="gregtech:gt.blockmachines:15538" />
- 85-92 <ItemLink id="miscutils:gtplusplus.blockcasings.2" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2" />
- 20 <ItemLink id="gregtech:gt.blockframes:348" /> <ItemImage id="gregtech:gt.blockframes:348" />
- 16 Isıtma Bobini <ItemImage id="gregtech:gt.blockcasings5:11" />
- 6 Solenoid Süperiletken Bobini <ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:10" />
- 6 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 4 <ItemLink id="gregtech:gt.blockcasings:11" /> <ItemImage id="gregtech:gt.blockcasings:11" />
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">LTR</Color>'ler kasa, cam, çerçeve kutusu ve yol/kapaklardan tasarruf etmek için her bir yanında duvar paylaşımı yapabilir. Birçok tarif 2A güç kullanır, bu nedenle en az Fluxed Elektrum bobinleri olmadan <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak MÜMKÜN DEĞİLDİR. 

## Kullanım
<Color id="GREEN">LTR</Color>, tek blok termal santrifüjden doğrudan bir yükseltmedir; çünkü %<Color id="RED">320</Color>'ye varan hızda çalışır, normalde gereken EU/t'nin yalnızca %<Color id="BLUE">39</Color>'u kadarını kullanır ve aşağıdaki tabloda görüldüğü gibi voltaj kademesi başına <Color color="#ed6401">8</Color> paralel ile solenoid kademesi başına <Color id="GREEN">2</Color> paralel sunar. Ayrıca her Isıtma Bobini kademesi %5 hız bonusu (toplamalı) ve %5 EU/t indirimi (çarpımsal) verir. 
### Isıtma Bobinleri:
|  Bobin | Hız | EU/t |
| --------------- | --------------- | --------------- |
| Bakır-Nikel | 255% | 76.0% |
| Kantal | 260% | 72.2% |
| Nikrom | 265% | 68.6% |
| TPV-Alaşım | 270% | 65.2% |
| HSS-G | 275% | 61.9% |
| HSS-S | 280% | 58.8% |
| Naquadah | 285% | 55.9% |
| Naquadah Alaşım | 290% | 53.1% |
| Trinyum | 295% | 50.4% |
| Fluxed Elektrum | 300% | 47.9% |
| Uyandırılmış Drakonyum | 305% | 45.5% |
| Sonsuzluk | 310% | 43.2% |
| Hipojen | 315% | 41.1% |
| Ebedi | 320% | 39.0% |

### Solenoidler:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
|--------------- | -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| MV | 12 | 20 | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 |
| HV | 14 | 22 | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 |
| EV | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 |
| IV | 18 | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 | 106 | 114 | 122 | 130 |
| LuV | 20 | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 | 132 |
| ZPM | 22 | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 | 134 |
| UV | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 | 136 |
| UHV | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 | 106 | 114 | 122 | 130 | 138 |
| UEV | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 | 132 | 140 |
| UIV | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 | 134 | 142 |
| UMV | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 | 136 | 144 |