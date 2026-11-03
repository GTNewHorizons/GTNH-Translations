---
item_ids:
  - Thaumcraft:ItemThaumometer
  - Thaumcraft:ItemInkwell
  - Thaumcraft:ItemResource:9
navigation:
  title: Aspektler, Tarama ve Araştırma
  parent: ./index.md
  icon: 'Thaumcraft:ItemResearchNotes'
  position: 80
---

# Aspektler, Tarama ve Araştırma

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Thaumcraft'te araştırma dünyayı anlamakla başlar. Tarama, eşyalarda, yaratıklarda ve düğümlerde bulunan <Color color="#B7A0D6">Aspektleri</Color> ortaya çıkarır; bu da Araştırma Puanları ve ipuçları kazandırır;<br>Araştırma Masası daha sonra bu keşifleri Aspektleri birleştirmek ve Araştırma Notları üzerinde çalışmak için kullanır ve sonunda bunları Thaumonomicon'daki bilgiye dönüştürür.

Araştırmanın en çok karıştırılan kısımları **Aspektleri keşfetmek, Araştırma Puanı kazanmak ve araştırmayı tamamlamaktır**. Bu sayfa bu gereksinimleri ve NH'nin sağladığı tarama ile araştırma kolaylıklarını açıklar.

## Aspekt Sistemi ve Bileşimi

**Aspektler** hem nesnelerin büyülü özelliklerini hem de araştırmada kullanılan kategorileri tanımlar. Altı İlkel Aspekt tüm sistemin temelini oluşturur, her Bileşik Aspekt ise iki Aspektten oluşur;<br>bu bileşen Aspektlerin kendisi de Bileşik Aspekt olabilir ve böylece katman katman açılan bir ilişkiler ağı ortaya çıkar.

Altı İlkel Aspekt şunlardır: <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Hava (Aer), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Toprak (Terra), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Ateş (Ignis), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Su (Aqua), <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Düzen (Ordo) ve <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" />Entropi (Perditio).

| Bileşik Aspekt | Bileşen Aspektleri |
| --- | --- |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"lux"}' scale="0.75" />Işık (Lux) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Hava + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ignis"}' scale="0.75" />Ateş |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"motus"}' scale="0.75" />Hareket (Motus) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aer"}' scale="0.75" />Hava + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"ordo"}' scale="0.75" />Düzen |
| <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"victus"}' scale="0.75" />Yaşam (Victus) | <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"terra"}' scale="0.75" />Toprak + <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"aqua"}' scale="0.75" />Su |

**Bir Aspektin bileşimi ile bir eşyanın Aspekt içeriği iki farklı bilgi türüdür.** "Yaşam Toprak ve Su'dan oluşur" araştırmada kullanılan bir ilişkiyi tanımlar; "bir eşya Yaşam içerir" ise o eşyanın özelliklerini tanımlar. İkincisi tarama ödüllerini ve Esans üretiminde malzeme seçimini etkiler, ancak Araştırma Masasının Araştırma Puanı üretmek için eşyayı doğrudan tükettiği anlamına gelmez.

Aynı şekilde, Araştırma Masasında Toprak ile Su'yu birleştirmek Yaşam Araştırma Puanı üretirken, Yaşam içeren bir eşyayı Simya Fırınında işlemek Yaşam Esansı üretir. İkisi de aynı Aspekt simgesini kullanır, ancak kaynaklar farklı yerlerde depolanır ve farklı amaçlara hizmet eder.

NH'nin eklentileri de Aspektler ekler. Yeni bir Aspekt keşfederken adını, bileşimini ve gerçek kaynaklarını göz önünde bulundur; orijinal modun wiki'sinde listelenen Aspekt sayısı mevcut mod paketinin toplamı olarak görülmemelidir.

## Tarama Ne Sağlar

