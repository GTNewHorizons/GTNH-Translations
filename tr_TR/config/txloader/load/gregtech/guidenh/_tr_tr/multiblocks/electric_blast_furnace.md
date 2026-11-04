---
item_ids:
  - gregtech:gt.blockmachines:1000
quest_ids:
  - AAAAAAAAAAAAAAAAAAAATQ
navigation:
  title: Elektrikli Yüksek Fırın
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1000
  position: -1001
---
# Elektrikli Yüksek Fırın
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1000" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> (Elektrikli Yüksek Fırın, kısaca EYF), LV'de kullanılabilen bir işleme multibloğudur. Elektrik ve Isıtma Bobinleri, Tuğlalı Yüksek Fırının ulaşamadığı sıcaklıklara ulaşmasını sağlar. İlk büyük kullanım alanı genellikle alüminyum üretimidir; sonrasında yüksek sıcaklıkta işlenmesi gereken birçok metali ve diğer malzemeyi işler.

EYF genellikle yeni bir oyuncunun ilk **GT elektrikli multibloğudur** ve MV malzemelerine doğru önemli bir adımdır. Onu inşa etmek yapı gereksinimlerini, eşya ve sıvı arayüzlerini, bakımı ve sürekli gücü bir araya getirir. İlk EYF'ini güvenilir şekilde çalıştırma deneyimi, sonraki birçok multibloğa aktarılır.

Kontrolcüyü elde ettiğin kademe, tariflerinin gerektirdiği güçten ayrıdır. İlk Enerji Kapakların LV olsa da yaygın alüminyum tarifleri MV güç gerektirir. İki LV Enerji Kapağı ve yeterli bir güç kaynağı, erken bir EYF'in bu tarifleri çalıştırmasını sağlar.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | LV; iki LV Enerji Kapağı genellikle erken MV tarifleri için güç sağlar |
| Yapı boyutu | 3×3×4; iki orta katmanın her birinin merkezi havadır |
| Güç | Birden fazla normal Enerji Kapağını destekler; Çok Amperli Enerji Kapaklarını veya Lazer Hedef Kapaklarını desteklemez |
| Hız aşırtma ve paralel | Genellikle normal hız aşırtma kullanır; yeterli fazla ısı bunların bir kısmını kusursuz hız aşırtmaya çevirir; ek paralel bonusu yoktur |
| İşleme bonusları | Tarif gereksiniminin her 900 K üzeri, güç kullanımını %95 ile çarpar; her 1800 K bir kusursuz hız aşırtmaya izin verir |
| Bakım ve kirlilik | Bakım ve bir Egzoz Çıkışı gerektirir; temel kirlilik 400 gibbl/s'dir ve gerçek emisyonlar Egzoz Çıkışı kademesine göre azalır |

İlk inşa için **Kupronikel Bobinler, iki LV Enerji Kapağı, kısa kablolar ve küçük bir grup alüminyum malzemesiyle** başla. Yapıyı oluşturmak yalnızca ilk adımdır: işlemin başarıyla tamamlanabilmesi için tarif, sıcaklık, çıkış alanı ve sürekli güç kaynağının hepsi uygun olmalıdır.

## Üretim ve İnşa

### Kontrolcüyü ve Arayüzleri Anlamak

Kontrolcü makine durumunu gösterir, yapıyı denetler ve kontroller sunar. Eşyalar, sıvılar ve güç aşağıdaki bileşenler üzerinden girer. Veriyolları ve kapaklar, ancak geçerli yapı konumlarına yerleştirildiğinde EYF'in parçası olur.

| Bileşen | Amaç |
| --- | --- |
| Giriş Yolu | Tozlar ve Programlanmış Devreler gibi eşya malzemelerini tutar |
| Çıkış Yolu | Külçeler ve sıcak külçeler gibi eşya ürünlerini alır |
| Girdi Kapağı | Azot gibi tarifin gerektirdiği sıvıları sağlar |
| Çıkış Kapağı | Tarifte listelenen sıvı ürünleri alır |
| Enerji Kapağı | Harici güç ağından EU alır ve multibloğa güç verir |
| Bakım Kapağı | Aletlerin bakım sorunlarını onarmasına izin verir |
| Egzoz Çıkışı | Kirliliği dışarı atar; menfez yüzü açık kalmalıdır |

