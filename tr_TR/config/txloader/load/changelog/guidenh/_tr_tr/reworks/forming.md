---
item_ids:
  - gregtech:gt.blockmachines:15552
navigation:
  title: Endüstriyel Şekillendirme Presi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15552
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Şekillendirme Presi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15552"/>
</GameScene>
<Color id="GREEN">Endüstriyel Şekillendirme Presi (IFP)</Color>, metalleri kalıplara preslemek için EV kademe bir multibloktur. <Color id="GREEN">IFP</Color>, tek bloklu şekillendirme presinden doğrudan bir yükseltmedir; <Color id="BLUE">%600</Color> hızda çalışır ve gerilim kademesi başına <Color id="RED">6</Color> paralel sunar. Aynı makinede farklı kalıplar ve programlanmış devreler kullanmak için <Color id="GREEN">IFP</Color>'de girdi ayrıştırmasını etkinleştir.

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapıldı:
> - Makinelerin Ayrıştırması: Bükme ve Şekillendirme işlevleri iki ayrı multibloka ayrıldı ([Endüstriyel Bükme Makinesine bak](bending.md))
> - Daha Fazla Paralel: Gerilim Kademesi Başına 4 -> 6

## Yapım
<Color id="GREEN">IFP</Color>'nin kademeli bileşeni yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki herhangi bir metal işleme makine gövdesinin yerini alabilir. <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak overclock için birden fazla normal enerji kapağı olabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15552"/>
- 5-20 <ItemLink id="miscutils:miscutils.blockcasings:4"/><ItemImage id="miscutils:miscutils.blockcasings:4"/>
- 6 <ItemLink id="gregtech:gt.blockframes:28"/><ItemImage id="gregtech:gt.blockframes:28"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 5 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 1 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">IFP</Color>'ler kasa, şekillendirme çekirdeği ve veriyolu/kapaklardan tasarruf etmek için her bir yanlarını paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmadığından <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">IFP</Color>, aşağıdaki tabloda görüldüğü gibi %600 hızda çalıştığı ve gerilim kademesi başına 6 paralel sunduğu için tek bloklu şekillendirme presinden doğrudan bir yükseltmedir.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |

Farklı giriş veriyollarındaki KATI bileşenlerin — kalıplar ve programlanmış devreler dahil — aynı tarifte kullanılmasını önlemek için <Color id="GREEN">IFP</Color>'de girdi ayrıştırmasını etkinleştir. Yani birçok giriş veriyoluna sahip tek bir <Color id="GREEN">IFP</Color>, aynı anda birçok farklı kalıbı veya programlanmış devreyi destekleyebilir. Sadece minimum metal işleme makine gövdesi sayısının üzerinde kalmayı unutma. Plaka kalıbı (mika esaslı levhalar için) ve dört AE2 devre presinin tamamı, herhangi bir çakışma olmadan aynı giriş veriyolunu kullanabilir.