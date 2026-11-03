---
item_ids:
  - gregtech:gt.blockmachines:1172
navigation:
  title: Temiz Oda
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:1172
  position: 12
quest_ids:
  - AAAAAAAAAAAAAAAAAAADrA
---

# Temiz Oda

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1172" tier={2} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" />, HV'de bulunan bir multiblok tesistir. İçine yerleştirilen makineler için temiz bir çevre sağlar ve daha gelişmiş veya daha ucuz devreler, devre kartları ve diğer ürünler için tariflere olanak tanır.

Temiz Oda'nın kendisi işlem girdileri almaz veya ürün çıktısı vermez. Asıl işlem makinelerini içine yerleştir, onlara kendi güçlerini sağla ve eşya ile sıvı G/Ç'lerini düzenle. Temiz Oda'nın Enerji Kapağı yalnızca çevreye güç verir.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | HV; Temiz Oda LV güçle çalıştırılabilir |
| Boyutlar | Her biri 3–15 blok dış genişlik ve uzunluk, 4–15 blok yükseklik; dikdörtgen bir taban alanına izin verilir |
| İlk yapı | 5×5×5, 3×3×3 kullanılabilir iç alan sağlar |
| Güç | Tam olarak bir sıradan Enerji Kapağı; bir LV Enerji Kapağı 2A kabul edebilir |
| Temizlik | Yüzde 0'dan %100'e kademeli olarak yükselir; %100'ün altında, Temiz Oda gerektiren tariflerden gelen eşya çıktıları kaybolabilir |
| Hız aşırtma ve bonuslar | Enerji Kapağını yükseltmek temizliği hızlandırır; içerideki makinelere ekstra hız, paralel işlem veya güç indirimi sağlamaz |
| Bakım ve kirlilik | Bir Bakım Kapağı gerektirir; her bakım sorunu maksimum temizliği 10 yüzde puan düşürür; içeride kirlilik üretilmemelidir |

> [!WARNING]
> **Temiz Oda gerektiren tarifler için malzeme vermeden önce %100 temizliği bekle.** %100'ün altında bir makine malzemeleri tüketip tarifi normal şekilde çalıştırabilir, ancak bir eşya çıktısını kaybedebilir.

## Üretim ve İnşaat

Kontrolcü, Plascrete Blokları ve Filtre Makine Kasaları için mevcut tarifler aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1172" />

<RecipesFor id="gregtech:gt.blockreinforced:2" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

### İlk 5×5×5 Temiz Odan

Bu boyutlar duvarları, zemini ve tavanı içerir ve 3×3×3 bir iç alan bırakır. Önce kabuğu ve güç kaynağını tamamla, ardından gerektiği kadar erişim ve taşıma bağlantı noktası ekle.

| Bileşen | Temel miktar ve konum |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" /> | Bir adet, tavanın merkezinde; kontrolcü yatay bakmalı, asla yukarı veya aşağı bakmamalı |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | Sekiz adet, tavanın iç alanının geri kalanını doldurur |
| <ItemLink id="gregtech:gt.blockreinforced:2" showIcon="left" /> | 87 adet, zemini, duvarları ve tavan çevresini oluşturur; bu sayı gerekli iki kapağı zaten hesaba katar |
| Enerji Kapağı | Tam olarak bir adet, bir Plascrete Bloğunun yerine geçer |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | Tam olarak bir adet, bir Plascrete Bloğunun yerine geçer |

Yukarıdaki önizleme kabuğu gösterir. İnşa ederken iki Plascrete Bloğunu Enerji Kapağı ve Bakım Kapağı ile değiştir. Her ek geçerli taşıma bağlantı noktası veya cam bloğu bir Plascrete Bloğu daha değiştirir.

Aşağıdaki sırayla inşa et:

