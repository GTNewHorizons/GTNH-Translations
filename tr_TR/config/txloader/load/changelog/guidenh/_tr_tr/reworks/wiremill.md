---
item_ids:
  - gregtech:gt.blockmachines:15511
navigation:
  title: Industrial Wire Factory
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15511
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-26
---

# Industrial Wire Factory

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15511"/>
</GameScene>
<Color id="GREEN">Yeşil Industrial Wire Factory (IWF)</Color>, metallerden tel çekmek için kullanılan IV kademe bir multibloktur. <Color id="GREEN">Yeşil IWF</Color>, tekli Tel Haddesine göre doğrudan bir yükseltmedir; çünkü eşya boru muhafazası kademesine bağlı olarak %400'e kadar hız bonusu kazanır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve her gerilim kademesi için 4 paralel sunar. Aynı makinede farklı programlanmış devreler kullanabilmek için IWF'de girdi ayrıştırması etkinleştirilmelidir.

<br clear="all"/>

> [!NOTE]
> Multibloğa (yapı dışında) aşağıdaki değişiklikler yapıldı:
> - Kademeli Eşya Boruları: Eşya Boru Muhafazası kademelerine göre %50-400 arasında değişen hız bonusu (önceki maksimum %300)
> - Yapı: Kasalar için daha fazla yer, daha fazla yol ve kapağa olanak tanır

## Yapım
<Color id="GREEN">Yeşil IWF</Color>'nin kademeli tek bir bileşeni vardır. Eşya boru muhafazaları makinenin hız bonusunu belirler. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir kasanın yerini alabilir. Çok amperli ve lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı bulunabilir. Bu bileşenlerin kademesini belirtmek için "item_pipe" ve "glass" alt kanallarıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan.
### Gereksinimler:

- 1 <ItemLink id="gregtech:gt.blockmachines:15511" /> <ItemImage id="gregtech:gt.blockmachines:15511" /> (Kontrolcü)
- 14-35 <ItemLink id="miscutils:miscutils.blockcasings:6" /> <ItemImage id="miscutils:miscutils.blockcasings:6" />
- 15 adet Kademeli Cam (herhangi)
- 3 Eşya Boru Muhafazası <ItemImage id="gregtech:gt.blockcasings11:5" />
- 1+ Enerji Kapağı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı:
<Color id="GREEN">Yeşil IWF</Color>'ler kasa, cam ve yol/kapaktan tasarruf etmek için her yüzünü duvar paylaşabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__iki__</u> makine arasında <u>__tek__</u> bir enerji kapağını paylaşmak mümkündür.
## Kullanım

| Kademe | Eşya Boru Muhafazası | Hız Bonusu |
| --------------- | --------------- | --------------- |
| 1 | Kalay | %50 |
| 2 | Pirinç | %100 |
| 3 | Elektrum | %150 |
| 4 | Platin | %200 |
| 5 | Osmiyum | %250 |
| 6 | Kuantinyum | %300 |
| 7 | Yüklenmiş Elektrum | %350 |
| 8 | Siyah Plütonyum | %400 |

----------


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


### Girdi Ayrıştırma
Farklı giriş yollarındaki __KATI__ bileşenlerin, programlanmış devreler dahil, aynı tarifte kullanılmasını önlemek için <Color id="GREEN">Yeşil IWF</Color>'de girdi ayrıştırması etkinleştirilmelidir. Bu, birçok giriş yolu bulunan tek bir <Color id="GREEN">Yeşil IWF</Color>'nin aynı anda birçok farklı devreyi destekleyebileceği anlamına gelir.