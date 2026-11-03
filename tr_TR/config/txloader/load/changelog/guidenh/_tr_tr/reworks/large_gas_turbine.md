---
item_ids:
  - gregtech:gt.blockmachines:15527
navigation:
  title: Büyük Gaz Türbini
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15527
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Büyük Gaz Türbini

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15527"/>
</GameScene>
<Color id="GREEN">Büyük Gaz Türbini (LGT)</Color>, gazdan güç üretmek için kullanılan EV kademe bir Multibloktur. <Color id="GREEN">Büyük Gaz Türbini</Color>, çok daha yüksek verimlilikle 4A'ya kadar güç verdiği için tek bloklu gaz Türbinlerinin doğrudan yükseltmesidir. Ancak makinenin çalışması için Kontrolcünün içine bir Türbin yerleştirilmelidir, Yakıt giriş hızı dikkatlice ayarlanmalıdır ve tamamen ısınması için en az 50 saniye çalışması gerekir. Türbinler dört farklı boyutta ve her biri kendi verimlilik bonusuna ve optimal akış hızına (L/t) sahip birçok farklı malzemede bulunur. Gaz Kirlilik haline gelirken güç, yapının arkasındaki 4A Dinamo Kapağından çekilir. Makine çalışırken Dinamo Kapağını kırmak patlamasına neden olur. Lapotronik Süperkapasitöre <ItemImage id="gregtech:gt.blockmachines:13106"/> bağlı bir RS mandalı ile LGT'yi otomatik açıp kapatarak Yakıttan tasarruf et.

<Color id="GREEN">LGT</Color>'nin yerini, 16 <Color id="GREEN">LGT</Color> kadar gaz tüketip o kadar güç üreten ancak yalnızca 12 Türbin gerektiren XL Turbo Gaz Türbini alır. Ayrıca ciddi güç üretimi için çok amperli ve lazer Enerji Kapaklarını da destekler. Türbin olmadan ve Çevreyi kirletmeden elektrik üretmek için gazı oksitleyen Katı Oksitli Yakıt Hücresi de vardır. Ancak çalışırken 100 L/s oksijen gerektirir, genellikle yüzde 100 verimliliğe sabitlenmiştir, taşmayı desteklemez ve XL varyantı yoktur. 

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> Yalnızca yapı değişti, Multiblokun mekaniği birebir aynı

