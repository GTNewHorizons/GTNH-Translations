---
item_ids:
  - gregtech:gt.blockmachines:1172
quest_ids:
  - AAAAAAAAAAAAAAAAAAADrA==
  - AAAAAAAAAAAAAAAAAAAHfQ==
navigation:
  title: Temiz Oda
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1172
  position: -3001
---
# Temiz Oda

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1172" tier={2} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" />, HV'de mevcut olan bir multiblok tesistir. İçine yerleştirilen makineler için temiz bir çevre sağlar ve daha gelişmiş veya daha ucuz devreler, devre kartları ve diğer ürünler için tariflere olanak tanır.

Temiz Odanın kendisi işleme malzemesi almaz ve ürün vermez. Asıl işleme makinelerini içine yerleştir, onlara kendi enerjilerini sağla ve eşya ile sıvı giriş/çıkışlarını ayarla. Temiz Odanın Enerji Kapağı yalnızca çevreyi besler.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | HV; Temiz Oda LV enerjiyle bakımda tutulabilir |
| Boyutlar | Dış genişlik ve uzunluk her biri 3–15 blok, yükseklik 4–15 blok; dikdörtgen bir taban alanı serbesttir |
| İlk inşa | 5×5×5, 3×3×3 kullanılabilir iç hacim sağlar |
| Enerji | Tam olarak bir sıradan Enerji Kapağı; bir LV Enerji Kapağı 2A kabul edebilir |
| Temizlik | Kademeli olarak yüzde 0'dan yüzde 100'e yükselir; %100'ün altında Temiz Oda gerektiren tariflerin eşya çıktıları kaybolabilir |
| Hız aşırtma ve bonuslar | Enerji Kapağını yükseltmek temizliği hızlandırır; içerideki makinelere ek hız, paralel veya enerji indirimi sağlamaz |
| Bakım ve kirlilik | Bir Bakım Kapağı gerektirir; her bakım sorunu maksimum temizliği 10 puan düşürür; içeride kirlilik oluşmamalıdır |

> [!WARNING]
> **Temiz Oda gerektiren tarifler için malzeme sağlamadan önce %100 temizliği bekle.** %100'ün altında bir makine malzemeleri tüketip tarifi normal çalıştırabilir ama bir eşya çıktısını kaybedebilir.

## Üretim ve İnşa

Kontrolcü, Plascrete Blokları ve Filtre Makinesi Kasaları için mevcut tarifler aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1172" />

<RecipesFor id="gregtech:gt.blockreinforced:2" />

<RecipesFor id="gregtech:gt.blockcasings3:11" />

### İlk 5×5×5 Temiz Odan

Bu boyutlar duvarları, zemini ve tavanı içerir, geriye 3×3×3 iç hacim kalır. Önce kabuğu ve enerji beslemesini tamamla, sonra gerektiği kadar erişim ve taşıma portu ekle.

| Bileşen | Temel miktar ve konum |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1172" showIcon="left" /> | Bir adet, tavanın merkezinde; kontrolcü yatay bakmalı, asla yukarı veya aşağı bakmamalı |
| <ItemLink id="gregtech:gt.blockcasings3:11" showIcon="left" /> | Sekiz adet, tavanın iç alanının kalanını doldurur |
| <ItemLink id="gregtech:gt.blockreinforced:2" showIcon="left" /> | 87 adet, zemini, duvarları ve tavan çevresini oluşturur; bu sayı gerekli iki kapağı zaten hesaba katar |
| Enerji Kapağı | Tam olarak bir adet, bir Plascrete Bloğunun yerine |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | Tam olarak bir adet, bir Plascrete Bloğunun yerine |

Yukarıdaki önizleme kabuğu gösterir. İnşa ederken iki Plascrete Bloğunu Enerji Kapağı ve Bakım Kapağı ile değiştir. Eklenen her geçerli taşıma portu veya cam bloğu bir Plascrete Bloğu daha değiştirir.

Şu sırayla inşa et:

