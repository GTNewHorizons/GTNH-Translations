---
item_ids:
  - gregtech:gt.blockmachines:31080
navigation:
  title: Buhar Ayırıcı
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31080
  position: 5
quest_ids:
  - 0rUmaWIPQPaL93q-_pgKXw
---

# Buhar Ayırıcı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" />, Buhar çağında kullanılabilen multiblok bir Santrifüjdür. Malzemeleri partiler hâlinde ayırmak için buhar kullanır ve aynı tarifin sekiz kopyasına kadarını tek seferde işleyebilir. Cevher tozlarını arıtabilir, Yapışkan Reçineden Ham Kauçuk Tozu elde edebilir ve Santrifüj tariflerinin eşya ve sıvı çıktılarını toplayabilir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Uygun Santrifüj tariflerini Buhar çağında kullanılabilir hâle getirir. Yüksek basınçlı yapıya yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Dökme Demir Plakalar, Bronz Dişliler, bir Tumbaga Çerçeve Kutusu ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, beş blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altı Santrifüj tarifleri; en fazla 32 EU/t gerektirir |
| Girişler ve çıkışlar | Buhar Giriş Yolları eşya kabul eder, Buhar Çıkış Yolları eşya verir ve normal Çıkış Kapakları sıvı verir; normal Girdi Kapakları kabul edilmez |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve overclock | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcünün, temel kasanın ve Buhar Kapağının mevcut tarifleri aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31080" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu ve bir Çıkış Kapağı varsayar; böylece hem eşya hem de sıvı çıktıları toplanabilir. Temel yapı bronz bileşenleri kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Dişli Kutusu Kasaları, boru muhafazası blokları ve Külhan Kasaları aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzenekte 65; aşağıdaki kapaklar veya veriyollarıyla değiştirilebilir, ancak en az 60 gerçek kasa kalmalıdır |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Sekiz: ikinci ve dördüncü katmanların her birinde merkezdeki Külhan Kasasının çevresinde dört |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Dört, üçüncü katmanda merkezdeki Külhan Kasasının çevresinde |
| Külhan Kasası | <ItemLink id="gregtech:gt.blockcasings3:13" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings3:14" showIcon="left" /> | Üç: ikinci, üçüncü ve dördüncü katmanların her birinin merkezinde bir |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31080" showIcon="left" /> | Aynı kontrolcü | Bir, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı veriyolu | En az bir, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı veriyolu | Eşya çıktıları için gerektiği kadar tak, bir kasanın yerine |
| Çıkış Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıktıları için gerektiği kadar tak, bir kasanın yerine |

Yapıda kasa veya kapak için 69 konum vardır. Yukarıda listelenen dört arayüz takıldığında 65 kasa kalır. Yalnızca eşya çıktısı olan tarifler işlenecekse, Çıkış Kapağını atlamak bunun yerine 66 kasa gerektirir. Veriyolu veya Çıkış Kapağı eklemek kasa sayısını buna göre azaltır, ancak en az 60 gerçek kasa kalmalıdır. Kapaklar ve veriyolları Dişli Kutusu Kasalarının, boru muhafazası bloklarının veya Külhan Kasalarının yerini alamaz.

Katmanları tabandan yukarı doğru say. Kasa düzeni katmanlar arasında farklılık gösterir; bu yüzden etkileşimli yapıyı veya hologramı takip et; boş konumların doldurulması gerekmez. En az bir Buhar Çıkış Yolu veya normal Çıkış Kapağı tak. Bir tarif hem eşya hem sıvı üretiyorsa, her iki çıkış arayüzü türünü de tak.

Külhan Kasaları yapı bloğudur. Yakıta veya ayrı bir su kaynağına ihtiyaçları yoktur. Makinenin buharı harici bir kazan tarafından üretilir ve Buhar Kapağı üzerinden sağlanır.

<ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> aracını yapıyı önizlemek ve inşa etmeye yardımcı olmak için kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Buhar Ayırıcı, Santrifüj tarif haritasını kullanır. NEI'ye bakarken önce tarifin **Santrifüj**e ait olduğunu doğrula, ardından kademesini, giriş biçimini, Programlanmış Devre yapılandırmasını ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Cevher tozlarını arıtma | Uygun Saf Olmayan Toz, Temizlenmiş Toz ve diğer ara ürünleri normal toza ve ilgili yan ürünlere dönüştürür; her mineralin miktarları ve çıktı biçimleri için NEI'ye bak |
| Yapışkan Reçineyi işleme | Ham Kauçuk Tozu, şansla bir Bitki Topu ve Yapıştırıcı üretir; hem eşya hem sıvı çıktıları ele alınmalıdır |
| Kütükleri santrifüjleme | Uygun kütük tarifleri Metan üretir; Kauçuk Ağacının ayrıca şansa bağlı eşya çıktıları vardır; NEI'nin gerektirdiği Programlanmış Devre yapılandırmasını kontrol et |
| Mineralleri ve malzemeleri ayırma | Uygun Netherrack Tozu, End Taşı Tozu ve diğer Santrifüj tariflerini işler; toplanacak birden fazla eşya veya sıvı çıktısı vardır |
| Hücre tarifleri | Yalnızca girişleri eşya olan Santrifüj tariflerini işler; bazı tarifler ayrıca ek Boş Hücreler gerektirir, bu yüzden tek başına dolu bir hücre gerekli tüm girişleri sağlamayabilir |

### Yapışkan Reçine ve Kauçuk

Mevcut Yapışkan Reçine tarifi **bir Yapışkan Reçine** tüketir ve **üç Ham Kauçuk Tozu ile 100 L Yapıştırıcı** üretir; **%10 şansla bir Bitki Topu** da üretir.

Yapışkan Reçineyi Buhar Giriş Yoluna gönder, Ham Kauçuk Tozu ve Bitki Toplarını bir Buhar Çıkış Yolu üzerinden, Yapıştırıcıyı ise normal bir Çıkış Kapağı üzerinden topla. Yapıştırıcı bir tarif çıktısıdır. **Onu almak için Girdi Kapağı takma.**

Sekiz paralelde bir çevrim sekiz Yapışkan Reçine tüketir ve 24 Ham Kauçuk Tozu ile 800 L Yapıştırıcı üretir. Bitki Topları şansa bağlı çıktı olarak kalır; bir çevrimin sekiz tane üretmesi garanti değildir. Sürekli çalıştırmadan önce her iki eşya türü için yer bırak ve Yapıştırıcıyı sürekli çekmek için sıvı boruları kullan.

### Sıvı Giriş Sınırı

Bu makine sıvı **çıktılarını** destekler, ancak normal Sıvı Girdi Kapaklarını kabul etmez. NEI'de sıvı girişi gerektiren tarifler, LV veya altında olsalar bile normal bir Girdi Kapağı eklenerek etkinleştirilemez. Buhar Kapağı güç sağlar ve Hava veya asitler gibi tarif sıvıları için giriş görevi göremez.

Örneğin, NEI'de doğrudan Hava sıvısı alan bir Santrifüj tarifi, sıvı girişlerini kabul eden bir Santrifüj gerektirir. Dolu hücreler, ancak ilgili tarif onları açıkça **eşya girişi** olarak listeliyorsa Buhar Giriş Yoluna gönderilebilir.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademeli tarifleri etkinleştirmez ve sıvı giriş sınırını kaldırmaz.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, Buhar Giriş Yolunun ve gerekli çıkış arayüzlerinin takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarif kademesini, tüm girişleri ve Programlanmış Devre yapılandırmasını, sıvı girişi gerekip gerekmediği dahil kontrol et.
4. Tüm eşya ve sıvı çıktıları için yer bırak, ardından az miktarda malzemeyle başla ve çıktıları ile buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini ve çıktı toplamayı doğruladıktan sonra giriş miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve Verim

Buhar Ayırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir çevrimde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca giriş miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı, NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alırken yüksek basınçlı yapı yaklaşık 0,8 katını alır. Örneğin 15 saniye olarak gösterilen Yapışkan Reçine tarifi, temel yapıda yaklaşık 24 saniye, yüksek basınçlı yapıda ise 12 saniye sürer. Paraleller bir çevrimde işlenen tarif sayısını artırır, ancak çevrim süresini paralel sayısına bölmez.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6 kat | Yaklaşık 0,8 kat |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1 kat | 2 kat |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |

Yüksek basınçlı yapıya yükseltmek, hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi iyileştirir; eşya başına toplam buhar maliyeti temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici kısa süreli eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır. Paralelleri artırırken eşya girişi, eşya çıkışı ve sıvı çıkışı da yetişmelidir.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek ve sürekli işlem sırasında tamponun sürekli düşüp düşmediğini izlemek için Waila'yı kullan. Değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'de paralel sınırını düşür, ardından kazan üretimini artır veya boru hattını iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen malzemeler geri verilmez. Yüksek basınçlı yapıya yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31080" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Dişli Kutusu Kasalarını, Bronz boru muhafazası bloklarını ve Bronz Külhan Kasalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Dişli Kutusu Kasaları, Çelik boru muhafazası blokları ve Çelik Külhan Kasalarıyla değiştir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınçlı kademeyi gösterdiğini doğrula.

Yüksek basınçlı yapı, makinenin yapı kademesidir. Yine normal buhar kullanır ve mevcut Buhar Kapağı, Buhar Giriş/Çıkış Yolları ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Çıktı Yönlendirme

Buhar Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir veriyolunun yanına sandık koymak otomasyon için yeterli değildir.

- **Giriş:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Ayrıca tarifin gerektirdiği Boş Hücreleri ve Programlanmış Devre yapılandırmasını sağla.
- **Eşya çıktısı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek, ardından ürünleri ana çıktı deposuna, yan ürün deposuna veya bir sonraki makineye yönlendir.
- **Sıvı çıktısı:** Yapıştırıcı, Metan ve diğer ürünleri normal Çıkış Kapaklarından çek. Her sıvı türü için depolama ve filtre yapılandır, birden fazla sıvı çıktısı olan tarifler için yeterli Çıkış Kapağı sağla.
- **Buhar:** Buhar Kapağına ayrı bir buhar besleme hattı bağla ve sıvı ürün hatlarını ondan uzak tut.
- **Cevher yönlendirmesi:** Normal toz, Saf Olmayan Toz, Temizlenmiş Toz ve küçük yan ürünler için filtreler ayarla; böylece zaten santrifüjlenmiş eşyalar giriş tamponunu tekrar doldurmaz.

Santrifüj tarifleri genellikle aynı anda birkaç farklı eşya üretir. Dört yuvalı tek bir Çıkış Yolu tüm çıktıları tutamayabilir. Ek Çıkış Yolları eşya çıkış alanını genişletir, ancak paralel sınırını yükseltmez. Kapak veya veriyolu eklerken en az 60 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm yan ürünleri toplamak için GUI'nin boşaltma modunu "Boşaltma Yapma" olarak ayarla ve her eşya ile sıvı çıktısı için yer sağla. Sıvı boşaltma etkinse, bir Çıkış Kapağı eksik veya tıkalı olduğunda Yapıştırıcı ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Neye bakmalısın |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik beş blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Dişli Kutusu Kasaları, boru muhafazası blokları ve Külhan Kasaları hologramda gösterildiği gibi mi konumlanmış? |
| Yapı kademesi uyuşmazlığı | Kasalar, Dişli Kutusu Kasaları, boru muhafazası blokları ve Külhan Kasalarının tümü aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik Buhar Kapağı veya Giriş Yolu | Tam olarak bir Buhar Kapağı ve en az bir Buhar Giriş Yolu var mı? Yanlışlıkla normal elektrikli makine eşya veriyolları mı kullanıldı? |
| Eksik çıkış arayüzü | En az bir Buhar Çıkış Yolu veya normal Çıkış Kapağı takılı mı? Tarifin çıktıları için gerekli iki arayüz türü de takılı mı? |
| Kapaklar eklendikten sonra yapı bozuluyor | En az 60 gerçek kasa kaldı mı? Dişli Kutusu Kasaları, boru muhafazası blokları veya Külhan Kasalarından herhangi biri kapakla değiştirildi mi? |
| Girişler var ama tarif bulunamıyor | Eşyanın Santrifüj tarifi var mı? Yanlışlıkla Termal Santrifüj tarifi mi kontrol edildi? Giriş miktarları, Boş Hücreler ve devre yapılandırması doğru mu? |
| Sıvı girişli LV tarifi işlenmiyor | Bu makine normal Girdi Kapaklarını kabul etmez. Gerekli giriş biçimini kabul eden bir Santrifüj kullan. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Eşya çıktıları görünüyor ama Yapıştırıcı veya diğer sıvılar eksik | Normal bir Çıkış Kapağı takılı mı? Yanlış sıvıya mı kilitlenmiş? Sıvı boşaltma etkin mi? Borular ürünü çoktan çekmiş olabilir mi? |
| Bitki Topu veya diğer şansa bağlı yan ürünler yok | Çıktı şansa bağlı mı? Az sayıda tariften hiç çıkmaması normal olabilir; çıktı alanını ve boşaltma ayarlarını da kontrol et. |
| Yetersiz çıktı alanı | Tüm eşya ve sıvı çıktıları için yer var mı? Dört yuvalı tek bir Çıkış Yolu yetersiz mi? Çıkış Kapakları tıkalı veya yanlış sıvıya kilitli mi? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınçlı kademe kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buhar veriyolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönünü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](../multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buhar Ayırıcı](https://wiki.gtnewhorizons.com/wiki/Steam_Separator)