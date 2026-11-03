---
item_ids:
  - gregtech:gt.blockmachines:31083
navigation:
  title: Steam Presser
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31083
  position: 2
quest_ids:
  - s6AEHSKiQe2XveT_oDZbZg
---

# Buharlı Presleme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" />, Buhar çağında bulunan bir multiblok Dövme Çekiç'tir. Cevherleri ve malzemeleri partiler hâlinde işlemek için Buhar kullanır; Plaka ve Uzun Çubuk yapımı gibi işlerde tek bloklu Buharlı Dövme Çekiç'in yerini alır. Aynı Tarifin en fazla sekiz kopyasını aynı anda işleyebilir.

Makinenin, aynı Kontrolcüyü paylaşan temel bronz ve Yüksek Basınçlı çelik yapıları vardır. Yüksek Basınçlı yapıya yükseltmek verimi artırır, ancak maksimum Tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; Kontrolcü Tarifi Dökme Demir Plaka, bir Örs, bir Tumbaga Çerçeve ve diğer Malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, yedi blok yüksekliğinde; Kontrolcü ikinci Katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Dövme Çekiç Tarifleri, en fazla 32 EU/t gerektiren |
| Paraleller | Aynı Tarifin en fazla sekiz kopyası; Yüksek Basınçlı yapı bu sınırı artırmaz |
| İşleme bonusları | Temel yapı, tek bloklu bronz Buharlı Dövme Çekiç'in Hızının %125'inde ve paralel başına Buhar tüketim oranının %62,5'inde çalışır |
| Yükseltmeler ve hız aşırtma | Yüksek Basınçlı yapı Hızı ve Buhar tüketim oranını ikiye katlar; Gerilim hız aşırtması yok |
| Bakım ve Kirlilik | Bakım yok, Kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel Kasa ve Buhar Kapağı için güncel Tarifler aşağıda gösterilmiştir. Diğer bileşenlerin Tariflerini görmek için tablodaki öğelere tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31083" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğlalar, Bronz Boru Muhafazaları ve Demir Blokları kullanır; Yüksek Basınçlı yapı ise bunların çelik karşılıklarını kullanır. **Üç yapı bileşeni türünün tümü de aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek Basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda 39; Kapaklar veya yollar ile değiştirilebilir, ancak en az 35 gerçek Kasa kalmalı |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | İki adet, altıncı ve yedinci Katmanların ortasında |
| Metal blok | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | İki adet, dördüncü ve beşinci Katmanların ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" /> | Aynı Kontrolcü | Bir adet, ikinci Katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir Kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir Kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir Kasanın yerine |
| Sıvı Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | İsteğe bağlı, bir Kasanın yerine; mineral ekin ürünlerini işlemek için kullanılan Asitler gibi Tarif Sıvılarını sağlar |

Kasa veya Kapak için 42 konum vardır. Gerekli üç arayüzü kurmak 39 Kasa bırakır; bir Sıvı Girdi Kapağı eklemek 38 bırakır. Kapak veya yol eklerken en az 35 gerçek Kasa kalmalıdır. Kapaklar ve yollar Boru Muhafazalarının veya metal blokların yerini alamaz.

### Katman Katman İnşa

Katmanları tabandan yukarı doğru say. Önce Kontrolcünün baktığı yönü seç, ardından etkileşimli yapıyı veya hologramı Katman Katman takip et. **Tabanın önü Kontrolcünün bir blok önüne uzanır**, bu yüzden Kontrolcüyü tabanın en ön kenarına yerleştirme.

| Katman | Ne yerleştirilecek |
| --- | --- |
| Birinci | Dört köşesi çıkarılmış 5×5 taban, 21 Kasa konumu verir |
| İkinci | Kontrolcü ve hologramda gösterilen çevresindeki dokuz Kasa konumu |
| Üçüncü | Sol ve sağ sütunları başlatmak için her iki yanda birer Kasa konumu |
| Dördüncü ve beşinci | İki sütunu sürdür ve her Katmanın ortasına bir Demir Bloğu yerleştir; Yüksek Basınçlı yapı için Çelik Blokları kullan |
| Altıncı | Hologramda gösterildiği gibi altı Kasa konumu, ortada ilk Boru Muhafazası ile |
| Yedinci | Birincinin tam üstünde ikinci Boru Muhafazası |

Önizlemedeki boş konumların Kasa ile doldurulması gerekmez. Boru bağlantıları kolay olsun diye Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını alt Kasa konumlarına yerleştir. Sıradan elektrikli makine öğe yolları buharlı sürümlerin yerini alamaz.

Yapıyı önizlemek ve inşa etmeye yardımcı olması için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Master kanal kademesi 1 temel yapıyı, kademe 2 ise Yüksek Basınçlı yapıyı seçer. Yardımlı inşadan sonra Kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Buharlı Presleme, Dövme Çekiç Tarif haritasını kullanır. NEI'ye bakarken önce öğenin Dövme Çekiç Tarifi olup olmadığını doğrula, ardından Kademesini, girdi miktarını ve çıktılarını kontrol et.

| Kullanım | Yaygın Tarifler ve dikkat edilecekler |
| --- | --- |
| Metal Plaka yapımı | Birçok erken metal, iki Plaka yapmak için üç külçe kullanır; paraleller aynı anda işlenen Tarif sayısını artırır, Malzeme oranını değiştirmez |
| Uzun Çubuk yapımı | Uygun Malzemeler bir Uzun Çubuk yapmak için iki Çubuk kullanır; Malzeme ve Tarif kademesi için NEI'ye bak |
| Cevherleri öğütme | Eşleşen Tariflere sahip Cevherleri Ezilmiş Cevher veya değerli taşlara işler; çıktılar her zaman aynı tür ara öğeyi üretmek yerine Cevhere göre değişir |
| Cevher işlemeyi tamamlama | Uygun Santrifüjlenmiş Cevheri Toza işler; Öğütücü güzergâhı ek yan ürünler sağlayabilir, bu yüzden önce NEI'deki tam çıktı listelerini karşılaştır |
| Mineral ekinlerini işleme | CropsNH hasat ürünlerini LV veya altındaki Dövme Çekiç Tarifleriyle işlemek için Sıvı Girdi Kapağı kullanır ve Temizlenmiş Ezilmiş Cevher veya Saf Olmayan Toz üretir |

Makine yalnızca Dövme Çekiç adımını gerçekleştirir. Çıktıları otomatik olarak yıkamaz, Santrifüjlemez veya eritmez. Cevher işleme hattı kurarken öğeleri gerçek ürünlerine göre yönlendir; böylece daha fazla işlem gerektiren ara ürünler doğrudan fırına gitmez.

> [!NOTE]
> Makinenin kilit açma kademesi ile maksimum Tarif kademesi ayrı sınırlardır. Her zaman Buharla çalışır. Yüksek Basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademeli Dövme Çekiç Tariflerini etkinleştirmez.

### Mineral Ekin Ürünleri

Sıvı Girdi Kapağı takmak, makinenin CropsNH mineral ekin hasatlarını işlemesini sağlar. Örneğin Coppon Fiber, Tine Twig ve Ferrofern Yaprakları, Sülfürik Asit gerektiren LV Dövme Çekiç Tariflerine sahiptir ve karşılık gelen minerallerinin sürekli bir kaynağını sağlar. Diğer ekinler farklı Sıvılar veya Tarif kademeleri gerektirebilir; her Tarifi NEI'de kontrol et.

Bu yaygın Tarifler çıktıyı seçmek için Programlanmış Devre kullanır: yapılandırma 1 Temizlenmiş Ezilmiş Cevher, yapılandırma 2 ise Saf Olmayan Toz üretir. Hasat ürünlerini buharlı Giriş Yoluna gönder, Devreyi NEI'de gösterildiği gibi ayarla ve sıradan bir Sıvı Girdi Kapağı aracılığıyla yeterli Tarif Sıvısı sağla.

Buhar, makineyi çalıştırmak için yine Buhar Kapağından girer. Asitler ve diğer Tarif Sıvıları ayrı bir Sıvı Girdi Kapağından girer. İki Kapak da gereklidir; bir Girdi Kapağı Buhar Kapağının yerini alamaz. Ekin ve Tarif Sıvısı gereksinimleri paralel sayısıyla artar.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buharlı Giriş Yolunun ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar Borusunu Buhar Kapağına bağla ve Buharın gerçekten içeri girdiğini doğrula.
3. Çıkış Yolunda boş yer bırak ve en az bir Tarife yetecek kadar az miktarda Malzeme koy. Ayrıca gereken Sıvıları ve Devre yapılandırmasını sağla.
4. Makineyi başlat ve çıktı güzergâhını ve Buhar Tamponunu gözlemle.
5. Sürekli Buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve Verim

Buharlı Presleme, **aynı Tarifin** en fazla sekiz kopyasını aynı anda işleyebilir. Bu, bir döngüde sekiz farklı öğeyi işleyebileceği anlamına gelmez. Gerçek paraleller ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Örneğin, bir Plaka Tarifi iki Plaka yapmak için üç külçe kullanıyorsa, sekiz paralel 24 külçe gerektirir ve bir döngüde 16 Plaka üretir. Yalnızca sekiz külçe koymak sekiz paralel için yeterli değildir.

Temel yapı, tek bloklu bronz Buharlı Dövme Çekiç'in Hızının %125'inde çalışır ve yaklaşık %80'i kadar sürer. Paralel başına Buhar tüketim oranı, tek bloklu makinenin oranının %62,5'idir. İki bonus birleştiğinde aynı miktarda Malzeme için toplam Buhar tüketiminin yaklaşık %50'si elde edilir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık Buhar talebini artırır.

| Özellik | Temel yapı | Yüksek Basınçlı yapı |
| --- | --- | --- |
| Kabul edilen Tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| Temel yapıya göre Hız | 1× | 2× |
| Aynı Tarif ve paralel sayısı için Buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam Buhar tüketimi | Referans | Yaklaşık olarak temel yapıyla aynı |

Yüksek Basınçlı yükseltmesi Hızı ve Buhar tüketim oranını birlikte artırır. Esas olarak verimi iyileştirir, öğe başına toplam Buhar maliyetini bir kez daha yarıya indirmez. Gerçek süre ve Buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L Buharı Tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli Kazan üretiminin yerini alamaz. Kazanları ve Boruları **işleme sırasındaki Buhar tüketim oranına** göre boyutlandır.

Çalışma sırasındaki Buhar tüketim oranını kontrol etmek için Waila kullan ve sürekli işleme sırasında Tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından Kazan üretimini artır veya Boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında Buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen materyaller geri verilmez. Yüksek Basınca yükseltmeden veya paralel sınırını artırmadan önce Buhar üretimini ve Boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={2} />
</GameScene>

Yüksek Basınçlı yapı aynı boyutları, Kapak konumlarını ve Kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Bloklarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Boru Muhafazaları ve Çelik Bloklarıyla değiştir. Yalnızca Kasaları değiştirmek veya tek bir Demir Bloğu bile bırakmak kademe kontrolünde başarısız olur.

Yükseltmeden önce işlemeyi ve Malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve Buharı ve üretimi geri açmadan önce makinenin Yüksek Basınçlı kademeyi gösterdiğini doğrula.

Yüksek Basınç bir yapı kademesidir, ayrı bir Buhar Sıvısı değildir. Makine yine sıradan Buhar kullanır ve mevcut Buhar Kapağı ve buharlı yollar yeniden kullanılabilir. Enerji Kapağı gerekmez. Yükseltme Hızı ve Buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve Tarif kademesi sınırı LV olarak kalır.

## Otomasyon ve Öğe Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her birinde dört öğe yuvası vardır. Yanlarındaki Sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir yolun yanına Sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Öğeleri Giriş Yolunun ön yüzüne göndermek için Hunileri, GT öğe Borularını, konveyörleri veya öğe kanallarını kullan.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden etkin şekilde çek ve ürünleri depoya veya sonraki makineye yönlendir.
- **Buhar:** Kazandan Buhar Kapağına Sıvı Boruları bağla. Öğe yolları Buhar alamaz.
- **Tarif Sıvıları:** Mineral ekinlerini veya Sıvı girdili diğer Tarifleri işlerken, NEI'nin gerektirdiği Asitleri veya diğer Sıvıları sağlamak için sıradan bir Girdi Kapağına ayrı bir Sıvı Borusu bağla.
- **Yönlendirme:** Plaka üretimi, Uzun Çubuk üretimi ve Cevher işleme için gerektiği gibi girdi filtreleri ayarla; böylece farklı Malzemeler dört girdi yuvasının tümünü doldurmaz. Mineral ürünleri gerçek öğe türlerine göre sonraki makinelere yönlendir.

Ek Giriş Yolları öğe Tamponlamasını genişletir, ek Çıkış Yolları ise çıktı tıkanıklığını önlemeye yardımcı olur. Hiçbiri sekiz paralel sınırını yükseltmez. Sıvı Girdi Kapakları veya yollar eklerken en az 35 gerçek Kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Ne kontrol etmeli |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik yedi blok mu? Kontrolcü ikinci Katmanda, tabanın en ön kenarının bir blok gerisinde mi? İki üst Boru Muhafazası ve iki merkez metal blok doğru konumda mı? |
| Yapı kademesi uyuşmuyor | Kasalar, Boru Muhafazaları ve metal blokların tümü aynı kademede mi? Yükseltmeden sonra kalan Demir Bloğu veya bronz bileşen var mı? |
| Buhar Kapağı veya yollar eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine öğe yolları mı kullanıldı? |
| Yol ekledikten sonra yapı bozuluyor | En az 35 gerçek Kasa kaldı mı? Boru Muhafazaları veya metal bloklar yollarla değiştirildi mi? |
| Girdiler var ama Tarif bulunamıyor | Öğenin Dövme Çekiç Tarifi var mı? Bir Tarif için yeterli girdi var mı? Gerekli Sıvılar ve Devre yapılandırması sağlandı mı? Yeterli çıktı alanı var mı? |
| Mineral ekin ürünleri işlenmiyor | Sıradan bir Sıvı Girdi Kapağı takılı ve gerekli Asit veya başka bir Sıvı sağlanmış mı? Devre yapılandırması doğru mu? Tarif LV veya altında mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen Tarif LV'yi aşıyor mu? Yüksek Basınçlı yapı da MV veya daha yüksek kademeli Tarifleri işleyemez. |
| Kapakta Buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya Buharı diğer makinelerle paylaşıyor mu? Mevcut paralel sayısı ve Yüksek Basınçlı kademe Kazan kapasitesini aşıyor mu? |
| Yolun yanındaki Sandık öğe aktarmıyor | Buharlı yollar öğeleri otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az Tarif işleniyor | Aynı Tarifin kopyaları için yeterli Malzeme var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multibloklar](../multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Buharlı Presleme](https://wiki.gtnewhorizons.com/wiki/Steam_Presser)