---
item_ids:
  - gregtech:gt.blockmachines:31041
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKzA
navigation:
  title: Buharlı Öğütücü
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31041
  position: -501
---
# Buharlı Öğütücü
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" />, Buhar çağında bulunabilen bir multiblok Öğütücü'dür. Cevherleri ve malzemeleri partiler hâlinde öğütmek için buhar kullanır. Tek blok Buharlı Öğütücü'nün yükseltmesi olarak aynı tarifin sekiz kopyasına kadarını aynı anda işleyebilir ve erken cevher işleme hatlarında işe yarar.

Makinenin aynı Kontrolcüyü paylaşan basit bronz ve Yüksek Basınçlı çelik yapıları vardır. Yüksek basınçlı yapıya yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez ve ek cevher yan ürünleri sağlamaz.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma kademesi | Buhar; Kontrolcü tarifi Elmas, Piston, bir Tumbaga Çerçeve ve diğer malzemeler gerektirir |
| Boyutlar | 3×3 taban alanı, dört blok yüksekliğinde; Kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki Öğütücü tarifleri, en fazla 32 EU/t gerektirir |
| Çıktı sınırı | Yalnızca tarifin çıktı listesindeki ilk eşya; yüksek basınçlı yapı çıktı türü eklemez |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; daha düşük tarif gücü bu sınırı yükseltmez |
| İşleme bonusları | Basit yapı, tek blok bronz Buharlı Öğütücü'nün hızının %125'inde çalışır ve paralel başına buhar tüketim oranı onun oranının %62.5'idir |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, Kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, basit Kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31041" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Basit yapı bronz bileşenler kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki Kasalar, Çerçeveler ve Dişli Kutusu Kasaları aynı kademeden olmalıdır.**

| Bileşen | Basit yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Basit kurulumda 17; aşağıdaki kapaklar veya yollar ile değiştirilebilir, ancak en az 14 gerçek Kasa kalmalı |
| Çerçeve | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Sekiz; ikinci ve üçüncü katmanların dört köşesinde |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | Bir; dördüncü katmanın ortasında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31041" showIcon="left" /> | Aynı Kontrolcü | Bir; ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı Kapak | Tam olarak bir; bir Kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı Yol | En az bir; bir Kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı Yol | En az bir; bir Kasanın yerine |

Yeni yapıda Kasa veya Kapak için 20 konum vardır. Gerekli üç arayüzü kurmak 17 Kasa bırakır; Yol eklemek Kasa sayısını buna göre azaltır. Kapaklar ve Yollar Çerçevelerin veya Dişli Kutusu Kasalarının yerine geçemez.

### Katman Katman İnşa

Katmanları tabandan yukarıya doğru say. Önce Kontrolcünün yönünü seç, ardından etkileşimli yapıyı veya hologramı katman katman takip et.

| Katman | Ne yerleştirilecek |
| --- | --- |
| Birinci | Tam 3×3 taban, dokuz Kasa konumu verir |
| İkinci | Dört köşenin tamamında Çerçeveler, ön ortada Kontrolcü ve sol, sağ ve arka kenarların ortasında birer Kasa konumu |
| Üçüncü | Dört köşenin tamamında Çerçeveler ve dört kenarın her birinin ortasında birer Kasa konumu |
| Dördüncü | Ortada bir Dişli Kutusu Kasası ve dört kenarın her birinin ortasında birer Kasa konumu; dört köşede blok gerekmez |

İkinci ve üçüncü katmanlardaki boş merkez konumlarının Kasa ile doldurulması gerekmez. Buhar Kapağını ve buharlı Giriş ve Çıkış Yollarını kolay boru bağlantıları için uygun Kasa konumlarına yerleştir. Sıradan elektrikli makine eşya yolları buharlı sürümlerin yerine geçemez.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 basit yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

> [!NOTE]
> Bu sayfa 2.9.0'daki yeni yapıyı açıklar. Mevcut RC-2 eski içi boş 3×3×3 yapıyı da kabul eder, ancak hologram ve yardımlı inşa yeni yapıyı kullanır. Eski sayfanın tarif gücüne dayalı paralel açıklaması mevcut sürüm için geçerli değildir; makinenin maksimumu sekiz paralel olarak sabittir.

## Makine Kullanımları ve Çıktılar

Buharlı Öğütücü, Öğütücü tarif haritasını kullanır. NEI'yi kontrol ederken önce eşyanın Öğütücü tarifi olup olmadığını doğrula, ardından kademesini, girdi miktarını ve **ilk eşya çıktısını** kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| İlk cevher kırma | Uygun cevherleri Ezilmiş Cevher'e dönüştürür; bu adım birçok yaygın cevher için ana çıktı miktarını artırır, kesin verimler NEI'de gösterilir |
| Cevher ara ürünlerini öğütme | Uygun Ezilmiş Cevheri Safsızlıklı Toz'a ve Santrifüjlenmiş Cevheri toza dönüştürür; makine sonraki yıkama, santrifüjleme veya eritme adımlarını otomatik olarak yapmaz |
| Malzeme öğütme | Külçeleri, değerli taşları ve eşleşen tarifi olan diğer malzemeleri alaşımlar ve ileri işleme için toza dönüştürür |
| Eşya geri dönüşümü | Öğütücü geri dönüşüm tarifleri olan bileşenleri veya eşyaları işler; hâlâ ihtiyacın olan eşyaları göndermeden önce çıktıları kontrol et |

### Neden Yan Ürün Yok

Makine yalnızca Öğütücü tarifinin çıktı listesindeki **ilk eşya çıktısını** üretir. NEI'de ikinci ve sonraki konumlardaki eşyalar, çıktı şansları olsa bile üretilmez. Bu, Çıkış Yolu'ndaki yuva eksikliği değil, makinenin bir sınırlamasıdır.

Örneğin bir tarif ana mineral, bir cevher yan ürünü ve Taş Tozu olmak üzere üç çıktı listeliyorsa Buharlı Öğütücü yalnızca ilk çıktının miktarını ve şansını kullanır. Çıkış Yolu eklemek, paralel sayısını artırmak veya yüksek basınçlı yapıya yükseltmek kalan çıktıları açmaz.

Öğütme adımından cevher yan ürünlerine ihtiyacın varsa <ItemLink id="gregtech:gt.blockmachines:303" showIcon="left" /> gibi daha fazla çıktısı olan makineleri düşün. Cevher yıkama ve santrifüjlemenin de kendi çıktıları vardır; her adımı makinesine ve NEI tarifine göre planla.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapıya yükseltmek MV veya daha yüksek kademeli tarifleri etkinleştirmez ve ilk eşya çıktısı sınırını değiştirmez.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, buharlı Giriş Yolu ve buharlı Çıkış Yolu'nun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içine girdiğini doğrula.
3. NEI'de tarif kademesini ve ilk eşya çıktısını kontrol et ve Çıkış Yolu'nda yer bırak.
4. Makineyi az miktarda malzemeyle başlat ve çıktı güzergâhını ve buhar tamponunu gözlemle.
5. Sürekli buhar beslemesini doğruladıktan sonra girdi miktarlarını ve paralel sayısını artır.

## Buhar Beslemesi ve Verim

Buharlı Öğütücü aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı eşya işleyebileceği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır. Daha düşük güçlü tarifler maksimumu sekizin üzerine çıkarmaz.

Basit yapı, tek blok bronz Buharlı Öğütücü'nün hızının %125'inde çalışır ve yaklaşık %80 süre alır. Paralel başına buhar tüketim oranı, tek blok makinenin oranının %62.5'idir. İki bonus birleştiğinde aynı miktarda malzeme için toplam buhar tüketiminin yaklaşık %50'si elde edilir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin anlık buhar ihtiyacını artırır.

| Özellik | Basit yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| Eşya çıktı türleri | Yalnızca tarifin ilk eşya çıktısı | Yalnızca tarifin ilk eşya çıktısı |
| Basit yapıya göre hız | 1× | 2× |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel değer | Basit yapıyla yaklaşık aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi artırır, eşya başına toplam buhar maliyetini tekrar yarıya indirmez. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini tutamaz. Kazanları ve boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila kullan ve sürekli işleme sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken uyumlu birimler kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31041" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve Kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Çerçeveleri ve Bronz Dişli Kutusu Kasalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Çerçeveler ve Çelik Dişli Kutusu Kasalarıyla değiştir. Yalnızca kasaları değiştirmek veya bazı bronz çerçeveleri ya da dişli kutularını bırakmak yeni yapının kademe kontrolünde başarısız olur.

Yükseltmeden önce işlemeyi ve malzeme girdisini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buhar ile üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç ayrı bir buhar sıvısı değil, bir yapı kademesidir. Makine hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı ve buharlı yollar yeniden kullanılabilir. Enerji Kapağı gerekmez. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Bitişik sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir sandığı yolun yanına koymak otomasyon için yeterli değildir.

- **Girdi:** Eşyaları Giriş Yolu'nun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolu'nun ön yüzünden aktif olarak çek ve ürünleri depolamaya ya da sonraki makineye yönlendir.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Eşya yolları buhar alamaz.
- **Yönlendirme:** Cevherler, Ezilmiş Cevher, Safsızlıklı Toz ve diğer malzemeler için filtreler ayarla, böylece ara ürünler yanlış işleme adımına girmez.

Aynı öğütücü bir cevher işleme hattında birkaç adıma hizmet edebilir. Hem ham cevherler hem de yeni üretilen Ezilmiş Cevher aynı Giriş Yoluna geri gönderiliyorsa, bir adımın girdi yuvalarını sürekli doldurmaması için filtreleri ve öncelikleri kontrol et. Birkaç adımdan geçen sürekli işleme için ayrı makineler düşün ve tüm hattın paylaştığı buhar beslemesini kontrol et.

Ek Giriş Yolları eşya tamponlamasını genişletirken ek Çıkış Yolları çıktı tıkanıklığını önlemeye yardımcı olur. İkisi de paralel sınırını yükseltmez veya yan ürünleri açmaz. Genişletirken en az 14 gerçek Kasa bırak ve ikinci bir Buhar Kapağı takma.

## Sorun Giderme

| Belirti | Neyi kontrol etmeli |
| --- | --- |
| Yeni yapı tamamlanmamış | Taban alanı 3×3 ve yükseklik dört blok mu? Kontrolcü ikinci katmanın ön ortasında mı? İkinci ve üçüncü katmanlardaki sekiz Çerçeve ve üstteki Dişli Kutusu Kasası doğru konumda mı? |
| Yapı kademesi uyuşmuyor | Kasalar, Çerçeveler ve Dişli Kutusu Kasası aynı kademede mi? Yalnızca bazı bronz bileşenler mi değiştirildi? |
| Buhar Kapağı veya yollar eksik | Tam olarak bir Buhar Kapağı ve en az bir buharlı Giriş Yolu ve Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Yol ekledikten sonra yapı başarısız oluyor | En az 14 gerçek Kasa kaldı mı? Herhangi bir Çerçeve veya Dişli Kutusu Kasası yollarla değiştirildi mi? |
| Girdi var ama tarif bulunamadı | Eşyanın Öğütücü tarifi var mı? Bir tarif için yeterli girdi var mı? Yeterli çıktı alanı var mı? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| NEI makinenin üretmediği yan ürünleri gösteriyor | Makine yalnızca ilk eşya çıktısını üretir. Çıkış Yolu eklemek veya yüksek basınçlı yapıya yükseltmek kalan çıktıları açmaz. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya diğer makinelerle buhar mı paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buharlı yollar eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin kopyaları için yeterli malzeme var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıktı yuvaları tüm ürünleri alabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buharlı Öğütücü](https://wiki.gtnewhorizons.com/wiki/Steam_Grinder)