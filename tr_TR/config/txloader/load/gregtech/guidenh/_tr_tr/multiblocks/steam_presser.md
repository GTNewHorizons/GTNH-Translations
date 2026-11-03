---
item_ids:
  - gregtech:gt.blockmachines:31083
quest_ids:
  - s6AEHSKiQe2XveT_oDZbZg
navigation:
  title: Buharlı Pres
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31083
  position: -501
---
# Buharlı Pres
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok Dövme Çekicidir. Cevherleri ve malzemeleri partiler halinde işlemek için buhar kullanır; plaka ve Uzun Çubuk yapmak gibi işlerde tek bloklu Buharlı Dövme Çekicinin yerini alır. Aynı tarifin en fazla sekiz kopyasını aynı anda işleyebilir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınçlı yapıya yükseltmek üretim hızını artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı kademe | Buhar; kontrolcü tarifi Dökme Demir Plaka, Örs, Tumbaga Çerçeve Kutusu ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, yedi blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV ve altı Dövme Çekici tarifleri; en fazla 32 EU/t gerektirir |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşleme bonusları | Temel yapı, tek bloklu bronz Buharlı Dövme Çekici hızının %125'inde ve paralel başına buhar tüketim hızının %62,5'inde çalışır |
| Yükseltmeler ve overclock | Yüksek basınçlı yapı hızı ve buhar tüketim hızını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31083" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğla, Bronz Boru Muhafazası ve Demir Blok kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Üç yapı bileşeni türünün tamamı aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel düzende 39; kapak veya veriyoluyla değiştirilebilir, ancak en az 35 gerçek kasa kalmalı |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | İki adet, altıncı ve yedinci katmanların ortasında |
| Metal blok | <ItemLink id="minecraft:iron_block" showIcon="left" /> | <ItemLink id="gregtech:gt.blockmetal6:13" showIcon="left" /> | İki adet, dördüncü ve beşinci katmanların ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31083" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Sıvı Girdi Kapağı | Örneğin <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | İsteğe bağlı, bir kasanın yerine; mineral ekin ürünlerini işlemek için kullanılan asitler gibi tarif sıvılarını sağlar |

Kasa veya kapak için 42 konum vardır. Gerekli üç arayüzü kurmak 39 kasa bırakır; bir Sıvı Girdi Kapağı eklemek 38 bırakır. Kapak veya veriyolu eklerken en az 35 gerçek kasa kalmalıdır. Kapaklar ve veriyolları Boru Muhafazalarının veya metal blokların yerini alamaz.

### Katman Katman İnşa

Katmanları tabandan yukarı doğru say. Önce kontrolcünün yönünü seç, ardından etkileşimli yapıyı veya hologramı katman katman takip et. **Tabanın ön tarafı kontrolcünün bir blok önüne uzanır**, bu yüzden kontrolcüyü tabanın en ön kenarına yerleştirme.

| Katman | Ne yerleştirilecek |
| --- | --- |
| Birinci | Dört köşesi çıkarılmış 5×5 taban; 21 kasa konumu verir |
| İkinci | Kontrolcü ve hologramda gösterilen çevresindeki dokuz kasa konumu |
| Üçüncü | Sol ve sağ sütunları başlatmak için her iki yanda birer kasa konumu |
| Dördüncü ve beşinci | Her iki sütunu sürdür ve her katmanın ortasına bir Demir Blok yerleştir; yüksek basınçlı yapı için Çelik Blok kullan |
| Altıncı | Hologramda gösterildiği gibi altı kasa konumu; ilk Boru Muhafazası ortada |
| Yedinci | İkinci Boru Muhafazası birincinin tam üstünde |

Önizlemedeki boş konumların kasalarla doldurulması gerekmez. Kolay boru bağlantıları için Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını alt kasa konumlarına yerleştir. Sıradan elektrikli makine eşya veriyolları buharlı sürümlerin yerini alamaz.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makinenin Kullanım Alanları

Buharlı Pres, Dövme Çekici tarif haritasını kullanır. NEI'ye bakarken önce eşyanın Dövme Çekici tarifi olup olmadığını doğrula, ardından kademesini, girdi miktarını ve çıktılarını kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Metal plaka üretimi | Birçok erken dönem metal, iki plaka yapmak için üç külçe kullanır; paraleller malzeme oranını değiştirmeden aynı anda işlenen tarif sayısını artırır |
| Uzun Çubuk üretimi | Uygun malzemeler bir Uzun Çubuk yapmak için iki Çubuk kullanır; malzeme ve tarif kademesi için NEI'ye bak |
| Cevher kırma | Eşleşen tariflere sahip cevherleri Ezilmiş Cevher veya değerli taşlara işler; çıktılar her zaman aynı tür ara eşyayı üretmek yerine cevhere göre değişir |
| Cevher işlemeyi tamamlama | Uygun Santrifüjlenmiş Cevheri toza işler; Öğütücü yolu ek yan ürünler sağlayabilir, bu yüzden önce NEI'deki tam çıktı listelerini karşılaştır |
| Mineral ekinlerini işleme | LV ve altı Dövme Çekici tarifleriyle CropsNH hasat ürünlerini işlemek için Sıvı Girdi Kapağı kullanır; Temizlenmiş Ezilmiş Cevher veya Saf Olmayan Toz üretir |

Makine yalnızca Dövme Çekici adımını gerçekleştirir. Çıktıları otomatik olarak yıkamaz, santrifüjlemez veya eritmez. Cevher işleme hattı kurarken eşyaları gerçek ürünlerine göre yönlendir; böylece daha fazla işlem gerektiren ara ürünler doğrudan fırına gönderilmez.

> [!NOTE]
> Makinenin açıldığı kademe ile maksimum tarif kademesi ayrı sınırlardır. Her zaman buharla çalışır. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademeli Dövme Çekici tariflerini açmaz.

### Mineral Ekin Ürünleri

Sıvı Girdi Kapağı takmak, makinenin CropsNH mineral ekin hasatlarını işlemesini sağlar. Örneğin Coppon Fiber, Tine Twig ve Ferrofern Leaf, Sülfürik Asit gerektiren LV Dövme Çekici tariflerine sahiptir ve ilgili minerallerinin sürekli bir kaynağını sağlar. Diğer ekinler farklı sıvılar veya tarif kademeleri gerektirebilir; her tarifi NEI'de kontrol et.

Bu yaygın tarifler çıktıyı seçmek için Programlanmış Devre kullanır: yapılandırma 1 Temizlenmiş Ezilmiş Cevher, yapılandırma 2 ise Saf Olmayan Toz üretir. Hasat ürünlerini buharlı Giriş Yoluna gönder, devreyi NEI'de gösterildiği gibi ayarla ve sıradan bir Sıvı Girdi Kapağından yeterli tarif sıvısı sağla.

Buhar, makineyi çalıştırmak için yine Buhar Kapağından girer. Asitler ve diğer tarif sıvıları ayrı bir Sıvı Girdi Kapağından girer. İki kapak da gereklidir; bir Girdi Kapağı Buhar Kapağının yerini alamaz. Ekin ve tarif sıvısı gereksinimleri paralel sayısıyla artar.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, buharlı Giriş Yolu ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. Çıkış Yolunda boş yer bırak ve en az bir tarife yetecek kadar az miktarda malzeme koy. Gerekli sıvıları ve devre yapılandırmasını da sağla.
4. Makineyi çalıştır ve çıktı yolunu ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve Üretim Hızı

Buharlı Pres, aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, tek bir döngüde sekiz farklı eşyayı işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Örneğin bir plaka tarifi iki plaka yapmak için üç külçe kullanıyorsa, sekiz paralel 24 külçe gerektirir ve tek döngüde 16 plaka üretir. Yalnızca sekiz külçe koymak sekiz paralel için yeterli değildir.

Temel yapı, tek bloklu bronz Buharlı Dövme Çekicinin hızının %125'inde çalışır ve yaklaşık %80'i kadar süre alır. Paralel başına buhar tüketim hızı, tek bloklu makinenin hızının %62,5'idir. İki bonus birleştiğinde aynı miktar malzeme için toplam buhar tüketiminin yaklaşık %50'si elde edilir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar talebini artırır.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| Temel yapıya göre hız | 1× | 2× |
| Aynı tarif ve paralel sayısı için buhar tüketim hızı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Referans | Temel yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim hızını birlikte artırır. Esas olarak üretim hızını iyileştirir; eşya başına toplam buhar maliyetini tekrar yarıya indirmez. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim hızına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim hızını kontrol etmek için Waila kullan ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t cinsinden gösteriliyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru hattını iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31083" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Boru Muhafazalarını ve Demir Blokları tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Boru Muhafazaları ve Çelik Bloklarla değiştir. Yalnızca kasaları değiştirmek veya tek bir Demir Blok bırakmak bile kademe kontrolünden geçmez.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buhar ile üretimi geri açmadan önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç ayrı bir buhar sıvısı değil, bir yapı kademesidir. Makine yine sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı veriyolları yeniden kullanılabilir. Enerji Kapağı gerekmez. Yükseltme hızı ve buhar tüketim hızını ikiye katlar, ancak maksimum sekiz paralel kalır ve tarif kademesi sınırı LV olarak devam eder.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; otomasyon için bir veriyolunun yanına sandık koymak yeterli değildir.

- **Giriş:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan.
- **Çıkış:** Aktif olarak Çıkış Yolunun ön yüzünden borular, kanallar veya konveyörlerle çek, ardından ürünleri depolamaya veya bir sonraki makineye yönlendir.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Eşya veriyolları buhar alamaz.
- **Tarif sıvıları:** Mineral ekinleri veya sıvı girdili diğer tarifleri işlerken, NEI'nin gerektirdiği asitleri veya diğer sıvıları sağlamak için ayrı bir sıvı borusunu sıradan bir Girdi Kapağına bağla.
- **Yönlendirme:** Gerektiğinde plaka üretimi, Uzun Çubuk üretimi ve cevher işleme için girdi filtreleri ayarla; böylece farklı malzemeler dört girdi yuvasının hepsini doldurmaz. Mineral ürünlerini gerçek eşya türlerine göre sonraki makinelere yönlendir.

Ek Giriş Yolları eşya tamponlamasını genişletir, ek Çıkış Yolları ise çıktı tıkanıklığını önlemeye yardımcı olur. Hiçbiri sekiz paralel sınırını yükseltmez. Sıvı Girdi Kapağı veya veriyolu eklerken en az 35 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Yapı tamamlanmamış | Taban alanı 5×5 ve yükseklik yedi blok mu? Kontrolcü ikinci katmanda, tabanın en ön kenarının bir blok gerisinde mi? Üstteki iki Boru Muhafazası ve ortadaki iki metal blok doğru konumda mı? |
| Yapı kademesi uyuşmuyor | Kasalar, Boru Muhafazaları ve metal blokların hepsi aynı kademede mi? Yükseltmeden sonra kalan Demir Blok veya bronz bileşen var mı? |
| Buhar Kapağı veya veriyolları eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ile Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya veriyolları mı kullanıldı? |
| Veriyolu ekledikten sonra yapı geçersiz | En az 35 gerçek kasa kaldı mı? Boru Muhafazaları veya metal bloklardan herhangi biri veriyoluyla değiştirildi mi? |
| Girdiler var ama tarif bulunamıyor | Eşyanın Dövme Çekici tarifi var mı? Bir tarif için yeterli girdi var mı? Gerekli sıvılar ve devre yapılandırması sağlandı mı? Yeterli çıktı alanı var mı? |
| Mineral ekin ürünleri işlenmiyor | Sıradan bir Sıvı Girdi Kapağı takılı ve gerekli asit veya başka bir sıvı sağlanıyor mu? Devre yapılandırması doğru mu? Tarif LV veya altında mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya diğer makinelerle buhar paylaşıyor mu? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buharlı veriyolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin kopyaları için yeterli malzeme var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## Kaynaklar

- [GTNH Wiki: Buharlı Pres](https://wiki.gtnewhorizons.com/wiki/Steam_Presser)