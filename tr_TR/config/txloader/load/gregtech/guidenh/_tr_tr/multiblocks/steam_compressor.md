---
item_ids:
  - gregtech:gt.blockmachines:31078
navigation:
  title: Steam Squasher
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31078
  position: 4
quest_ids:
  - Plg8vg0gS9Ks2Ddc5sIVOg
---

# Steam Squasher

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" />, Buhar çağında kullanılabilen bir Multiblok Kompresör'dür. Materyalleri partiler hâlinde sıkıştırmak için buhar kullanır. Tek bloklu Buharlı Kompresör'ün yükseltmesi olarak aynı Tarifin sekize kadar kopyasını aynı anda işleyebilir; materyal blokları, Sıkıştırılmış Ateş Kili ve Sıkıştırılmış Hava Hücreleri üretir.

Makinenin, aynı Kontrolcüyü paylaşan temel bronz ve Yüksek Basınçlı çelik yapıları vardır. Yüksek Basınçlı yapıya yükseltmek iş verimini artırır, ancak maksimum Tarif Kademesini yükseltmez veya makineleri özel sıkıştırma kademeleriyle değiştirmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılım kademesi | Buhar; Kontrolcü Tarifi Pistonlar, Tumbaga Dişlileri, bir Tumbaga Çerçeve ve diğer materyalleri gerektirir |
| Boyutlar | Üç blok genişlik, yedi blok derinlik ve üç blok yükseklik; Kontrolcü ikinci Katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV ve altındaki sıradan Kompresör Tarifleri, en fazla 32 EU/t gerektirir |
| Özel sınır | Özel bir sıkıştırma kademesi gerektiren Tarifleri işleyemez; Yüksek Basınçlı çelik yapı bunların kilidini açmaz |
| Paraleller | Aynı Tarifin en fazla sekiz kopyası; Yüksek Basınçlı yapı bu sınırı artırmaz |
| İşleme bonusları | Temel yapı, tek bloklu bronz Buharlı Kompresör'ün Hızının %125'inde ve paralel başına buhar tüketim oranının %62,5'inde çalışır |
| Yükseltmeler ve hız aşırtma | Yüksek Basınçlı yapı Hızı ve buhar tüketim oranını ikiye katlar; Gerilim hız aşırtması yok |
| Bakım ve Kirlilik | Bakım yok, Kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel Kasa ve Buhar Kapağı için mevcut Tarifler aşağıda gösterilmiştir. Diğer bileşenlerin Tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31078" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Bloklarını kullanırken Yüksek Basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki Kasalar, Boru Muhafazaları ve metal blokların tümü aynı Kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek Basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda 27; aşağıdaki Kapaklar veya yollar ile değiştirilebilir, ancak en az 14 gerçek Kasa kalmalıdır |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | On: sekizi öndeki Kontrolcünün etrafında, ikisi de yapının içindeki ikinci Katmanın ortası boyunca |
| Metal blok | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | Altı: önden sayıldığında beşinci sırada, ikinci ve üçüncü Katmanların her birinde üç |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31078" showIcon="left" /> | Aynı Kontrolcü | Bir, ikinci Katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı Kapak | Tam olarak bir, bir Kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı Yol | En az bir, bir Kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı Yol | En az bir, bir Kasanın yerine |
| Sıvı Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı Kapak | İsteğe bağlı, bir Kasanın yerine; Tarif Sıvılarını sağlar |

Yeni yapıda Kasalar veya Kapaklar için 30 konum vardır. Gerekli üç arayüz takıldığında 27 Kasa Yaprakları kalır; bir Sıvı Girdi Kapağı eklendiğinde 26 Kasa Yaprakları kalır. Daha fazla Kapak veya Yol eklerken en az 14 gerçek Kasa kalmalıdır. Kapaklar ve yollar Boru Muhafazalarının veya metal blokların yerini alamaz.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal Kademe 1 temel yapıyı, Kademe 2 ise Yüksek Basınçlı yapıyı seçer. Yardımlı inşadan sonra Kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Steam Squasher, Kompresör Tarif haritasını kullanır. NEI'yi kontrol ederken önce eşyanın bir Kompresör Tarifi olup olmadığını doğrula, sonra Kademesini, girdi miktarını, çıktılarını ve özel gereksinimlerini kontrol et.

| Kullanım | Yaygın Tarifler ve dikkat edilecekler |
| --- | --- |
| Materyal blokları yapmak | Uygun metaller genellikle bir metal bloğu yapmak için dokuz külçe kullanır; bazı Tozların da blok sıkıştırma Tarifleri vardır. Materyali ve Tarif Kademesini NEI'de kontrol et. |
| İnşa blokları yapmak | Kil Toplarını, Tuğlaları, Nether Tuğlalarını, Parlak taş Tozunu ve diğer malzemeleri karşılık gelen bloklarına sıkıştırır; örneğin dört Tuğla eşyası bir Tuğla bloğu yapar |
| Sıkıştırılmış Ateş Kili yapmak | Ateş Kili Tozunu daha sonra pişirilmek üzere Sıkıştırılmış Ateş Kiline sıkıştırır; Kompresör pişirme adımını kendisi gerçekleştirmez |
| Sıkıştırılmış Hava Hücreleri üretmek | Boş Hücreleri daha sonraki hava işlemesi için Sıkıştırılmış Hava Hücrelerine sıkıştırır |
| Diğer sıradan sıkıştırma Tarifleri | Alaşım Plakalarını ve uygun Tariflere sahip diğer malzemeleri işler; uyumluluğu doğrulamak için NEI'deki Kompresör Tarifini kontrol et |

### Hava Hücreleri ve Sonraki Oksijen Üretimi

Sıradan bir sıkıştırma Tarifi **bir Boş Hücreyi bir Sıkıştırılmış Hava Hücresine** dönüştürür. Boş Hücreler buharlı Giriş Yolundan girer ve Sıkıştırılmış Hava Hücreleri buharlı Çıkış Yolundan çıkar. Bu Tarif güç için yalnızca buhar gerektirir; ek bir Su beslemesi, Girdi Kapağı aracılığıyla sağlanan Hava veya özel bir hava toplama cihazı gerekmez.

Sıkıştırılmış Hava Hücreleri sonraki oksijen ve Azot üretiminde kullanılabilir, ancak bu makine yalnızca Sıkıştırılmış Hava Hücreleri üretir. **Doğrudan Oksijen veya Azot çıktısı vermez.** Daha ileri işlemeden önce NEI'de Sıkıştırılmış Hava Hücrelerinin ve Hava Sıvısının kullanımlarını kontrol et, sonra sonraki makinenin Tarifinin gerektirdiği Sıvıları, hücreleri ve çıktı arayüzlerini sağla.

Otomasyon için Boş Hücreleri Kompresöre ve Sıkıştırılmış Hava Hücrelerini sonraki makineye gönder. İşlemden dönen Boş Hücreler girdiye geri yönlendirilebilir. Hücre dolaşımı için yeterli Tampon bırak ki tüm Boş Hücreler diğer makinelerde sıkışıp kalmasın.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar olan Tarifleri kabul eder. Yüksek Basınçlı çelik yapı makinenin yapı Kademesini yükseltir. MV veya daha yüksek Kademeli Tarifleri ya da özel bir sıkıştırma kademesi gerektiren Tarifleri etkinleştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buharlı Giriş Yolunun ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de Tarifi ve girdi miktarını kontrol et ve Çıkış Yolunda boş yer bırak.
4. Makineyi az miktarda malzemeyle başlat ve çıktı yolunu ve buhar Tamponunu gözlemle.
5. Sürekli bir buhar beslemesi olduğunu doğruladıktan sonra girdi miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve İş Verimi

Steam Squasher aynı anda **aynı Tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Örneğin, bir blok sıkıştırma Tarifi bir metal bloğu yapmak için dokuz külçe kullanıyorsa sekiz paralel 72 külçe gerektirir ve bir döngüde sekiz metal bloğu üretir.

Temel yapı, tek bloklu bronz Buharlı Kompresör'ün Hızının %125'inde çalışır ve yaklaşık %80'i kadar sürer. Paralel başına buhar tüketim oranı, tek bloklu makinenin oranının %62,5'idir. İki bonusu birleştirmek, aynı miktarda malzeme için toplam buhar tüketiminin yaklaşık %50'sini verir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar talebini artırır.

| Özellik | Temel yapı | Yüksek Basınçlı yapı |
| --- | --- | --- |
| Kabul edilen Tarif kademeleri | LV ve altındaki sıradan Kompresör Tarifleri | LV ve altındaki sıradan Kompresör Tarifleri |
| Maksimum paralel | 8 | 8 |
| Temel yapıya göre Hız | 1× | 2× |
| Aynı Tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Başlangıç değeri | Temel yapıyla yaklaşık aynı |

Yüksek Basınçlı yükseltme Hızı ve buhar tüketim oranını birlikte artırır. Esas olarak iş verimini artırır, eşya başına toplam buhar maliyetini tekrar yarıya indirmez. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli Kazan üretiminin yerini alamaz. Kazanları ve Boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila kullan ve sürekli işleme sırasında Tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru iş verimini karşılaştırırken uyumlu birimler kullan. Buhar beslemesi yetersizse GUI'de paralel sınırını düşür, sonra Kazan üretimini artır veya Boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın bitmesi mevcut işlemi iptal eder ve zaten tüketilen malzemeler geri verilmez. Yüksek Basınçlı yapıya yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve Boru iş verimini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31078" tier={2} />
</GameScene>

Yüksek Basınçlı yapı aynı boyutları, Kapak konumlarını ve Kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Bloklarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Boru Muhafazaları ve Çelik Blokları ile değiştir.

Yükseltmeden önce işlemeyi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin Yüksek Basınçlı kademeyi gösterdiğini doğrula.

Yüksek Basınç, makinenin yapı Kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı yollar yeniden kullanılabilir. Yükseltme Hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik Sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir Yolun yanına Sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Eşyaları Giriş Yolunun ön yüzüne göndermek için Huniler, GT eşya Boruları, konveyörler veya eşya kanalları kullan.
- **Çıktı:** Borular, kanallar veya konveyörler ile Çıkış Yolunun ön yüzünden aktif olarak çek, sonra ürünleri Depolamaya veya sonraki makineye yönlendir.
- **Buhar:** Kazandan Buhar Kapağına Sıvı Boruları bağla. Sıradan bir Girdi Kapağı, güç için Buhar Kapağının yerini alamaz.
- **Tarif Sıvıları:** NEI Tarifi bir Sıvı girdisi gerektirdiğinde yalnızca ek bir sıradan Girdi Kapağı tak ve karşılık gelen Sıvıyı sağla. Sıkıştırılmış Hava Hücresi üretmek bu arayüzü gerektirmez.
- **Yönlendirme:** Materyal blokları, Sıkıştırılmış Ateş Kili, Sıkıştırılmış Hava Hücreleri ve diğer ürünler için filtreler ayarla ki hava hücreleri materyal Depolamasına girmesin ve pişirilmesi gereken ara ürünler çıktıda kalmasın.

Blok sıkıştırma Tarifleri genellikle aynı anda birkaç eşya tüketir. Girdi Tamponunu "Tarif başına girdi × hedef paralel" için boyutlandır. Girdi yuvalarını çok sayıda farklı malzemenin küçük miktarlarıyla doldurmaktan kaçın; aksi hâlde her birinden bir Tarif için bile çok az kalır.

Ek Giriş Yolları eşya tamponlamasını genişletirken ek Çıkış Yolları çıktı tıkanıklığını önlemeye yardımcı olur. İkisi de paralel sınırını artırmaz. Genişletirken en az 14 gerçek Kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Yeni yapı tamamlanmamış | Yapı üç blok genişlik, yedi blok derinlik ve üç blok yükseklikte mi? Kontrolcü ikinci Katmanın ön ortasında mı? On Boru Muhafazası ve altı metal blok doğru konumda mı? |
| Yapı kademesi uyuşmuyor | Kasalar, Boru Muhafazaları ve metal blokların tümü aynı Kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi veya Demir Bloklardan kalan var mı? |
| Buhar Kapağı veya yollar eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapaklar eklendikten sonra yapı geçersiz | En az 14 gerçek Kasa kaldı mı? Boru Muhafazalarının veya metal blokların yerine Kapak ya da Yol mu konuldu? |
| Girdiler var ama Tarif bulunamıyor | Eşyanın bir Kompresör Tarifi var mı? Bir Tarif için yeterli girdi var mı? Tarif bir sıkıştırma kademesi gerektiriyor mu? Yeterli çıktı alanı var mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen Tarif LV'yi aşıyor mu? Yüksek Basınçlı yapı da MV veya daha yüksek Kademeli Tarifleri işleyemez. |
| Boş Hücreler Oksijen Hücrelerine dönüşmüyor | Kompresör Sıkıştırılmış Hava Hücreleri üretir. Oksijen ve Azot, diğer makinelerde daha ileri işleme gerektirir. |
| Kapağın içinde buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve Yüksek Basınçlı kademe Kazan kapasitesini aşıyor mu? |
| Yolun yanındaki Sandık eşya aktarmıyor | Buharlı yollar eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az Tarif işlendi | Aynı Tarifin sekiz kopyası için yeterli girdi var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multibloklar](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [Multibloklar](./multiblocks_index.md)
- [GTNH Çince Wiki: Steam Squasher](https://gtnh.huijiwiki.com/wiki/大型蒸汽压缩机)