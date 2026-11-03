---
item_ids:
  - gregtech:gt.blockmachines:15514
navigation:
  title: Endüstriyel Elektrolizör
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15514
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Elektrolizör

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15514"/>
</GameScene>
<Color id="GREEN">Endüstriyel Elektrolizör</Color>, tozları ve sıvıları alt bileşiklerine veya bileşen elementlerine elektroliz etmek için kullanılan bir IV kademesi multibloktur (ör. metanı karbona ve hidrojene). <Color id="GREEN">Endüstriyel Elektrolizör</Color>, %280 hızda çalıştığı, normalde gereken EU/t'nin yalnızca %90'ını kullandığı ve gerilim kademesi başına 4 paralel sunduğu için tek bloklu elektrolizörün doğrudan yükseltmesidir. 

<br clear="all"/>

> [!NOTE]
> Önceki sürümden tek fark (yapının kendisi dışında), artık Gerilim Kademesi başına 4 paralel sunmasıdır. Hepsi bu!

## İnşaat
<Color id="GREEN">Endüstriyel Elektrolizör</Color>'ün kademeli bileşeni yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki elektrolizör kasasının yerine geçebilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15514" /> <ItemImage id="gregtech:gt.blockmachines:15514" />
- 6-43 <ItemLink id="miscutils:miscutils.blockcasings:5" /> <ItemImage id="miscutils:miscutils.blockcasings:5" />
- 12 <ItemLink id="miscutils:blockFrameGtPotin" /> <ItemImage id="miscutils:blockFrameGtPotin" />
- 4 <ItemLink id="gregtech:gt.blockcasings11" /> <ItemImage id="gregtech:gt.blockcasings11" />
- 4 <ItemLink id="gregtech:gt.blockcasings11:1" /> <ItemImage id="gregtech:gt.blockcasings11:1" />
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Endüstriyel Elektrolizör</Color>, kasa, çerçeve kutusu ve veriyolu/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımına açabilir. Buna her iki yandaki eşya boru kasaları da dahildir, ancak kontrolcülerden biri önce yatay olarak çevrilmeden (anahtarla eğilerek sağ tıkla) değiştirilemezler. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Endüstriyel Elektrolizör</Color>, <Color id="GREEN">%280</Color> hızda çalıştığı, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%90</Color>'ını kullandığı ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına <Color color="#ed6401">4</Color> paralel sunduğu için tek bloklu elektrolizörün doğrudan yükseltmesidir. 


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |