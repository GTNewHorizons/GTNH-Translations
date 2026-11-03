---
item_ids:
  - gregtech:gt.blockmachines:15519
navigation:
  title: XL Turbo Buhar Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15519
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# XL Turbo Buhar Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15519"/>
</GameScene>
<Color id="GREEN">XL Turbo Buhar Türbini (XLST)</Color>, buhardan muazzam güç üretmek için kullanılan bir EV kademe multibloktur. <Color id="GREEN">XLST</Color>, Büyük Buhar Türbini <ItemImage id="gregtech:gt.blockmachines:15524"/> üzerine doğrudan bir yükseltmedir; çünkü yalnızca 12 türbinle <Color id="RED">16x</Color> işleme kapasitesine sahiptir, <Color id="GREEN">Çok Amperli ve Lazer Dinamo Kapaklarını</Color> destekler, hem normal hem de yoğun buharı işler ve makine çalışırken dinamo kapağı bozulsa bile patlamaz. Ancak makinenin çalışması için türbinlerin birebir aynı olması gerekir, optimal akış hızının aşılmasında daha ağır cezalar vardır ve makinenin tamamen ısınması için en az 50 saniye çalışması gerekir. Lapotronik Süperkapasitöre <ItemImage id="gregtech:gt.blockmachines:13106"/> bağlı bir RS mandalı ile <Color id="GREEN">XLST</Color>'yi otomatik olarak açıp kapatarak yakıttan tasarruf et.

Yoğun buhar varyantları yalnızca Ekstrem Eşanjör <ItemImage id="gregtech:gt.blockmachines:32017"/> içinde plazma kullanılarak elde edilir ve normal buhar varyantlarına göre 1,000 kat yakıt yoğunluğuna sahiptir. Bu da optimal akış hızının yalnızca 1/1000'i ile aynı miktarda güç ürettikleri anlamına gelir. 

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1FTFdfmY_UWbTbFOyNzARKeI90pbHvPBH6M3JHJmaC-E/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Bu multiblokta yalnızca yapı değişti, mekanikler aynı kalıyor

## İnşaat

<Color id="GREEN">XLST</Color>'nin kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur. Selenoid bobinler özellikle MV olmalıdır ve bunların da makinenin çalışmasına etkisi yoktur. Yollar/kapaklar yapının herhangi bir yerindeki türbin gövdelerinin yerini alabilir. Ciddi güç üretimi için <Color id="GREEN">Çok Amperli ve Lazer Dinamo Kapakları</Color> desteklenir ve birden fazla olabilir. Egzoz Çıkışı yoktur, bu yüzden bir tane ekleme. Türbinleri bir Giriş Yolu veya kontrolcünün arayüzü aracılığıyla yerleştir. Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

