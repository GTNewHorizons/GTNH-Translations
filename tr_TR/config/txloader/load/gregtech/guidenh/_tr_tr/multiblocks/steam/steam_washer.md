---
item_ids:
  - gregtech:gt.blockmachines:31082
navigation:
  title: Buhar Arıtıcısı
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31082
  position: 6
quest_ids:
  - zorY0c3BQuqLJp7ThOLG-g
---

# Buhar Arıtıcısı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" />, Buhar çağında kullanılabilen bir cevher yıkama multiblokudur. Mineralleri partiler halinde işlemek için buhar ve su kullanır ve aynı tarifin aynı anda en fazla sekiz kopyasını işleyebilir. **Cevher Yıkayıcı** ve **Basit Yıkayıcı** modları, yan ürünleri toplamak ile hızlı yıkamak arasında seçim yapmanı sağlar.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve Yüksek Basınçlı çelik yapıları vardır. Ezilmiş Cevherleri yıkamayı Buhar çağında kullanılabilir hale getirir; Basit Yıkayıcı modu ayrıca uygun Saf Olmayan Tozları ve Arıtılmış Tozları da hızlıca yıkayabilir. Yüksek Basınçlı yapıya yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | Buhar; kontrolcü tarifi Dökme Demir Plaklar, Kalay Rotorlar, bir Tumbaga Çerçeve Kutusu ve diğer malzemeleri gerektirir |
| Boyutlar | Dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde; kontrolcü küçük küpün ikinci katmanının ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Cevher Yıkayıcı ya da Basit Toz Yıkayıcı tarifleri; 32 EU/t'yi aşmamalı |
| Girişler ve çıkışlar | Buhar Giriş Yolları eşya kabul eder, Girdi Kapakları tarif suyunu kabul eder ve buhar Çıkış Yolları eşya çıkarır |
| Çalışma modları | Varsayılan olarak Cevher Yıkayıcı modu; tornavida veya GUI ile Basit Yıkayıcı moduna geç |
| Paraleller | Aynı tarifin en fazla sekiz kopyası; Yüksek Basınçlı yapı bu sınırı yükseltmez |
| İşlem süresi | Temel yapıda NEI'de gösterilen sürenin yaklaşık 1,6 katı, Yüksek Basınçlı yapıda 0,8 katı |
| Yükseltmeler ve overclock | Yüksek Basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31082" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki düzenek bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Girdi Kapağı kullanır. Temel yapı bronz bileşenleri kullanırken Yüksek Basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları ve boru muhafazaları aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek Basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzenekte 59 adet; aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az 55 gerçek kasa kalmalı |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz adet, tankın tabanında merkezi kasanın çevresinde |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | 12 adet, tankın içindeki boruları ve yukarıdaki bağlantı borularını oluşturur |
| Cam | Örneğin <ItemLink id="minecraft:glass" showIcon="left" /> | Mevcut cam yeniden kullanılabilir | 24 adet, iki katman tank duvarı oluşturur; hologramın kabul ettiği cam bloklarını kullan |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" /> | Aynı kontrolcü | Bir adet, küçük küpün ikinci katmanının ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Giriş Kapağı | Örneğin <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | Su sağlamak için en az bir adet, bir kasanın yerine |

Yapıda kasa veya kapak için 63 konum vardır. Yukarıda listelenen dört arayüzü kurmak 59 kasa bırakır. Girdi Kapakları veya yollar eklemek kasa sayısını buna göre azaltır, ancak en az 55 gerçek kasa kalmalıdır. Kapaklar ve yollar Dişli Kutusu Kasalarının, boru muhafazalarının veya camın yerini alamaz.

Katmanları tabandan yukarı doğru say. Yapı bir küçük küp, yanında bir cam tank ve üstünde borulardan oluşur. Dokuz blok genişliğindeki yapının tamamının merkezinde kontrolcü yoktur. Etkileşimli yapıyı veya hologramı takip et. Kontrolcü yalnızca yatay olarak yönelebilir ve yapı ön yüzü etrafında döndürülemez; hologramdaki boş konumların doldurulması gerekmez.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise Yüksek Basınçlı yapıyı seçer. Destekli inşadan sonra kapakları tak ve yapıyı kontrol et.

### Tank Suyu ve Tarif Suyu

Buhar, yapının tankındaki su ve tarif suyu farklı amaçlara hizmet eder:

| Konum | Amaç |
| --- | --- |
| Buhar Kapağı | Makineye güç sağlamak için harici kazanın ürettiği buharı alır |
| Giriş Kapağı | Sıradan Suyu veya tarifin gerektirdiği Damıtılmış Suyu alır; her tarif suyunu buradan tüketir |
| Yapının tankı | İkinci katmanda merkezi boru muhafazasının çevresindeki sekiz su konumu; su kaynaklarını elle yerleştir veya makinenin doldurmasına izin ver |

Boru muhafazasını tankın merkezinde tut. Çevredeki sekiz su konumu başlangıçta boş bırakılabilir. Tankı kontrol ederken makine, bir su kaynağı bloğu yerleştirmek için Girdi Kapaklarından seferde **1.000 L sıradan Su** alır. Sekiz konumun tamamı boşsa ilk dolum **8.000 L'ye kadar ek sıradan Su** tüketir. Bu, mevcut döngünün tarif suyundan ayrıdır, bu yüzden başlamadan önce yeterli tampon sağla.

Sekiz konumun tamamını su kovalarıyla elle de doldurabilirsin. **Tanka konulan su, Girdi Kapaklarındaki tarif suyunun yerini tutmaz.** Tank dolduktan sonra Girdi Kapaklarına su vermeye devam et. Tank suyu her tarifte tüketilmez, ancak bir kaynak kaldırılırsa makine daha sonraki bir kontrolde onu yeniden doldurmaya çalışır. Yapı kontrolü su kaynaklarını veya havayı kabul eder; akan su, kaynak bloklarının yerini alamaz.

Cevher Yıkayıcı modu Damıtılmış Su tarifleri içerir, ancak boş bir tankın otomatik doldurulması yalnızca **sıradan Su** kullanır. Damıtılmış Suyla yıkamadan önce tankı kovalarla doldur veya otomatik dolum için sıradan Su içeren ek bir Giriş Kapağı tak.

## Makinenin Kullanımı

### İki Yıkama Modu

<kbd>Sağ tıkla</kbd> ile kontrolcüye <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> uygula veya GUI'deki mod düğmesine tıkla ve Cevher Yıkayıcı ile Basit Yıkayıcı modları arasında geçiş yap.

| Özellik | Cevher Yıkayıcı modu | Basit Yıkayıcı modu |
| --- | --- | --- |
| Tarif haritası | NEI'deki Cevher Yıkayıcı tarifleri | NEI'deki Basit Toz Yıkayıcı tarifleri |
| Yaygın girişler | Ezilmiş Cevherler ve diğer uygun mineral ara ürünleri | Uygun Ezilmiş Cevherler, Saf Olmayan Tozlar ve Arıtılmış Tozlar |
| Yaygın ana çıktılar | Ezilmiş Cevherler Arıtılmış Ezilmiş Cevherlere dönüşür | Ezilmiş Cevherler Arıtılmış Ezilmiş Cevherlere dönüşür; Saf Olmayan Tozlar ve Arıtılmış Tozlar normal tozlara dönüşür |
| Yan ürünler | Tarifte listelenen Taş Tozunu ve mineral yan ürünlerini toplar; bazı çıktılar şansa bağlıdır | Yalnızca temizlenmiş ana ürünü üretir; cevher yıkama veya santrifüjleme yan ürünleri yoktur |
| Tarif başına tipik su | 1.000 L sıradan Su veya 200 L Damıtılmış Su; ilgili NEI tarifini kontrol et | 100 L sıradan Su |
| NEI'de gösterilen tipik süre | Sıradan Suyla 25 saniye veya Damıtılmış Suyla 15 saniye; tek tek tarifler farklı olabilir | Beş tick, yani normal 20 TPS'de 0,25 saniye |

Mineral yan ürünlerine ihtiyacın olduğunda Cevher Yıkayıcı modunu seç ve her ürün için çıkış alanı bırak. Yalnızca ana ürüne hızlıca ihtiyacın olduğunda Basit Yıkayıcı modunu seç. Basit yıkama hızlıdır ve az su kullanır; bu da yan ürünlerini atlamaya karar verdiğin malzemeleri toplu işlemek için uygundur.

Saf Olmayan Tozlar ve Arıtılmış Tozlar için [Buhar Ayırıcı](./steam_centrifuge.md) tariflerine de bak. Santrifüjleme, normal toz üretirken genellikle ilgili yan ürünleri kurtarabilir; basit yıkama ise bu yan ürünleri atlar. İşleme rotasını o mineralin NEI tariflerini kullanarak seç.

> [!WARNING]
> Basit Yıkayıcı modu, normal cevher yıkama veya santrifüjlemeden gelen yan ürünleri üretmez. Cevher Yıkayıcı moduna geri dönmek, Basit Yıkayıcı modunda zaten işlenmiş eşyalardaki yan ürünleri kurtaramaz. Yan ürünlerine ihtiyacın olan mineralleri işlemeden önce mevcut modu kontrol et.

### Mineral İşleme Rotaları

Ezilmiş Cevher yıkamak genellikle her üretim tarifine hazır normal toz değil, **Arıtılmış Ezilmiş Cevher** üretir. NEI'de sonraki öğütme, santrifüjleme veya diğer işlem adımlarını seç ve eşyaları adlarına ve biçimlerine göre yönlendir.

- **Yan ürünleri koru:** Ezilmiş Cevheri Cevher Yıkayıcı moduna gönder, Arıtılmış Ezilmiş Cevheri, Taş Tozunu ve mineral yan ürünlerini ayrı ayrı topla, ardından sonraki işlemleri düzenle.
- **Hızlı yıka:** Uygun Ezilmiş Cevheri Basit Yıkayıcı moduna gönder ve yalnızca Arıtılmış Ezilmiş Cevheri topla.
- **Cevher tozlarını hızlıca arıt:** Uygun Saf Olmayan Tozu veya Arıtılmış Tozu normal toz elde etmek için Basit Yıkayıcı moduna gönder. İlgili yan ürünlerine ihtiyacın varsa bunun yerine santrifüjleme kullan.

Her malzemenin veya mineral biçiminin bir Basit Toz Yıkayıcı tarifi yoktur. Arıtılmış Ezilmiş Cevher ile Arıtılmış Toz farklı eşyalardır. Adında "Arıtılmış" geçmesi, o eşyanın Basit Yıkayıcı modunda tekrar işlenebileceği anlamına gelmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buhar Giriş Yolunun, buhar Çıkış Yolunun ve Girdi Kapağının takılı olduğunu doğrula.
2. Buhar Kapağına buhar, Giriş Kapağına su vermek için ayrı hatlar kullan. Tank boşsa önce otomatik dolum için yeterli miktarda sıradan Su tamponla.
3. İstediğin modu seç ve NEI'de ilgili tarif haritasını, giriş biçimini, su türünü ve tüm çıktıları kontrol et.
4. Her çıktı için yer bırak, ardından az miktarda malzemeyle başla ve tankı, çıktıları, buhar tamponunu ve Giriş Kapağının içeriğini gözlemle.
5. Sürekli buhar ve su beslemesini ve çıktı toplamayı doğruladıktan sonra giriş miktarlarını ve paralelleri artır.

> [!NOTE]
> Mevcut sürümde makine, ilk çalıştırmasında veya periyodik tank kontrolünde kısa süreliğine "Su Yok" gösterebilir. Kontrolden sonra bir sonraki tarif kontrolünde yeniden deneyecektir. Giriş Kapağındaki suyu ve tanktaki kaynak bloklarını doğrula, sonra bekle ve gözlemle. Hâlâ çalışmıyorsa aşağıdaki sorun giderme bölümünü kullan.

## Buhar Beslemesi, Su Beslemesi ve Verim

Buhar Arıtıcısı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı minerali işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca giriş miktarlarına, tarif suyuna, çıkış alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı, NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alır, Yüksek Basınçlı yapı ise yaklaşık 0,8 katını. 25 saniye olarak gösterilen tipik bir sıradan Su yıkama tarifi, temel yapıda yaklaşık 40 saniye veya Yüksek Basınçlı yapıda 20 saniye sürer. Beş tick olarak gösterilen bir Basit Toz Yıkayıcı tarifi, temel yapıda yaklaşık sekiz tick veya Yüksek Basınçlı yapıda dört tick sürer. Gerçek sürekli verim ayrıca tarif kontrollerine, giriş beslemesine ve çıktı işlemeye bağlıdır.

| Özellik | Temel yapı | Yüksek Basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısında buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel değer | Temel yapıyla yaklaşık aynı |
| Tarif başına su | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Paraleller, bir döngüde işlenen tarif sayısını artırır; döngünün süresini paralel sayısına bölmez. Sekiz paralelde tipik bir sıradan Su yıkama döngüsü **8.000 L Su**, bir Damıtılmış Su döngüsü **1.600 L Damıtılmış Su** ve basit bir yıkama döngüsü **800 L Su** gerektirir. Başlangıçta tankın hâlâ otomatik doldurulması gerekiyorsa bunun için ayrıca ek sıradan Su sağla.

Basit Yıkayıcı modu tarif başına az su kullanır ancak hızlı işler, bu yüzden Girdi Kapağı tamponu ve su boruları yine de darboğaz olabilir. Yüksek Basınçlı yapı yükseltmesi tarif başına suyu azaltmaz. İşlem hızı ikiye katlandığından sürekli üretim daha yüksek bir su besleme oranı da gerektirir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır ve Giriş Kapağının su beslemesinin yetişip yetişmediğini de izle.

Çalışma sırasındaki buhar tüketim oranını görmek için Waila'yı kullan ve sürekli işlem sırasında tamponun sürekli düşüp düşmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s'ye çevirmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar veya su beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boruları iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen malzemeler geri verilmez. Yüksek Basınçlı yapıya yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={2} />
</GameScene>

Yüksek Basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Dişli Kutusu Kasalarını ve Bronz boru muhafazalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları ve Çelik boru muhafazaları ile değiştir. Cam, bronz-çelik kademe kontrolüne katılmaz, bu yüzden mevcut sıradan cam yeniden kullanılabilir.

Yükseltmeden önce işlemeyi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı, suyu ve üretimi geri yüklemeden önce makinenin Yüksek Basınçlı kademeyi gösterdiğini doğrula.

Yüksek Basınçlı yapı, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı, buhar yolları ve Girdi Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek kademe tarifler kullanılamaz durumda kalır.

## Otomasyon ve Çıktı Yönlendirme

Buhar Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Giriş:** Mineralleri Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Ezilmiş Cevher, Saf Olmayan Toz ve Arıtılmış Toz gibi biçimlere göre filtrele.
- **Çıkış:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek, ardından ürünleri ana çıktı deposuna, yan ürün deposuna veya bir sonraki makineye yönlendir.
- **Buhar ve su:** Buharı Buhar Kapağına, suyu Girdi Kapaklarına bağlayarak ayrı hatlar kullan. Damıtılmış Suyla yıkama ile tankı sıradan Suyla doldurma için ayrı tamponlar ve arayüzler düzenle.
- **Yan ürünler:** Cevher Yıkayıcı modunda ana çıktının yanı sıra Taş Tozunu ve mineral yan ürünlerini de ele al. Yalnızca ana çıktıyı filtrelemek, diğer eşyaların çıkış yolunda birikmesine yol açar.
- **Mod değişiklikleri:** Malzeme girişini durdur ve mevcut işlemin bitmesini bekle. Aktarımı sürdürmeden önce modu ve kalan girişleri kontrol et; böylece sonraki malzemeler istemeden diğer rotadan işlenmez.

Cevher yıkama tarifleri aynı anda birkaç farklı eşya üretebilir. Dört yuvalı tek bir Çıkış Yolu, sürekli işlem sırasında tüm ürünleri tutamayabilir. Ek Çıkış Yolları çıkış alanını genişletir ancak paralel sınırını yükseltmez. Kapak veya yol eklerken en az 55 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin yok etme modunu "Yok Etme" olarak ayarla ve her çıktı için yer sağla. Eşya yok etme etkinse çıkış tıkandığında ana ürünler veya yan ürünler atılabilir.

## Sorun Giderme

| Belirti | Neye bakmalısın |
| --- | --- |
| Eksik yapı | Yapı dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde mi? Kontrolcü küçük küpün ikinci katmanının ön ortasında mı? Borular, Dişli Kutusu Kasaları, cam ve su konumları hologramda gösterildiği gibi mi düzenlenmiş? |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutusu Kasaları ve boru muhafazaları aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik kapak veya yol | Tam olarak bir Buhar Kapağı ve en az bir buhar Giriş Yolu, buhar Çıkış Yolu ve Girdi Kapağı var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapak ekledikten sonra yapı hata veriyor | En az 55 gerçek kasa kaldı mı? Cam, Dişli Kutusu Kasaları veya boru muhafazaları kapaklarla mı değiştirildi? |
| Tank otomatik dolmuyor | Giriş Kapağında sıradan Su var mı? Her boş su konumu 1.000 L gerektirir. Yalnızca Damıtılmış Su tankı otomatik dolduramaz; kovalarla kaynak blokları da yerleştirebilirsin. |
| Tankta su var ama işlem başlamıyor | Giriş Kapağı hâlâ tarifin gerektirdiği suyu içeriyor mu? Tank suyu tarif suyunun yerini tutmaz. Kaynak yerine yalnızca akan su blokları mı var? |
| Kısa süreli "Su Yok" mesajı | Makine ilk veya periyodik tank kontrolünü yapıyor olabilir. Su miktarlarını doğrula ve bir sonraki tarif kontrolünü bekle. Hâlâ çalışmıyorsa modu, tarifi ve yapıyı kontrol et. |
| Mineraller var ama tarif bulunamıyor | Doğru Cevher Yıkayıcı veya Basit Yıkayıcı modu mu seçili? İlgili bir tarif var mı? Arıtılmış Ezilmiş Cevher ile Arıtılmış Toz karıştırıldı mı? Giriş suyu türü doğru mu? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek Basınçlı yapı da MV veya daha yüksek kademe tarifleri işleyemez. |
| Taş Tozu veya mineral yan ürünü yok | Basit Yıkayıcı modu mu seçili? Yan ürünler şansa mı bağlı? Eşya yok etme etkin mi? Borular onları zaten çekmiş olabilir mi? |
| Yetersiz çıkış alanı | Her çıktı için yer var mı? Dört yuvalı tek bir Çıkış Yolu yetersiz mi? Taş Tozu veya yan ürünler çıkış yolunda mı kalıyor? |
| Yalnızca düşük paraleller veya sık bekleme | Giriş miktarları, Giriş Kapağı suyu ve çıkış alanı yeterli mi? Su beslemesi Basit Yıkayıcı moduna yetişebiliyor mu? GUI paralel sınırı çok düşük mü ayarlanmış? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve Yüksek Basınçlı kademe kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](../multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buhar Arıtıcısı](https://wiki.gtnewhorizons.com/wiki/Steam_Purifier)
