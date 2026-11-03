---
item_ids:
  - gregtech:gt.blockmachines:15553
navigation:
  title: Endüstriyel Bükme Makinesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15553
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Bükme Makinesi
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15553"/>
</GameScene>

<Color id="GREEN">Endüstriyel Bükme Makinesi (IBM)</Color>, külçeleri levhaya bükmek için EV kademesinde bir multibloktur. <Color id="GREEN">IBM</Color>, tek bloklu bükme makinesinin doğrudan yükseltmesidir çünkü <Color id="RED">%600</Color> hızda çalışır ve gerilim kademesi başına <Color id="BLUE">6</Color> paralel sunar. Aynı makine içinde farklı programlanmış devreler kullanmak için <Color id="GREEN">IBM</Color> üzerinde giriş ayrıştırması etkinleştirilmelidir.

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapıldı:
> - Makinelerin Ayrıştırması: Bükme ve Şekillendirme işlevleri iki ayrı multibloğa ayrıldı ([Endüstriyel Şekillendirme Presine bak](forming.md))
> - Daha Fazla Paralel: Gerilim Kademesi başına 4 -> 6

## İnşaat
<Color id="GREEN">IBM</Color> makinesinin kademeli bileşenleri yoktur. Giriş/çıkış yolları ve kapaklar yapının herhangi bir yerindeki herhangi bir Metal İşleme Makine Gövdesinin yerini alabilir. <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15553"/>
- 4-15 <ItemLink id="miscutils:miscutils.blockcasings:4"/><ItemImage id="miscutils:miscutils.blockcasings:4"/>
- 9 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 6 <ItemLink id="gregtech:gt.blockframes:28"/><ItemImage id="gregtech:gt.blockframes:28"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">IBM'ler</Color> kasa, çerçeve kutusu, damgalama çekirdeği ile giriş/çıkış yolu ve kapaklardan tasarruf için her bir yüzünü duvar paylaşımında kullanabilir. Hiçbir tarif 1 A'dan fazla güç kullanmaz, bu yüzden <u>__tek__</u> bir enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">IBM</Color>, tek bloklu bükme makinesinin doğrudan yükseltmesidir çünkü %600 hızda çalışır ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 6 paralel sunar.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |


Giriş ayrıştırması, farklı Giriş Yollarındaki KATI bileşenlerin, programlanmış devreler dahil, aynı tarifte kullanılmasını önlemek için <Color id="GREEN">IBM</Color> üzerinde etkinleştirilmelidir. Bu, çok sayıda Giriş Yoluna sahip tek bir <Color id="GREEN">IBM</Color> makinesinin aynı anda birçok farklı programlanmış devreyi destekleyebileceği anlamına gelir. Yalnızca minimum Metal İşleme Makine Gövdesi sayısının üzerinde kalmayı unutma.

Bükme makinesi tariflerinde en yaygın programlanmış devreler 1, 2, 3, 4, 5, 9 ve 10'dur.