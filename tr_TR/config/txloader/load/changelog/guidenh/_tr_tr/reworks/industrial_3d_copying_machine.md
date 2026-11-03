---
item_ids:
  - gregtech:gt.blockmachines:15554
navigation:
  title: Endüstriyel 3D Kopyalama Makinesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15554
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel 3D Kopyalama Makinesi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15554"/>
</GameScene>
<Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>, blokları dekoratif varyantlarına dönüştürmek için keski işlemi yapan bir EV kademesi Multibloktur. <Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>, tek bloklu otomatik keskinin doğrudan yükseltmesidir; çünkü <Color id="RED">%300</Color> Hız ile çalışır, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%75</Color>'ini kullanır ve Gerilim kademesi başına <Color id="GREEN">16</Color> paralel sunar. Hedef blok, Giriş Yolundaki veya Kontrolcüdeki programlanmış bir Devre ile ya da Keski Yolu kullanılıyorsa bloğun kendisiyle seçilir. 
<br clear="all"/>

> [!NOTE]
> Yeni yapı dışında bu Multiblokta mekanik bir değişiklik yoktur

## Yapım
<Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>'nin kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışması üzerinde hiçbir etkisi yoktur. Isıtma Bobini özellikle Bakır-Nikel olmalıdır ve onun da makinenin çalışması üzerinde hiçbir etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki Dayanıklı Yazıcı Kasasının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal Enerji Kapağı olabilir. Yapıyı "glass" alt kanalıyla görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan; bu, Camın kademesini belirtir.

<Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>'ye özgü olan Keski Yolu, hedef bloğu belirtmek için bir ek yuvaya sahip Büyük bir Giriş Yolu niteliğindedir. Hedef blok fiziksel olarak Keski Yolunun içine yerleştirilmelidir; bu da onu normal bir Giriş Yolunda programlanmış Devre kullanmaya göre pek de iyi bir alternatif yapmaz. Üç kademede Keski Yolu vardır (LV, MV, HV) ve tek fark yuva sayılarıdır (32, 48, 64). 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15554"/><ItemImage id="gregtech:gt.blockmachines:15554"/>
- 40-48 <ItemLink id="miscutils:gtplusplus.blockcasings.5:5"/><ItemImage id="miscutils:gtplusplus.blockcasings.5:5"/>
- 37 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 18 Kademeli Cam (herhangi) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1 <ItemLink id="IC2:blockFenceIron"/><ItemImage id="IC2:blockFenceIron"/>
- 1 <ItemLink id="gregtech:gt.blockcasings5"/><ItemImage id="gregtech:gt.blockcasings5"/>
- 1+ Enerji Kapağı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Keski Yolu (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:31778"/>
- 0+ Çıkış Yolu (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Endüstriyel 3D Kopyalama Makineleri</Color> kasa, çerçeve kutusu, Cam ve yol/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımıyla kullanabilir. Hiçbir Tarif 1A'dan fazla Güç kullanmadığı için <u>__iki__</u> makine arasında <u>__tek__</u> bir Enerji Kapağı paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>, tek bloklu otomatik keskinin doğrudan yükseltmesidir; çünkü %300 Hız ile çalışır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve aşağıdaki tabloda görüldüğü gibi Gerilim kademesi başına 16 paralel sunar.

### Paralleller:

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |


Her keski Tarifinin temel süresi 1.0sn'dir ve herhangi bir hız aşırtma veya Hız bonusu öncesinde 16 EU/t (LV) tüketir. <Color id="GREEN">Endüstriyel 3D Kopyalama Makinesi</Color>, Tariflerin Çıktısını belirlemek için programlanmış bir Devre kullanır; ancak Keski Yolu kullanılıyorsa bunun yerine hedef blok gerekir. İkincisi önerilmez çünkü hedef blok üretilmeli ve fiziksel olarak Keski Yolunun içine yerleştirilmelidir--NEI'den sürüklemek ÇALIŞMAZ. Hedef blok belirtilmezse makine mevcut bir sonraki keski Tarifine geçer. 