### Gereksinimler:
- 1 XL Turbo Buhar Türbini Kontrolcüsü (türe bağlı)<ItemImage id="gregtech:gt.blockmachines:15519"/>
- 372-439 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:1"/>
- 100 Boru Muhafazası (türe bağlı) <ItemImage id="gregtech:gt.blockcasings2:13"/>
- 36 Kademeli Cam (herhangi)
- 34 Çerçeve (türe bağlı) <ItemImage id="gregtech:gt.blockframes:305"/>
- 20 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 1 Dinamo Kapağı (herhangi bir türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1+ Giriş Yolu (herhangi bir türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ Girdi Kapağı (herhangi bir türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ Çıkış Kapağı (herhangi bir türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">XLST</Color>'ler gövde, çerçeve ve yol/kapaklardan tasarruf etmek için her bir kenarında duvar paylaşımı yapabilir. Ancak girdi kapağını paylaşma; çünkü yakıt <Color id="GREEN">XLST</Color>'ler arasında eşit olarak paylaşılmaz -- biri her şeyi tüketir, diğeri hiçbir şey almaz. 

## Kullanım
<Color id="GREEN">XLST</Color>'nin aşağıda listelenen iki çalışma modu vardır, ancak aralarındaki ölçülebilir farklar için yukarıda bağlantılı planlayıcıya bak. İlki, buhar üretiminin düşük olduğu oyunun başından ortasına kadar daha iyidir; ikincisi ise güç çıkışının verimlilikten daha önemli olduğu oyunun sonlarında daha iyidir. Kontrolcüye tornavida kullanarak modlar arasında geçiş yap.

- Sıkı Oturma Modu - Yüksek verimlilik, düşük optimal akış hızı (güç).
- Gevşek Oturma Modu - Düşük verimlilik, yüksek optimal akış hızı (güç).

<Color id="GREEN">XLST</Color>'nin hızı etkinken doğrusal olarak %100'e kadar artar ve etkin değilken %0 geri düşer. Hız, makinenin güç çıkışıyla doğru orantılıdır ve türbin boyutu/malzemesi ne olursa olsun maksimum değerine ulaşması 50 saniye sürer. <Color id="GREEN">XLST</Color> devre dışı bırakıldığında, türbin çıkarıldığında, yapı bozulduğunda veya yakıt tükendiğinde hız son derece hızlı düşer. Kontrolcü üzerinde Taşınabilir Tarayıcı <ItemImage id="gregtech:gt.metaitem.01:32762"/> kullanarak veya WAILA'daki "efficiency" değerine bakarak türbinin mevcut hızını görüntüle. 

## Optimal Akış Hızı
Buharın <Color id="GREEN">XLST</Color>'ye girdiği hız (L/t) son derece önemlidir. Çok az buhar olursa potansiyel gücün yalnızca bir kısmı üretilir; çok fazla buhar olursa muazzam miktarda yakıt boşa harcanır. İdeal olarak buhar, <Color id="GREEN">XLST</Color>'ye türbinin optimal akış hızında girer; bu hız türbinin boyutu/malzemesi ve makinenin çalışma moduyla önemli ölçüde değişir. NEI'de görülebilse de, L/t cinsinden optimal akış hızı ($$\dot{m}^*$$) aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpan, size 1=küçük ile 4=dev arasında bir sabit ve $$\eta_0$$ türbinin temel verimliliğidir. Bunların Büyük Buhar Türbini'nin optimal akış hızlarının tam olarak 16 katı olduğunu ve buhar yoğunsa hızın 1,000'e bölündüğünü unutma.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 800">
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\text{size}$$: Türbin boyutuna göre (1:4) aralığındaki sabit
</Latex>
<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 2,400 \times 1.1^{20(\eta_0 - 0.8)}">
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\text{size}$$: Türbin boyutuna göre (1:4) aralığındaki sabit
  - $$\eta_0$$: Türbinin Temel Verimliliği
</Latex>

Bazı türbinlerin optimal akış hızları inanılmaz derecede yüksektir çünkü buharın yakıt yoğunluğu 0.5 EU/L gibi çok düşüktür; özellikle de <Color id="GREEN">XLST</Color> gevşek moddaysa. Yoğun buhar kullanmıyorsan, pratikte hiçbir transfer limiti olmayan ve sıcaklık ya da ısı kapasitesi endişesi taşımayan AE2 sıvı P2P tünellerini kullanmak neredeyse zorunludur.
| Yakıt   | EU/L    |
|--------------- | --------------- |
| Buhar   | 0.5   |
| Kızdırılmış (SH) Buhar   | 1.0   |
| Süperkritik (SC) Buhar   | 1.0   |
| Yoğun Buhar   | 500   |
| Yoğun Kızdırılmış (SH) Buhar | 1,000 |
| Yoğun Süperkritik (SC) Buhar | 1,000 |

## Güç
<Color id="GREEN">XLST</Color> tarafından üretilen güç; mevcut akış hızına ($$\dot{m}$$), optimal akış hızına ($$\dot{m}^*$$) ve türbinlerin verimliliğine ($$\eta$$) bağlıdır. Optimal akış hızını aşmak yalnızca daha az verimli olmakla kalmaz, aynı zamanda üretilen toplam güç miktarını da azaltır. Taşma kademesinin makinenin çalışmasına etkisi yoktur. Makinenin mevcut güç çıkışını kontrolcüye bakarken WAILA aracılığıyla veya bir endüstriyel bilgi paneliyle görüntüle.

Güç, yapının herhangi bir yerindeki lazer veya çok amperli dinamo kapağından çekilir. Dinamonun tamponundaki maksimum EU/t veya toplam EU değerini aşmak tamamen güvenlidir; bağlı bir pil tamponu veya Lapotronik Süperkapasitör (LSC) doluysa ve EU'nun gidecek yeri yoksa <Color id="GREEN">XLST</Color> patlamaz. Fazladan EU basitçe yok edilir. Yakıt israfını önlemek için <Color id="GREEN">XLST</Color>'yi bir kızıltaş RS mandalıyla otomatik olarak açıp kapatman şiddetle önerilir.

# Türbinler
Makinenin çalışması için 12 türbinin hepsi birebir aynı olmalıdır. Türbinler dört farklı boyutta ve her biri kendi verimlilik bonusuna ve optimal akış hızına sahip çok farklı malzemede bulunur. Hepsini burada listelemek için fazlasıyla permütasyon var, ancak yukarıda bağlantılı planlayıcıda tüm ilgili bilgiler ve herhangi bir türbinin herhangi bir yakıtla güç çıkışını ve yaşam ömrünü belirlemek için bir hesaplayıcı bile var.

- Küçük türbinler uzun magnalyum çubuklarla üretilir (LV kadar erken elde edilebilir)
- Normal türbinler uzun titanyum çubuklarla üretilir (Ay'a gittikten sonra HV'nin sonunda elde edilebilir <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- Büyük türbinler uzun tungsten çeliği çubuklarla üretilir (tungsten işleme hattından sonra IV'te elde edilebilir)
- Dev türbinler uzun amerikyum çubuklarla üretilir (Füzyon Reaktörü Mk-II inşa ettikten sonra ZPM'de elde edilebilir <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## Dayanıklılık
Türbinler, üretilen güçle orantılı olarak yavaş yavaş dayanıklılık kaybeder. Bir türbinin toplam dayanıklılığı malzemeye bağlıdır ve %0 ulaştığında anında yok olur. Türbinler giriş yolu aracılığıyla kontrolcüye otomatik olarak yerleştirilebilir, ancak otomatik olarak çıkarılamaz.

Aşağıdaki denklem, bir <Color id="GREEN">XLST</Color>'nin mevcut güç çıkışından türbinlerin yaşam ömrünü (saat cinsinden) hesaplar. Gevşek oturma modunun, daha yüksek güç çıkışının azalttığı yaşam ömrünü telafi etmek için %25 dayanıklılık artışı sağladığını ve türbinlerin burada Büyük Buhar Türbini'ne kıyasla çok daha uzun dayandığını unutma. Türbinler genellikle birkaç yüz saatlik (veya daha fazla) yaşam ömrüne sahiptir, bu yüzden çok sık değiştirilmeleri gerekmez. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- Gevşek oturma modunda yaşam ömrü sonucunu 1.25 ile çarp.