1. Sağlam bir 5×5 zemin döşe ve dört duvarı inşa et; güç, bakım ve erişim için yer ayır.
2. Tavan çevresini Plascrete Blokları ile inşa et. Kontrolcüyü merkeze ve sekiz Filtre Makine Kasasını kalan iç konumlara yerleştir.
3. Enerji Kapağını ve Bakım Kapağını tak, ardından kalan tüm boşlukları kapat.
4. İşlem makinelerini, kabloları ve boruları duvarların içine, zeminin üstüne ve filtrelerin altına yerleştir. İşlem makineleri duvar bloklarının yerine geçemez.
5. Yapıyı kontrol et, tüm bakım sorunlarını gider, kararlı bir güç kaynağı bağla ve %100 temizliği bekle.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> öğesini kullan. Genişletmeden önce üretimi ve malzeme girişini durdur. İşleme devam etmeden önce yeniden inşa edilen odayı kontrol et ve temizle.

### Genişletme ve Kasa Değişimleri

Taban alanı dikdörtgen olabilir. Kontrolcüyü tavanın merkezinde tut ve tavan çevresinin içindeki diğer tüm konumları Filtre Makine Kasalarıyla doldur. Genişlik veya uzunluk çift ise, o eksen boyunca ortadaki konumlardan herhangi biri geçerlidir. İkisi de çift ise dört olası merkez konumu vardır.

Varsayılan yapılandırma **en az 20 gerçek Plascrete Bloğu** gerektirir ve diğer geçerli bloklarla yapılan değişimleri sınırlar. Değişim payı “değişim blokları ÷ (Plascrete Blokları + değişim blokları)” olarak hesaplanır; yüzdesi bir tam sayıya aşağı yuvarlanır ve **%30**'u aşmamalıdır. Filtreler ve kontrolcü bu hesaplamadan hariç tutulur. Enerji ve Bakım Kapakları, kapılar, cam ve taşıma bağlantı noktalarının tümü değişim olarak sayılır.

| Değişim | Yerleştirme kuralları |
| --- | --- |
| Sıradan Enerji Kapağı ve Bakım Kapağı | Plascrete konumları; her birinden tam olarak bir adet |
| GT Makine Gövdeleri ve Diyotlar | Plascrete konumları; kabuktan taşıma için kullanılır |
| Geçerli cam | Plascrete konumları; sıradan vanilla cam geçersizdir |
| IC2 Güçlendirilmiş Kapı | Yan duvarlar, dikey kenarlardan ve köşelerden uzakta; zeminde veya tavanda değil |
| OpenBlocks Elevators ve Ender IO Travel Anchors | Zemin dahil Plascrete konumları |

EV ve daha yüksek kademe cam kabul edilir. Paketin varsayılan yapılandırması ayrıca BartWorks kademeli camı gibi belirli bloklara, HV camı dahil, izin verir. Bu nedenle her geçerli camın EV olması gerekmez ve her dekoratif cam geçerli bir değişim değildir.

Temiz Oda Giriş Otobüslerine, Çıkış Otobüslerine, sıvı kapaklarına veya bir Egzoz Çıkışına ihtiyaç duymaz ve bunlar duvar bloklarının yerine geçemez. Eşyaları ve sıvıları içerideki işlem makinelerinin kendi arayüzlerine ulaştır.

Kapı geçişi olarak Extra Utilities'ın <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> öğesi önerilir; oyuncuların temizliği azaltmadan geçmesini sağlar.

## Kullanımlar ve İlk Başlatma

Devre Montajcıları, Lazer Gravürcüleri, Montaj Makineleri, Kesme Makineleri ve Otoklavlardaki **bazı tarifler** temiz bir çevre gerektirir. NEI'de tek tek tarifin “Temiz Oda Gerekir” notunu kontrol et.

İlk başlatmadan önce işlem makinelerini kapat veya malzemelerini geri tut, ardından odayı hazırla:

1. Kontrolcünün doğru kapak sayılarıyla tam bir yapı bildirdiğini doğrula.
2. Altı bakım sorununun tümünü gider. Bkz. [Multiblok Makineleri: Bakım](../multiblocks_index.md#maintenance).
3. Kapıları kapat ve içerideki hiçbir ekipmanın kirlilik üretmediğinden emin ol.
4. Temiz Oda'ya sürekli güç sağla ve temizliğinin yükselişini izle.
5. %100'de her işlem makinesini kendi güç kaynağına bağla ve işlemeye başlamak için malzemeleri yerleştir.

Sıradan GT tek bloklu makineleri, temizlik yüzde 0'ın üzerine çıktığında Temiz Oda gerektiren tarifleri başlatabilir, ancak çıktıları güvenli garantili değildir. Yetersiz temizlik nedeniyle eşya kaybı **tarif başladığında ve malzemelerini tükettiğinde** belirlenir. İşleme yarısında %100'e ulaşmak, kayıp için zaten seçilmiş bir çıktıyı kurtaramaz.

%100 temizlik yalnızca çevreden kaynaklanan kayıpları ortadan kaldırır. Doğası gereği olasılıklı çıktıları olan bir tarif yine NEI'de gösterilen şansları kullanır.

Büyük Kimyasal Reaktör ve Hiper Yoğunluklu Lazer Gravürcüsü gibi bazı ileri multiblokların Temiz Oda'ya yerleştirilmesi gerekmez. **Tüm multiblok makinelerinin yerleşik bir temiz oda çevresi vardır.**

## Temizlik ve Güç

HV, kontrolcünün kilit açma kademesidir, minimum güç kademesi değildir. Bir LV Enerji Kapağı ile Temiz Oda başlangıçta **40 EU/t** tüketir. Tüketim, temizlik yükseldikçe kademeli olarak azalır ve %100'de **4 EU/t**'ye düşer.

40 EU/t, bir LV jeneratörün nominal çıktısını aşar, ancak Temiz Oda'nın LV Enerji Kapağı 2A kabul edebilir. İlk yapı için iki LV jeneratör veya sürekli olarak yeterli güç sağlayabilen başka bir LV kaynağı kullan; kablolama da akıma uygun olmalıdır. Tek bir 32 EU/t LV jeneratör odayı tek başına yüzde 0'dan temizleyemez. Kablo kayıplarını da hesaba kat.

Aşağıdaki örnek **beş blok dış yükseklik, bakım sorunu yok, kapılar kapalı ve yüzde 0'dan %100'e temizlik** varsayar. Süreler 20 TPS'de normal çalışmayı varsayar.

| Enerji Kapağı kademesi | Başlangıç tüketimi | %100'de tüketim | Yaklaşık temizlik süresi |
| --- | --- | --- | --- |
| LV | 40 EU/t | 4 EU/t | 15 dakika |
| MV | 40 EU/t | 4 EU/t | 15 dakika |
| HV | 160 EU/t | 16 EU/t | 7 dakika 30 saniye |
| EV | 640 EU/t | 64 EU/t | 3 dakika 45 saniye |

MV, LV'den daha hızlı temizlemez. HV'den başlayarak standart kayıplı hız aşırtma, gücü dörtle çarpar ve her hız aşırtmada temizlik süresini yarıya indirir. Daha yüksek odaların temizlenmesi daha uzun sürer; yalnızca genişlik veya uzunluğu artırmak temizlik döngüsünü uzatmaz.

**Temiz Oda'ya ve işlem makinelerine ayrı ayrı güç ver.** Temiz Oda'nın Enerji Kapağı kademesi, içerideki makinelerin gerilimini sınırlamaz veya onlara hız aşırtma bonusları vermez. Güç kaynağını boyutlandırırken Temiz Oda'nın tüketimini tüm işlem makinelerinin tüketimine ekle.

Odayı %100'e ulaştıktan sonra çalışır durumda tut. Boşta gücünden tasarruf etmek için kapatma. Kapatma, güç kesintisi veya bozulmuş yapıdan sonra çevreyi yeniden sağla ve işlemeye devam etmeden önce %100 temizliği doğrula.

## Duvarlardan Erişim, Güç ve Taşıma

### Erişim

Bir IC2 Güçlendirilmiş Kapı erişim sağlar. Açık bir kapı algılandığında Temiz Oda sürekli temizlik kaybeder, normalde her beş saniyede iki yüzde puanı. Kullanımdan sonra kapıları kapat. Sık erişim için, bir kapıyı tekrar tekrar açmaktan kaçınmak üzere Extra Utilities'ın <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> öğesini kullan.

Tahta kapılar, vanilla demir kapılar, delikler ve sıradan borular geçerli Temiz Oda duvar blokları değildir. Güç kabloları veya ME kabloları için boşluk bırakma.

### Duvarlardan Güç

Duvara uygun kademede bir **GT Makine Gövdesi** veya **Diyot** gömerek harici güç kaynağını içerideki makine kablolarına bağla. Örneğin, bir <ItemLink id="gregtech:gt.blockmachines:13" showIcon="left" /> HV gücünü duvardan taşıyabilir.

Bir Makine Gövdesi gücü ön yüzünden verir ve diğer yüzlerinden güç kabul eder. Çıkışını içeri doğru bakacak şekilde yerleştir ve kabloları iki taraftan bağla. Daha yüksek akım için uygun nominal değere sahip bir Diyot kullan ve her iki kablo hattının akım kapasitesini kontrol et.

> [!WARNING]
> İçerideki makinelere sağlanan gerilimi yükseltirken duvardaki Makine Gövdelerini, Diyotları ve kabloları da kontrol et. Daha yüksek kademe gücü eski daha düşük kademe bir bağlantı noktasına bağlamak aşırı gerilim patlamasına neden olur. Yalnızca eşya taşıma için kullanılan güçsüz bir gövdenin makinenin gerilimiyle yükseltilmesi gerekmez.

### Eşyalar ve Sıvılar

GT Makine Gövdelerinin bir eşya yuvası ve bir sıvı tamponu vardır; bu, duvardan taşıma kapları olarak hizmet etmelerini sağlar. Bu tampona eklemek ve buradan çıkarmak için iki tarafta borular veya Konveyör Modülleri kullan, ardından içerideki makinelere ulaştır. Gövde tarifleri işlemez veya her şeyi otomatik olarak amaçlanan makinelere dağıtmaz.

Mümkün olduğunda malzemeler, ürünler ve farklı sıvılar için ayrı bağlantı noktaları kullan; böylece istenmeyen materyaller paylaşılan küçük bir tamponu dolduramaz. İşlem makinelerinin giriş yüzlerini, çıkış yüzlerini ve otomatik çıkışını ayrı ayrı yapılandır; duvardaki bir gövde bu ayarların yerine geçmez.

AE2 ile odanın içinde ve dışında <ItemLink id="appliedenergistics2:tile.BlockWirelessConnector" showIcon="left" /> öğelerini kullanarak bir bağlantı kur, ardından içerideki ME Arayüzlerini, otobüsleri ve diğer cihazları bağla. Kablosuz Bağlayıcılar duvar konumlarını işgal etmez ve kasa değişim payında daha fazla yer bırakır.

ME ağına güç vermek, işlem makinelerine GT EU sağlamaz. Makine gücünü Makine Gövdeleri, Diyotlar veya ayrı olarak yapılandırılmış bir GT EU P2P kurulumu üzerinden sağla.

## Bakım, Kirlilik ve İzleme

Çözülmemiş her bakım sorunu maksimum temizliği **10 yüzde puanı** düşürür. Bir sorun %90'da, iki sorun %80'de sınırlar. Temiz Oda yine de çalışabilir, ancak güvenli %100'e ulaşamaz. Onarımlardan sonra, çevre gerektiren tariflere devam etmeden önce temizliğin toparlanmasını bekle.

> [!WARNING]
> Temiz Oda'nın içine kirletici jeneratörler veya diğer kirletici ekipmanları koyma. İçerideki bir makineden gelen kirlilik temizliği sıfıra sıfırlar ve altı bakım sorununun tümünü tetikleyerek Temiz Oda'yı durdurur. Bir Egzoz Çıkışı bunu düzeltemez. Kirlilik kaynağını dışarı taşı, ardından onar, yeniden başlat ve odayı tekrar temizle.

Temizliği, bakımı ve çalışmayı kontrol etmek için kontrolcü GUI'sini ve Waila'yı kullan. Bir ışığa veya alarma bağlı bir Endüstriyel Bilgi Paneli ya da Needs Maintenance Cover, bakım sorunlarını izlemeye yardımcı olabilir. Bakım sorunu olmaması temizliğin zaten %100 olduğu anlamına gelmez; kapıları açtıktan, güç kesintilerinden veya yeniden başlatmadan sonra çevreyi kontrol et.

Kontrolcü ayrıca her taraftan temizliği yansıtan bir kızıltaş sinyali yayar. **%100, sinyal gücü 15'e karşılık gelir.** Malzeme girişini otomatik olarak kontrol etmek için sinyal gücü 15'i kontrol et. Sıfır olmayan her sinyal yetersizdir, çünkü düşük temizlik de sinyal üretebilir. Yapı kontrolleri ve kızıltaş güncellemeleri gecikmelidir; bu nedenle kapıları kapalı, gücü kararlı tut ve herhangi bir interlokla birlikte bakımı da çöz.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Eksik yapı | Dış boyutlar, yatay bakan merkezi bir tavan kontrolcüsü, iç tavan boyunca filtreler ve tamamen kapalı duvarlar ve zemin |
| Yanlış kapak sayısı | Tam olarak bir sıradan Enerji Kapağı ve bir Bakım Kapağı; kabukta Giriş Otobüsü, sıvı kapağı veya Egzoz Çıkışı olmamalı |
| Cam veya bağlantı noktaları eklendikten sonra oda oluşmuyor | Değişimlerin geçerli olup olmadığı, en az 20 Plascrete Bloğunun kalıp kalmadığı ve tüm değişimlerin birlikte yüzde sınırını karşılayıp karşılamadığı |
| LV güçle hemen kapanma | Yalnızca bir 32 EU/t jeneratörün bağlı olup olmadığı; yeterli sürekli başlangıç gücü, kablo akım kapasitesi, kablo kayıpları ve enerji tamponu |
| MV güç temizliği hızlandırmıyor | MV'nin temizlik hız aşırtması yoktur; daha hızlı temizlik HV'de başlar. Gerilimi yükseltmeden önce Enerji Kapağını ve besleme kablolarını yükselt |
| Temizlik %90 veya %80'de kalıyor | Çözülmemiş bakım sorunları; temizlik düşmeye devam ediyorsa açık Güçlendirilmiş Kapıları da kontrol et |
| Malzemeler tüketildi ama bir eşya çıktısı eksik | Tarif başladığında temizliğin %100 olup olmadığı; ardından doğal çıktı şanslarını ve makinenin çıktı yapılandırmasını kontrol et |
| İçerideki makine hâlâ Temiz Oda gerektiriyor | Tamamen içeride olup olmadığı, Temiz Oda'nın yüzde 0'ın üzerinde temizlikle oluşup oluşmadığı ve yerleştirme veya genişletmeden bu yana bir yapı kontrolünün gerçekleşip gerçekleşmediği |
| Temiz Oda çalışıyor ama içerideki bir makine çalışmıyor | Makine gücünün ayrı olup olmadığını, gerilimini, malzemelerini, sıvılarını, Entegre Devre yapılandırmasını ve çıktı alanını kontrol et |
| Temizlik tüm bakım sorunlarıyla aniden sıfırlanıyor | İçerideki bir kirlilik kaynağını bul ve kaldır, bakımı onar ve yeniden başlat; işlem malzemelerini geri tut |

Genel alet kontrolleri, bakım ve güç kesintisi rehberliği için [Multiblok Makineleri](../multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Temiz Oda](https://wiki.gtnewhorizons.com/wiki/Cleanroom)