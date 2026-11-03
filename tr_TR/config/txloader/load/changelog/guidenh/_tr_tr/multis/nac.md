---
item_ids:
  - gregtech:gt.blockmachines:9500
navigation:
  title: Nanoçip Montaj Kompleksi
  parent: multis.md
  icon: gregtech:gt.blockmachines:9500
categories:
    - Yeni Multibloklar
author: Skorched
date: 2026-05-26
---

# Nanoçip Montaj Kompleksi
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9500" />
</GameScene>
<Color id="GREEN">Nanoçip Montaj Kompleksi (NAC)</Color>, seri devre montajı için UEV kademe bir multobloktur. <Color id="GREEN">NAC</Color>, kristal, nöro, biyo, optik, piko ve kuantum devreler için <ItemLink id="gregtech:gt.blockmachines:12735"/> <ItemImage id="gregtech:gt.blockmachines:12735"/> makinesinin doğrudan yükseltmesidir; çünkü <Color id="RED">sınırsız paralel işlem</Color> sunar, <Color id="BLUE">2/2 kusursuz hız aşırtma</Color> çalıştırır ve bir tarifin tüm süresi boyunca yeterli enerji yoksa işleme başlamaz. <Color id="GREEN">NAC</Color> ayrıca inanılmaz yüksek iş hacmi için <Color id="RED">Çok Amperli ve Lazer Enerji Kapaklarını</Color> destekler.

Tüm işleme ve devre montajı, yapının merkezindeki kontrol odasını çevreleyen modüller tarafından yapılır. Aralarından seçim yapabileceğin 11 farklı modül ve 12 modül yuvası vardır. Birkaç modülün kendine özgü zorlukları veya maliyetleri vardır, ancak çoğu oldukça basittir. Eşyalar ve devre bileşenleri (CC'ler), sınırsız depolama kapasitesi ve iş hacmine sahip vakum konveyör kapakları ve vakum konveyör borularıyla modüller arasında yönlendirilir. Aynı devre türünden yeterince üretmek, <Color id="GREEN">NAC</Color>'yi o belirli devre hattına kalibre eder ve ek bonuslar verir. 
<br clear="all"/>

## İnşaat:
<Color id="GREEN">NAC</Color>, 12 modül yuvasıyla çevrili büyük bir kontrol odasından oluşur. Kontrol odası makinenin hem girişleri hem de çıkışları içindir; modüller ise devre bileşenlerini (CC'ler) işlemek içindir. Çok amperli ve lazer enerji kapakları desteklenir, ancak yalnızca bir tane olabilir ve kontrol odasının içinde veya altında olmalıdır. Güç, kontrol odasından tüm modüllere talep edilme sırasına göre otomatik olarak dağıtılır; <ItemLink id="gregtech:gt.blockmachines:14003"/><ItemImage id="gregtech:gt.blockmachines:14003"/> makinesine benzer. Tek istisna <ItemLink id="gregtech:gt.blockmachines:9504"/><ItemImage id="gregtech:gt.blockmachines:9504"/> modülüdür; bu modül enerji tamponunu doldurmada diğer tüm modüllerden daha düşük önceliğe sahiptir. Bakım kapağı yoktur. Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/> kullan.

Modüller, kendi kontrolcüleri ve inşaat gereksinimleri olan kendi multibloklarıdır. Herhangi bir modül yuvasının üst kenarındaki <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/> bloklarından birini değiştir ve onları görselleştirmek/inşa etmek için Multiblok Yapı Hologram Projektörünü kullan. Her yöne bakabilirler, ancak baş aşağı inşa edilemezler. Doğru yapıldıysa, <Color id="GREEN">NAC</Color> etkinleştirildiğinde modülün kontrolcüsü "Ana Komplekse Bağlı" yazmalıdır. 
### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9500"/><ItemImage id="gregtech:gt.blockmachines:9500"/>
- 3.956 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 2.226 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 1.708-1.720 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 721 <ItemLink id="gregtech:gt.blockcasings12:3"/><ItemImage id="gregtech:gt.blockcasings12:3"/>
- 53 <ItemLink id="gregtech:gt.blockframes:324"/><ItemImage id="gregtech:gt.blockframes:324"/>
- 32 <ItemLink id="gregtech:gt.blockcasings12:4"/><ItemImage id="gregtech:gt.blockcasings12:4"/>
- 1 Enerji Kapağı (kontrol odasında herhangi bir yan arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:15065"/>
- 0+ Giriş Yolu (kontrol odasında herhangi bir yan arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ Çıkış Yolu (kontrol odasında herhangi bir yan arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:80"/>

## Vakum Konveyör Sistemi
<Color id="GREEN">NAC</Color>'ye özgü olan, modüller arasında eşya veya CC taşıyan <ItemLink id="gregtech:gt.blockmachines:9501"/> (VCI) <ItemImage id="gregtech:gt.blockmachines:9501"/> ve <ItemLink id="gregtech:gt.blockmachines:9502"/> (VCO) <ItemImage id="gregtech:gt.blockmachines:9502"/> kapakları vardır. Bunlar, çalışmak için renklendirilmeleri ve bağlantıların 1'e 1 olması gerektiğinden optik iletim ve alım kapaklarına benzer. Kapaklar makineye özeldir, bu yüzden <Color id="GREEN">NAC</Color>'ler arasında CC aktaramazlar. Kapakları birleştiren vakum konveyör boruları da renklendirilmelidir ve serbestçe bükülebilir. Her şeyi renklendirmek için <ItemLink id="gregtech:gt.metaitem.01:32468"/><ItemImage id="gregtech:gt.metaitem.01:32468"/> kullanman şiddetle tavsiye edilir.

Her iki kapak da aynı anda 16 farklı eşya yığını tutabilir; kapasitede üst sınır ve bağlantılar arasında transfer sınırı yoktur. Bu, oyun sonuna kolayca ölçeklenen inanılmaz yüksek bir iş hacmi sağlar. Kapakların içinde depolanan eşyalarla doğrudan etkileşime girilemez, ancak depolanan eşyaları bir AE2 depolama hücresine boşaltma/paketten çıkarma veya tüm depolanan eşyaları silme seçeneği vardır. Sıvılar vakum konveyör sistemine girmez ve doğrudan onları kullanan modüle/modüllere yönlendirilmelidir.

Eşyaların doğru modüle yönlendirildiğinden emin olmak için düzgün filtreleme veya ayırma yapmanın iki yolu vardır. Birincisi her şeyi NAC'ye girmeden önce filtrelemek, ikincisi <ItemLink id="gregtech:gt.blockmachines:9510"/><ItemImage id="gregtech:gt.blockmachines:9510"/> modülünü kullanmaktır. İkincisi bir modül yuvası kullanır ancak giriş rengi, çıkış rengi, eşya türü ve/veya verilen kızıltaş seviyesine göre özel yönlendirmeye izin verir. 

----------

## Modüller:
<Color id="GREEN">NAC</Color>, devre bileşenlerini (CC'ler) yalnızca sabit 5 saniyelik bir döngüde paketler ve paketten çıkarır. Devreleri gerçekte işleyen ve monte eden şey modüllerdir. Kontrol odasının çevresinde aralarından seçim yapabileceğin 11 farklı modül ve 12 modül yuvası vardır, ancak tüm modüller gerekli değildir ve her birinin sayısında bir sınır yoktur. Ek işlemeye rağmen modüller, Devre Montaj Hattı'na göre doğrudan bir yükseltmedir; çünkü sınırsız paralel işleme sahiptirler, tarif kademesinin üzerindeki her voltaj kademesi için 5 saniyeye kadar 2/2 kusursuz hız aşırtma çalıştırırlar ve enerji tamponları üretim için yeterince büyük değilse işleme başlamazlar. Bu, inanılmaz yüksek bir iş hacmine sahip oldukları ve enerji kesintisi yaşayamayacakları veya eşya yok edemeyecekleri anlamına gelir. Hız aşırtmaların, daha uzun tariflerin hızını artırmak için paralel işlemlerden önce hesaplandığını unutma.

<Color id="GREEN">NAC</Color>'nin genel iş akışı aşağıda listelenmiştir. Görsel de referans olarak verilmiştir, ancak her şey (örneğin eklenmiş çerçeveler) Nanoçip Montaj Matrisine yönlendirilmediği için hafif bir basitleştirmedir. Daha ayrıntılı kurulum adımları için aşağıdaki kalibrasyon bölümüne bak. 
1. Eşyaları kontrol odasındaki <u>renkli</u> bir giriş yolundan (normal veya stoklu) yerleştir
2. <Color id="GREEN">NAC</Color> eşyaları CC olarak paketler ve aynı renkteki bir VCO kapağına aktarır
3. Önceden yapılmadıysa, paketlenmiş CC'leri doğru modüle yönlendirmek için bir Nanoparçacık Ayırıcı modülüyle filtrele.
4. Modüller paketlenmiş CC'leri, paketten çıkarılamayan veya <Color id="GREEN">NAC</Color>'den ayrılamayan işlenmiş bileşenlere (PC'ler) dönüştürür
5. Devre CC'leri oluşturmak için PC'leri Nanoçip Montaj Matrisinde birleştir ve kontrol odasına geri yönlendir
6. <Color id="GREEN">NAC</Color> devre CC'lerini paketten çıkarır ve alınmaları için bir çıkış yoluna aktarır
<FloatingImage src="../assets/multis/nac_overview.png" displayWidth="384">
  <ImageAnnotation>
    Fox tarafından hazırlanan Nanoçip Montaj Kompleksi genel görünümü
  </ImageAnnotation>
</FloatingImage>
<br clear="all"/>

## Nanoçip Montaj Matrisi <ItemImage id="gregtech:gt.blockmachines:9504"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9504" />
</GameScene>
<Color id="GREEN">Nanoçip Montaj Matrisi</Color>, işlenmiş bileşenlerden (PC'ler) devre CC'leri monte eder. Bu modül, devre CC'lerinin gerçek devrelere dönüştürülmek üzere paketten çıkarılacağı kontrol odasına gönderilmesinden önceki her zaman son adımdır. <Color id="GREEN">Nanoçip Montaj Matrisi</Color>, enerji tamponunu doldurmada tüm modüller arasında en düşük önceliğe sahiptir ve 5 saniyeye kadar 2/2 kusursuz hız aşırtma, tarif voltaj kademesi yerine tarif kasa kademesine dayanır. İkisi de NEI'de gösterilir ve genellikle birbirinden farklıdır.
<br clear="all"/>
<Latex formula="\text{Max Overclocks} = \text{Energy Hatch Tier} - \text{Recipe Casing Tier}"/>

<Color id="GREEN">Nanoçip Montaj Matrisi</Color> girişleri ayrı VCI'lerde olabilir ve hepsinin aynı renkte olması gerekmez. Tarifler Montaj Hattı tariflerine benzese de bileşenlerin sıralamasında da bir kısıtlama yoktur. Çıkış rengi, genellikle devre kartı veya kaplama PC'si olan ilk bileşene dayanır. 

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9504"/><ItemImage id="gregtech:gt.blockmachines:9504"/>
- 25 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 24 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 20 Bileşen Montaj Hattı Kasası (Kademeli) <ItemImage id="GoodGenerator:componentAssemblylineCasing"/>
- 12 <ItemLink id="gregtech:gt.blockframes:325"/><ItemImage id="gregtech:gt.blockframes:325"/>
- 8 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 3 <ItemLink id="gregtech:gt.sheetmetal:325"/><ItemImage id="gregtech:gt.sheetmetal:325"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>


| Devre Hattı   | Kasa Kademesi    |
|--------------- | --------------- |
| Kristal | LuV |
| Nöro | ZPM |
| Biyo | UV  |
| Optik | UHV |
| Piko | UEV   |
| Kuantum | UIV |
| Planck  | UMV |


## Nanoparçacık Ayırıcı <ItemImage id="gregtech:gt.blockmachines:9510"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9510" />
</GameScene>
<Color id="GREEN">Nanoparçacık Ayırıcı</Color> tüm CC'leri filtreler ve düzenler. Giriş rengi, çıkış rengi, eşya türü ve/veya verilen kızıltaş seviyesine göre özel yönlendirme kuralları belirlemek için kontrolcünün GUI'si üzerinden kural yöneticisini aç. En azından bir veya daha fazla giriş rengi ve bir veya daha fazla çıkış rengi seçili olmalıdır. <Color id="GREEN">Nanoparçacık Ayırıcı</Color>, yalnızca eşya türüne ve hatta CC'lerin paketten çıkarılmış hallerine göre filtreleyemez. Tek bir eşya türü için birden fazla geçerli filtre varsa, aralarında eşit olarak bölünür.

Ayırıcı Kızıltaş Girişi, yapının üstündeki herhangi bir nanoçip örgü arayüz kasasının yerini alan ve harici bir kızıltaş alıcısı görevi gören isteğe bağlı bir kapaktır. Gelen kızıltaş sinyalinin gücü, kuralları yönetmek için kapağın GUI'sinde yapılandırılan kanalla ilişkilendirilir. 
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9510"/><ItemImage id="gregtech:gt.blockmachines:9510"/>
- 37 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 18 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 10 <ItemLink id="gregtech:gt.blockframes:765"/><ItemImage id="gregtech:gt.blockframes:765"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9515"/> (herhangi bir üst arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9515"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## Parça Hazırlama Aparatı <ItemImage id="gregtech:gt.blockmachines:9505"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9505" />
</GameScene>
<Color id="GREEN">Parça Hazırlama Aparatı</Color> SMD CC'lerini işler. Bu modül tüm devre hatları için gereklidir.
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9505"/><ItemImage id="gregtech:gt.blockmachines:9505"/>
- 44 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 20 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 17 <ItemLink id="gregtech:gt.blockframes:979"/><ItemImage id="gregtech:gt.blockframes:979"/>
- 8 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 4 <ItemLink id="gregtech:gt.blockcasingsNH:10"/><ItemImage id="gregtech:gt.blockcasingsNH:10"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## Nanohassas Tel İzleyici <ItemImage id="gregtech:gt.blockmachines:9509"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9509" />
</GameScene>
<Color id="GREEN">Nanohassas Tel İzleyici</Color> tel CC'lerini işler. Bu modül tüm devre hatları için gereklidir.
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9509"/><ItemImage id="gregtech:gt.blockmachines:9509"/>
- 46 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 28 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 25 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 20 <ItemLink id="gregtech:gt.blockframes:985"/><ItemImage id="gregtech:gt.blockframes:985"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## Nanohassas Kesim Odası <ItemImage id="gregtech:gt.blockmachines:9508"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9508" />
</GameScene>
<Color id="GREEN">Nanohassas Kesim Odası</Color>, civata, çerçeve, bellek çipi ve yonga plakası CC'lerini işler. Bu modül tüm devre hatları için gereklidir.
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9508"/><ItemImage id="gregtech:gt.blockmachines:9508"/>
- 31 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 28 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 24 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 21 <ItemLink id="gregtech:gt.blockframes:129"/><ItemImage id="gregtech:gt.blockframes:129"/>
- 16 <ItemLink id="gregtech:gt.blockcasings9:12"/><ItemImage id="gregtech:gt.blockcasings9:12"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 1+ Giriş Kapağı (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>

## Tam Kart Daldırma Cihazı <ItemImage id="gregtech:gt.blockmachines:9506"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9506" />
</GameScene>
<Color id="GREEN">Tam Kart Daldırma Cihazı</Color>, devre kartı CC'lerini karşılık gelen daldırma sıvısında temizleyerek işler. Tarifler daldırma sıvısından hiç tüketmez, bunun yerine kirliliği %100'e kadar artırır. Daha yüksek kirlilik, modülün güç tüketimini, ister kontrolcünün GUI'si üzerinden manuel olarak ister yapılandırılmış bir yüzde seviyesinde otomatik tahliyeyi tetikleyerek boşaltılana kadar %300'e kadar artırır. Otomatik tahliye %1-100 arasında olmalıdır, bu yüzden tankın sonunda yeniden doldurulması gerekir.

Dört daldırma sıvısı mevcuttur, ancak dahili tank aynı anda yalnızca birini tutabilir. Başlamak için normal bir giriş kapağından 500.000L ile 1.000.000L arasında daldırma sıvısı sağla. Fazla daldırma sıvısı tüketilmez ve maksimumdan daha azına sahip olmak, aşağıdaki denklemde görüldüğü gibi kirliliğin artma hızını artırır. Toplam eşya sayısı iterasyonlar arasında devreder, böylece tarif veya parti boyutundan bağımsız olarak her 1.000 eşyada bir kirlilik eklenir. 
<br clear="all"/>

<Latex formula="+\text{Impurity}\% = \frac{10,000,000,000,000 \times \lfloor \text{Items} \div 1,000 \rfloor}{\text{Immersion Fluid}^{2.5}}"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9506"/><ItemImage id="gregtech:gt.blockmachines:9506"/>
- 52 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 27 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 19 <ItemLink id="miscutils:blockFrameGtOctiron"/><ItemImage id="miscutils:blockFrameGtOctiron"/>
- 10 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 1+ Giriş Kapağı (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>

| Devre Kartı   | Daldırma Sıvısı    |
|--------------- | --------------- |
| Elit (Kristal)   | Demir III Klorür   |
| Nöro   | Büyüme Katalizörü Ortamı   |
| Biyo   | Sterilize Biyo Katalizör Ortamı   |
| Optik   | Prizmatik Asit   |

----------

| Daldırma Sıvısı | +Kirlilik% | Maks. Yaşam Ömrü |
| --------------- | --------------- | --------------- |
| 500.000L | 1.000 başına %0,056 | 1.786.000 Eşya |
| 750.000L | 1.000 başına %0,021 | 4.872.000 Eşya |
| 1.000.000L | 1.000 başına %0,010 | 10.000.000 Eşya |

----------


| Kirlilik | EU/t |
| -------------- | --------------- |
| %0-15 | %70 + (2 x Kirlilik%) |
| %15-65 | %100 |
| %65-100 | %100 + (2 x Kirlilik%) |

## Nanometre Kaplama Sarıcısı <ItemImage id="gregtech:gt.blockmachines:9513"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9513" />
</GameScene>

<Color id="GREEN">Nanometre Kaplama Sarıcısı</Color> levha ve çerçeve CC'lerini işler. Bu modülü filtrelemek en zorudur çünkü çoğu tarifin birden fazla girişi vardır ve çıktılar genellikle birçok farklı yerde gereklidir. Bu modül tüm devre hatları için gereklidir. 
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9513"/><ItemImage id="gregtech:gt.blockmachines:9513"/>
- 47 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 40 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 32 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 32 <ItemLink id="gregtech:gt.blockframes:391"/><ItemImage id="gregtech:gt.blockframes:391"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## Süperiletken Tel Demeti Ayırıcı <ItemImage id="gregtech:gt.blockmachines:9511"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9511" />
</GameScene>
<Color id="GREEN">Süperiletken Tel Demeti Ayırıcı</Color>, aktifken saniyede 1.000 L süper soğutucu maliyetiyle süperiletken CC'lerini işler. Bu modül piko/kuantum devre hattı için gerekli değildir. 
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9511"/><ItemImage id="gregtech:gt.blockmachines:9511"/>
- 40 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 29 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 24 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 16 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils:8"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:8"/>
- 6 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils:7"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:7"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 1+ Giriş Kapağı (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>

## Ultra Yüksek Enerji Aşındırma Dizisi <ItemImage id="gregtech:gt.blockmachines:9507"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9507" />
</GameScene>
<Color id="GREEN">Ultra Yüksek Enerji Aşındırma Dizisi</Color>, kristal CC'lerini kendi lazer kaynağı kapağıyla işler. Tam kalibre edilmiş bir kristal NAC'de modülün güç tüketimi lazer kaynağı kapağının $$\log_4(\text{Amps})$$ değerine bölünür ve tariflerin süresi $$\text{Voltage Tier} - 9$$ değerine bölünür. Bu modül optik veya piko/kuantum devre hatları için gerekli değildir. 
<br clear="all"/>

| Amperaj   | EU/t    |
|--------------- | --------------- |
| 256   | %100   |
| 1.024   | %50,0   |
| 4.096   | %33,3   |
| 16.384   | %25,0   |
| 65.536   | %20,0   |
| 262.144   | %16,7   |
| 1.048.576   | %14,3   |
| 4.194.304   | %12,5   |
| 16.777.216   | %11,1   |

| Voltaj   | Süre    |
|--------------- | --------------- |
| UEV   | %100   |
| UIV   | %50   |
| UMV   | %33   |
| UXV   | %25   |


### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9507"/><ItemImage id="gregtech:gt.blockmachines:9507"/>
- 28 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 24 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 17 <ItemLink id="gregtech:gt.blockframes:582"/><ItemImage id="gregtech:gt.blockframes:582"/>
- 13 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 9 <ItemLink id="gtnhlanth:casing.shielded_accelerator"/><ItemImage id="gtnhlanth:casing.shielded_accelerator"/>
- 4 <ItemLink id="gregtech:gt.blockglass1:3"/><ItemImage id="gregtech:gt.blockglass1:3"/>
- 1 Lazer Kaynağı Kapağı <ItemImage id="gregtech:gt.blockmachines:15230"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>

## Hızlandırılmış Biyolojik Koordinatör <ItemImage id="gregtech:gt.blockmachines:9514"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9514" />
</GameScene>
<Color id="GREEN">Hızlandırılmış Biyolojik Koordinatör</Color> canlı CC'leri işler. Tam kalibre edilmiş bir nöro NAC'de hiç büyüme katalizörü ortamı tüketmez ve tam kalibre edilmiş bir biyo NAC'de hiç sterilize biyo katalizör ortamı tüketmez. Bu modül kristal, optik veya piko/kuantum devre hatları için gerekli değildir. 
<br clear="all"/>

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9514"/><ItemImage id="gregtech:gt.blockmachines:9514"/>
- 37 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 36 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 36 <ItemLink id="gregtech:gt.blockframes:329"/><ItemImage id="gregtech:gt.blockframes:329"/>
- 20 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 1+ Giriş Kapağı (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>

## Optik Olarak Optimize Edilmiş Düzenleyici <ItemImage id="gregtech:gt.blockmachines:9512"/>
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:9512" />
</GameScene>
<Color id="GREEN">Optik Olarak Optimize Edilmiş Düzenleyici</Color>, optik CC'lerini 3. ve 8. derece dahil olmak üzere iki tür temizlenmiş suda temizleyerek işler. Her temizlenmiş su modüle bir bonus verir, aşağıdaki tabloda görüldüğü gibi. Benzer etkiler birbiriyle çarpımsal olarak yığılır ve tam kalibre edilmiş bir optik NAC'de tüm etkiler iki kez uygulanır. Bu modül kristal, nöro, biyo veya piko/kuantum devre hatları için gerekli değildir. 

| Su | Maliyet | Bonus |
| --------------- | --------------- | --------------- |
| 3. Derece | 1.000 L/s | x0,8 Su Maliyeti |
| 4. Derece | 800 L/s | x0,6 Su Maliyeti |
| 5. Derece | 800 L/s | x0,9 Süre |
| 6. Derece | 600 L/s | x0,7 Süre |
| 7. Derece | 600 L/s | x0,9 EU/t |
| 8. Derece | 400 L/s | x0,7 EU/t |

### Gereksinimler:
- 1 <ItemLink id="gregtech:gt.blockmachines:9512"/><ItemImage id="gregtech:gt.blockmachines:9512"/>
- 55 <ItemLink id="gregtech:gt.blockcasings12:2"/><ItemImage id="gregtech:gt.blockcasings12:2"/>
- 49 <ItemLink id="gregtech:gt.blockcasings12:1"/><ItemImage id="gregtech:gt.blockcasings12:1"/>
- 48 <ItemLink id="gregtech:gt.blockframes:976"/><ItemImage id="gregtech:gt.blockframes:976"/>
- 40 <ItemLink id="gregtech:gt.blockglass1:8"/><ItemImage id="gregtech:gt.blockglass1:8"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9501"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9501"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:9502"/> (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:9502"/>
- 1+ Giriş Kapağı (herhangi bir temel arayüz kasası) <ItemImage id="gregtech:gt.blockmachines:50"/>
----------
## Kalibrasyon:
<Color id="GREEN">NAC</Color>, son 100.000 devre içinde her devre türünün sıklığını izlemek için Nanoçip Montaj Matrisinde (NAM) üretilen her devreyi kaydeder. Devre geçmişi yalnızca her 1.000 devrede bir güncellenir ve önce en eski bilgiyi değiştirir. Mevcut devre geçmişini ve sonraki 1.000 devreye doğru ilerlemeyi kontrolcünün GUI'si üzerinden görüntüle.

Aynı devre türünden yeterince üretildiğinde, <Color id="GREEN">NAC</Color> o devre hattına kalibre edilir ve aşağıdaki tablolarda görüldüğü gibi en fazla üç yığılan bonus kazanır. Aynı anda yalnızca bir kalibrasyon aktif olabilir ve yüksek kademeler düşük olanlara göre daha yüksek önceliğe sahiptir. Her kalibrasyon kademesinin, hangisinin etkin olduğunu belirlemeye yardımcı olmak için kontrolcünün GUI'sindeki makine adına eklenen kendine özgü bir öneki vardır. Kalibrasyon bonuslarını en üst düzeye çıkarmak için her devre hattı başına bir <Color id="GREEN">NAC</Color> inşa etmen önerilir. 

Kalibrasyonun ayrıntıları her devre türüne çok özgüdür ve burada açıklanamayacak kadar detaylıdır, bu yüzden daha fazla bilgi için [NAC Wiki Sayfası](https://wiki.gtnewhorizons.com/wiki/Nanochip_Assembly_Complex) sayfasına göz at!