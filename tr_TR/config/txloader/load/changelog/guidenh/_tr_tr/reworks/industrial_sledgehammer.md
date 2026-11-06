---
item_ids:
  - gregtech:gt.blockmachines:15555
navigation:
  title: Endüstriyel Balyoz
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15555
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---
# Endüstriyel Balyoz

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15555"/>
</GameScene>
<Color id="GREEN">Endüstriyel Balyoz</Color>, örs üzerinde metal dövmek için IV kademe bir multibloktur. <Color id="GREEN">Endüstriyel Balyoz</Color>, tek bloklu dövme çekicinin ve Buhar Presinin <ItemImage id="gregtech:gt.blockmachines:31083"/> doğrudan yükseltmesidir çünkü %200 hızda çalışır ve $$\text{Gerilim Kademesi} \times \text{Solenoid Kademesi} \times 6$$ paralel sunar (en fazla 1.080). 

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapıldı:

## İnşa
<Color id="GREEN">Endüstriyel Balyozun</Color> tek bir kademeli bileşeni vardır. Solenoid bobinleri toplam paralel sayısını belirler. Yollar/kapaklar yapının herhangi bir yerindeki dövme kasasının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Solenoid bobinlerinin kademesini belirtmek için "solenoid" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15555"/><ItemImage id="gregtech:gt.blockmachines:15555"/>
- 10-29 <ItemLink id="miscutils:gtplusplus.blockcasings.5:6"/><ItemImage id="miscutils:gtplusplus.blockcasings.5:6"/>
- 20 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:32100"/><ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:32100"/>
- 3 Solenoid Süper İletken Bobin (Kademeli) <ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:10"/>
- 2 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Endüstriyel Balyozlar</Color>, kasa ile yol/kapaktan tasarruf etmek için her bir yüzünü duvar paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür. 

## Kullanım
Endüstriyel Balyoz, tek bloklu dövme çekiciye ve Buhar Presine göre doğrudan bir yükseltmedir çünkü %200 hızda çalışır ve $$\text{Gerilim Kademesi} \times \text{Solenoid Kademesi} \times 6$$ paralel sunar.
