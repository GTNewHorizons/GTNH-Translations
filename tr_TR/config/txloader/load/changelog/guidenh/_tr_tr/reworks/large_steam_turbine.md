---
item_ids:
  - gregtech:gt.blockmachines:15524
navigation:
  title: Büyük Buhar Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15524
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Buhar Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15524"/>
</GameScene>
<Color id="GREEN">Büyük Buhar Türbini (LST)</Color>, buhardan güç üretmek için kullanılan bir HV kademesi multibloktur. <Color id="GREEN">LST</Color>, çok daha yüksek verimle 4A'ya kadar güç çıkışı sağladığı için tek bloklu buhar türbinlerinin doğrudan yükseltmesidir. Ancak makinenin çalışması için kontrolcünün içine bir türbin yerleştirilmelidir, buhar giriş hızı dikkatle ayarlanmalıdır ve tam ısınma için en az 50 saniye çalışması gerekir. Türbinler dört farklı boyutta ve her biri kendi verim bonusuna ve optimal akış hızına (L/t) sahip birçok farklı malzemede bulunur. Güç, yapının arkasındaki 4A'lık dinamo kapağından alınır; buhar çıkış kapağında damıtılmış suya yoğuşur. Makine çalışırken dinamo kapağını kırmak patlamasına neden olur. Yakıttan tasarruf etmek için <Color id="GREEN">LST</Color>'yi bir Lapotronik Süperkapasitöre <ItemImage id="gregtech:gt.blockmachines:13106"/> bağlı RS mandalıyla otomatik olarak açıp kapat.

<Color id="RED">Büyük Yüksek Basınç Buhar Türbini (LST-HP)</Color> <ItemImage id="gregtech:gt.blockmachines:15525"/> ve <Color id="BLUE">Büyük Süperkritik Buhar Türbini (LST-SC)</Color> <ItemImage id="gregtech:gt.blockmachines:15526"/>, LST ile neredeyse aynıdır; tek fark, sırasıyla yalnızca kızgın buharı ve süperkritik buharı işlemeleridir. Süperkritik buhar, aynı optimal akış hızında normal buharın iki katı EU üretir ve kızgın buhara dönüşür. Kızgın buhar, aynı optimal akış hızında normal buharın iki katı EU üretir ve normal buhara dönüşür.

[GTNH Güç Planlayıcısı](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)

<Color id="GREEN">LST</Color>'nin yerini, 16 <Color id="GREEN">LST</Color> kadar buhar tüketen ve aynı gücü üreten ancak yalnızca 12 türbin gerektiren [XL Turbo Buhar Türbini](./xl_turbo_steam.md) alır. Ayrıca ciddi güç üretimi için <Color id="GREEN">Çok Amperli ve Lazer Enerji Kapakları</Color> desteği sunar ve yüksek basınç ile süperkritik varyantları olarak gelir. 
<br clear="all"/>

> [!NOTE]
> Yalnızca yapı değişti; mekanikler bunun dışında aynı kaldı

## İnşaat
<Color id="GREEN">LST</Color>'nin kademeli bileşeni yoktur. Bakım kapağı, girdi kapağı ve çıkış kapağı yapının arka yarısındaki herhangi bir türbin gövdesinin yerine geçebilir. Dinamo kapağı yalnızca yapının en arkasındaki orta kasaya konabilir ve 4A'dan büyük olamaz. Egzoz Çıkışı YOKTUR, bu yüzden bir tane ekleme. Kontrolcünün hemen önündeki 9 blok boş (hava) olmak zorundadır. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Büyük türbinlere özgü olan türbin muhafazası <ItemImage id="gregtech:gt.blockmachines:31025"/>, esasen yedek bir türbin depolayan bir ULV giriş yoludur ve kontrolcünün içindeki türbin kırıldığında onu otomatik olarak değiştirir. Tamamen isteğe bağlıdır ve UV'de açılır, ancak çalışma süresini en üst düzeye çıkarmaya yardımcı olur. 

