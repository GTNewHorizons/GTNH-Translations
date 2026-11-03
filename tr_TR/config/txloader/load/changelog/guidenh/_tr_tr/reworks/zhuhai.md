---
item_ids:
  - gregtech:gt.blockmachines:15544
navigation:
  title: Zhuhai Balıkçı Limanı
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15544
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Zhuhai Balıkçı Limanı

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15544"/>
</GameScene>
<Color id="GREEN">Zhuhai Balıkçı Limanı</Color>, balık ve diğer muhtelif ganimetlerin seri üretimi için kullanılan bir IV kademesi multibloğudur. <Color id="GREEN">Zhuhai</Color>, tek bloklu Balık Yakalayıcıya göre doğrudan bir yükseltmedir <ItemImage id="miscutils:blockFishTrap"/> çünkü overclocklarıyla önemli ölçüde daha hızlıdır ve $$2 \times (\text{Tier} + 1)$$ paralel sunar. Makinenin tek girdisi güçtür ve çıktılar tamamen rastgeledir. Mevcut üç tarifin (balık, çöp veya hazine) her birinin kendine özgü ganimet tablosu vardır ve kontrolcüdeki veya Giriş Yolundaki belirli bir Programlanmış Devre ile seçilir.
<br clear="all"/>

> [!NOTE]
> Yalnızca yapının kendisi değişti; multibloğun temel işlevselliği öncekiyle aynıdır

## İnşa
<Color id="GREEN">Zhuhai</Color>'nin kademeli bileşeni yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Su, makineyi ilk çalıştırmak için tek seferlik bir maliyettir ve yapıya bir rezervuar kapağı veya Girdi Kapağı aracılığıyla verilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15544"/><ItemImage id="gregtech:gt.blockmachines:15544"/>
- 160-167 <ItemLink id="miscutils:gtplusplus.blockcasings.3"/><ItemImage id="miscutils:gtplusplus.blockcasings.3"/>
- 12 <ItemLink id="gregtech:gt.sheetmetal:306"/><ItemImage id="gregtech:gt.sheetmetal:306"/>
- 12 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Zhuhai Balıkçı Limanları</Color> kasa ve veriyolu/kapaktan tasarruf etmek için her yüzünü duvar paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığı için <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağı paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">Zhuhai</Color>, tek bloklu Balık Yakalayıcıya göre doğrudan bir yükseltmedir çünkü overclocklarıyla önemli ölçüde daha hızlıdır ve aşağıdaki tabloda görüldüğü gibi $$2 \times (\text{Tier} + 1)$$ paralel sunar.
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 |