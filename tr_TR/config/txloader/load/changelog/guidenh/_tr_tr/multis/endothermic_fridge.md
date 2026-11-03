---
item_ids:
  - gregtech:gt.blockmachines:15518
navigation:
  title: Endotermik Buzdolabı
  parent: multis.md
  icon: gregtech:gt.blockmachines:15518
categories:
    - New Multiblocks
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endotermik Buzdolabı
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15518" />
</GameScene>
<Color id="GREEN">Endotermik Buzdolabı (EnF)</Color>, sıcak külçeleri ve sıvıları toplu halde soğutmak için ZPM kademesinde bir multibloktur. <Color id="GREEN">ENF</Color>, <ItemLink id="gregtech:gt.blockmachines:1002"/><ItemImage id="gregtech:gt.blockmachines:1002"/> modelinin doğrudan yükseltmesidir çünkü <Color id="BLUE">%1.200</Color> hıza kadar çalışır, <Color id="RED">256</Color> paralel sunar, ciddi overclock için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapaklarını</Color> destekler ve sınırsız kademe atlamasına sahiptir. <Color id="GREEN">EnF</Color>, Mega Vakum Dondurucunun yerini alır. Yani yeterli güç olduğu sürece gerilim kademesinden bağımsız olarak herhangi bir tarifi çalıştırabilir. Hız, çalışırken yavaşça 1.5x'e kadar artar ve boştayken 1.0x'e geri düşer. İsteğe bağlı olarak, 250-375 L/s dondurucu kriyotheum karşılığında hız çarpanının artış oranını 5 katına çıkarmak için kontrolcünün GUI'sinde kriyotheum soğutmasını etkinleştir. Yapıyı sonsuzluk soğutmalı kasalarla yükselterek alt uzay soğutmasının kilidini açabilirsin; bu, egzotik soğutucular karşılığında hem makinenin hızını hem de dondurucu kriyotheum tüketim oranını daha da çarpar. EnF, Kriyojenik Dondurucuyu <ItemImage id="gregtech:gt.blockmachines:15565"/> yalnızca 256 paralelinin tam avantajını kullanabildiğinde (4+ overclock) veya alt uzay soğutmasını kullanabildiğinde geride bırakır. Ayrıca [Kriyojenik Dondurucunun](../reworks/cryogenic_freezer.md) bu yeni değişikliklere uyum sağlaması için güçlendirildiğini, paralelinin iki katına çıktığını (8->16) ve hızının arttığını (%220->%300) belirtmek gerekir. 

<br clear="all"/>

## İnşaat:
<Color id="GREEN">EnF</Color> iki kademede mevcuttur ancak aralarındaki tek yapısal fark T2 yapısına eklenen sonsuzluk soğutmalı kasalardır <ItemImage id="gregtech:gt.blockcasings8:14"/>. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki buzdolabı kasalarının yerini alabilir. Cam kademesinden bağımsız olarak ciddi overclock için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan; camın kademesini belirtmek için "glass" alt kanalını, makinenin kademesini belirtmek için tek bir yığında tutulan projektör sayısını kullan.

