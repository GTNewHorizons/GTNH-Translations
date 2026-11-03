---
item_ids:
  - gregtech:gt.blockmachines:15548
navigation:
  title: Endüstriyel Ark Fırını
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15548
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-31
---

# Endüstriyel Ark Fırını

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15548"/>
</GameScene>
<Color id="GREEN">Endüstriyel Ark Fırını (IAF)</Color>, malzemeleri elektrik arkıyla aşırı ısıtmak ve parçalarına ayırmak için IV kademe bir multibloktur. <Color id="GREEN">IAF</Color>, tek bloklu ark fırınından doğrudan bir yükseltmedir; farklı amaçlara yönelik çeşitli modlar çalıştırabilir, <Color id="RED">10 kat</Color> hıza, çifte mükemmel (8/4) overclock'a ve <Color id="BLUE">1024</Color> paralele kadar olanak sunar. Ciddi overclock için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir. <Color id="GREEN">IAF</Color> ayrıca çoğu tarifte plazma kullanabilir; bu, tek bloklu ark fırınlarında artık mümkün değildir.
<br clear="all"/>

> [!NOTE]
> Multiblokta (yapı dışında) aşağıdaki değişiklikler yapıldı:
> - Farklı Modlar: "Normal", EYF modu (EYF tarifleri 16 kat daha fazla güçle), Cevher modu (fırında eritilebilen ham cevherleri işleyerek eriyik metal verir)
> - Yeni Elektrot Mekanikleri: IAF artık makinenin istatistiklerini belirleyen bir Elektrot eşyası alır. Değişiklikler kapsamlı olduğundan ayrıntılar için aşağıya bak

## Yapım
<Color id="GREEN">IAF</Color>'ın kademeli bileşeni yoktur. Ciddi overclock için çok amperli enerji kapakları desteklenir. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15548"/><ItemImage id="gregtech:gt.blockmachines:15548"/>
- 175 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 10-173 <ItemLink id="gregtech:gt.blockcasings2"/><ItemImage id="gregtech:gt.blockcasings2"/>
- 101 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 72 <ItemLink id="bartworks:bw.werkstoffblockscasing.01:32090"/><ItemImage id="bartworks:bw.werkstoffblockscasing.01:32090"/>
- 30 Isıtma Bobini (herhangi biri) <ItemImage id="gregtech:gt.blockcasings5:13"/>
- 17 <ItemLink id="miscutils:miscutils.blockcasings:14"/><ItemImage id="miscutils:miscutils.blockcasings:14"/>
- 15 <ItemLink id="gregtech:gt.blockcasings13:4"/><ItemImage id="gregtech:gt.blockcasings13:4"/>
- 12 <ItemLink id="gregtech:gt.blockcasings13:2"/><ItemImage id="gregtech:gt.blockcasings13:2"/>
- 12 <ItemLink id="miscutils:miscutils.blockcasings:3"/><ItemImage id="miscutils:miscutils.blockcasings:3"/>
- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1 Elektrot Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:14203" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ Çıkış Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:60" />
- 0+ Elektrot Dedektör Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:14204" />


### Duvar Paylaşımı
<Color id="GREEN">IAF</Color>'lar kasa ile veriyolu/kapaklardan tasarruf etmek için her bir yanlarını komşu makinelerle paylaşabilir. Enerji kapaklarını paylaşırken dikkat et; farklı elektrotların amper gereksinimleri farklı olabilir.

## Kullanım
<Color id="GREEN">IAF</Color>'ın aşağıda açıklanan 3 çalışma modu vardır. Hangi mod seçilirse seçilsin bir <Color id="BLUE">Başlatma Süresi</Color> (normal için 6 saniye, cevher modu için 10 saniye) ve ark işi bittikten sonra bir kapanma aşaması olur. Hız, paralel, overclock ve güç kullanımı, elektrot kapağına yerleştirilen zorunlu elektrot tarafından belirlenir. Mevcut elektrotlardan bazılarının özel bonusları vardır; seçim yapmana yardımcı olması için NEI'deki ipucunu mutlaka kontrol et!

Başlatmada ark fırını, işlemeden önce arkı ateşlemelidir; tarifler bittikten sonra 6 saniyelik bir kapanma aşaması yaşanır.

### Normal Mod:
<Color id="GREEN">IAF</Color> bu modda standart ark fırını tariflerini, geri dönüşüm tarifleri dahil, işler. Normal tariflerin çoğu isteğe bağlı olarak plazma da kullanabilir; bu, tek bloklu ark fırınında artık mümkün değildir.

### Yüksek Fırın Modu:
<Color id="GREEN">IAF</Color> artık tüm EYF tariflerini işleyebilir, ancak güç maliyetinin 16 katı karşılığında. Yeterli gücün varsa bu, EYF'lerindeki yükün bir kısmını hafifletebilir.

### Cevher Modu:
<Color id="GREEN">IAF</Color> bu modu cevherleri ve ham cevherleri doğrudan eriyik metale dönüştürmek için kullanabilir. Bu yalnızca girdi cevherleri bir fırında doğrudan eritilebiliyorsa (örneğin bir işleme hattı veya EYF gerektirmiyorsa) çalışır.

Bu modda başlatma süresi 10 saniyedir. Tüm giriş yollarındaki tüm cevherleri ve ham cevherleri tüketir. Kuyruğa alınan cevher miktarı kapasiteyi aşarsa başlatma aşaması hemen sona erer. 5 tick boyunca cevher girilmezse başlatma yine hemen sona erer.

## Elektrot Bakımı
Her işlem gerçekleştiğinde elektrot kapağındaki elektrot hasar alır. Elektrotlar elektrot kapağına takılır; elektrotu almak veya değiştirmek makinede güç kesintisine yol açar. Bu, 0 tick'lik değişimleri de kapsar; yani elektrot değiştirmek için makinenin gücü kesilmelidir.

- %30'un altındaki dayanıklılıkta rastgele bir ark dalgalanması şansı %5'tir (arkı yeniden başlatır)
- %10'un altındaki dayanıklılıkta arktaki eşyaları yok etme şansı %2'dir

Bu nedenle elektrot değişimini alınan hasara göre otomatikleştirmek çok önemlidir. Bu otomasyona, dayanıklılığı algılayan ve GUI'sinde yapılandırılabilir bir eşikte kızıltaş sinyali veren Elektrot Dedektör Kapağı yardımcı olabilir.

<Color id="GREEN">IAF</Color> __kademe atlayamaz__. Başlatmada makine $$\text{MaxParallels} \times \text{AmpsPerParallel} \times (1+\text{SurgePenalty})$$ amper çeker; bu, elektrota bağlı olarak oldukça yüksek olabilir!