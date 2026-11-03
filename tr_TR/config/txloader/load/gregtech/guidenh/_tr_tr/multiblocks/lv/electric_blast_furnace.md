---
item_ids:
  - gregtech:gt.blockmachines:1000
navigation:
  title: Elektrikli Yüksek Fırın
  parent: ../multiblocks_index.md
  icon: gregtech:gt.blockmachines:1000
  position: 5
quest_ids:
  - AAAAAAAAAAAAAAAAAAAATQ
---

# Elektrikli Yüksek Fırın

<GameScene interactive={true} wrap="square" align="right" width="320" height="280">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1000" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> (Electric Blast Furnace, kısaca EYF), LV'de kullanılabilen bir işleme multiblogudur. Elektrik ve Isıtma Bobinleri, onun Tuğlalı Yüksek Fırının ulaşamadığı sıcaklıklara ulaşmasını sağlar. İlk büyük kullanımı genellikle alüminyum üretimidir; daha sonra yüksek sıcaklıkta işleme gerektiren birçok metali ve diğer malzemeyi işler.

EYF genellikle yeni bir oyuncunun ilk **GT elektrikli multiblogudur** ve MV malzemelerine doğru önemli bir adımdır. Onu inşa etmek; yapı gereksinimlerini, eşya ve sıvı arayüzlerini, bakımı ve sürekli gücü bir araya getirir. İlk EYF'ini güvenilir şekilde çalıştırma deneyimi sonraki birçok multibloğa aktarılır.

Kontrolcüyü elde ettiğin kademe, tariflerinin gerektirdiği güçten ayrıdır. İlk Enerji Kapakların LV olsa da yaygın alüminyum tarifleri MV gücü gerektirir. İki LV Enerji Kapağı ve yeterli bir güç kaynağı, erken bir EYF'in bu tarifleri çalıştırmasını sağlar.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı kademe | LV; iki LV Enerji Kapağı genellikle erken MV tarifleri için gücü sağlar |
| Yapı boyutu | 3×3×4; ortadaki iki katmanın her birinin merkezi havadır |
| Güç | Birden fazla normal Enerji Kapağını destekler; Çok Amperli Enerji Kapaklarını veya Lazer Hedef Kapaklarını desteklemez |
| Hız Aşırtma ve paralel | Normalde normal hız aşırtma kullanır; yeterli fazla ısı bunların bir kısmını kusursuz hız aşırtmaya dönüştürür; ek paralel bonusu yok |
| İşleme bonusları | Tarif gereksiniminin her 900 K üzeri güç kullanımını %95 ile çarpar; her 1800 K bir kusursuz hız aşırtmaya izin verir |
| Bakım ve kirlilik | Bakım ve bir Egzoz Çıkışı gerektirir; temel kirlilik 400 gibbl/s olup gerçek emisyonlar Egzoz Çıkışı kademesiyle azalır |

İlk inşaat için **Kupronikel Bobinler, iki LV Enerji Kapağı, kısa kablolar ve küçük bir parti alüminyum bileşeni** ile başla. Yapıyı oluşturmak yalnızca ilk adımdır: işlemin başarıyla tamamlanabilmesi için tarif, sıcaklık, çıkış alanı ve sürekli güç kaynağının hepsi uygun olmalıdır.

## Üretim ve İnşaat

### Kontrolcüyü ve Arayüzleri Anlamak

Kontrolcü makine durumunu gösterir, yapıyı doğrular ve denetimler sunar. Eşyalar, sıvılar ve güç aşağıdaki bileşenlerden girer. Veriyolları ve kapaklar ancak geçerli yapı konumlarına takıldığında EYF'in parçası olur.

| Bileşen | Amaç |
| --- | --- |
| Giriş Yolu | Tozlar ve Programlanmış Devreler gibi eşya bileşenlerini barındırır |
| Çıkış Yolu | Külçeler ve sıcak külçeler gibi eşya ürünlerini alır |
| Girdi Kapağı | Tarifin gerektirdiği sıvıları, örneğin azotu sağlar |
| Çıkış Kapağı | Tarifte listelenen sıvı ürünleri alır |
| Enerji Kapağı | Dış güç ağından EU alır ve multibloğu besler |
| Bakım Kapağı | Aletlerle bakım sorunlarını onarmaya izin verir |
| Egzoz Çıkışı | Kirliliği dışarı verir; havalandırma yüzü açık kalmalıdır |

Giriş Yolu ile Girdi Kapağı farklı amaçlara hizmet eder. Tozu kontrolcünün yuvasına koymak veya bir Giriş Yoluna sıvı borusu bağlamak, gereken arayüzlerin yerini tutmaz.

### Bileşenleri Hazırlamak

Kontrolcü ve Isı Geçirmez Makine Gövdelerinin güncel tarifleri aşağıda gösterilmiştir. Isıtma Bobinleri birkaç kademede gelir; üretmeden önce malzemelerini ve tariflerini NEI'den kontrol et.

<RecipesFor id="gregtech:gt.blockmachines:1000" />

<RecipesFor id="gregtech:gt.blockcasings:11" />

<RecipesFor id="gregtech:gt.blockcasings5:0" />

Alt katman kontrolcüyü ve arayüzlerin çoğunu barındırır. Ortadaki iki katmanın her biri, merkezi hava olacak şekilde aynı kademeden sekiz Isıtma Bobininden oluşan bir halkadır. Üst merkezde Egzoz Çıkışı bulunmalıdır. Kalan alt ve üst halka konumlarını Isı Geçirmez Makine Gövdeleriyle veya o konumlarda izin verilen arayüzlerle doldur.

| Bileşen | Miktar ve konum |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> | Bir adet, alt katmanın ön merkezinde |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> veya diğer Isıtma Bobinleri | On altı adet, ortadaki iki katmanda; hepsi aynı kademede olmalı |
| <ItemLink id="gregtech:gt.blockcasings:11" showIcon="left" /> | 0–12, alt katmandaki ve üst halkadaki kullanılmayan konumları doldurur |
| Normal Enerji Kapağı | En az bir adet, alt katmanda; erken MV tarifleri için genellikle iki <ItemLink id="gregtech:gt.blockmachines:41" showIcon="left" /> kullanılır |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | Bir adet, alt katmanda |
| <ItemLink id="gregtech:gt.blockmachines:91" showIcon="left" /> | Bir adet, üst merkezde; havalandırma yüzünü engelleme |
| Giriş Yolu veya Girdi Kapağı | En az bir giriş arayüzü, alt katmanda; tarifin gerektirdiği eşya ve sıvı girişlerini sağla |
| Çıkış Yolu veya Çıkış Kapağı | En az bir çıkış arayüzü; Çıkış Yolları alt katmanda yer alır, Çıkış Kapakları üst halkada da bulunabilir |

En az bir giriş ve bir çıkış arayüzü gereklidir. Yalnızca iki LV Enerji Kapağı, bir Bakım Kapağı, bir Giriş Yolu ve bir Çıkış Yolu ile kalan konumlar için **11 Isı Geçirmez Makine Gövdesi** gerekir. Ek sıvı kapakları veya veriyolları izin verilen konumlarda kasaların yerini alabilir; bobinlerin veya Egzoz Çıkışının yerini alamazlar.

Aşağıdaki animasyon, gaz kullanan tarifler için bir <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> da içerir, bu yüzden **10 Isı Geçirmez Makine Gövdesi** kullanır. İlk tarifinde sıvı girişi yoksa başlangıçta orada bir kasa bırakıp daha sonra yerine Girdi Kapağı koyabilirsin.

### Katman Katman İnşa Etmek

İnşaat sırasını görmek için oynat'a bas veya bir adıma geri dönmek için zaman çizelgesini sürükle. Animasyon kontrolcüyle başlar, ardından alt katman arayüzlerini, iki bobin halkasını, üst katmanı ve yağmurdan koruma için bir çatı ekler.

<GameScene interactive={true} width="480" height="340">
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_build.json" />
</GameScene>

1. **Ön yönü seç ve kontrolcüyü yerleştir.** 3×3'lük bir taban ayır ve kontrolcüyü ön merkezine, dışa bakacak şekilde yerleştir. Bakım, eşya ve sıvı arayüzleri ile kablo bağlantıları için erişim bırak.
2. **Tabanı tamamla.** Alt katmandaki diğer sekiz konum Enerji Kapaklarını, bir Bakım Kapağını ve giriş/çıkış arayüzlerini kabul eder. Kullanılmayan konumları Isı Geçirmez Makine Gövdeleriyle doldur. Alt merkez de yapının parçasıdır ve boş bırakılmamalıdır.
3. **İlk bobin halkasını yerleştir.** Tabanın üstünde, merkezi hava kalacak şekilde sekiz Kupronikel Bobininden oluşan 3×3'lük bir halka inşa et.
4. **İkinci bobin halkasını yerleştir.** Aynı bobinlerden bir halka daha ekle, toplam on altı olsun. Tüm bobinler aynı kademede olmalı; Kupronikel ve Kantal katmanlarını karıştırma.
5. **Üstü bitir ve Egzoz Çıkışını tak.** Egzoz Çıkışını dördüncü katmanın merkezine, normalde yukarı doğru havalandıracak şekilde koy. Dıştaki sekiz konumu kasalarla doldur veya gerektiğinde sıvı Çıkış Kapaklarıyla değiştir.
6. **Yapıyı kontrol et.** Her iki orta katmanın merkez bloklarını meşalelerden, kablolardan, borulardan ve diğer bloklardan uzak tut. EYF oluşmazsa yapıyı kontrolcü arayüzünde yeniden kontrol et ve eksik veya yanlış yerleştirilmiş bileşenleri ara.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. `coil` alt kanalı bobin kademesini seçer. İnşaattan sonra yapıyı kontrolcüde kontrol et ve bakım sorunlarını Bakım Kapağında onar.

> [!WARNING]
> Enerji Kapaklarını, jeneratörleri ve Pil Tamponlarını yağmurdan koru. Egzoz Çıkışının havalandırmasının önünde en az bir hava bloğu bırak ve çatıyı daha yukarıda inşa et. Doğrudan yukarı bakan bir Egzoz Çıkışının üzerine çatı koyma veya havalandırmasını kablolarla ya da borularla kapatma.

Eski rehberler, egzoz gazlarını geri kazanmak için üst halkada gaz Çıkış Kapakları gerektirebilir. Bu özel egzoz geri kazanım sistemi güncel sürümde kaldırıldı. Bir tarif sıvı üretiyorsa NEI'de gösterilen çıktılar için Çıkış Kapakları sağla; alt katmandaki Çıkış Kapakları da gazları alabilir. Üst halka, Çıkış Kapakları için geçerli bir konum olmaya devam eder.

### Bakımı Tamamlamak

Yeni yerleştirilmiş bir EYF'te genellikle bakım sorunları vardır. Bakım Kapağını aç, ilgili GT aletini imlecinde tut ve sorunu onarmak için bakım düğmesine tıkla. Lehim Demiri ayrıca şarj ve lehim gerektirir. Ardından kontrolcüye dön ve her sorunun onarıldığını doğrula.

| Kontrolcü mesajı | Alet |
| --- | --- |
| Boru gevşek | İngiliz Anahtarı |
| Vidalar gevşek | Tornavida |
| Bir şey sıkışmış | Yumuşak Tokmak |
| Kaplamalar çökük | Sert Çekiç |
| Devre yanmış | Lehim Demiri |
| Buraya ait olmayan bir şey var | Levye |

LV'de aletleri bir Alet Çantasına koyup onunla Bakım Kapağına sağ tıklayarak birkaç sorunu aynı anda onarabilirsin. Makine çalışırken bakım sorunları ara sıra tekrarlayabilir, bu yüzden otomasyondan sonra kapağı erişilebilir tut.

Bakım, gerçek güç kullanımını etkiler. Bir sorun EYF verimliliğini %90'a düşürerek 120 EU/t'lik bir tarifi yaklaşık **133 EU/t**'ye çıkarır. Bu, dört LV jeneratörün nominal 128 EU/t çıkışını aşar. Tüm bakımı tamamlamak, iki LV Enerji Kapağıyla beslenen erken bir EYF için özellikle önemlidir.

## Yetenekler

EYF, NEI'de Electric Blast Furnace altında listelenen tarifleri çalıştırır. Yaygın kullanımlar arasında alüminyum, çelik, yüksek sıcaklık alaşımları ve belirli bir sıcaklık gerektiren tozlar bulunur. Bazı tarifler ayrıca bir Programlanmış Devre veya gaz girişi gerektirir. Bir malzemenin farklı süre ve maliyetlerde birkaç gaz destekli tarifi olabilir.

Bir üretim hattı tasarlarken tarifin eşyalarını, sıvılarını, EU/t'sini, sıcaklığını ve çıktı türünü kontrol et. Bazı tarifler, daha ileri işleme öncesinde bir [Vakum Dondurucu](../hv/vacuum_freezer.md) gerektiren **sıcak külçeler** üretir. Normal külçelerin dondurulması gerekmez.

Giriş Yolları tozları ve Programlanmış Devreleri barındırır; Girdi Kapakları tarifin gerektirdiği gazları veya diğer sıvıları sağlar. Çıkış Yolları eşyaları, Çıkış Kapakları sıvıları toplar. Birden fazla giriş arayüzü takabilirsin, ancak her yüksek fırın tarifinin gaz gerektirdiğini varsayma.

### İlk Alüminyumunu Üretmek

NEI'de <ItemLink id="gregtech:gt.metaitem.01:11019" showIcon="left" /> için Electric Blast Furnace tariflerini kontrol et. Tüm bileşenlerini, sıvılarını ve devrelerini elde edebileceğin birini seç. Farklı alüminyum kaynakları ve gaz seçenekleri farklı işlem sürelerine sahip olabilir; bir tarifin gereksinimlerini her alüminyum tarifine uygulama.

İlk denemen için şu kontrol listesini izle:

1. **Tarif gereksinimlerini oku.** Bileşenleri, devre ayarını, sıvı miktarını, EU/t'yi ve sıcaklığı kontrol et. Erken bir yapı normalde iki LV Enerji Kapağının destekleyebileceği 120 EU/t'lik bir tarif kullanır.
2. **Yapıyı ve bakımı kontrol et.** Kontrolcü yapı veya bakım sorunu bildirmemeli, Egzoz Çıkışı havalandırabilmeli ve makine etkin olmalıdır.
3. **Çıkışları hazırla.** Uygun Çıkış Yolunda ve Çıkış Kapağında yeterli alan bırak. İlk denemelerinde çıkış korumasını etkin tut ki işe yarar ürünler taşma olarak yok edilmesin.
4. **Önce gücü hazırla.** Kazanın ve jeneratörlerin stabilize olmasını bekle veya pilleri önceden şarj et. Her iki Enerji Kapağının da sürekli güç aldığından emin ol.
5. **Yalnızca küçük bir parti koy.** Tozları ve gereken devreyi bir Giriş Yoluna koy ve bir Girdi Kapağına sıvı sağla. Bir tarifin baştan sona tamamlanmasını izle.
6. **Otomasyonu sonra ekle.** Girdi miktarını artırmadan önce ürünlerin doğru çıkış arayüzlerine ulaştığını ve depolanan enerjinin sürekli azalmadığını doğrula.

Makine deneme sırasında güç kaybederse önce beslemeyi araştır. Tekrar tekrar daha fazla bileşen koymak bunu düzeltmez. Çelik, EYF için bir başka önemli erken kullanımdır; çelik üretiminin bir kısmını Tuğlalı Yüksek Fırından uzaklaştırmadan önce farklı bileşenleri ve gaz seçeneklerini karşılaştır.

## Güç ve Hız Aşırtma

### Neden İki LV Enerji Kapağı Kullanmalı?

EYF normal Enerji Kapakları kullanır. Yalnızca bir normal Enerji Kapağıyla tarif hesaplamaları 1 A'lık kullanılabilir güç kullanır. Aynı kademeden iki kapağın birleşik amperajı bir kademe daha yüksek tarifleri destekleyebilir. Her LV Enerji Kapağı en fazla 2 A LV kabul eder ve birleşik en fazla **4 A × 32 EU = 128 EU/t** verir. Bu, yaygın 120 EU/t'lik MV tariflerini destekler.