<ItemLink id="Thaumcraft:ItemThaumometer" showIcon="left" /> eşyaların, blokların, yaratıkların ve Aura Düğümlerinin büyülü özelliklerini gözlemlemek için kullanılır. Tarama üç ana ödül türü sağlar:

|  |  |
| --- | --- |
| Bir nesnenin Aspektlerini keşfetmek | Nesnenin içerdiği Aspektleri ve miktarlarını ortaya çıkarır, daha önce bilinmeyen Aspektleri açığa çıkarabilir |
| Araştırma Puanları | Oyuncu için Aspekt bazında kaydedilir ve Araştırma Masasında harcanmaya hazırdır |
| Araştırma ipuçları | Belirli nesneler gizli araştırmaları açığa çıkarabilir ve Thaumonomicon'da mevcut araştırmaları genişletir |

Bu üç ödül birbirinin aynısı değildir. Aspektlerini zaten bildiğin yeni bir eşyayı taramak yine de Araştırma Puanlarını yenileyebilir; gizli araştırma için belirli bir nesneyi taramak ise araştırma ipuçlarına odaklanır.

**Tarama, gözlemlenen eşyayı tüketmez veya Esansa ayrıştırmaz.** Sıradan eşyaları taramak ve malzemeleri Simya Fırınında işlemek sırasıyla bilgi edinme ve büyülü kaynak üretme yollarıdır.

Tarama kayıtları ve Araştırma Puanları oyuncunun araştırma verisinin parçasıdır. Bir nesne türü bir kez tarandıktan sonra tekrar tekrar taranması sınırsız puan sağlayamaz.

## Dünya, Envanter ve Kap Taraması

Dünyadaki bloklar, düşen eşyalar ve yaratıklar bir Thaumometre tutarken gözlemlenebilir. NH ayrıca Araştırma Puanı kazanmayı kolaylaştırmak için envanter ve kap taraması sağlar.

 - Dünya taraması | Thaumometreyi dünyadaki geçerli bir nesneye doğrult ve gözlemlemeye devam et
 - Envanter taraması | Thaumometreyi imleçte tut ve bir envanterdeki veya kaptaki eşya yuvasının üzerine gel
 - Kap taraması | Kap taraması araştırmasını tamamladıktan sonra Thaumometreyi bir kapta kullan

Kap taraması araştırması Thaumonomicon'un Temel Bilgiler kategorisindedir ve Ayrıştırma Masası araştırmasını gerektirir; kap taraması araştırmasının kendisi de tamamlanmalıdır.<br>
NH'nin "Tarama Çok Kolay" görevi bu iki kolaylığı tanıtır. Kap taraması eğilip sağ tıklama ile kullanılır; sandık bloğunun kendisini taramak ile içindeki eşyaları taramak da ayrı ayrı anlaşılmalıdır.<br>

Envanter taraması her arayüzdeki her yuvada çalışmaz. Örneğin AE2'de depolama hücrelerini taramak başka bir eşya gerektirir: <ItemLink id="thaumicenergistics:cell.microscope" showIcon="left" />

## Bilinmeyen Aspektler ve Tarama Gereksinimleri

Thaumometre bir şeyi anlayamadığını söylediğinde yaygın bir neden, nesnenin henüz keşfetmediğin bir Bileşik Aspekt içermesidir.<br>İlgili nesneyi anlamak için o Aspekti veya iki bileşen Aspektinin ikisini de bilmen gerekir.<br>Karmaşık nesneler aynı anda birkaç Bileşik Aspekt içerebilir, bu yüzden bir taramanın başarılı olup olmaması hangi Aspektlerin keşfedildiğine bağlıdır.

Araştırma Masasında Aspektleri birleştirmek yeni Bileşik Aspektleri keşfetmenin başka bir yoludur. Doğru bir birleşim oyuncunun yeni Aspekti keşfetmesini ve biraz Araştırma Puanı kazanmasını sağlar; bu aynı zamanda anlayıp tarayabileceği nesne yelpazesini genişletir.

