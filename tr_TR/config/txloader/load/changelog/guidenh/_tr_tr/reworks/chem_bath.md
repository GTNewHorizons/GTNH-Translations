---
item_ids:
  - gregtech:gt.blockmachines:15551
navigation:
  title: Endüstriyel Kimyasal Banyo
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15551
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Kimyasal Banyo

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15551"/>
</GameScene>
<Color id="GREEN">Endüstriyel Kimyasal Banyo (ICB)</Color>, çeşitli malzemeleri kimyasal banyodan geçirmek için kullanılan EV kademe bir multibloktur. <Color id="GREEN">ICB</Color>, tek blok kimyasal banyonun doğrudan yükseltmesidir; çünkü <Color id="RED">%500</Color> hızda çalışır ve gerilim kademesi başına <Color id="BLUE">4</Color> paralel sunar.

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> - Ayrıştırma: Cevher Yıkama Tesisi ayrı yapılara bölündü (bu yapı gibi!)

## İnşa
<Color id="GREEN">ICB</Color>'nin kademeli bileşeni yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki yıkama tesisi kasasının yerini alabilir. <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Su, makineyi ilk kez çalıştırmak için tek seferlik bir maliyettir ve yapıya bir rezervuar kapağı veya girdi kapağı aracılığıyla verilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15551"/><ItemImage id="gregtech:gt.blockmachines:15551"/>
- 30-38 <ItemLink id="miscutils:gtplusplus.blockcasings.2:4"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:4"/>
- 20 <ItemLink id="miscutils:blockFrameGtWatertightSteel"/><ItemImage id="miscutils:blockFrameGtWatertightSteel"/>
- 4 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 2 <ItemLink id="gregtech:gt.blockmetal8:6"/><ItemImage id="gregtech:gt.blockmetal8:6"/>
- 2 <ItemLink id="gregtech:gt.blockmetal2:7"/><ItemImage id="gregtech:gt.blockmetal2:7"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">ICB</Color>'ler kasa ve veriyolu/kapaktan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Buna su sağlamak için kullanılan rezervuar kapağı da dahildir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">ICB</Color>, tek blok kimyasal banyonun doğrudan yükseltmesidir; çünkü aşağıdaki tabloda görüldüğü gibi %500 hızda çalışır ve gerilim kademesi başına 4 paralel sunar.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |