---
item_ids:
  - gregtech:gt.blockmachines:31084
navigation:
  title: Buharlı Karıştırıcı
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:31084
  position: 7
quest_ids:
  - WEwrzX4ZRkSxJ3M6cBesfA
---

# Buharlı Karıştırıcı

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" />, Buhar çağında kullanılabilen bir Karıştırıcıdır ve Multibloklar arasında yer alır. Malzemeleri partiler hâlinde karıştırmak için buhar kullanır ve aynı tarifin aynı anda en fazla sekiz kopyasını işleyebilir. Bronz Tozu, Pirinç Tozu, Ateş Kili Tozu ve diğer malzemeleri üretebilir; Tuzlu Su gibi uygun ürünler için sıvıları doğrudan alıp çıktı olarak verebilir.

Makinenin, aynı kontrolcüyü paylaşan temel bronz ve yüksek basınçlı çelik yapıları vardır. Buhar çağında kullanılabilen uygun Karıştırıcı tariflerini etkinleştirir. Yüksek basınçlı yapıya yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılım kademesi | Buhar; kontrolcü tarifi Tumbaga Halkaları, Tumbaga Rotorları, bir Tumbaga Çerçevesi ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 taban alanı, dört blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV ve altındaki, sıvı hücresi gerektirmeyen ve en fazla 32 EU/t gerektiren Karıştırıcı tarifleri |
| Eşya arayüzleri | Buhar Giriş ve Çıkış Yolları; sıradan elektrikli makine eşya yolları bunların yerini alamaz |
| Sıvı arayüzleri | Sıradan Girdi Kapakları tarif sıvılarını sağlar ve sıradan Çıkış Kapakları sıvı ürünleri toplar; güç için kullanılan Buhar Kapağından ayrıdır |
| Paralel işlemler | Aynı tarifin en fazla sekiz kopyası; yüksek basınçlı yapı bu sınırı yükseltmez |
| İşlem süresi | Temel yapı için NEI'de gösterilen sürenin yaklaşık 1,6 katı, yüksek basınçlı yapı için 0,8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek basınçlı yapı hızı ve buhar tüketim hızını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağı için güncel tarifler aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31084" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki düzen, eşya ve sıvı tariflerini işlemek için bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu, bir Girdi Kapağı ve bir Çıkış Kapağı kullanır. Temel yapı bronz bileşenler kullanırken yüksek basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, çerçeveler, dişli kutusu kasaları ve boru muhafazaları tamamen aynı kademede olmalıdır.**

| Bileşen | Temel yapı | Yüksek basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzende 35 adet; aşağıdaki kapaklar veya yollar ile değiştirilebilir, ancak en az 25 gerçek kasa kalmalıdır |
| Çerçeve | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Dört adet: ikinci katmandaki merkezî dişli kutusu kasasının önünde, arkasında, solunda ve sağında birer tane |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | İki adet: ikinci ve dördüncü katmanların her birinin merkezinde birer tane |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Bir adet, üçüncü katmanın merkezinde |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | Eşya girişleri için gerektiği kadar tak, bir kasanın yerine; Programlanmış Devre ayarını da sağlayabilir |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | Eşya çıkışları için gerektiği kadar tak, bir kasanın yerine |
| Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | Sıvı girişleri için gerektiği kadar tak, bir kasanın yerine |
| Çıkış Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıkışları için gerektiği kadar tak, bir kasanın yerine |

Yeni yapıda kasa veya kapaklar için 40 konum bulunur. Yukarıda listelenen beş arayüzü takmak 35 kasa bırakır (Yaprakları: 35). Yalnızca toz karıştırmak için bir Buhar Kapağı, bir Buhar Giriş Yolu ve bir Buhar Çıkış Yolu yeterlidir; bu durumda 37 kasa kalır. Yol veya kapak eklemek kasa sayısını buna göre azaltır, ancak en az 25 gerçek kasa kalmalıdır. Kapaklar ve yollar Çerçevelerin, Dişli Kutusu Kasalarının veya Boru Muhafazalarının yerini alamaz.

Yapı denetimi en az bir tür tarif giriş arayüzü ve en az bir tür çıkış arayüzü gerektirir; eşya ve sıvı arayüzlerinin hepsinin takılı olmasını gerektirmez. Gerçek işleme için tüm tarif girişleri ve çıkışları için arayüz sağla. Birden fazla giriş sıvısı gerektiğinde tek bir sıradan Girdi Kapağı hepsini aynı anda tutamaz, bu yüzden karşılık gelen sayıda Girdi Kapağı sağla.

Yapıyı önizlemek ve inşa etmeye yardım almak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise yüksek basınçlı yapıyı seçer. Destekli inşadan sonra kapakları tak ve yapıyı denetle.

## Makine Kullanımları

### Tarif Haritası ve Sıvı Hücreleri

Buharlı Karıştırıcı **Multiblok Karıştırıcı tarif haritasını** kullanır; İngilizce NEI'de **Multiblock Mixer** olarak görünür. Sıvı hücreleri içeren tek blok Karıştırıcı tarifleri genellikle bu haritada ilgili sıvıları doğrudan alıp veren tariflere dönüşür. Programlanmış Devreler dâhil eşya gereksinimleri yine de karşılanmalıdır.

NEI'yi kontrol ederken tarifin bu haritaya ait olduğunu doğrula, ardından eşya miktarlarını, sıvı türlerini ve miktarlarını, Programlanmış Devre ayarını, tarif kademesini ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Alaşım tozlarını karıştırma | Bakır Tozu ve Kalay Tozu Bronz Tozu olur; Bakır Tozu ve Çinko Tozu Pirinç Tozu olur. Giriş oranlarını ve devre ayarını kontrol et; ürün tozdur, külçe değil. |
| Ateş Kili Tozu | Sonraki refrakter malzeme tarifleri için Tuğla Tozu ve Kil Tozu karıştırır |

> [!NOTE]
> Makine Buhar çağında kullanılabilir, ancak yalnızca LV'ye kadar tarifleri kabul eder. Bir alaşım tozunun, kimyasal karışımın veya başka bir malzemenin işlenip işlenemeyeceğini belirlemek için tarifin EU/t değerini kontrol et. Yüksek basınçlı çelik yapı MV veya daha yüksek kademedeki tarifleri etkinleştirmez.

### Programlanmış Devreler ve Bronz Tozu

Birçok Karıştırıcı tarifi bir <ItemLink id="gregtech:gt.integrated_circuit:1" showIcon="left" /> gerektirir. NEI'nin gerektirdiği ayarı Buhar Giriş Yolu arayüzünün devre yuvasına gir.

Güncel yaygın Bronz Tozu tarifi, tarif başına **üç Bakır Tozu, bir Kalay Tozu ve 1'e ayarlanmış bir Programlanmış Devre** gerektirir ve **dört Bronz Tozu** üretir. Bakır Tozu ve Kalay Tozunu Buhar Giriş Yoluna gönder, devre ayarını 1 yap ve Bronz Tozunu Buhar Çıkış Yolu üzerinden topla.

Sekiz paralelde bir döngü 24 Bakır Tozu ve sekiz Kalay Tozu tüketir ve 32 Bronz Tozu üretir. Sürekli çalışma sırasında 3:1 giriş oranını koru; böylece Bakır Tozu her yuvayı doldurup Kalay Tozunun girişini engellemez.

Bronz Tozu için sonraki eritme işlemlerini NEI'yi kullanarak ayarla. Diğer alaşım tozları bir Elektrikli Yüksek Fırın veya başka makineler gerektirebilir.

### İlk Çalıştırma

1. Yapıyı denetle ve Buhar Kapağının ve gerekli eşya ve sıvı arayüzlerinin takılı olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve her tarif sıvısını kendi sıradan Girdi Kapağına ver.
3. NEI'de sıvı hücresi içermeyen tarifi, tüm giriş miktarlarını, Programlanmış Devre ayarını ve tarif kademesini kontrol et.
4. Devreyi ayarla, tüm eşya ve sıvı çıkışları için yer bırak, sonra az miktarda malzemeyle başla.
5. Buhar tamponunu, giriş oranlarını ve çıktıları gözle. Sürekli giriş beslemesini ve çıkış toplamayı doğruladıktan sonra paralel sayısını artır.