> [!NOTE]
> Her Aspekt çifti geçerli bir birleşim oluşturmaz. Geçersiz bir birleşim denemek de Araştırma Puanı tüketir, bu yüzden araştırma kaynaklarını tekrar tekrar tahmin yürüterek harcamamak için önce Aspekt ilişkileri hakkındaki bilinen bilgilere başvur.

Nesneleri tarama sıran bu yüzden ilerlemeni etkiler. "Artık Ne Tarayacağımı Söyle!" görevi referans olarak taranacak bir dizi nesne sunar.

## Eşya Aspektleri ve NEI Sorguları

Taranmış eşyaların Aspektleri ve miktarları ipuçlarında görüntülenebilir. Varsayılan olarak bu bilgiyi göstermek için eğilme tuşunu (genellikle Shift) basılı tut.<br>Bilinmeyen simgeler, keşfedilmiş Aspektler ve belirli miktarlar farklı keşif durumlarını ve Aspekt miktarlarını belirtir.

GTNH'de NEI, taranmış eşyaların Aspektlerini, Aspekt birleşimlerini, belirli bir Aspekti içeren eşyaları ve Gizemli, Simya ve İnfüzyon tarifi sorgularını görüntüleyebilir. Bu, seri Esans üretimi için kaynak bulmakta kullanışlıdır.

## Araştırma Puanlarının Kaynakları ve Kullanımları

<Color color="#B7A0D6">Araştırma Puanları</Color> her Aspekt için ayrı ayrı kaydedilir. Araştırma Masasındaki sayılar oyuncunun kullanabileceği araştırma kaynaklarını gösterir.<br>Bir Bileşik Aspekt zaten keşfedilmiş olsa bile Araştırma Puanları tükendiğinde bağlantı oluşturmak için yerleştirilemez.

| Kaynak | Sağladığı | Sınırlar ve Özellikler |
| --- | --- | --- |
| Yeni geçerli bir nesneyi taramak | Nesnedeki Aspektler için Araştırma Puanı; bir Aspekti ilk kez keşfetmek ek ödüller verir | Zaten taranmış bir nesne türü tekrar tekrar puan sağlayamaz |
| Araştırma Masasında Aspektleri birleştirmek | İlgili Bileşik Aspekt için Araştırma Puanı | Her iki bileşen Aspektten de Araştırma Puanı tüketir; kaynakları bedavaya üretmez |
| Bilgi Parçaları | Kullanıldığında her İlkel Aspekte 1–2 puan ekler | Elde edilmesi zor ve kullanımda tüketilir |
| Ayrıştırma Masası | İlkel Aspekt Araştırma Puanı elde etmek için eşyaları tüketir | Bileşik Aspektler ayrıştırılır; çıktı yavaştır ve başarı şansı düşüktür |
| Araştırma Masasındaki çevre bonusları | Çevre tarafından üretilen küçük miktarda bonus Araştırma Puanı | Yavaş elde edilir ve istikrarlı bir Araştırma Puanı kaynağının yerini alamaz |

**Bilgi Parçaları** hem temel araştırma kaynaklarını doldurabilir hem de kayıp bilginin keşfedilmesine yardımcı olabilir. Bu iki kullanım ayrı ayrı anlaşılmalıdır; özel araştırma ararken Thaumonomicon'daki Bilgi Parçaları girdisine başvur.

Varsayılan olarak NH, taramadan kazanılan Araştırma Puanlarına yumuşak bir üst sınır uygular: oyuncu bir Aspekte 500 Araştırma Puanına ulaştığında daha fazla tarama o Aspekt için daha az puan verir.

Araştırma Puanları esas olarak notlara Aspekt yerleştirmek, Bileşik Aspektleri birleştirmek ve araştırmayı çoğaltmak için kullanılır. Çok sayıda Bileşik Aspekt kullanırken bileşen Aspektlerinin rezervlerini de izle; sonunda yalnızca tek tür Araştırma Puanıyla kalıp ihtiyaç duyduğun diğerlerini dolduramamak istemezsin.

