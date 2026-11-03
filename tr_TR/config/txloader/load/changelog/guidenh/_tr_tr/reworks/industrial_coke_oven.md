---
item_ids:
  - gregtech:gt.blockmachines:15543
navigation:
  title: Endüstriyel Kok Fırını
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15543
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Endüstriyel Kok Fırını

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15543"/>
</GameScene>
<Color id="GREEN" >Endüstriyel Kok Fırını (ICO)</Color>, kütükleri toplu halde yakarak kömür ve tek bir sıvı yan ürüne (kömür gazı, odun gazı, odun sirkesi, odun katranı veya kömür yan ürünleri) dönüştürmek için kullanılan EV kademesi bir multibloktur. Sıvı yan ürünler etilen, benzen ve toluen gibi organik bileşiklerin üretiminde işe yarar. <Color id="GREEN">ICO</Color>, Piroliz Fırını <ItemImage id="gregtech:gt.blockmachines:15546"/> ve Gelişmiş Kok Fırını <ItemImage id="Railcraft:machine.alpha:12"/> göre doğrudan bir yükseltmedir; çünkü her ısıtma bobini kademesi için (çarpımsal) <Color id="RED">%2</Color> enerji indirimi kazanır ve <Color id="BLUE">32</Color> paralel ile yapıya eklenen her ek dilim için <Color id="BLUE">16</Color> paralel daha sunar. Ek dilimler, sınırı olmayan ebedi dışındaki tüm ısıtma bobini kademelerinde 15 ile sınırlıdır (temel yapı dahil toplam 16). <Color id="GREEN">ICO</Color> ayrıca sonsuzluk ısıtma bobinleri veya daha iyisiyle bir adet <Color id="GREEN">Çok Amperli Enerji Kapağı</Color> kullanma olanağını açar.

<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) şu değişiklikler yapıldı:
> - "Dilim Mimarisi": ICO artık ek "dilimlere" sahip olabilir; her biri yapı kademesine bağlı olarak +8/16 paralel verir (en fazla 15 dilim, ebedi bobinler sınırsız dilim açar)
> - Çok Amperli Desteği: Sonsuzluk Bobinleri veya daha iyisini kullanmak, tek Çok Amperli Kapakların kullanımını açar!
> - EU Tasarrufu: Gerilim Kademesi başına -%4 EU/t yerine artık Isıtma Bobini başına (çarpımsal) -%2 EU/t kullanır

## Yapım
<Color id="GREEN">ICO</Color>'nun iki kademeli bileşeni vardır. Kok fırını kasaları hem temel paralel sayısını hem de dilim başına ek paralel sayısını belirler. Isıtma bobinleri makinenin enerji indirimini belirler. Veriyolları/kapaklar temel yapıdaki herhangi bir yapısal kok fırını kasasının yerine geçebilir; ek dilimlerdekilerin yerine GEÇEMEZ. Lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı veya ısıtma bobinleri sonsuzluk ya da daha iyisiyse tek bir çok amperli enerji kapağı kullanılabilir. Bileşenlerin kademesini belirtmek için "coke_oven_casing" ve "coil" alt kanallarıyla, toplam dilim sayısını belirtmek için "length" alt kanalıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Temel Yapı İçin Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15543"/><ItemImage id="gregtech:gt.blockmachines:15543"/>
- 35-48 <ItemLink id="miscutils:miscutils.blockcasings:1"/><ItemImage id="miscutils:miscutils.blockcasings:1"/>
- 10 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8 Isıtma Bobini (Kademeli) <ItemImage id="gregtech:gt.blockcasings5:3"/>
- 8 Isıya Dayanıklı/Isı Geçirmez Kok Fırını Kasası <ItemImage id="miscutils:miscutils.blockcasings:2"/> / <ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 1+ Enerji Kapağı (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir yapısal kasa) <ItemImage id="gregtech:gt.blockmachines:60" />

### Her Ek Dilim İçin Gerekli:
- 19 <ItemLink id="miscutils:miscutils.blockcasings:1"/><ItemImage id="miscutils:miscutils.blockcasings:1"/>
- 10 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8 Isıtma Bobini (Kademeli) <ItemImage id="gregtech:gt.blockcasings5:3"/>
- 5 Isıya Dayanıklı/Isı Geçirmez Kok Fırını Kasası <ItemImage id="miscutils:miscutils.blockcasings:2"/> / <ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>

### Duvar Paylaşımı
<Color id="GREEN">ICO</Color>'lar, neredeyse tüm yapılarını karşı uçta ve yatay olarak çevrilmiş başka bir ICO ile duvar paylaşımı yaparak kullanabilir. Bu şiddetle önerilir; çünkü inanılmaz miktarda kasa, çerçeve kutusu ve ısıtma bobininden tasarruf sağlar; ikinci makine adeta bedavadır. Ancak veriyolları/kapaklar temel yapıyla sınırlıdır ve bu nedenle bu düzenlemede paylaşılamaz. Enerji indirimine bakılmaksızın hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden <u>__bir__</u> enerji kapağını <u>__iki__</u> makine arasında paylaşmak mümkündür.

## Kullanım
<Color id="GREEN">ICO</Color>, her ısıtma bobini kademesi için (çarpımsal) %2 enerji indirimi kazandığı ve aşağıdaki tablolarda görüldüğü gibi 32 paralel ile yapıya eklenen her ek dilim için 16 paralel daha sunduğu için Piroliz Fırını ve Gelişmiş Kok Fırınına göre doğrudan bir yükseltmedir. Ek dilimler, sınırı olmayan ebedi dışındaki tüm ısıtma bobini kademelerinde 15 ile sınırlıdır (temel yapı dahil toplam 16).

<Color id="GREEN">ICO</Color> esas olarak kütükleri, TEK bir sıvı yan ürün seçeneğiyle kömüre yakmak için kullanılır; bu yan ürün Giriş Yolu'ndaki veya kontrolcüdeki programlanmış devre ile belirlenir. En yaygın seçim kömür yan ürünleridir; çünkü bunlar bir Damıtma Kulesinde <ItemImage id="gregtech:gt.blockmachines:1126"/> dimetilbenzen, odun gazı, odun sirkesi ve odun katranına ayrışır. Bir diğer yaygın seçim, nitrobenzeni daha doğrudan/verimli üretmek için odun katranıdır. Ayrıca makinenin işlem hızını ikiye katlamak için 4 kütük başına 250L azot gazı kullanma seçeneği de vardır; bu da yine Giriş Yolu'ndaki veya kontrolcüdeki programlanmış devre ile belirlenir.