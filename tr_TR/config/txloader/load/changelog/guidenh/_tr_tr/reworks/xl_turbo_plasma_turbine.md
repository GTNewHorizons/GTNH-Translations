---
item_ids:
  - gregtech:gt.blockmachines:15523
navigation:
  title: XL Turbo Plazma Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15523
categories:
    - Yapı Revizyonları
author: Skorched
date: 2026-05-27
---

# XL Turbo Plazma Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15523"/>
</GameScene>
<Color id="GREEN">XL Turbo Plazma Türbini (XLPT)</Color>, plazmadan muazzam güç üretmek için ZPM kademesinde bir Multibloktur. <Color id="GREEN">XLPT</Color>, Büyük Plazma Türbini'nin doğrudan yükseltmesidir; çünkü yalnızca 12 türbinle 16 kat işlem kapasitesine sahiptir, çok amperli ve lazer dinamo kapaklarını destekler ve makine çalışırken dinamo kapağı bozulsa bile patlamaz. Ancak makinenin çalışması için türbinler birebir aynı olmalıdır; optimum akış hızını aşmanın daha ağır cezaları vardır, daha düşük yoğunluklu yakıt kullanmanın cezaları vardır ve makinenin tamamen ısınması için en az 50 saniye çalışması gerekir. Lapotronik Süperkapasitör <ItemImage id="gregtech:gt.blockmachines:13106"/> ile bağlantılı bir RS mandalıyla <Color id="GREEN">XLPT</Color>'yi otomatik açıp kapatarak yakıttan tasarruf et. 
<br clear="all"/>


[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)

> [!NOTE]
> Bu Multiblokun yalnızca yapısı değişti; mekanikleri aynı kaldı