## Araştırma Masası, Araştırma Notları ve Yazı Araçları

<ItemLink id="Thaumcraft:ItemThaumonomicon" showIcon="left" /> mevcut araştırma yollarını gösterir, Araştırma Masası notları ve Aspektleri işler, <ItemLink id="Thaumcraft:ItemInkwell" showIcon="left" /> ise yazmak için gereken kalem ve mürekkebi sağlar.

| İçerik | Amaç |
| --- | --- |
| Thaumonomicon'daki araştırma girdileri | Ön koşulları görüntüle, mevcut araştırmalar için not al ve açılmış bilgiyi oku |
| Tamamlanmamış Araştırma Notları | Bir araştırma projesinin konusunu ve bağlanması gereken Aspektleri kaydeder |
| Araştırma Masası | Aspektleri birleştir, notlar üzerinde çalış ve açılmış araştırma yardım özelliklerini kullan |
| Yazı Araçları | Not almak ve Araştırma Masasında yazmak için kullanılır; mürekkep tüketilir |
| Tamamlanmış araştırma | Okunduğunda ilgili araştırmayı oyuncunun bilgi ilerlemesine ekler |

Hem Araştırma Notları edinmek hem de Araştırma Masasında yazmak Yazı Araçları gerektirir. İki set yapman önerilir; biri not almak, diğeri Aspektleri bağlamak için.<br>
**GTNH araştırmayı Zor ayarına kilitler, bu yüzden sıradan araştırma girdileri de tamamlanmak için not gerektirir.**

Thaumcraft Research Tweaks, Araştırma Masası arayüzünü değiştirir. Aspektler sürükle-bırak ile veya sürüklerken sağ tıklama kullanılarak birleştirilebilir; ilgili yöntemler notlardaki yuvalara Aspekt yazmak için de kullanılır.<br>
Thaumonomicon'daki araştırma talimatları bu arayüz özelliklerini kapsayacak şekilde güncellenmiştir. Okurken mevcut arayüze başvur.

## Araştırma Notları için Bağlantı Kuralları

Notlar, Aspektler arasındaki ilişkileri temsil etmek için altıgen bir ızgara kullanır. Bunları tamamlamak için verilen tüm Aspektleri geçerli bağlantılarla tek bir bağlı bütün haline getir.

Bir Bileşik Aspekt bileşen Aspektlerine bağlanabilir ve bir bileşen Aspekt de onu içeren Bileşik Aspektlere bağlanabilir. Benzer adlar, benzer simge renkleri veya ikisinin de bir İlkel Aspekte dayanması otomatik olarak doğrudan bir bağlantı oluşturmaz.

Örneğin Toprak ve Su, ikisi de temel Aspekt olduğu için doğrudan bir ilişkiye sahip değildir, ancak Yaşam Toprak ve Su'dan oluşur, bu yüzden "Toprak—Yaşam—Su" iki geçerli ilişkiyi temsil eder.<br>Başka bir örnek Işık ve Hareket'tir; ikisinin de bileşiminde Hava bulunur, "Işık—Hava—Hareket" onları ortak bileşen Aspektleri üzerinden bağlar.

Hem bileşim hem de konum gereksinimleri karşılanmalıdır: yalnızca geçerli bir ilişkiye sahip bitişik Aspektler birbirine bağlanabilir.

Bir Aspekt yerleştirmek karşılık gelen Araştırma Puanlarını tüketirken yazmak ve değişiklik yapmak da mürekkep tüketir. Normalde yanlış yerleştirilmiş bir Aspekti kaldırmak Araştırma Puanlarını iade etmez; Araştırma Uzmanlığı ve Araştırma Ustalığı bunları geri kazanma şansı verir.

