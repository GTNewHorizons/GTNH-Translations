---
item_ids:
  - gregtech:gt.blockmachines:31041
navigation:
  title: Buharlı Öğütücü
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31041
  position: 3
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKzA
---

# Buharlı Öğütücü

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok Öğütücüdür. Cevherleri ve materyalleri partiler halinde öğütmek için buhar kullanır. Tek bloklu Buharlı Öğütücünün yükseltmesi olarak aynı tariften aynı anda en fazla sekiz kopya işleyebilir ve erken cevher işleme hatlarında işe yarar.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınç yapısına yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez veya ek cevher yan ürünleri sağlamaz.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | Buhar; kontrolcü tarifi Elmas, Piston, Tumbaga Çerçeve Kutusu ve diğer materyalleri gerektirir |
| Boyutlar | 3×3 ayak izi, dört blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki, en fazla 32 EU/t gerektiren Öğütücü tarifleri |
| Çıkış sınırı | Tarifin çıkış listesindeki yalnızca ilk eşya; yüksek basınç yapısı çıkış türü eklemez |
| Paraleller | Aynı tariften en fazla sekiz kopya; daha düşük tarif gücü bu sınırı artırmaz |
| İşleme bonusları | Temel yapı, tek bloklu bronz Buharlı Öğütücünün hızının %125'inde ve paralel başına buhar tüketim oranının %62,5'inde çalışır |
| Yükseltmeler ve overclock | Yüksek basınç yapısı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağının güncel tarifleri aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31041" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı bronz bileşenleri kullanırken yüksek basınç yapısı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Çerçeve Kutuları ve Dişli Kutusu Kasalarının tamamı aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınç yapısı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel düzende 17; aşağıdaki kapaklar veya veriyollarıyla değiştirilebilir, ancak en az 14 gerçek kasa kalmalıdır |
| Çerçeve Kutusu | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Sekiz adet, ikinci ve üçüncü katmanların dört köşesinde |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Bir adet, dördüncü katmanın ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |

Yeni yapıda kasalar veya kapaklar için 20 konum vardır. Gerekli üç arayüzün takılması 17 kasa bırakır; veriyolu eklemek kasa sayısını buna göre azaltır. Kapaklar ve veriyolları Çerçeve Kutularının veya Dişli Kutusu Kasalarının yerine geçemez.

### Katman Katman İnşa

Katmanları tabandan yukarı doğru say. Önce kontrolcünün baktığı yönü seç, ardından etkileşimli yapıyı veya hologramı katman katman takip et.

| Katman | Ne yerleştirilir |
| --- | --- |
| Birinci | Tam 3×3 taban, dokuz kasa konumu sağlar |
| İkinci | Dört köşenin tamamında Çerçeve Kutuları, ön ortada kontrolcü ve sol, sağ ve arka kenarların ortasında birer kasa konumu |
| Üçüncü | Dört köşenin tamamında Çerçeve Kutuları ve dört kenarın her birinin ortasında bir kasa konumu |
| Dördüncü | Ortada bir Dişli Kutusu Kasası ve dört kenarın her birinin ortasında bir kasa konumu; dört köşede blok gerekmez |

İkinci ve üçüncü katmanlardaki boş merkez konumlarının kasalarla doldurulması gerekmez. Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını, boru bağlantıları kolay olsun diye uygun kasa konumlarına yerleştir. Sıradan elektrikli makine eşya veriyolları buharlı sürümlerin yerine geçemez.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınç yapısını seçer. Destekli inşadan sonra kapakları tak ve yapıyı kontrol et.

> [!NOTE]
> Bu sayfa 2.9.0'daki yeni yapıyı açıklar. Mevcut RC-2 eski içi boş 3×3×3 yapıyı da kabul eder, ancak hologram ve destekli inşa yeni yapıyı kullanır. Eski sayfanın tarif gücüne dayalı paralel açıklaması mevcut sürüm için geçerli değildir; makinenin maksimumu sekiz paralel olarak sabittir.

## Makine Kullanımı ve Çıktılar

Buharlı Öğütücü, Öğütücü tarif haritasını kullanır. NEI'ye bakarken önce eşyanın bir Öğütücü tarifi olup olmadığını doğrula, ardından kademesini, girdi miktarını ve **ilk eşya çıktısını** kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Başlangıç cevher kırma | Uygun cevherleri Ezilmiş Cevhere dönüştürür; bu adım birçok yaygın cevher için ana çıktı miktarını artırır, kesin verimler NEI'de gösterilir |
| Cevher ara ürünlerini öğütme | Uygun Ezilmiş Cevheri Saf Olmayan Toza ve Santrifüjlenmiş Cevheri toza dönüştürür; makine sonraki yıkama, santrifüjleme veya eritme adımlarını otomatik yapmaz |
| Materyal öğütme | Eşleşen tariflere sahip külçeleri, mücevherleri ve diğer materyalleri alaşımlar ve ileri işleme için toza dönüştürür |
| Eşya geri dönüşümü | Öğütücü geri dönüşüm tarifleri olan bileşenleri veya eşyaları işler; hâlâ ihtiyaç duyduğun eşyaları vermeden önce çıktıları kontrol et |

### Neden Yan Ürün Yok?

Makine, Öğütücü tarifinin çıktı listesindeki yalnızca **ilk eşya çıktısını** üretir. NEI'de ikinci ve sonraki konumlardaki eşyalar, çıktı şansları olsa bile üretilmez. Bu, Çıkış Yolundaki yuva eksikliği değil, makinenin bir sınırlamasıdır.

Örneğin bir tarif ana mineral, bir cevher yan ürünü ve Taş Tozu olmak üzere üç çıktı listeliyorsa Buharlı Öğütücü yalnızca ilk çıktının miktarını ve şansını kullanır. Çıkış Yolu eklemek, paralelleri artırmak veya yüksek basınç yapısına yükseltmek kalan çıktıların kilidini açmaz.

Öğütme adımından cevher yan ürünleri istiyorsan <ItemLink id="gregtech:gt.blockmachines:303" showIcon="left" /> gibi daha fazla çıktısı olan makineleri düşün. Cevher yıkama ve santrifüjlemenin de kendi çıktıları vardır; her adımı makinesine ve NEI tarifine göre planla.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademe tarifleri etkinleştirmez ve ilk eşya çıktısı sınırını değiştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buharlı Giriş Yolunun ve buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de tarif kademesini ve ilk eşya çıktısını kontrol et ve Çıkış Yolunda boş yer bırak.
4. Makineyi az miktarda materyalle çalıştır ve çıktı yolunu ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralelleri artır.

## Buhar Beslemesi ve Verim

Buharlı Öğütücü aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, tek döngüde sekiz farklı eşya işleyebileceği anlamına gelmez. Gerçek paraleller ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır. Daha düşük güçlü tarifler maksimumu sekizin üzerine çıkarmaz.

Temel yapı, tek bloklu bronz Buharlı Öğütücünün hızının %125'inde çalışır ve işlem süresi yaklaşık %80'e iner. Paralel başına buhar tüketim oranı, tek bloklu makinenin oranının %62,5'idir. İki bonus birleştiğinde aynı miktarda materyal için toplam buhar tüketiminin yaklaşık %50'si elde edilir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar talebini artırır.

| Özellik | Temel yapı | Yüksek basınç yapısı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| Eşya çıktı türleri | Yalnızca tarifin ilk eşya çıktısı | Yalnızca tarifin ilk eşya çıktısı |
| Temel yapıya göre hız | 1× | 2× |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi iyileştirir, eşya başına toplam buhar maliyetini tekrar yarıya indirmez. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini tutamaz. Kazanları ve boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila kullan ve sürekli işleme boyunca tamponun düşmeye devam edip etmediğini izle. Bir değer L/t cinsinden gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen materyaller geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={2} />
</GameScene>

Yüksek basınç yapısı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplı Tuğlaları, Bronz Çerçeve Kutularını ve Bronz Dişli Kutusu Kasalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Çerçeve Kutuları ve Çelik Dişli Kutusu Kasalarıyla değiştir. Yalnızca kasaları değiştirmek veya bazı bronz çerçeveler ya da dişli kutuları bırakmak yeni yapının kademe kontrolünden geçmez.

Yükseltmeden önce işlemeyi ve materyal girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı ve üretimi geri açmadan önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç ayrı bir buhar sıvısı değil, bir yapı kademesidir. Makine yine sıradan buhar kullanır ve mevcut Buhar Kapağı ile buharlı veriyolları yeniden kullanılabilir. Enerji Kapağı gerekmez. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik çekmez veya ürünleri onlara itmez; bir veriyolunun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Eşyaları Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan.
- **Çıktı:** Ürünleri depolamaya veya sonraki makineye yönlendirmek için Çıkış Yolunun ön yüzünden borular, kanallar veya konveyörlerle aktif olarak çek.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Eşya veriyolları buhar alamaz.
- **Yönlendirme:** Cevherler, Ezilmiş Cevher, Saf Olmayan Toz ve diğer materyaller için filtreler ayarla; ara ürünler yanlış işleme adımına girmesin.

Aynı öğütücü bir cevher işleme hattındaki birkaç adıma hizmet edebilir. Hem ham cevherler hem de yeni üretilen Ezilmiş Cevher aynı Giriş Yoluna geri gönderiliyorsa, bir adımın girdi yuvalarını sürekli doldurmaması için filtreleri ve öncelikleri kontrol et. Birkaç adım boyunca sürekli işleme için ayrı makineler düşün ve tüm hattın paylaştığı buhar beslemesini kontrol et.

Ek Giriş Yolları eşya tamponlamasını genişletirken ek Çıkış Yolları çıktı tıkanıklığını önlemeye yardımcı olur. İkisi de paralel sınırını artırmaz veya yan ürünlerin kilidini açmaz. Genişletirken en az 14 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Eksik yeni yapı | Ayak izi 3×3 ve yükseklik dört blok mu? Kontrolcü ikinci katmanın ön ortasında mı? İkinci ve üçüncü katmanlardaki sekiz Çerçeve Kutusu ve üstteki Dişli Kutusu Kasası doğru konumda mı? |
| Yapı kademesi uyuşmazlığı | Kasalar, Çerçeve Kutuları ve Dişli Kutusu Kasası aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Eksik Buhar Kapağı veya veriyolları | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya veriyolları mı kullanıldı? |
| Veriyolu ekledikten sonra yapı başarısız | En az 14 gerçek kasa kaldı mı? Herhangi bir Çerçeve Kutusu veya Dişli Kutusu Kasası veriyoluyla değiştirildi mi? |
| Girdiler var ama tarif bulunamıyor | Eşyanın bir Öğütücü tarifi var mı? Bir tarif için yeterli girdi var mı? Yeterli çıktı alanı var mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınç yapısı da MV veya daha yüksek kademe tarifleri işleyemez. |
| NEI, makinenin üretmediği yan ürünleri gösteriyor | Makine yalnızca ilk eşya çıktısını üretir. Çıkış Yolu eklemek veya yüksek basınç yapısına yükseltmek kalan çıktıların kilidini açmaz. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buharlı veriyolları eşyaları otomatik çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin kopyaları için yeterli materyal var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](../multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Steam Grinder](https://wiki.gtnewhorizons.com/wiki/Steam_Grinder)