1. Sağlam bir 5×5 zemin döşe ve dört duvarı ör; enerji, bakım ve erişim için yer ayır.
2. Tavan çevresini Plascrete Bloklarıyla ör. Kontrolcüyü merkeze, sekiz Filtre Makinesi Kasasını kalan iç konumlara yerleştir.
3. Enerji Kapağını ve Bakım Kapağını tak, ardından kalan tüm boşlukları kapat.
4. İşleme makinelerini, kabloları ve boruları duvarların içine, zeminin üstüne ve filtrelerin altına yerleştir. İşleme makineleri duvar bloklarının yerini alamaz.
5. Yapıyı kontrol et, tüm bakım sorunlarını gider, sabit bir enerji beslemesi bağla ve %100 temizliği bekle.

Yapıyı önizlemek ve inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Genişletmeden önce üretimi ve malzeme girişini durdur. İşlemeye devam etmeden önce yeniden inşa edilen odayı kontrol et ve temizle.

### Genişletme ve Kasa Değişimleri

Taban alanı dikdörtgen olabilir. Kontrolcüyü tavanın merkezinde tut ve tavan çevresinin içindeki diğer tüm konumları Filtre Makinesi Kasalarıyla doldur. Genişlik veya uzunluk çift sayıysa o eksen boyunca ortadaki iki konumdan biri geçerlidir. İkisi de çift ise dört olası merkez konumu vardır.

Varsayılan yapılandırma **en az 20 gerçek Plascrete Bloğu** gerektirir ve diğer geçerli bloklarla yapılan değişimleri sınırlar. Değişim payı "değişim blokları ÷ (Plascrete Blokları + değişim blokları)" olarak hesaplanır; yüzdesi tam sayıya aşağı yuvarlanır ve **%30**'u aşmamalıdır. Filtreler ve kontrolcü bu hesaplamanın dışındadır. Enerji ve Bakım Kapakları, kapılar, cam ve taşıma portlarının hepsi değişim olarak sayılır.

| Değişim | Yerleştirme kuralları |
| --- | --- |
| Sıradan Enerji Kapağı ve Bakım Kapağı | Plascrete konumları; her birinden tam olarak bir adet |
| GT Makine Gövdeleri ve Diyotlar | Plascrete konumları; kabuktan taşıma için kullanılır |
| Geçerli cam | Plascrete konumları; sıradan vanilla cam geçersizdir |
| IC2 Güçlendirilmiş Kapı | Yan duvarlar, dikey kenarlardan ve köşelerden uzakta; zeminde veya tavanda olamaz |
| OpenBlocks Elevators ve Ender IO Travel Anchors | Plascrete konumları, zemin dahil |

EV ve daha yüksek kademe cam kabul edilir. Paketin varsayılan yapılandırması ayrıca BartWorks kademeli camı gibi belirli bloklara, HV camı dahil, izin verir. Bu yüzden her geçerli camın EV olması gerekmez ve her dekoratif cam geçerli bir değişim değildir.

Temiz Oda Giriş Otobüsleri, Çıkış Otobüsleri, sıvı kapakları veya bir Egzoz Çıkışı gerektirmez ve bunlar duvar bloklarının yerini alamaz. Eşya ve sıvıları içerideki işleme makinelerinin kendi arayüzlerine ulaştır.

Kapı geçişi olarak Extra Utilities'in <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> bloğu önerilir; oyuncular temizliği düşürmeden içinden geçebilir.

## Kullanımlar ve İlk Başlatma

Devre Montaj Makineleri, Lazer Gravür Makineleri, Montaj Makineleri, Kesme Makineleri ve Otoklavlardaki **bazı tarifler** temiz bir çevre gerektirir. NEI'de ilgili tarifin "Requires Cleanroom" notunu kontrol et.

İlk başlatmadan önce işleme makinelerini kapat veya malzemelerini beklet, sonra odayı hazırla:

