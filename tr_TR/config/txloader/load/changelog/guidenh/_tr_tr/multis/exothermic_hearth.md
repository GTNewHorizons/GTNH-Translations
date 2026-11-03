---
item_ids:
  - gregtech:gt.blockmachines:15517
navigation:
  title: Ekzotermik Ocak
  parent: multis.md
  icon: gregtech:gt.blockmachines:15517
categories:
    - New Multiblocks
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Ekzotermik Ocak
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15517" />
</GameScene>
<Color id="GREEN">Ekzotermik Ocak (ExH)</Color>, tozları seri üretimle külçelere eritmek, silisyum kristalleri üretmek ve çeşitli materyalleri ısıtmak için kullanılan ZPM kademe bir multibloktur. Önceki Mega Elektrikli Yüksek Fırın'ın yerini alır. <Color id="GREEN">ExH</Color>, Elektrikli Yüksek Fırın <ItemImage id="gregtech:gt.blockmachines:1000"/> için doğrudan bir yükseltmedir; çünkü <Color id="RED">512</Color> paralele kadar sunar, ciddi hız aşırtma için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapaklarını</Color> destekler ve <Color id="BLUE">sınırsız kademe atlama</Color> özelliğine sahiptir. Bu, yeterli güç ve ısı olduğu sürece her tarifi gerilim kademesinden bağımsız çalıştırabileceği anlamına gelir. Kullanılabilir paralel sayısı etkinken yavaşça 512'ye kadar çıkar ve boştayken 256'ya kadar geri düşer. İsteğe bağlı olarak, kontrolcünün GUI'sinde Pirotheum ısıtmayı etkinleştirerek 250-500 L/s Alevli Pirotheum karşılığında paralel kazanma hızını 6 katına çıkarabilirsin. <Color id="GREEN">ExH</Color>, tarif gereksiniminin üzerindeki her 900K için %5 enerji indirimi ve her 1,800K için bir tam hız aşırtma kazanır. Volcanus <ItemImage id="gregtech:gt.blockmachines:963"/> ile karşılaştırıldığında ExH, yalnızca 512 paralelinden (4+ hız aşırtma) tam olarak yararlanabildiğinde onu geride bırakır.
<br clear="all"/>

## İnşa:
<Color id="GREEN">ExH</Color>'nin iki kademeli bileşeni vardır. Isıtma bobinleri tariflerin maksimum kademesini, enerji indirimini ve tam hız aşırtma sayısını belirler. Cam, enerji kapağının maksimum kademesini belirler. UMV kademeli cam tüm kısıtlamaları kaldırır. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir ocak kasasının yerine geçebilir; ancak yapının üst katmanındaki merkez kasayla sınırlı olan Egzoz Çıkışı bunun dışındadır. Çok amperli ve lazer enerji kapakları desteklenir, ancak ikincisi en az UV kademeli cam gerektirir. Bu bileşenlerin kademesini belirtmek için "coil" ve "glass" alt kanallarıyla Multiblok Yapı Hologram Projektörünü kullanarak yapıyı görselleştir/inşa et. 
### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15517"/><ItemImage id="gregtech:gt.blockmachines:15517"/>
- 1,800-1,918 <ItemLink id="gregtech:gt.blockcasings14:3"/><ItemImage id="gregtech:gt.blockcasings14:3"/>
- 925 <ItemLink id="gregtech:gt.blockcasings:11"/><ItemImage id="gregtech:gt.blockcasings:11"/>
- 860 Isıtma Bobini (kademeli) <ItemImage id="gregtech:gt.blockcasings5:11"/>
- 780 <ItemLink id="miscutils:gtplusplus.blockcasings.2:11"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:11"/>
- 426 <ItemLink id="gregtech:gt.blockcasings8:10"/><ItemImage id="gregtech:gt.blockcasings8:10"/>
- 332 Kademeli Cam <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 308 <ItemLink id="gregtech:gt.blockcasings11:7"/><ItemImage id="gregtech:gt.blockcasings11:7"/>
- 280 <ItemLink id="miscutils:miscutils.blockcasings:14"/><ItemImage id="miscutils:miscutils.blockcasings:14"/>
- 131 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 56 <ItemLink id="gregtech:gt.blockframes:163"/><ItemImage id="gregtech:gt.blockframes:163"/>
- 1+ Enerji Kapağı (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 <ItemLink id="gregtech:gt.blockmachines:90"/> (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:90"/>
- 1 Egzoz Çıkışı (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:91"/>
- 0+ Giriş Yolu (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Girdi Kapağı (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Çıkış Yolu (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ Çıkış Kapağı (herhangi bir ocak kasası)<ItemImage id="gregtech:gt.blockmachines:60"/>

### Duvar Paylaşımı:
<Color id="GREEN">ExH'ler</Color> kasa ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Bu, ısıtma bobinlerini veya camı KAPSAMAZ. 
## Kullanım:
<Color id="GREEN">ExH</Color>, Elektrikli Yüksek Fırın'a doğrudan bir yükseltmedir; çünkü 512 paralele kadar sunar, ciddi hız aşırtma için çok amperli ve lazer enerji kapaklarını destekler ve sınırsız kademe atlama özelliğine sahiptir. Bu, yeterli güç ve ısı olduğu sürece her tarifi gerilim kademesinden bağımsız çalıştırabileceği anlamına gelir. Örneğin, bir ZPM 256A lazer enerji kapağı, ısı kapasitesi yeterince yüksekse UIV tariflerini çalıştırabilir. Cam kademesi yalnızca enerji kapağının gerilim kademesini sınırlar, tariflerin gerilim kademesini DEĞİL.

Kullanılabilir paralel sayısı etkinken yavaşça 512'ye kadar çıkar ve boştayken 256'ya kadar geri düşer; aşağıda görüldüğü gibi. Maksimum 512 paralele ulaşmak 30 dakika kesintisiz etkinlik gerektirir, ancak hepsini kaybetmek yalnızca 4 dakika 16 saniye sürer. İsteğe bağlı olarak, kontrolcünün GUI'sinde Pirotheum ısıtmayı etkinleştirerek 250-500 L/s Alevli Pirotheum karşılığında paralel kazanma hızını 6 katına çıkarabilirsin. Tüketim hızı ek paralel sayısıyla doğrusal olarak ölçeklenir, ancak bu sayede ExH maksimum 512 paralele yalnızca 5 dakikada ulaşabilir. Pirotheum ısıtma etkinken Alevli Pirotheum tükenirse makine anında kapanır ve mevcut tarifi geçersiz kılar.

- Etkinken 5 saniyede +0.711 paralel (Pirotheum ısıtma kapalı), maksimuma 30 dakika
- Etkinken 5 saniyede +4.267 paralel (Pirotheum ısıtma açık), maksimuma 5 dakika
- Boştayken saniyede -1 paralel, minimuma 4.26 dakika

## Isı Kapasitesi
Son olarak <Color id="GREEN">ExH</Color>, tarif gereksiniminin üzerindeki her 900K için %5 enerji indirimi ve her 1,800K için bir tam hız aşırtma kazanır. Ayrıca MV'nin üzerindeki her gerilim kademesi için +100K ısı bonusu vardır.