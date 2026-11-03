---
item_ids:
  - Thaumcraft:blockStoneDevice:2
  - Thaumcraft:blockStoneDevice:1
navigation:
  title: İnfüzyon Üretimi
  parent: ./index.md
  icon: 'Thaumcraft:blockStoneDevice:2'
  position: 50
---

# İnfüzyon Üretimi

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**İnfüzyon Üretimi**, asa bileşenleri, sihirli cihazlar, ekipman ve mod entegrasyonu için materyaller oluşturmak üzere esansı ve çevredeki malzemeleri merkezi bir eşyaya infüze eder.<br>
Araştırma ilerledikçe aynı sunak ekipman yükseltmelerini ve infüzyon büyülemesini de gerçekleştirebilir.

Bir İnfüzyon Sunağı kullanmak <Color color="#B7A0D6">tarifler, denge ve esans tedariki</Color> konularına dikkat etmeyi gerektirir.<br>
GTNH'de Thaumic Energistics, İnfüzyon Pençeleri, İnfüzyon Engelleyicileri ve diğer cihazlar tedarik ve aktivasyonu yönetebilir; böylece sunak sürekli üretimi destekleyebilir.

## İnfüzyon Sunağı

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/infusion_altar.snbt" />
</GameScene>

Sunak ana yapısı bir <ItemLink id="Thaumcraft:blockStoneDevice:2" showIcon="left" />, merkezi bir <ItemLink id="Thaumcraft:blockStoneDevice:1" showIcon="left" /> ve dört sütundan oluşur. Sütunlar <ItemLink id="Thaumcraft:blockCosmeticSolid:6" showIcon="left" /> ve <ItemLink id="Thaumcraft:blockCosmeticSolid:7" showIcon="left" /> ile inşa edilir; asa ile etkinleştirildiklerinde İnfüzyon Sütunlarına dönüşürler.

Merkezi kaide, matrisin tam iki blok altında yer alır ve infüze edilen eşyayı tutar. Çevresindeki ek kaideler tarif malzemelerini tutar. Sahne, etkinleştirilmiş bir sunağı ve tariflere uyacak şekilde genişletilebilen bir dizi dış kaideyi gösterir.

- **Yapı aktivasyonu:** İnfüzyon araştırmasını tamamla, Thaumonomicon'da gösterilen yapıyı inşa et ve asa ile matrise sağ tıkla. Ana yapı içindeki boş alanları açık bırak; lojistik cihazlar aktivasyondan sonra bağlanabilir.
- **Dış kaide menzili:** Kaideler matrisin altında, X ve Z yatay eksenlerinin her biri boyunca 8 blok içinde ve matrisin en fazla 10 blok altında olmalıdır.
- **Kaide katmanları:** Her dikey sütunda yalnızca bir dış kaide tanınır. Birden fazla katman kullanırken yatay konumlarını kaydır.
- **Alan ayırma:** Merkezi kaidenin altında esans bağlantısı, çevredeki kaidelerin altında ise eşya lojistiği için yer bırak. Matrisin üstüne bir İnfüzyon Pençesi kurulabilir.

## Tarifler ve Üretim Süreci

Bir infüzyon tarifi merkezi bir eşya, dış malzemeler, belirtilen esans ve onu etkinleştiren oyuncu tarafından tamamlanmış ilgili araştırmayı gerektirir. Thaumonomicon ve NEI, mevcut tarifin eşyalarını, esans miktarlarını ve dengesizliğini gösterir.

Standart bir sunak önce esansı çeker, ardından dış malzemeleri tek tek emer. Bitmiş eşya merkezi kaidede kalır. Türleri ve miktarları tarife uyduğu sürece dış malzemelerin konumları yeniden düzenlenebilir.

> [!WARNING]
> Standart bir sunak, başlamadan önce gerekli tüm esansın mevcut olup olmadığını kontrol etmez. Eksik esans veya kaidelerden düşen malzemeler, risk kontrolleri devam ederken ayini durdurur; bu da dengesizliği veya esans gereksinimlerini artırır. Üretimden önce esansı ve malzemeleri hazırla ve sunak dengesini kontrol et.

Her dış malzeme girdisi ayrı bir kaide kaplar. Bir tarif aynı malzemeyi birkaç kez gerektirdiğinde, eşleştirme için birden fazla kaide gerekir. Geri dönen kaplar veya yeniden kullanılabilir malzemeler kaidelerinde kalabilir; yığın üretim için toplanmalarını düzenle.

## Kaide Düzeni ve Denge

Sunak <Color color="#B7A0D6">merkezi simetriyi</Color> kontrol eder: aynı yükseklikteki iki konum, matrisin dikey ekseni etrafında 180° döndürüldüğünde birbirine karşılık gelir. Örneğin, matrisin üç blok doğusunda ve bir blok kuzeyindeki bir kaide, üç blok batısında ve bir blok güneyindeki bir kaideyle eşleşir.

- **Kaideleri eşleştir:** Her dış kaidenin karşı tarafta karşılık gelen bir kaidesi olmalıdır. Boş kaideler de simetriye dahil edilir.
- **Dolu konumları eşleştir:** Karşılıklı iki kaide, ikisi de malzeme tuttuğunda dengede kalır; malzemeler farklı eşyalar olabilir. Ek dengeleyiciler, tek sayıda malzemenin yol açtığı doluluk dengesizliğini telafi edebilir.
- **Kullanılmayan malzemeleri kaldır:** Menzil içindeki diğer kaidelerdeki eşyalar tarif eşleştirmesine katılır. Başka bir üretimden kalan malzemeleri bırakmak tarifin tanınmasını engelleyebilir.
- **Ayarlamalardan sonra kontrol et:** Kaide ekledikten veya kaldırdıktan, dengeleyicileri taşıdıktan ya da eklenti cihazlarını bağladıktan sonra Esrarengiz Abaküs kullan.

Tarifin dengesizliği ve sunağın çevresel değiştiricisi birlikte ayinin başlangıç riskini belirler. Dengeleyiciler hedef tarifin riskini dengelemeli ve eksiklikler ile otomatik aktivasyon cihazları için pay bırakmalıdır.

Bir <ItemLink id="WitchingGadgets:item.WG_Material:7" showIcon="left" /> matrisin dengesini okur, eşleşmemiş dengeleyicileri belirler ve mevcut veya kullanılabilir tarif için risk ve esans maliyeti bilgilerini gösterir.<br>
Önce kaideleri ve dengeleyicileri düzenle, ardından sonucu kontrol etmek için hedef tarifin malzemelerini yerleştir.

## Dengeleyicileri Yerleştirme

Dengeleyiciler arasında mumlar, kafatasları, kristaller ve eklentilerden uygun bloklar bulunur. Bir İnfüzyon Sunağını dengeleyebileceklerini belirten bir ipucuna sahip bloklar NEI'de bulunabilir ve sunağın çevresinde kullanılabilir.

Bir <ItemLink id="thaumicbases:quicksilverBlock" showIcon="left" /> GTNH'de yaygın bir seçimdir ve birden fazla dengeleyici katmanına sahip bir temel için uygundur. Mevcut materyallere göre mumlar, kafatasları ve diğer geçerli dengeleyiciler de kullanılabilir.

- **Etkili menzil:** X ve Z eksenlerinin her biri boyunca 12 bloğa kadar, matrisin 5 blok üstüne ve 10 blok altına kadar.
- **Eşleştirme:** Geçerli dengeleyicileri matrise göre merkezi simetrik konumlarda aynı yüksekliğe yerleştir. Eşleşmemiş dengeleyiciler dengesizliği artırır.
- **Birden fazla katman:** Her katmanın kendi simetrisi olmalıdır. Zemin seviyesinde erişim ve lojistik için yer bırakmak üzere dengeleyiciler sunağın altına yerleştirilebilir.
- **Merkezi sütun:** Matrisin doğrudan üstündeki ve altındaki dikey sütun, olağan dengeleyici simetri kontrollerinden hariç tutulur.

Çiftler halinde yerleştirilen her 10 sıradan dengeleyici toplamda 1 denge puanı sağlar. Daha büyük temeller için her katmanın sınırını eksiksiz tut ve eksik blokları bulmak için Esrarengiz Abaküs kullan.

Dengeleyici menzili içindeki diğer geçerli bloklar da sayılır. Yakındaki süslemeler, başka bir sunağın dengeleyicileri ve sonradan eklenen bloklar mevcut sunağın dengesini etkileyebilir.

## Esans Tedariki

Standart bir sunak gerekli aspektleri matrisin yakınındaki esans kaynaklarından çeker. Her <ItemLink id="Thaumcraft:blockJar:0" showIcon="left" /> 64 puan tutar; bir aspektin gereksinimi bir kavanozu aştığında aynı türden birkaç kavanoz hazırla.

- **Kavanoz tedariki:** Küçük bir tarif grubu veya ara sıra yapılan infüzyonlar için uygundur. Gerekli her aspekti ayrı ayrı hazırla.
- <ItemLink id="Thaumcraft:blockMirror:6" showIcon="left" />: Bağlantılı çiftler sunağa uzak bir depolama alanından esans sağlar.
- <ItemLink id="thaumicenergistics:thaumicenergistics.block.infusion.provider" showIcon="left" />: Bir ME Ağına bağlandığında sunağın ağ stoklarından esans çekmesini sağlar. Kavanoz taşımayı azaltmak için onu sunağın çekme menzili içine yerleştir.

Gerekli bir aspekt stokta yoksa, bir İnfüzyon Sağlayıcısı 32 puanlık yığınlar halinde esans otomatik üretimi talep edebilir.<br>
Bu, kullanılabilir bir desen ve üretim CPU'su gerektirir. Yaygın aspektleri stokta tutmak sürekli infüzyon sırasındaki beklemeyi azaltır.

Standart bir matris yine de esansı ardışık adımlarla çeker. Daha fazla aspekt türü ve daha büyük miktarlar bu aşamayı uzatır. Yüksek esans talebi olan tarifler bir İnfüzyon Engelleyici veya Gelişmiş İnfüzyon Sağlayıcısı kullanabilir.

Üretim, depolama ve taşıma için "Simya ve Esans" bölümüne bak. Birkaç sunak stokları paylaştığında, eşzamanlı çalışma sırasında birleşik taleplerini hesaba kat.

## İnfüzyon Kazaları ve Kayıplar

Dengesiz infüzyonlar malzemeleri kaidelerden düşürebilir, malzemeleri yok edebilir, Flux salabilir veya yakındaki varlıklara zarar verebilir.<br>
Eksik malzemeler üretimi geciktirir ve daha fazla kaza olasılığını artırır.

- **Yok edilen malzemeler:** Eksik eşyaları değiştir. Değerli tarifler için mümkünse yedek dış malzemeler hazırla.
- **Esans akışı durur:** Matrisin hâlâ hangi aspektlere ihtiyaç duyduğunu, kavanoz içeriklerini, sağlayıcı stoklarını ve tedarik yollarını kontrol et.
- **Esans talebi artar:** Ayinin şu anda gerektirdiği miktarları yenile ve eksikliği gider. Daha fazla beklemek ek kayıplara yol açabilir.
- **Flux sızıntıları:** Sunağın yakınına Flux temizleme cihazları yerleştir ve malzemeleri yenilemek ile eşyaları toplamak için erişim bırak.

> [!WARNING]
> Bir infüzyon kesintiye uğradığında zaten emilmiş esans ve malzemeler otomatik olarak geri verilmez. Merkezi eşyayı kaldırmak veya değiştirmek ayini sonlandırabilir. Otomatik ürün toplama da girdiyi erken çekmemek için üretim tamamlanana kadar beklemelidir.

Kazalar tekrarlanırsa, daha fazla malzeme tüketmeden önce sunak dengesini iyileştir ve tedarik sorunlarını çöz. Yüksek riskli tarifler için esans veya eksik malzemeler için harcanan bekleme süresini azalt.

## İnfüzyon Büyülemesi

**İnfüzyon Büyüsü** araştırmasını tamamladıktan sonra sunak, desteklenen büyüleri aletlere, silahlara ve zırhlara uygulayabilir. Bu tarifler eşya ve esansın yanı sıra tecrübe gerektirir ve bunu sunağın yakınındaki oyunculardan çeker.

- **Daha yüksek büyü seviyeleri:** İzin verilen maksimum seviyesine kadar aynı büyüyü tekrarla. Daha yüksek seviyeler daha fazla esans ve tecrübe gerektirir.
- **Mevcut büyüler:** Eşyadaki diğer büyüler kaynak maliyetlerini ve dengesizliği artırır. Kitaptaki temel gereksinimleri hedef eşyanın mevcut durumuyla karşılaştır.
- **Uygulanabilirlik ve uyumluluk:** Büyü kuralları, bir büyünün bir eşyaya uygulanıp uygulanamayacağını ve mevcut büyüleriyle birlikte var olup olamayacağını belirlemeye devam eder.

Bir ekipman seti hazırlarken, işlem sırasını istenen nihai büyülere göre planla ve mevcut eşyanın maliyetlerini kontrol etmek için Esrarengiz Abaküs kullan. Birkaç büyüye sahip ekipman, daha büyük denge payına sahip bir sunaktan yararlanır.

NH'nin eklentileri ayrıca Osmotik Büyüleyici ve Aşırı Büyüleme Masası gibi cihazlar sağlar. Tarifleri, kaynak maliyetleri ve seviye kuralları kendi araştırma girdilerinde açıklanmıştır.

## Otomatik Aktivasyon ve Eşya Lojistiği

Bir <ItemLink id="gadomancy:BlockInfusionClaw" showIcon="left" /> Rünik Matrisin üstüne kurulur. İçine bir asa veya büyük bir asa yerleştirildiğinde, yandan gelen bir kızıltaş sinyaliyle infüzyonu tetikleyebilir. Cihaz sahibine bağlıdır ve tarif tanıma için o oyuncunun araştırmasını kullanır.

İnfüzyon Pençesi, asası için Vis takviyesine ihtiyaç duyar ve bir Centi-Vis ağından güç alabilir.<br>
Etkinleştirdiği ayinlere dengesizlik ekler. Daha büyük kapasiteli bir asa veya uygun bir büyük asa bu etkiyi azaltır.

Eşya otomasyonu esas olarak aşağıdaki görevleri yönetir:

- **Merkezi eşya tahsisi:** Merkezi eşyayı ve dış malzemeleri atanmış kaidelerine gönder. Birkaç tarif bir sunağı paylaştığında doğru tahsis kurallarını koru.
- **Bireysel dış girdiler:** Aynı malzemenin tekrarlanan kullanımları dahil her malzeme girdisi bir kaide gerektirir.
- **Aktivasyon kontrolü:** Malzemeler yerleştikten sonra İnfüzyon Pençesini tetikle. Sürekli üretim için önceki üretimin bitmesini bekle.
- **Ürün toplama:** Bitmiş eşyayı tanımla ve merkezi kaideden çıkar. Dış kaidelerde kalan kapları veya yeniden kullanılabilir malzemeleri de ele al.

Bir ME Ağı girdileri ve ürünleri yönetebilir; kızıltaş, OC veya diğer kontrol cihazları aktivasyon ve toplamayı koordine eder.<br>
Sürekli üretimin durmasını önlemek için geri dönen kapları veya artık malzemeleri bir sonraki üretim başlamadan önce ele al.

