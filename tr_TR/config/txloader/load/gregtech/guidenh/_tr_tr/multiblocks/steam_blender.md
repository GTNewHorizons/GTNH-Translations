---
item_ids:
  - gregtech:gt.blockmachines:31084
quest_ids:
  - WEwrzX4ZRkSxJ3M6cBesfA
navigation:
  title: Buharlı Karıştırıcı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:31084
  position: -501
---
# Buharlı Karıştırıcı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={1} />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" />, Buhar Çağı'nda kullanılabilen bir multiblok Karıştırıcıdır. Malzemeleri partiler hâlinde karıştırmak için buhar kullanır ve aynı tarifin sekiz kopyasına kadar aynı anda işleyebilir. Bronz Tozu, Pirinç Tozu, Şamot Tozu ve diğer malzemeleri üretebilir; Tuzlu Su gibi uygun ürünleri yapmak için sıvıları doğrudan kabul edip çıktı verebilir.

Makine, aynı kontrolcüyü paylaşan temel bronz ve Yüksek Basınçlı çelik yapılara sahiptir. Buhar Çağı'nda erişilebilen uygun Karıştırıcı tariflerini çalıştırır. Yüksek Basınçlı yapıya yükseltmek verimi artırır, ancak maksimum tarif kademesini yükseltmez.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | Buhar; kontrolcü tarifi Tumbaga Halkaları, Tumbaga Rotorları, bir Tumbaga Çerçeve ve diğer malzemeleri gerektirir |
| Boyutlar | 5×5 ayak izi, dört blok yüksekliğinde; kontrolcü ikinci katmanın ön ortasında |
| Güç | Tam olarak bir Buhar Kapağı; Enerji Kapağı yok |
| Tarif aralığı | LV ve altında, sıvı hücresi gerektirmeyen ve 32 EU/t'yi aşmayan Karıştırıcı tarifleri |
| Eşya arayüzleri | Buhar Giriş ve Çıkış Yolları; sıradan elektrikli makine eşya yolları bunların yerini alamaz |
| Sıvı arayüzleri | Sıradan Girdi Kapakları tarif sıvılarını sağlar ve sıradan Çıkış Kapakları sıvı ürünleri toplar; güç için kullanılan Buhar Kapağından ayrıdır |
| Paralel sayısı | Aynı tarifin en fazla sekiz kopyası; Yüksek Basınçlı yapı bu sınırı artırmaz |
| İşlem süresi | Temel yapıda NEI'de gösterilen sürenin yaklaşık 1.6 katı, Yüksek Basınçlı yapıda yaklaşık 0.8 katı |
| Yükseltmeler ve hız aşırtma | Yüksek Basınçlı yapı hızı ve buhar tüketim oranını ikiye katlar; gerilim hız aşırtması yok |
| Bakım ve kirlilik | Bakım yok, kirlilik yok ve Egzoz Çıkışı gerekmez |

## Üretim ve İnşa

Kontrolcü, temel kasa ve Buhar Kapağının güncel tarifleri aşağıda gösterilmiştir. Diğer bileşenlerin tariflerini görmek için tablodaki eşyalara tıkla.

<RecipesFor id="gregtech:gt.blockmachines:31084" />

<RecipesFor id="gregtech:gt.blockcasings:10" />

<RecipesFor id="gregtech:gt.blockmachines:31040" />

### Yapı Malzemeleri

Aşağıdaki düzen, eşya ve sıvı tariflerini işlemek için bir Buhar Kapağı, bir Giriş Yolu, bir Çıkış Yolu, bir Girdi Kapağı ve bir Çıkış Kapağı kullanır. Temel yapı bronz bileşenler kullanırken Yüksek Basınçlı yapı bunların çelik karşılıklarını kullanır. **Bir makinedeki kasalar, Çerçeveler, Dişli Kutusu Kasaları ve Boru Muhafazaları aynı kademeden olmalıdır.**

| Bileşen | Temel yapı | Yüksek Basınçlı yapı | Miktar ve konum |
| --- | --- | --- | --- |
| Kasa | <ItemLink id="gregtech:gt.blockcasings:10" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:0" showIcon="left" /> | Yukarıda açıklanan düzende 35 adet; aşağıdaki kapaklar veya yollar ile değiştirilebilir, ancak en az 25 gerçek kasa kalmalıdır |
| Çerçeve | <ItemLink id="gregtech:gt.blockframes:300" showIcon="left" /> | <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | Dört adet: ikinci katmandaki merkezî Dişli Kutusu Kasasının önünde, arkasında, solunda ve sağında birer adet |
| Dişli Kutusu Kasası | <ItemLink id="gregtech:gt.blockcasings2:2" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:3" showIcon="left" /> | İki adet: ikinci ve dördüncü katmanların her birinin merkezinde birer adet |
| Boru Muhafazası | <ItemLink id="gregtech:gt.blockcasings2:12" showIcon="left" /> | <ItemLink id="gregtech:gt.blockcasings2:13" showIcon="left" /> | Bir adet, üçüncü katmanın merkezinde |
| Kontrolcü | <ItemLink id="gregtech:gt.blockmachines:31084" showIcon="left" /> | Aynı kontrolcü | Bir adet, ikinci katmanın ön ortasında |
| Buhar Kapağı | <ItemLink id="gregtech:gt.blockmachines:31040" showIcon="left" /> | Aynı kapak | Tam olarak bir adet, bir kasanın yerine |
| Giriş Yolu | <ItemLink id="gregtech:gt.blockmachines:31046" showIcon="left" /> | Aynı yol | Eşya girdileri için gerektiği kadar kur, bir kasanın yerine; Programlanmış Devre ayarını da sağlayabilir |
| Çıkış Yolu | <ItemLink id="gregtech:gt.blockmachines:31047" showIcon="left" /> | Aynı yol | Eşya çıktıları için gerektiği kadar kur, bir kasanın yerine |
| Girdi Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> | Aynı kapak | Sıvı girdileri için gerektiği kadar kur, bir kasanın yerine |
| Çıkış Kapağı | Örneğin, <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" /> | Aynı kapak | Sıvı çıktıları için gerektiği kadar kur, bir kasanın yerine |

Yeni yapıda kasa veya kapaklar için 40 konum vardır. Yukarıda listelenen beş arayüzü kurmak 35 kasa bırakır. Yalnızca toz karıştırmak için bir Buhar Kapağı, bir buhar Giriş Yolu ve bir buhar Çıkış Yolu yeterlidir; 37 kasa kalır. Yol veya kapak eklemek kasa sayısını buna göre azaltır, ancak en az 25 gerçek kasa kalmalıdır. Kapaklar ve yollar Çerçevelerin, Dişli Kutusu Kasalarının veya Boru Muhafazalarının yerini alamaz.

Yapı kontrolü en az bir tür tarif girdi arayüzü ve en az bir tür çıktı arayüzü gerektirir; her eşya ve sıvı arayüzünün kurulmasını gerektirmez. Gerçek işlem için tarifin tüm girdileri ve çıktıları için arayüz sağla. Birden fazla girdi sıvısı gerektiğinde tek bir sıradan Girdi Kapağı hepsini aynı anda tutamaz, bu yüzden uygun sayıda Girdi Kapağı sağla.

Yapıyı önizlemek ve inşa etmeye yardım almak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Ana kanal kademesi 1 temel yapıyı, kademe 2 ise Yüksek Basınçlı yapıyı seçer. Destekli inşadan sonra kapakları kur ve yapıyı kontrol et.

## Makine Kullanımları

### Tarif Haritası ve Sıvı Hücreleri

Buharlı Karıştırıcı **Multiblok Karıştırıcı tarif haritasını** kullanır; İngilizce NEI'de **Multiblock Mixer** olarak görünür. Sıvı hücreleri içeren tek bloklu Karıştırıcı tarifleri bu haritada genellikle ilgili sıvıları doğrudan kabul edip veren tariflere dönüşür. Programlanmış Devreler dâhil eşya gereksinimleri yine de karşılanmalıdır.

NEI'ye bakarken tarifin bu haritaya ait olduğunu doğrula, sonra eşya miktarlarını, sıvı türlerini ve miktarlarını, Programlanmış Devre ayarını, tarif kademesini ve tüm çıktıları kontrol et.

| Kullanım | Yaygın tarifler ve dikkat edilecekler |
| --- | --- |
| Alaşım tozlarını karıştırma | Bakır Tozu ve Kalay Tozu Bronz Tozu olur; Bakır Tozu ve Çinko Tozu Pirinç Tozu olur. Girdi oranlarını ve devre ayarını kontrol et; ürün külçe değil tozdur. |
| Şamot Tozu | Sonraki refrakter malzeme tarifleri için Tuğla Tozu ve Kil Tozu karıştırır |

> [!NOTE]
> Makine Buhar Çağı'nda kullanılabilir, ancak yalnızca LV'ye kadar olan tarifleri kabul eder. Bir alaşım tozunun, kimyasal karışımın veya başka bir malzemenin işlenip işlenemeyeceğini belirlemek için tarifin EU/t değerini kontrol et. Yüksek Basınçlı çelik yapı MV veya daha yüksek kademeli tarifleri etkinleştirmez.

### Programlanmış Devreler ve Bronz Tozu

Birçok Karıştırıcı tarifi bir <ItemLink id="gregtech:gt.integrated_circuit:1" showIcon="left" /> gerektirir. NEI'nin gerektirdiği ayarı buhar Giriş Yolu GUI'sinin devre yuvasına gir.

Mevcut yaygın Bronz Tozu tarifi, tarif başına **üç Bakır Tozu, bir Kalay Tozu ve 1'e ayarlanmış bir Programlanmış Devre** gerektirir ve **dört Bronz Tozu** üretir. Bakır Tozu ve Kalay Tozu'nu buhar Giriş Yoluna gönder, devre ayarını 1 yap ve Bronz Tozu'nu buhar Çıkış Yolu üzerinden topla.

Sekiz paralelde bir döngü 24 Bakır Tozu ve sekiz Kalay Tozu tüketir ve 32 Bronz Tozu üretir. Sürekli çalışma sırasında 3:1 girdi oranını koru, böylece Bakır Tozu tüm yuvaları doldurup Kalay Tozu'nun girişini engellemez.

Bronz Tozu için sonraki eritme işlemini NEI'yi kullanarak ayarla. Diğer alaşım tozları bir Elektrikli Yüksek Fırın veya başka makineler gerektirebilir.

### İlk Çalıştırma

1. Yapıyı kontrol et ve Buhar Kapağı ile gerekli eşya ve sıvı arayüzlerinin kurulu olduğunu doğrula.
2. Buhar borusunu Buhar Kapağına bağla ve her tarif sıvısını kendi sıradan Girdi Kapağına ver.
3. NEI'de sıvı hücresi olmayan tarifi, tüm girdi miktarlarını, Programlanmış Devre ayarını ve tarif kademesini kontrol et.
4. Devreyi ayarla, tüm eşya ve sıvı çıktıları için yer bırak, sonra az miktarda malzemeyle başla.
5. Buhar tamponunu, girdi oranlarını ve çıktıları gözlemle. Sürekli girdi beslemesini ve çıktı toplamayı doğruladıktan sonra paralel sayısını artır.

## Buhar Beslemesi ve Verim

Buharlı Karıştırıcı aynı anda **aynı tarifin** en fazla sekiz kopyasını işleyebilir. Bu, bir döngüde sekiz farklı tarif çalıştırabileceği veya bir döngünün yalnızca sekiz eşya tükettiği anlamına gelmez. Gerçek paralel sayısı ayrıca girdi oranlarına, eşya ve sıvı miktarlarına, çıktı alanına ve GUI'de ayarlanan paralel sınırına bağlıdır.

Temel yapı NEI'de gösterilen tarif süresinin yaklaşık 1.6 katı kadar sürer, Yüksek Basınçlı yapı ise yaklaşık 0.8 katı. Örneğin iki saniye olarak gösterilen Bronz Tozu tarifi temel yapıda yaklaşık 3.2 saniye, Yüksek Basınçlı yapıda ise 1.6 saniye sürer. Paralel sayısı, döngü süresini paralel sayısına bölmeden bir döngüde işlenen tarif sayısını artırır.

| Özellik | Temel yapı | Yüksek Basınçlı yapı |
| --- | --- | --- |
| Kabul edilen tarif kademeleri | LV ve altı | LV ve altı |
| Maksimum paralel sayısı | 8 | 8 |
| NEI'ye göre işlem süresi | Yaklaşık 1.6 katı | Yaklaşık 0.8 katı |
| Aynı tarif ve paralel sayısı için buhar tüketim oranı | 1× | 2× |
| Tarif başına toplam buhar tüketimi | Temel değer | Yaklaşık olarak temel yapıyla aynı |
| Tarif başına girdiler ve çıktılar | NEI tarifinde belirtildiği gibi | Temel yapıyla aynı |

Yüksek Basınçlı yükseltme hızı ve buhar tüketim oranını birlikte artırır. Esas olarak verimi artırır; tarif başına toplam buhar maliyeti temel yapıyla yaklaşık aynıdır. Gerçek süre ve buhar tüketimi ayrıca tick ve tam sayı yuvarlamasından etkilenir. Sürekli üretim sırasında eşya ve tarif sıvısı aktarım hızları da işlem hızıyla birlikte artmalıdır.

Buhar Kapağı 64.000 L buhar tamponlar, ancak bu yalnızca geçici açıkları kapatır ve sürekli kazan üretiminin yerini alamaz. Kazanları ve boruları **işlem sırasındaki buhar tüketim oranına** göre boyutlandır ve tarif sıvıları için ayrı hatlar kullan.

Çalışma sırasındaki buhar tüketim oranını kontrol etmek için Waila'yı kullan ve sürekli işlem sırasında tamponun düşmeye devam edip etmediğini izle. Bir değer L/t olarak gösteriliyorsa, normal 20 TPS'de L/s elde etmek için 20 ile çarp. Boru verimini karşılaştırırken aynı birimleri kullan. Buhar beslemesi yetersizse GUI'deki paralel sınırını düşür, sonra kazan üretimini artır veya boru hattını iyileştir.

> [!WARNING]
> İşlem sırasında buharın bitmesi mevcut işlemi iptal eder ve hâlihazırda tüketilen eşyalar ve tarif sıvıları geri verilmez. Yüksek Basınçlı yapıya yükseltmeden veya paralel sınırını artırmadan önce buhar üretimini ve boru verimini kontrol et.

## Yüksek Basınçlı Yapıya Yükseltme

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31084" tier={2} />
</GameScene>

Yüksek Basınçlı yapı aynı boyutları, kapak konumlarını ve kontrolcüyü korur. **Tüm** Bronz Kaplamalı Tuğlaları, Bronz Çerçeveleri, Bronz Dişli Kutusu Kasalarını ve Bronz Boru Muhafazalarını tabloda listelenen Sağlam Çelik Makine Kasaları, Çelik Çerçeveler, Çelik Dişli Kutusu Kasaları ve Çelik Boru Muhafazaları ile değiştir.

Yükseltmeden önce işlemi ve malzeme girişini durdur. Bileşenleri değiştirdikten sonra yapıyı yeniden kontrol et ve buharı, girdileri ve üretimi geri yüklemeden önce makinenin Yüksek Basınçlı kademeyi gösterdiğini doğrula.

Yüksek Basınç makinenin yapı kademesidir. Hâlâ sıradan buhar kullanır ve mevcut Buhar Kapağı, buhar yolları ve sıradan Girdi ve Çıkış Kapakları yeniden kullanılabilir. Yükseltme hızı ve buhar tüketim oranını ikiye katlar, ancak maksimum sekiz paralel olarak kalır ve MV veya daha yüksek kademeli tarifler kullanılamaz durumda kalır.

## Otomasyon ve Çıktı Yönlendirmesi

Buhar Giriş ve Çıkış Yollarının her birinde dört eşya yuvası vardır ve Giriş Yolunda ek bir devre yuvası bulunur. Yanlarındaki sandıklardan otomatik olarak eşya çekmez veya ürünleri onlara itmez; bir yolun yanına sandık koymak otomasyon için yeterli değildir.

- **Eşya girişi:** Malzemeleri Giriş Yolunun ön yüzüne göndermek için Huniler, GT eşya boruları, konveyörler veya eşya kanalları kullan. Doğru tarif oranlarını sağla ve her toz türü için yuva ayır.
- **Eşya çıktısı:** Borular, kanallar veya konveyörlerle Çıkış Yolunun ön yüzünden aktif olarak çek ve ürünleri malzeme depolamasına veya bir sonraki işlem makinesine yönlendir.
- **Sıvı girişi:** Her sıvı türü için ayrı hatlar ve Girdi Kapakları kullan; filtreleri, sıvı kilitlerini ve miktarları kontrol et. Buhar besleme hattını Buhar Kapağına bağla.
- **Sıvı çıktısı:** Ürünleri Çıkış Kapağından çek veya otomatik çıktı için ön yüzüne bir Tank yerleştir.
- **Programlanmış Devre:** Bir malzeme üretirken gerekli ayarı koru. Tarifleri değiştirmeden önce girdiyi durdur ve mevcut işlemin bitmesini bekle, sonra kalan eşyaları ve sıvıları halledip devreyi ayarla.
- **Kapak renkleri:** İlk inşa sırasında istersen kapakları boyasız bırak. Boyadıktan sonra bir tarifin gerektirdiği eşyaların, sıvıların ve devrenin hâlâ aynı girdi grubunun parçası olarak okunabildiğinden emin ol.

Bir tarif bir yolun tutabileceğinden daha fazla eşya türü gerektiriyorsa buhar Giriş Yolları ekle. Birden fazla sıvı veya döngü başına büyük miktarlar da ek kapaklar gerektirebilir. Arayüz eklerken en az 25 gerçek kasa bırak ve ikinci bir Buhar Kapağı kurma.

> [!WARNING]
> Tüm ürünleri toplamak için GUI'nin imha modunu "İmha Etme" olarak ayarla ve her eşya ve sıvı çıktısı için yer sağla. Sıvı imhası etkinse, bir Çıkış Kapağı eksik veya tıkalı olduğunda Tuzlu Su, Kral Suyu ve diğer ürünler atılabilir.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Eksik yapı | Ayak izi 5×5 ve yükseklik dört blok mu? Kontrolcü ikinci katmanın ön ortasında mı? Çerçeveler, Dişli Kutusu Kasaları ve Boru Muhafazaları hologramda gösterildiği gibi mi konumlanmış? |
| Yapı kademesi uyuşmazlığı | Kasalar, Çerçeveler, Dişli Kutusu Kasaları ve Boru Muhafazaları aynı kademeden mi? Bronz bileşenlerin yalnızca bir kısmı mı değiştirildi? |
| Girdi veya çıktı arayüzü eksik | En az bir tür tarif girdisi ve bir tür çıktı kurulu mu? Tarifin gerektirdiği eşya yolları ve sıvı kapaklarının ikisi de var mı? |
| Buhar Kapağı eksik veya buhar yolları kurulamıyor | Tam olarak bir Buhar Kapağı var mı? Yanlışlıkla sıradan elektrikli makine eşya yolları mı kullanıldı? |
| Kapak ekledikten sonra yapı geçersiz | En az 25 gerçek kasa kaldı mı? Çerçeveler, Dişli Kutusu Kasaları veya Boru Muhafazalarından herhangi biri kapaklarla değiştirildi mi? |
| Tozlar var ama tarif bulunamıyor | Girdi biçimleri, türleri ve oranları NEI ile eşleşiyor mu? Miktarlar yeterli ve devre ayarı doğru mu? Yanlışlıkla başka bir makinenin karıştırma tarifine mi bakıldı? |
| Dolu sıvı hücreleri işlenmiyor | Tek bloklu bir tarife mi bakıldı? Tarif haritasında hücresiz doğrudan sıvı girdilerini doğrula, sonra sıradan Girdi Kapakları sağla. |
| İki asit de var ama Kral Suyu oluşmuyor | Gerekli devre ayarı yapıldı mı? İki sıvı ayrı sıradan Girdi Kapaklarında mı? Çıktı alanı var mı? Kapak renkleri girdileri birbirinden ayırmış olabilir mi? |
| Külçe yerine alaşım tozu çıkıyor | Bu, toz karıştırma tarifinin normal çıktısıdır. Sonraki eritme işlemini NEI'yi kullanarak ayarla. |
| Tarif kademesi çok yüksek | NEI'de gösterilen tarif LV'yi aşıyor mu? Yüksek Basınçlı yapı da MV veya daha yüksek kademeli tarifleri işleyemez. |
| Paralel sayısı düşük kalıyor | Her eşya ve sıvı girdisinden yeterince var mı? Kapak kapasitesi veya çıktı alanı döngü başına miktarı sınırlıyor mu? GUI paralel sınırı çok düşük mü ayarlanmış? |
| Eşya çıktıları var ama sıvılar eksik | Sıradan bir Çıkış Kapağı kurulu mu? Yanlış sıvıya mı kilitlenmiş? Sıvı imhası etkin mi? Borular ürünü çoktan çekmiş olabilir mi? |
| Çıktı alanı yetersiz | Tüm eşya ve sıvı çıktıları için yer var mı? Çıkış Yolları veya Çıkış Kapakları tıkalı mı? Çekme ve filtre ayarları doğru mu? |
| Kapakta buhar olmasına rağmen makine duruyor | Sürekli besleme yetişiyor mu? Borular kısıtlı mı veya diğer makinelerle buhar paylaşıyor mu? Mevcut paralel sayısı ve Yüksek Basınçlı kademe kazan kapasitesini aşıyor mu? |
| Yolun yanındaki sandık eşya aktarmıyor | Buhar yolları eşyaları otomatik olarak çekmez veya itmez. Aktif aktarım ekipmanını, bağlantı yüzünü, yönü ve filtreleri kontrol et. |

Genel yapı kontrolleri ve araç kullanımı için [Multiblok Makineleri](./multiblocks_index.md) sayfasına bak.

## İlgili Sayfalar

- [GTNH Wiki: Buharlı Karıştırıcı](https://wiki.gtnewhorizons.com/wiki/Steam_Blender)