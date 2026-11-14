---
item_ids:
  - gregtech:gt.blockmachines:1126
navigation:
  title: Damıtma Kulesi
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:1126
  position: 11
---

# Damıtma Kulesi

<GameScene interactive={true} wrap="square" align="right" width="320" height="300">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1126" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> (Damıtma Kulesi, kısaca DK ve çoğu zaman "büyük damıtıcı" olarak anılır) bir HV kademesi işleme multibloğudur. Bir sıvıyı, NEI tarifinde listelenen tüm fraksiyonlara aynı anda ayırır. Tek bloklu Damıtıcıya göre doğrudan bir yükseltme olduğundan, genellikle petrol, Ahşap Katranı, biyokütle ve birçok kimyasal sıvıyı işlemek için kullanılır.

Bir Damıtma Kulesinin gereken yüksekliği, tarifteki sıvı çıktısı sayısına bağlıdır. Her sıvı çıktısı kendi çıkış katmanını kaplar; bu yüzden inşa etmeden önce başka bir kulenin yüksekliğini kopyalamak yerine hedef tarifi kontrol et.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı kademe | HV; kontrolcü tarifi EV kademesi devreler gerektirir, bu yüzden genellikle önce bir Temiz Oda gerekir |
| Yapı boyutu | 3×3×3–12, alt katmanın üzerinde içi boş ve üst katmanın merkezinde kapaklı |
| Güç | Standart Enerji Kapakları; birden fazla kapak kullanılabilir, ancak Çok Amperli Enerji Kapakları ve Lazer Enerji Kapakları desteklenmez |
| Hız aşırtma | Standart kusurlu hız aşırtma: her hız aşırtma 4× güç kullanır ve süreyi yarıya indirir |
| İşleme bonusları | Maksimum paralel 1, ek hız veya güç bonusu yok |
| Bakım ve kirlilik | Bakım gerektirir, kirlilik üretmez ve Egzoz Çıkışı gerektirmez |

## Üretim ve İnşa

Kontrolcünün ve Temiz Paslanmaz Çelik Makine Gövdesinin güncel tarifleri aşağıda gösterilmiştir.

<RecipesFor id="gregtech:gt.blockmachines:1126" />

<RecipesFor id="gregtech:gt.blockcasings4:1" />

Damıtma Kulesinin sabit 3×3 taban alanı ve değişken bir yüksekliği vardır. Kontrolcüyü alt katmanın ön yüzünün merkezine yerleştir ve giriş arayüzlerini o katmana koy. İkinci katmandan başlayarak her katman en az bir Çıkış Kapağı içermelidir. Ara katmanların her birinin merkezini hava olarak bırak ve üst katmanın merkezini bir Temiz Paslanmaz Çelik Makine Gövdesiyle kapat.

Toplam yüksekliği $$h$$ olan bir yapıda en az $$7h-5$$ adet gerçek Temiz Paslanmaz Çelik Makine Gövdesi bulunmalıdır. Kapaklar ve veriyolları bu minimuma sayılmaz.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1126" showIcon="left" /> | 1, alt katmanın ön yüzünün merkezinde |
| <ItemLink id="gregtech:gt.blockcasings4:1" showIcon="left" /> | En az 16–79 |
| Girdi Kapağı | En az 1, alt katmandaki herhangi bir kasa konumunda |
| Giriş Yolu | İsteğe bağlı, alt katmandaki herhangi bir kasa konumunda; tarif eşya girdisi gerektirdiğinde bir tane yerleştir |
| Çıkış Yolu | İsteğe bağlı, alt katmandaki herhangi bir kasa konumunda; tarif eşya çıktısı ürettiğinde bir tane yerleştir |
| Çıkış Kapağı | Alt katmanın üzerindeki her katmanda en az 1, toplamda en az 2–11 |
| Standart Enerji Kapağı | En az 1, uygun herhangi bir kasa konumunda |
| Bakım Kapağı | 1, uygun herhangi bir kasa konumunda |

Minimum 3 katmanlı yapı 2 çıkış katmanı ve en az 16 kasa gerektirir. Dört sıvı çıktısı olan yaygın bir tarif 5 katmanlı bir yapı, 4 çıkış katmanı ve en az 30 kasa gerektirir. Maksimum 12 katmanlı yapı 11 sıvı çıktısını işleyebilir ve en az 79 kasa gerektirir.

Bir katman birden fazla Çıkış Kapağı içerebilir, ancak kapak eklemek kasa sayısını minimumun altına düşüremez. Katman başına bir Çıkış Kapağı kullanmak genellikle yönlendirmesi en kolay düzendir. Bir katmandaki ek kapaklar yalnızca tamponlama veya o katmana atanan aynı sıvı için başka bir çıkış arayüzü ekler; makinenin başka bir çıktıyı işlemesini sağlamaz.

Yapıyı önizlemek ve inşaata yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. Kanal ayarlarını açmak için havaya sağ tıkla, öngörülen toplam yüksekliği seçmek için `height` alt kanalını 3 ile 12 arasında ayarla, ardından projektörü kontrolcü üzerinde kullan.

## Yetenekler

Tek bloklu Damıtıcı normalde hedef fraksiyonlardan birini seçmek için bir Programlanmış Devre kullanır, diğer fraksiyonlar aynı anda üretilmez. Damıtma Kulesi kendi Damıtma Kulesi tariflerini çalıştırır ve aynı girdi yığınından her sıvı çıktısını elde eder. Malzeme verimliliğini artırmasının ve karmaşık kimyasal işleme hatlarını basitleştirmesinin ana nedeni budur.

Yaygın kullanımlar şunlardır:

- **Petrol fraksiyonlama**: Ağır Yakıt, Hafif Yakıt, Nafta ve Rafineri Gazı gibi fraksiyonları aynı anda üretir; Dizel, Setan Takviyeli Dizel ve petrol kraking üretim hatlarını besler.
- **Ahşap kimyası**: Ahşap Katranı, Ahşap Sirkesi ve Ahşap Gazını Benzen, Toluen, Fenol ve Metanol gibi yakıt ve kimyasal hammaddelere işler.
- **Biyokütle işleme**: Fermente Biyokütle gibi sıvılardan birden çok yan ürün geri kazanır.
- **Kimyasal Ayrıştırma**: Tariflerinde birden çok faydalı çıktı bulunan seyreltik asitleri, çatlak yakıtlarını ve diğer sıvıları işler.

Kesin girdiler, çıktılar, Programlanmış Devre, güç kullanımı ve süre için NEI'deki Damıtma Kulesi tarifini izle. Bazı tarifler eşya girdileri veya eşya yan ürünleri içerir; bu yüzden yalnızca sıvı kapakları her zaman yeterli değildir.

## Kule Yüksekliği ve Katmanlı Çıktılar

Önce NEI tarifindeki **sıvı çıktısı** sayısını $$n$$ olarak belirle; eşya çıktıları kulenin yüksekliğini etkilemez. Gereken toplam yükseklik:

$$
h=\max(3,n+1)
$$

Minimum yükseklik her zaman 3'tür, bu yüzden yalnızca tek sıvı çıktısı olan bir tarif bile iki çıkış katmanı gerektirir. Bir yapı tarifin gerektirdiğinden daha yüksek olabilir; bu durumda üstteki fazladan Çıkış Kapakları kullanılmadan kalır, ancak gereken yükseklikten kısa olamaz.

NEI'de sıvı çıktılarını **soldan sağa, sonra aşağıdan yukarıya** oku. İlk sıvı çıktısı ikinci katmandaki Çıkış Kapağına, ikincisi üçüncü katmana vb. gider. Örneğin dört sıvı çıktısı olan bir tarif ikinci ile beşinci katmanları kullanır ve bu yüzden en az 5 katman yüksekliğinde bir kule gerektirir.

> [!WARNING]
> Çıkış Kapakları, mevcut sıvılarına veya bağlı boru filtrelerine göre otomatik olarak atanmaz. Yanlış katmanı bağlamak bir ürünü yanlış tanka veya boruya gönderir; bu da sıvıları karıştırabilir ya da üretim hattını tıkayabilir. Tarif her değiştiğinde her katmanı NEI ile yeniden kontrol et.

## Güç ve İş Hacmi

HV, kontrolcünün erişilebilir hale geldiği kademedir, ancak Damıtma Kulesi HV gücüyle sınırlı değildir. Kullanılabilir gerilimi, takılı standart Enerji Kapakları belirler. Onları daha yüksek kademe kapaklarla değiştirmek, makinenin daha yüksek gerilimli tarifleri işlemesine ve [hız aşırtma](../../tierskipping_overcloking_parallels/overclocking.md) yapmasına olanak tanır. Aynı kademeden iki standart Enerji Kapağı da normal multiblok kuralları çerçevesinde [çift kapaklı kademe atlama](../../tierskipping_overcloking_parallels/tierskipping.md) sağlayabilir.

Damıtma Kulesi Çok Amperli Enerji Kapaklarını veya Lazer Enerji Kapaklarını desteklemez ve paralel yeteneği yoktur. Her standart kusurlu hız aşırtma 4× güç kullanır ve süreyi yarıya indirir. Makine 1 tick'e ulaştıktan sonra hız aşırtma yapmaya devam edebilir, ancak bu bir tarifi aynı anda birden çok kez işlemesini sağlamaz.

