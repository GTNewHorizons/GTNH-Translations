---
item_ids:
  - gregtech:gt.blockmachines:236
  - gregtech:gt.blockmachines:237
  - gregtech:gt.blockcasings12:0
navigation:
  title: Kok Fırını
  parent: reworks.md
  icon: gregtech:gt.blockmachines:236
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# Kok Fırını
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:236"/>
</GameScene>
<Color id="GREEN">Kok Fırını</Color>, kütükleri odun kömürüne yakmak ve kömürü kok kömürüne rafine etmek için Taş kademesindeki bir multibloktur. İşlem kütük/kömür başına 90 saniye sürer ve yan ürün olarak kreozot yağı üretir. Kreozot yağı fırınlarda, Railcraft Kazanında, Büyük Kazanda ve daha fazlasında yakıt olarak kullanılabilir. Ayrıca meşaleleri çok verimli şekilde üretmek ve bir damıtıcıda, bira üreticisinde veya Damıtma Kulesinde yağlayıcı yapmak için de kullanılabilir. Kok Fırınının yerini MV'de Piroliz Fırını <ItemImage id="gregtech:gt.blockmachines:15543"/> ve Gelişmiş Kok Fırını <ItemImage id="Railcraft:machine.alpha:12"/> alır. 

<br clear="all"/>

> [!NOTE]
> Multibloğa (yapı dışında) şu değişiklikler yapıldı:
> Yeni Otomasyon: Kok fırını artık otomasyon için özel Kok Fırını Kapakları kullanıyor
> Duvar Paylaşımı: Artık GT multiblokları oldukları için duvarlarını paylaşabilirler!

## İnşa
<Color id="GREEN">Kok Fırını</Color>, kok fırını tuğlalarıyla çevrili içi boş bir küptür ve bir yanında bir kontrolcü bulunur. <Color id="GREEN">Kok Fırını</Color> ile kontrolcünün GUI'si üzerinden manuel olarak etkileşime gir veya girdileri ekleme ve çıktıları çıkarma işlemini otomatikleştirmek için <Color id="RED">Kok Fırını Kapaklarını</Color> <ItemImage id="gregtech:gt.blockmachines:237"/> kullan. <Color id="RED">Kok fırını kapağı/kapakları</Color> yapının herhangi bir yerindeki herhangi bir tuğlanın yerini alabilir ve mevcut üç moddan birinde çalışır: giriş, çıkış (eşyalar) ve çıkış (sıvılar). Modları değiştirmek için kapağa tornavidayla sağ tıkla ve kapağı döndürmek için ingiliz anahtarıyla sağ tıkla. Kok fırını kapağının kendi iç envanteri yoktur, bu yüzden kırıldığında eşya düşürmez veya sıvı yok etmez; bunu yalnızca kontrolcü yapar. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Üç kapaklı bir <Color id="GREEN">Kok Fırını</Color> inşa etmek 114 kok fırını tuğlası (külçe), 54 demir ve 18 bronz gerektirir. Tuğlalar 190 kum, 114 kil ve ahşap kalıbın 38 kullanımına mal olur. Ancak ek Kok Fırınları inşa etmek için oyunun başında bundan çok daha fazlasını toplaman şiddetle tavsiye edilir.

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:236"/><ItemImage id="gregtech:gt.blockmachines:236"/>
- 0-25 <ItemLink id="gregtech:gt.blockmachines:237"/><ItemImage id="gregtech:gt.blockmachines:237"/>
- 0+ <ItemLink id="gregtech:gt.blockcasings12"/><ItemImage id="gregtech:gt.blockcasings12"/>

### Duvar Paylaşımı
<FloatingImage src="../assets/reworks/coke_oven_wallshare.png" displayWidth="128" align="right">
  <ImageAnnotation>
    Dörtlü duvar paylaşımlı bir kok fırını örneği
  </ImageAnnotation>
</FloatingImage>
<Color id="GREEN">Kok Fırınları</Color>, kok fırını tuğlalarından ve kok fırını kapaklarından tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Bu, önemli miktarda kaynak tasarrufu sağladığı ve gereken kapak sayısını azalttığı için şiddetle tavsiye edilir. Örneğin sağdaki görsel, hepsi yapının merkezindeki aynı kok fırını kapağını kullanan dört ayrı kok fırınını gösterir. 

