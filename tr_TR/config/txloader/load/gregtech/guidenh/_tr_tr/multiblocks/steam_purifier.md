---
item_ids:
  - gregtech:gt.blockmachines:31082
quest_ids:
  - zorY0c3BQuqLJp7ThOLG-g
navigation:
  title: Buhar Temizleyici
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31082
  position: -501
---
# Buhar Temizleyici
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok cevher yıkama makinesidir. Buhar ve su kullanarak cevherleri gruplar hâlinde işler ve aynı tarifin aynı anda sekiz kopyasına kadar işleyebilir. **Cevher Yıkayıcı** ve **Basit Yıkayıcı** modları, yan ürünleri toplamak ile hızlı yıkamak arasında seçim yapmanı sağlar.

Makine, aynı Kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapılara sahiptir. Ezilmiş Cevherleri yıkamayı Buhar çağında kullanılabilir hâle getirir; Basit Yıkayıcı modu ayrıca uygun Kirlenmiş Tozları ve Temizlenmiş Tozları hızlıca yıkayabilir. Yüksek basınçlı yapıya yükseltmek işlem kapasitesini artırır ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; Kontrolcü tarifi Dökme Demir Plakalar, Kalay Rotorlar, bir Tumbaga Çerçeve ve diğer malzemeler gerektirir |
| Boyutlar | Dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde; Kontrolcü küçük küpün ikinci katmanının ön merkezinde |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Cevher Yıkayıcı ya da Basit Toz Yıkayıcı tarifleri; 32 EU/t'den fazlasını gerektirmez |
| Girdiler ve çıktılar | Buhar Giriş Yolları eşya kabul eder, Girdi Kapakları tarif suyunu kabul eder ve Buhar Çıkış Yolları eşya çıkarır |
| Çalışma modları | Varsayılan olarak Cevher Yıkayıcı modundadır; tornavida veya GUI ile Basit Yıkayıcı moduna geç |
| Paraleller | Aynı tarifin sekiz kopyasına kadar; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı veya yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı Hızı ve Buhar tüketim oranını ikiye katlar; Gerilim hız aşırtması yok |
| Bakım ve Kirlilik | Bakım yok, Kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31082" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki kurulum bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Girdi Kapağı kullanır. Temel yapı bronz bileşenler kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları ve Boru Muhafazaları hepsi aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan kurulumda 59; aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az 55 gerçek Kasa kalmalıdır |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz; tankın tabanında, merkezî kasanın etrafında |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | 12; tankın içindeki Boruları ve üstteki bağlantı Borularını oluşturur |
| Cam | Örneğin, <ItemLink id="minecraft:glass" showIcon="left" /> | Mevcut cam yeniden kullanılabilir | 24; tank duvarlarının iki katmanını oluşturur; hologramın kabul ettiği cam bloklarını kullan |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" /> | Aynı Kontrolcü | Bir; küçük küpün ikinci katmanının ön merkezinde |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir; bir Kasanın yerine geçer |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir; bir Kasanın yerine geçer |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir; bir Kasanın yerine geçer |
| Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | En az bir; bir Kasanın yerine geçer ve Su sağlar |

Yapıda kasalar veya kapaklar için 63 konum vardır. Yukarıda listelenen dört arayüzün takılması 59 Kasa bırakır. Girdi Kapakları veya yollar eklemek Kasa sayısını buna göre azaltır, ancak en az 55 gerçek Kasa kalmalıdır. Kapaklar ve yollar Dişli Kutusu Kasalarının, Boru Muhafazalarının veya camın yerini alamaz.

Katmanları tabandan yukarı doğru say. Yapı, küçük bir küp, yanındaki bir cam tank ve üstteki Borulardan oluşur. Kontrolcü, dokuz blok genişliğindeki tüm yapının merkezinde değildir. Etkileşimli yapıyı veya hologramı takip et. Kontrolcü yalnızca yatay olarak bakabilir ve yapı ön yüzü etrafında döndürülemez; hologramdaki boş konumların doldurulması gerekmez.

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullanarak yapıyı önizle ve inşa etmeye yardımcı ol. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

### Tank Suyu ve Tarif Suyu

Buhar, yapının tankındaki Su ve tarif Suyu farklı amaçlara hizmet eder:

| Konum | Amaç |
| --- | --- |
| Buhar Kapağı | Harici bir Kazan tarafından üretilen Buharı makineye güç sağlamak için alır |
| Girdi Kapağı | Normal Suyu veya tarifin gerektirdiği Damıtılmış Suyu alır; her tarif Suyunu buradan tüketir |
| Yapının tankı | İkinci katmanda merkezî Boru Muhafazasının etrafındaki sekiz Su konumu; Su kaynaklarını elle yerleştir veya makinenin doldurmasına izin ver |

Boru Muhafazasını tankın merkezinde tut. Etraftaki sekiz Su konumu başlangıçta boş bırakılabilir. Tankı kontrol ederken makine, bir Su kaynağı bloğu yerleştirmek için Girdi Kapaklarından her seferinde **1,000 L normal Su** alır. Sekiz konumun tamamı boşsa ilk dolum **8,000 L ek normal Su** tüketebilir. Bu, mevcut döngünün tarif Suyundan ayrıdır; bu nedenle başlamadan önce yeterli tampon sağla.

Sekiz konumun tamamını elle doldurmak için Su kovalarını da kullanabilirsin. **Tanka yerleştirilen Su, Girdi Kapaklarındaki tarif Suyunun yerini tutmaz.** Tank dolduktan sonra Girdi Kapaklarına besleme yapmaya devam et. Tank Suyu her tarif tarafından tüketilmez, ancak bir kaynak kaldırılırsa makine daha sonraki bir kontrolde onu yeniden doldurmayı dener. Yapı kontrolü Su kaynaklarını veya Havayı kabul eder; akan Su kaynak bloklarının yerini tutamaz.

Cevher Yıkayıcı modu Damıtılmış Su tarifleri içerir, ancak boş bir tankın otomatik doldurulması yalnızca **normal Su** kullanır. Damıtılmış Su ile yıkamadan önce tankı kovalarla doldur veya otomatik doldurma için normal Su içeren ek bir Girdi Kapağı tak.

## Makine Kullanımları

### İki Yıkama Modu

Cevher Yıkayıcı ve Basit Yıkayıcı modları arasında geçiş yapmak için <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> ile Kontrolcüye <kbd>sağ tık</kbd> yap veya GUI'deki mod düğmesine tıkla.

| Özellik | Cevher Yıkayıcı modu | Basit Yıkayıcı modu |
| --- | --- | --- |
| Tarif haritası | NEI'deki Cevher Yıkayıcı tarifleri | NEI'deki Basit Toz Yıkayıcı tarifleri |
| Yaygın girdiler | Ezilmiş Cevherler ve diğer uygun cevher ara ürünleri | Uygun Ezilmiş Cevherler, Kirlenmiş Tozlar ve Temizlenmiş Tozlar |
| Yaygın ana çıktılar | Ezilmiş Cevherler Temizlenmiş Ezilmiş Cevherlere dönüşür | Ezilmiş Cevherler Temizlenmiş Ezilmiş Cevherlere dönüşür; Kirlenmiş Tozlar ve Temizlenmiş Tozlar normal tozlara dönüşür |
| Yan ürünler | Tarifte listelenen Taş Tozunu ve cevher yan ürünlerini toplar; bazı çıktılar şansa bağlıdır | Yalnızca temizlenmiş ana ürünü üretir; cevher yıkama veya santrifüjleme yan ürünleri olmaz |
| Tarif başına tipik Su | 1,000 L normal Su veya 200 L Damıtılmış Su; ilgili NEI tarifini kontrol et | 100 L normal Su |
| NEI'de gösterilen tipik süre | Normal Su ile 25 saniye veya Damıtılmış Su ile 15 saniye; tek tek tarifler farklılık gösterebilir | Beş tick veya normal 20 TPS'de 0,25 saniye |

Cevher yan ürünlerine ihtiyacın olduğunda Cevher Yıkayıcı modunu seç ve her ürün için çıkış alanı bırak. Yalnızca ana ürüne hızlıca ihtiyacın olduğunda Basit Yıkayıcı modunu seç. Basit yıkama hızlıdır ve az Su kullanır; yan ürünlerini atlamaya karar verdiğin malzemeleri toplu işlemek için uygundur.

Kirlenmiş Tozlar ve Temizlenmiş Tozlar için [Buhar Ayırıcı](./steam_seperator.md) tariflerini de kontrol et. Santrifüjleme, normal toz üretirken genellikle karşılık gelen yan ürünleri geri kazanabilir; basit yıkama ise bu yan ürünleri atlar. İşleme rotasını belirli cevherin NEI tariflerini kullanarak seç.

> [!WARNING]
> Basit Yıkayıcı modu, normal cevher yıkama veya santrifüjlemeden gelen yan ürünleri üretmez. Cevher Yıkayıcı moduna geri dönmek, Basit Yıkayıcı modunda zaten işlenmiş eşyalardan bu yan ürünleri geri kazanamaz. Yan ürünlerine ihtiyacın olan cevherleri işlemeden önce mevcut modu kontrol et.

### Cevher İşleme Rotaları

Ezilmiş Cevher yıkamak genellikle her üretim tarifine hazır normal toz yerine **Temizlenmiş Ezilmiş Cevher** üretir. NEI'de sonraki öğütme, santrifüjleme veya diğer işleme adımlarını seç ve eşyaları adlarına ve biçimlerine göre yönlendir.

- **Yan ürünleri topla:** Ezilmiş Cevheri Cevher Yıkayıcı moduna gönder, Temizlenmiş Ezilmiş Cevheri, Taş Tozunu ve cevher yan ürünlerini ayrı ayrı topla, ardından sonraki işlemeyi düzenle.
- **Hızlı yıka:** Uygun Ezilmiş Cevheri Basit Yıkayıcı moduna gönder ve yalnızca Temizlenmiş Ezilmiş Cevheri topla.
- **Cevher tozlarını hızlıca temizle:** Normal toz elde etmek için uygun Kirlenmiş Tozu veya Temizlenmiş Tozu Basit Yıkayıcı moduna gönder. Karşılık gelen yan ürünlerine ihtiyacın varsa bunun yerine santrifüjleme kullan.

Her malzeme veya cevher biçiminin bir Basit Toz Yıkayıcı tarifi yoktur. Temizlenmiş Ezilmiş Cevher ve Temizlenmiş Toz farklı eşyalardır. Bir eşyanın adında "Temizlenmiş" geçmesi, Basit Yıkayıcı modunda yeniden işlenebileceği anlamına gelmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, Buhar Giriş Yolu, Buhar Çıkış Yolu ve Girdi Kapağının takılı olduğunu doğrula.
2. Buhar Kapağına Buhar, Girdi Kapağına Su sağlamak için ayrı hatlar kullan. Tank boşsa önce otomatik doldurma için yeterli normal Su tamponla.
3. İstediğin modu seç ve NEI'de karşılık gelen tarif haritasını, girdi biçimini, Su türünü ve tüm çıktıları kontrol et.
4. Her çıktı için alan bırak, ardından az miktarda malzemeyle başla ve tankı, çıktıları, Buhar tamponunu ve Girdi Kapağı içeriğini gözlemle.
5. Sürekli Buhar ve Su beslemesini ve çıktı toplamayı doğruladıktan sonra girdi miktarlarını ve paralel sayısını artır.

> [!NOTE]
> Mevcut sürümde makine, ilk çalıştırması sırasında veya periyodik bir tank kontrolünde kısa süreliğine "Su Yok" gösterebilir. Kontrolden sonra bir sonraki tarif kontrolünde tekrar deneyecektir. Girdi Kapağındaki Suyu ve tanktaki kaynak bloklarını doğrula, ardından bekle ve gözlemle. Hâlâ çalışamıyorsa aşağıdaki sorun giderme bölümünü kullan.

## Buhar Beslemesi, Su Beslemesi ve İşlem Kapasitesi

Buhar Temizleyici aynı anda **aynı tarifin** sekiz kopyasına kadar işleyebilir. Bu, bir döngüde sekiz farklı cevheri işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, tarif Suyuna, çıkış alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı, NEI'de gösterilen tarif süresinin yaklaşık 1,6 katı sürerken yüksek basınçlı yapı yaklaşık 0,8 katı sürer. 25 saniye olarak gösterilen tipik bir normal Su yıkama tarifi, temel yapıda yaklaşık 40 saniye veya yüksek basınçlı yapıda 20 saniye sürer. Beş tick olarak gösterilen bir Basit Toz Yıkayıcı tarifi, temel yapıda yaklaşık sekiz tick veya yüksek basınçlı yapıda dört tick sürer. Gerçek sürekli işlem kapasitesi ayrıca tarif kontrollerine, girdi beslemesine ve çıktı işlemeye bağlıdır.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel sayısı | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısı için Buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam Buhar tüketimi | Temel değer | Temel yapıyla yaklaşık aynı |
| Tarif başına Su | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Paraleller, bir döngüde işlenen tarif sayısını artırır ancak döngü süresini paralel sayısına bölmez. Sekiz paralelde tipik bir normal Su yıkama döngüsü **8,000 L Su**, bir Damıtılmış Su döngüsü **1,600 L Damıtılmış Su** ve basit bir yıkama döngüsü **800 L Su** gerektirir. Başlangıçta tank hâlâ otomatik doldurma gerektiriyorsa bunun için ayrıca ek normal Su sağla.

Basit Yıkayıcı modu tarif başına az Su kullanır ancak hızlı işler; bu nedenle Girdi Kapağı tamponu ve Su Boruları yine de darboğaz olabilir. Yüksek basınç yükseltmesi tarif başına Suyu azaltmaz. İşlem Hızı iki katına çıktığında sürekli üretim daha yüksek bir Su besleme oranı da gerektirir.

Buhar Kapağı 64,000 L Buhar tamponlar, ancak bu yalnızca geçici eksiklikleri kapatır ve sürekli Kazan üretiminin yerini tutamaz. Kazanları ve Boruları işlem sırasındaki Buhar tüketim oranına göre boyutlandır ve ayrıca Girdi Kapağının Su beslemesinin yetişip yetişmediğini izle.

Çalışma sırasındaki Buhar tüketim oranını kontrol etmek ve sürekli işleme sırasında tamponun düşmeye devam edip etmediğini izlemek için Waila'yı kullan. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru işlem kapasitesini karşılaştırırken eşleşen birimleri kullan. Buhar veya Su beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından Kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında Buhar biterse mevcut işlem iptal edilir ve hâlihazırda tüketilen malzemeler geri verilmez. Yüksek basınçlı yapıya yükseltmeden veya paralel sınırını artırmadan önce Buhar üretimini ve Boru işlem kapasitesini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve Kontrolcüyü korur. Tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları ve Çelik Boru Muhafazaları ile **tüm** Bronz Kaplamalı Tuğlaları, Bronz Dişli Kutusu Kasalarını ve Bronz Boru Muhafazalarını değiştir. Cam, bronz ile çelik kademe kontrolüne katılmaz; bu nedenle mevcut normal cam yeniden kullanılabilir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve Buhar, Su ve üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç, makinenin yapı kademesidir. Hâlâ normal Buhar kullanır ve mevcut Buhar Kapağı, Buhar yolları ve Girdi Kapakları yeniden kullanılabilir. Yükseltme Hızı ve Buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek kademeli tarifler kullanılamaz.

## Otomasyon ve Çıktı Yönlendirme

Buhar Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Cevherleri Giriş Yolunun ön yüzüne göndermek için Huniler, GT eşya Boruları, konveyörler veya eşya kanalları kullan. Ezilmiş Cevher, Kirlenmiş Toz ve Temizlenmiş Toz gibi biçimlere göre filtrele.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek ve ardından ürünleri ana çıktı depolamasına, yan ürün depolamasına veya sonraki makineye yönlendir.
- **Buhar ve Su:** Ayrı hatlar kullan; Buharı Buhar Kapağına, Suyu Girdi Kapaklarına bağla. Damıtılmış Su ile yıkama ve tankı normal Su ile doldurma için ayrı tamponlar ve arayüzler düzenle.
- **Yan ürünler:** Cevher Yıkayıcı modunda ana çıktının yanı sıra Taş Tozunu ve cevher yan ürünlerini de ele al. Yalnızca ana çıktıyı filtrelemek, diğer eşyaların yolda birikmesine neden olur.
- **Mod değişiklikleri:** Malzeme girişini durdur ve mevcut işlemin bitmesini bekle. Transferi sürdürmeden önce modu ve kalan girdileri kontrol et; böylece sonraki malzemeler istemeden diğer rotadan işlenmez.

Cevher yıkama tarifleri aynı anda birkaç farklı eşya üretebilir. Dört yuvalı tek bir Çıkış Yolu, sürekli işleme sırasında tüm ürünleri tutamayabilir. Ek Çıkış Yolları çıkış alanını genişletir ancak paralel sınırını artırmaz. Kapak veya yol eklerken en az 55 gerçek Kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin yok etme modunu "Yok Etme" olarak ayarla ve her çıktı için alan sağla. Eşya yok etme etkinse çıktı tıkandığında ana ürünler veya yan ürünler atılabilir.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yapı | Yapı dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde mi? Kontrolcü küçük küpün ikinci katmanının ön merkezinde mi? Borular, Dişli Kutusu Kasaları, cam ve Su konumları hologramda gösterildiği gibi mi düzenlenmiş? |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutusu Kasaları ve Boru Muhafazaları hepsi aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik kapak veya yol | Tam olarak bir Buhar Kapağı ve en az bir Buhar Giriş Yolu, Buhar Çıkış Yolu ve Girdi Kapağı var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapak ekledikten sonra yapı başarısız oluyor | En az 55 gerçek Kasa kaldı mı? Cam, Dişli Kutusu Kasaları veya Boru Muhafazaları kapaklarla mı değiştirildi? |
| Tank otomatik dolmuyor | Girdi Kapağında normal Su var mı? Her boş Su konumu 1,000 L gerektirir. Yalnızca Damıtılmış Su tankı otomatik dolduramaz; ayrıca kovalarla kaynak blokları yerleştirebilirsin. |
| Tankta Su var ancak işlem başlamıyor | Girdi Kapağı hâlâ tarifin gerektirdiği Suyu içeriyor mu? Tank Suyu tarif Suyunun yerini tutamaz. Kaynaklar yerine yalnızca akan Su blokları mı var? |
| Kısa süreli "Su Yok" mesajı | Makine ilk veya periyodik tank kontrolünü yapıyor olabilir. Su miktarlarını doğrula ve bir sonraki tarif kontrolünü bekle. Hâlâ çalışamıyorsa modu, tarifi ve yapıyı kontrol et. |
| Cevherler var ancak tarif bulunamıyor | Doğru Cevher Yıkayıcı veya Basit Yıkayıcı modu seçili mi? Karşılık gelen bir tarif var mı? Temizlenmiş Ezilmiş Cevher ile Temizlenmiş Toz karıştırıldı mı? Girdi Su türü doğru mu? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Taş Tozu veya cevher yan ürünü yok | Basit Yıkayıcı modu mu seçili? Yan ürünler şansa bağlı mı? Eşya yok etme etkin mi? Borular onları zaten çekmiş olabilir mi? |
| Yetersiz çıkış alanı | Her çıktı için yer var mı? Dört yuvalı tek Çıkış Yolu yetersiz mi? Yolda Taş Tozu veya yan ürünler mi kaldı? |
| Yalnızca düşük paralel veya sık bekleme | Girdi miktarları, Girdi Kapağı Suyu ve çıkış alanı yeterli mi? Su beslemesi Basit Yıkayıcı moduna yetişebiliyor mu? GUI paralel sınırı çok düşük mü ayarlanmış? |
| Kapakta Buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya diğer makinelerle Buhar paylaşıyor mu? Mevcut paralel sayısı ve yüksek basınç kademesi Kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Aktif transfer ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve alet kullanımı için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buhar Temizleyici](https://wiki.gtnewhorizons.com/wiki/Steam_Purifier)