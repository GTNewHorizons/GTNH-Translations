---
item_ids:
  - gregtech:gt.blockmachines:31086
navigation:
  title: Buharlı Alaşım İzabesi
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31086
  position: 8
quest_ids:
  - WGhhKERfRTiJXKZEPoRf1Q
---

# Buharlı Alaşım İzabesi

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={1} />
</GameScene>

The <ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" />, Buhar çağında kullanılabilen bir multiblok Alaşım İzabesidir. Alaşımları partiler hâlinde üretmek ve uygun kalıplama tariflerini işlemek için buhar kullanır. Tek bloklu Buharlı Alaşım İzabesine yükseltme olarak aynı tarifin en fazla sekiz kopyasını aynı anda işleyebilir; Bronz, Kırmızı Alaşım, Pirinç ve diğer malzemeleri üretir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Yüksek basınçlı yapıya yükseltmek işleme kapasitesini artırır ancak maksimum tarif kademesini yükseltmez. Makine buharla çalışır ve kömür veya başka yakıt, ısıtma bobinleri ya da fırın sıcaklığı ayarı gerektirmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi bir Tumbaga Çerçeve, Bronz Sıvı Boruları, Yüksek Fırınlar ve diğer malzemeler gerektirir |
| Boyutlar | Üç blok genişliğinde, dört blok derinliğinde ve üç blok yüksekliğinde; kontrolcü ikinci katmanın ön merkezinde |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altındaki, en fazla 32 EU/t gerektiren Alaşım İzabesi tarifleri |
| Eşya arayüzleri | En az bir Buharlı Giriş Yolu ve bir Buharlı Çıkış Yolu; sıradan elektrikli makine eşya yolları bunların yerini alamaz |
| Sıvı arayüzleri | Güç için yalnızca bir Buhar Kapağı gerekir; sıradan Giriş ve Çıkış Kapakları kabul edilmez |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı artırmaz |
| İşleme süresi | Temel yapıda NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınçta 0,8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için mevcut tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31086" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki miktarlar bir Buhar Kapağı, bir Giriş Yolu ve bir Çıkış Yolu varsayar. Temel yapı Bronz Kaplamalı Tuğlalar ve Bronz Boru Muhafazaları kullanır; yüksek basınçlı yapı ise bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar ve Boru Muhafazaları aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Temel kurulumda 26; aşağıdaki kapak veya yollarla değiştirilebilir, ancak en az 25 gerçek kasa kalmalıdır |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | İki adet, ikinci katmanın merkezi boyunca, doğrudan kontrolcünün arkasında |
| Cam | <ItemLink id="minecraft:glass" showIcon="left" /> veya desteklenen başka bir cam | Mevcut cam yeniden kullanılabilir | Dört adet: her Boru Muhafazasının solunda ve sağında birer adet |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31086" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön merkezinde |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | En az bir adet, bir kasanın yerine |

Yapıda kasa veya kapaklar için 29 konum vardır. Gerekli üç arayüzü takmak 26 kasa bırakır. En fazla bir kasa daha ek bir Buharlı Giriş veya Çıkış Yolu ile değiştirilebilir; daha fazla arayüz eklemek 25'ten az kasa bırakır. Kapaklar ve yollar camı veya Boru Muhafazalarını değiştiremez.

Alt ve üst katmanlar tam 3×4 düzlemlerdir. İkinci katman önden arkaya doğru “kasa, kontrolcü, kasa”, “cam, boru, cam”, “cam, boru, cam” ve üç kasalık bir sıradan oluşur. Kapağı ve yolları kasa konumlarına yerleştir.

> [!NOTE]
> Bu makinede Sıradan Cam çalışır. Projeksiyon Borosilikat Cam gösterdiği için Bor elde etmen gerekmez. Camın bronz veya çelik yapı kademesiyle eşleşmesi gerekmez ve yüksek basınca yükseltirken korunabilir.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 yüksek basınçlı yapıyı seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

Buharlı Alaşım İzabesi **Alaşım İzabesi tarif haritasını** kullanır; İngilizce NEI'de **Alloy Smelter** olarak görünür. NEI'yi kontrol ederken tarifin Alaşım İzabesine ait olduğunu doğrula, ardından girdi biçimlerini, oranları, tarif kademesini ve gereken kalıbı kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Yaygın alaşımlar | Bakır ve Kalay Bronz yapar; Bakır ve Çinko Pirinç yapar. NEI'de gösterilen külçe, toz veya diğer girdi biçimlerini kullan. |
| Devre ve tel malzemeleri | Bakır ve Kızıltaş Kırmızı Alaşım yapar; Gümüş ve Elektrotin Mavi Alaşım yapar |
| Diğer düşük gerilim alaşımları | Altın ve Gümüş Elektrum yapar, Kurşun ve Antimon Pil Alaşımı yapar, Kalay ve Antimon Lehim Alaşımı yapar; kesin oranlar için NEI'yi kontrol et |
| Kauçuk işleme | Ham Kauçuk Tozu ve Sülfür Tozu, daha ileri kauçuk ürünleri için Kauçuk Çubukları yapar |
| Kalıplama | Uygun tariflerde ilgili kalıbı kullanarak metal külçe parçaları, külçeler, dişliler, eşya kasaları ve diğer parçaları yapar; kalıp ve malzeme miktarları için NEI'yi kontrol et |

Alaşım tarifleri, önce alaşım tozunu karıştırıp eritmeden doğrudan alaşım külçeleri üretir. Ancak makine her Fırın veya Elektrikli Yüksek Fırın tarifini kabul etmez. Sıradan eritme için [Buharlı Ocak](./steam_hearth.md) kullan, yüksek fırın sıcaklığı veya daha yüksek gerilim gerektiren tarifler için uygun makineyi kullan.

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Yüksek basınçlı çelik yapı makinenin yapı kademesini yükseltir. MV veya daha yüksek tarifleri etkinleştirmez. Uyumluluğu yalnızca malzeme adına bakarak değerlendirmek yerine belirli tarifin EU/t değerini kontrol et.

### Girdi Oranları ve Bronz Üretimi

Yaygın bir Bronz tarifi **üç Bakır Külçesi ve bir Kalay Külçesi kullanarak dört Bronz Külçesi üretir**. İlgili tozları veya külçe ve toz karışımını kullanan tarifler de vardır. Girdi biçimlerini NEI'ye göre seç; külçe miktarlarını kullanarak Minik Toz Yığınları, Küçük Toz Yığınları veya metal külçe parçalarıyla ikame etme.

Tüm alaşımlar aynı girdi oranını kullanmaz. Örneğin Kırmızı Alaşım Bakır ve Kızıltaş kullanırken Lehim Alaşımı Kalay ve Antimon kullanır. Malzemeleri değiştirirken Bronz oranını yeniden kullanmak yerine NEI'yi tekrar kontrol et.

### Kalıplar ve Malzeme Şekillendirme

Bazı Alaşım İzabesi tarifleri kalıp gerektirir. NEI'de belirtilen kalıbı ve malzemeyi birlikte Buharlı Giriş Yoluna koy. Tarif tarafından tüketilmediği işaretlenen kalıplar yeniden kullanılabilir kalır; sekiz paralel sekiz kalıp gerektirmez.

Alaşım İzabesi kalıpları ve Ekstrüder Şekilleri farklı eşyalardır. Simgeleri veya hedef şekilleri benzer görünse bile Alaşım İzabesi tarifinin belirttiği kalıbı kullan. Bir kalıp yalnızca o tarifin kabul ettiği malzemeleri şekillendirir; makinenin daha yüksek gerilimli tarifleri işlemesini sağlamaz.

Tek bir parçanın sürekli üretimi için kalıp için bir girdi yuvası ayır ve aktarım ekipmanını yalnızca tüketilen malzemeleri yeniden dolduracak şekilde yapılandır. Kalıpları değiştirmeden önce malzeme beslemeyi durdur, mevcut işlemin bitmesini bekle ve başka bir kalıplama tarifinin çalışmasını önlemek için kalan girdileri temizle.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı, Buharlı Giriş Yolu ve Buharlı Çıkış Yolunun takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve buharın gerçekten içeri girdiğini doğrula.
3. NEI'de girdi biçimlerini, oranları ve tarif kademesini kontrol et; gerekiyorsa ilgili kalıbı yerleştir.
4. Çıkış için yer bırak ve makineyi az miktarda malzemeyle çalıştır.
5. Girdi oranlarını, buhar tamponunu ve çıkış yolunu izle. Sürekli buhar beslemesini doğruladıktan sonra paralel sayısını artır.

## Buhar Beslemesi ve İşleme Kapasitesi

Buharlı Alaşım İzabesi aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı alaşım tarifi çalıştırabileceği veya bir döngünün yalnızca sekiz eşya tükettiği anlamına gelmez. Gerçek paralel sayısı ayrıca her girdinin miktarına, çıkış alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alır, yüksek basınçlı yapı ise yaklaşık 0,8 katını alır. Örneğin on saniye olarak gösterilen bir Bronz tarifi temel yapıda yaklaşık 16 saniye, yüksek basınçta sekiz saniye sürer. Sekiz paralelde bu döngü 32 Bronz Külçesi üretir; süresi tekrar sekize bölünmez.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işleme süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |
| Tarif başına girdiler ve çıktılar | NEI'de gösterildiği gibi | Temel yapıyla aynı |

Temel yapı, tek bloklu bronz Buharlı Alaşım İzabesinin hızının %125'inde ve paralel başına buhar tüketim oranının %62,5'inde çalışır. Aynı tarif için toplam buhar tüketimi tek bloklu makinenin yaklaşık %50'sidir. Ancak daha fazla paralel çalıştırmak yine de tüm makinenin buhar tüketim oranını artırır, bu nedenle tek bir tek bloklu makine için boyutlandırılmış besleme maksimum paralelde üretim için yeterli değildir.

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak işleme kapasitesini iyileştirir; tarif başına toplam buhar tüketimi temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamalarından da etkilenir.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır. Birkaç makine aynı boruyu paylaşıyorsa her makineye ulaşan gerçek akışı da hesaba kat.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek ve sürekli işleme sırasında tamponun düşmeye devam edip etmediğini izlemek için Waila'yı kullan. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru kapasitesini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın tükenmesi mevcut işlemi iptal eder ve zaten tüketilen malzemeler geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru kapasitesini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31086" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları ve Bronz Boru Muhafazalarını tabloda listelenen Sağlam Çelik Makine Kasaları ve Çelik Boru Muhafazalarıyla değiştir. Mevcut cam, Buhar Kapağı ve buhar yolları yeniden kullanılabilir.

Yükseltmeden önce işlemeyi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı, malzemeleri ve üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınçlı yapı, makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek tariflerin kilidi açılmaz.

## Otomasyon ve Eşya Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her biri dört eşya yuvasına sahiptir. Yanlarındaki sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; otomasyon için yolanın yanına sandık koymak yeterli değildir.

- **Girdi:** Malzemeleri Giriş Yolunun ön yüzüne göndermek için Huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Her girdi için yuva ayır ve bunları tarif oranına göre yenile.
- **Kalıplar:** Gerektiren tarifler için ilgili kalıbı bulundur. Çıkarma ekipmanının kalıbı almasını önle ve yanlış kalıbın eklenmesini önlemek için girdi filtrelerini kullan.
- **Çıktı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden etkin şekilde çek, ardından ürünleri alaşım deposuna, plaka üretimine veya diğer işlemlere yönlendir.
- **Buhar:** Kazandan Buhar Kapağına sıvı boruları bağla. Sıradan bir Giriş Kapağı güç için Buhar Kapağının yerini alamaz.
- **Tarif değiştirme:** Kalan girdileri ve kalıpları temizlemeden önce malzeme beslemeyi durdur ve mevcut işlemin bitmesini bekle. Yolu farklı tarifler için az miktarda malzemeyle doldurmaktan veya bunları istenmeyen bir alaşımda birleştirmekten kaçın.

Temel kurulum en fazla bir ek Buharlı Giriş veya Çıkış Yoluna izin verir. Tıkanıklığın oluştuğu yere göre daha fazla girdi veya çıktı tamponlaması arasında seçim yap. Ek yollar paralel sınırını artırmaz, en az 25 gerçek kasa kalmalıdır ve ikinci bir Buhar Kapağı takılamaz.

> [!WARNING]
> Tüm ürünler toplanacaksa GUI'de boşaltmayı “Hiçbir Şeyi Hiçleme” olarak ayarla. Etkin boşaltma nedeniyle alaşımları ve kalıplanmış parçaları kaybetmemek için Çıkış Yolu veya depolama dolduğunda çıkış tıkanıklığını gider.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yapı | Yapı üç blok genişliğinde, dört blok derinliğinde ve üç blok yüksekliğinde mi? Kontrolcü ikinci katmanın ön merkezinde mi? İki Boru Muhafazası ve dört cam bloğu doğru konumda mı? |
| Yapı kademesi uyuşmazlığı | Kasalar ve Boru Muhafazaları tamamen aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Cam konumları kontrolü geçemiyor | Sıradan Cam gibi desteklenen cam blokları mı kullanıldı? Yanlışlıkla Cam Panelleri veya desteklenmeyen Dekoratif bloklar mı kullanıldı? |
| Eksik Buhar Kapağı veya yollar | Tam olarak bir Buhar Kapağı ve en az bir Buharlı Giriş Yolu ile Çıkış Yolu var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Arayüz ekledikten sonra yapı başarısız oluyor | En az 25 gerçek kasa kaldı mı? Cam veya Boru Muhafazaları kapaklarla mı değiştirildi? Yanlışlıkla sıradan Giriş veya Çıkış Kapakları mı eklendi? |
| Girdiler var ama tarif bulunamıyor | Tarif bir Alaşım İzabesi tarifi mi? Girdi biçimleri ve oranları NEI ile eşleşiyor mu? Kalıp doğru mu? Yeterli çıkış alanı var mı? |
| Bakır var ama Bronz üretimi duruyor | Yeterli Kalay var mı, yoksa Bakır her girdi yuvasını doldurup Kalayı mı engelliyor? Yanlışlıkla Bakır Külçe Parçaları, Minik Bakır Tozu Yığınları veya başka girdi biçimleri mi kullanıldı? |
| Kalıp yerleştirildi ama şekillendirme olmuyor | Yanlışlıkla bir Ekstrüder Şekli mi kullanıldı? NEI o malzeme için bir kalıplama tarifi gösteriyor mu? Malzeme miktarı ve tarif kademesi gereksinimleri karşılanıyor mu? |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek tarifleri işleyemez. |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı diğer makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolanın yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Etkin aktarım ekipmanını, bağlantı yüzünü, yönünü ve filtreleri kontrol et. |
| Aynı anda sekizden az tarif işleniyor | Aynı tarifin sekiz kopyası için her girdiden yeterince var mı? Paralel sınırı daha düşük mü ayarlanmış? Çıkış Yolu tüm ürünleri tutabiliyor mu? |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Çince Wiki: Buharlı Alaşım İzabesi](https://gtnh.huijiwiki.com/wiki/大型蒸汽合金炉)