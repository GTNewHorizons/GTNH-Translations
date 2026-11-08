---
item_ids:
  - gregtech:gt.blockmachines:31084
navigation:
  title: Buhar Karıştırıcısı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31084
  position: 7
quest_ids:
  - WEwrzX4ZRkSxJ3M6cBesfA
---

# Buhar Karıştırıcısı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={1} />
</GameScene>

Buhar çağında kullanılabilen bir multiblok Karıştırıcı olan <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" />, malzemeleri partiler halinde karıştırmak için buhar kullanır ve aynı tarifin sekiz kopyasına kadar aynı anda işleyebilir. Bronz Tozu, Pirinç Tozu, Ateş Kili Tozu ve diğer malzemeleri üretebilir; ayrıca Tuzlu Su gibi uygun ürünleri yapmak için sıvıları doğrudan alıp çıktı olarak verebilir.

Makinenin aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Buhar çağında kullanılabilen uygun Karıştırıcı tariflerini erişilebilir kılar. Yüksek basınç yapısına geçmek verimi artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Tumbaga Yüzükleri, Tumbaga Rotorları, bir Tumbaga Çerçeve Kutusu ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, dört blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV veya altında, sıvı hücresi içermeyen ve en fazla 32 EU/t gerektiren Karıştırıcı tarifleri |
| Eşya arayüzleri | Buhar Giriş ve Çıkış Yolları; sıradan elektrikli makine eşya veriyolları bunların yerini alamaz |
| Sıvı arayüzleri | Sıradan Girdi Kapakları tarif sıvılarını sağlar ve sıradan Çıkış Kapakları sıvı ürünleri toplar; güç için kullanılan Buhar Kapağından ayrıdır |
| Paraleller | Aynı tarifin en fazla sekiz kopyası; yüksek basınç yapısı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınç yapısı için 0,8 katı |
| Yükseltmeler ve overclock | Yüksek basınç yapısı hızı ve buhar tüketim oranını ikiye katlar; gerilim overclock'u yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağının güncel tarifleri aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31084" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki kurulum, eşya ve sıvı tariflerini işlemek için bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu, bir Girdi Kapağı ve bir Çıkış Kapağı kullanır. Temel yapı bronz bileşenleri kullanırken yüksek basınç yapısı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Çerçeve Kutuları, Dişli Kutusu Kasaları ve Boru Muhafazaları aynı kademeden olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınç yapısı | Adet ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan kurulumda 35 adet; aşağıdaki kapak veya veriyollarla değiştirilebilir, ancak en az 25 gerçek kasa kalmalı |
| Çerçeve Kutusu | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Dört adet: ikinci katmandaki merkezî Dişli Kutusu Kasasının önünde, arkasında, solunda ve sağında birer tane |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | İki adet: ikinci ve dördüncü katmanların her birinin merkezinde birer tane |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Bir adet, üçüncü katmanın merkezinde |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı veriyolu | Eşya girişleri için gerektiği kadar tak, bir kasanın yerine; Programlanmış Devre ayarını da sağlayabilir |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı veriyolu | Eşya çıkışları için gerektiği kadar tak, bir kasanın yerine |
| Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | Sıvı girişleri için gerektiği kadar tak, bir kasanın yerine |
| Çıkış Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıkışları için gerektiği kadar tak, bir kasanın yerine |

Yeni yapıda kasa veya kapak için 40 konum vardır. Yukarıda listelenen beş arayüzü takmak 35 kasa bırakır. Yalnızca toz karıştırmak için bir Buhar Kapağı, buharlı Giriş Yolu ve buharlı Çıkış Yolu yeterlidir ve 37 kasa kalır. Veriyolu veya kapak eklemek kasa sayısını buna göre azaltır, ancak en az 25 gerçek kasa kalmalıdır. Kapaklar ve veriyolları Çerçeve Kutularının, Dişli Kutusu Kasalarının veya Boru Muhafazalarının yerini alamaz.

Yapı kontrolü en az bir tür tarif giriş arayüzü ve en az bir tür çıkış arayüzü gerektirir; her eşya ve sıvı arayüzünün takılı olmasını gerektirmez. Gerçek işleme için tüm tarif girişleri ve çıkışları için arayüz sağla. Birden çok giriş sıvısı gerektiğinde tek bir sıradan Girdi Kapağı hepsini aynı anda tutamaz, bu yüzden karşılık gelen sayıda Girdi Kapağı sağla.

Yapıyı önizlemek ve inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınç yapısını seçer. Yardımlı inşadan sonra kapakları tak ve yapıyı kontrol et.

## Makine Kullanımları

### Tarif Haritası ve Sıvı Hücreleri

Buhar Karıştırıcısı **Multiblok Karıştırıcı tarif haritasını** kullanır; İngilizce NEI'de **Multiblock Mixer** olarak görünür. Sıvı hücresi içeren tek bloklu Karıştırıcı tarifleri genellikle bu haritada ilgili sıvıları doğrudan alıp veren tariflere dönüşür. Programlanmış Devreler dahil eşya gereksinimleri yine de karşılanmalıdır.

NEI'ye bakarken tarifin bu haritaya ait olduğunu doğrula; ardından eşya miktarlarını, sıvı türlerini ve miktarlarını, Programlanmış Devre yapılandırmasını, tarif kademesini ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Alaşım tozlarını karıştırma | Bakır Tozu ve Kalay Tozu Bronz Tozu olur; Bakır Tozu ve Çinko Tozu Pirinç Tozu olur. Giriş oranlarını ve devre yapılandırmasını kontrol et; ürün külçe değil tozdur. |
| Ateş Kili Tozu | Sonraki refrakter malzeme tarifleri için Tuğla Tozu ve Kil Tozu karıştırır |

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Bir alaşım tozunun, kimyasal karışımın veya başka bir malzemenin işlenip işlenemeyeceğini belirlemek için tarifin EU/t değerini kontrol et. Yüksek basınçlı çelik yapı, MV veya daha yüksek kademe tarifleri etkinleştirmez.

### Programlanmış Devreler ve Bronz Tozu

Birçok Karıştırıcı tarifi bir <ItemLink id="gregtech:gt.integrated_circuit:1" showIcon="left" /> gerektirir. NEI'nin gerektirdiği yapılandırmayı buharlı Giriş Yolu GUI'sinin devre yuvasında ayarla.

Mevcut yaygın Bronz Tozu tarifi, tarif başına **üç Bakır Tozu, bir Kalay Tozu ve 1'e ayarlanmış bir Programlanmış Devre** gerektirir ve **dört Bronz Tozu** üretir. Bakır Tozu ve Kalay Tozunu buharlı Giriş Yoluna gönder, devre yapılandırmasını 1'e ayarla ve Bronz Tozunu buharlı Çıkış Yolundan topla.

Sekiz paralelde bir döngü 24 Bakır Tozu ve sekiz Kalay Tozu tüketir ve 32 Bronz Tozu üretir. Sürekli çalışma sırasında 3:1 giriş oranını koru; böylece Bakır Tozu tüm yuvaları doldurup Kalay Tozunun girmesini engellemez.

Bronz Tozu için sonraki eritme düzenini NEI kullanarak ayarla. Diğer alaşım tozları Elektrikli Yüksek Fırın veya başka makineler gerektirebilir.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı ile gerekli eşya ve sıvı arayüzlerinin takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve her tarif sıvısını kendi sıradan Girdi Kapağına besle.
3. NEI'de sıvı hücresi içermeyen tarifi, tüm giriş miktarlarını, Programlanmış Devre yapılandırmasını ve tarif kademesini kontrol et.
4. Devreyi ayarla, tüm eşya ve sıvı çıkışları için yer bırak, sonra az miktarda malzemeyle başla.
5. Buhar tamponunu, giriş oranlarını ve çıktıları gözlemle. Sürekli giriş beslemesini ve çıktı toplamayı doğruladıktan sonra paralelleri artır.

## Buhar Beslemesi ve Verim

Buhar Karıştırıcısı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı tarif çalıştırabileceği veya bir döngünün yalnızca sekiz eşya tükettiği anlamına gelmez. Gerçek paraleller ayrıca giriş oranlarına, eşya ve sıvı miktarlarına, çıkış alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı, NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alırken yüksek basınç yapısı yaklaşık 0,8 katını alır. Örneğin iki saniye olarak gösterilen Bronz Tozu tarifi temel yapıda yaklaşık 3,2 saniye, yüksek basınç yapısında 1,6 saniye sürer. Paraleller bir döngüde işlenen tarif sayısını artırır, ancak döngünün süresini paralel sayısına bölmez.

| Özellik | Temel yapı | Yüksek basınç yapısı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel | Temel yapıyla yaklaşık aynı |
| Tarif başına girişler ve çıkışlar | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi iyileştirir; tarif başına toplam buhar maliyeti ise temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir. Sürekli üretim sırasında eşya ve tarif sıvısı aktarım hızları işlem hızıyla birlikte artmalıdır.

Buhar Kapağı 64.000 L buhar depolar, ancak bu yalnızca geçici eksikleri kapatır ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işleme sırasındaki buhar tüketim oranına** göre boyutlandır ve tarif sıvıları için ayrı hatlar kullan.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek ve sürekli işleme sırasında tamponun azalmaya devam edip etmediğini izlemek için Waila kullan. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, ardından kazan üretimini artır veya boru tesisatını iyileştir.

> [!WARNING]
> İşleme sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen eşyalar ile tarif sıvıları geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={2} />
</GameScene>

Yüksek basınç yapısı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. Tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Çerçeve Kutuları, Çelik Dişli Kutusu Kasaları ve Çelik Boru Muhafazalarıyla Bronz Kaplamalı Tuğlaların, Bronz Çerçeve Kutularının, Bronz Dişli Kutusu Kasalarının ve Bronz Boru Muhafazalarının **tümünü** değiştir.

Yükseltmeden önce işlemeyi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı, girişleri ve üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç, makinenin yapı kademesidir. Yine sıradan buhar kullanır ve mevcut Buhar Kapağı, buharlı veriyolları ile sıradan Giriş ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek kademe tarifler kullanılamaz.

## Otomasyon ve Çıktı Yönlendirme

Buharlı Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır ve Giriş Yolunda ek bir devre yuvası bulunur. Bitişik sandıklardan otomatik olarak eşya çekmez veya ürünleri onlara itmezler; otomasyon için bir veriyolunun yanına sandık koymak yeterli değildir.

- **Eşya girişi:** Malzemeleri Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Doğru tarif oranlarını sağla ve her toz türü için yuva ayır.
- **Eşya çıkışı:** Çıkış Yolunun ön yüzünden borular, kanallar veya konveyörlerle etkin şekilde çek, sonra ürünleri malzeme deposuna veya bir sonraki işleme makinesine yönlendir.
- **Sıvı girişi:** Her sıvı türü için ayrı hatlar ve Girdi Kapakları kullan; filtreleri, sıvı kilitlerini ve miktarları kontrol et. Buhar besleme hattını Buhar Kapağına bağla.
- **Sıvı çıkışı:** Ürünleri Çıkış Kapağından çek veya otomatik çıkış için ön yüzüne bir tank yerleştir.
- **Programlanmış Devre:** Bir malzeme üretirken gerekli yapılandırmayı koru. Tarifleri değiştirmeden önce girişi durdur ve mevcut işlemin bitmesini bekle, sonra kalan eşya ve sıvıları işle ve devreyi ayarla.
- **Kapak renkleri:** İlk inşa sırasında istersen kapakları boyasız bırak. Boyadıktan sonra bir tarifin gerektirdiği eşyaların, sıvıların ve devrenin hâlâ aynı giriş grubunun parçası olarak okunabildiğinden emin ol.

Bir tarif tek bir veriyolunun tutabileceğinden daha fazla eşya türü gerektiriyorsa buharlı Giriş Yolları ekle. Döngü başına birden çok sıvı veya büyük miktarlar da ek kapak gerektirebilir. Arayüz eklerken en az 25 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm ürünleri toplamak için GUI'nin boşaltma modunu "Hiçleme" olarak ayarla ve her eşya ve sıvı çıkışı için yer sağla. Sıvı boşaltma etkinse, bir Çıkış Kapağı eksik veya tıkalı olduğunda Tuzlu Su, Kral Suyu ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik dört blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Çerçeve Kutuları, Dişli Kutusu Kasaları ve Boru Muhafazaları hologramda gösterildiği gibi mi yerleştirilmiş? |
| Yapı kademesi uyuşmazlığı | Kasalar, Çerçeve Kutuları, Dişli Kutusu Kasaları ve Boru Muhafazaları aynı kademeden mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Giriş veya çıkış arayüzü eksik | En az bir tür tarif girişi ve bir tür çıkış takılı mı? Tarifin gerektirdiği hem eşya veriyolları hem de sıvı kapakları mevcut mu? |
| Buhar Kapağı eksik veya buharlı veriyolları takılamıyor | Tam olarak bir Buhar Kapağı var mı? Yanlışlıkla sıradan elektrikli makine eşya veriyolları mı kullanıldı? |
| Kapak ekledikten sonra yapı başarısız | En az 25 gerçek kasa kaldı mı? Herhangi bir Çerçeve Kutusu, Dişli Kutusu Kasası veya Boru Muhafazası kapakla mı değiştirildi? |
| Tozlar var ama tarif bulunamıyor | Giriş biçimleri, türleri ve oranları NEI ile eşleşiyor mu? Miktarlar yeterli ve devre yapılandırması doğru mu? Yanlışlıkla başka bir makinenin karıştırma tarifine mi bakıldı? |
| Dolu sıvı hücreleri işlenmiyor | Tek bloklu bir tarife mi bakıldı? Tarif haritasında hücresiz doğrudan sıvı girişlerini doğrula, sonra sıradan Girdi Kapakları sağla. |
| İki asit de var ama Kral Suyu işlenmiyor | Gerekli devre yapılandırması ayarlı mı? İki sıvı ayrı sıradan Girdi Kapaklarında mı? Çıkış alanı mevcut mu? Kapak renkleri girişleri ayırdı mı? |
| Külçe yerine alaşım tozu çıkıyor | Bu, toz karıştırma tarifinin normal çıktısıdır. Sonraki eritme düzenini NEI ile ayarla. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınç yapısı da MV veya daha yüksek kademe tarifleri işleyemez. |
| Yalnızca düşük paraleller | Her eşya ve sıvı girişinden yeterince var mı? Kapak kapasitesi veya çıkış alanı döngü başına miktarı sınırlıyor mu? GUI paralel sınırı çok düşük mü ayarlanmış? |
| Eşya çıkışları var ama sıvılar eksik | Sıradan bir Çıkış Kapağı takılı mı? Yanlış sıvıya mı kilitli? Sıvı boşaltma etkin mi? Borular ürünü zaten çekmiş olabilir mi? |
| Yetersiz çıkış alanı | Tüm eşya ve sıvı çıkışları için yer var mı? Çıkış Yolları veya Çıkış Kapakları tıkalı mı? Çekme ve filtre ayarları doğru mu? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişebiliyor mu? Borular kısıtlı mı veya buharı başka makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Veriyolunun yanındaki sandık eşya aktarmıyor | Buharlı veriyolları eşyaları otomatik olarak çekmez veya itmez. Etkin aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Çince Wiki: Buhar Karıştırıcısı](https://gtnh.huijiwiki.com/wiki/大型蒸汽搅拌机)