## Kullanım
<Color id="GREEN">Kok Fırını</Color> öncelikle kütükleri odun kömürüne yakmak için kullanılır, ancak aşağıdaki tabloda görüldüğü gibi birkaç başka niş kullanımı da vardır. Bonsai ağaçları, oyunun başında önemli miktarda kütük toplamanın mükemmel bir yoludur. Herhangi bir vanilya fidanıyla ekin çubuklarına sağ tıklayarak bonsai oluştur; ladin ve orman ağacı en iyileridir çünkü hasat başına daha fazla ürün verirler. Başka bir yöntem, bir Tinker's Construct Kereste Baltası üretip kutsal meşe ağaçlarını veya tek seferde binlerce kütük düşürebilen diğer devasa ağaçları tekrar tekrar hasat etmektir. Kutsal meşe ağaçları Sacred Springs biyomunda doğal olarak oluşur ve fidanları Görev Kitabında görev ödülü olarak kazanılabilir.

<Color id="GREEN">Kok Fırını</Color> ayrıca kömürü kok kömürüne rafine etmek için kullanılır. Fark, kok kömürünün iki kat yanma süresine sahip olması ve Tuğlalı Yüksek Fırında <ItemImage id="gregtech:gt.blockmachines:140"/> demiri %33 daha hızlı çeliğe eritebilmesidir. Kaktüs koksu ve şeker koksu çok benzer ve yenilenebilir alternatiflerdir, ancak enerji yoğunlukları kok kömürününkine yakın bile değildir. Mevcut tüm tariflerin özeti için aşağıdaki tabloya bak; bunlar NEI'de de görülebilir. 

| Süre | Girdi (Yanma Süresi) | Çıktı (Yanma Süresi) | Yan Ürün (Yanma Süresi) |
| --------------- | --------------- | --------------- | --------------- |
| 90 sn | 1 Kütük (300) | 1 Odun Kömürü (1.600) | 250 L Kreozot Yağı (1.600) |
| 90 sn | 1 Kömür (1.600) | 1 Kok Kömürü (3.200) | 500 L Kreozot Yağı (3.200) |
| 810 sn | Kömür Bloğu (16.000) | 1 Kok Kömürü Bloğu (32.000) | 4.500 L Kreozot Yağı (28.800) |
| 25 sn | 1 Kaktüs (50) | 1 Kaktüs Kömürü (400) | 30 L Kreozot Yağı (192) |
| 25 sn | 1 Kaktüs Kömürü (400) | 1 Kaktüs Koksu (800) | 30 L Kreozot Yağı (192) |
| 25 sn | 1 Şeker Kamışı (50) | 1 Şeker Kömürü (400) | 30 L Kreozot Yağı (192) |
| 25 sn | 1 Şeker Kömürü (400) | 1 Şeker Koksu (800) | 30 L Kreozot Yağı (192) |


## Kreozot Yağı
<Color id="GREEN">Kreozot Yağı</Color> neredeyse tüm Kok Fırını tariflerinin yan ürünüdür. Kreozot yağını kovalar, sıvı hücreleri, kavrulmuş tanklar ve süper tanklarla manuel olarak veya bir kok fırını kapağına bağlı sıvı borularıyla otomatik olarak çıkar. Kreozot yağını bir Railcraft Tankında, süper tankta veya başka herhangi bir sıvı tankında depola. Kreozot yağı vanilya fırınları, Railcraft Kazanı ve Büyük Kazan dahil olmak üzere çeşitli yerlerde yakıt olarak kullanılabilir. Ayrıca meşaleleri çok verimli şekilde üretmek ve bir damıtıcıda, bira üreticisinde veya Damıtma Kulesinde yağlayıcı yapmak için de kullanılabilir.

Kok Fırını, kreozot yağı veya odun kömürü/kok için yer kalmadığında işlemi otomatik olarak durdurur. Bu nedenle çalışmaya devam etmesi için belirli aralıklarla boşaltılması gerekir. Bu manuel veya otomatik olarak yapılabilir; otomatik yöntem için sonraki bölüme bak. Kreozot yağı, kontrolcüyü kırıp yeniden yerleştirerek de hemen yok edilebilir. 

# Otomasyon
Kok Fırını, aşağıdaki videoda görüldüğü gibi kok fırını kapaklarıyla tamamen otomatikleştirilebilir. Kok fırını kapakları bitişik envanterlerden otomatik çekim yapamaz ancak otomatik itme yapabilir; bu da gerçekte gereken tek şeyin bir huni veya konveyör modülü olduğu anlamına gelir. İkincisini kullanıyorsan konveyör modülünü IMPORT olarak ayarla çünkü muhtemelen envanterin kendisine değil eşya borusuna bağlıdır. 

<GameScene width="420" height="280" zoom={3} interactive={true}>
  <ImportStructure src="../assets/reworks/coke_oven.snbt" />
  <ImportPonder src="../assets/reworks/coke_oven.json"/>
</GameScene>