## Yapım
<Color id="GREEN">LGT</Color>'nin kademeli bileşenleri yoktur. Bakım Kapağı, Egzoz Çıkışı, Girdi Kapağı ve Çıkış Kapağı yapının arka yarısındaki herhangi bir Türbin Gövdesinin yerini alabilir. Dinamo Kapağı yapının en arkasındaki merkez kasayla sınırlıdır ve 4A'dan büyük olamaz. Kontrolcünün hemen önündeki 9 blok Hava Blokları olmak zorundadır. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Büyük Türbinlere özgü olan Türbin muhafazası, esasen Kontrolcünün içindeki Türbin kırıldığında otomatik olarak onun yerini alacak fazladan bir Türbin depolamaya yarayan bir ULV Giriş Yolu'dur. Tamamen isteğe bağlıdır ve UV'ye kilitlidir, ancak çalışma süresini en üst düzeye çıkarmaya yardımcı olur. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:15527"/><ItemImage id="gregtech:gt.blockmachines:15527"/>
- 14 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8-13 <ItemLink id="gregtech:gt.blockcasings4:10"/><ItemImage id="gregtech:gt.blockcasings4:10"/>
- 12 <ItemLink id="gregtech:gt.blockcasings11"/><ItemImage id="gregtech:gt.blockcasings11"/>
- 1 Dinamo Kapağı (arka orta Türbin Gövdesi) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 Bakım Kapağı (arka Türbin Gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 0+ Girdi Kapağı (arka Türbin Gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ Çıkış Kapağı (arka Türbin Gövdelerinden herhangi biri) <ItemImage id="gregtech:gt.blockmachines:60" />

### Duvar Paylaşımı
<Color id="GREEN">LGT</Color>'ler kasa, çerçeve kutusu ve kapaktan tasarruf etmek için her bir yanını duvar paylaşabilir. Ancak Girdi Kapağını paylaşMA çünkü Yakıt <Color id="GREEN">LGT</Color>'ler arasında eşit olarak bölünmez -- biri her şeyi tüketir, diğeri hiçbir şey almaz. Kapak konumlarındaki kısıtlama zaten bunu başarmayı zorlaştırır. 

## Kullanım
<Color id="GREEN">LGT</Color>'nin aşağıda listelenen iki çalışma modu vardır, ancak aralarındaki ölçülebilir farklar için yukarıda bağlantısı verilen planlayıcıya bak. Gaz üretiminin düşük olduğu oyunun erken-orta döneminde ilki, güç çıktısının verimlilikten daha önemli olduğu geç oyunda ise ikincisi daha iyidir. Kontrolcüye tornavida kullanarak modlar arasında geçiş yap.

- Sıkı Geçme Modu - Yüksek verimlilik, Düşük optimal akış hızı (güç).
- Gevşek Geçme Modu - Düşük verimlilik, Yüksek optimal akış hızı (güç).

<Color id="GREEN">LGT</Color>'nin hızı çalışırken doğrusal olarak yüzde 100 değerine kadar artar ve çalışmadığında tekrar yüzde 0 değerine düşer. Hız, makinenin güç çıktısıyla doğru orantılıdır ve Türbinin boyutu/malzemesi ne olursa olsun maksimum değerine ulaşması 50 saniye sürer. Hız, <Color id="GREEN">LGT</Color> devre dışı bırakıldığında, Türbin çıkarıldığında, yapı bozulduğunda veya Yakıt bittiğinde son derece hızlı düşer. Türbinin mevcut hızını, Kontrolcüde Taşınabilir Tarayıcı <ItemImage id="gregtech:gt.metaitem.01:32762"/> kullanarak veya WAILA'daki "verimlilik" değerine bakarak görebilirsin. 

## Optimal Akış Hızı
Gazın <Color id="GREEN">LGT</Color>'ye girdiği hız (L/t) son derece önemlidir. Çok az gaz olursa potansiyel gücün yalnızca bir kısmı üretilir; çok fazla gaz olursa muazzam miktarda Yakıt boşa harcanır. İdeal olarak gaz, <Color id="GREEN">LGT</Color>'ye Türbinin optimal akış hızında girer; bu hız boyut/malzeme ve makinenin çalışma moduna göre önemli ölçüde değişir. NEI'de görünse de, L/t cinsinden optimal akış hızı ($$\dot{m}$$) aşağıdaki denklemlerle hesaplanır; burada $$k$$ her malzemeyle ilişkili bir çarpandır, size 1=küçük ile 4=devasa arasında bir sabittir, EU/L gazın yoğunluğudur ve $$\eta_0$$ Türbinin temel verimliliğidir. 

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 50 \div EU/L">
  Burada:
  - $$\dot{m}^* =$$ Optimal Akış Hızı
  - $$k =$$ Malzeme Çarpanı
  - size = Türbin boyutu (1=küçük, 4=devasa)
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 100 \div EU/L \times 1.05^{20(\eta_0 - 0.8)}">
  Burada:
  - $$\dot{m}^* =$$ Optimal Akış Hızı
  - $$k =$$ Malzeme Çarpanı
  - size = Türbin boyutu (1=küçük, 4=devasa)
  - $$\eta_0 =$$ Temel Verimlilik
</Latex>

Sıkı geçme modunda optimal akış hızını hesaplamanın daha hızlı ve kolay yolu, optimal gaz EU/t değerini (NEI'de görünür) gazın yoğunluğuna bölmek ve ardından sonucu 2'ye bölmektir. Bazıları çok düşük yoğunluğa ve dolayısıyla çok yüksek optimal akış hızına sahiptir--özellikle <Color id="GREEN">LGT</Color> gevşek moddaysa. Oyuncunun artan talebi karşılamak için sıvı regülatörünü yükseltmesi veya ikinci bir Girdi Kapağı eklemesi gerekebilir. Sonunda, etkin olarak aktarım sınırı olmayan ve Sıcaklık veya ısı kapasitesini hesaba katmayan AE2 sıvı P2P tünellerine geçmek gerekli hale gelir. 

## Güç ve Taşma
<Color id="GREEN">LGT</Color> tarafından üretilen güç, mevcut akış hızına ($$\dot{m}$$), optimal akış hızına ($$\dot{m}^*$$) ve Türbinin verimliliğine ($$\eta$$) bağlıdır. Optimal akış hızını aşmak, Türbinin taşma kademesine ($$T$$) bağlı olarak azalan getiriyle ek güç üretir. Toplamda yalnızca üç taşma kademesi vardır ve bunlar kesinlikle Türbinin malzemesine bağlıdır. Daha yüksek bir taşma kademesi maksimum akış hızını ($$\dot{m}_{max}$$) da artırır. Bir Türbinin taşma kademesini NEI'den, makinenin mevcut güç çıktısını ise WAILA'dan gör.

Güç, yapının arkasındaki 4A Dinamo Kapağından çekilir. Makine çalışırken Dinamo Kapağını kırma, yoksa <Color id="GREEN">LGT</Color> patlar. Maksimum EU/t'yi veya Dinamonun Tamponundaki toplam EU'yu aşmak tamamen güvenlidir; bağlı bir Pil Tamponu veya Lapotronik Süperkapasitör (LSC) doluysa ve EU'nun gidecek başka yeri yoksa <Color id="GREEN">LGT</Color> patlamaz. Fazladan EU basitçe yok edilir. Yakıt israfını önlemek için <Color id="GREEN">LGT</Color>'yi bir kızıltaş RS mandalı ile otomatik olarak açıp kapatman şiddetle önerilir.


<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times EU/L \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verimlilik
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (3T-1)} \Biggr) \times EU/L \times \eta">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}^*$$: Optimal Akış Hızı
  - $$\eta$$: Verimlilik
  - $$T$$: Taşma Kademesi
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (1.5T)">
  - $$\dot{m}$$: Mevcut Akış Hızı
  - $$\dot{m}_{max}$$: Maksimum Akış Hızı
  - $$T$$ Taşma Kademesi
</Latex>