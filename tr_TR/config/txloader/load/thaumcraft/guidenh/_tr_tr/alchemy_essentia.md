---
item_ids:
  - Thaumcraft:blockMetalDevice:0
  - Thaumcraft:blockStoneDevice:0
  - Thaumcraft:blockMetalDevice:1
navigation:
  title: Simya ve Esans
  parent: ./index.md
  icon: 'Thaumcraft:blockMetalDevice:0'
  position: 60
---

# Simya ve Esans

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**Simya**, materyallerdeki aspektleri kullanarak onları sihirli materyallere, yakıtlara ve araştırma için gereken eşyalara dönüştürür.<br>
İnfüzyon ve sihirli cihazlar kullanılabilir hale geldikçe, bu aspektler <Color color="#B7A0D6">esans</Color> olarak da çıkarılabilir; böylece bunları depolayan, dağıtan ve talep üzerine sağlayan bir üretim sistemi oluşur.

GTNH'de simya, teknolojik materyallerin işlenmesine de katkıda bulunur. Dönüşümü, simyevi çoğaltma ve ilgili araştırmalar materyal dönüştürme tarifleri sağlarken, sihirli cihazlar ve eklentiler esansın kullanım alanlarını genişletir.<br>
Tek tek tarifler için NEI ve Thaumonomicon'a bak.

## Potlar ve Simya Tarifleri

<ItemLink id="Thaumcraft:blockMetalDevice:0" showIcon="left" />, yerleştirilmiş bir Kazan'a asa kullanılarak oluşturulan temel simya tesisidir.<br>
1000 mB su alır ve altında sürekli bir ısı kaynağı gerektirir. Su kaynayıp kabarcıklar göründüğünde, malzemeleri çözebilir ve tarifleri gerçekleştirebilir.<br>
Su, sıvı borularıyla sağlanabilir. Ateş, lav veya <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" /> ısı sağlayabilir.

Pota'ya eklenen malzemeler aspektlerini katar. Gerekli aspektler mevcut olduğunda, uygun **katalizörü** eklemek bu aspektleri tüketir ve sonucu üretir.<br>
Katalizör kullanımı araştırmaya ve tarif koşullarına bağlıdır. Bir tarif gerçekleştirilemediğinde, aspekt içeren bir katalizör de çözülebilir.

- <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" /> ışık sağlar; Potları ve Thaumatorium'ları ısıtabilir.
- <ItemLink id="Thaumcraft:ItemResource:0" showIcon="left" />, Simya Fırını'nda esans damıtmasını da hızlandıran simyevi bir yakıttır.
- <ItemLink id="Thaumcraft:ItemResource:2" showIcon="left" />, Dengeli Parçalar ve diğer simyevi materyaller sonraki cihazlarda ve sihirli eşyalarda yaygın olarak kullanılır.

Her başarılı Pota tarifi 50 mB su tüketir. Üretimden sonra kalan aspektler diğer tarifler için kullanılabilir kalır.<br>
<ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> takmak türlerini ve miktarlarını gösterir.

GTNH, su bittiğinde bir yığın katalizörün işlenmesine yönelik bir düzeltmeyi etkinleştirir ve su tükendiğinde daha fazla üretimi durdurur. Toplu işlem yaparken, katalizörlerin çözülmesini önlemek için kalan aspektleri ve araştırma gereksinimlerini takip et.

## Artık Aspektler ve Flux

Pota'daki aspektler zamanla bozunur. Her bozunma, bileşik bir aspekti bileşenlerinden birine dönüştürürken temel aspektler kaybolur.<br>

Bu süreç <Color color="#B7A0D6">Flux</Color> üretebilir.

Pota toplamda 100 aspekt puanından fazlasını içerdiğinde, kayıplar ve Flux taşmaları sıklaşır.
GTNH ayrıca 200 puanın üzerinde ek bozunmayı etkinleştirir; miktar, fazlalık arttıkça artar.<br>
Aynı eşyanın büyük partileri için bir Thaumatorium tüketimi kontrol etmeyi kolaylaştırır.

Malzemeleri ilgili tariflerin gereksinimlerini göz önünde bulundurarak seç ve artan aspektleri başka bir ürün için kullan. Pota'da uzun süre kalan kalıntıları azaltmak için girdi miktarlarını planlanan üretim sayısından hesapla.

> [!WARNING]
> Bir Pota'ya asa ile eğilip sağ tıklamak suyunu ve aspektlerini boşaltır, Flux açığa çıkarır. Hem büyük fazlalıkların bozunması hem de Pota'nın boşaltılması çevreyi kirletebilir. Simya alanında Flux arıtımı için yer bırak.

Bir <ItemLink id="Thaumcraft:blockStoneDevice:14" showIcon="left" /> yakındaki Flux Gazı ve Flux Yapışkan Madde'yi temizler, Aer enerjisi gerektirir ve bir miktar esans geri kazanabilir.<br>
Çoktan yayılmış Taint, uygun arıtma tesisleri gerektirir.

## Thaumatorium

**Otomatik Simya** araştırmasını tamamladıktan sonra, bir Pota ve iki <ItemLink id="Thaumcraft:blockMetalDevice:9" showIcon="left" /> bloklarından oluşan bir yapı, asa ile etkinleştirilerek bir Thaumatorium oluşturulabilir.<br>
Simyevi materyallerin tekrarlanan üretimine uygundur ve her tarifin gerektirdiği esans miktarlarını harici kaynaklardan çeker.

- **Çalışma gereksinimleri:** Hâlâ altında bir ısı kaynağına ihtiyaç duyar, ancak su gerektirmez.
- **Tarif seçimi:** Bir katalizör eklemek, arayüzde ilgili tarifleri listeler; buradan açılmış bir sonuç seçebilirsin.
- **Esans beslemesi:** Mevcut tarifin istediği aspektleri sağlamak için uyumlu bir bağlantı noktasına borular veya bir Esans Sağlayıcı bağla.
- **Ürün çıktısı:** Ürünler üst ön kısımdaki küçük açıklıktan çıkar. Bu açıklığın önüne yerleştirilen bir envanter bunları doğrudan alabilir.
- **Tarif hafızası:** Normalde bir etkin tarif tutar. Her <ItemLink id="Thaumcraft:blockMetalDevice:12" showIcon="left" /> iki tane daha ekler.

Thaumatorium, katalizör girişinin, esans beslemesinin ve ürün toplamanın lojistik sistemlerine ayrı ayrı bağlanmasına olanak tanır. Birkaç ürün aynı katalizörü paylaştığında, özellikle otomatik üretim kullanırken hangi tariflerin etkin olduğunu kontrol et.

## Esans Damıtması

Bir <ItemLink id="Thaumcraft:blockStoneDevice:0" showIcon="left" /> eşyaları esansa ayrıştırır; üzerindeki <ItemLink id="Thaumcraft:blockMetalDevice:1" showIcon="left" /> bunları aspekte göre ayırır. Tek bir fırına en fazla beş imbik üst üste konabilir.

- **Fırın tamponu:** Toplam 50 puan, birden çok aspekt arasında paylaşılır.
- **İmbik tamponu:** Her biri 32 puan, aynı anda tek tür esans tutar.
- **Malzeme girişi:** Ayrıştırılacak eşyaları fırının yanlarından besle.
- **Yakıt girişi:** Alttan katı yakıt sağla. Alumentum damıtmayı hızlandırır.

Daha fazla aspekt içeren eşyaların ayrıştırılması daha uzun sürer. Bir eşyanın toplam aspekt içeriği fırının kalan tampon alanını aşarsa, fırın işlemeye devam edemez.<br>
İmbiklerde kalan esans da çıktıyı engelleyebilir; bu yüzden sürekli üretim bir toplama sistemi gerektirir.

Bir imbiğe esans kavanozuyla sağ tıkla; kavanozun içeriğiyle uyumlu esansı topla.<br>
Bir <ItemLink id="Thaumcraft:ItemEssence:0" showIcon="left" /> aynı anda 8 puan toplar ve imbikte 8 puandan az varsa doldurulamaz.<br>
Otomatik toplama borular, simya golemleri veya Thaumic Energistics'in Esans İçe Aktarma Veri Yolları'nı kullanabilir.

## Esans Malzemelerini Seçme

NEI'nin aspekt kaynak sayfaları malzeme bulmana yardımcı olur. Aspekt verimini, yan ürünleri, edinme maliyetini ve istikrarlı bir tedarik sürdürme yeteneğini göz önünde bulundur.

- **Ana talep:** İstenen aspektin eşya başına miktarını ve fırının onu işleme süresini karşılaştır.
- **Diğer aspektler:** Aynı malzemenin ürettiği diğer esans için depolama veya bir çıkış sağla. Dolu bir yan ürün deposu tüm üretim hattını durdurabilir.
- **Güvenilir kaynaklar:** Çiftlikler, ağaç çiftlikleri, yaratık düşmeleri ve mevcut işleme hatlarının yan ürünleri sürekli damıtmaya uygundur.
- **İşlenmiş formlar:** Aynı materyalin farklı eşya formları farklı aspektler içerebilir. Malzemeleri mevcut işleme tesislerine göre seç.

<Color color="#B7A0D6">Sihir (Praecantatio)</Color>, Metal (Metallum) veya Yaşam (Victus) gibi esanslar için aspekte göre aday malzemeler bul, ardından genel çıktılarını karşılaştır. Esans sistemi kurulduktan sonra, sık kullanılan malzemeler için ayrı girdiler belirli stokları yenilemeyi kolaylaştırır.

## Kavanozlar, Etiketler ve Şişeler

Bir <ItemLink id="Thaumcraft:blockJar:0" showIcon="left" /> tek tür esanstan 64 puan tutar ve kırıldığında içeriğini korur. Kavanozlar taşıma, cihazlar için malzeme hazırlama ve aspekte göre sıralanmış daha küçük depolama alanları oluşturma için kullanışlıdır.

Bir <ItemLink id="Thaumcraft:ItemResource:13" showIcon="left" /> bir kavanozu belirli bir aspekte kilitler. Bir aspekte atanmış bir etiket boş bir kavanoza da uygulanabilir. Etiketler boru sistemlerinde emiş önceliğini etkiler:

- Etiketsiz sıradan bir kavanoz 32 emişe sahiptir.
- Etiketli sıradan bir kavanoz dolana kadar 64 emişe sahiptir, ardından esans çekmeyi durdurur.
- Bir <ItemLink id="Thaumcraft:blockJar:3" showIcon="left" /> dolduktan sonra fazla esansı kabul etmeye ve yok etmeye devam eder. Etiketlendiğinde dolana kadar 48 emişe sahiptir, ardından 32'ye düşer.

Boşluk Kavanozları zamanla fazla kalan yan ürünler için bir çıkış sağlar. Boru ağlarında, etiketli sıradan kavanozlar genellikle önce dolar. AE depolama sistemlerinde, Depolama Veri Yolu önceliğini ve Boşluk Kavanozlarını kullanma seçeneğini yapılandır.

Cam Şişeler ve Esans Şişeleri, dolu şişe başına 8 puan tutar; bu da onları küçük miktarları taşımak ve aktarmak için kullanışlı kılar. Ayrıca bazı tariflerde ve etiketlere aspekt atamak için kullanılırlar.

> [!WARNING]
> Bir kavanoza veya imbiğe boş elle eğilip sağ tıklamak esansını temizler. Bir kavanozun etiketli yüzüne tıklamak etiketi kaldırır; başka bir yüze tıklamak kavanozu boşaltabilir. Bir Boşluk Kavanozu tarafından kabul edilen fazla esans da kalıcı olarak kaybolur.

## Esans Boruları ve Emiş

Bir <ItemLink id="Thaumcraft:blockTube:0" showIcon="left" /> esans akışını belirlemek için <Color color="#B7A0D6">emiş</Color> kullanır. Bir alıcı cihazın emişi borular boyunca kaynağa doğru yayılır ve her sıradan boru parçasında 1 puan kaybeder. Esans, daha yüksek emişe sahip uyumlu bir alıcıya doğru hareket eder.

Her sıradan boru parçası aynı anda yalnızca tek tür esans tutar ve tek bir emiş türüne yanıt verir.<br>
Farklı aspektler için etiketli kavanozlar aynı hattı paylaştığında, istekleri birbirine karışabilir; bu da akışın durmasına veya dışarı atılmaya yol açabilir. Filtreler ve valfler, isteklerin yayılmasını sınırlayarak tek tek dalların amaçlandığı gibi çalışmasını sağlayabilir.

Yönlendirme ve kontrol için yaygın bileşenler şunlardır:

- <ItemLink id="Thaumcraft:blockTube:3" showIcon="left" />: Etiketlendiğinde yalnızca seçilen esansın geçmesine izin verir.
- <ItemLink id="Thaumcraft:blockTube:1" showIcon="left" />: Manuel olarak veya kızıltaş ile açılıp kapanır; geçici olarak kullanılmayan dalları izole eder.
- <ItemLink id="Thaumcraft:blockTube:6" showIcon="left" />: Aktarım yönünü kısıtlar, dallar arasında geri akışı önlemeye yardımcı olur.
- <ItemLink id="Thaumcraft:blockTube:5" showIcon="left" />: Yayılan emişi yarıya indirerek dallar arasındaki rekabeti ayarlar.
- <ItemLink id="Thaumcraft:blockTube:4" showIcon="left" />: Birden çok esans türü arasında toplamda 8 puan geçici olarak depolar. Varsayılan emişi düşüktür; Esrarengiz Körükler takmak bunu artırır.

Bir <ItemLink id="Thaumcraft:ItemResonator" showIcon="left" /> cihazlardaki veya borulardaki esans türünü, miktarını ve emişi okur.<br>
Akış durduğunda, emişin nerede kesildiğini veya aspekt isteklerinin nerede çakıştığını bulmak için kaynağı, boruları ve alıcıyı incele.

Tek tek aspektler için ayrılmış hatları dengeli tutmak daha kolaydır. Birden çok aspekti işleyen sistemler için tamponlar ve kontrollü dallar kullan veya ana depolama ve dağıtımı Thaumic Energistics'in yönetmesine izin ver.

## Santrifüjleme ve Diğer Taşıma Seçenekleri

Bir <ItemLink id="Thaumcraft:blockTube:2" showIcon="left" /> alttan bileşik esans alır ve üstten bileşen aspektlerinden birini çıkarır.<br>
Tüketilen her bileşik esans puanı, rastgele seçilen bir bileşenin 1 puanını üretir; bu bileşen kendisi de hâlâ bileşik bir aspekt olabilir.

Bu, mevcut bileşik esansın daha temel aspektleri yenilemesini sağlar. Santrifüjün üzerine bir Esans Tamponu bağla, ardından iki olası çıktıyı ayrı dallara yönlendir. Daha ileri ayrıştırma, birden çok aşama ve uygun çıktı yönetimi gerektirir.

- **Simya golemleri:** Kaynaklar ve kavanozlar arasında esans taşır; birkaç konuma yayılmış depolama alanlarına hizmet eder. Menzil, görevlendirmeler ve yükseltmeler için golem araştırmasına bak.
- <ItemLink id="Thaumcraft:blockMirror:6" showIcon="left" />: Bağlantılı çiftler, yakındaki kaynaklardan çeken Rünik Matrisler'e ve diğer cihazlara uzaktaki esansı sağlar.
- <ItemLink id="Thaumcraft:blockTube:7" showIcon="left" />: Esansı, eşya olarak depolamak ve taşımak için Ruhani Esanslara yoğunlaştırır.

## Thaumic Energistics ve Esans Otomatik Üretimi

Thaumic Energistics, esansı bir ME ağda depolar; stokları yönetmek için **Esans Depolama Hücreleri** ve bir **Esans Terminali** kullanır. Yaygın arayüzleri şunlardır:

- **Esans İçe Aktarma Veri Yolu:** İmbiklerden, kavanozlardan ve diğer cihazlardan esansı ağa aktarır.
- **Esans Dışa Aktarma Veri Yolu:** Yapılandırılmış esans türlerini harici cihazlara veya kaplara sağlar.
- **Esans Depolama Veri Yolu:** Harici esans kaplarını ağın envanterinin parçası yapar; mevcut kavanoz depolamasını birleşik yönetim altına alır.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.essentia.provider" showIcon="left" />: Esans borusu bağlantılarıyla çalışır; Thaumatorium'ların ve benzer cihazların esansı ağdan almasını sağlar. Ayrıca bitişik kaynaklardan esans toplayabilir ve 8 emişe sahiptir.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.infusion.provider" showIcon="left" />: Ağdaki esansı Rünik Matrisler'e ve yakındaki kaynaklardan çeken diğer cihazlara sağlar.

<ItemLink id="thaumicenergistics:thaumicenergistics.block.distillation.encoder" showIcon="left" />, eşya damıtmasını esans otomatik üretim kalıplarına kodlar.<br>
Kodlarken gerçek bir eşya ve aspekt bilgisini kullan, istediğin esans çıktılarını seç ve kalıbı ME otomatik üretim sistemine ver.<br>
Damıtma hattı malzemeleri alır ve çıkarılan esansı ağa geri döndürür.

Bu, eksik esansın talep üzerine üretilmesini sağlar. Aynı malzemeden gelen diğer aspektlerin yine de toplanması gerekir. Sık kullanılan bir aspekti düzenli olarak yenilerken, zamanla biriken yan ürünler için depolama veya bir çıkış sağla.

Bir Boşluk Kavanozunu Esans Depolama Veri Yolu üzerinden bağlarken, veri yolu arayüzünde ilgili seçeneği aktifleştir ve normal depolamanın esansı önce alması için daha düşük bir öncelik ayarla.

## Esans Üretimini Artırmak

Talep arttıkça, mevcut depolama ve dağıtım sistemini koruyarak çıkarma cihazlarını yükseltebilirsin:

- <ItemLink id="thaumicbases:advAlchFurnace" showIcon="left" />: Daha hızlı işleme sahip sıradan Simya Fırını'nın bir yükseltmesi. Hâlâ üzerindeki Esrarengiz İmbikler aracılığıyla çıktı verir ve körük kullanabilir.
- <ItemLink id="Thaumcraft:blockAlchemyFurnace" showIcon="left" />: Primordial İnci içeren bir araştırma gerektirir, 500 puanlık bir esans tamponuna sahiptir ve Ignis, Perditio ve Aqua Centi-Vis kullanır.
Eşyalar üstteki açıklıktan girer ve alt portlar esans çıkarır. Bir Eşya Izgarası, eşya lojistiği kullanarak malzeme beslemeyi kolaylaştırır.
- **Büyük Esans Dökümhanesi:** Elektrik ve Centi-Vis gerektiren GT'nin büyük ölçekli çıkarma makinesi. Esans Çıkış Kapakları veya ME Esans Çıkış Kapakları onu sonraki sistemlere bağlar. Yapısı ve Difüzyon Hücreleri işleme performansını etkiler.

Çıkarma hızını artırırken imbiklerin ve esans arayüzlerinin verimini de kontrol et. Esans bir çıkarma cihazının tamponunda uzun süre kalıyorsa, önce çıktı ve depolamayı ele al.

Gelişmiş Simya Fırını sıcaklığını korumak için Ignis kullanır ve boştayken bile bunu tüketir. Perditio ve Aqua işleme sırasında kullanılır.<br>
Centi-Vis kaynakları, bağlantıları ve çıktısı için [Asalar, Vis ve Düğümler](./wands_vis_nodes.md) sayfasına bak.

## Yaygın Sorunlar

- **Pota'ya malzeme ekledikten sonra çıktı yok:** Suyun kaynayıp kaynamadığını, araştırmanın tamamlanıp tamamlanmadığını, katalizörün uyup uymadığını ve gerekli aspektlerin bozunup bozunmadığını kontrol et.
- **Katalizörler çözülüyor:** Kalan aspektleri ve araştırma gereksinimlerini kontrol et. Partiler için suyu ve başarılı üretim sayısını takip et.
- **Simya Fırını işlemeyi durduruyor:** Yakıtı, kalan tampon alanını ve imbiklerin boşaltılıp boşaltılmadığını kontrol et. Bir malzemenin toplam aspekt içeriği kalan tampon alanını da aşabilir.
- **Bir esans türü hiç akmıyor:** Emişi ve aspekt türlerini incelemek için bir Esans Rezonatörü kullan, ardından etiketleri, filtreleri, valfleri ve rakip dalları kontrol et.
- **Bir Thaumatorium'da katalizörler var ama çalışmıyor:** Isı kaynağını, etkin tarifleri ve her gerekli aspekt için besleme yolunu kontrol et.
- **Bir esans hattı periyodik olarak duruyor:** Dolu yan ürün depolarını, mevcut ağ depolama alanını ve arayüz verimini kontrol et.
- **AE'de esans var ama bir cihazda hâlâ eksik:** Arayüzün hedef cihaza uyup uymadığını, ağ gücü, kanallar ve yapılandırmayla birlikte kontrol et.

<br>
</Column>