Giriş Yolu ile Girdi Kapağı farklı amaçlara hizmet eder. Tozu kontrolcünün yuvasına koymak veya bir Giriş Yoluna sıvı borusu bağlamak, gereken arayüzlerin yerini tutmaz.

### Bileşenleri Hazırlamak

Kontrolcü ve Isı Geçirmez Makine Kasalarının güncel tarifleri aşağıda gösterilmiştir. Isıtma Bobinleri birkaç kademede gelir; üretmeden önce malzemelerini ve tariflerini NEI'den kontrol et.

<RecipesFor id="gregtech:gt.blockmachines:1000" />

<RecipesFor id="gregtech:gt.blockcasings:11" />

<RecipesFor id="gregtech:gt.blockcasings5:0" />

Alt katman kontrolcüyü ve arayüzlerin çoğunu barındırır. İki orta katmanın her biri, merkezi hava olacak şekilde sekiz Isıtma Bobininden oluşan bir halkadır. Üst merkezde Egzoz Çıkışı bulunmalıdır. Kalan alt katman ve üst halka konumlarını Isı Geçirmez Makine Kasalarıyla veya o konumlara izin verilen arayüzlerle doldur.

| Bileşen | Miktar ve konum |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1000" showIcon="left" /> | Bir adet, alt katmanın ön merkezinde |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> veya diğer Isıtma Bobinleri | On altı adet, iki orta katmanda; hepsi aynı kademede olmalı |
| <ItemLink id="gregtech:gt.blockcasings:11" showIcon="left" /> | 0–12 adet, alt katmandaki ve üst halkadaki kullanılmayan konumları doldurur |
| Normal Enerji Kapağı | En az bir adet, alt katmanda; erken MV tarifleri için genellikle iki <ItemLink id="gregtech:gt.blockmachines:41" showIcon="left" /> kullanılır |
| <ItemLink id="gregtech:gt.blockmachines:90" showIcon="left" /> | Bir adet, alt katmanda |
| <ItemLink id="gregtech:gt.blockmachines:91" showIcon="left" /> | Bir adet, üst merkezde; menfez yüzünü açık tut |
| Giriş Yolu veya Girdi Kapağı | En az bir giriş arayüzü, alt katmanda; tarifin gerektirdiği eşya ve sıvı girişlerini sağla |
| Çıkış Yolu veya Çıkış Kapağı | En az bir çıkış arayüzü; Çıkış Yolları alt katmana gider, Çıkış Kapakları ise üst halkayı da doldurabilir |

En az bir giriş ve bir çıkış arayüzü gereklidir. Yalnızca iki LV Enerji Kapağı, bir Bakım Kapağı, bir Giriş Yolu ve bir Çıkış Yolu ile kalan konumlar için **11 Isı Geçirmez Makine Kasası** gerekir. Ek sıvı kapakları veya veriyolları, izin verilen konumlarda kasaların yerini alabilir; bobinlerin veya Egzoz Çıkışının yerini alamazlar.

Aşağıdaki animasyon, gaz kullanan tarifler için bir <ItemLink id="gregtech:gt.blockmachines:51" showIcon="left" /> de içerir, bu yüzden **10 Isı Geçirmez Makine Kasası** kullanır. İlk tarifinde sıvı girişi yoksa başlangıçta orada bir kasa bırakıp daha sonra yerine bir Girdi Kapağı koyabilirsin.

### Katman Katman İnşa Etmek

İnşa sırasını görmek için oynat'a bas veya bir adımı tekrar görmek için zaman çizelgesini sürükle. Animasyon kontrolcüyle başlar, ardından alt katman arayüzlerini, iki bobin halkasını, üst katmanı ve yağmurdan koruma için bir çatı ekler.

<GameScene interactive={true} width="480" height="340">
  <ImportStructure src="/assets/structures/ebf_ponder.snbt" />
  <ImportPonder src="/assets/ponders/ebf_build.json" />
</GameScene>

