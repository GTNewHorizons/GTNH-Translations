---
item_ids:
  - gregtech:gt.blockmachines:15513
navigation:
  title: Amazon Depolama Tesisi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15513
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-16
---

# Amazon Depolama Tesisi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15513"/>
</GameScene>
<Color id="GREEN">Amazon Depolama Tesisi (AWD)</Color>, çeşitli eşyaları paketleyip paketlerini açmak için IV kademesi bir multibloktur. Tek bloklu paketleyicinin doğrudan yükseltmesidir: <Color id="GREEN">%900</Color> hıza kadar çalışır, normalde gereken EU/t'nin yalnızca <Color id="RED">%75</Color>'ini kullanır ve <Color color="#ed6401">16</Color> paralel sunar.

<Color id="GREEN">AWD</Color> hem paketleme hem de paket açma tariflerini işleyebilir ve tek bloklu selefine göre her açıdan __çok__ daha hızlıdır.

<br clear="all"/>

> [!NOTE]
> Multiblokta aşağıdaki değişiklikler yapıldı (yapı dışında):
> - Kademeli Hız: Tarif hızı artık eşya boru muhafazası kademesine bağlı olarak %200-900 arasında (eski maksimum %600 idi)

## İnşa
<Color id="GREEN">AWD</Color>'nin kademeli tek bir bileşeni vardır. Eşya boru muhafazaları makinenin hız bonusunu belirler. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Bu bileşenlerin kademesini belirtmek üzere "item_pipe" ve "glass" alt kanallarıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15513" /> <ItemImage id="gregtech:gt.blockmachines:15513" />
- 4-15 <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" /> <ItemImage id="miscutils:gtplusplus.blockcasings.3:9" />
- 3 Eşya Boru Muhafazası <ItemImage id="gregtech:gt.blockcasings11:5" />
- 3 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 2 <ItemLink id="gregtech:gt.blockframes:32" /> <ItemImage id="gregtech:gt.blockframes:32" />
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı:
<Color id="GREEN">AWD</Color>'ler kasa, çerçeve kutusu ve veriyolu/kapak tasarrufu için her bir yanlarını duvar paylaşımıyla kullanabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">AWD</Color>, tek bloklu paketleyici ve paket açıcıya göre doğrudan bir yükseltmedir; çünkü her iki tarif türünü de işleyebilir, <Color id="GREEN">%900</Color> hıza kadar çalışır, normalde gereken EU/t'nin yalnızca <Color id="RED">%75</Color>'ini kullanır ve aşağıdaki tablolarda görüldüğü gibi gerilim kademesi başına <Color color="#ed6401">16</Color> paralel sunar.
| Kademe | Eşya Boru Muhafazası | Hız |
| --------------- | --------------- | --------------- |
| 1 | Kalay | %200 |
| 2 | Pirinç | %300 |
| 3 | Elektrum | %400 |
| 4 | Platin | %500 |
| 5 | Osmiyum | %600 |
| 6 | Kuantinyum | %700 |
| 7 | Fluxlu Elektrum | %800 |
| 8 | Kara Plütonyum | %900 |

----------


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |