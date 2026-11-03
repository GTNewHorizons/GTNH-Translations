---
item_ids:
  - gregtech:gt.blockmachines:1126
quest_ids:
  - AAAAAAAAAAAAAAAAAAADAA==
navigation:
  title: Damıtma Kulesi
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1126
  position: -3001
---
# Damıtma Kulesi
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1126" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> (Damıtma Kulesi, kısaltması DK ve çoğu zaman "büyük damıtıcı" olarak anılır) HV kademesinde bir işleme multibloğudur. Bir sıvıyı NEI tarifinde listelenen tüm fraksiyonlara aynı anda ayırır. Tek bloklu Damıtıcı'nın doğrudan yükseltmesi olduğundan genellikle petrol, Odun Katranı, biyokütle ve birçok kimyasal sıvıyı işlemek için kullanılır.

Bir Damıtma Kulesi'nin gereken yüksekliği, tarifteki sıvı çıktı sayısına bağlıdır. Her sıvı çıktı kendi çıktı katmanını kaplar; bu yüzden inşa etmeden önce başka bir kulenin yüksekliğini kopyalamak yerine hedef tarifi kontrol et.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | HV; kontrolcü tarifi EV kademesi devreler gerektirir, bu yüzden genellikle önce bir Temiz Oda gerekir |
| Yapı boyutu | 3×3×3–12; alt katmanın üzeri içi boş, üst katmanın merkezi kapalı |
| Güç | Standart Enerji Kapakları; birden fazla kapak kullanılabilir, ancak Çok Amperli Enerji Kapakları ve Lazer Enerji Kapakları desteklenmez |
| Hız Aşırtma | Standart kusurlu hız aşırtma: her hız aşırtma 4× güç harcar ve süreyi yarıya indirir |
| İşleme bonusları | Maksimum paralel 1; ek hız veya güç bonusu yok |
| Bakım ve kirlilik | Bakım gerektirir, kirlilik üretmez ve Egzoz Çıkışı gerektirmez |

## Üretim ve İnşa

Kontrolcü ile Temiz Paslanmaz Çelik Makine Gövdesi'nin güncel tarifleri aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1126" />

<RecipesFor id="gregtech:gt.blockcasings4:1" />

Damıtma Kulesi'nin ayak izi sabit 3×3, yüksekliği ise değişkendir. Kontrolcüyü alt katmanda ön yüzün merkezine yerleştir ve giriş arayüzlerini o katmana koy. İkinci katmandan başlayarak her katman en az bir Çıkış Kapağı içermelidir. Her ara katmanın merkezini hava olarak bırak ve üst katmanın merkezini bir Temiz Paslanmaz Çelik Makine Gövdesi ile kapat.

Toplam yükseklik $$h$$ için yapıda en az $$7h-5$$ adet gerçek Temiz Paslanmaz Çelik Makine Gövdesi kalmalıdır. Kapaklar ve veriyolları bu minimuma sayılmaz.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> | 1, alt katmanda ön yüzün merkezinde |
| <ItemLink id="gregtech:gt.blockcasings4:1" showIcon="left" /> | En az 16–79 |
| Girdi Kapağı | En az 1, alt katmandaki herhangi bir kasa konumunda |
| Giriş Yolu | İsteğe bağlı, alt katmandaki herhangi bir kasa konumunda; tarif eşya girdisi gerektirdiğinde bir tane kur |
| Çıkış Yolu | İsteğe bağlı, alt katmandaki herhangi bir kasa konumunda; tarif eşya çıktısı ürettiğinde bir tane kur |
| Çıkış Kapağı | Alt katmanın üzerindeki her katmanda en az 1; toplamda en az 2–11 |
| Standart Enerji Kapağı | En az 1, uygun herhangi bir kasa konumunda |
| Bakım Kapağı | 1, uygun herhangi bir kasa konumunda |

Minimum 3 katmanlı yapı 2 çıktı katmanı ve en az 16 kasa gerektirir. Dört sıvı çıktılı yaygın bir tarif 5 katmanlı yapı, 4 çıktı katmanı ve en az 30 kasa gerektirir. Maksimum 12 katmanlı yapı 11 sıvı çıktıyı işleyebilir ve en az 79 kasa gerektirir.

Bir katman birden fazla Çıkış Kapağı içerebilir, ancak kapak eklemek kasa sayısını minimumun altına indiremez. Katman başına bir Çıkış Kapağı kullanmak genellikle yönlendirmesi en kolay düzendir. Bir katmandaki ek kapaklar yalnızca tampon veya o katmana atanan aynı sıvı için başka bir çıktı arayüzü ekler; makinenin başka bir çıktı işlemesini sağlamaz.

Yapıyı önizlemek ve inşaya yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Kanal ayarlarını açmak için havaya sağ tıkla, toplam öngörülen yüksekliği seçmek için `height` alt kanalını 3 ile 12 arasında ayarla, ardından projektörü kontrolcüye kullan.

## Yetenekler

Tek bloklu Damıtıcı normalde bir hedef fraksiyon seçmek için Programlanmış Devre kullanır; diğer fraksiyonlar aynı anda üretilmez. Damıtma Kulesi kendi Damıtma Kulesi tariflerini çalıştırır ve aynı girdi partisinden her sıvı çıktısını elde eder. Malzeme verimliliğini artırmasının ve karmaşık kimyasal işleme hatlarını basitleştirmesinin ana nedeni budur.

Yaygın kullanımlar şunlardır:

- **Petrol fraksiyonlama**: Ağır Yakıt, Hafif Yakıt, Nafta ve Rafineri Gazı gibi fraksiyonları aynı anda üretir; Dizel, Setan Takviyeli Dizel ve petrol kraking üretim hatlarını besler.
- **Odun kimyası**: Odun Katranı, Odun Sirkesi ve Odun Gazı'nı Benzen, Toluen, Fenol ve Metanol gibi yakıt ve kimyasal hammaddelere işler.
- **Biyokütle işleme**: Fermente Biyokütle gibi sıvılardan birden fazla yan ürün geri kazanır.
- **Kimyasal ayrıştırma**: Tariflerinde birden fazla faydalı çıktı bulunan seyreltilmiş asitleri, çatlak yakıtlarını ve diğer sıvıları işler.

Kesin girdiler, çıktılar, Programlanmış Devre, güç kullanımı ve süre için NEI'deki Damıtma Kulesi tarifini izle. Bazı tarifler eşya girdisi veya eşya yan ürünü içerir, bu yüzden yalnızca sıvı kapakları her zaman yeterli değildir.

## Kule Yüksekliği ve Katmanlı Çıktılar

Önce NEI tarifindeki **sıvı çıktı** sayısını, yani $$n$$ değerini say; eşya çıktıları kule yüksekliğini etkilemez. Gereken toplam yükseklik:

$$
h=\max(3,n+1)
$$

Minimum yükseklik her zaman 3'tür, bu yüzden yalnızca bir sıvı çıktısı olan bir tarif bile yine iki çıktı katmanı gerektirir. Bir yapı tarifin gerektirdiğinden daha yüksek olabilir; bu durumda üstteki fazla Çıkış Kapakları kullanılmadan kalır, ancak yapı gereken yükseklikten kısa olamaz.

NEI'deki sıvı çıktıları **soldan sağa, sonra aşağıdan yukarıya** oku. İlk sıvı çıktısı ikinci katmandaki Çıkış Kapağına, ikincisi üçüncü katmana gider ve bu şekilde devam eder. Örneğin dört sıvı çıktılı bir tarif ikinci ila beşinci katmanları kullanır ve dolayısıyla en az 5 katman yüksekliğinde bir kule gerektirir.

> [!WARNING]
> Çıkış Kapakları mevcut sıvılarına veya bağlı boru filtrelerine göre otomatik atanmaz. Yanlış katmanı bağlamak bir ürünü yanlış tanka veya boruya gönderir; bu da sıvıları karıştırabilir veya üretim hattını tıkayabilir. Tarif her değiştiğinde her katmanı NEI ile yeniden karşılaştır.

## Güç ve Verim

HV, kontrolcünün kullanılabilir hale geldiği kademedir, ancak Damıtma Kulesi HV gücüyle sınırlı değildir. Kullanılabilir gerilimi, takılı standart Enerji Kapakları belirler. Bunları daha yüksek kademeli kapaklarla değiştirmek makinenin daha yüksek gerilimli tarifleri işlemesine ve [hız aşırtma](../../tierskipping_overcloking_parallels/overclocking.md) yapmasına olanak tanır. Aynı kademeden iki standart Enerji Kapağı, normal multiblok kuralları altında [çift kapaklı kademe atlama](../../tierskipping_overcloking_parallels/tierskipping.md) da sağlayabilir.

Damıtma Kulesi Çok Amperli Enerji Kapaklarını ve Lazer Enerji Kapaklarını desteklemez ve paralel yeteneği yoktur. Her standart kusurlu hız aşırtma 4× güç harcar ve süreyi yarıya indirir. Makine 1 tick'e ulaştıktan sonra hız aşırtma yapmaya devam edebilir, ancak bu bir tarifin birden fazla kopyasını aynı anda işlemesini sağlamaz.

Her fraksiyonu aynı anda üretmek, Damıtma Kulesi tariflerinin bir özelliğidir; paralel bonusu değildir. Verimi değerlendirirken tek bloklu Damıtıcı'nın tek çıktılı tarifinden tahmin yürütmek yerine NEI'deki Damıtma Kulesi tarifinde gösterilen girdi miktarını, süreyi ve gücü kullan.

> [!WARNING]
> İşleme sırasında güç kaybı mevcut tarifi iptal eder ve yerleştirilen girdileri yok eder. Enerji Kapaklarını yükselttikten veya çift kapaklı kademe atlamayı kullandıktan sonra kabloların, transformatörlerin ve jeneratörlerin gerekli gücü sürekli sağlayabildiğinden emin ol.

## Otomasyon ve Çıktı Yönlendirme

Her çıktı katmanını ayrı bir sıvı borusuna ve tanka bağla. Damıtma Kulesi bir sonraki işlemine ancak ilgili tüm ürünler için çıktı alanı olduğunda başlar; bu yüzden düşük talepli bir yan ürünün tamponunu doldurmak tüm kuleyi durdurabilir.

| Yöntem | Dikkat edilecekler |
| --- | --- |
| Standart Çıkış Kapağı | Her katmanı ayrı bir tanka bağla; tank, aşağı akıştaki geçici duruşları tamponlamalı |
| ME Çıkış Kapağı | Her çıktı katmanı yine kendi kapağını gerektirir; ME kablolarının her yönden bağlanabilmesi için kapağa Tel Kesici ile sağ tıkla |
| Yok Etme Taşması | Yalnızca etkilenen ürün güvenle atılabiliyorsa etkinleştir; dolu bir aşağı akış hedefine giremeyen sıvı kalıcı olarak yok edilir |
| Paylaşılan kasalar veya kapaklar | Duvar paylaşımı malzeme tasarrufu sağlar, ancak paylaşılan Çıkış Kapakları o katmandaki çıktıları uyumlu değilse iki kulenin birbirini tıkamasına yol açabilir |

Tarif bir Programlanmış Devre veya başka bir eşya girdisi gerektiriyorsa alt katmana bir Giriş Yolu kur. Toz veya başka bir eşya çıktısı üretiyorsa ayrıca bir Çıkış Yolu kur. Otomasyonu bağladıktan sonra önce bir parti işle ve sürekli girdiyi etkinleştirmeden önce her katmanda gerçek ürünü ve hedef tankı doğrula.

## Sorun Giderme

| Belirti | Neye bakmalı |
| --- | --- |
| Yapı tamamlanmıyor | Toplam yükseklik 3–12; her ara katmanın merkezi hava; üst merkez kapalı; alt katmanın üzerindeki her katmanda bir Çıkış Kapağı var; en az $$7h-5$$ gerçek kasa kalıyor |
| Yetersiz çıktı alanı | Kule her sıvı çıktısı için yeterince yüksek; ilgili Çıkış Kapağı, boru veya tank dolu değil; tarifte eşya çıktısı varsa bir Çıkış Yolu kurulu |
| Girdiler ve güç var ama tarif yok | Girdi sıvısı, Programlanmış Devre ve diğer eşyalar NEI ile eşleşiyor; eşyalar bir Giriş Yolu'nda; Enerji Kapağı yeterli gerilim sağlıyor |
| Ürünler yanlış boruya giriyor | NEI'yi soldan sağa ve aşağıdan yukarıya yeniden oku, sonra ikinci katmandan yukarıya doğru Çıkış Kapaklarıyla karşılaştır |
| Kule uzatıldıktan sonra eski yüksekliğinde oluşuyor | Eski üst-merkez kapağı kaldırıldı; her yeni katmanda bir Çıkış Kapağı var; inşa sonrasında manuel yapı kontrolü çalıştırıldı |
| Makine başladıktan hemen sonra duruyor | Daha fazla test malzemesi koymadan önce mevcut gücü, kablo kaybını, enerji tamponlarını ve bakım durumunu kontrol et |

Genel multiblok kullanımı için [Multiblok Makineler](./multiblocks_index.md) sayfasına bak. IV'te Dangote Distillus kullanılabilir hale gelir; LuV'te Mega Damıtma Kulesi daha yüksek verim sağlayabilir.

## Kaynaklar

- [GTNH Wiki: Damıtma Kulesi](https://wiki.gtnewhorizons.com/wiki/Distillation_Tower)