---
item_ids:
  - gregtech:gt.blockmachines:31078
navigation:
  title: Buharlı Pres
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31078
  position: 4
quest_ids:
  - Plg8vg0gS9Ks2Ddc5sIVOg
---

# Buharlı Pres

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> Buhar çağında kullanılabilen bir multiblok Kompresördür. Malzemeleri parti hâlinde sıkıştırmak için buhar kullanır. Tek bloklu Buharlı Kompresörün yükseltmesi olarak, aynı tarifin sekiz kopyasını aynı anda işleyebilir; malzeme blokları, Sıkıştırılmış Şamot ve Sıkıştırılmış Hava Hücreleri üretir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınçlı yapıya yükseltmek işlem hacmini artırır, ancak maksimum tarif kademesini yükseltmez veya özel sıkıştırma kademelerine sahip makinelerin yerini tutmaz.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | Buhar; kontrolcü tarifi Pistonlar, Tumbaga Dişlileri, bir Tumbaga Çerçeve ve diğer malzemeleri gerektirir |
| Boyutlar | Üç blok genişliğinde, yedi blok derinliğinde ve üç blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV ve altındaki sıradan Kompresör tarifleri; en fazla 32 EU/t gerektirir |
| Özel sınır | Özel sıkıştırma kademesi gerektiren tarifleri işleyemez; yüksek basınçlı çelik yapı bunların kilidini açmaz |
| Paralel işlem | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşlem bonusları | Temel yapı, tek bloklu bronz Buharlı Kompresörün hızının %125'inde ve paralel başına buhar tüketim hızının %62,5'inde çalışır |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim hızını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşaat

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki öğelere tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31078" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplı Tuğlalar, Bronz Boru Muhafazaları ve Demir Blokları kullanır; yüksek basınçlı yapı ise bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Boru Muhafazaları ve metal blokların tümü aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel düzende 27; aşağıdaki kapaklar veya yollarla değiştirilebilir, ancak en az 14 gerçek kasa kalmalıdır |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | On: sekiz tanesi öndeki kontrolcünün etrafında, iki tanesi daha yapının içinde ikinci katmanın ortasında |
| Metal blok | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | Altı: önden sayıldığında beşinci sırada, ikinci ve üçüncü katmanların her birinde üç tane |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> | Aynı kontrolcü | Bir, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir, bir kasanın yerine |
| Sıvı Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | İsteğe bağlı, bir kasanın yerine; tarif sıvılarını sağlar |

Yeni yapıda kasa veya kapaklar için 30 konum vardır. Gerekli üç arayüzün takılması 27 kasa bırakır; bir Sıvı Girdi Kapağı eklenmesi 26 bırakır. Daha fazla kapak veya yol eklerken en az 14 gerçek kasa kalmalıdır. Kapaklar ve yollar Boru Muhafazalarının veya metal blokların yerini alamaz.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademe 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşaatın ardından kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Buharlı Pres, Kompresör tarif haritasını kullanır. NEI'yi kontrol ederken önce öğenin bir Kompresör tarifi olup olmadığını doğrula, sonra kademesini, girdi miktarını, çıktılarını ve özel gereksinimlerini kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Malzeme blokları yapmak | Uygun metaller genellikle bir metal bloğu yapmak için dokuz külçe kullanır; bazı tozların da blok sıkıştırma tarifleri vardır. Malzeme ve tarif kademesi için NEI'yi kontrol et. |
| İnşaat blokları yapmak | Kil Toplarını, Tuğlaları, Nether Tuğlalarını, Parlak taş Tozunu, Yaprakları ve diğer malzemeleri karşılık gelen bloklarına sıkıştırır; örneğin dört tuğla öğesi bir tuğla bloğu yapar |
| Sıkıştırılmış Şamot yapmak | Şamot Tozunu daha sonra pişirilmek üzere Sıkıştırılmış Şamota sıkıştırır; Kompresör pişirme adımını kendisi yapmaz |
| Sıkıştırılmış Hava Hücreleri üretmek | Boş Hücreleri daha sonraki hava işlemesi için Sıkıştırılmış Hava Hücrelerine sıkıştırır |
| Diğer sıradan sıkıştırma tarifleri | Alaşım Plakalarını ve uygun tariflere sahip diğer malzemeleri işler; uyumluluğu doğrulamak için NEI'deki Kompresör tarifini kontrol et |

### Hava Hücreleri ve Sonraki Oksijen Üretimi

Sıradan bir sıkıştırma tarifi **bir Boş Hücreyi bir Sıkıştırılmış Hava Hücresine** dönüştürür. Boş Hücreler buharlı Giriş Yolundan girer ve Sıkıştırılmış Hava Hücreleri buharlı Çıkış Yolundan çıkar. Bu tarif güç için yalnızca buhar gerektirir; ek bir su kaynağı, Girdi Kapağı aracılığıyla sağlanan hava veya özel bir hava toplama cihazı gerektirmez.

Sıkıştırılmış Hava Hücreleri sonraki oksijen ve azot üretiminde kullanılabilir, ancak bu makine yalnızca Sıkıştırılmış Hava Hücreleri üretir. **Doğrudan oksijen veya azot vermez.** Daha ileri işlemeden önce NEI'de Sıkıştırılmış Hava Hücrelerinin ve Hava sıvısının kullanımlarını kontrol et, ardından sonraki makinenin tarifinin gerektirdiği sıvıları, hücreleri ve çıktı arayüzlerini sağla.

Otomasyon için Boş Hücreleri Kompresöre ve Sıkıştırılmış Hava Hücrelerini sonraki makineye gönder. İşlemden dönen Boş Hücreler girdiye geri yönlendirilebilir. Hücre dolaşımı için yeterli tampon bırak, böylece tüm Boş Hücreler diğer makinelerde sıkışıp kalmasın.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar olan tarifleri kabul eder. Yüksek basınçlı çelik yapı makinenin yapı kademesini yükseltir. MV veya daha yüksek kademeli tarifleri ya da özel sıkıştırma kademesi gerektiren tarifleri etkinleştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buharlı Giriş Yolunun ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarifi ve girdi miktarını kontrol et ve Çıkış Yolunda boş yer bırak.
4. Makineyi az miktarda malzemeyle başlat ve çıktı güzergâhını ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralel sayısını artır.

## Buhar Beslemesi ve İşlem Hacmi

Buharlı Pres, **aynı tarifin** en fazla sekiz kopyasını aynı anda işleyebilir. Bu, tek bir döngüde sekiz farklı öğeyi işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Örneğin, bir blok sıkıştırma tarifi bir metal bloğu yapmak için dokuz külçe kullanıyorsa, sekiz paralel 72 külçe gerektirir ve tek döngüde sekiz metal bloğu üretir.

Temel yapı, tek bloklu bronz Buharlı Kompresörün hızının %125'inde çalışır ve yaklaşık %80'i kadar süre alır. Paralel başına buhar tüketim hızı, tek bloklu makinenin hızının %62,5'idir. İki bonus birleştiğinde aynı miktarda malzeme için toplam buhar tüketiminin yaklaşık %50'si elde edilir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar talebini artırır.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altındaki sıradan Kompresör tarifleri | LV ve altındaki sıradan Kompresör tarifleri |
| Maksimum paralel | 8 | 8 |
| Temel yapıya göre hız | 1× | 2× |
| Aynı tarif ve paralel sayısı için buhar tüketim hızı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Referans | Temel yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim hızını birlikte artırır. Esas olarak işlem hacmini iyileştirir, öğe başına toplam buhar maliyetini yeniden yarıya indirmez. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim hızına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim hızını kontrol etmek için Waila'yı kullan ve sürekli işlem boyunca tamponun düşmeye devam edip etmediğini izle. Bir değer L/t cinsinden gösteriliyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru işlem hacmini karşılaştırırken eşleşen birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında buharın tükenmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru işlem hacmini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Bloklarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Boru Muhafazaları ve Çelik Bloklarıyla değiştir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buharı ve üretimi geri açmadan önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı ve buharlı yollar yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim hızını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Öğe Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her birinde dört öğe yuvası vardır. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Öğeleri Giriş Yolunun ön yüzüne göndermek için huniler, GT öğe boruları, konveyörler veya öğe kanalları kullan.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek ve ürünleri depolamaya veya sonraki makineye yönlendir.
- **Buhar:** Sıvı borularını kazandan Buhar Kapağına bağla. Sıradan bir Girdi Kapağı güç için Buhar Kapağının yerini alamaz.
- **Tarif sıvıları:** Yalnızca NEI tarifi sıvı girdisi gerektirdiğinde ek bir sıradan Girdi Kapağı tak ve ilgili sıvıyı sağla. Sıkıştırılmış Hava Hücreleri üretmek bu arayüzü gerektirmez.
- **Yönlendirme:** Hava hücrelerinin malzeme deposuna girmemesi ve pişirilmesi gereken ara ürünlerin çıktıda kalmaması için malzeme blokları, Sıkıştırılmış Şamot, Sıkıştırılmış Hava Hücreleri ve diğer ürünler için filtreler ayarla.

Blok sıkıştırma tarifleri genellikle aynı anda birkaç öğe tüketir. Girdi tamponunu "tarif başına girdi × hedef paralel" için boyutlandır. Girdi yuvalarını birçok farklı malzemenin küçük miktarlarıyla doldurup her birinden tek bir tarife bile yetmeyecek kadar az bırakmaktan kaçın.

Ek Giriş Yolları öğe tamponlamasını genişletir, ek Çıkış Yolları ise çıktı tıkanıklığını önlemeye yardımcı olur. Hiçbiri paralel sınırını yükseltmez. Genişletirken en az 14 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yeni yapı | Yapı üç blok genişliğinde, yedi blok derinliğinde ve üç blok yüksekliğinde mi? Kontrolcü ikinci katmanın ön ortasında mı? On Boru Muhafazası ve altı metal bloğu doğru konumlandırılmış mı? |
| Yapı kademesi uyuşmazlığı | Kasalar, Boru Muhafazaları ve metal blokların tümü aynı kademede mi? Yalnızca bazı bronz bileşenler mi değiştirildi, yoksa Demir Blokları kaldı mı? |
| Eksik Buhar Kapağı veya yollar | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine öğe yolları mı kullanıldı? |
| Kapaklar eklendikten sonra yapı hata veriyor | En az 14 gerçek kasa kaldı mı? Boru Muhafazaları veya metal bloklar kapaklarla ya da yollarla değiştirildi mi? |
| Girdiler var ama tarif bulunamıyor | Öğenin bir Kompresör tarifi var mı? Bir tarif için yeterli girdi var mı? Tarif bir sıkıştırma kademesi gerektiriyor mu? Yeterli çıktı alanı var mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Boş Hücreler Oksijen Hücrelerine dönüşmüyor | Kompresör Sıkıştırılmış Hava Hücreleri üretir. oksijen ve azot diğer makinelerde daha ileri işleme gerektirir. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle paylaşıyor mu? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık öğe aktarmıyor | Buharlı yollar öğeleri otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin sekiz kopyası için yeterli girdi var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multibloklar](../multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Steam Squasher](https://wiki.gtnewhorizons.com/wiki/Steam_Squasher)