1. **Ön tarafı seç ve kontrolcüyü yerleştir.** 3×3'lük bir taban ayır ve kontrolcüyü dışa bakacak şekilde ön merkezine yerleştir. Bakıma, eşya ve sıvı arayüzlerine ve kablo bağlantılarına erişim bırak.
2. **Tabanı tamamla.** Kalan sekiz alt katman konumu Enerji Kapaklarını, bir Bakım Kapağını ve giriş/çıkış arayüzlerini kabul eder. Kullanılmayan konumları Isı Geçirmez Makine Kasalarıyla doldur. Alt merkez de yapının bir parçasıdır ve boş bırakılmamalıdır.
3. **İlk bobin halkasını yerleştir.** Tabanın üzerine, merkezi hava kalacak şekilde sekiz Kupronikel Bobin'den oluşan 3×3'lük bir halka inşa et.
4. **İkinci bobin halkasını yerleştir.** Aynı bobinlerden bir halka daha ekle, toplam on altı olsun. Tüm bobinler aynı kademede olmalı; Kupronikel ve Kantal katmanlarını karıştırma.
5. **Üst kısmı bitir ve Egzoz Çıkışını tak.** Egzoz Çıkışını dördüncü katmanın merkezine, normalde yukarı doğru menfez açacak şekilde koy. Dıştaki sekiz konumu kasalarla doldur veya gerektiğinde yerlerine sıvı Çıkış Kapakları koy.
6. **Yapıyı denetle.** Her iki orta katmanın merkez bloklarını meşalelerden, kablolardan, borulardan ve diğer bloklardan uzak tut. EYF oluşmazsa kontrolcü arayüzünde yapıyı yeniden denetle ve eksik veya yanlış yerleştirilmiş bileşenlere bak.

Yapıyı önizlemek ve inşa etmeye yardımcı olmak için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan. `coil` alt kanalı bobin kademesini seçer. İnşadan sonra yapıyı kontrolcüde denetle ve bakım sorunlarını Bakım Kapağında onar.

> [!WARNING]
> Enerji Kapaklarını, jeneratörleri ve Pil Tamponlarını yağmurdan koru. Egzoz Çıkışının menfezinin önünde en az bir hava bloğu bırak ve çatıyı daha yukarıya inşa et. Yukarı bakan bir Egzoz Çıkışının doğrudan üzerine çatı koyma veya menfezini kablolar ya da borularla kapatma.

Eski rehberler, egzoz gazlarını geri kazanmak için üst halkada gaz Çıkış Kapakları gerektirebilir. Bu özel egzoz geri kazanım sistemi güncel sürümde kaldırıldı. Bir tarif sıvı üretiyorsa NEI'de gösterilen çıktılar için Çıkış Kapakları sağla; alt katmandaki Çıkış Kapakları da gaz alabilir. Üst halka, Çıkış Kapakları için geçerli bir konum olmaya devam eder.

### Bakımı Tamamlamak

Yeni yerleştirilmiş bir EYF'te genellikle bakım sorunları olur. Bakım Kapağını aç, ilgili GT aletini imlecinde tut ve sorunu onarmak için bakım düğmesine tıkla. Lehim demiri ayrıca şarj ve lehim gerektirir. Ardından kontrolcüye dön ve her sorunun onarıldığını doğrula.

| Kontrolcü mesajı | Alet |
| --- | --- |
| Boru gevşek | İngiliz Anahtarı |
| Vidalar gevşek | Tornavida |
| Bir şey sıkışmış | Yumuşak Tokmak |
| Kaplamalar çökük | Sert Çekiç |
| Devreler yanmış | Lehim Demiri |
| Buraya ait olmayan bir şey var | Levye |

LV'de aletleri bir Alet Kutusuna koyup onunla Bakım Kapağına sağ tıklayarak birkaç sorunu aynı anda da onarabilirsin. Bakım sorunları makine çalışırken ara sıra yeniden ortaya çıkabilir, bu yüzden otomasyondan sonra da kapağı erişilebilir tut.

Bakım, gerçek güç kullanımını etkiler. Bir sorun EYF verimliliğini %90'a düşürerek 120 EU/t'lik bir tarifi yaklaşık **133 EU/t**'ye çıkarır. Bu, dört LV jeneratörün nominal 128 EU/t çıkışını aşar. İki LV Enerji Kapağı üzerinden beslenen erken bir EYF için tüm bakımı tamamlamak özellikle önemlidir.

## Yetenekler

EYF, NEI'de Elektrikli Yüksek Fırın altında listelenen tarifleri çalıştırır. Yaygın kullanımlar arasında alüminyum, çelik, yüksek sıcaklık alaşımları ve belirli bir sıcaklık gerektiren tozlar bulunur. Bazı tarifler ayrıca bir Programlanmış Devre veya gaz girişi gerektirir. Bir malzemenin farklı süre ve maliyetlerde birkaç gaz destekli tarifi olabilir.

Bir üretim hattı tasarlarken tarifin eşyalarını, sıvılarını, EU/t'sini, sıcaklığını ve çıktı türünü kontrol et. Bazı tarifler, daha ileri işleme öncesinde [Vakum Dondurucu](./vacuum_freezer.md) gerektiren **sıcak külçeler** üretir. Normal külçelerin dondurulması gerekmez.

Giriş Yolları tozları ve Programlanmış Devreleri tutar; Girdi Kapakları tarifin gerektirdiği gazları veya diğer sıvıları sağlar. Çıkış Yolları eşyaları, Çıkış Kapakları ise sıvıları toplar. Birden fazla giriş arayüzü kurabilirsin, ancak her yüksek fırın tarifinin gaz gerektirdiğini varsayma.

### İlk Alüminyumunu Üretmek

NEI'de <ItemLink id="gregtech:gt.metaitem.01:11019" showIcon="left" /> için Elektrikli Yüksek Fırın tariflerini kontrol et. Tüm malzemelerini, sıvılarını ve devrelerini elde edebileceğin birini seç. Farklı alüminyum kaynakları ve gaz seçenekleri farklı işlem sürelerine sahip olabilir; bir tarifin gereksinimlerini her alüminyum tarifine uygulama.

İlk denemen için şu kontrol listesini takip et:

1. **Tarif gereksinimlerini oku.** Malzemeleri, devre ayarını, sıvı miktarını, EU/t'yi ve sıcaklığı kontrol et. Erken bir yapı normalde iki LV Enerji Kapağının destekleyebileceği 120 EU/t'lik bir tarif kullanır.
2. **Yapıyı ve bakımı denetle.** Kontrolcü yapı veya bakım sorunu bildirmemeli, Egzoz Çıkışı kirliliği dışarı atabilmeli ve makine etkin olmalı.
3. **Çıkışları hazırla.** Uygun Çıkış Yolunda ve Çıkış Kapağında yeterli alan bırak. İlk denemelerinde çıkış korumasını açık tut, böylece faydalı ürünler taşma olarak yok edilmez.
4. **Önce gücü hazırla.** Kazanın ve jeneratörlerin oturmasını bekle veya pilleri önceden şarj et. Her iki Enerji Kapağının sürekli güç aldığından emin ol.
5. **Yalnızca küçük bir parti koy.** Tozları ve gereken devreyi bir Giriş Yoluna koy ve bir Girdi Kapağına sıvı sağla. Bir tarifin tamamen bitmesini izle.
6. **Otomasyonu sonra ekle.** Girdi miktarını artırmadan önce ürünlerin doğru çıkış arayüzlerine ulaştığını ve depolanan enerjinin sürekli azalmadığını doğrula.

Makine deneme sırasında güç kaybederse önce beslemeyi araştır. Tekrar tekrar daha fazla malzeme koymak bunu düzeltmez. Çelik, EYF'in bir başka önemli erken kullanım alanıdır; bir miktar çelik üretimini Tuğlalı Yüksek Fırından taşımadan önce farklı malzemeleri ve gaz seçeneklerini karşılaştır.

## Güç ve Hız Aşırtma

### Neden İki LV Enerji Kapağı Kullanılır?

EYF normal Enerji Kapakları kullanır. Yalnızca bir normal Enerji Kapağıyla tarif hesaplamaları 1 A kullanılabilir güç kullanır. Aynı kademeden iki kapakla, birleşik amperajları bir kademe daha yüksek tarifleri destekleyebilir. Her LV Enerji Kapağı en fazla 2 A LV kabul eder ve birleşik en fazla **4 A × 32 EU = 128 EU/t** verir. Bu, yaygın 120 EU/t'lik MV tariflerini destekler.

Bu kademe atlama biçimi, makinenin çalıştırabildiği daha yüksek kademeli tarifleri tanımlar. **Harici kablolar hâlâ 32 V LV güç taşır.** Daha fazla LV amperaj sağla; MV gerilimini doğrudan LV Enerji Kapaklarına verme. Kablo kapasitesi, jeneratör sayısı ve kapak sayısı güç gereksinimini birlikte karşılamalıdır.

| Yapılandırma | Kullanılabilir güç ve kullanım |
| --- | --- |
| Bir LV Enerji Kapağı | Tarif hesaplamaları 1 A LV veya 32 EU/t kullanır; yaygın 120 EU/t'lik tarifleri başlatamaz |
| İki LV Enerji Kapağı | Birleşik 4 A LV'ye kadar kabul eder, nominal 128 EU/t; erken MV tarifleri için uygundur |
| Bir MV Enerji Kapağı | Tarif hesaplamaları 1 A MV veya 128 EU/t kullanır; uygun bir MV beslemesi ve kabloları gerektirir |

128 EU/t ile 120 EU/t'lik bir tarif arasında yalnızca **8 EU/t'lik pay** vardır. Aşağıdaki hesaplama, dört LV paketinin de aynı kayıplı yollardan gittiğini ve başka yük olmadığını varsayar:

| Kapaklara ulaşmadan önce paket başına kayıp | EYF'in aldığı maksimum güç | 120 EU/t'lik tarif için pay |
| --- | --- | --- |
| 0 EU | 4 × 32 = 128 EU/t | 8 EU/t |
| 1 EU | 4 × 31 = 124 EU/t | 4 EU/t |
| 2 EU | 4 × 30 = 120 EU/t | 0 EU/t |
| 3 EU | 4 × 29 = 116 EU/t | Yetersiz güç |

Gerçek yollarda farklı kablo uzunlukları ve kayıplar olabilir, bu yüzden her birini ayrı hesapla. Enerji Kapağı tamponları makineyi geçici olarak ayakta tutabilir, ancak sürekli düşen bir tampon ortalama girişin yetersiz olduğu anlamına gelir. Başarıyla başlamak, tarifin tamamen biteceğini garanti etmez. Ayrıntılar için [Yerel Enerji Ağları](/power/enet.md) ve [Kablo Kaybı](/power/cable_loss.md) sayfalarına bak.

> [!WARNING]
> İşlem sırasında güç kaybı mevcut tarifi iptal eder ve hâlihazırda tüketilmiş malzemeleri yok edebilir. İlk partinden önce yeterli sürekli güç olduğunu doğrula. Yalnızca jeneratörlerin nominal çıkışına güvenmek yerine kablo kayıplarını da hesaba kat.

### Seçenek 1: Kısa Kablolarla Doğrudan Güç

Dört <ItemLink id="gregtech:gt.blockmachines:1120" showIcon="left" />, her biri en fazla 1 A LV çıkışıyla erken bir EYF'i besleyebilir. Aşağıdaki örnek, her Enerji Kapağına iki türbin atar ve iki dalı da kısa tutar.

<GameScene interactive={true} width="480" height="340" zoom="1.2">
  <ImportStructure src="/assets/structures/powering_ebf_1.snbt" />
  <RemoveBlocks id="Railcraft:residual.heat" />
  <ImportPonder src="/assets/ponders/ebf_power_direct.json" />
</GameScene>

- Her kapak iki türbinden güç alır; dalı en az 2 A LV kapasite gerektirir. Dört türbin de tek bir besleme gövdesini paylaşıyorsa o gövde en az 4 A kapasite gerektirir.
- Türbin enerji çıkışlarını kablolara yöneltmek için İngiliz Anahtarı kullan. Buhar geçerli sıvı giriş yüzlerinden girmelidir; bir türbini basitçe bir Enerji Kapağının yanına koymak bağlantıyı garanti etmez.
- Sürekli türbin çıkışı sürekli buhar gerektirir. Isınmamış bir kazan, tükenmiş yakıt veya yetersiz boru dağıtımı bir türbinin üretimini durdurabilir.
- Bu düzende çok az pay vardır ve erken EYF'e ayrılmış bir beslemeye uygundur. Başka makineler bağlarsan yükü yeniden hesapla.

Türbinlerin ve Enerji Kapaklarının üzerine çatı eklerken Egzoz Çıkışı menfezini açık tut. Animasyondaki oklar bağlantı yönlerini gösterir; gerçek güç yine de kablolara, jeneratörlere ve istikrarlı bir yakıt ve buhar beslemesine bağlıdır.