## Buhar Beslemesi ve Verim

Buharlı Karıştırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı tarif çalıştırabileceği veya bir döngünün yalnızca sekiz eşya tükettiği anlamına gelmez. Gerçek paralel sayısı ayrıca giriş oranlarına, eşya ve sıvı miktarlarına, çıkış alanına ve arayüzde ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1,6 katını alırken yüksek basınçlı yapı yaklaşık 0,8 katını alır. Örneğin iki saniye olarak gösterilen Bronz Tozu tarifi temel yapıda yaklaşık 3,2 saniye, yüksek basınçlı yapıda 1,6 saniye sürer. Paralellik, bir döngüde işlenen tarif sayısını artırır ancak döngü süresini paralel sayısına bölmez.

| Özellik | Temel yapı | Yüksek basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1,6× | Yaklaşık 0,8× |
| Aynı tarif ve paralel sayısı için buhar tüketim hızı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel değer | Temel yapıyla yaklaşık aynı |
| Tarif başına girişler ve çıkışlar | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Yüksek basınç yükseltmesi hızı ve buhar tüketim hızını birlikte artırır. Esas olarak verimi iyileştirir ve tarif başına toplam buhar maliyeti temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi tick ve tam sayı yuvarlamasından da etkilenir. Sürekli üretim sırasında eşya ve tarif sıvısı aktarım hızları da işlem hızıyla birlikte artmalıdır.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici eksiklikleri karşılar ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim hızına** göre boyutlandır ve tarif sıvıları için ayrı hatlar kullan.

Waila kullanarak çalışma sırasındaki buhar tüketim hızını kontrol et ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse arayüzdeki paralel sınırını düşür, sonra kazan üretimini artır veya boru hattını iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen eşyalar ve tarif sıvıları geri verilmez. Yüksek basınca yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınca Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={2} />
</GameScene>

Yüksek basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Çerçeveleri, Bronz Dişli Kutusu Kasalarını ve Bronz Boru Muhafazalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Çerçeveler, Çelik Dişli Kutusu Kasaları ve Çelik Boru Muhafazaları ile değiştir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden denetle ve buharı, girişleri ve üretimi geri yüklemeden önce makinenin yüksek basınç kademesini gösterdiğini doğrula.

Yüksek basınç makinenin yapı kademesidir. Makine yine sıradan buhar kullanır ve mevcut Buhar Kapağı, buhar yolları ile sıradan Girdi ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim hızını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek kademedeki tarifler kullanılamaz durumda kalır.

## Otomasyon ve Çıkış Yönlendirme

Buhar Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır ve Giriş Yolunda ek bir devre yuvası bulunur. Komşu Sandıklardan otomatik olarak çekmez veya ürünleri onlara itmez; bir Sandığı yolun yanına koymak otomasyon için yeterli değildir.

- **Eşya girişi:** Malzemeleri Giriş Yolunun ön yüzüne göndermek için huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Doğru tarif oranlarını sağla ve her toz türü için yuva ayır.
- **Eşya çıkışı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek ve ürünleri malzeme deposuna veya sonraki işleme makinesine yönlendir.
- **Sıvı girişi:** Her sıvı türü için ayrı hatlar ve Girdi Kapakları kullan; Filtreleri, sıvı kilitlerini ve miktarları kontrol et. Buhar besleme hattını Buhar Kapağına bağla.
- **Sıvı çıkışı:** Ürünleri Çıkış Kapağından çek veya otomatik çıkış için ön yüzüne bir Tank yerleştir.
- **Programlanmış Devre:** Bir malzeme üretirken gerekli ayarı koru. Tarifleri değiştirmeden önce girişi durdur ve mevcut işlemin bitmesini bekle, sonra kalan eşyaları ve sıvıları halledip devreyi ayarla.
- **Kapak renkleri:** İlk inşa sırasında kapakları istersen boyasız bırak. Boyadıktan sonra bir tarifin gerektirdiği eşyaların, sıvıların ve devrenin hâlâ aynı giriş grubunun parçası olarak okunabildiğinden emin ol.

Bir tarif bir yolun tutabileceğinden daha fazla eşya türü gerektiriyorsa Buhar Giriş Yolları ekle. Birden fazla sıvı veya döngü başına büyük miktarlar da ek kapaklar gerektirebilir. Arayüz eklerken en az 25 gerçek kasa bırak ve ikinci bir Buhar Kapağı takma.

> [!WARNING]
> Tüm ürünleri toplamak için arayüzün imha modunu "Do Not Void" olarak ayarla ve her eşya ve sıvı çıkışı için yer sağla. Sıvı imhası etkinse bir Çıkış Kapağı eksik veya tıkalı olduğunda Tuzlu Su, Kral Suyu ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Eksik yapı | Taban alanı 5×5 ve yükseklik dört blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Çerçeveler, Dişli Kutusu Kasaları ve Boru Muhafazaları hologramda gösterildiği gibi mi yerleştirilmiş? |
| Yapı kademesi uyuşmuyor | Kasalar, Çerçeveler, Dişli Kutusu Kasaları ve Boru Muhafazaları hepsi aynı kademede mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Giriş veya çıkış arayüzü eksik | En az bir tür tarif girişi ve bir tür çıkış takılı mı? Tarifin gerektirdiği eşya yolları ve sıvı kapaklarının ikisi de mevcut mu? |
| Buhar Kapağı eksik veya buhar yolları takılamıyor | Tam olarak bir Buhar Kapağı var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapak ekledikten sonra yapı doğrulanmıyor | En az 25 gerçek kasa kaldı mı? Herhangi bir Çerçeve, Dişli Kutusu Kasası veya Boru Muhafazası kapakla değiştirildi mi? |
| Tozlar var ama tarif bulunamıyor | Giriş biçimleri, türleri ve oranları NEI ile eşleşiyor mu? Miktarlar yeterli ve devre ayarı doğru mu? Yanlışlıkla başka bir makinenin karıştırma tarifine mi bakıldı? |
| Dolu sıvı hücreleri işlenmiyor | Tek blok bir tarif mi kontrol edildi? Tarif haritasında hücresiz doğrudan sıvı girişlerini doğrula, sonra sıradan Girdi Kapaklarına besle. |
| İki asit de mevcut ama Kral Suyu işlenmiyor | Gerekli devre ayarı yapıldı mı? İki sıvı ayrı sıradan Girdi Kapaklarında mı? Çıkış alanı mevcut mu? Kapak renkleri girişleri ayırdı mı? |
| Külçe yerine alaşım tozu çıkıyor | Bu, toz karıştırma tarifinin normal çıktısıdır. Sonraki eritmeyi NEI'yi kullanarak ayarla. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek basınçlı yapı da MV veya daha yüksek kademedeki tarifleri işleyemez. |
| Sadece düşük paralel sayısı | Her eşya ve sıvı girişinden yeterince var mı? Kapak kapasitesi veya çıkış alanı döngü başına miktarı sınırlıyor mu? Arayüzdeki paralel sınırı çok düşük mü ayarlanmış? |
| Eşya çıktıları var ama sıvılar eksik | Sıradan bir Çıkış Kapağı takılı mı? Yanlış sıvıya mı kilitlenmiş? Sıvı imhası etkin mi? Borular ürünü çoktan çekmiş olabilir mi? |
| Çıkış alanı yetersiz | Tüm eşya ve sıvı çıkışları için yer var mı? Çıkış Yolları veya Çıkış Kapakları tıkalı mı? Çekme ve filtre ayarları doğru mu? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya buharı başka makinelerle mi paylaşıyor? Mevcut paralel sayısı ve yüksek basınç kademesi kazan kapasitesini aşıyor mu? |
| Yolun yanındaki Sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Etkin aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı denetimleri ve araç kullanımı için [Multibloklar Makineleri](../multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Steam Blender](https://wiki.gtnewhorizons.com/wiki/Steam_Blender)