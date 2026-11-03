---
item_ids:
  - gregtech:gt.blockmachines:15556
navigation:
  title: Boldarnator
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15556
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---
# Boldarnator

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15556"/>
</GameScene>
<Color id="GREEN">Boldarnator</Color>, temel kayaları üretmek ve toplamak için IV kademe bir Multibloktur. <Color id="GREEN">Boldarnator</Color>, tek bloklu kaya kırıcının doğrudan yükseltmesidir; çünkü %300 hızda çalışır, normalde gereken EU/t'nin yalnızca <Color id="BLUE">%75</Color>'ini kullanır ve her gerilim kademesi için <Color id="RED">8</Color> paralel sunar. Kullanılabilir kayalar kırıktaş, taş, obsidyen, bazalt, derin kayrak, netherrack ve end taşıdır. Tek gereksinim, bir giriş yolunda bir katalizör ve/veya programlanmış devre bulunmasıdır. Lav, su ve katalizör işleme sırasında TÜKETİLMEZ, bu yüzden tek maliyet her obsidyen için 1 kızıltaş tozu ve her netherrack için 1 parlak taş tozudur. Diğer her şey tamamen bedavadır. 

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> Lav ve su artık sağlanmak zorunda değil, çünkü yapıyla birlikte hazır bulunuyorlar

## İnşaat
<Color id="GREEN">Boldarnator</Color>'ın kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına bir etkisi yoktur. Yollar/kapaklar yapı üzerinde herhangi bir yerdeki herhangi bir kasanın yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı kullanılabilir. Lav ve su, yapı kurulduğunda bedavaya oluşturulur ve bu yüzden elle yerleştirilmeleri GEREKMEZ. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15556"/><ItemImage id="gregtech:gt.blockmachines:15556"/>
- 50-53 <ItemLink id="miscutils:gtplusplus.blockcasings.2"/><ItemImage id="miscutils:gtplusplus.blockcasings.2"/>
- 36 <ItemLink id="gregtech:gt.blockframes:81"/><ItemImage id="gregtech:gt.blockframes:81"/>
- 12 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">Boldarnator</Color>, kasa, cam, çerçeve ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Buna iki yandaki tanklar da dahildir, ancak kontrolcülerden biri önce yatay olarak çevrilmeden (İngiliz Anahtarı ile eğilip sağ tıklayarak) sıvılar değiştirilemez. Hiçbir tarif 0,5A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__dört__</u> makine arasında paylaşmak mümkündür. 

## Kullanım
<Color id="GREEN">Boldarnator</Color>, tek bloklu kaya kırıcının doğrudan yükseltmesidir; çünkü %300 hızda çalışır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve her gerilim kademesi için 8 paralel sunar. 

<Color id="GREEN">Boldarnator</Color>'ın, programlanmış devre değerlerine göre aşağıda listelenen yedi kullanılabilir tarifi vardır. Bunlardan beşi tamamen bedavadır ve yalnızca giriş yolunda belirli, tüketilemeyen katalizörler gerektirir. Diğer ikisi her obsidyen için 1 kızıltaş tozu ve her netherrack için 1 parlak taş tozu tüketir. NEI'de gereksinim olarak görünmesine rağmen lav ve su doğrudan iki yandaki tanklardan alınır ve bir girdi kapağında bulunmaları gerekmez.

1. Kırıktaş - Bedava
2. Taş - Bedava
3. Obsidyen - Her işlemde 1 kızıltaş tüketir.
4. Bazalt - Bedava. Giriş yolunda ruh kumu ve mavi buz gerektirir.
5. Derin kayrak - Bedava. Giriş yolunda ruh kumu ve magma bloğu gerektirir.
6. Netherrack - Her işlemde 1 parlak taş tüketir.
7. End taşı - Bedava.

<Color id="GREEN">Boldarnator</Color> özellikle kırıktaştan silisyuma uzanan bir işleme hattı için kullanışlıdır. Kırıktaşı çakıla, ardından tekrar kuma öğüt. Kumu silisyum dioksit tozuna elektroliz et ve sonsuz silisyum kaynağı elde etmek için bunu magnezyum tozuyla tepkimeye sok. Magnezya tozu, kayıpsız kapalı devre bir sistemde tekrar magnezyum tozuna elektroliz edilebilir. Bu ayrıca yan ürün olarak bir miktar oksijen üretir.

<Color id="GREEN">Boldarnator</Color> ayrıca, kırıktaşı otomatik olarak ruh kumuna (nether fidanı) veya end taşına (end fidanı) dönüştüren Thaumcraft fidanları için kırıktaş üretmede de kullanışlıdır. Sonsuz güherçile, kömür tozu, kum ve petrol için ruh kumunu santrifüj et. Sonsuz tungstat, platin metalik tozu, kum ve helyum için end taşı tozunu santrifüj et. Bunun nasıl kurulacağına dair video anlatımını [burada](https://www.youtube.com/watch?v=-Xvlm86FScA) bulabilirsin.

Boldarnator'ın diğer kullanımları arasında LuV'de Ender Taşocağı için yeterli obsidyen ve UV'de Katmankayamsı için yeterli kırıktaş üretmek yer alır (külçe başına 26.244 kırıktaş). 