### Seçenek 2: EYF'in Yanında Bir Pil Tamponu

EYF'in yanına bir <ItemLink id="gregtech:gt.blockmachines:171" showIcon="left" /> koyabilir, dört kullanılabilir LV pil takabilir ve iki Enerji Kapağını kısa kablolarla bağlayabilirsin. Tamponun maksimum çıkış amperajı kullanılabilir pil sayısına bağlıdır: **yalnızca tek pili olan dört yuvalı bir tampon 4 A çıkış veremez**.

<GameScene interactive={true} width="480" height="340" zoom="1.1">
  <ImportStructure src="/assets/structures/powering_ebf_2.snbt" />
  <ImportPonder src="/assets/ponders/ebf_power_buffer.json" />
</GameScene>

Bu örnek sekiz LV Buhar Türbini kullanır ve başka LV makinelerini de besler. Jeneratör sayısını gerçek yüküne göre ayarla. EYF'in 120 EU/t'sinin yanında kablo kayıplarını, Pil Tamponuyla ilgili kayıpları ve diğer makineleri de hesaba kat.

Tamponun çıkış yüzünü EYF dalına yönelt ve jeneratörleri diğer geçerli giriş yüzlerine bağla. Çıkış gövdesi en az 4 A LV kapasite, her Enerji Kapağı dalı da en az 2 A gerektirir. Jeneratör tarafındaki kabloları da üzerlerinden geçebilecek birleşik akıma göre boyutlandır.

Tampon, jeneratörlerden gelen dalgalanmaları yumuşatır ve EYF yakınında daha kısa kablolara izin verir. Yine de yeterli ortalama üretime ihtiyaç duyar. Pilleri şarj et, ardından arka arkaya birkaç parti çalıştır. Her partiden sonra şarj düşüyorsa üretimi artır, kablo kaybını azalt veya diğer yükleri azalt. Pil kapasitesi eklemek yalnızca pillerin tükenme süresini geciktirir.

> [!WARNING]
> Enerji Kapağı gerilim sınırları hâlâ geçerlidir. MV gücünü doğrudan LV Enerji Kapaklarına bağlama. MV güce yükseltme yaparken kapakları değiştir ve kabloları da kontrol et. Kablolar hem gerilim hem de amper sınırlarını karşılamalıdır, yoksa yanabilirler.

### Gücü Yükseltmek ve Hız Aşırtma

Daha yüksek kademeli veya ek normal Enerji Kapakları, [kademe atlama](/tierskipping_overcloking_parallels/tierskipping.md) ve [hız aşırtma](/tierskipping_overcloking_parallels/overclocking.md) yoluyla daha yüksek güçlü tarifleri destekleyebilir ve işlemi kısaltabilir. Her normal hız aşırtma EU/t'yi dörtle çarpar ve süreyi yarıya indirir. Kullanılabilir güç ve sıcaklık yine de hız aşırtma sayısını sınırlar.

Örneğin, fazla ısı indirimlerini hesaba katmazsak bir normal hız aşırtma 120 EU/t'lik bir tarifi yaklaşık 480 EU/t'ye çıkarır ve süresini yarıya indirir. Enerji Kapağını yükselttikten sonra jeneratör sayısını ve buhar beslemesini yeniden kontrol et; ilk 120 EU/t'lik güç bütçesi artık yeterli değildir.

## Sıcaklık ve Isıtma Bobinleri

### Tarif Gereksinimini Karşılamak

Aynı kademeden bobinler temel sıcaklığı belirler. İki LV Enerji Kapağıyla Kupronikel Bobinler **1801 K** sağlar; bu, 1300 K gerektiren alüminyum tarifleri için yeterlidir. Yine de seçtiğin tarifi kontrol et.

| Bobin | İki LV Enerji Kapağı veya bir MV Enerji Kapağıyla sıcaklık |
| --- | --- |
| <ItemLink id="gregtech:gt.blockcasings5:0" showIcon="left" /> | 1801 K |
| <ItemLink id="gregtech:gt.blockcasings5:1" showIcon="left" /> | 2701 K |
| <ItemLink id="gregtech:gt.blockcasings5:2" showIcon="left" /> | 3601 K |

Makine ayrıca sıcaklığı **normal Enerji Kapaklarının nominal gerilimleri toplamının gerilim kademesine** göre ayarlar. MV temel alınır; üzerindeki her kademe 100 K ekler. Bu nedenle Kupronikel Bobinlerle bir HV Enerji Kapağı 1901 K verir. Aynı kademedeki kapak sayısını değiştirmek de sıcaklığı değiştirebilir. Yalnızca bir LV Enerji Kapağıyla Kupronikel Bobinler 1701 K verir.

Bu sıcaklık hesabı, gelen kablo geriliminden, gerçek amperajdan ve kablo kaybından ayrıdır. Bobinleri veya Enerji Kapaklarını yükselttikten sonra gerçek sıcaklığı kontrol etmek için bir <ItemLink id="gregtech:gt.metaitem.01:32762" showIcon="left" /> kullan. Bunu makinenin o anda tükettiği EU/t'den çıkarsama.

Makine sıcaklığı tarif gereksiniminin altındaysa daha fazla güç tarifi başlatmaz. On altı bobinin tümünü aynı kademeyle değiştir ve bitişik makinelerle paylaşılan bobinleri de kontrol et.

### Fazla Isının Faydaları

Tarif gereksiniminin her 900 K üzeri, çarpımsal olarak %5 daha fazla güç indirimi sağlar. Her 1800 K, bir normal hız aşırtmanın kusursuz hız aşırtmaya dönüşmesine izin verir. Kusursuz hız aşırtma EU/t'yi yine dörtle çarpar ama süreyi dörde böler, böylece o hız aşırtma tarif başına toplam enerjiyi artırmaz.

| Tarif gereksiniminin üzerindeki sıcaklık | Güç çarpanı | Kusursuz olabilecek hız aşırtma sayısı |
| --- | --- | --- |
| 900 K'den az | %100 | 0 |
| 900–1799 K | %95 | 0 |
| 1800–2699 K | 0,95 × 0,95 = %90,25 | 1 |
| 2700–3599 K | 0,95³ ≈ %85,74 | 1 |
| 3600–4499 K | 0,95⁴ ≈ %81,45 | 2 |

Örneğin bir HV Enerji Kapağı ve Nikrom Bobinler 3701 K verir. 1300 K gerektiren bir alüminyum tarifinde 2401 K fazla ısı vardır; bu iki %5'lik güç indirimi sağlar ve bir kusursuz hız aşırtmaya izin verir. Ortaya çıkan tarif gücü ve süresi için NEI'yi ve makine ekranını kontrol et.

Kusursuz hız aşırtmalar, güç kaynağının zaten desteklediği hız aşırtmaları iyileştirir. Fazla ısı ek güç yaratmaz. Önce erken makineyi güvenilir şekilde çalıştır, ardından daha iyi bobinlerin, daha fazla gücün ve ek EYF'lerin maliyetlerini karşılaştır.

## Duvar Paylaşımı ve Otomasyon

<GameScene interactive={true} width="240" height="240" zoom="1.2" wrap="square" align="right">
  <ImportStructure src="/assets/structures/quad_ebf.snbt" />
  <ImportStructure src="/assets/structures/side_qebf.snbt" x="-8" />
  <RemoveBlocks id="Railcraft:residual.heat" />
</GameScene>

Birden fazla EYF yan duvar kasalarını ve bobinlerini paylaşabilir. 2×2 düzeninde dört tanesi, bağımsız yapılar için gereken 64 bobini 42'ye düşürür. Paylaşılan bobinler bağlı her makinenin kademe gereksinimini karşılamalıdır, bu yüzden yükseltme yaparken etkilenen tüm EYF'leri kontrol et.

Bakım Kapakları ve bazı giriş/çıkış arayüzleri de paylaşılabilir. Güç, aynı anda çalışan tüm makineleri karşılamalıdır. Paylaşılan Enerji Kapakları makinelerin amperaj için rekabet etmesine yol açar; bu da özellikle iki kapaklı kademe atlama kullanırken güç kesintilerine neden olma olasılığı yüksektir.

