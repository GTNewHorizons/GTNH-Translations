---
item_ids:
  - gregtech:gt.blockmachines:15528
navigation:
  title: Büyük Plazma Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15528
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Plazma Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15528"/>
</GameScene>
<Color id="GREEN">Büyük Plazma Türbini (LPT)</Color>, plazmadan güç üretmek için kullanılan LuV kademesi bir multibloktur. <Color id="GREEN">LPT</Color>, tek blok plazma jeneratörlerine göre doğrudan bir yükseltmedir; çünkü çok daha yüksek verimle 4A'ya kadar güç çıkışı verir. Ancak makinenin çalışması için kontrolcünün içine bir türbin yerleştirilmeli, plazmanın giriş hızı dikkatle ayarlanmalı ve tam ısınma için en az 50 saniye çalışması gerekir. Türbinler dört farklı boyutta ve her biri kendi verim bonusuna ve optimal akış hızına (L/s) sahip birçok farklı malzemeden gelir. Plazma sıvıya yoğuşurken güç, yapının arkasındaki 4A'lık dinamo kapağından çekilir. Makine çalışırken dinamo kapağını kırarsan makine patlar. <Color id="GREEN">LPT</Color>'yi bir Lapotronik Süperkapasitöre <ItemImage id="gregtech:gt.blockmachines:13106"/> bağlı Kızıltaş RS mandalıyla otomatik olarak açıp kapatarak yakıttan tasarruf et.

<Color id="GREEN">LPT</Color>'nin yerini, XL Turbo Plazma Türbini <ItemImage id="gregtech:gt.blockmachines:15523"/> alır; 16 <Color id="GREEN">LPT</Color> kadar plazma tüketip aynı gücü üretir, ancak yalnızca 12 türbin gerektirir. Ciddi güç üretimi için çok amperli ve lazer enerji kapaklarını da destekler. 

