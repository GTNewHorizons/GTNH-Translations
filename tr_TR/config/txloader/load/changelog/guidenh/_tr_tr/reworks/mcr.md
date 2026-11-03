---
navigation:
  title: Mega Kimyasal Reaktör
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15515
categories:
    - Yapı Yenilemeleri
author: Skorched
date: 2026-05-23
---

# Mega Kimyasal Reaktör

<GameScene wrap="square">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15515"/>
</GameScene>
<Color id="GREEN">Mega Kimyasal Reaktör</Color>, daha da büyük ve daha gelişmiş kimyasal tepkimeler gerçekleştirmek için LuV kademesinde bir multibloktur. <Color id="GREEN">MCR</Color>, Büyük Kimyasal Reaktör<ItemImage id="gregtech:gt.blockmachines:1169"/> için doğrudan bir yükseltmedir; çünkü <Color id="RED">256</Color> paralel sunar, ciddi hız aşırtma için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapaklarını</Color> destekler ve <Color id="BLUE">sınırsız</Color> kademe atlaması yapar. Bu, yeterli güç olduğu sürece gerilimden bağımsız olarak her tarifi çalıştırabileceği anlamına gelir. O kadar iyi ölçeklendikleri için bunlardan yalnızca birkaç tane inşa etmeyi bekle.

<br clear="all"/>

> [!NOTE]
> Mega Kimyasal Reaktör'deki başlıca değişiklikler şunlardır:
> - Kapak kısıtlamaları kaldırıldı, yani artık herhangi bir kapağı kasaların herhangi bir yerine yerleştirebilirsin! (Yapı başına hâlâ tek enerji kapağı sınırı var)
> - Onu <ItemLink id="gregtech:gt.blockmachines:1169" />'den ayırt etmek için yeni bir kaplama dokusu eklendi
> - (İsteğe bağlı) <ItemLink id="gregtech:gt.blockcasings5:13" /> <ItemImage id="gregtech:gt.blockcasings5:13" /> artık makine çalışırken parlıyor


## Yapım
<Color id="GREEN">MCR</Color>'nin kademeli tek bir bileşeni vardır. Cam, enerji kapağının maksimum kademesini belirler, ancak amperajda bir sınır yoktur. Füzyon bobin blokları, tercih edilirse ebedi ısıtma bobinleriyle değiştirilebilir. Yollar/kapaklar, yapının herhangi bir yerindeki kimyasal olarak etkisiz makine gövdesinin yerini alabilir. Ciddi hız aşırtma için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir, ancak ikincisi en az UV kademesi cam gerektirir. Camın kademesini belirtmek için yapıyı "glass" alt kanalıyla görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.
### Gerekenler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15515"/><ItemImage id="gregtech:gt.blockmachines:15515"/>
- 0-79 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 64 Kademeli Cam <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 28 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings4:7"/><ItemImage id="gregtech:gt.blockcasings4:7"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />
### Duvar Paylaşımı
<Color id="GREEN">MCR</Color>'ler kasa ve yol/kapak tasarrufu sağlamak için her bir yüzünü duvar paylaşabilir. Ancak enerji kapağını paylaşma, çünkü makine hâlâ paralel veya hız aşırtma mevcut olduğu sürece mümkün olduğunca fazla amper çeker.
## Kullanım
<Color id="GREEN">MCR</Color>, Büyük Kimyasal Reaktör için doğrudan bir yükseltmedir; çünkü 256 paralel sunar, ciddi hız aşırtma için çok amperli ve lazer enerji kapaklarını destekler ve sınırsız kademe atlaması yapar. Bu, yeterli güç olduğu sürece gerilimden bağımsız olarak her tarifi çalıştırabileceği anlamına gelir. 