1. Kontrolcünün doğru kapak sayılarıyla tam bir yapı bildirdiğini doğrula.
2. Altı bakım sorununun hepsini gider. Bkz. [Multiblok Makineleri: Bakım](./multiblocks_index.md#maintenance).
3. Kapıları kapat ve içerideki hiçbir ekipmanın kirlilik üretmediğinden emin ol.
4. Temiz Odayı sürekli besle ve temizliğin yükselişini izle.
5. %100'de her işleme makinesini kendi enerji beslemesine bağla ve işlemeye başlamak için malzemeleri yerleştir.

Sıradan GT tek bloklu makineleri, temizlik %0'ın üzerine çıktığında Temiz Oda gerektiren tarifleri başlatabilir, ancak çıktıları güvenli garanti edilmez. Yetersiz temizlikten kaynaklanan eşya kaybı **tarif başladığında ve malzemelerini tükettiğinde** belirlenir. İşlemenin yarısında %100'e ulaşmak, kayıp için zaten seçilmiş bir çıktıyı geri kazandıramaz.

%100 temizlik yalnızca çevreden kaynaklanan kayıpları ortadan kaldırır. Doğası gereği olasılıklı çıktıları olan bir tarif yine NEI'de gösterilen şansları kullanır.

Büyük Kimyasal Reaktör ve Yüksek Yoğunluklu Lazer Gravür Makinesi gibi bazı ileri multiblokların Temiz Oda içine yerleştirilmesi gerekmez. **Tüm multiblok makinelerinin yerleşik bir temiz oda çevresi vardır.**

## Temizlik ve Enerji

HV, kontrolcünün kilit açma kademesidir, minimum enerji kademesi değildir. Bir LV Enerji Kapağıyla Temiz Oda başlangıçta **40 EU/t** tüketir. Tüketim temizlik yükseldikçe kademeli olarak azalır ve %100'de **4 EU/t**'ye iner.

40 EU/t, bir LV jeneratörün nominal çıktısını aşar, ancak Temiz Odanın LV Enerji Kapağı 2A kabul edebilir. İlk inşa için iki LV jeneratörü veya sürekli olarak yeterli enerji sağlayabilen başka bir LV beslemesi kullan ve kabloları akıma uygun seç. Tek bir 32 EU/t LV jeneratörü odayı tek başına yüzde 0'dan temizleyemez. Kablo kayıplarını da hesaba kat.

Aşağıdaki örnek **beş blok dış yükseklik, bakım sorunu olmaması, kapalı kapılar ve yüzde 0'dan yüzde 100'e temizlik** varsayar. Süreler 20 TPS'te normal çalışmayı varsayar.

| Enerji Kapağı kademesi | Başlangıç tüketimi | %100'de tüketim | Yaklaşık temizlik süresi |
| --- | --- | --- | --- |
| LV | 40 EU/t | 4 EU/t | 15 dakika |
| MV | 40 EU/t | 4 EU/t | 15 dakika |
| HV | 160 EU/t | 16 EU/t | 7 dakika 30 saniye |
| EV | 640 EU/t | 64 EU/t | 3 dakika 45 saniye |

MV, LV'den daha hızlı temizlemez. HV'den itibaren standart kayıplı hız aşırtma, her hız aşırtmada enerjiyi dörde katlar ve temizlik süresini yarıya indirir. Daha yüksek odaların temizlenmesi daha uzun sürer; yalnızca genişliği veya uzunluğu artırmak temizlik döngüsünü uzatmaz.

**Temiz Odayı ve içindeki işleme makinelerini ayrı ayrı besle.** Temiz Odanın Enerji Kapağı kademesi içerideki makinelerin voltajını sınırlamaz ve onlara hız aşırtma bonusu vermez. Enerji beslemesini boyutlandırırken Temiz Odanın tüketimini tüm işleme makinelerinin tüketimine ekle.

%100'e ulaştıktan sonra odayı çalışır durumda tut. Boştaki enerjisinden tasarruf etmek için kapatma. Kapatma, enerji kesintisi veya bozulmuş yapı sonrasında çevreyi yeniden kur ve işlemeye devam etmeden önce %100 temizliği doğrula.

## Duvarlardan Erişim, Enerji ve Taşıma

### Erişim

Erişim için IC2 Güçlendirilmiş Kapı kullanılır. Açık bir kapı algılandığında Temiz Oda sürekli temizlik kaybeder, normalde her beş saniyede iki puan. Kullandıktan sonra kapıları kapat. Sık erişim için bir kapıyı tekrar tekrar açmamak adına Extra Utilities'in <ItemLink id="ExtraUtilities:etherealglass:0" showIcon="left" /> bloğunu kullan.

Tahta kapılar, vanilla demir kapılar, delikler ve sıradan borular geçerli Temiz Oda duvar blokları değildir. Enerji kabloları veya ME kabloları için boşluk bırakma.

### Duvarlardan Enerji

Duvara uygun kademede bir **GT Makine Gövdesi** veya **Diyot** gömerek dış enerji beslemesini içerideki makine kablolarına bağla. Örneğin bir <ItemLink id="gregtech:gt.blockmachines:13" showIcon="left" /> HV enerjisini duvardan geçirebilir.

Bir Makine Gövdesi enerjiyi ön yüzünden verir ve diğer yüzlerinden enerji alır. Çıkışını içeri doğru çevir ve kabloları iki taraftan bağla. Daha yüksek akım için uygun değerde bir Diyot kullan ve her iki kablo hattının akım kapasitesini kontrol et.

> [!WARNING]
> İç makinelere verilen voltajı yükseltirken duvardaki Makine Gövdelerini, Diyotları ve kabloları da kontrol et. Daha yüksek kademe enerjiyi eski bir düşük kademe porta bağlamak aşırı voltaj patlamasına neden olur. Yalnızca eşya taşıma için kullanılan ve enerji almayan bir gövdenin makinenin voltajıyla yükseltilmesi gerekmez.

### Eşyalar ve Sıvılar

GT Makine Gövdelerinin bir eşya yuvası ve bir sıvı tamponu vardır; bu sayede duvardan geçen aktarım kapları olarak görev yapabilirler. Bu tampona eklemek ve oradan çekmek için iki tarafta borular veya Konveyör Modülleri kullan, sonra içerideki makinelere ulaştır. Gövde tarif işlemez ve her şeyi hedef makinelere otomatik olarak dağıtmaz.

Mümkün olduğunda malzemeler, ürünler ve farklı sıvılar için ayrı portlar kullan; böylece istenmeyen materyaller paylaşılan küçük bir tamponu dolduramaz. İşleme makinelerinin giriş yüzlerini, çıkış yüzlerini ve otomatik çıkışı ayrı ayrı ayarla; duvardaki bir gövde bu ayarların yerini tutmaz.

AE2 ile odanın içinde ve dışında <ItemLink id="appliedenergistics2:tile.BlockWirelessConnector" showIcon="left" /> kullanarak bir bağlantı kur, sonra içerideki ME Arayüzlerini, otobüsleri ve diğer cihazları bağla. Kablosuz Bağlayıcılar duvar konumlarını işgal etmez ve kasa değişim payında daha fazla yer bırakır.

ME ağını beslemek işleme makinelerine GT EU sağlamaz. Makine enerjisini Makine Gövdeleri, Diyotlar veya ayrı yapılandırılmış bir GT EU P2P kurulumu aracılığıyla sağla.

## Bakım, Kirlilik ve İzleme

Çözülmemiş her bakım sorunu maksimum temizliği **10 puan** düşürür. Bir sorun %90'da, iki sorun %80'de sınırlar. Temiz Oda yine de çalışabilir ama güvenli %100'e ulaşamaz. Onarımlardan sonra çevre gerektiren tariflere devam etmeden önce temizliğin toparlanmasını bekle.

> [!WARNING]
> Temiz Odanın içine kirlilik üreten jeneratörler veya başka kirlilik üreten ekipmanlar koyma. İçerideki bir makineden gelen kirlilik temizliği sıfıra indirir ve altı bakım sorununun tamamını tetikleyerek Temiz Odayı durdurur. Bir Egzoz Çıkışı bunu düzeltemez. Kirlilik kaynağını dışarı taşı, sonra onar, yeniden başlat ve odayı tekrar temizle.

Temizliği, bakımı ve çalışmayı kontrol etmek için kontrolcü GUI'sini ve Waila'yı kullan. Bir ışığa veya alarma bağlanmış Endüstriyel Bilgi Paneli ya da Bakım Gerekli Kapağı bakım sorunlarını izlemeye yardımcı olabilir. Bakım sorunu olmaması temizliğin zaten %100 olduğu anlamına gelmez; kapıları açtıktan, enerji kesintilerinden veya yeniden başlatmadan sonra çevreyi kontrol et.

Kontrolcü ayrıca her taraftan temizliği yansıtan bir Kızıltaş sinyali yayar. **%100, sinyal gücü 15'e karşılık gelir.** Malzeme girişini otomatik kontrol etmek için gücü 15 olan sinyali kontrol et. Sıfır olmayan her sinyal yetersizdir, çünkü düşük temizlik de sinyal üretebilir. Yapı kontrolleri ve Kızıltaş güncellemeleri gecikmelidir, bu yüzden herhangi bir interlokla birlikte kapıları kapalı, enerjiyi sabit ve bakımı çözülmüş tut.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Eksik yapı | Dış boyutlar, yatay bakan merkezi bir tavan kontrolcüsü, tavanın iç kısmının tamamında filtreler ve tamamen kapalı duvarlar ile zemin |
| Yanlış kapak sayısı | Tam olarak bir sıradan Enerji Kapağı ve bir Bakım Kapağı; kabukta Giriş Otobüsü, sıvı kapağı veya Egzoz Çıkışı olmamalı |
| Cam veya port ekledikten sonra oda oluşmuyor | Değişimlerin geçerli olup olmadığı, en az 20 Plascrete Bloğu kalıp kalmadığı ve tüm değişimlerin birlikte yüzde sınırını karşılayıp karşılamadığı |
| LV enerjiyle anında kapanma | Yalnızca bir 32 EU/t jeneratörün bağlı olup olmadığı; yeterli sürekli başlangıç enerjisi, kablo akım kapasitesi, kablo kayıpları ve enerji tamponu |
| MV enerji temizliği hızlandırmıyor | MV'nin temizlik hız aşırtması yoktur; daha hızlı temizlik HV'de başlar. Voltajı yükseltmeden önce Enerji Kapağını yükselt ve kabloları sağla |
| Temizlik %90 veya %80'de kalıyor | Çözülmemiş bakım sorunları; temizlik düşmeye devam ediyorsa açık Güçlendirilmiş Kapıları da kontrol et |
| Malzemeler tüketildi ama eşya çıktısı yok | Tarif başladığında temizliğin %100 olup olmadığı; sonra doğal çıktı şanslarını ve makinenin çıkış yapılandırmasını kontrol et |
| İçerideki makine hâlâ Temiz Oda istiyor | Tamamen içeride olup olmadığı, Temiz Odanın oluşmuş ve temizliğinin %0'ın üzerinde olup olmadığı ve yerleştirme veya genişletmeden sonra bir yapı kontrolü yapılıp yapılmadığı |
| Temiz Oda çalışıyor ama içerideki makine çalışmıyor | Makinenin ayrı enerjisi, voltaj, malzemeler, sıvılar, Entegre Devre yapılandırması ve çıkış alanı |
| Temizlik aniden sıfırlanıyor ve tüm bakım sorunları var | İçerideki bir kirlilik kaynağını bulup kaldır, bakımı onar ve yeniden başlat; işleme malzemelerini beklet |

Genel alet kontrolleri, bakım ve enerji kesintisi rehberliği için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Cleanroom](https://wiki.gtnewhorizons.com/wiki/Cleanroom)