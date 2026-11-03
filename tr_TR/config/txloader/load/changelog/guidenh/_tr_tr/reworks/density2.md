---
item_ids:
  - gregtech:gt.blockmachines:15547
navigation:
  title: Density^2
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15547
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Density^2

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15547"/>
</GameScene>
<Color id="GREEN">Density^2</Color>, patlayıcılarla plakaları ve tozları sıkıştıran IV kademe bir Multibloktur. <Color id="GREEN">Density^2</Color>, <Color id="RED">%200</Color> hızda çalıştığı, yarısı kadar kirlilik ürettiği ve her iki gerilim kademesi için bir paralel sunduğu için Patlama Kompresörünün <ItemImage id="gregtech:gt.blockmachines:1001"/> doğrudan yükseltmesidir. <Color id="GREEN">Density^2</Color>'nin yerini UHV'de [Elektrik Patlama Kompresörü](./eic.md) <ItemImage id="gregtech:gt.blockmachines:15563"/> alır. 
<br clear="all"/>

> [!NOTE]
> Bu Multiblokta yalnızca yapı değişti, mekanikler aynı kalıyor

## İnşaat
<Color id="GREEN">Density^2</Color>'nin kademeli bileşenleri yoktur. Yollar/kapaklar yapının herhangi bir yerindeki Tungsten Çeliği Makine Gövdesinin yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı bulunabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15547"/><ItemImage id="gregtech:gt.blockmachines:15547"/>
- 80 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 50-60 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 24 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 4 <ItemLink id="gregtech:gt.sheetmetal:86"/><ItemImage id="gregtech:gt.sheetmetal:86"/>
- 4 <ItemLink id="gregtech:gt.blockframes:86"/><ItemImage id="gregtech:gt.blockframes:86"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Density^2</Color>'ler kasa, çerçeve kutusu, İşlenmiş Grafit Blokları ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımı yapabilir. Buna tüm grafit küresi dahil DEĞİLDİR. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Density^2</Color>, yarısı kadar kirlilik ürettiği, iki kat daha hızlı çalıştığı ve aşağıdaki tabloda görüldüğü gibi her iki gerilim kademesi için bir paralel sunduğu için Patlama Kompresörünün <ItemImage id="gregtech:gt.blockmachines:1001"/> doğrudan yükseltmesidir.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 7 | 7 | 8 | 8 |


Patlama kompresörü tariflerinin tümü LV'dir ve aşağıda listelenen patlayıcılardan birini gerektirir. Patlayıcı sayısı tipe ve tarife bağlıdır. Barut fıçıları diğerlerinden çok daha yüksek miktarlarda gerekir, ancak barutu karbondan, sülfürden ve güherçileden üretmek çok kolaydır. TNT ve endüstriyel TNT çoğunlukla sadece toluendir; bu da odun katranı ve/veya ağır yakıtın damıtılmasıyla elde edilir. Dinamit çoğunlukla sadece gliseroldür; bu da tohum/balık yağından gelen yenilenebilir bir kaynaktır. Ancak en iyi ve en yenilenebilir seçenek, patlayıcı arısını kullanarak doğrudan çok miktarda endüstriyel TNT'yi pasif olarak üretmektir -- hiç kimya gerekmez.

- Barut Fıçısı
- TNT
- Dinamit
- Endüstriyel TNT