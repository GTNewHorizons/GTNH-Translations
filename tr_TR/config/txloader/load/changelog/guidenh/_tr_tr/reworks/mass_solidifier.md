---
item_ids:
  - gregtech:gt.blockmachines:368
navigation:
  title: Kütle Katılaştırıcı
  parent: reworks.md
  icon: gregtech:gt.blockmachines:368
categories:
    - Yeni Multibloklar
    - Yapı Yenilemeleri
author: Skorched
date: 2026-05-27
---

# Kütle Katılaştırıcı

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:368"/>
</GameScene>
<Color id="GREEN">Kütle Katılaştırıcı</Color> (yeşil), sıvı metalleri kalıplara dökmek için kullanılan IV kademe bir multibloktur. <Color id="GREEN">Kütle Katılaştırıcı</Color>, tek bloklu sıvı katılaştırıcının doğrudan yükseltmesidir; çünkü <Color id="RED">%300</Color> (kırmızı) hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%80</Color>'ini (mavi) kullanır ve gerilim kademesi başına <Color id="GREEN">10</Color> paralel sunar. Makine çalışırken hız her saniye %5 artar, çalışmadığında ise her saniye %10 azalır. Katılaştırıcı Kapakları <ItemImage id="gregtech:gt.blockmachines:31781"/> yalnızca kendi kapağındaki sıvıya uygulanan, yapılandırılabilir bir hayalet kalıp yuvasına sahiptir; böylece tek bir makine gerektiği kadar tarifi işleyebilir. <Color id="GREEN" >Kütle Katılaştırıcı</Color>'nın yerini UEV kademesinde [Exo-Foundry](../multis/exo_foundry.md) alır. 

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> - Kullanımdan kaldırma: Bu, eski Sıvı Şekillendirici'nin yerini alır
> - Katılaştırıcı Kapakları: Sıvı alan ve hayalet kalıp yuvasına sahip yeni kapaklar
> - Paraleller: "Dilim" başına 2 + 3 yerine Gerilim Kademesi başına 10 paralel


## İnşaat
<Color id="GREEN">Kütle Katılaştırıcı</Color>'nın kontrolcü dışında tek kademeli bileşeni vardır: cam. Cam, enerji kapağının maksimum kademesini belirler. UEV kademe cam her kademeye izin verir ve kısıtlamayı fiilen ortadan kaldırır. Yollar/kapaklar yapının herhangi bir yerindeki katılaştırıcı kasasının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı olabilir. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

<Color id="GREEN">Kütle Katılaştırıcı</Color>'ya özgü olan <Color id="BLUE">Katılaştırıcı Kapağı</Color> <ItemImage id="gregtech:gt.blockmachines:31781"/>, aslında yapılandırılabilir bir hayalet kalıp yuvasına sahip bir girdi kapağıdır. Tüm mevcut seçenekleri içeren bir menü açmak için kalıp yuvasına shift-tıkla. Kalıp, girdi ayrıştırma ayarlarından bağımsız olarak yalnızca kendi kapağındaki sıvıya uygulanır. Katılaştırıcı kapağının iç kapasitesini artıran dört kademesi vardır ve sonunda yerini Üretim Girdi Tamponuna bırakır. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:368"/><ItemImage id="gregtech:gt.blockmachines:368"/>
- 24-73 <ItemLink id="gregtech:gt.blockcasings10:13"/><ItemImage id="gregtech:gt.blockcasings10:13"/>
- 42 Kademeli Cam <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 34 <ItemLink id="gregtech:gt.blockcasings10:14"/><ItemImage id="gregtech:gt.blockcasings10:14"/>
- 13 <ItemLink id="gregtech:gt.blockcasings:11"/><ItemImage id="gregtech:gt.blockcasings:11"/>
- 7 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Kütle Katılaştırıcılar</Color>, kasa, cam ve yol/kapaklardan tasarruf etmek için her bir kenarında duvar paylaşımı yapabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu nedenle <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağı paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Kütle Katılaştırıcı</Color>, tek bloklu sıvı katılaştırıcının doğrudan yükseltmesidir; çünkü %300'e kadar hızda çalışır, normalde gereken EU/t'nin yalnızca %80'ini kullanır ve aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 10 paralel sunar.



| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 | 110 | 120 | 130 | 140 | 150 |


<Color id="GREEN">Kütle Katılaştırıcı</Color>'nın hızı çalışırken her saniye %5 artar, çalışmadığında ise her saniye %10 azalır. Bu, maksimum hızına ulaşmasının 40 saniye çalışma süresi aldığı, ancak tümünü kaybetmesinin yalnızca 20 saniye sürdüğü anlamına gelir. Artıştan tam olarak yararlanmak için desenleri çoğaltman ve makineyi olabildiğince uzun süre çalıştırman şiddetle önerilir. 