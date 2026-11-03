---
item_ids:
  - gregtech:gt.blockmachines:31078
quest_ids:
  - Plg8vg0gS9Ks2Ddc5sIVOg
navigation:
  title: Steam Squasher
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31078
  position: -501
---
# Steam Squasher
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok Kompresördür. Malzemeleri partiler hâlinde sıkıştırmak için buhar kullanır. Tek bloklu Buharlı Kompresörün yükseltmesi olarak aynı tarifin sekiz kopyasına kadar aynı anda işleyebilir; malzeme blokları, Sıkıştırılmış Ateş Kili ve Sıkıştırılmış Hava Hücreleri üretir.

Makinenin, aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınç yapısına yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez ve özel sıkıştırma kademelerine sahip makinelerin yerini tutmaz.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Pistonlar, Tumbaga Dişlileri, bir Tumbaga Çerçeve ve diğer malzemeleri gerektirir |
| Boyutlar | Üç blok genişliğinde, yedi blok derinliğinde ve üç blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki sıradan Kompresör tarifleri, 32 EU/t'yi aşmayacak şekilde |
| Özel sınır | Özel bir sıkıştırma kademesi gerektiren tarifleri işleyemez; yüksek basınçlı çelik yapı bunları açmaz |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; yüksek basınç yapısı bu sınırı artırmaz |
| İşlem bonusları | Temel yapı, tek bloklu bronz Buharlı Kompresörün hızının %125'inde ve paralel başına buhar tüketim hızının %62,5'inde çalışır |
| Yükseltmeler ve hız aşırtma | Yüksek basınç yapısı hızı ve buhar tüketim hızını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31078" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğlalar, Bronz Boru Muhafazaları ve Demir Blokları kullanır; yüksek basınç yapısı ise bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, boru muhafazaları ve metal blokların tümü aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınç yapısı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda 27; aşağıdaki kapaklar veya yollar ile değiştirilebilir, ancak en az 14 gerçek kasa kalmalıdır |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | On: sekizi ön kontrolcünün etrafında, ikisi daha yapının içindeki ikinci katmanın ortası boyunca |
| Metal blok | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | Altı: önden sayıldığında beşinci sırada, ikinci ve üçüncü katmanların her birinde üç tane |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> | Aynı kontrolcü | Bir, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir, bir kasanın yerine |
| Sıvı Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | İsteğe bağlı, bir kasanın yerine; tarif sıvılarını sağlar |

Yeni yapıda kasalar veya kapaklar için 30 konum vardır. Gerekli üç arayüzün takılması kasa Yapraklarından 27'sini bırakır; bir Sıvı Girdi Kapağı eklemek Yaprakları 26'ya indirir. Daha fazla kapak veya yol eklerken en az 14 gerçek kasa kalmalıdır. Kapaklar ve yollar, Boru Muhafazalarının veya metal blokların yerini alamaz.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınç yapısını seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Steam Squasher, Kompresör tarif haritasını kullanır. NEI'de kontrol ederken önce eşyanın bir Kompresör tarifi olup olmadığını doğrula, sonra kademesini, girdi miktarını, çıktıları ve özel gereksinimleri kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Malzeme blokları yapmak | Uygun metaller genellikle bir metal bloğu yapmak için dokuz külçe kullanır; bazı tozların da blok sıkıştırma tarifleri vardır. Malzeme ve tarif kademesi için NEI'ye bak. |
| İnşaat blokları yapmak | Kil Toplarını, Tuğlaları, Nether Tuğlalarını, Parlak taş Tozunu ve diğer malzemeleri karşılık gelen bloklarına sıkıştırır; örneğin dört tuğla eşyası bir tuğla bloğu yapar |
| Sıkıştırılmış Ateş Kili yapmak | Ateş Kili Tozunu, sonradan pişirilmek üzere Sıkıştırılmış Ateş Kiline sıkıştırır; Kompresör pişirme adımını kendisi yapmaz |
| Sıkıştırılmış Hava Hücreleri üretmek | Boş Hücreleri, sonradan hava işleme için Sıkıştırılmış Hava Hücrelerine sıkıştırır |
| Diğer sıradan sıkıştırma tarifleri | Alaşım Plakalarını ve uygun tariflere sahip diğer malzemeleri işler; uyumluluğu doğrulamak için NEI'deki Kompresör tarifini kontrol et |

### Hava Hücreleri ve Sonraki Oksijen Üretimi

Sıradan bir sıkıştırma tarifi **bir Boş Hücreyi bir Sıkıştırılmış Hava Hücresine** dönüştürür. Boş Hücreler buharlı Giriş Yolundan girer ve Sıkıştırılmış Hava Hücreleri buharlı Çıkış Yolundan çıkar. Bu tarif güç için yalnızca buhar gerektirir; ek su beslemesi, Girdi Kapağından verilen hava veya özel bir hava toplama cihazı gerekmez.

Sıkıştırılmış Hava Hücreleri sonraki oksijen ve azot üretiminde kullanılabilir, ancak bu makine yalnızca Sıkıştırılmış Hava Hücreleri üretir. **Doğrudan Oksijen veya Azot çıkarmaz.** Daha ileri işlemeden önce NEI'de Sıkıştırılmış Hava Hücrelerinin ve Hava sıvısının kullanımlarını kontrol et, sonra bir sonraki makinenin tarifinin gerektirdiği sıvıları, hücreleri ve çıktı arayüzlerini sağla.

Otomasyon için Boş Hücreleri Kompresöre, Sıkıştırılmış Hava Hücrelerini bir sonraki makineye gönder. İşlemden geri dönen Boş Hücreler girdiye geri yönlendirilebilir. Hücre dolaşımı için yeterli tampon bırak, böylece tüm Boş Hücreler diğer makinelerde sıkışıp kalmasın.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar olan tarifleri kabul eder. Yüksek basınçlı çelik yapı makinenin yapı kademesini yükseltir. MV veya daha yüksek kademeli tarifleri ya da özel bir sıkıştırma kademesi gerektiren tarifleri etkinleştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, buharlı Giriş Yolu ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarifi ve girdi miktarını kontrol et ve Çıkış Yolunda yer bırak.
4. Makineyi az miktarda malzemeyle başlat ve çıktı yolunu ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralel sayısını artır.

## Buhar Beslemesi ve Verim

Steam Squasher aynı anda **aynı tarifin** sekiz kopyasına kadar işleyebilir. Bu, bir döngüde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Örneğin, bir blok sıkıştırma tarifi bir metal bloğu yapmak için dokuz külçe kullanıyorsa, sekiz paralel 72 külçe gerektirir ve bir döngüde sekiz metal bloğu üretir.

Temel yapı, tek bloklu bronz Buharlı Kompresörün hızının %125'inde çalışır ve yaklaşık %80 süre alır. Paralel başına buhar tüketim hızı, tek bloklu makinenin hızının %62,5'idir. İki bonusu birleştirmek, aynı malzeme miktarı için toplam buhar tüketiminin yaklaşık %50'sini verir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar talebini artırır.

| Özellik | Temel yapı | Yüksek basınç yapısı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altındaki sıradan Kompresör tarifleri | LV ve altındaki sıradan Kompresör tarifleri |
| Maksimum paralel sayısı | 8 | 8 |
| Temel yapıya göre hız | 1× | 2× |
| Aynı tarif ve paralel sayısı için buhar tüketim hızı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Referans | Temel yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim hızını birlikte artırır. Esas olarak verimi iyileştirir; eşya başına toplam buhar maliyetini bir kez daha yarıya indirmez. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini tutamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim hızına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim hızını kontrol etmek için Waila kullan ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'de paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında buharın tükenmesi mevcut işlemi iptal eder ve tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={2} />
</GameScene>

Yüksek basınç yapısı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Bloklarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Boru Muhafazaları ve Çelik Blokları ile değiştir.

Yükseltmeden önce işlemeyi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı yollar yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim hızını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan.
- **Çıktı:** Çıkış Yolunun ön yüzünden borular, kanallar veya konveyörlerle aktif olarak çek, sonra ürünleri depolamaya veya bir sonraki makineye yönlendir.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Sıradan bir Girdi Kapağı güç için Buhar Kapağının yerini alamaz.
- **Tarif sıvıları:** Yalnızca NEI tarifi bir sıvı girdisi gerektirdiğinde ek bir sıradan Girdi Kapağı tak ve karşılık gelen sıvıyı sağla. Sıkıştırılmış Hava Hücreleri üretmek bu arayüzü gerektirmez.
- **Yönlendirme:** Malzeme blokları, Sıkıştırılmış Ateş Kili, Sıkıştırılmış Hava Hücreleri ve diğer ürünler için filtreler ayarla, böylece hava hücreleri malzeme deposuna girmez ve pişirilmesi gereken ara ürünler çıktıda kalmaz.

Blok sıkıştırma tarifleri genellikle aynı anda birkaç eşya tüketir. Girdi tamponunu "tarif başına girdi × hedef paralel" için boyutlandır. Girdi yuvalarını birçok farklı malzemenin az miktarlarıyla doldurmaktan kaçın; aksi hâlde her birinden tek bir tarif için bile çok az kalır.

Ek Giriş Yolları eşya tamponunu genişletir, ek Çıkış Yolları ise çıktı tıkanıklığını önlemeye yardımcı olur. Hiçbiri paralel sınırını artırmaz. Genişletirken en az 14 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Yeni yapı tamamlanmıyor | Yapı üç blok genişliğinde, yedi blok derinliğinde ve üç blok yüksekliğinde mi? Kontrolcü ikinci katmanın ön ortasında mı? On Boru Muhafazası ve altı metal blok doğru konumda mı? |
| Yapı kademesi uyuşmuyor | Kasalar, Boru Muhafazaları ve metal blokların tümü aynı kademede mi? Yalnızca bazı bronz bileşenler mi değiştirildi, yoksa Demir Blokları mı kaldı? |
| Buhar Kapağı veya yollar eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapaklar eklendikten sonra yapı hata veriyor | En az 14 gerçek kasa kaldı mı? Herhangi bir Boru Muhafazası veya metal blok kapak ya da yolla değiştirildi mi? |
| Girdiler var ama tarif bulunamıyor | Eşyanın bir Kompresör tarifi var mı? Bir tarif için yeterli girdi var mı? Tarif bir sıkıştırma kademesi gerektiriyor mu? Yeterli çıktı alanı var mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınç yapısı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Boş Hücreler Oksijen Hücresine dönüşmüyor | Kompresör Sıkıştırılmış Hava Hücreleri üretir. Oksijen ve Azot, diğer makinelerde daha ileri işleme gerektirir. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buharlı yollar eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin sekiz kopyası için yeterli girdi var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri tutabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multibloklar](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Steam Squasher](https://wiki.gtnewhorizons.com/wiki/Steam_Squasher)