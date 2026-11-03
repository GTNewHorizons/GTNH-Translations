---
item_ids:
  - gregtech:gt.blockmachines:15549
navigation:
  title: Endüstriyel Ekstrüzyon Makinesi
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15549
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---
# Endüstriyel Ekstrüzyon Makinesi

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15549"/>
</GameScene>
Yeşil renkle işaretli <Color id="GREEN">Endüstriyel Ekstrüzyon Makinesi (IEM)</Color>, metalleri çeşitli şekillere ve bileşenlere ekstrüde eden IV kademe bir Multibloktur. <Color id="GREEN">IEM</Color>, tek bloklu ekstrüderin doğrudan yükseltmesidir; çünkü mavi renkle işaretli <Color id="BLUE">%350</Color> hızda çalışır ve gerilim kademesi başına kırmızı renkle işaretli <Color id="RED">6</Color> paralel sunar. Ekstrüzyon yolları <ItemImage id="gregtech:gt.blockmachines:31785"/>, yalnızca kendi yolundaki eşyalara uygulanan, yapılandırılabilir bir ekstrüder kalıbı hayalet yuvasına sahiptir; bu sayede tek bir makine gerektiği kadar tarifi işleyebilir. 

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapılmıştır:
> Paraleller: Gerilim Kademesi başına 4 -> 6'ya çıkarıldı

## Yapım
<Color id="GREEN">IEM</Color>'in kademeli bileşenleri yoktur. Yollar/kapaklar yapının herhangi bir yerindeki kasaların yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı bulunabilir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

<Color id="GREEN">IEM</Color>'e özgü olan ekstrüzyon yolu, aslında yapılandırılabilir bir ekstrüder kalıbı hayalet yuvasına sahip bir giriş yoludur. Tüm mevcut seçenekleri içeren bir menü açmak için kalıp yuvasına Shift ile tıkla. Kalıp, girdi ayrıştırma ayarlarından bağımsız olarak yalnızca kendi yolundaki eşyalara uygulanır. Ekstrüzyon yolunun dahili kapasitesini artıran dört kademesi vardır ve sonunda yerini üretim girdi tamponuna bırakır. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15549"/><ItemImage id="gregtech:gt.blockmachines:15549"/> (Kontrolcü)
- 8-33 <ItemLink id="gregtech:gt.blockcasings10:3"/><ItemImage id="gregtech:gt.blockcasings10:3"/>
- 24 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 3-7 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 1+ Enerji Kapağı (herhangi bir muhafaza veya paslanmaz çelik kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir muhafaza veya paslanmaz çelik kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir muhafaza veya paslanmaz çelik kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Ekstrüzyon Yolu (herhangi bir muhafaza kasası)
- 0+ Giriş Yolu (herhangi bir muhafaza kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Çıkış Yolu (herhangi bir muhafaza kasası) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">IEM</Color>'ler kasa ile yol/kapaklardan tasarruf etmek için her bir yüzünü duvar paylaşımında kullanabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu nedenle <u>__iki__</u> makine arasında <u>__bir__</u> enerji kapağını paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">IEM</Color>, aşağıdaki tabloda görüldüğü üzere %350 hızda çalıştığı ve gerilim kademesi başına 6 paralel sunduğu için tek bloklu ekstrüderin doğrudan yükseltmesidir. 
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |


<Color id="GREEN">IEM</Color>'de girdi ayrıştırma kalıcı olarak etkindir; bu, farklı giriş yollarındaki KATI bileşenlerin, ekstrüder kalıpları da dahil olmak üzere, aynı tarifte kullanılmasını engeller. Bu, birçok ekstrüzyon/girdi yoluna sahip tek bir <Color id="GREEN">IEM</Color>'in aynı anda birçok farklı ekstrüder kalıbını destekleyebileceği anlamına gelir. Yalnızca minimum muhafaza ve paslanmaz çelik kasa sayısının üzerinde kalmayı unutma. 