### Gereksinimler:
- 1 Büyük Buhar Türbini (İlgili tipte) <ItemImage id="gregtech:gt.blockmachines:15524"/>
- 14 Çerçeve Kutusu (Türbin tipine göre) <ItemImage id="gregtech:gt.blockframes:32"/>
- 8-14 Türbin Gövdesi (Türbin tipine göre) <ItemImage id="gregtech:gt.blockframes:32"/>
- 12 Boru Muhafazası (Türbin tipine göre) <ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1 Dinamo Kapağı (arka orta türbin gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (arka türbin gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 0+ Girdi Kapağı (arka türbin gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (arka türbin gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">LST</Color>'ler kasa, çerçeve kutusu ve veriyolu/kapaklardan tasarruf etmek için her bir yüzlerini duvar paylaşımına açabilir. Ancak girdi kapağını PAYLAŞMA; çünkü yakıt <Color id="GREEN">LST</Color>'ler arasında eşit bölünmez -- biri her şeyi tüketir, diğeri hiçbir şey almaz. Kapak konumlarındaki kısıtlama zaten bunu yapmayı zorlaştırır. 

----------

## Kullanım
<Color id="GREEN">LST</Color>'nin aşağıda listelenen iki çalışma modu vardır; aralarındaki ölçülebilir farklar için yukarıda bağlantısı verilen planlayıcıya bak. İlki, buhar üretiminin düşük olduğu oyunun başından ortasına kadar daha iyidir; ikincisi ise güç çıkışının verimden daha önemli olduğu oyun sonunda daha iyidir. Kontrolcüye tornavida kullanarak modlar arasında geçiş yap.

- Sıkı Geçme Modu - Yüksek verim, Düşük optimal akış hızı (güç).
- Gevşek Geçme Modu - Düşük verim, Yüksek optimal akış hızı (güç).

<Color id="GREEN">LST</Color>'nin hızı çalışırken doğrusal olarak %100'e kadar artar ve çalışmadığında %0 seviyesine geri düşer. Hız, makinenin güç çıkışıyla doğru orantılıdır ve türbin boyutu/malzemesi ne olursa olsun maksimum değerine ulaşması 50 saniye sürer. <Color id="GREEN">LST</Color> devre dışı bırakıldığında, türbin çıkarıldığında, yapı kırıldığında veya yakıt tükendiğinde hız son derece hızlı düşer. Kontrolcüde Taşınabilir Tarayıcı <ItemImage id="gregtech:gt.metaitem.01:32762"/> kullanarak veya WAILA'daki "efficiency" değerine bakarak türbinin mevcut hızını görüntüle. 

## Optimal Akış Hızı
Buharın <Color id="GREEN">LST</Color>'ye giriş hızı (L/t) son derece önemlidir. Buhar çok az olursa potansiyel gücün yalnızca küçük bir kısmı üretilir; çok fazla olursa muazzam miktarda yakıt israf edilir. İdeal olarak buhar, <Color id="GREEN">LST</Color>'ye türbinin optimal akış hızında girer; bu değer boyut/malzeme ve makinenin çalışma moduna göre önemli ölçüde değişir. NEI'de görünse de, L/t cinsinden optimal akış hızı ($$\dot{m}^*$$ ) aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpan, boyut (size) 1=küçük ile 4=dev arasında bir sabit ve $$\eta_0$$ türbinin <u>temel</u> verimidir.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 50">
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\text{size}$$: Türbin boyutuna göre (1:4) aralığında sabit
</Latex>

<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 150 \times 1.1^{20(\eta_0 - 0.8)}">
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\text{size}$$: Türbin boyutuna göre (1:4) aralığında sabit
  - $$\eta_0$$: Türbinin Temel Verimi
</Latex>

Bazı türbinlerin optimal akış hızları inanılmaz derecede yüksektir; çünkü buharın yakıt yoğunluğu 0,5 EU/L gibi çok düşüktür, özellikle <Color id="GREEN">LST</Color> gevşek moddayken. Oyuncunun artan talebi karşılamak için sıvı regülatörünü yükseltmesi veya ikinci bir girdi kapağı eklemesi gerekebilir. Sonunda, pratikte aktarım sınırı olmayan ve sıcaklık ya da ısı kapasitesi endişesi taşımayan AE2 sıvı P2P tünellerine <ItemImage id="appliedenergistics2:item.ItemMultiPart:463"/> geçmek gerekli hale gelir.

## Güç ve Taşma
<Color id="GREEN">LST</Color>'nin ürettiği güç, mevcut akış hızına ($$\dot{m}$$), optimal akış hızına ($$\dot{m}^*$$) ve türbinin verimine ($$\eta$$) bağlıdır. Optimal akış hızını aşmak, türbinin taşma kademesine ($$T$$) bağlı olarak azalan getiriyle ek güç üretir. Toplamda yalnızca üç taşma kademesi vardır ve bunlar kesinlikle türbinin malzemesine bağlıdır. Daha yüksek taşma kademesi maksimum akış hızını ($$\dot{m}_{max}$$) da artırır. Bir türbinin taşma kademesini NEI'den, makinenin mevcut güç çıkışını WAILA'dan görüntüle.

Güç, yapının arkasındaki 4A'lık dinamo kapağından alınır. Makine çalışırken dinamo kapağını kırma, yoksa <Color id="GREEN">LST</Color> patlar. Maksimum EU/t'yi veya dinamonun tamponundaki toplam EU'yu aşmak tamamen güvenlidir; <Color id="GREEN">LST</Color>, bağlı bir pil tamponu veya Lapotronik Süperkapasitör (LSC) <ItemImage id="gregtech:gt.blockmachines:13106"/> doluysa ve EU'nun gidecek yeri yoksa patlamaz. Fazladan EU basitçe yok edilir. Yakıt israfını önlemek için <Color id="GREEN">LST</Color>'yi bir kızıltaş RS mandalıyla otomatik olarak açıp kapatman şiddetle önerilir.

### Büyük Buhar Türbini:
<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 0.5 \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (T+1)} \Biggr) \times 0.5 \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
  - $$T$$: Taşma Kademesi
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1)">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$T$$ Taşma Kademesi
</Latex>

### Büyük Yüksek Basınç Buhar Türbini:
<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (T+2)} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
  - $$T$$: Taşma Kademesi
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1.5)">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$T$$ Taşma Kademesi
</Latex>

