---
item_ids:
  - gregtech:gt.blockmachines:31080
quest_ids:
  - 0rUmaWIPQPaL93q-_pgKXw
navigation:
  title: Buhar Ayırıcı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31080
  position: -501
---
# Buhar Ayırıcı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" />, Multibloklar arasında Buhar çağında kullanılabilen bir Santrifüjdür. Materyalleri partiler halinde ayırmak için buhar kullanır ve aynı anda aynı tarifin en fazla sekiz kopyasını işleyebilir. Cevher tozlarını temizleyebilir, Yapışkan Reçineden Ham Kauçuk Tozu elde edebilir ve Santrifüj tariflerinden eşya ve sıvı çıktılarını toplayabilir.

Makinenin aynı Kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Uygun Santrifüj tariflerini Buhar çağında kullanılabilir hale getirir. Yüksek basınçlı yapıya yükseltmek verimi artırır ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; Kontrolcü tarifi Dökme Demir Plakalar, Bronz Dişliler, bir Tumbaga Çerçeve ve diğer materyaller gerektirir |
| Boyutlar | 5×5 taban alanı, beş blok yüksekliğinde; Kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Santrifüj tarifleri, en fazla 32 EU/t gerektirir |
| Girdiler ve çıktılar | Buhar Giriş Yolları eşya kabul eder, Buhar Çıkış Yolları eşya çıkarır ve sıradan Çıkış Kapakları sıvı çıkarır; sıradan Girdi Kapakları kabul edilmez |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı veya yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; voltaj hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31080" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Çıkış Kapağı varsayar; böylece hem eşya hem de sıvı çıktıları toplanabilir. Temel yapı bronz bileşenler kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları, Boru Muhafazaları ve Külhan Kasaları aynı kademeden olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzenekte 65 adet; aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az 60 gerçek kasa kalmalıdır |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz: ikinci ve dördüncü katmanların her birinde merkezi Külhan Kasasının etrafında dört adet |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Dört adet, üçüncü katmandaki merkezi Külhan Kasasının etrafında |
| Külhan Kasası | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Üç: ikinci, üçüncü ve dördüncü katmanların her birinin merkezinde bir adet |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" /> | Aynı Kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | Eşya çıktıları için gerektiği kadar kur; bir kasanın yerini alır |
| Çıkış Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıktıları için gerektiği kadar kur; bir kasanın yerini alır |

Yapıda kasalar veya kapaklar için 69 konum vardır. Yukarıda listelenen dört arayüzü kurmak 65 kasa bırakır. Yalnızca eşya çıktılı tarifler işlenecekse Çıkış Kapağını atlamak bunun yerine 66 kasa gerektirir. Yol veya Çıkış Kapağı eklemek kasa sayısını buna göre azaltır, ancak en az 60 gerçek kasa kalmalıdır. Kapaklar ve yollar Dişli Kutusu Kasaları, Boru Muhafazaları veya Külhan Kasalarının yerini alamaz.

Katmanları tabandan yukarıya doğru say. Kasa düzeni katmanlar arasında farklıdır; bu yüzden etkileşimli yapıyı veya hologramı takip et; boş konumların doldurulması gerekmez. En az bir Buhar Çıkış Yolu veya sıradan Çıkış Kapağı kur. Bir tarif hem eşya hem sıvı üretiyorsa iki tür çıktı arayüzünü de kur.

Külhan Kasaları yapı bloklarıdır. Yakıt veya ayrı bir su kaynağı gerektirmezler. Makine için buhar harici bir kazan tarafından üretilir ve Buhar Kapağı aracılığıyla sağlanır.

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullanarak yapıyı önizle ve inşa etmeye yardımcı ol. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Destekli inşadan sonra kapakları kur ve yapıyı kontrol et.

## Makine Kullanımları

Buhar Ayırıcı, Santrifüj tarif haritasını kullanır. NEI'yi kontrol ederken önce tarifin **Santrifüj**e ait olduğunu doğrula, ardından kademesini, girdi biçimini, Programlanmış Devre yapılandırmasını ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Cevher tozlarını temizleme | Uygun Kirli Toz, Temizlenmiş Toz ve diğer ara ürünleri sıradan toza ve ilgili yan ürünlere dönüştürür; her mineralin miktarları ve çıktı biçimleri için NEI'yi kontrol et |
| Yapışkan Reçineyi işleme | Ham Kauçuk Tozu, bir Plantball şansı ve Yapıştırıcı üretir; hem eşya hem de sıvı çıktıları yönetilmelidir |
| Kütükleri santrifüjleme | Uygun kütük tarifleri Metan üretir; Kauçuk Ağacı ve Yaprakları ayrıca şansa bağlı eşya çıktılarına sahiptir; NEI'nin gerektirdiği Programlanmış Devre yapılandırmasını kontrol et |
| Mineralleri ve materyalleri ayırma | Uygun Netherrack Tozu, Endstone Tozu ve diğer Santrifüj tariflerini işler; toplanacak birden fazla eşya veya sıvı çıktısı vardır |
| Hücre tarifleri | Yalnızca girdi olarak eşya alan Santrifüj tariflerini işler; bazı tarifler ayrıca ek Boş Hücreler gerektirir, bu yüzden dolu bir hücre tek başına gerekli tüm girdileri sağlamayabilir |

### Yapışkan Reçine ve Kauçuk

Mevcut Yapışkan Reçine tarifi **bir Yapışkan Reçine** tüketir ve **üç Ham Kauçuk Tozu ile 100 L Yapıştırıcı** üretir; **%10 şansla bir Plantball** verir.

Yapışkan Reçineyi Buhar Giriş Yoluna gönder, Ham Kauçuk Tozunu ve Plantball'ları bir Buhar Çıkış Yolu aracılığıyla topla ve Yapıştırıcıyı sıradan bir Çıkış Kapağı aracılığıyla topla. Yapıştırıcı bir tarif çıktısıdır. **Onu almak için bir Girdi Kapağı kurma.**

Sekiz paralelde bir döngü sekiz Yapışkan Reçine tüketir ve 24 Ham Kauçuk Tozu ile 800 L Yapıştırıcı üretir. Plantball'lar şansa bağlı çıktılar olarak kalır; bir döngünün sekiz adet üretmesi garanti değildir. Sürekli çalıştırmadan önce her iki eşya türü için yer bırak ve Yapıştırıcıyı sürekli çekmek için sıvı borularını kullan.

### Sıvı Girdi Sınırı

Bu makine sıvı **çıktılarını** destekler ancak sıradan Sıvı Girdi Kapaklarını kabul etmez. NEI'de sıvı girdi gerektiren tarifler, LV veya altında olsalar bile sıradan bir Girdi Kapağı eklenerek etkinleştirilemez. Buhar Kapağı güç sağlar ve Hava veya asitler gibi tarif sıvıları için girdi olarak kullanılamaz.

Örneğin, NEI'de doğrudan Hava sıvısı alan bir Santrifüj tarifi, sıvı girdileri kabul eden bir Santrifüj gerektirir. Dolu hücreler, yalnızca ilgili tarif onları açıkça **eşya girdileri** olarak listeliyorsa Buhar Giriş Yoluna gönderilebilir.

> [!NOTE]
> Makine Buhar çağında kullanılabilir ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademe tarifleri etkinleştirmez ve sıvı girdi sınırını kaldırmaz.

### İlk Başlatma

1. Yapıyı kontrol et ve Buhar Kapağının, Buhar Giriş Yolunun ve gerekli çıktı arayüzlerinin kurulu olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarif kademesini, tüm girdileri ve Programlanmış Devre yapılandırmasını; sıvı girdi gerekip gerekmediği dahil kontrol et.
4. Tüm eşya ve sıvı çıktıları için yer bırak, ardından az miktarda materyalle başla ve çıktıları ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini ve çıktı toplamayı doğruladıktan sonra girdi miktarlarını ve paralel sayısını artır.

## Buhar Beslemesi ve Verim

Buhar Ayırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralellik ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alırken yüksek basınçlı yapı yaklaşık 0,8 katını alır. Örneğin, 15 saniye olarak gösterilen Yapışkan Reçine tarifi temel yapıda yaklaşık 24 saniye, yüksek basınçlı yapıda ise 12 saniye sürer. Paralellik, bir döngüde işlenen tarif sayısını artırır ancak döngü süresini paralel sayısına bölmez.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel sayısı | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6 katı | Yaklaşık 0,8 katı |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1 katı | 2 katı |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi artırır; eşya başına toplam buhar maliyeti temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır. Paralel sayısını artırırken eşya girdisi, eşya çıktısı ve sıvı çıktısı da yetişmelidir.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila'yı kullan ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken eşleşen birimler kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında buharın tükenmesi mevcut işlemi iptal eder ve halihazırda tüketilen materyaller geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve Kontrolcüyü korur. Tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları, Çelik Boru Muhafazaları ve Çelik Külhan Kasalarıyla **tüm** Bronz Kaplı Tuğlaları, Bronz Dişli Kutusu Kasalarını, Bronz Boru Muhafazalarını ve Bronz Külhan Kasalarını değiştir.

Yükseltmeden önce işlemi ve materyal girdisini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek Basınçlı yapı, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı, buhar yolları ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Çıktı Yönlendirme

Buhar Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak çekmezler veya ürünleri onlara itmezler; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Ayrıca tarifin gerektirdiği Boş Hücreleri ve Programlanmış Devre yapılandırmasını da sağla.
- **Eşya çıktısı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek, ardından ürünleri ana çıktı depolamasına, yan ürün depolamasına veya bir sonraki makineye yönlendir.
- **Sıvı çıktısı:** Yapıştırıcı, Metan ve diğer ürünleri sıradan Çıkış Kapaklarından çek. Her sıvı türü için depolama ve filtreleri yapılandır ve birden fazla sıvı çıktısı olan tarifler için yeterli Çıkış Kapağı sağla.
- **Buhar:** Buhar Kapağına ayrı bir buhar besleme hattı bağla ve sıvı ürün hatlarını ondan uzak tut.
- **Cevher yönlendirme:** Zaten santrifüjlenmiş eşyaların girdi tamponunu tekrar doldurmaması için sıradan toz, Kirli Toz, Temizlenmiş Toz ve küçük yan ürünler için filtreler ayarla.

Santrifüj tarifleri genellikle aynı anda birkaç farklı eşya üretir. Dört yuvaya sahip tek bir Çıkış Yolu tüm çıktıları tutamayabilir. Ek Çıkış Yolları eşya çıktı alanını genişletir ancak paralel sınırını yükseltmez. Kapak veya yol eklerken en az 60 gerçek kasa bırak ve ikinci bir Buhar Kapağı kurma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin imha modunu "Yok Etme" olarak ayarla ve her eşya ve sıvı çıktısı için yer sağla. Sıvı imhası etkinse bir Çıkış Kapağı eksik veya tıkalı olduğunda Yapıştırıcı ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik beş blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Dişli Kutusu Kasaları, Boru Muhafazaları ve Külhan Kasaları hologramda gösterildiği gibi konumlandırılmış mı? |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutusu Kasaları, Boru Muhafazaları ve Külhan Kasaları aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik Buhar Kapağı veya Giriş Yolu | Tam olarak bir Buhar Kapağı ve en az bir Buhar Giriş Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Eksik çıktı arayüzü | En az bir Buhar Çıkış Yolu veya sıradan Çıkış Kapağı kurulu mu? Tarifin çıktıları için gerekli iki arayüz türü de kurulu mu? |
| Kapak ekledikten sonra yapı başarısız oluyor | En az 60 gerçek kasa kaldı mı? Dişli Kutusu Kasaları, Boru Muhafazaları veya Külhan Kasalarından herhangi biri kapaklarla değiştirildi mi? |
| Girdiler var ancak tarif bulunamıyor | Eşyanın bir Santrifüj tarifi var mı? Yanlışlıkla bir Termal Santrifüj tarifi mi kontrol edildi? Girdi miktarları, Boş Hücreler ve devre yapılandırması doğru mu? |
| Sıvı girdili LV tarifi işlenmiyor | Bu makine sıradan Girdi Kapaklarını kabul etmez. Gerekli girdi biçimini kabul eden bir Santrifüj kullan. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademe tariflerini işleyemez. |
| Eşya çıktıları görünüyor ancak Yapıştırıcı veya diğer sıvılar eksik | Sıradan bir Çıkış Kapağı kurulu mu? Yanlış sıvıya mı kilitlenmiş? Sıvı imhası etkin mi? Borular ürünü zaten çekmiş olabilir mi? |
| Plantball veya diğer şansa bağlı yan ürün yok | Çıktı şansa bağlı mı? Az sayıda tariften hiçbir şey almamak normal olabilir; ayrıca çıktı alanını ve imha ayarlarını kontrol et. |
| Yetersiz çıktı alanı | Tüm eşya ve sıvı çıktıları için yer var mı? Dört yuvalı bir Çıkış Yolu yetersiz mi? Çıkış Kapakları tıkalı veya yanlış sıvıya mı kilitli? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Bir yolun yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönünü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buhar Ayırıcı](https://wiki.gtnewhorizons.com/wiki/Steam_Separator)