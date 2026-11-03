---
item_ids:
  - gregtech:gt.blockmachines:12792
navigation:
  title: Ekstrem Endüstriyel Sera
  parent: reworks.md
  icon: gregtech:gt.blockmachines:12792
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-16
---

# Ekstrem Endüstriyel Sera

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12792"/>
</GameScene>
<Color id="GREEN">Ekstrem Endüstriyel Sera (EIG)</Color>, devasa bir tarla kurmaya gerek kalmadan binlerce ekin yetiştirmek için IV kademe bir multibloktur. Tüm tohumlar makinenin içinde yetiştirilir ve hasat edilir, asla dünyaya fiziksel olarak yerleştirilmez; bu da TPS tasarrufu sağlar ve lojistiği basitleştirir. <Color id="GREEN">EIG</Color>'nin kapasitesi enerji kapağının kademesine ve dolayısıyla camın kademesine bağlıdır. <Color id="RED">CropsNH</Color> tohumları DESTEKLENMEZ; bunlar Industrial Farm'da yetiştirilmelidir. Her zaman Su gerekir ve 1000'den fazla tohum varsa Weed-EX gerekir. Aksi halde her işlemde tohumların yaklaşık %1'i yok olur. Gübre isteğe bağlıdır ve hasat başına toplam ekin miktarını artırır. 

<br clear="all"/>

> [!NOTE]
> <Color id="GREEN">EIG</Color> artık sadece... şey, bir seraya benzemekle kalmıyor, aynı zamanda otomatik arazi hazırlama özelliklerine de sahip! Tamamlanmış bir yapı kontrolünden sonra toprağı otomatik olarak sürer ve içine su blokları yerleştirir.
> Ayrıca artık diğer multibloklarla aynı yöntemleri kullanarak otomatik yerleştirmeyi tam olarak destekliyor!<ItemImage id="structurelib:item.structurelib.constructableTrigger" />


## İnşaat
<Color id="GREEN">EIG</Color>'nin kademeli tek bir bileşeni vardır. Cam, enerji kapağının maksimum kademesini belirler. Yollar/kapaklar yapının herhangi bir yerindeki steril çiftlik kasalarının yerini alabilir. <Color id="RED">Çok Amperli ve Lazer Kapakları</Color> desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı olabilir. <Color id="GREEN">EIG</Color> içindeki toprak blokları RandomThings modundan gübrelenmiş toprak, lambalar ise ProjectRed Illumination modundan mor lamba olmalıdır. Lambalar başka bir renkte olamaz ancak enerji verilebilir ve/veya ters çevrilebilir. Toprak, yapı kurulduğunda sürülür ve su ücretsiz olarak oluşturulur, bu nedenle elle yerleştirilmesi GEREKMEZ. Su sağlamak için bir girdi kapağı yerine bir <ItemLink id="gregtech:gt.blockmachines:12972" /> <ItemImage id="gregtech:gt.blockmachines:12972" /> önerilir. Yapıyı camın kademesini belirten "glass" alt kanalıyla görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" /> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:12792" /> <ItemImage id="gregtech:gt.blockmachines:12792"/>
- 102 Kademeli Cam (gerilim kademesiyle uyumlu) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 70-85 <ItemLink id="miscutils:gtplusplus.blockcasings.2:15" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:15" />
- 33 <ItemLink id="gregtech:gt.blockframes:316" /> <ItemImage id="gregtech:gt.blockframes:316" />
- 21 <ItemLink id="RandomThings:fertilizedDirt" /> <ItemImage id="RandomThings:fertilizedDirt" />
- 3 Mor Lamba (ProjectRed Illumination, normal veya ters çevrilmiş)

- 1+ Enerji Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 Bakım Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ Giriş Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ Girdi Kapağı (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir kasa) <ItemImage id="gregtech:gt.blockmachines:80" />

### Duvar Paylaşımı
<Color id="GREEN">EIG</Color>'ler kasa, cam, çerçeve kutuları ve yol/kapaklardan tasarruf etmek için her bir kenarını duvar paylaşabilir. Buna su sağlayan rezervuar kapağı da dahildir. 

## Kullanım
<Color id="GREEN">EIG</Color>'nin aşağıda listelenen üç çalışma modu vardır. Modları kontrolcünün içindeki yapılandırma menüsünden veya kontrolcüye tornavidayla sağ tıklayarak değiştir. Makine devre dışıyken mevcut moddan bağımsız olarak tohumlar kontrolcünün GUI'si aracılığıyla yerleştirilebilir veya çıkarılabilir. Çalışma modu ek tohum üretmez, yalnızca ürün üretir.

- <Color id="GREEN">Girdi</Color> - Giriş yolu aracılığıyla EIG'ye tohum (ve gerekli blokları) yerleştirir. Güç tüketmez.
- <Color id="RED">Çalışma</Color> - Tohumları büyütür ve ekinleri hasat eder. 1 enerji kapağıyla 1A, 2 enerji kapağıyla 4A güç tüketir.
- <Color id="BLUE">Çıktı</Color> - Çıkış yolu aracılığıyla EIG'den tohumları (ve gerekli blokları) çıkarır. Güç tüketmez.

Yapılandırma menüsündeki IC2 modu, GTNH 2.9'da kullanımdan kaldırılmadan önceki IC2 tohum torbaları içindi. Artık nem moduyla birlikte hiçbir şey yapmaz ve makinenin çalışması için devre dışı bırakılmalıdır. CropsNH tohumları DESTEKLENMEZ; bunlar Industrial Farm'da yetiştirilmelidir.