Otomasyon için toz, devre ve sıvı girişlerini düzenle ve sıcak külçeler, normal eşyalar ve sıvılar için yeterli çıkış alanı bırak. Bir EYF bir Vakum Dondurucuyu besliyorsa küçük bir partiyle test et ve ona yalnızca soğutma gerektiren sıcak külçelerin ulaştığını doğrula. Giriş filtrelemesi, eşya taşıma ve depolama ayarları için [Vakum Dondurucu rehberine](./vacuum_freezer.md#hot-ingot-routing) bak.

Birden fazla Giriş Yolu varsa kontrolcünün **giriş ayrıştırması** ayarını kontrol et. Etkinleştirildiğinde her yolun eşyaları ayrı bir tarif grubu olarak değerlendirilir. Bir tarif için gereken tozları ve devreyi birlikte eşleştirebilecek bir yolda tut. Farklı tarifler için ayrı yollar ve devreler, istenmeyen tarif eşleşmelerini azaltabilir.

Bir Vakum Dondurucu edinmeden önce normal külçe üreten ve sonraki işlemesi senin için mevcut olan tariflere öncelik ver. Daha sonra EYF'leri alüminyuma, çeliğe ve yüksek sıcaklık malzemelerine ayırabilirsin. Bobinleri paylaşan dört EYF yapı malzemesinden tasarruf sağlar, ancak aynı anda çalışma yine de dördü için yeterli güç gerektirir.

## Sorun Giderme

| Belirti | Neye bakmalısın |
| --- | --- |
| Yapı tamamlanmamış | On altı bobinin tümü aynı kademede; iki orta merkez hava; Egzoz Çıkışı üst merkezde; tabanda Enerji Kapakları, bir Bakım Kapağı ve giriş/çıkış arayüzleri var |
| Yeni makinede bakım sorunları var | Bakım Kapağında altı aletin tümüyle onar, ardından kontrolcüde doğrula; yapıyı oluşturmak ve bakımı tamamlamak ayrı adımlardır |
| Yetersiz sıcaklık | Gerçek sıcaklığı tara ve bobin kademesini, güç yapılandırmasını ve tarifin NEI'deki sıcaklık gereksinimini kontrol et |
| Malzemeler var ama tarif bulunamıyor | Malzeme türlerini ve miktarlarını, devre ayarını, sıvıları ve EU/t'yi kontrol et; giriş ayrıştırması açıksa gereken eşyaların yollara bölünmediğinden emin ol |
| Yetersiz gerilim veya güç | Erken bir yapıda iki LV Enerji Kapağı veya yükseltilmiş tarifler için uygun kapaklar olup olmadığını kontrol et; Giriş Yolu kademesi makine gerilimini belirlemez |
| Makine başladıktan hemen sonra duruyor | Üretimi, kablo kapasitesini ve kaybını ve kapaklara sürekli güç gidip gitmediğini kontrol et; test etmek için pahalı malzemeleri tekrar tekrar koyma |
| Makine kısa süre çalışıp sonra güç kaybediyor | Pil ve kapak tamponlarının sürekli düşüp düşmediğini izle; kazan buhar çıkışını, boru dağıtımını, diğer yükleri ve bakımı kontrol et |
| Dört yuvalı bir Pil Tamponu yetersiz güç veriyor | Dört kullanılabilir ve şarjlı LV pil, doğru çıkış yüzü ve yeterli ortalama üretim olup olmadığını kontrol et |
| Yetersiz çıkış alanı | Uygun Çıkış Yollarının ve Çıkış Kapaklarının var olduğunu, dolu olmadığını ve tarif çıktısının tamamını alabildiğini kontrol et |
| Kirlilik dışarı atılamıyor | Egzoz Çıkışının havaya menfez açtığını ve gelişmiş bir Egzoz Çıkışının gereken Hava Filtresine sahip olduğunu kontrol et |
| Kablolar yanıyor veya Enerji Kapakları patlıyor | Kablo gerilim ve amperaj sınırlarını, Enerji Kapaklarındaki aşırı gerilimi ve yağmura maruz kalmayı kontrol et |

Genel kurallar için [Multiblok Makineler](/gtnh_basics/multiblocks.md) sayfasına bak. Malzeme talebi arttıkça ek EYF'ler, yalnızca tek bir makinenin tekrarlanan hız aşırtmalarına güvenmek yerine iş yükünü bölebilir.

## Kaynaklar

- [GTNH Wiki: Elektrikli Yüksek Fırın](https://wiki.gtnewhorizons.com/wiki/Electric_Blast_Furnace)