Bu tür kademe atlama, makinenin çalıştırabileceği daha yüksek kademeli tarifleri tanımlar. **Dış kablolar hâlâ 32 V LV güç taşır.** Daha fazla LV amperaj sağla; MV gerilimini doğrudan LV Enerji Kapaklarına verme. Kablo kapasitesi, jeneratör sayısı ve kapak sayısı güç gereksinimini birlikte karşılamalıdır.

| Yapılandırma | Kullanılabilir güç ve kullanım |
| --- | --- |
| Bir LV Enerji Kapağı | Tarif hesaplamaları 1 A LV veya 32 EU/t kullanır; yaygın 120 EU/t'lik tarifleri başlatamaz |
| İki LV Enerji Kapağı | Birleşik en fazla 4 A LV, nominal 128 EU/t kabul eder; erken MV tarifleri için uygundur |
| Bir MV Enerji Kapağı | Tarif hesaplamaları 1 A MV veya 128 EU/t kullanır; uygun bir MV beslemesi ve kablo gerektirir |

128 EU/t ile 120 EU/t'lik bir tarif arasında yalnızca **8 EU/t'lik pay** vardır. Aşağıdaki hesaplama, dört LV paketinin de aynı kayıplı yollardan gittiğini ve başka yük olmadığını varsayar:

| Bir kapağa ulaşmadan önce paket başına kayıp | EYF'in aldığı maksimum güç | 120 EU/t'lik tarif için pay |
| --- | --- | --- |
| 0 EU | 4 × 32 = 128 EU/t | 8 EU/t |
| 1 EU | 4 × 31 = 124 EU/t | 4 EU/t |
| 2 EU | 4 × 30 = 120 EU/t | 0 EU/t |
| 3 EU | 4 × 29 = 116 EU/t | Yetersiz güç |

Gerçek yollarda farklı kablo uzunlukları ve kayıpları olabilir, bu yüzden her birini ayrı hesapla. Enerji Kapağı tamponları makineyi geçici olarak ayakta tutabilir, ancak sürekli azalan bir tampon ortalama girişin yetersiz olduğu anlamına gelir. Başarıyla başlamak, tarifin tamamının biteceğini garanti etmez. Ayrıntılar için [Yerel Enerji Ağları](../../power/enet.md) ve [Kablo Kaybı](../../power/cable_loss.md) sayfalarına bak.

> [!WARNING]
> İşlem sırasında güç kaybı mevcut tarifi iptal eder ve hâlihazırda tüketilmiş bileşenleri yok edebilir. İlk partinden önce yeterli sürekli güç olduğunu doğrula. Yalnızca jeneratörlerin nominal çıkışına güvenmek yerine kablo kayıplarını hesaba kat.

### Seçenek 1: Kısa Kablolarla Doğrudan Güç

Dört <ItemLink id="gregtech:gt.blockmachines:1120" showIcon="left" /> erken bir EYF'i besleyebilir; her biri en fazla 1 A LV çıkışı verir. Aşağıdaki örnek her Enerji Kapağına iki türbin atar ve her iki dalı da kısa tutar.

<GameScene interactive={true} width="480" height="340" zoom="1.2">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
  <ImportPonder src="/assets/ponders/ebf_power_direct.json" />
</GameScene>

- Her kapak iki türbinden güç alır; dalı en az 2 A LV kapasitesine ihtiyaç duyar. Dört türbinin tümü tek bir besleme ana hattını paylaşıyorsa bu hat en az 4 A kapasite gerektirir.
- Türbin enerji çıkışlarını kablolara bakacak şekilde yönlendirmek için İngiliz Anahtarı kullan. Buhar geçerli sıvı giriş yüzlerinden girmelidir; bir türbini yalnızca Enerji Kapağına dayamak bağlantıyı garanti etmez.
- Sürekli türbin çıkışı sürekli buhar gerektirir. Isınmamış bir kazan, tükenmiş yakıt veya yetersiz boru dağıtımı bir türbinin üretim yapmasını durdurabilir.
- Bu düzenin payı çok azdır ve erken bir EYF'e ayrılmış beslemeye uygundur. Başka makineler bağlarsan yükü yeniden hesapla.

Türbinlerin ve Enerji Kapaklarının üzerine çatı eklerken Egzoz Çıkışının havalandırmasını açık tut. Animasyondaki oklar bağlantı yönlerini gösterir; gerçek güç hâlâ kablolara, jeneratörlere ve istikrarlı yakıt ile buhar beslemesine bağlıdır.

### Seçenek 2: EYF'in Yanında Pil Tamponu

EYF'in yanına bir <ItemLink id="gregtech:gt.blockmachines:171" showIcon="left" /> yerleştirebilir, dört kullanılabilir LV pil takabilir ve her iki Enerji Kapağını kısa kablolarla bağlayabilirsin. Tamponun maksimum çıkış amperajı kullanılabilir pil sayısına bağlıdır: **yalnızca bir pilli dört yuvalı bir tampon 4 A çıkış veremez**.

<GameScene interactive={true} width="480" height="340" zoom="1.1">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <ImportPonder src="/assets/ponders/ebf_power_buffer.json" />
</GameScene>

Bu örnek sekiz LV Buhar Türbini kullanır ve diğer LV makinelerini de besler. Jeneratör sayısını gerçek yüküne göre ayarla. EYF'in 120 EU/t'siyle birlikte kablo kayıplarını, Pil Tamponuyla ilgili kayıpları ve diğer makineleri hesaba kat.

Tamponun çıkış yüzünü EYF dalına doğrult ve jeneratörleri diğer geçerli giriş yüzlerine bağla. Çıkış ana hattı en az 4 A LV kapasite, her Enerji Kapağı dalı en az 2 A gerektirir. Jeneratör tarafındaki kabloları da içlerinden geçebilecek birleşik akıma göre boyutlandır.

Tampon, jeneratörlerdeki dalgalanmaları yumuşatır ve EYF yakınında daha kısa kablolara izin verir. Yine de yeterli ortalama üretime ihtiyaç duyar. Pilleri şarj et, ardından art arda birkaç parti çalıştır. Her partiden sonra şarj düşüyorsa üretimi artır, kablo kaybını azalt veya diğer yükleri azalt. Pil kapasitesi eklemek yalnızca pillerin tükendiği zamanı geciktirir.

> [!WARNING]
> Enerji Kapağı gerilim sınırları hâlâ geçerlidir. MV gücünü doğrudan LV Enerji Kapaklarına bağlama. MV gücüne yükseltirken kapakları değiştir ve kabloları da kontrol et. Kablolar hem gerilim hem de amperaj sınırlarını karşılamalıdır, aksi halde yanabilirler.

### Gücü Yükseltmek ve Hız Aşırtma

Daha yüksek kademeli veya ek normal Enerji Kapakları, daha yüksek güçlü tarifleri destekleyebilir ve [kademe atlama](../../tierskipping_overcloking_parallels/tierskipping.md) ile [hız aşırtma](../../tierskipping_overcloking_parallels/overclocking.md) sayesinde işlemi kısaltabilir. Her normal hız aşırtma EU/t'yi dörtle çarpar ve süreyi yarıya indirir. Kullanılabilir güç ve sıcaklık hâlâ hız aşırtma sayısını sınırlar.

Örneğin, fazla ısı indirimlerini yok sayarsak bir normal hız aşırtma 120 EU/t'lik bir tarifi yaklaşık 480 EU/t'ye çıkarır ve süresini yarıya indirir. Enerji Kapağını yükselttikten sonra jeneratör sayısını ve buhar beslemesini yeniden kontrol et; başlangıçtaki 120 EU/t'lik güç bütçesi artık yeterli değildir.

## Sıcaklık ve Isıtma Bobinleri

### Tarif Gereksinimini Karşılamak

Aynı kademedeki bobinler temel sıcaklığı belirler. İki LV Enerji Kapağıyla Kupronikel Bobinler **1801 K** sağlar; bu, 1300 K gerektiren alüminyum tarifleri için yeterlidir. Yine de seçtiğin tarifi kontrol et.

| Bobin | İki LV Enerji Kapağı veya bir MV Enerji Kapağı ile sıcaklık |
| --- | --- |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> | 1801 K |
| <ItemLink id="gregtech:gt.blockcasings5:1" showIcon="left" /> | 2701 K |
| <ItemLink id="gregtech:gt.blockcasings5:2" showIcon="left" /> | 3601 K |

Makine ayrıca sıcaklığı **normal Enerji Kapaklarının nominal gerilimleri toplamının gerilim kademesine** göre ayarlar. MV temel alınır; üzerindeki her kademe 100 K ekler. Bu yüzden Kupronikel Bobinlerle bir HV Enerji Kapağı 1901 K verir. Aynı kademedeki kapak sayısını değiştirmek de sıcaklığı değiştirebilir. Yalnızca bir LV Enerji Kapağıyla Kupronikel Bobinler 1701 K verir.

Bu sıcaklık hesabı, gelen kablo geriliminden, gerçek amperajdan ve kablo kaybından ayrıdır. Bobinleri veya Enerji Kapaklarını yükselttikten sonra gerçek sıcaklığı kontrol etmek için bir <ItemLink id="gregtech:gt.metaitem.01:32762" showIcon="left" /> kullan. Makinenin o anda tükettiği EU/t'den bunu çıkarsama.

Makine sıcaklığı tarif gereksiniminin altındaysa daha fazla güç tarifi başlatmaz. On altı bobinin tamamını aynı kademeden olanlarla değiştir ve bitişik makinelerle paylaşılan bobinleri de kontrol et.

### Fazla Isının Faydaları

Tarif gereksiniminin her 900 K üzeri, çarpımsal olarak %5 daha güç indirimi sağlar. Her 1800 K, bir normal hız aşırtmanın kusursuz hız aşırtmaya dönüşmesini sağlar. Kusursuz hız aşırtma yine EU/t'yi dörtle çarpar ama süreyi dörde böler; böylece bu hız aşırtma tarif başına toplam enerjiyi artırmaz.

| Tarif gereksiniminin üzerindeki sıcaklık | Güç çarpanı | Kusursuz olabilecek hız aşırtma sayısı |
| --- | --- | --- |
| 900 K'den az | %100 | 0 |
| 900–1799 K | %95 | 0 |
| 1800–2699 K | 0,95 × 0,95 = %90,25 | 1 |
| 2700–3599 K | 0,95³ ≈ %85,74 | 1 |
| 3600–4499 K | 0,95⁴ ≈ %81,45 | 2 |

Örneğin, bir HV Enerji Kapağı ve Nikrom Bobinler 3701 K verir. 1300 K gerektiren bir alüminyum tarifinde 2401 K fazla ısı vardır; bu iki %5 güç indirimi sağlar ve bir kusursuz hız aşırtmaya izin verir. Ortaya çıkan tarif gücü ve süresi için NEI'yi ve makine ekranını kontrol et.

Kusursuz hız aşırtmalar, güç kaynağının zaten desteklediği hız aşırtmaları iyileştirir. Fazla ısı ek güç yaratmaz. Önce erken makineyi güvenilir şekilde çalıştır, ardından daha iyi bobinlerin, daha fazla gücün ve ek EYF'lerin maliyetlerini karşılaştır.

## Duvar Paylaşımı ve Otomasyon

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right">
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

Birden fazla EYF yan duvar kasalarını ve bobinlerini paylaşabilir. 2×2 düzenlemeyle dört EYF, bağımsız yapılarda 64 olan bobin sayısını 42'ye düşürür. Paylaşılan bobinler her bağlı makinenin kademe gereksinimini karşılamalıdır, bu yüzden yükseltme yaparken etkilenen tüm EYF'leri kontrol et.

Bakım Kapakları ve bazı giriş/çıkış arayüzleri de paylaşılabilir. Güç, aynı anda çalışan tüm makineleri kapsamalıdır. Paylaşılan Enerji Kapakları makinelerin amperaj için rekabet etmesine yol açar; bu özellikle iki kapaklı kademe atlama kullanırken güç kesintilerine neden olma olasılığı yüksektir.

