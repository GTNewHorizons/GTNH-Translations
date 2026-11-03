---
item_ids:
  - gregtech:gt.blockmachines:15546
navigation:
  title: Piroliz Fırını
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15546
categories:
    - Yapı Revizyonları
author: Skorched
date: 2026-05-27
---

# Piroliz Fırını
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15546"/>
</GameScene>
<Color id="GREEN">Piroliz Fırını (PO)</Color>, kütükleri odun kömürüne yakmak ve isteğe bağlı olarak bir sıvı yan ürün (örn. kömür gazı, odun gazı, odun sirkesi, odun katranı, odun kömürü yan ürünleri) üretmek için MV kademe bir Multibloktur. <Color id="GREEN">Piroliz Fırını</Color>, temel Kok Fırınının doğrudan yükseltmesidir <ItemImage id="gregtech:gt.blockmachines:236"/> çünkü elektrikle çalışır ve yeterli güçle hız aşırtma yapabilir. Ayrıca ısıtma bobinlerinin kademesiyle doğrusal olarak ölçeklenen bir hız bonusu kazanır. Sıvı yan ürünler, etilen, benzen ve toluen gibi organik bileşiklerin üretiminde faydalıdır. Başlangıçta daha yavaş olsa da, Piroliz Fırını genellikle Gelişmiş Kok Fırını <ItemImage id="Railcraft:machine.alpha:12"/> yerine önerilir çünkü daha iyi ölçeklenir ve sıvı yan ürünler ilerleme için kritiktir. Her ikisinin de yerini EV'de Endüstriyel Kok Fırını <ItemImage id="gregtech:gt.blockmachines:15543"/> alır. 
<br clear="all"/>

> [!NOTE]
> Bu Multibloktaki tek değişiklik yapının kendisindedir.

## Yapım
<Color id="GREEN">Piroliz Fırını</Color>nın kademeli bir bileşeni vardır. Isıtma bobinleri makinenin ısı kapasitesini belirler ve yapının oluşması için hepsinin aynı kademede olması gerekir. Enerji kapağı, bakım kapağı ve çıkış yolu/kapağı yapının alt katmanındaki herhangi bir piroliz fırını kasasının yerini alabilir. Egzoz çıkışı ve giriş yolu/kapağı yapının üst katmanındaki herhangi bir piroliz fırını kasasının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı olabilir--EYF ve neredeyse her GregTech Multiblokunda olduğu gibi. Isıtma bobinlerinin kademesini belirtmek üzere "coil" alt kanalıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15546"/><ItemImage id="gregtech:gt.blockmachines:15546"/>
- 60-68 <ItemLink id="gregtech:gt.blockcasingsNH:2"/><ItemImage id="gregtech:gt.blockcasingsNH:2"/>
- 12 Isıtma Bobini (kademeli) <ItemImage id="gregtech:gt.blockcasings5:11"/>
- 8 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 4 <ItemLink id="gregtech:gt.blockcasings3:14"/><ItemImage id="gregtech:gt.blockcasings3:14"/>
- 2 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 1+ Enerji Kapağı (herhangi bir alt katman kasası) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir alt katman kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir üst katman kasası) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir üst katman kasası) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir üst katman kasası) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir alt katman kasası) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir alt katman kasası) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Piroliz Fırınları</Color>, kasa, çerçeve kutusu ve yol/kapaklardan tasarruf etmek için yanlarının her birini duvar paylaşımına açabilir. Buna, yukarıdaki görselde görüldüğü gibi ısıtma bobinlerinin yarısına kadarı da dahildir. Isıtma bobinleri yapının en pahalı kısmı olduğundan bu şiddetle önerilir. 

## Kullanım
<Color id="GREEN">Piroliz Fırını</Color>, ısıtma bobinlerinin kademesiyle doğrusal olarak ölçeklenen bir hız bonusu kazanır. Daha spesifik olarak, işleme hızı bakır-nikel bobinlerle %50'de başlar ve bunun üzerindeki her ısıtma bobini kademesinde %50 artar; aşağıdaki tabloda görüldüğü gibi. Temel işleme süresi 16 saniye olan ve hız aşırtma içermeyen bir tarifin süresi referans olarak verilmiştir. Hız bonusu, EU/t aynı kaldığı için Piroliz Fırınının güç tüketimini ARTIRMAZ. Aksine, daha kısa süre çalıştığı için tüketilen toplam EU'yu aslında azaltır. 

| Isıtma Bobini | Hız | Örnek | Toplam EU |
| --------------- | --------------- | --------------- | --------------- |
| Bakır-Nikel | 50% | 32.00s | 200% |
| Kantal | 100% | 16.00s | 100% |
| Nikrom | 150% | 10.67s | 66.7% |
| TPV-Alaşım | 200% | 8.00s | 50.0% |
| HSS-G | 250% | 6.40s | 40.0% |
| HSS-S | 300% | 5.33s | 33.3% |
| Naquadah | 350% | 4.57s | 28.6% |
| Naquadah Alaşımı | 400% | 4.00s | 25.0% |
| Trinyum | 450% | 3.56s | 22.2% |
| Elektrum Flaks | 500% | 3.20s | 20.0% |
| Uyandırılmış Drakonyum | 550% | 2.91s | 18.2% |
| Sonsuzluk | 600% | 2.67s | 16.7% |
| Hipojen | 650% | 2.46s | 15.4% |
| Ebedi | 700% | 2.29s | 14.3% |

<Color id="GREEN">Piroliz Fırını</Color> esas olarak kütükleri odun kömürüne yakmak için kullanılır ve isteğe bağlı BİR sıvı yan ürün üretir--bu, giriş yolu veya kontrolcüdeki programlanmış devre tarafından belirlenir. En yaygın seçenek odun kömürü yan ürünleridir çünkü bunlar bir Damıtma Kulesi <ItemImage id="gregtech:gt.blockmachines:1126"/> içinde dimetilbenzen, odun gazı, odun sirkesi ve odun katranına ayrışır. Bir diğer yaygın seçenek, nitrobenzeni daha doğrudan/verimli üretmek için odun katranıdır. Ayrıca, makinenin işleme hızını çift katına çıkarmak için 16 kütük başına 1.000L azot gazı kullanma seçeneği de vardır; bu da yine giriş yolu veya kontrolcüdeki programlanmış devre tarafından belirlenir.