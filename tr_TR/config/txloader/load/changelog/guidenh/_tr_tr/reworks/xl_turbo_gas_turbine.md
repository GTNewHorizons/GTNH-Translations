---
item_ids:
  - gregtech:gt.blockmachines:15522
navigation:
  title: XL Turbo Gaz Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15522
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# XL Turbo Gaz Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15522"/>
</GameScene>
<Color id="GREEN">XL Turbo Gaz Türbini (XLGT)</Color>, gazdan muazzam güç üretmek için kullanılan bir LuV kademesi multibloğudur. <Color id="GREEN">XLGT</Color>, Büyük Gaz Türbinine göre doğrudan bir yükseltmedir çünkü yalnızca 12 türbinle 16 kat iş hacmi sunar, çok amperli ve lazer dinamo kapaklarını destekler ve makine çalışırken dinamo kapağı kırılsa bile patlamaz. Ancak makinenin çalışması için türbinlerin birebir aynı olması gerekir, optimal akış hızını aşmanın cezaları daha ağırdır, benzen kara listededir ve makinenin tam ısınması için en az 50 saniye çalışması gerekir. Lapotronik Süperkapasitöre bağlı bir RS mandalıyla <Color id="GREEN">XLGT</Color>'yi otomatik açıp kapatarak yakıttan tasarruf et. <ItemImage id="gregtech:gt.blockmachines:13106"/>

[GTNH Güç Planlayıcısı](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Bu multibloğun yalnızca yapısı değişti; mekanikler aynı kaldı

## İnşa
<Color id="GREEN">XLGT</Color>'nin kademeli bileşeni yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Solenoid bobinler özellikle MV olmalıdır ve bunların da makinenin çalışmasına etkisi yoktur. Veriyolları/kapaklar yapının herhangi bir yerindeki Türbin Gövdesinin yerini alabilir. Ciddi güç üretimi için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteklenir ve birden fazla olabilir. Türbinleri bir Giriş Yolu üzerinden veya kontrolcünün arayüzünden yerleştir. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15522"/><ItemImage id="gregtech:gt.blockmachines:15522"/>
- 340-345 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:3"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:3"/>
- 104 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 80 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 76 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 20 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1+ Dinamo Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:90" />
- 4 Egzoz Çıkışı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ Giriş Yolu (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Girdi Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />

### Duvar Paylaşımı
<Color id="GREEN">XLGT</Color>'ler kasa, çerçeve kutusu, cam ve veriyolu/kapaktan tasarruf etmek için her yüzünü duvar paylaşabilir. Ancak Girdi Kapağını paylaşma; yakıt <Color id="GREEN">XLGT</Color>'ler arasında eşit bölünmez -- biri her şeyi tüketir, diğeri hiçbir şey almaz.

## Kullanım
Gazın <Color id="GREEN">XLGT</Color>'ye giriş hızı (L/t) son derece önemlidir. Gaz çok azsa potansiyel gücün yalnızca bir kısmı üretilir; çok fazlaysa muazzam miktarda yakıt boşa gider. İdeal olarak gaz, türbinin optimal akış hızında <Color id="GREEN">XLGT</Color>'ye girer; bu hız türbin boyutu/malzemesi ve makinenin çalışma moduyla önemli ölçüde değişir. NEI'de görünse de optimal akış hızı ($$\dot{m}^*$$) L/t cinsinden aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpan, size 1=küçük ile 4=dev arasında bir sabit ve $$\eta_0$$ türbinin temel verimidir. Bunların Büyük Gaz Türbinin optimal akış hızlarının tam olarak 16 katı olduğunu unutma.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 800 \div EU/L">
  Burada:
  - $$\dot{m}^*$$: Optimal Yakıt Hızı
  - $$k$$: Malzeme Çarpanı
  - size: Türbin boyutuna göre sabit (1=küçük, 4=dev)
</Latex>
<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 1,600 \div EU/L \times 1.05^{20(\eta_0 - 0.8)}">
  Burada:
  - $$\dot{m}^*$$: Optimal Yakıt Hızı
  - $$k$$: Malzeme Çarpanı
  - size: Türbin boyutuna göre sabit (1=küçük, 4=dev)
  - $$\eta_0$$: Temel Verim
</Latex>

Sıkı geçme modunda optimal akış hızını hesaplamanın daha hızlı ve kolay yolu, optimal gaz EU/t değerini (NEI'de görünür) aşağıdaki tabloda listelenen gazın yoğunluğuna bölmek ve sonucu 16 ile çarpmaktır. Bazılarının yoğunluğu çok düşüktür ve bu yüzden optimal akış hızları çok yüksektir -- özellikle <Color id="GREEN">XLGT</Color> gevşek geçme modundaysa. Artan talebi karşılamak için sıvı regülatörünü yükseltmen veya ikinci bir Girdi Kapağı eklemen gerekebilir. Bir noktadan sonra, pratikte aktarım sınırı olmayan ve sıcaklığı ya da ısı kapasitesini dikkate almayan AE2 sıvı P2P tünellerine geçmek gerekli hale gelir.

> [!IMPORTANT]
> Benzen, <Color id="GREEN">XLGT</Color>'de kara listededir

## Güç
<Color id="GREEN">XLGT</Color>'nin ürettiği güç, mevcut akış hızına ($$\dot{m}$$), optimal akış hızına ($$\dot{m}^*$$) ve türbinlerin verimine ($$\eta$$) bağlıdır. Optimal akış hızını aşmak yalnızca verimi düşürmez, aynı zamanda üretilen toplam gücü de azaltır. Taşma kademesinin makinenin çalışmasına etkisi yoktur. Makinenin mevcut güç çıktısını kontrolcüye bakarken WAILA üzerinden veya bir endüstriyel bilgi paneliyle görüntüle.

Güç, yapının herhangi bir yerindeki lazer veya çok amperli dinamo kapağından alınır. Dinamonun tamponundaki maksimum EU/t veya toplam EU değerini aşmak tamamen güvenlidir; bağlı bir pil tamponu veya Lapotronik Süperkapasitör (LSC) doluysa ve EU'nun gidecek yeri yoksa <Color id="GREEN">XLGT</Color> patlamaz. Fazladan EU basitçe yok edilir. Yakıt israfını önlemek için <Color id="GREEN">XLGT</Color>'yi kızıltaş RS mandalıyla otomatik açıp kapatman şiddetle önerilir.

<Latex formula="EU/t = \dot{m} \times \Biggl( 1 - \frac{| \dot{m} - \dot{m}^* |}{\dot{m}^*} \Biggr) \times EU/L \times \eta">
  Burada:
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Türbin Verimi
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times 1.25">
  Burada:
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
</Latex>

# Türbinler
Makinenin çalışması için 12 türbinin hepsi birebir aynı olmalıdır. Türbinler dört farklı boyutta ve her biri kendi verim bonusuna ve optimal akış hızına sahip birçok farklı malzemede gelir. Buraya sığdıramayacağımız kadar çok farklı permütasyon var, ancak üstte bağlantısı verilen planlayıcı tüm ilgili bilgileri ve hatta herhangi bir yakıtla herhangi bir türbinin güç çıktısını ve yaşam ömrünü belirlemek için bir hesaplayıcı içerir.

- Küçük türbinler uzun magnalyum çubuklarla üretilir (LV kadar erken erişilebilir)
- Normal türbinler uzun titanyum çubuklarla üretilir (Ay'a gittikten sonra HV'nin sonunda erişilebilir <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- Büyük türbinler uzun tungsten çeliği çubuklarla üretilir (tungsten işleme hattından sonra IV'te erişilebilir)
- Dev türbinler uzun amerikyum çubuklarla üretilir (Füzyon Reaktörü Mk-II inşa ettikten sonra ZPM'de erişilebilir <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## Dayanıklılık
Türbinler, üretilen güçle orantılı olarak yavaşça dayanıklılık kaybeder. Bir türbinin toplam dayanıklılığı malzemeye bağlıdır ve sıfıra düştüğünde anında yok olur. Türbinler Giriş Yolu aracılığıyla kontrolcüye otomatik olarak yerleştirilebilir, ancak otomatik olarak çıkarılamaz.

Aşağıdaki denklem, bir <Color id="GREEN">XLGT</Color>'nin mevcut güç çıktısından türbinlerin yaşam ömrünü (saat cinsinden) hesaplar. Gevşek geçme modunun, daha yüksek güç çıktısının kısalttığı yaşam ömrünü telafi etmek için %25 dayanıklılık artışı sağladığını unutma; türbinler burada Büyük Buhar Türbinindekinden çok daha uzun dayanır. Türbinlerin yaşam ömrü genellikle birkaç yüz saat (veya daha fazla) olduğundan çok sık değiştirilmeleri gerekmez.

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- Gevşek geçme modunda yaşam ömrü sonucunu 1.25 ile çarp.