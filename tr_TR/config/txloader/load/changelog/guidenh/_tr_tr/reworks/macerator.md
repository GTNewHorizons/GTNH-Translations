---
item_ids:
  - gregtech:gt.blockmachines:15539
navigation:
  title: Endüstriyel Öğütme Yığını
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15539
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Öğütme Yığını

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15539"/>
</GameScene>

<Color id="GREEN">Endüstriyel Öğütme Yığını (IMS)</Color>, eşyaları tozlara kırmak ve öğütmek için EV kademesinde bir multibloktur. <Color id="GREEN">IMS</Color>, tek bloklu öğütücüye ve Buharlı Öğütücüye doğrudan bir yükseltmedir çünkü iki kademede bulunur ve kademeye göre artan bonusları vardır. T1 yapısı <Color id="BLUE">%160</Color> hızda çalışır ve gerilim kademesi başına <Color id="RED">2</Color> paralel sunar. T2 yapısı <Color id="BLUE">%640</Color> hızda çalışır ve gerilim kademesi başına <Color id="RED">8</Color> paralel sunar. <Color id="GREEN">IMS</Color> öğesini kontrolcüye bir öğütme yükseltme çipi <ItemImage id="miscutils:MU-metaitem.01:32152"/> yerleştirerek ya da çip elindeyken kontrolcüye sağ tıklayarak yükselt.
<br clear="all"/>

> [!NOTE]
> Multibloğa (yapı dışında) şu değişiklikler yapıldı:
> - T1 hiçbir şekilde değiştirilmedi.
> - T2: Yeni yapı, artırılmış hız (%160->%640)

## İnşa
<Color id="GREEN">IMS</Color> iki kademede bulunur. T1 yapısında kademeli bileşen yoktur ve veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir kasayı değiştirebilir. T2 yapısında da kademeli bileşen yoktur ve veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir öğütme yığını kasasını değiştirebilir. Cam herhangi bir kademede olabilir ve makinenin çalışmasını etkilemez. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan; camın kademesini belirtmek için "glass" alt kanalını, hangi kademeyi inşa edeceğini belirtmek için de tek bir yığında tutulan projektör sayısını kullan.

### T1 Gereksinimleri:
- 1 <ItemLink id="gregtech:gt.blockmachines:15539"/><ItemImage id="gregtech:gt.blockmachines:15539"/>
- 26-44 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### T2 Gereksinimleri:
- 1 <ItemLink id="gregtech:gt.blockmachines:15539"/><ItemImage id="gregtech:gt.blockmachines:15539"/>
- 69-87 <ItemLink id="miscutils:miscutils.blockcasings:7"/><ItemImage id="miscutils:miscutils.blockcasings:7"/>
- 20 <ItemLink id="gregtech:gt.blockframes:372"/><ItemImage id="gregtech:gt.blockframes:372"/>
- 18 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 8 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 6 <ItemLink id="gregtech:gt.blockcasings3:10"/><ItemImage id="gregtech:gt.blockcasings3:10"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">IMS</Color> yapıları, kasa, çerçeve kutusu, cam ve veriyolu/kapaklardan tasarruf etmek için kenarlarını duvar paylaşımıyla birleştirebilir. Hiçbir tarif 1A'dan fazla güç kullanmaz; bu yüzden <u>__tek bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">IMS</Color>, tek bloklu öğütücüye ve Buharlı Öğütücüye doğrudan bir yükseltmedir çünkü iki kademede bulunur ve kademeye göre artan bonusları vardır. T1 yapısı %160 hızda çalışır ve gerilim kademesi başına 2 paralel sunar. T2 yapısı %640 hızda çalışır ve gerilim kademesi başına 8 paralel sunar. IMS öğesini kontrolcüye bir <ItemLink id="miscutils:MU-metaitem.01:32152"/><ItemImage id="miscutils:MU-metaitem.01:32152"/> yerleştirerek ya da çip elindeyken kontrolcüye sağ tıklayarak yükselt. Çip anında tüketilir ve geri alınamaz. 

### Paraleller:

|   | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| T1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 |
| T2 | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |