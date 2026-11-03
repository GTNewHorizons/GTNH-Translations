---
item_ids:
  - gregtech:gt.blockmachines:31082
navigation:
  title: Buharlı Arıtıcı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31082
  position: 6
quest_ids:
  - zorY0c3BQuqLJp7ThOLG-g
---

# Buharlı Arıtıcı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" />, Buhar çağında bulunan bir multiblok cevher yıkama makinesidir. Mineralleri partiler hâlinde işlemek için buhar ve su kullanır ve aynı anda aynı tarifin en fazla sekiz kopyasını işleyebilir. **Cevher Yıkayıcı** ve **Basit Yıkayıcı** modları, yan ürünleri toplamak ile hızlı yıkamak arasında seçim yapmanı sağlar.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Ezilmiş Cevherleri yıkamayı Buhar çağında kullanılabilir hâle getirir; Basit Yıkayıcı modu ayrıca uygun Saf Olmayan Tozları ve Temizlenmiş Tozları hızlıca yıkayabilir. Yüksek basınçlı yapıya yükseltmek verimi artırır ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Dökme Demir Plakalar, Kalay Rotorlar, bir Tumbaga Çerçeve ve diğer materyaller gerektirir |
| Boyutlar | Dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde; kontrolcü küçük küpün ikinci katmanının ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Cevher Yıkayıcı ya da Basit Toz Yıkayıcı tarifleri; en fazla 32 EU/t gerektirir |
| Girdiler ve çıktılar | Buhar Giriş Yolları eşya kabul eder, Girdi Kapakları tarif suyunu kabul eder ve buhar Çıkış Yolları eşya çıkarır |
| Çalışma modları | Varsayılan olarak Cevher Yıkayıcı modundadır; tornavida veya GUI ile Basit Yıkayıcı moduna geçilir |
| Paralellik | Aynı tariften en fazla sekiz kopya; yüksek basınçlı yapı bu sınırı artırmaz |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31082" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki kurulum bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Girdi Kapağı kullanır. Temel yapı bronz bileşenler kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları ve Boru Muhafazaları aynı kademeden olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan kurulumda 59; aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az 55 gerçek kasa kalmalıdır |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz; tankın tabanında merkezî kasanın etrafında |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | 12; tankın içindeki boruları ve yukarıdaki bağlantı borularını oluşturur |
| Cam | Örneğin, <ItemLink id="minecraft:glass" showIcon="left" /> | Mevcut cam yeniden kullanılabilir | 24; tank duvarlarının iki katmanını oluşturur; hologramın kabul ettiği cam bloklarını kullan |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31082" showIcon="left" /> | Aynı kontrolcü | Bir adet; küçük küpün ikinci katmanının ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet; bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet; bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet; bir kasanın yerine |
| Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | En az bir adet; su sağlamak için bir kasanın yerine |

Yapıda kasalar veya kapaklar için 63 konum vardır. Yukarıda listelenen dört arayüzün kurulması 59 kasa bırakır. Girdi Kapakları veya yollar eklemek kasa sayısını buna göre azaltır, ancak en az 55 gerçek kasa kalmalıdır. Kapaklar ve yollar Dişli Kutusu Kasalarının, Boru Muhafazalarının veya camın yerini alamaz.

Katmanları tabandan yukarı doğru say. Yapı küçük bir küp, yanında bir cam tank ve üstünde borulardan oluşur. Kontrolcü, dokuz blok genişliğindeki tüm yapının merkezinde değildir. Etkileşimli yapıyı veya hologramı takip et. Kontrolcü yalnızca yatay olarak yönlendirilebilir ve yapı ön yüzü etrafında döndürülemez; hologramdaki boş konumların doldurulması gerekmez.

Yapıyı önizlemek ve inşa etmeye yardım almak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademe 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

### Tank Suyu ve Tarif Suyu

Buhar, yapının tankındaki su ve tarif suyu farklı amaçlara hizmet eder:

| Konum | Amaç |
| --- | --- |
| Buhar Kapağı | Makineye güç vermek için harici bir kazan tarafından üretilen buharı alır |
| Girdi Kapağı | Normal Su veya tarifin gerektirdiği Damıtılmış Suyu alır; her tarif suyunu buradan tüketir |
| Yapının tankı | İkinci katmanda merkezî Boru Muhafazasının etrafındaki sekiz su konumu; su kaynaklarını elle yerleştir veya makinenin doldurmasına izin ver |

Boru Muhafazasını tankın merkezinde tut. Çevredeki sekiz su konumu başlangıçta boş bırakılabilir. Tankı kontrol ederken makine, bir su kaynak bloğu yerleştirmek için Girdi Kapaklarından her seferinde **1.000 L normal Su** alır. Sekiz konumun tamamı boşsa ilk dolum **8.000 L ek normal Su** tüketir. Bu, mevcut döngünün tarif suyundan ayrıdır; bu yüzden başlamadan önce yeterli tampon sağla.

Sekiz konumun tamamını su kovalarıyla elle de doldurabilirsin. **Tanka konulan su, Girdi Kapaklarındaki tarif suyunun yerini tutmaz.** Tank dolduktan sonra Girdi Kapaklarına su vermeye devam et. Tank suyu her tarifte tüketilmez, ancak bir kaynak kaldırılırsa makine daha sonraki bir kontrolde onu yeniden doldurmaya çalışır. Yapı kontrolü su kaynaklarını veya havayı kabul eder; akan su kaynak bloklarının yerini alamaz.

Cevher Yıkayıcı modu Damıtılmış Su tarifleri içerir, ancak boş bir tankın otomatik doldurulması yalnızca **normal Su** kullanır. Damıtılmış Suyla yıkamadan önce tankı kovalarla doldur veya otomatik dolum için normal Su içeren ek bir Girdi Kapağı tak.

## Makine Kullanımları

### İki Yıkama Modu

Cevher Yıkayıcı ve Basit Yıkayıcı modları arasında geçiş yapmak için kontrolcüye <ItemLink id="gregtech:gt.metatool.01:22" showIcon="left" /> ile <kbd>sağ tıkla</kbd> veya GUI'deki mod düğmesine tıkla.

| Özellik | Cevher Yıkayıcı modu | Basit Yıkayıcı modu |
| --- | --- | --- |
| Tarif haritası | NEI'deki Cevher Yıkayıcı tarifleri | NEI'deki Basit Toz Yıkayıcı tarifleri |
| Yaygın girdiler | Ezilmiş Cevherler ve diğer uygun mineral ara ürünleri | Uygun Ezilmiş Cevherler, Saf Olmayan Tozlar ve Temizlenmiş Tozlar |
| Yaygın ana çıktılar | Ezilmiş Cevherler Temizlenmiş Ezilmiş Cevherlere dönüşür | Ezilmiş Cevherler Temizlenmiş Ezilmiş Cevherlere dönüşür; Saf Olmayan Tozlar ve Temizlenmiş Tozlar normal tozlara dönüşür |
| Yan Ürünler | Tarifte listelenen Taş Tozunu ve mineral yan ürünlerini toplar; bazı çıktılar şansa bağlıdır | Cevher yıkama veya santrifüjleme yan ürünleri olmadan yalnızca temizlenmiş ana ürünü üretir |
| Tarif başına tipik su | 1.000 L normal Su veya 200 L Damıtılmış Su; ilgili NEI tarifini kontrol et | 100 L normal Su |
| NEI'de gösterilen tipik süre | Normal Suyla 25 saniye veya Damıtılmış Suyla 15 saniye; tek tek tarifler farklı olabilir | Beş tick veya normal 20 TPS'de 0,25 saniye |

Mineral yan ürünlerine ihtiyaç duyduğunda Cevher Yıkayıcı modunu seç ve her ürün için çıkış alanı bırak. Yalnızca ana ürüne hızlıca ihtiyaç duyduğunda Basit Yıkayıcı modunu seç. Basit yıkama hızlıdır ve az su kullanır; yan ürünlerini atlamaya karar verdiğin materyalleri toplu işlemek için uygundur.

Saf Olmayan Tozlar ve Temizlenmiş Tozlar için [Buharlı Santrifüj](./steam_centrifuge.md) tariflerini de kontrol et. Santrifüjleme, normal toz üretirken çoğu zaman ilgili yan ürünleri geri kazanabilir; basit yıkama ise bu yan ürünleri atlar. İşleme yolunu ilgili mineralin NEI tariflerini kullanarak seç.

> [!WARNING]
> Basit Yıkayıcı modu, normal cevher yıkama veya santrifüjleme yan ürünlerini üretmez. Cevher Yıkayıcı moduna geri dönmek, Basit Yıkayıcı modunda zaten işlenmiş eşyalardan bu yan ürünleri geri kazanamaz. Yan ürünlerine ihtiyaç duyduğun mineralleri işlemeden önce mevcut modu kontrol et.

### Mineral İşleme Yolları

Ezilmiş Cevher yıkamak genellikle her üretim tarifine hazır normal toz yerine **Temizlenmiş Ezilmiş Cevher** üretir. Sonraki öğütme, santrifüjleme veya diğer işleme adımlarını NEI'de seç ve eşyaları adlarına ve biçimlerine göre yönlendir.

- **Yan ürünleri koru:** Ezilmiş Cevheri Cevher Yıkayıcı moduna gönder, Temizlenmiş Ezilmiş Cevheri, Taş Tozunu ve mineral yan ürünlerini ayrı ayrı topla, ardından sonraki işlemeyi düzenle.
- **Hızlı yıka:** Uygun Ezilmiş Cevheri Basit Yıkayıcı moduna gönder ve yalnızca Temizlenmiş Ezilmiş Cevheri topla.
- **Cevher tozlarını hızlıca temizle:** Uygun Saf Olmayan Tozu veya Temizlenmiş Tozu normal toz elde etmek için Basit Yıkayıcı moduna gönder. İlgili yan ürünlerine ihtiyacın varsa bunun yerine santrifüjleme kullan.

Her materyal veya mineral biçiminin bir Basit Toz Yıkayıcı tarifi yoktur. Temizlenmiş Ezilmiş Cevher ve Temizlenmiş Toz farklı eşyalardır. Bir eşyanın adında "Temizlenmiş" olması, Basit Yıkayıcı modunda yeniden işlenebileceği anlamına gelmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buhar Giriş Yolunun, buhar Çıkış Yolunun ve Girdi Kapağının takılı olduğunu doğrula.
2. Buhar Kapağına buhar ve Girdi Kapağına su sağlamak için ayrı hatlar kullan. Tank boşsa önce otomatik dolum için yeterli normal Su tamponla.
3. İstediğin modu seç ve ilgili tarif haritasını, girdi biçimini, su türünü ve tüm çıktıları NEI'de kontrol et.
4. Her çıktı için alan bırak, sonra az miktarda materyalle başla ve tankı, çıktıları, buhar tamponunu ve Girdi Kapağı içeriğini gözlemle.
5. Sürekli buhar ve su beslemesini ve çıktı toplamayı doğruladıktan sonra girdi miktarlarını ve paralelliği artır.

> [!NOTE]
> Mevcut sürümde makine, ilk çalıştırmasında veya periyodik tank kontrolünde kısa süreliğine "Su Yok" gösterebilir. Kontrolden sonra bir sonraki tarif kontrolünde yeniden deneyecektir. Girdi Kapağındaki suyu ve tanktaki kaynak bloklarını doğrula, sonra bekle ve gözlemle. Hâlâ çalışmıyorsa aşağıdaki sorun giderme bölümünü kullan.

## Buhar Beslemesi, Su Beslemesi ve Verim

Buharlı Arıtıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı mineral işleyebileceği anlamına gelmez. Gerçek paralellik ayrıca girdi miktarlarına, tarif suyuna, çıkış alanına ve GUI'de ayarlanan paralellik sınırına bağlıdır.

Temel yapı, NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alır; yüksek basınçlı yapı ise yaklaşık 0,8 katını. 25 saniye olarak gösterilen tipik bir normal Su yıkama tarifi, temel yapıda yaklaşık 40 saniye veya yüksek basınçlı yapıda 20 saniye sürer. Beş tick olarak gösterilen bir Basit Toz Yıkayıcı tarifi, temel yapıda yaklaşık sekiz tick veya yüksek basınçlı yapıda dört tick sürer. Gerçek sürekli verim ayrıca tarif kontrollerine, girdi beslemesine ve çıktı işlemeye bağlıdır.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralellik | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralellik sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel | Yaklaşık olarak temel yapıyla aynı |
| Tarif başına su | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Paralellik, bir döngüde işlenen tarif sayısını artırır ancak döngü süresini paralellik sayısına bölmez. Sekiz paralellikte tipik bir normal Su yıkama döngüsü **8.000 L Su**, bir Damıtılmış Su döngüsü **1.600 L Damıtılmış Su** ve basit bir yıkama döngüsü **800 L Su** gerektirir. Başlangıçta tankın hâlâ otomatik doluma ihtiyacı varsa bunun için ayrıca ek normal Su sağla.

Basit Yıkayıcı modu tarif başına az su kullanır ancak hızlı işler; bu nedenle Girdi Kapağı tamponu ve su boruları yine de darboğaz olabilir. Yüksek basınç yükseltmesi tarif başına suyu azaltmaz. İşlem hızı ikiye katlandığında sürekli üretim daha yüksek bir su besleme oranı da gerektirir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır ve Girdi Kapağının su beslemesinin yetişip yetişmediğini de izle.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila'yı kullan ve sürekli işleme sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken eşleşen birimleri kullan. Buhar veya su beslemesi yetersizse GUI'deki paralellik sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın tükenmesi mevcut işlemi iptal eder ve zaten tüketilen materyaller geri verilmez. Yüksek basınçlı yapıya yükseltmeden veya paralellik sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31082" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Dişli Kutusu Kasalarını ve Bronz Boru Muhafazalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları ve Çelik Boru Muhafazaları ile değiştir. Cam, bronz ile çelik kademe kontrolüne katılmaz; bu nedenle mevcut normal cam yeniden kullanılabilir.

Yükseltmeden önce işlemeyi ve materyal girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı, suyu ve üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç, makinenin yapı kademesidir. Hâlâ normal buhar kullanır ve mevcut Buhar Kapağı, buhar yolları ve Girdi Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralellik olarak kalır ve MV veya daha yüksek kademeli tarifler kullanılamaz.

## Otomasyon ve Çıktı Yönlendirmesi

Buhar Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak eşya çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Mineralleri Giriş Yolunun ön yüzüne göndermek için Huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Ezilmiş Cevher, Saf Olmayan Toz ve Temizlenmiş Toz gibi biçimlere göre filtrele.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek ve ürünleri ana çıktı depolamasına, yan ürün depolamasına veya bir sonraki makineye yönlendir.
- **Buhar ve su:** Ayrı hatlar kullan; buharı Buhar Kapağına, suyu Girdi Kapaklarına bağla. Damıtılmış Suyla yıkama ve tankı normal Suyla doldurma için ayrı tamponlar ve arayüzler düzenle.
- **Yan ürünler:** Cevher Yıkayıcı modunda ana çıktının yanı sıra Taş Tozunu ve mineral yan ürünlerini de ele al. Yalnızca ana çıktıyı filtrelemek diğer eşyaların yolda birikmesine neden olur.
- **Mod değişiklikleri:** Materyal girişini durdur ve mevcut işlemin bitmesini bekle. Aktarımı sürdürmeden önce modu ve kalan girdileri kontrol et; böylece sonraki materyaller istemeden diğer yoldan işlenmez.

Cevher yıkama tarifleri aynı anda birkaç farklı eşya üretebilir. Dört yuvalı tek bir Çıkış Yolu, sürekli işleme sırasında tüm ürünleri tutamayabilir. Ek Çıkış Yolları çıkış alanını genişletir ancak paralellik sınırını yükseltmez. Kapak veya yol eklerken en az 55 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin imha modunu "İmha Etme" olarak ayarla ve her çıktı için alan sağla. Eşya imhası etkinse çıktı tıkandığında ana ürünler veya yan ürünler atılabilir.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Eksik yapı | Yapı dokuz blok genişliğinde, beş blok derinliğinde ve altı blok yüksekliğinde mi? Kontrolcü küçük küpün ikinci katmanının ön ortasında mı? Borular, Dişli Kutusu Kasaları, cam ve su konumları hologramda gösterildiği gibi düzenlenmiş mi? |
| Yapı kademesi uyuşmuyor | Kasalar, Dişli Kutusu Kasaları ve Boru Muhafazaları hepsi aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik kapak veya yol | Tam olarak bir Buhar Kapağı ve en az bir buhar Giriş Yolu, buhar Çıkış Yolu ve Girdi Kapağı var mı? Yanlışlıkla normal elektrikli makine eşya yolları mı kullanıldı? |
| Kapaklar eklendikten sonra yapı başarısız | En az 55 gerçek kasa kaldı mı? Cam, Dişli Kutusu Kasaları veya Boru Muhafazaları kapaklarla mı değiştirildi? |
| Tank otomatik dolmuyor | Girdi Kapağında normal Su var mı? Her boş su konumu 1.000 L gerektirir. Tek başına Damıtılmış Su tankı otomatik dolduramaz; kaynak bloklarını kovalarla da yerleştirebilirsin. |
| Tankta su var ama işleme başlamıyor | Girdi Kapağında hâlâ tarifin gerektirdiği su var mı? Tank suyu tarif suyunun yerini tutamaz. Kaynak yerine yalnızca akan su blokları mı var? |
| Kısa süreli "Su Yok" mesajı | Makine ilk veya periyodik tank kontrolünü yapıyor olabilir. Su miktarlarını doğrula ve bir sonraki tarif kontrolünü bekle. Hâlâ çalışmıyorsa modu, tarifi ve yapıyı kontrol et. |
| Mineraller var ama tarif bulunamıyor | Doğru Cevher Yıkayıcı veya Basit Yıkayıcı modu mu seçili? İlgili bir tarif var mı? Temizlenmiş Ezilmiş Cevher ile Temizlenmiş Toz karıştırıldı mı? Girdi su türü doğru mu? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Taş Tozu veya mineral yan ürünü yok | Basit Yıkayıcı modu mu seçili? Yan ürünler şansa bağlı mı? Eşya imhası etkin mi? Borular onları zaten çekmiş olabilir mi? |
| Yetersiz çıkış alanı | Her çıktı için yer var mı? Dört yuvalı bir Çıkış Yolu yetersiz mi? Taş Tozu veya yan ürünler yolda mı kalmış? |
| Yalnızca düşük paralellik veya sık bekleme | Girdi miktarları, Girdi Kapağı suyu ve çıkış alanı yeterli mi? Su beslemesi Basit Yıkayıcı moduna yetişebiliyor mu? GUI paralellik sınırı çok düşük mü ayarlanmış? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralellik sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Etkin aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Çince Wiki: Buharlı Arıtıcı](https://gtnh.huijiwiki.com/wiki/大型蒸汽洗矿厂)