Her fraksiyonu aynı anda üretmek, Damıtma Kulesi tariflerinin bir özelliğidir, paralel bonusu değildir. İş hacmini değerlendirirken tek bloklu Damıtıcının bir çıktı tarifinden tahmin yürütmek yerine NEI'deki Damıtma Kulesi tarifinde gösterilen girdi miktarını, süreyi ve gücü kullan.

> [!WARNING]
> İşleme sırasında güç kaybetmek mevcut tarifi iptal eder ve yerleştirilen girdileri yok eder. Enerji Kapaklarını yükselttikten veya çift kapaklı kademe atlamayı kullandıktan sonra kabloların, transformatörlerin ve jeneratörlerin gereken gücü sürekli sağlayabildiğinden emin ol.

## Otomasyon ve Çıktı Yönlendirmesi

Her çıkış katmanını ayrı bir sıvı borusuna ve tanka bağla. Damıtma Kulesi bir sonraki işleme ancak ilgili tüm ürünler için çıkış alanı olduğunda başlar; bu yüzden düşük talepli bir yan ürünün tamponunu doldurmak tüm kuleyi durdurabilir.

| Yöntem | Dikkat edilecekler |
| --- | --- |
| Standart Çıkış Kapağı | Her katmanı ayrı bir tanka bağla; tank, aşağı akıştaki geçici duruşları tamponlamalı |
| ME Çıkış Kapağı | Her çıkış katmanı yine kendi kapağını gerektirir; ME kablolarının her yönden bağlanabilmesi için kapağa Tel Kesici ile sağ tıkla |
| Hiçlik Taşması | Yalnızca etkilenen ürün güvenle atılabiliyorsa etkinleştir; dolu bir aşağı akış hedefine giremeyen sıvı kalıcı olarak yok edilir |
| Paylaşılan kasalar veya kapaklar | Duvar paylaşımı malzemeden tasarruf sağlar, ancak paylaşılan Çıkış Kapakları o katmandaki çıktıları uyumlu değilse iki kulenin birbirini engellemesine yol açabilir |

Bir tarif Programlanmış Devre veya başka bir eşya girdisi gerektiriyorsa alt katmana bir Giriş Yolu yerleştir. Toz veya başka bir eşya çıktısı üretiyorsa ayrıca bir Çıkış Yolu yerleştir. Otomasyonu bağladıktan sonra önce tek bir parti işle ve sürekli girdiyi etkinleştirmeden önce her katmandaki gerçek ürünü ve hedef tankı doğrula.

## Sorun Giderme

| Belirti | Neye bakmalısın |
| --- | --- |
| Yapı tamamlanmamış | Toplam yükseklik 3–12 arasında; her ara merkez hava; üst merkez kapalı; alt katmanın üzerindeki her katmanda bir Çıkış Kapağı var; en az $$7h-5$$ gerçek kasa duruyor |
| Çıkış alanı yetersiz | Kule her sıvı çıktısı için yeterince yüksek; ilgili Çıkış Kapağı, boru veya tank dolu değil; tarifte eşya çıktısı olduğunda bir Çıkış Yolu takılı |
| Girdiler ve güç var ama tarif yok | Girdi sıvısı, Programlanmış Devre ve diğer eşyalar NEI ile eşleşiyor; eşyalar bir Giriş Yolunda; Enerji Kapağı yeterli gerilim sağlıyor |
| Ürünler yanlış boruya giriyor | NEI'yi soldan sağa ve aşağıdan yukarıya yeniden oku, sonra ikinci katmandan yukarıya doğru Çıkış Kapaklarıyla karşılaştır |
| Kule uzatıldıktan sonra hâlâ eski yüksekliğinde oluşuyor | Eski üst merkez kapağı kaldırıldı; her yeni katmanda bir Çıkış Kapağı var; inşaattan sonra manuel yapı kontrolü çalıştırıldı |
| Makine başladıktan hemen sonra duruyor | Daha fazla test malzemesi koymadan önce mevcut gücü, kablo kaybını, enerji tamponlarını ve bakım durumunu kontrol et |

Genel multiblok kullanımı için [Multiblok Makineler](../multiblocks_index.md) sayfasına bak. IV'te Dangote Distillus kullanılabilir hale gelir; LuV'de Mega Damıtma Kulesi daha yüksek iş hacmi sağlayabilir.

## Kaynaklar

- [GTNH Wiki: Damıtma Kulesi](https://wiki.gtnewhorizons.com/wiki/Distillation_Tower)