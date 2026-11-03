---
item_ids:
  - gregtech:gt.blockmachines:15512
navigation:
  title: Endüstriyel Santrifüj
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15512
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Santrifüj

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15512"/>
</GameScene>
<Color id="GREEN">Endüstriyel Santrifüj (IC)</Color>, tozları, sıvıları ve diğer eşyaları bileşenlerine ayırmak için kullanılan EV kademesi bir multibloktur. Tek blok santrifüje göre doğrudan bir yükseltmedir. ZPM kademesinde yerini <Color id="RED">Spinmatron-2737</Color> alır.
<br clear="all"/>

> [!NOTE]
> Bu multibloktaki değişiklikler nispeten küçüktür; daha büyük bir temel yapıya sahip olduğu için kapak yerleşimi için daha fazla alan vardır. İnşa maliyeti ve yeni tasarım dışında, bu makinenin işlevselliğine dokunulmadı!

## Yapım
<Color id="GREEN">Endüstriyel Santrifüj</Color> tek tip kasadan oluşur, ancak yapısında <Color id="RED">Elek Izgaraları</Color> ve <Color id="BLUE">Eglin Çeliği Çerçeve Kutuları</Color> kullanır. Veriyolları/kapaklar yapıdaki herhangi bir kasanın yerine geçebilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı kullanılabilir. Animasyonları devre dışı bırakmak için kontrolcüye tornavidayla sağ tıkla. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15512" /> <ItemImage id="gregtech:gt.blockmachines:15512" />
- 6-32 <ItemLink id="miscutils:miscutils.blockcasings" /> <ItemImage id="miscutils:miscutils.blockcasings" />
- 24 <ItemLink id="miscutils:blockFrameGtEglinSteel" /> <ItemImage id="miscutils:blockFrameGtEglinSteel" />
- 18 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:6" />
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Endüstriyel Santrifüjler</Color>, kasa, çerçeve kutusu ve veriyolu/kapaktan tasarruf etmek için her bir yüzlerini duvar paylaşımıyla kullanabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">Endüstriyel Santrifüj</Color>, %225 hızda çalıştığı, normalde gereken EU/t'nin yalnızca %90'ını kullandığı ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 6 paralel sunduğu için tek blok santrifüje göre doğrudan bir yükseltmedir.
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |