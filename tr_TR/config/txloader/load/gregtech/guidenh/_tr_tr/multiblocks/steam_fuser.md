---
item_ids:
  - gregtech:gt.blockmachines:31086
quest_ids:
  - WGhhKERfRTiJXKZEPoRf1Q
navigation:
  title: Buhar Kaynaştırıcı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31086
  position: -501
---
# Buhar Kaynaştırıcı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok Alaşım İzabesi'dir. Alaşımları partiler halinde üretmek ve uygun kalıplama tariflerini işlemek için buhar kullanır. Tek bloklu Buhar Alaşım İzabesi'nin yükseltmesi olarak aynı tarifin sekiz kopyasına kadar aynı anda işleyebilir; Bronz, Kırmızı Alaşım, Pirinç ve diğer materyalleri üretir.

Makinenin, aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınç yapısına yükseltmek işlem kapasitesini artırır, ancak azami tarif kademesini yükseltmez. Makine buharla çalışır; kömüre veya başka bir yakıta, ısıtma bobinlerine ya da fırın sıcaklığı ayarına ihtiyaç duymaz.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi bir Tumbaga Çerçeve Kutusu, Bronz Sıvı Boruları, Yüksek Fırınlar ve diğer materyalleri gerektirir |
| Boyutlar | Üç blok genişliğinde, dört blok derinliğinde ve üç blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altı Alaşım İzabesi tarifleri, en fazla 32 EU/t gerektiren |
| Eşya arayüzleri | En az bir buhar Giriş Yolu ve bir buhar Çıkış Yolu; sıradan elektrikli makine eşya veriyolları bunların yerini alamaz |
| Sıvı arayüzleri | Güç için yalnızca bir Buhar Kapağı gerekir; sıradan Girdi ve Çıkış Kapakları kabul edilmez |
| Paraleller | Aynı tarifin en fazla sekiz kopyası; yüksek basınç yapısı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınç için 0,8 katı |
| Yükseltmeler ve overclock | Yüksek basınç yapısı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31086" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Materyalleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğlalar ve Bronz boru muhafazası blokları kullanırken yüksek basınç yapısı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar ve boru muhafazası blokları tamamen aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınç yapısı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda 26; aşağıdaki kapak veya veriyollarıyla değiştirilebilir, ancak en az 25 gerçek kasa kalmalıdır |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | İki adet, ikinci katmanın ortası boyunca, kontrolcünün hemen arkasında |
| Cam | <ItemLink id="minecraft:glass" showIcon="left" /> veya desteklenen başka bir cam | Mevcut cam yeniden kullanılabilir | Dört adet: her boru muhafazasının bir solunda, bir sağında |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı veriyolu | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı veriyolu | En az bir adet, bir kasanın yerine |

Yapıda kasa veya kapak için 29 konum vardır. Gerekli üç arayüzü kurmak 26 kasa bırakır. En fazla bir kasa daha ek bir buhar Giriş veya Çıkış Yoluyla değiştirilebilir; daha fazla arayüz eklemek 25'ten az kasa bırakır. Kapaklar ve veriyolları camın veya boru muhafazası bloklarının yerini alamaz.

Alt ve üst katmanlar tam 3×4 düzlemlerdir. İkinci katman önden arkaya doğru "kasa, kontrolcü, kasa", "cam, boru, cam", "cam, boru, cam" ve üç kasadan oluşan bir sıradan oluşur. Kapağı ve veriyollarını kasa konumlarına yerleştir.

> [!NOTE]
> Sıradan Cam bu makinede çalışır. Projeksiyon Borosilikat Cam gösteriyor diye Bor elde etmek zorunda değilsin. Camın bronz veya çelik yapı kademesiyle eşleşmesi gerekmez ve yüksek basınca yükseltirken korunabilir.

Yapıyı önizlemek ve inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınç yapısını seçer. Yardımlı inşaattan sonra kapakları tak ve yapıyı kontrol et.

## Makinenin Kullanım Alanları

Buhar Kaynaştırıcı, İngilizce NEI'de **Alloy Smelter** olarak gösterilen **Alaşım İzabesi tarif haritasını** kullanır. NEI'ye bakarken tarifin Alaşım İzabesi'ne ait olduğunu doğrula; ardından girdi biçimlerini, oranları, tarif kademesini ve gereken kalıbı kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Yaygın alaşımlar | Bakır ve Kalay Bronz yapar; Bakır ve Çinko Pirinç yapar. NEI'de gösterilen külçe, toz veya diğer girdi biçimlerini kullan. |
| Devre ve tel materyalleri | Bakır ve Kızıltaş Kırmızı Alaşım yapar; Gümüş ve Elektrotin Mavi Alaşım yapar |
| Diğer düşük gerilim alaşımları | Altın ve Gümüş Elektrum, Kurşun ve Antimon Pil Alaşımı, Kalay ve Antimon Lehim Alaşımı yapar; kesin oranlar için NEI'ye bak |
| Kauçuk işleme | Ham Kauçuk Tozu ve Sülfür Tozu, ileri kauçuk ürünleri için Kauçuk Çubukları yapar |
| Kalıplama | Uygun tariflerde ilgili kalıbı kullanarak metal kırıntıları, külçeler, dişliler, eşya kasaları ve diğer parçaları üretir; kalıp ve materyal miktarları için NEI'ye bak |

Alaşım tarifleri doğrudan alaşım külçeleri üretir; önce alaşım tozu karıştırıp eritmek gerekmez. Ancak makine her Fırın veya Elektrikli Yüksek Fırın tarifini kabul etmez. Sıradan eritme için [Buhar Ocağı](./steam_hearth.md) kullan, yüksek fırın sıcaklığı veya daha yüksek gerilim gerektiren tarifler için uygun makineyi kullan.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapı makinenin yapı kademesini yükseltir. MV veya daha yüksek tarifleri etkinleştirmez. Uyumluluğu yalnızca materyal adına bakarak değerlendirmek yerine ilgili tarifin EU/t değerini kontrol et.

### Girdi Oranları ve Bronz Üretimi

Yaygın bir Bronz tarifi **üç Bakır Parçası ve bir Kalay Parçası kullanarak dört Bronz Parçası üretir**. İlgili tozları veya külçe ve toz karışımını kullanan tarifler de vardır. Girdi biçimlerini NEI'ye göre seç; külçe miktarlarıyla Minik Toz Yığınlarını, Küçük Toz Yığınlarını veya metal kırıntılarını ikame etme.

Tüm alaşımlar aynı girdi oranını kullanmaz. Örneğin Kırmızı Alaşım Bakır ve Kızıltaş kullanırken Lehim Alaşımı Kalay ve Antimon kullanır. Materyal değiştirdiğinde Bronz oranını yeniden kullanmak yerine NEI'ye tekrar bak.

### Kalıplar ve Materyal Şekillendirme

Bazı Alaşım İzabesi tarifleri kalıp gerektirir. NEI'de belirtilen kalıbı ve materyali birlikte buhar Giriş Yoluna koy. Tarif tarafından tüketilmediği belirtilen kalıplar yeniden kullanılabilir; sekiz paralel sekiz kalıp gerektirmez.

Alaşım İzabesi kalıpları ve Ekstrüder Şekilleri farklı eşyalardır. Simgeleri veya hedef şekilleri benzer görünse bile Alaşım İzabesi tarifinin belirttiği kalıbı kullan. Bir kalıp yalnızca o tarifin kabul ettiği materyalleri şekillendirir; makinenin daha yüksek gerilimli tarifleri işlemesini sağlamaz.

Tek bir parçanın sürekli üretimi için kalıba bir girdi yuvası ayır ve aktarma ekipmanını yalnızca tüketilen materyalleri tamamlayacak şekilde yapılandır. Kalıpları değiştirmeden önce materyal beslemeyi durdur, mevcut işlemin bitmesini bekle ve yanlışlıkla başka bir kalıplama tarifinin çalışmaması için kalan girdileri temizle.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağının, buhar Giriş Yolunun ve buhar Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de girdi biçimlerini, oranları ve tarif kademesini kontrol et; gerekiyorsa ilgili kalıbı yerleştir.
4. Çıktı için yer bırak ve makineyi az miktarda materyalle çalıştır.
5. Girdi oranlarını, buhar tamponunu ve çıktı güzergâhını izle. Sürekli buhar beslemesini doğruladıktan sonra paralelleri artır.

## Buhar Beslemesi ve İşlem Kapasitesi

Buhar Kaynaştırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, tek döngüde sekiz farklı alaşım tarifi çalıştırabileceği ya da bir döngünün yalnızca sekiz eşya tükettiği anlamına gelmez. Gerçek paralel sayısı ayrıca her girdinin miktarına, çıktı alanına ve arayüzde ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını, yüksek basınç yapısı ise yaklaşık 0,8 katını alır. Örneğin on saniye gösterilen bir Bronz tarifi temel yapıda yaklaşık 16 saniye, yüksek basınçta sekiz saniye sürer. Sekiz paralelle bu döngü 32 Bronz Parçası üretir; süresi tekrar sekize bölünmez.

| Özellik | Temel yapı | Yüksek basınç yapısı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Azami paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Referans | Temel yapıyla yaklaşık aynı |
| Tarif başına girdiler ve çıktılar | NEI'de gösterildiği gibi | Temel yapıyla aynı |

Temel yapı, tek bloklu bronz Buhar Alaşım İzabesi'nin hızının %125'inde ve paralel başına buhar tüketim oranının %62,5'inde çalışır. Aynı tarif için toplam buhar tüketimi tek bloklu makinenin yaklaşık %50'sidir. Ancak daha fazla paralel çalıştırmak yine de makinenin tamamının buhar tüketim oranını artırır, bu yüzden tek bloklu bir makine için ölçeklenmiş bir besleme azami paralelde üretim için yeterli değildir.

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak işlem kapasitesini iyileştirir; tarif başına toplam buhar tüketimi temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici açıkları kapatır ve sürekli kazan üretiminin yerini tutamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır. Birkaç makine aynı boruyu paylaşıyorsa her makineye ulaşan gerçek akışı da hesaba kat.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izlemek için Waila'yı kullan. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru işlem kapasitesini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse arayüzdeki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve tüketilen materyaller iade edilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru işlem kapasitesini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={2} />
</GameScene>

Yüksek basınç yapısı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları ve Bronz boru muhafazası bloklarını tabloda listelenen Sağlam Çelik Makine Kasaları ve Çelik boru muhafazası bloklarıyla değiştir. Mevcut cam, Buhar Kapağı ve buhar veriyolları yeniden kullanılabilir.

Yükseltmeden önce işlemi ve materyal girişini durdur. Bileşenleri değiştirdikten sonra yapıyı tekrar kontrol et ve buharı, materyalleri ve üretimi geri açmadan önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç makinenin yapı kademesidir. Yine sıradan buhar kullanır. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak azami sekiz paralel olarak kalır ve MV veya daha yüksek tariflerin kilidi açılmaz.

## Otomasyon ve Eşya Yönlendirme

Buhar Giriş ve Çıkış Veriyollarının her birinde dört eşya yuvası vardır. Bitişik sandıklardan otomatik olarak eşya çekmez veya ürünleri onlara itmez; bir veriyolunun yanına sandık koymak otomasyon için yeterli değildir.

- **Girdi:** Materyalleri Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Her girdi için yuva ayır ve bunları tarif oranına göre tamamla.
- **Kalıplar:** Gerektiren tarifler için ilgili kalıbı bulundur. Çıkarma ekipmanının kalıbı almasını önle ve yanlış kalıp yerleştirmemek için girdi filtreleri kullan.
- **Çıktı:** Çıkış Yolunun ön yüzünden borular, kanallar veya konveyörlerle etkin şekilde çıkar, ardından ürünleri alaşım deposuna, plaka üretimine veya diğer işlemlere yönlendir.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Sıradan bir Girdi Kapağı güç için Buhar Kapağının yerini alamaz.
- **Tarif değiştirme:** Materyal beslemeyi durdur ve kalan girdileri ve kalıpları temizlemeden önce mevcut işlemin bitmesini bekle. Veriyolunu farklı tarifler için az miktarda materyalle doldurmaktan veya bunları istenmeyen bir alaşımda birleştirmekten kaçın.

Temel kurulum en fazla bir ek buhar Giriş veya Çıkış Yoluna izin verir. Tıkanıklığın nerede oluştuğuna göre daha fazla girdi veya çıktı tamponlaması arasında seçim yap. Ek veriyolları paralel sınırını yükseltmez, en az 25 gerçek kasa kalmalıdır ve ikinci bir Buhar Kapağı takılamaz.

> [!WARNING]
> Tüm ürünlerin toplanması gerektiğinde arayüzde yok etmeyi "Void Nothing" olarak ayarla. Etkin yok etme nedeniyle alaşımları ve kalıplanmış parçaları kaybetmemek için Çıkış Yolu veya depo dolduğunda çıktı tıkanıklığını gider.

## Sorun Giderme

| Belirti | Neye bakmalısın |
| --- | --- |
| Eksik yapı | Yapı üç blok genişliğinde, dört blok derinliğinde ve üç blok yüksekliğinde mi? Kontrolcü ikinci katmanın ön ortasında mı? İki boru muhafazası ve dört cam blok doğru konumda mı? |
| Yapı kademesi uyuşmazlığı | Kasalar ve boru muhafazası blokları tamamen aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Cam konumları kontrolden geçmiyor | Sıradan Cam gibi desteklenen cam bloklar mı kullanıldı? Yanlışlıkla Cam Panel veya desteklenmeyen dekoratif blok mu kullanıldı? |
| Buhar Kapağı veya veriyolları eksik | Tam olarak bir Buhar Kapağı ve en az bir buhar Giriş Yolu ile Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya veriyolları mı kullanıldı? |
| Arayüz ekledikten sonra yapı başarısız | En az 25 gerçek kasa kaldı mı? Cam veya boru muhafazası blokları kapaklarla mı değiştirildi? Yanlışlıkla sıradan Giriş veya Çıkış Kapağı mı eklendi? |
| Girdiler var ama tarif bulunamıyor | Tarif bir Alaşım İzabesi tarifi mi? Girdi biçimleri ve oranları NEI ile eşleşiyor mu? Kalıp doğru mu? Yeterli çıktı alanı var mı? |
| Bakır var ama Bronz üretimi duruyor | Yeterli Kalay var mı, yoksa Bakır tüm girdi yuvalarını doldurup Kalay'ı mı engelliyor? Yanlışlıkla Bakır Kırıntısı, Minik Bakır Tozu Yığını veya başka bir girdi biçimi mi kullanıldı? |
| Kalıp yerleştirildi ama şekillendirme olmuyor | Yanlışlıkla bir Ekstrüder Şekli mi kullanıldı? NEI o materyal için kalıplama tarifi gösteriyor mu? Materyal miktarı ve tarif kademesi gereksinimleri karşılanıyor mu? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınç yapısı da MV veya daha yüksek tarifleri işleyemez. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı başka makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buhar veriyolları otomatik olarak eşya çekmez veya itmez. Etkin aktarma ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin sekiz kopyası için her girdiden yeterli var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıkış Yolu tüm ürünleri tutabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buhar Kaynaştırıcı](https://wiki.gtnewhorizons.com/wiki/Steam_Fuser)