---
item_ids:
  - gregtech:gt.blockmachines:15557
navigation:
  title: Termal Kazan
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15557
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Termal Kazan

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15557"/>
</GameScene>
<Color id="GREEN">Termal Kazan</Color>, lav, pahoehoe lavı, sıcak soğutucu veya sıcak güneş tuzundan gelen ısıyla suyu buhara buharlaştıran bir IV kademesi multibloktur. Ayrıca lavdan veya pahoehoe lavından birkaç yan ürün toplar, ancak yalnızca kontrolcünün içinde bir lav filtresi varsa. <Color id="GREEN">Termal Kazan</Color> hiçbir güç veya yakıt tüketmez, ancak yeterli su verilmezse yine de patlama riski taşır. Dört sıcak sıvı tarifinin tamamı sabittir, bu yüzden giriş/çıkış hızlarında esneklik yoktur. Sıcak sıvının %100'ü her zaman daha soğuk eşdeğerine geri dönüştürülür ve buharın %100'ü maksimum verimde [Büyük Buhar Türbinleri](./large_steam_turbine.md) tarafından damıtılmış suya geri dönüştürülür--bu da sürdürülebilir bir kapalı döngü sistemi oluşturur. Alternatif olarak giriş olarak bir su rezervuarı kapağı kullan ve fazla damıtılmış suyu yok et. <Color id="GREEN">Termal Kazan</Color>'ın yerini LuV'de Aşırı Isı Eşanjörü <ItemImage id="gregtech:gt.blockmachines:32017"/> ve Whakawhiti Wera XL <ItemImage id="gregtech:gt.blockmachines:31079"/> alır, ancak yalnızca buhar debisi açısından.

<Color id="GREEN">Termal Kazan</Color>, Büyük Isı Eşanjörüne (LHE) <ItemImage id="gregtech:gt.blockmachines:1154"/> çok benzer. Fark, LHE'nin daha yüksek debiye sahip olması, yan ürün üretmemesi, yalnızca damıtılmış su kullanması ve pahoehoe lavı kabul etmemesidir. Başka bir deyişle, tantal, tungstat veya altın gibi kaynaklar için <Color id="GREEN">Termal Kazan</Color>'ı, güç için ise LHE'yi kullan.

[GTNH Güç Planlayıcısı](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit)
<br clear="all"/>

> [!NOTE]
> Bu multiblokun yalnızca yapısı değişti, mekanikler aynı kaldı