Centi-Vis kaynakları ve bağlantıları için [Asalar, Vis ve Düğümler](./wands_vis_nodes.md) bölümüne bak.

## İnfüzyon Hızını Artırma

Bir <ItemLink id="thaumicinsurgence:infusionIntercepter" showIcon="left" /> doğrudan merkezi kaidenin altına kurulur ve esansı alt yüzünden alır.<br>
Gerekli esansı doğrudan ilgili Rünik Matrise göndermek için altına esans tüpleri veya bir Thaumic Energistics Esans Sağlayıcısı bağla.

Bir ME Esans Sağlayıcısı ve girdide yeterli stokla, çok büyük miktarlarda esansı çok hızlı sağlayabilir. Tüplerle gerçek tedarik hızı performansını sınırlar. Yalnızca doğrudan üstündeki sunağa hizmet eder; kurmadan önce ana sunak yapısını etkinleştir.

Bir <ItemLink id="thaumicenergistics:thaumicenergistics.block.advanced.infusion.provider" showIcon="left" /> etkin bir infüzyona gereken tüm esansı bir anda sağlar ve eksik miktarlar için otomatik üretim talep eder.<br>
X ve Z eksenlerinin her biri boyunca 12 blok ve dikey olarak 5 blok içindeki birden fazla matrise bağlanabilir.

- **İnfüzyon Engelleyicileri** bireysel sunaklar için hızlı esans tedariki sağlar.
- **Gelişmiş İnfüzyon Sağlayıcıları** birden fazla sunağın ağ stoklarını ve esans otomatik üretimini paylaşmasını sağlar.
- **Dünya Hızlandırıcıları** matris çalışmasını daha da hızlandırabilir, ancak önce yeterli denge ve tedariki sağla. Eksiklik sırasında hızlandırma, ayin durmuşken risk kontrollerini de hızlandırır.

Esans tedariki daha az zaman aldığında bile, dış malzemelerin tek tek emilmesi üretim süresine katkıda bulunmaya devam eder. Üretimi genişletmek için, her biri için eksiksiz girdi ve toplama kontrolüyle tarif ve malzeme sayısına göre birden fazla sunak düzenle.

## Sorun Giderme

- **Asa ile sağ tıklama infüzyonu başlatmıyor:** Yapı aktivasyonunu, araştırma tamamlanmasını, merkezi eşyayı ve dış malzemeleri ve menzil içinde kalan ilgisiz malzemeleri kontrol et.
- **Bazı dış malzemeler tanınmıyor:** Kaidelerinin matrisin altında, menzil içinde ve başka bir kaideyle aynı dikey sütunda olup olmadığını kontrol et.
- **Dengeleyicileri yerleştirdikten sonra risk hâlâ yüksek:** Asimetrik konumları, dengeleyici menzilini ve dolu dış kaideleri kontrol etmek için Esrarengiz Abaküs kullan. Bir İnfüzyon Pençesi kullanırken ondan gelen ek dengesizliği de hesaba kat.
- **İnfüzyon Pençesi tarifi başlatmıyor:** Sahibinin araştırmasını, yerleştirilen asayı, güç kaynağını ve kızıltaş tetikleyicisini kontrol et, ardından sunaktaki tarif malzemelerini doğrula.
- **Engelleyici esans sağlamıyor:** Doğrudan merkezi kaidenin altında olup olmadığını, alt yüzünün geçerli bir esans kaynağına bağlanıp bağlanmadığını ve kaynağın gerekli aspektleri içerip içermediğini kontrol et.
- **Otomasyon yalnızca ilk üretimi tamamlıyor:** Merkezi ürünün ve dış artıkların toplanmasını, bir sonraki malzeme setinin tahsisini ve aktivasyon sinyalinin yeniden tetiklenip tetiklenmediğini kontrol et.

</Column>