Otomasyon için toz, devre ve sıvı girişlerini düzenle ve sıcak külçeler, normal eşyalar ve sıvılar için yeterli çıkış alanı bırak. Bir EYF bir Vakum Dondurucuyu besliyorsa küçük bir partiyle test et ve yalnızca soğutma gerektiren sıcak külçelerin oraya ulaştığını doğrula. Giriş filtreleme, eşya taşıma ve depolama ayarları için [Vakum Dondurucu rehberine](../hv/vacuum_freezer.md#hot-ingot-routing) bak.

Birden fazla Giriş Yoluyla kontrolcünün **giriş ayrıştırması** ayarını kontrol et. Etkinleştirildiğinde her Giriş Yolunun eşyaları ayrı bir tarif grubu olarak değerlendirilir. Bir tarif için gereken tozları ve devreyi birlikte eşleşebilecekleri bir Giriş Yolunda tut. Farklı tarifler için ayrı Giriş Yolları ve devreler, istenmeyen tarif eşleşmelerini azaltabilir.

Bir Vakum Dondurucu edinmeden önce normal külçe üreten ve sonraki işlemesi sende mevcut olan tarifleri önceliklendir. Daha sonra EYF'leri alüminyuma, çeliğe ve yüksek sıcaklık malzemelerine adayabilirsin. Bobinleri paylaşan dört EYF yapı malzemesinden tasarruf sağlar, ancak aynı anda çalışma yine de dördü için yeterli güç gerektirir.

## Sorun Giderme

| Belirti | Kontrol edilecekler |
| --- | --- |
| Yapı tamamlanmamış | On altı bobinin tümü aynı kademede; iki orta merkez hava; Egzoz Çıkışı üst merkezde; tabanda Enerji Kapakları, bir Bakım Kapağı ve giriş/çıkış arayüzleri var |
| Yeni makinede bakım sorunları var | Bakım Kapağında altı aletin tümünü kullanarak onar, ardından kontrolcüde doğrula; yapıyı oluşturmak ve bakımı tamamlamak ayrı adımlardır |
| Yetersiz sıcaklık | Gerçek sıcaklığı tara ve bobin kademesini, güç yapılandırmasını ve tarifin NEI'deki sıcaklık gereksinimini kontrol et |
| Bileşenler var ama tarif bulunamıyor | Bileşen türlerini ve miktarlarını, devre ayarını, sıvıları ve EU/t'yi kontrol et; giriş ayrıştırmasıyla gerekli eşyaların Giriş Yolları arasında bölünmediğinden emin ol |
| Yetersiz gerilim veya güç | Erken bir yapıda iki LV Enerji Kapağı veya yükseltilmiş tarifler için uygun kapaklar olup olmadığını kontrol et; Giriş Yolu kademesi makine gerilimini belirlemez |
| Makine başladıktan hemen sonra duruyor | Üretimi, kablo kapasitesini ve kaybını, kapaklara sürekli güç gidip gitmediğini kontrol et; test etmek için tekrar tekrar pahalı bileşenler koyma |
| Makine kısa süre çalışıp sonra güç kaybediyor | Pil ve kapak tamponlarının sürekli azalıp azalmadığını izle; kazan buhar çıkışını, boru dağıtımını, diğer yükleri ve bakımı kontrol et |
| Dört yuvalı Pil Tamponu yetersiz güç sağlıyor | Dört kullanılabilir, şarjlı LV pil, doğru çıkış yüzü ve yeterli ortalama üretim olup olmadığını kontrol et |
| Yetersiz çıkış alanı | Uygun Çıkış Yollarının ve Çıkış Kapaklarının var olduğunu, dolu olmadığını ve tarifin tüm çıktısını alabildiğini kontrol et |
| Kirlilik dışarı verilemiyor | Egzoz Çıkışının havaya havalandırdığını ve gelişmiş bir Egzoz Çıkışında gereken Hava Filtresinin takılı olduğunu kontrol et |
| Kablolar yanıyor veya Enerji Kapakları patlıyor | Kablo gerilim ve amperaj sınırlarını, Enerji Kapaklarındaki aşırı gerilimi ve yağmura maruz kalmayı kontrol et |

Genel kurallar için [Multiblok Makineler](../../gtnh_basics/multiblocks.md) sayfasına bak. Malzeme talebi arttıkça, tek bir makinede tekrarlanan hız aşırtmalara güvenmek yerine ek EYF'ler iş yükünü bölebilir.

## Kaynaklar

- [GTNH Wiki: Elektrikli Yüksek Fırın](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)