### Büyük Süperkritik Buhar Türbini:
<Latex formula="\text{EU/t} = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1.5)">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$T$$ Taşma Kademesi
</Latex>

## Türbinler
Makinenin çalışması için kontrolcünün GUI'sine bir türbin yerleştirilmelidir. Türbinler dört farklı boyutta ve her biri kendi verim bonusuna ve optimal akış hızına sahip birçok farklı malzemede bulunur. Burada hepsini listelemek için çok fazla farklı kombinasyon var, ancak yukarıda bağlantısı verilen planlayıcı tüm ilgili bilgilere ve hatta herhangi bir türbinin herhangi bir yakıtla güç çıkışını ve yaşam ömrünü belirlemek için bir hesaplayıcıya sahiptir.

- Küçük türbinler uzun magnalyum çubuklarla üretilir (LV kadar erken erişilebilir)
- Normal türbinler uzun titanyum çubuklarla üretilir (aya seyahat ettikten sonra HV'nin sonunda erişilebilir <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- Büyük türbinler uzun tungsten çeliği çubuklarla üretilir (tungsten işleme hattından sonra IV'te erişilebilir)
- Dev türbinler uzun amerikyum çubuklarla üretilir (Füzyon Reaktörü Mk-II inşa ettikten sonra ZPM'de erişilebilir <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## Dayanıklılık
Türbinler üretilen güçle orantılı olarak yavaşça dayanıklılık kaybeder. Bir türbinin toplam dayanıklılığı malzemeye bağlıdır ve %0 seviyesine ulaştığında anında geçersiz olur. Türbinler kontrolcüye takılıp çıkarılamaz, ancak türbin muhafazaları yenisini takmak için her 60 saniyede bir kontrolcünün boş olup olmadığını kontrol eder. Gerekirse aralığı azaltmak için muhafazaya tornavida kullan ve <Color id="GREEN">LST</Color>'yi bir makine kontrolcüsü kapağıyla yeniden etkinleştir.

Aşağıdaki denklem, bir <Color id="GREEN">LST</Color>'nin mevcut güç çıkışından bir türbinin yaşam ömrünü (saat cinsinden) hesaplar. Gevşek geçme modunun, daha yüksek güç çıkışının azalan ömrünü telafi etmek için %25 dayanıklılık artışı sağladığını unutma. Türbinlerin yaşam ömrü genellikle birkaç yüz saat (veya daha fazla) olduğundan çok sık değiştirilmeleri gerekmez. 

<Latex formula="\text{Lifespan} (h) = \frac{\text{Durability}}{36 \times \text{min}(0.2 \times \text{EU/t}, (\text{EU/t})^{0.6})}"/>

- Gevşek geçme modunda yaşam ömrü sonucunu 1,25 ile çarp.