## İnşaat
<Color id="GREEN">Termal Kazan</Color>'ın kademeli bileşeni yoktur. Bakım kapağı ve egzoz çıkışı yapının herhangi bir yerindeki termal muhafaza kasasının yerine geçebilir. Giriş ve çıkış kapakları yapının herhangi bir yerindeki termal işleme kasasının veya sağlam tungsten çelik makine gövdesinin yerine geçebilir--aralarında eşit olarak bölünmeleri veya belirli bir şekilde düzenlenmeleri gerekmez. Her zaman yeterli su sağlamak için bir rezervuar kapağı kullanman şiddetle önerilir; ancak kullanmazsan sıcak sıvı ve su aynı girdi kapağından girebilir, tıpkı soğuk sıvı ve buharın makineden aynı çıkış kapağından çıkabilmesi gibi. Makine hiçbir güç tüketmediği için enerji kapağı yoktur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15557"/><ItemImage id="gregtech:gt.blockmachines:15557"/>
- 20-25 <ItemLink id="miscutils:gtplusplus.blockcasings.2:11"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:11"/>
- 10-17 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 10-17 <ItemLink id="miscutils:gtplusplus.blockcasings.2"/><ItemImage id="miscutils:gtplusplus.blockcasings.2"/>
- 16 <ItemLink id="miscutils:blockFrameGtMaragingSteel350"/><ItemImage id="miscutils:blockFrameGtMaragingSteel350"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 1 Bakım Kapağı (herhangi bir termal muhafaza kasası) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 Egzoz Çıkışı (herhangi bir termal muhafaza kasası) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Girdi Kapağı (herhangi bir termal işleme veya tungsten çeliği makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Yolu (herhangi bir termal işleme veya tungsten çeliği makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:80" />
- 1+ Çıkış Kapağı (herhangi bir termal işleme veya tungsten çeliği makine gövdesi) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">Termal Kazanlar</Color> kasa, çerçeve kutusu ve veriyolu/kapaklardan tasarruf etmek için her bir yüzlerini duvar paylaşımına açabilir. Giriş/çıkış hızlarının tamamı sabittir, bu yüzden giriş veya çıkış kapaklarını paylaşmakta sorun yoktur. Tüm <Color id="GREEN">Termal Kazanlar</Color>'ın hâlâ yeterli su aldığından ve çıkış kapağının birleşik buhar çıkışını destekleyecek kadar büyük olduğundan emin ol (10.000 L/t SH Buharı için LV+). 

## Kullanım
<Color id="GREEN">Termal Kazan</Color>, lav, pahoehoe lavı, sıcak soğutucu veya sıcak güneş tuzundan gelen ısıyla suyu buhara buharlaştırır. Gerekirse damıtılmış su da işe yarar. <Color id="GREEN">Termal Kazan</Color> güç tüketmez, ancak susuz 10 saniyeden uzun süre çalışırsa patlar. Aktif olarak çalışırken su eklemek veya kontrolcüyü kırmak tamamen güvenlidir. Su olmadan buhar ÜRETİLMEZ.

<Color id="GREEN">Termal Kazan</Color>'ın, buhar çıkış hızıyla ve dolayısıyla kapalı döngü sisteminde makineye geri dönüştürülen damıtılmış su miktarıyla doğru orantılı kendi verim değeri vardır. <Color id="GREEN">Termal Kazan</Color>'ın verimi makine aktifken doğrusal olarak artar ve boştayken neredeyse anında %0 seviyesine geri döner. Maksimum verime ulaşması yaklaşık 42 saniye sürer, bu yüzden istikrarlı bir sıcak sıvı beslemesi sağlamak çok önemlidir. Bakım sorunlarının her biri maksimum verimi %10 azaltır.

## Isı Değişimi
<Color id="GREEN">Termal Kazan</Color> saniyede bir kez sıcak sıvıyı daha soğuk sürümüne, suyu da buhara dönüştürür. Üretilen buhar türü kesinlikle sıcak sıvı türüne bağlıdır ve hepsi sabit değerler olduğundan giriş hızına göre değişmez. Fazla girdi TÜKETİLMEZ.

## Yan Ürünler
<Color id="GREEN">Termal Kazan</Color> öncelikle lavdan veya pahoehoe lavından yan ürün üretmek için kullanılır. Obsidyen dışındaki yan ürünlerin üretilme şansına sahip olması için bile kontrolcünün içinde bir lav filtresi gerekir. Lav filtreleri 100 dayanıklılık puanıyla başlar ve her işlemde 1/30 şansla bir puan kaybeder. Bu, bir lav filtresinin ortalama yaşam ömrünün 3.000 işlem veya 50 dakika olduğu anlamına gelir. Sıcak soğutucu ve sıcak güneş tuzu hiçbir yan ürün üretmez ve bu nedenle lav filtresine ihtiyaç duymaz. Lav filtresi olsun olmasın buhar yine de üretilir. 

Lav kaynakları arasında Everburn Urn'lar <ItemImage id="ThaumicExploration:everburnUrn"/>, Ross128b'deki Sıvı Sondaj Kuleleri <ItemImage id="gtneioreplugin:blockDimensionDisplay_Rb"/> veya Simmering peteklerinden elde edilen fosfor <ItemImage id="Forestry:beeCombs:2"/> bulunur. Bu üç seçenek arasında Everburn Urn en iyisidir; çünkü güç gerektirmez ve <Color id="GREEN">Termal Kazan</Color> ile aynı yere yerleştirilebilir.

## Güç
Birincil amacı olmasa da, <Color id="GREEN">Termal Kazan</Color>'ın ürettiği buhar, aşağıda listelenen sırayla bir dizi [Büyük Buhar Türbini](./large_steam_turbine.md) ile güç üretmek için kullanılır. Her iki buhar türü de aynı dönüşüm oranına sahiptir, bu yüzden birinin çıkışı doğrudan diğerinin girişini besleyebilir. Maksimum verimde buharın %100'ü damıtılmış suya geri dönüştürülür--bu da sürdürülebilir bir kapalı döngü sistemi oluşturur. Daha sonra bunların her birinin XL Turbo varyantları kullanılabilir. SH buharı, aynı optimal akış hızında normal buhardan 2 kat daha fazla EU üretir.

- Büyük Yüksek Basınç Buhar Türbini, SH buharından güç üretir ve onu 1:1 oranında normal buhara dönüştürür.
- Büyük Buhar Türbini, normal buhardan güç üretir ve onu 160:1 oranında damıtılmış suya dönüştürür.

Buhar debisi buhar valfleri veya sıvı boruları için çok yüksekse bunun yerine sıvı P2P tünelleri kullan. Aktarım sınırları yoktur ve tüm sıvıları tüm çıkış bağlantıları arasında eşit olarak dağıtırlar. 