## İnşa
<Color id="GREEN">XLPT</Color>'de kademeli bileşenler yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışması üzerinde etkisi yoktur. Isıtma Bobinleri özellikle Naquadah olmalıdır ve bunların da makinenin çalışması üzerinde etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki herhangi bir Türbin Gövdesinin yerine geçebilir. Ciddi güç üretimi için <Color id="GREEN">Çok Amperli ve Lazer Dinamo Kapakları</Color> desteklenir ve birden fazla olabilir. Egzoz Çıkışı yoktur; bu yüzden bir tane eklemeyin. Türbinleri bir Giriş Yolu veya Kontrolcünün arayüzü üzerinden yerleştir. Camın kademesini belirtmek üzere "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15523"/><ItemImage id="gregtech:gt.blockmachines:15523"/>
- 330-351 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:4"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:4"/>
- 100 <ItemLink id="gregtech:gt.blockcasings5:5"/><ItemImage id="gregtech:gt.blockcasings5:5"/>
- 72 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 36 Kademeli Cam (herhangi biri) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 32 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1+ Dinamo Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1+ Giriş Yolu (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Girdi Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ Çıkış Kapağı (herhangi bir Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">XLPT</Color>'ler gövde, Isıtma Bobinleri ve yol/kapaklardan tasarruf etmek için her bir yanlarını duvar paylaşımıyla birleştirebilir. Ancak Girdi Kapağını paylaşmayın; çünkü yakıt <Color id="GREEN">XLPT</Color>'ler arasında eşit olarak bölünmez -- biri her şeyi tüketir, diğeri hiçbir şey almaz. 

## Kullanım
<Color id="GREEN">XLPT</Color>'nin aşağıda listelenen iki çalışma modu vardır; ancak aralarındaki ölçülebilir farklar için yukarıda bağlantısı verilen planlayıcıya bak. İlki, yakıt üretiminin düşük olduğu oyunun erken-orta aşamasında; ikincisi ise güç çıktısının verimlilikten daha önemli olduğu oyun sonunda daha iyidir. Kontrolcüye tornavida kullanarak modlar arasında geçiş yap.

- Sıkı Geçme Modu - Yüksek verimlilik, düşük optimum akış hızı (güç).
- Gevşek Geçme Modu - Düşük verimlilik, yüksek optimum akış hızı (güç).

<Color id="GREEN">XLPT</Color>'nin Hızı etkinken doğrusal olarak %100'e kadar artar ve etkin değilken %0 geri düşer. Hız, makinenin güç çıktısıyla doğru orantılıdır ve türbin boyutu/malzemesi ne olursa olsun maksimum değerine ulaşması 50 saniye sürer. <Color id="GREEN">XLPT</Color> devre dışı bırakıldığında, türbin çıkarıldığında, yapı bozulduğunda veya yakıt tükendiğinde Hız aşırı hızlı şekilde düşer. Türbinin mevcut hızını, Kontrolcüye bir Taşınabilir Tarayıcı <ItemImage id="gregtech:gt.metaitem.01:32762"/> kullanarak veya WAILA'daki "verimlilik" değerine bakarak görüntüle. 

## Optimum Akış Hızı
Plazmanın <Color id="GREEN">XLPT</Color>'ye giriş hızı (L/s) aşırı derecede önemlidir. Çok az plazma olursa potansiyel gücün yalnızca bir kısmı üretilir; çok fazla plazma olursa muazzam miktarda yakıt boşa harcanır. İdeal olarak plazma, <Color id="GREEN">XLPT</Color>'ye türbinin optimum akış hızında girer; bu hız boyut/malzeme ve makinenin çalışma moduna göre önemli ölçüde değişir. NEI'de görülebilse de, L/s cinsinden optimum akış hızı ($$\dot{m}^*$$), aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpan, boyut 1=küçük ile 4=dev arasında bir sabit ve $$\eta_0$$ türbinin temel verimliliğidir. Bunların, [Büyük Plazma Türbini](./large_plasma_turbine.md) optimum akış hızlarının tam olarak 16 katı olduğunu unutma. 

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 16,000 \div EU/L">
  Burada:
  - $$\dot{m}^*$$: Optimum Akış Hızı
  - $$k$$: Malzeme Çarpanı
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 32,000 \div EU/L \times 1.03^{20(\eta_0 - 0.8)}">
  Burada:
  - $$\dot{m}^*$$: Optimum Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\eta_0$$: Temel Verimlilik
</Latex>

Bazı plazmalar biraz daha düşük yoğunluğa ve dolayısıyla daha yüksek optimum akış hızına sahiptir -- özellikle <Color id="GREEN">XLPT</Color> gevşek moddayken. Oyuncunun artan talebi karşılamak için sıvı regülatörünü yükseltmesi veya ikinci bir Girdi Kapağı eklemesi gerekebilir. Sonunda, fiilen aktarım sınırı olmayan ve sıcaklık ya da ısı kapasitesini dikkate almayan AE2 sıvı P2P tünellerine geçmek gerekli hale gelir. 

> [!IMPORTANT]
> Daha düşük yoğunluklu yakıtlar kullanmanın bir güç cezası vardır; aşağıdaki denklemde görüldüğü gibi 

<Latex formula="\epsilon = \frac{(\text{EU/L} \div 200,000)^2}{\text{Optimal EU/t (Tight)}}"/>

## Güç
<Color id="GREEN">XLPT</Color> tarafından üretilen güç; mevcut akış hızına ($$\dot{m}$$), optimum akış hızına ($$\dot{m}^*$$), türbinlerin verimliliğine ($$\eta$$) ve yoğunluk cezasına ($$\epsilon$$) bağlıdır. Optimum akış hızını aşmak yalnızca daha az verimli olmakla kalmaz, aynı zamanda üretilen toplam güç miktarını azaltır. Taşma kademesinin makinenin çalışması üzerinde etkisi yoktur. Makinenin mevcut güç çıktısını Kontrolcüye bakarken WAILA üzerinden veya endüstriyel bir bilgi paneliyle görüntüle.

Güç, yapının herhangi bir yerindeki bir lazer veya çok amperli Dinamo Kapağından çekilir. Dinamonun Tamponundaki maksimum EU/t veya toplam EU değerini aşmak tamamen güvenlidir; bağlı bir Pil Tamponu veya Lapotronik Süperkapasitör (LSC) doluysa ve EU'nun gidecek bir yeri yoksa <Color id="GREEN">XLPT</Color> patlamaz. Fazladan EU basitçe yok edilir. Yakıt israfını önlemek için <Color id="GREEN">XLPT</Color>'yi Kızıltaş RS mandalıyla otomatik olarak açıp kapatman önemle tavsiye edilir.

<Latex formula="EU/t = \dot{m} \times \Biggl( 1 - \frac{| \dot{m} - \dot{m}^* |}{\dot{m}^*} \Biggr) \times EU/L \times \eta \times \epsilon \div 20">
  Burada:
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimum Akış Hızı
  - $$\eta$$: Türbin Verimliliği
  - $$\epsilon$$: Yoğunluk Cezası
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times 1.25">
  Burada:
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$\dot{m}^*$$: Optimum Akış Hızı
</Latex>

# Türbinler
Makinenin çalışması için 12 türbinin tamamı birebir aynı olmalıdır. Türbinler, her biri kendi verimlilik bonusuna ve optimum akış hızına sahip dört farklı boyut ve birçok farklı malzeme olarak gelir. Burada hepsini listelemek için çok fazla farklı kombinasyon var; ancak yukarıda bağlantısı verilen planlayıcıda tüm ilgili bilgiler ve herhangi bir türbinin herhangi bir yakıtla güç çıktısını ve yaşam ömrünü belirlemek için bir hesaplayıcı bile var.

- Küçük türbinler uzun magnalyum çubuklarıyla üretilir (LV'de bile erişilebilir)
- Normal türbinler uzun Titanyum çubuklarıyla üretilir (Ay'a gittikten sonra HV'nin sonunda erişilebilir <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- Büyük türbinler uzun Tungsten Çeliği çubuklarıyla üretilir (Tungsten işleme hattından sonra IV'te erişilebilir)
- Dev türbinler uzun Amerikyum çubuklarıyla üretilir (Füzyon Reaktörü Mk-II inşa ettikten sonra ZPM'de erişilebilir <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## Dayanıklılık
Türbinler, üretilen güçle orantılı olarak yavaş yavaş dayanıklılık kaybeder. Bir türbinin toplam dayanıklılığı malzemeye bağlıdır ve %0 ulaştığında anında yok olur. Türbinler Giriş Yolu aracılığıyla Kontrolcüye otomatik olarak yerleştirilebilir, ancak otomatik olarak çıkarılamaz.

Aşağıdaki denklem, bir <Color id="GREEN">XLPT</Color>'nin mevcut güç çıktısından türbinlerin yaşam ömrünü (saat cinsinden) hesaplar. Gevşek geçme modunun, daha yüksek güç çıktısının azalan yaşam ömrünü telafi etmek için %25 dayanıklılık artışı sağladığını ve türbinlerin burada Büyük Buhar Türbini'ndekinden çok daha uzun süre dayandığını unutma. Türbinler genellikle birkaç yüz saatlik (veya daha fazla) bir yaşam ömrüne sahiptir; bu yüzden çok sık değiştirilmeleri gerekmez. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- Gevşek geçme modunda yaşam ömrü sonucunu 1,25 ile çarp.