[GTNH Güç Planlayıcısı](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Yalnızca yapının kendisi değişti; multiblokun temel işlevselliği öncekiyle aynı

## Yapım
<Color id="GREEN">LPT</Color>'nin kademeli bileşenleri yoktur. Bakım kapağı, Girdi Kapağı ve Çıkış Kapağı, yapının arka yarısındaki herhangi bir Türbin Gövdesi'nin yerini alabilir. Dinamo kapağı yalnızca yapının en arkasındaki orta kasaya konabilir ve 4A'dan büyük olamaz. Egzoz Çıkışı YOKTUR, bu yüzden bir tane ekleme. Kontrolcünün hemen önündeki 9 blok zorunlu olarak havadır. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Büyük türbinlere özgü olan türbin muhafazası <ItemImage id="gregtech:gt.blockmachines:31025"/>, fazladan bir türbin depolamak için kullanılan ve adeta bir ULV Giriş Yolu gibi çalışan bir parçadır; kontrolcünün içindeki türbin kırıldığında onu otomatik olarak değiştirir. Tamamen isteğe bağlıdır ve UV kademesine kilitlidir, ancak çalışma süresini en üst düzeye çıkarmaya yardımcı olur. 

### Gerekli:
- 1 <ItemLink id="gregtech:gt.blockmachines:15528"/><ItemImage id="gregtech:gt.blockmachines:15528"/>
- 14 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 8-14 <ItemLink id="gregtech:gt.blockcasings4:12"/><ItemImage id="gregtech:gt.blockcasings4:12"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 1 Dinamo Kapağı (arka orta Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (herhangi bir arka Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 0+ Girdi Kapağı (herhangi bir arka Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (herhangi bir arka Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">LPT</Color>'ler alandan, Türbin Gövdesi'nden ve kapaktan tasarruf etmek için her bir yüzlerini duvar paylaşımıyla kullanabilir. Ancak Girdi Kapağı'nı PAYLAŞMA, çünkü yakıt <Color id="GREEN">LPT</Color>'ler arasında eşit olarak bölünmez; biri her şeyi tüketir, diğeri hiçbir şey almaz. Kapak konumlarındaki kısıtlama zaten bunu yapmayı zorlaştırır. 

## Kullanım
<Color id="GREEN">LPT</Color>'nin aşağıda listelenen iki çalışma modu vardır; aralarındaki ölçülebilir farklar için yukarıda bağlantısı verilen planlayıcıya bak. Plazma üretiminin düşük olduğu oyunun başı ve ortasında ilki, güç çıkışının verimden daha önemli olduğu oyunun sonlarında ise ikincisi daha iyidir. Modlar arasında kontrolcüye tornavida kullanarak geçiş yap.

- Sıkı Geçme Modu - Yüksek verim, düşük optimal akış hızı (güç).
- Gevşek Geçme Modu - Düşük verim, yüksek optimal akış hızı (güç).

<Color id="GREEN">LPT</Color>'nin hızı çalışırken doğrusal olarak yüzde 100'e kadar yükselir, çalışmadığında ise yüzde 0'a geri düşer. Hız, makinenin güç çıkışıyla doğru orantılıdır ve türbin boyutu/malzemesi ne olursa olsun maksimum değerine ulaşması 50 saniye sürer. <Color id="GREEN">LPT</Color> devre dışı bırakıldığında, türbin çıkarıldığında, yapı kırıldığında veya yakıt tükendiğinde hız son derece hızlı düşer. Kontrolcüye Taşınabilir Tarayıcı kullanarak ya da WAILA'daki "efficiency" değerine bakarak türbinin mevcut hızını görüntüle. 

## Optimal Akış Hızı
Plazmanın <Color id="GREEN">LPT</Color>'ye girdiği hız (L/s) son derece önemlidir. Çok az plazma olursa potansiyel gücün yalnızca bir kısmı üretilir; çok fazla plazma olursa muazzam miktarda yakıt boşa gider. İdeal olarak plazma, <Color id="GREEN">LPT</Color>'ye türbinin optimal akış hızında girer; bu hız boyut/malzemeye ve makinenin çalışma moduna göre önemli ölçüde değişir. NEI'de görünse de optimal akış hızı ($$\dot{m}^*$$) L/s cinsinden aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpan, size 1=küçük ile 4=dev arasında bir sabit ve $$\eta_0$$ türbinin temel verimidir.

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 1,000 \div EU/L">
  Burada:
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 2,000 \div EU/L \times 1.03^{20(\eta_0 - 0.8)}">
  Burada:
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$k$$: Malzeme Çarpanı
  - $$\eta_0$$: Temel Verim
</Latex>

Sıkı geçme modunda optimal akış hızını hesaplamanın daha hızlı ve kolay yolu, optimal plazma EU/t değerini (NEI'de görünür) plazmanın yoğunluğuna bölmek ve sonucu 40/3 ile çarpmaktır. Bazı plazmaların yoğunluğu biraz daha düşüktür ve dolayısıyla optimal akış hızları daha yüksektir; özellikle <Color id="GREEN">LPT</Color> gevşek moddaysa. Oyuncunun artan talebi karşılamak için sıvı Regülatörünü yükseltmesi veya ikinci bir Girdi Kapağı eklemesi gerekebilir. Sonunda, etkin biçimde aktarım sınırı olmayan ve sıcaklık ya da ısı kapasitesini dikkate almayan AE2 sıvı P2P tünellerine geçmek gerekli hale gelir. 

## Güç ve Taşma
<Color id="GREEN">LPT</Color>'nin ürettiği güç, mevcut akış hızına ($$\dot{m}$$), optimal akış hızına ($$\dot{m}^*$$) ve türbinin verimine ($$\eta$$) bağlıdır. Optimal akış hızının aşılması, türbinin taşma kademesine ($$T$$) bağlı olarak azalan getiriyle ek güç üretir. Toplamda yalnızca üç taşma kademesi vardır ve bu tamamen türbinin malzemesine bağlıdır. Daha yüksek taşma kademesi maksimum akış hızını ($$\dot{m}_{max}$$) da artırır. Türbinin taşma değerini NEI'den, makinenin mevcut güç çıkışını WAILA'dan görüntüle.

Güç, yapının arkasındaki 4A'lık bir dinamo kapağından çekilir. Makine çalışırken dinamo kapağını kırma, yoksa <Color id="GREEN">LPT</Color> patlar. Maksimum EU/t değerinin veya dinamonun tamponundaki toplam EU'nun aşılması tamamen güvenlidir; bağlı bir Pil tamponu ya da Lapotronik Süperkapasitör (LSC) doluysa ve EU'nun gidecek yeri yoksa <Color id="GREEN">LPT</Color> patlamaz. Fazladan EU yalnızca yok edilir. Yakıt israfını önlemek için <Color id="GREEN">LPT</Color>'yi Kızıltaş RS mandalıyla otomatik olarak açıp kapatman şiddetle önerilir.

<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times EU/L \times \eta \div 20">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (3T+1)} \Biggr) \times EU/L \times \eta \div 20">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verim
  - $$T$$: Taşma Kademesi
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (1.5T + 1)">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$T$$ Taşma Kademesi
</Latex>

# Türbinler
Makinenin çalışması için kontrolcünün GUI'sine bir türbin yerleştirilmelidir. Türbinler dört farklı boyutta ve her biri kendi verim bonusuna ve optimal akış hızına sahip birçok farklı malzemeden gelir. Burada hepsini listelemek için çok fazla farklı kombinasyon var; ancak yukarıda bağlantısı verilen planlayıcıda tüm ilgili bilgiler ve hatta herhangi bir türbinin herhangi bir yakıtla güç çıkışını ve Yaşam ömrünü belirlemeye yarayan bir hesaplayıcı var.

- Küçük türbinler uzun magnalyum çubuklarla üretilir (LV kadar erken kullanılabilir)
- Normal türbinler uzun titanyum çubuklarla üretilir (aya gittikten sonra HV'nin sonunda kullanılabilir <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- Büyük türbinler uzun tungsten çeliği çubuklarla üretilir (tungsten işleme hattından sonra IV'te kullanılabilir)
- Dev türbinler uzun Amerikyum çubuklarla üretilir (Füzyon Reaktörü Mk-II inşa ettikten sonra ZPM'de kullanılabilir <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## Dayanıklılık
Türbinler üretilen güce orantılı olarak yavaşça dayanıklılık kaybeder. Bir türbinin toplam dayanıklılığı malzemesine bağlıdır ve yüzde 0'a ulaştığında anında yok olur. Türbinler Giriş Yolu aracılığıyla kontrolcüye otomatik olarak yerleştirilebilir, ancak otomatik olarak çıkarılamaz.

Aşağıdaki denklem, bir <Color id="GREEN">LPT</Color>'nin mevcut güç çıkışından türbinlerin Yaşam ömrünü (saat cinsinden) hesaplar. Gevşek geçme modunun, daha yüksek güç çıkışının kısalttığı Yaşam ömrünü telafi etmek için %25 dayanıklılık artışı sağladığını ve türbinlerin burada Büyük Buhar Türbinine göre çok daha uzun dayandığını unutma. Türbinler genellikle birkaç yüz saatlik (veya daha fazla) Yaşam ömrüne sahiptir, bu yüzden çok sık değiştirilmeleri gerekmez. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(36 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>