Notların tüm parçaları bağlandığında tamamlanmış araştırmaya dönüşürler. **Bağlantıları tamamladıktan sonra ilgili araştırmayı açmak için sonucu okumalısın.**

## Araştırma Ön Koşulları ve Gizli Bilgi

Thaumonomicon'daki bağlantılar araştırma girdileri arasındaki ön koşul ilişkilerini gösterir, ancak tek bir bağlantı her gereksinimi göstermek zorunda değildir.<br>
Bazı içerik ayrıca belirli taramalar, önceki keşifler, Delilikle ilgili olaylar veya diğer modlardaki araştırma ilerlemesini gerektirir.

> [!WARNING]
> <Color color="#D5B77A">Yasak Bilgi</Color> olarak işaretlenmiş araştırmayı okumak Delilik ekler. Tehlike düzeyi eklenen Deliliğin türünü ve miktarını belirtir.

## <ItemLink id="gregtech:gt.blockmachines:13001" showIcon="left" />

**<ItemLink id="gregtech:gt.blockmachines:13001" showIcon="left" />** Araştırma Notlarını tamamlamanın başka bir yolunu sunar ve Aspektleri bağlama işini elle yapmak yerine bir makinenin yapmasını sağlar.<br>
Teknoloji ile büyüyü bir araya getiren bir tesistir; ilgili araştırmayı ve malzemeleri gerektirir.<br>
Makine EU tüketir ve yapısındaki düğümleri kendisine verilen Araştırma Notlarını tamamlamak için kullanır.

> [!WARNING]
> Araştırma Tamamlayıcısı işlem için kullanılan düğümleri tüketir.

Araştırma yardım tesisleri tekrarlayan işleri azaltır, ancak her birinin kendi maliyetleri ve gereksinimleri vardır.

## Sık Sorulan Sorular

| Belirti | Neye Bakmalı |
| --- | --- |
| Thaumometre bir nesneyi anlayamıyor | Aspektlerinden hangilerinin keşfedildiğini, özellikle bilinmeyen Bileşik Aspektleri ve bileşenlerini kontrol et |
| Aynı tür eşyayı tekrar tekrar taramak yeni puan vermiyor | O nesne türü zaten taranmış olabilir; aynı eşyaların sayısını artırmak yeni bir keşif yaratmaz |
| Yeni bir tarama eşyanın Aspekt miktarlarından daha az puan veriyor | Bir Aspekteki yüksek Araştırma Puanı rezervi tarama ödüllerindeki yumuşak üst sınırı tetikler |
| Envanter taraması yanıt vermiyor | Thaumometrenin imleçte tutulduğundan, yeterince uzun beklediğinden ve hedefin sıradan geçerli bir envanter yuvası olduğundan emin ol |
| Tek tek eşyalar taranabiliyor ama sandığın tamamı taranamıyor | Kap taraması araştırmasının tamamlandığını kontrol et ve sandık bloğunu içindeki eşyalardan ayır |
| Bir Aspekt biliniyor ama notlara yerleştirilemiyor | O Aspekt için kalan Araştırma Puanlarını, Yazı Araçlarını ve hedef yuvanın durumunu kontrol et |
| Aspektleri birleştirmek İlkel Araştırma Puanlarını azaltıyor | Birleştirme bileşen Aspektleri tüketir; geçersiz birleşimler de puan harcayabilir |
| Bitişik simgeler bağlanmıyor | Doğrudan bir bileşim ilişkisi gerekir; yalnızca adlar veya simgeler bunu değerlendirmek için yeterli değildir |
| Araştırma Notları tamamlandı ama Thaumonomicon girdisi kilitli kalıyor | Tamamlanmış araştırmanın okunup okunmadığını kontrol et |
| NEI bir Aspekt için kaynak göstermiyor | Sorgular tarama ve keşif ilerlemesinden etkilenir; liste olası her kaynağı temsil etmez |

</Column>