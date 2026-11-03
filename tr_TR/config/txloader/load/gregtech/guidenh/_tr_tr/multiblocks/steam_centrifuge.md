---
item_ids:
  - gregtech:gt.blockmachines:31080
navigation:
  title: Buhar Ayırıcı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31080
  position: 5
quest_ids:
  - 0rUmaWIPQPaL93q-_pgKXw
---

# Buhar Ayırıcı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" />, Buhar Çağı'nda kullanılabilen multiblok bir Santrifüj'dür. Malzemeleri partiler halinde ayırmak için buhar kullanır ve aynı tarifin sekiz kopyasına kadar aynı anda işleyebilir. Cevher tozlarını saflaştırabilir, Yapışkan Reçine'den Ham Kauçuk Tozu elde edebilir ve Santrifüj tariflerinden eşya ve sıvı çıktıları toplayabilir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Uygun Santrifüj tariflerini Buhar Çağı'nda kullanılabilir hale getirir. Yüksek basınçlı yapıya yükseltme işlem hacmini artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Dökme Demir Plakalar, Bronz Dişliler, bir Tumbaga Çerçeve Kutusu ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, beş blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki, 32 EU/t'den fazlasını gerektirmeyen Santrifüj tarifleri |
| Girişler ve çıkışlar | Buhar Giriş Yolları eşya kabul eder, buhar Çıkış Yolları eşya verir ve sıradan Çıkış Kapakları sıvı verir; sıradan Girdi Kapakları kabul edilmez |
| Paraleller | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı artırmaz |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı veya yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve overclock | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31080" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Çıkış Kapağı varsayar; böylece hem eşya hem de sıvı çıktıları toplanabilir. Temel yapı bronz bileşenleri kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları, Boru Kasaları ve Külhan Kasaları tamamen aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzenekte 65 adet; aşağıdaki kapaklar veya veriyollarıyla değiştirilebilir, ancak en az 60 gerçek kasa kalmalı |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz adet: ikinci ve dördüncü katmanların her birinde merkezdeki Külhan Kasasının çevresinde dört adet |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Dört adet, üçüncü katmanda merkezdeki Külhan Kasasının çevresinde |
| Külhan Kasası | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Üç adet: ikinci, üçüncü ve dördüncü katmanların her birinin merkezinde birer adet |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı veriyolu | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı veriyolu | Eşya çıktıları için gerektiği kadar tak, bir kasanın yerine |
| Çıkış Kapağı | Örneğin <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıktıları için gerektiği kadar tak, bir kasanın yerine |

Yapıda kasa veya kapak için 69 konum vardır. Yukarıda listelenen dört arayüzün takılması 65 kasa bırakır. Yalnızca eşya çıktılı tarifler işlenecekse Çıkış Kapağını atlamak bunun yerine 66 kasa gerektirir. Veriyolu veya Çıkış Kapağı eklemek kasa sayısını buna göre azaltır, ancak en az 60 gerçek kasa kalmalıdır. Kapaklar ve veriyolları Dişli Kutusu Kasalarının, Boru Kasalarının veya Külhan Kasalarının yerini alamaz.

Katmanları tabandan yukarı doğru say. Kasa düzeni katmanlar arasında farklıdır, bu yüzden etkileşimli yapıyı veya hologramı takip et; boş konumların doldurulması gerekmez. En az bir buhar Çıkış Yolu veya sıradan Çıkış Kapağı tak. Bir tarif hem eşya hem sıvı üretiyorsa her iki çıktı arayüzü türünü de tak.

Külhan Kasaları yapı bloklarıdır. Yakıta veya ayrı bir su beslemesine ihtiyaç duymazlar. Makine için buhar harici bir kazan tarafından üretilir ve Buhar Kapağı üzerinden sağlanır.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makinenin Kullanımları

Buhar Ayırıcı, Santrifüj tarif haritasını kullanır. NEI'yi kontrol ederken önce tarifin **Santrifüj**'e ait olduğunu doğrula, ardından kademesini, giriş biçimini, Programlanmış Devre yapılandırmasını ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Cevher tozlarını saflaştırma | Uygun Saf Olmayan Toz, Temizlenmiş Toz ve diğer ara ürünleri sıradan toza ve ilgili yan ürünlere dönüştürür; her mineralin miktarları ve çıktı biçimleri için NEI'ye bak |
| Yapışkan Reçine işleme | Ham Kauçuk Tozu, bir Bitki Topu şansı ve Yapıştırıcı üretir; hem eşya hem sıvı çıktıları ele alınmalıdır |
| Kütükleri santrifüjleme | Uygun kütük tarifleri Metan üretirken Kauçuk Ağacı'nın ayrıca şansa bağlı eşya çıktıları vardır; NEI'nin gerektirdiği Programlanmış Devre yapılandırmasını kontrol et |
| Mineralleri ve malzemeleri ayırma | Uygun Netherrack Tozu, Endstone Tozu ve diğer Santrifüj tariflerini işler; toplanacak birden çok eşya veya sıvı çıktısı vardır |
| Hücre tarifleri | Yalnızca girdisi eşya olan Santrifüj tariflerini işler; bazı tarifler ayrıca ek Boş Hücre gerektirir, bu yüzden tek başına dolu bir hücre gerekli tüm girdileri sağlamayabilir |

### Yapışkan Reçine ve Kauçuk

Güncel Yapışkan Reçine tarifi **bir Yapışkan Reçine** tüketir ve **üç Ham Kauçuk Tozu ile 100 L Yapıştırıcı** üretir; **%10 şansla bir Bitki Topu** da verir.

Yapışkan Reçineyi buhar Giriş Yoluna gönder, Ham Kauçuk Tozu ve Bitki Toplarını buhar Çıkış Yolu üzerinden topla ve Yapıştırıcıyı sıradan bir Çıkış Kapağı üzerinden topla. Yapıştırıcı bir tarif çıktısıdır. **Onu almak için Girdi Kapağı takma.**

Sekiz paralelde bir döngü sekiz Yapışkan Reçine tüketir ve 24 Ham Kauçuk Tozu ile 800 L Yapıştırıcı üretir. Bitki Topları şansa bağlı çıktı olarak kalır; bir döngünün sekiz adet üretmesi garanti değildir. Sürekli çalıştırmadan önce her iki eşya türü için de yer bırak ve Yapıştırıcıyı sürekli çekmek için sıvı boruları kullan.

### Sıvı Girişi Sınırı

Bu makine sıvı **çıktılarını** destekler, ancak sıradan Sıvı Girdi Kapaklarını kabul etmez. NEI'de sıvı girdisi gerektiren tarifler LV veya altında olsalar bile sıradan bir Girdi Kapağı eklenerek etkinleştirilemez. Buhar Kapağı güç sağlar ve Hava veya asitler gibi tarif sıvıları için giriş görevi göremez.

Örneğin NEI'de doğrudan Hava sıvısı alan bir Santrifüj tarifi, sıvı girdilerini kabul eden bir Santrifüj gerektirir. Dolu hücreler, yalnızca ilgili tarif onları açıkça **eşya girdisi** olarak listeliyorsa buhar Giriş Yoluna gönderilebilir.

> [!NOTE]
> Makine Buhar Çağı'nda kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademeli tarifleri etkinleştirmez ve sıvı girişi sınırını kaldırmaz.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, buhar Giriş Yolu ve gerekli çıktı arayüzlerinin takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarif kademesini, tüm girdileri ve Programlanmış Devre yapılandırmasını, sıvı girdisi gerekip gerekmediği dahil kontrol et.
4. Tüm eşya ve sıvı çıktıları için yer bırak, sonra az miktarda malzemeyle başla; çıktıları ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini ve çıktı toplamayı doğruladıktan sonra girdi miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve İşlem Hacmi

Buhar Ayırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alırken yüksek basınçlı yapı yaklaşık 0,8 katını alır. Örneğin 15 saniye olarak gösterilen Yapışkan Reçine tarifi temel yapıda yaklaşık 24 saniye, yüksek basınçlı yapıda ise 12 saniye sürer. Paraleller bir döngüde işlenen tarif sayısını artırır ancak döngü süresini paralel sayısına bölmez.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6 katı | Yaklaşık 0,8 katı |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |

Yüksek basınçlı yükseltme hızı ve buhar tüketim oranını birlikte artırır. Esas olarak işlem hacmini iyileştirir ve eşya başına toplam buhar maliyeti temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici açıkları kapatır ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır. Paralelleri artırırken eşya girişi, eşya çıkışı ve sıvı çıkışı da yetişmelidir.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila kullan ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t cinsinden gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru işlem hacmini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında buharın tükenmesi mevcut işlemi iptal eder ve zaten tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru işlem hacmini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlalarını, Bronz Dişli Kutusu Kasalarını, Bronz Boru Kasalarını ve Bronz Külhan Kasalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları, Çelik Boru Kasaları ve Çelik Külhan Kasalarıyla değiştir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buharı ve üretimi geri yüklemeden önce makinenin yüksek basınçlı yapı kademesini gösterdiğini doğrula.

Yüksek basınçlı yapı, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı, buhar veriyolları ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Çıktı Yönlendirme

Buhar Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik olarak çekmezler veya ürünleri onlara itmezler; bir veriyolunun yanına sandık koymak otomasyon için yeterli değildir.

- **Giriş:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Ayrıca tarifin gerektirdiği Boş Hücreleri ve Programlanmış Devre yapılandırmasını da sağla.
- **Eşya çıkışı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek, sonra ürünleri ana çıktı deposuna, yan ürün deposuna veya bir sonraki makineye yönlendir.
- **Sıvı çıkışı:** Yapıştırıcı, Metan ve diğer ürünleri sıradan Çıkış Kapaklarından çek. Her sıvı türü için depolama ve filtreleri yapılandır ve birden çok sıvı çıktılı tarifler için yeterli Çıkış Kapağı sağla.
- **Buhar:** Buhar Kapağına ayrı bir buhar besleme hattı bağla ve sıvı ürün hatlarını ondan uzak tut.
- **Cevher yönlendirme:** Sıradan toz, Saf Olmayan Toz, Temizlenmiş Toz ve küçük yan ürünler için filtreler ayarla; böylece zaten santrifüjlenmiş eşyalar giriş tamponunu tekrar doldurmaz.

Santrifüj tarifleri genellikle aynı anda birkaç farklı eşya üretir. Dört yuvalı tek bir Çıkış Yolu tüm çıktıları tutmayabilir. Ek Çıkış Yolları eşya çıkış alanını genişletir ancak paralel sınırını yükseltmez. Kapak veya veriyolu eklerken en az 60 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin yok etme modunu "Yok Etme" olarak ayarla ve her eşya ve sıvı çıktısı için yer sağla. Sıvı yok etme etkinse, bir Çıkış Kapağı eksik veya tıkalı olduğunda Yapıştırıcı ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik beş blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Dişli Kutusu Kasaları, Boru Kasaları ve Külhan Kasaları hologramda gösterildiği gibi konumlanmış mı? |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutusu Kasaları, Boru Kasaları ve Külhan Kasaları tamamen aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Buhar Kapağı veya Giriş Yolu eksik | Tam olarak bir Buhar Kapağı ve en az bir buhar Giriş Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya veriyolları mı kullanıldı? |
| Çıktı arayüzü eksik | En az bir buhar Çıkış Yolu veya sıradan Çıkış Kapağı takılı mı? Tarifin çıktıları için gerekli her iki arayüz türü de takılı mı? |
| Kapaklar eklendikten sonra yapı başarısız | En az 60 gerçek kasa kaldı mı? Dişli Kutusu Kasalarından, Boru Kasalarından veya Külhan Kasalarından herhangi biri kapaklarla mı değiştirildi? |
| Girdiler var ama tarif bulunamıyor | Eşyanın Santrifüj tarifi var mı? Yanlışlıkla Termal Santrifüj tarifi mi kontrol edildi? Girdi miktarları, Boş Hücreler ve devre yapılandırması doğru mu? |
| Sıvı girdili LV tarifi işlenmiyor | Bu makine sıradan Girdi Kapaklarını kabul etmez. Gerekli giriş biçimini kabul eden bir Santrifüj kullan. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Eşya çıktıları görünüyor ama Yapıştırıcı veya diğer sıvılar eksik | Sıradan bir Çıkış Kapağı takılı mı? Yanlış sıvıya mı kilitlenmiş? Sıvı yok etme etkin mi? Borular ürünü zaten çekmiş olabilir mi? |
| Bitki Topu veya diğer şansa bağlı yan ürün yok | Çıktı şansa bağlı mı? Az sayıda tariften hiçbir şey almamak normal olabilir; çıktı alanını ve yok etme ayarlarını da kontrol et. |
| Yetersiz çıktı alanı | Tüm eşya ve sıvı çıktıları için yer var mı? Dört yuvalı tek Çıkış Yolu yetersiz mi? Çıkış Kapakları tıkalı veya yanlış sıvıya mı kilitli? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınçlı yapı kademesi kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buhar veriyolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarma ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Çince Wiki: Buhar Ayırıcı](https://gtnh.huijiwiki.com/wiki/大型蒸汽离心机)