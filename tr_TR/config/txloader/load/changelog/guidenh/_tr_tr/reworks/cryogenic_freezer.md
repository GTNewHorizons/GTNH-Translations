---
item_ids: 
  - gregtech:gt.blockmachines:15565
navigation:
  title: Kriyojenik Dondurucu
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15565
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Kriyojenik Dondurucu 

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15565"/>
</GameScene>

<Color id="GREEN">Kriyojenik Dondurucu (CF)</Color>, sıcak külçeleri ve sıvıları toplu olarak soğutmak için IV kademe bir multibloktur. <Color id="GREEN">CF</Color>, Vakum Dondurucudan doğrudan bir yükseltmedir çünkü <Color id="BLUE">%300</Color> hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="GREEN">%90</Color>'ını kullanır ve sabit <Color id="RED">16</Color> paralel sunar. <Color id="GREEN">CF</Color>, çalışma sırasında özel bir Kriyotheum soğutma kapağı üzerinden 10 L/s gelid Kriyotheum tüketir. Eğer tükenirse makine anında çöker ve rastgele bir bakım sorununun oluşmasına neden olur. [Endotermik Buzdolabı](../multis/endothermic_fridge.md), Kriyojenik Dondurucuyu ancak 256 paralelinden (4+ overclock) tam olarak yararlanabildiğinde veya alt uzay soğutması kullanabildiğinde geride bırakır. 
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> - Daha yüksek hız: 220% -> 300%
> - Daha fazla paralel: 8 -> 16

## İnşaat
<Color id="GREEN">Kriyojenik Dondurucu</Color>'nun kademeli bileşenleri yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. <Color id="RED">Çok Amperli ve Lazerli Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15565"/><ItemImage id="gregtech:gt.blockmachines:15565"/>
- 46-56 <ItemLink id="miscutils:gtplusplus.blockcasings.3:10"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:10"/>
- 24 <ItemLink id="miscutils:blockFrameGtGrisium"/><ItemImage id="miscutils:blockFrameGtGrisium"/>
- 1+ <ItemLink id="gregtech:gt.blockmachines:967"/><ItemImage id="gregtech:gt.blockmachines:967"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Kriyojenik Dondurucular</Color> kasa, çerçeve kutusu, yol ve kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığından <u>__tek__</u> bir enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Kriyojenik Dondurucu</Color>, %300 hızda çalıştığı, normalde gereken EU/t'nin yalnızca %90'ını kullandığı ve sabit 16 paralel sunduğu için Vakum Dondurucudan doğrudan bir yükseltmedir.

<Color id="GREEN">Kriyojenik Dondurucu</Color>, çalışma sırasında özel bir Kriyotheum soğutma kapağı üzerinden 10 L/s gelid Kriyotheum tüketir. Eğer tükenirse makine anında çöker ve rastgele bir bakım sorununun oluşmasına neden olur. Kriyotheum esas olarak Europa'daki evrimleşmiş soğuk blaze'lerden veya Kriyotheum arısından elde edilir. Gerekirse blaze tozundan Blizz tozu da yapılabilir. 