208 sonsuzluk soğutmalı kasa inşa etmek için 255k (L) sonsuzluk, 240k (L) uzayzaman ve 59,9k (L) Hipojen gerekir. Hipojen, Mk-IV Füzyon Reaktörü tarifine güvenmek yerine Boyutsal Aşkın Plazma Ocağında <ItemImage id="gregtech:gt.blockmachines:1004"/> üretilebilir hale gelene kadar beklemen önerilir.
### T1 Gereksinimleri:
- 1 <ItemLink id="gregtech:gt.blockmachines:15518"/><ItemImage id="gregtech:gt.blockmachines:15518"/>
- 750-773 <ItemLink id="gregtech:gt.blockcasings14:4"/><ItemImage id="gregtech:gt.blockcasings14:4"/>
- 351 <ItemLink id="gregtech:gt.blockcasings2:1"/><ItemImage id="gregtech:gt.blockcasings2:1"/>
- 148 <ItemLink id="gregtech:gt.blockreinforced:3"/><ItemImage id="gregtech:gt.blockreinforced:3"/>
- 148 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 146 <ItemLink id="gregtech:gt.blockframes:389"/><ItemImage id="gregtech:gt.blockframes:389"/>
- 135 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 51 <ItemLink id="gregtech:gt.blockcasings10:9"/><ItemImage id="gregtech:gt.blockcasings10:9"/>
- 40 <ItemLink id="gregtech:gt.sheetmetal:390"/><ItemImage id="gregtech:gt.sheetmetal:390"/>
- 18 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 1+ Enerji Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 Bakım Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ Giriş Yolu (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ Çıkış Yolu (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ Çıkış Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:60"/>

### T2 Gereksinimleri:

- 1 <ItemLink id="gregtech:gt.blockmachines:15518"/><ItemImage id="gregtech:gt.blockmachines:15518"/>
- 750-773 <ItemLink id="gregtech:gt.blockcasings14:4"/><ItemImage id="gregtech:gt.blockcasings14:4"/>
- 208 <ItemLink id="gregtech:gt.blockcasings8:14"/><ItemImage id="gregtech:gt.blockcasings8:14"/>
- 148 <ItemLink id="gregtech:gt.blockreinforced:3"/><ItemImage id="gregtech:gt.blockreinforced:3"/>
- 148 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 146 <ItemLink id="gregtech:gt.blockframes:389"/><ItemImage id="gregtech:gt.blockframes:389"/>
- 143 <ItemLink id="gregtech:gt.blockcasings2:1"/><ItemImage id="gregtech:gt.blockcasings2:1"/>
- 135 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 51 <ItemLink id="gregtech:gt.blockcasings10:9"/><ItemImage id="gregtech:gt.blockcasings10:9"/>
- 40 <ItemLink id="gregtech:gt.sheetmetal:390"/><ItemImage id="gregtech:gt.sheetmetal:390"/>
- 18 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 1+ Enerji Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 Bakım Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ Giriş Yolu (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ Çıkış Yolu (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ Çıkış Kapağı (herhangi bir buzdolabı kasası) <ItemImage id="gregtech:gt.blockmachines:60"/>

### Duvar Paylaşımı:
<Color id="GREEN">EnF'ler</Color>, kasa ve veriyolu/kapak tasarrufu için her bir yüzlerini duvar paylaşımına açabilir. Buna sonsuzluk soğutmalı kasaların hiçbiri dahil değildir. 

## Kullanım:
<Color id="GREEN">EnF</Color>, Vakum Dondurucunun doğrudan yükseltmesidir çünkü %1.200 hıza kadar çalışır, 256 paralel sunar, ciddi overclock için çok amperli ve lazer enerji kapaklarını destekler ve sınırsız kademe atlamasına sahiptir. Yani yeterli güç olduğu sürece gerilim kademesinden bağımsız olarak herhangi bir tarifi çalıştırabilir. Örneğin, bir ZPM 256A lazer enerji kapağı UIV tariflerini çalıştırabilir.

<Color id="GREEN">EnF</Color> hız çarpanı, aşağıda görüldüğü gibi çalışırken 1.5x'e kadar artar ve boştayken 1.0x'e geri düşer. Maksimum hız çarpanına ulaşmak 5 dakika kesintisiz çalışma gerektirir ancak hepsini kaybetmek yalnızca 20 saniye sürer. İsteğe bağlı olarak, 250-375 L/s dondurucu kriyotheum karşılığında hız çarpanının artış oranını 5 katına çıkarmak için kontrolcünün GUI'sinde kriyotheum soğutmasını etkinleştir. Tüketim oranı hız çarpanıyla doğrusal olarak ölçeklenir ancak bu sayede <Color id="GREEN">EnF</Color> maksimum 1.5x hız çarpanına yalnızca 1 dakikada ulaşabilir. Kriyotheum soğutması etkinken dondurucu kriyotheum biterse makine anında kapanır ve mevcut tarifi yok eder.

- Çalışırken 5 saniyede +0.00833 hız çarpanı (kriyotheum soğutması kapalı), maksimuma 5 dakika
- Çalışırken 5 saniyede +0.04167 hız çarpanı (kriyotheum soğutması açık), maksimuma 1 dakika
- Boştayken saniyede -0.025 hız çarpanı, minimuma 20 saniye

## Alt Uzay Soğutması
<Color id="GREEN">EnF</Color> yapısını sonsuzluk soğutmalı kasalarla yükselterek alt uzay soğutmasının kilidini aç; bu, egzotik soğutucular karşılığında makinenin hızını anında çarpar. Kriyotheum soğutması etkinse hız artışı dondurucu kriyotheum tüketim oranına da uygulanır. Bunun, daha önceki 1.5x hız çarpanıyla çarpımsal olarak birikerek %1.200 hıza kadar çıktığını unutma. Maksimuma ulaşma süresi, bu hız artışları anında uygulandığı için kriyotheum soğutması olmadan yine 5 dakika, kriyotheum soğutmasıyla 1 dakikadır. Egzotik soğutucular birikmez ve bunlar sağlandıktan sonra tükenirse makine anında kapanır ve mevcut tarifi yok eder. 

| Egzotik Soğutucu | Giriş Oranı | Hız Artışı | Maks. Hız | Dondurucu Kriyotheum |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| Yok | 0 L/s | 1.0x | %150 | 250 - 375 L/s |
| Eriyik Sonsuzluk | 20 L/s | 2.0x | %300 | 500 - 750 L/s |
| Eriyik Uzayzaman | 20 L/s | 4.0x | %600 | 1.000 - 1.500 L/s |
| Eriyik Ebediyet | 20 L/s | 8.0x | %1.200 | 1.500 - 3.000 L/s |