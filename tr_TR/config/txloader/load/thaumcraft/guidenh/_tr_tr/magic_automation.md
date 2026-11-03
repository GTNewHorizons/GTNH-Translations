---
item_ids:
  - Automagy:blockTally
  - Automagy:blockThirstyTank
  - Thaumcraft:blockMirror:0
navigation:
  title: Büyü Otomasyonu
  parent: ./index.md
  icon: 'Automagy:blockTally'
  position: 40
---

# Büyü Otomasyonu

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Thaumcraft ve **Automagy**; eşya toplama, envanter izleme, uzun mesafelere taşıma ve sıvı beslemesi için olanaklar sunar.<br>
Bir üretim sisteminin belirli kısımlarını yönetmek için mevcut borulara, ME ağlarına ve kızıltaş kontrollerine bağlanabilirler.

Başlıca kullanımları <Color color="#B7A0D6">toplama ve dağıtım, envanter koşulları, uzamsal taşıma ve üretim desteği</Color> alanlarındadır.

## Eşya Toplama ve Dağıtım

**Düşen eşyaları toplama**

<ItemLink id="Thaumcraft:blockChestHungry" showIcon="left" /> kendisine dokunan düşen eşyaları emer. Bir cihazın eşya fırlattığı yere yerleştirildiğinde, ürünleri mevcut lojistiğin çekebileceği bir envantere toplar.

**Bitişik envanterlerden eşya alma**

<ItemLink id="Automagy:blockGreedyChest" showIcon="left" /> komşu envanterlere eklenen eşyaları izler ve ayarlarına göre bunların bir kısmını kendine aktarır.<br>
Varsayılan payı %50'dir. Çekme yönlerini ve çalışma modlarını seçmek için ayarlarını bir asa ile aç.

- **Orantılı dağıtım:** Bitişik bir envantere girenlerin seçilen bir payını alarak tek bir kaynağı farklı kullanımlar arasında böler.
- **Stok koruma:** Üretim hattının bir dalı için sabit arz tutarak hedef miktara göre eşya alır.
- **Fazlayı alma:** Gerekli stoğu bitişik envanterde bırakıp eşiğin üzerindeki miktarı alır.
- **Eşya filtreleme:** Hangi eşyaların dağıtıma katılacağını seçmek için bir <ItemLink id="Automagy:enchantedPaper:1" showIcon="left" /> veya <ItemLink id="Automagy:enchantedPaper:2" showIcon="left" /> kullan.

Bir Greedy Chest, tam altındaki bir huniden eşya almaz. İki Greedy Chest arasındaki transferler de yön ayarlarına bağlıdır.<br>
Bir makinenin tarif tamponunun yanında kullanıyorsan, gerekli malzemelerin başka yöne çekilmemesi için önce yönleri ve filtreleri yapılandır.

**Eşya örneklerini koruma**

<ItemLink id="Automagy:blockTenaciousChest" showIcon="left" /> her eşya türünden bir örnek korur ve çekme kurallarına uyan otomasyonun bunların hepsini kaldırmasını önler.<br>
Kalan stoğun çekilmeye devam edebilmesi için bir eşyayı ayrı bir yığına ayırmaya çalışır. Oyuncular ayrılan eşyaları yine de elle alabilir.

Bu kap; tohumlar, fidanlar ve sıralama örnekleri için uygundur. Yapılandırıldıktan sonra lojistik, üretimi yeniden başlatmak veya eşyaları tanımlamak için gereken örnekleri koruyarak fazla stoğu sürekli çekebilir.

## Aynalar ve Uzun Mesafeli Taşıma

Birbirine bağlı <ItemLink id="Thaumcraft:blockMirror:0" showIcon="left" /> blok çiftleri eşyaları uzun mesafelere, hatta boyutlar arasında taşır. Eşyalar bir aynaya atılabilir veya lojistik yoluyla içine konabilir. Alıcı uçta çıkışı işleyecek bir envanter veya eşya toplama cihazı olmalıdır.

Standart Magic Mirror'lar çiftler halinde bağlanır. Söküldüklerinde önceki eşleşme bilgilerini korurlar ve yeni bir hedefe de bağlanabilirler. Bir aynayı taşıdıktan sonra alıcı konumunu ve toplama düzeneklerini kontrol et.

Yoğun ve sürekli trafik aynalarda yük biriktirerek çıkış hızını düşürür. Bu yük zamanla azalır; Ordo esansı da bunu gidermeye yardımcı olabilir.<br>
Birden çok üretim hattı aynı toplama noktasını paylaşıyorsa hem ayna verimini hem de alıcı ucun işleme kapasitesini hesaba kat.

**Gezinirken eve eşya gönderme**

<ItemLink id="Thaumcraft:HandMirror" showIcon="left" /> yanında taşınabilir. Sabit bir Magic Mirror'a bağlandıktan sonra arayüzü eşyaları o konuma geri gönderir.<br>
Keşif yaparken, kaynak toplarken veya malzeme taşırken eşyaları üsse göndermek için kullanışlıdır. Üsteki mevcut toplama ve sıralama sistemleri bunları alabilir.

**Birden çok kaynağı birleştirme**

<ItemLink id="Automagy:blockMirrorAlt:0" showIcon="left" /> yalnızca giriş kabul eder. Cihazı o aynanın taşıma kanalına bağlamak için zaten eşleşmiş bir Magic Mirror seçmek üzere bir <ItemLink id="Automagy:crystalEye" showIcon="left" /> kullan.

Birden çok Melding Mirror, dağınık çiftliklere, işleme cihazlarına ve uzak toplama alanlarına hizmet ederek farklı konumlardan ortak bir toplama noktasına eşya gönderebilir. Hedef Magic Mirror geçerli bir eşleşmeyi korumalı ve çıkış ucunda sürekli eşya toplama olmalıdır.

> [!WARNING]
> Ayna çıkışları düşen eşya üretebilir. Eşyaların yerde kalıp kaybolmaması için alıcı ucun toplama düzenekleri, depolama kapasitesi ve çıkış hızı gerçek verimi kaldırabilmelidir. Değerli malzemeleri aynalardan göndermeden önce alıcı konumu doğrula.

## Envanter İzleme ve Otomatik Kontrol

**Eşya miktarlarına dayalı sinyaller**

<ItemLink id="Automagy:blockTally" showIcon="left" /> hedef envanterdeki eşyaları okur ve bir Rünik Beyaz Liste veya Kara Liste ile belirlenen koşullara göre kızıltaş sinyali verir. Kontrol edilen envantere bakar ve sinyali ters yönde çıkarır.

Sonucu bir üretim cihazının kızıltaş kontrolüne bağlayarak azalan stokları tamamlayabilir, hedef miktarda durdurabilir veya bir malzeme kümesi hazır olduğunda başka bir cihazı tetikleyebilirsin.

Tally Box'lar neyi algıladıklarını değiştirmek için mercek de kullanabilir:

- <ItemLink id="Automagy:tallyLens:1" showIcon="left" />: Hedef konumdaki serbest eşyaları algılar; bir toplama noktasındaki birikimi kontrol etmeyi sağlar.
- <ItemLink id="Automagy:tallyLens:2" showIcon="left" />: Hedef bloğun olası düşen eşyalarını, normal ve İpek Dokunuş sonuçları dahil kontrol eder; böylece belirli bir bloğun varlığı tetikleme koşulu olabilir.

**Envanterleri uzaktan okuma**

<ItemLink id="Automagy:blockRemoteComparator" showIcon="left" /> bir hedefe bağlanmak için Crystalline Eye kullanır ve 20 blok içindeki bir envanterin veya uyumlu bloğun karşılaştırıcı durumunu okur. Böylece algılama cihazları kontrol kablolarının yanında durabilir ve envanterin yanları lojistik bağlantıları için boş kalır.

Bir Tally Box'ın üstüne yerleştirilen Remote Comparator, uzaktaki bir envanterdeki eşya bilgisini değerlendirilmek üzere kutuya aktarır. Tally Box'lar ve Remote Comparator'lar da hedef bilgisini bir röle işleviyle zincir boyunca aktararak envanter koşullarını daha uzak kontrol noktalarına taşıyabilir.

**Varlık sayısını algılama**

<ItemLink id="Automagy:blockEntitySignal" showIcon="left" /> menzil içinde seçilen türdeki varlıkları algılar ve sayıları sinyal gücünü etkiler.<br>
Hedef türü seçmek için bir <ItemLink id="Automagy:crystalEntityEye" showIcon="left" /> kullan. Yetişkin ve yavru hayvanlar ayrı ayrı seçilebilir; bu da cihazı üreme, kesim ve varlık sayısıyla kontrol edilen diğer düzenekler için kullanışlı kılar.

Maksimum algılama alanı 11×11×11'dir. Cihazın çevresindeki katı bloklar algılama yönlerini ve alanını değiştirir: bir yüzü kapatmak o yöndeki algılamayı sınırlar ve karşı tarafa doğru genişletir. Cam, su ve benzeri bloklar algılamayı aynı şekilde engellemez.<br>
Hayvan ağıllarının yanına yerleştirirken kapsama alanını duvarlara göre kontrol et.

**Zamanlanmış etkinleştirme**

<ItemLink id="Automagy:blockHourglassMagic" showIcon="left" /> tekrarlanabilir zamanlama ve kızıltaş çıkışı sağlar.<br>
Zamanlama bittiğinde darbeler, zamanlama sürerken sürekli sinyaller, dönüşümlü çıkış ve kısa kesintiler üretebilir. Giriş sinyalleri zamanlayıcıyı başlatabilir, sıfırlayabilir veya durdurabilir.

Bir Magic Hourglass aralıklı besleme, periyodik toplama veya cihaz etkinleştirme için zamanlama sağlar. Zamanlamasını ve modlarını bir asa ile ayarladıktan sonra, bir cihazın ne zaman çalışabileceğine karar vermek için envanter koşullarıyla birleştir.

**Redcrystal kablolaması**

<ItemLink id="Automagy:blockRedcrystal" showIcon="left" /> farklı blok yüzlerine takılabilir ve köşelerden dolaşarak bağlanabilir. Bir asa, komşu redcrystal'lere bağlantıları ayarlayarak kontrolleri kompakt kurulumların çevresinden geçirmene yardımcı olur.

- <ItemLink id="Automagy:blockRedcrystalAmp" showIcon="left" />: Gelen sinyali yükseltir ve seçilen yönde çıkarır.
- <ItemLink id="Automagy:blockRedcrystalDim" showIcon="left" />: Maksimum çıkış sinyal gücünü sınırlar.
- <ItemLink id="Automagy:blockRedcrystalDense" showIcon="left" />: Yalnızca seçilen minimum gücü karşılayan sinyalleri geçirir.
- <ItemLink id="Automagy:blockRedcrystalRes" showIcon="left" />: İki kristal birbirine baktığında, aralarında 15 bloğa kadar düz bir hat boyunca uzaydan sinyal iletirler.
- <ItemLink id="Automagy:blockRedcrystalMerc" showIcon="left" />: Kızıltaş sinyallerini eşleşmiş Magic Mirror'lar üzerinden iletir. Her ucu ilgili aynaya bağla ve o aynanın 8 bloğu içine yerleştir.

Mercurial Redcrystal, envanter koşullarını alıcı uçtan uzaktaki üretim hatlarına geri gönderebilir; böylece arz ve toplama ayna lojistiği üzerinden koordine edilir.

## Sıvı Toplama ve Besleme

<ItemLink id="Automagy:blockThirstyTank" showIcon="left" /> varsayılan olarak 16.000 mB kapasiteye sahiptir. Tek bir sıvı türü toplar ve depolar; sıvı borularına bağlanabilir. Kovayla toplanabilen bağlı sıvıları emer ve kaynakları aynı sıvının bağlantılı bölgeleri üzerinden bulur.

GTNH'nin varsayılan yapılandırması bitişik su kaynaklarını korur; bu sayede bir kaynağın yanındaki tank sürekli su çekebilir. Mevcut yapılandırma ayrıca açıkta duran tankların yağmur suyu toplamasını sağlar. Diğer sıvılar için tankı havuzun bağlantı yapısına göre konumlandır.

**Gliflerle işlev ekleme**

Bir Thirsty Tank'ın altı yüzünün her biri bir glif alabilir. Yönlü işlevler için seçilen yüz önemlidir. Kapasite, hız ve bertaraf etkileri ihtiyaca göre yapılandırılabilir.

- <ItemLink id="Automagy:glyph:3" showIcon="left" />: Sıvıyı o yüzün yönündeki kaba çıkarır.
- <ItemLink id="Automagy:glyph:4" showIcon="left" />: Sıvıyı o yüzün yönündeki kaptan alır.
- <ItemLink id="Automagy:glyph:5" showIcon="left" />: Yalnızca kızıltaş sinyali alırken etkin toplama yapar.
- <ItemLink id="Automagy:glyph:6" showIcon="left" />: Tankın tamamen boşalmasını önlemek için bir miktar sıvı tutar.
- <ItemLink id="Automagy:glyph:7" showIcon="left" />: Toplama sıklığını artırır. Bu türden birden çok glif bunu daha da artırır.
- <ItemLink id="Automagy:glyph:8" showIcon="left" />: Glif başına 16.000 mB kapasite ekler.

Glyph of Siphoning ve Glyph of Envy, bitişik kaplar arasında sıvı sağlar. Bir Glyph of Temperance, envanter izlemeye veya üretim kontrollerine bağlanabilir. Sabit bir sıvı türünü korumak için Glyph of Preservation, tankı o türe bağlı tutan bir rezerv bırakır.

> [!WARNING]
> <ItemLink id="Automagy:glyph:1" showIcon="left" /> tankın kapasitesinin ötesindeki sıvıyı kabul edip yok eder; <ItemLink id="Automagy:glyph:2" showIcon="left" /> ise içindeki sıvıyı sürekli yok eder. Sıvı geri kazanımı veya yan ürün işleme düzenlerken koruman gereken sıvıların bertaraf için yapılandırılmış tanklara girmemesini sağla.

**Otomatik sağım**

<ItemLink id="Automagy:glyph:9" showIcon="left" /> takıldığında tank, glifin yönünde inek arar ve süt toplar; çevredeki sıvıları toplamayı bırakır. İnekler ilgili algılama alanının içinde olmalı; tankın çıkış için alana ve onu çekmenin bir yoluna ihtiyacı vardır.

NH'de her ineğin 2000 oyun tiklik, yani normal hızda yaklaşık 100 saniyelik bir sağım bekleme süresi vardır. Bekleme süresi ineğin üzerinde saklandığından aynı ineği paylaşan birden çok tank aynı sınıra tabidir. Glyph of the Guzzler arama sıklığını artırır; sürekli çıktı ayrıca sırayla sağılabilecek inek sayısına bağlıdır.

## Üretim Desteği

**Mahsul büyümesini hızlandırma**

<ItemLink id="Thaumcraft:blockMetalDevice:8" showIcon="left" /> etkili ışık kapsama alanındaki bitkileri hızlandırmak için Bitki (Herba) esansı kullanır. Buğday, havuç ve patates gibi sıradan mahsullerin çiftliklerini destekler; hasat ve toplama mevcut cihazlarca yapılır.

Işığın ekili alanı kaplamasını sağlayacak şekilde konumlandır ve Herba arzını sürdür.

**Hayvan yetiştirme**

<ItemLink id="Thaumcraft:blockMetalDevice:13" showIcon="left" /> menzildeki uygun hayvanları üreme moduna sokmak için Yaşam (Victus) esansı tüketir. Bir türden sekiz veya daha fazla hayvan bulunduğunda lamba o türün üremesini teşvik etmeyi bırakır.

Üreme, nüfus kontrolü ve ürün işlemenin sistemin birer parçasını yönetmesi için bunu bir Signum Entia ve mevcut hayvan hasat cihazlarıyla birleştir. Menzildeki yavru hayvanlar da sınıra sayıldığından ağıl düzeni ve alt işleme hızı sürekli üretimi etkiler.

**Yönlü madencilik**

Bir <ItemLink id="Thaumcraft:blockWoodenDevice:5" showIcon="left" />, bir <ItemLink id="Thaumcraft:blockWoodenDevice:4" showIcon="left" /> bloğunun üstüne veya altına takılır. İçine bir <ItemLink id="Thaumcraft:FocusExcavation" showIcon="left" /> ve kazma yerleştirildiğinde kızıltaş, seçilen yönde madenciliği kontrol eder.

Odak ve kazmadaki büyüler performansı etkiler; kazma dayanıklılığı ise çalışmanın ne kadar sürebileceğini belirler. Ürünler tabanın çıkış portundan çıkar veya oraya konan bir envantere girer. Yönü değiştirdikten sonra madencilik yolunu ve çıkış konumunu kontrol et.

Entropi (Perditio) esansı veya karşılık gelen Centi-Vis delme hızını artırır. Yönü, aletleri ve toplama düzeneklerini madencilik yapılacak alanın çevresine göre ayarla; Centi-Vis mevcut bir düğüm ağından sağlanır.

### Ek Golem Kullanımları

Golemler taşıma, hasat ve cihazlar arasındaki eşya etkileşimlerini destekleyebilir. Yaptıkları iş, takılı çekirdeklerine bağlıdır. Envanterleri, konumları ve çalışma hedeflerini bağlamak için bir <ItemLink id="Thaumcraft:GolemBell" showIcon="left" /> kullan.

- **Simya çekirdekleri** esansı imbikler, kavanozlar ve uyumlu cihazlar arasında taşır.
- **Hasat çekirdekleri** uyumlu olgun mahsulleri işler ve yeniden dikmek için uygun yükseltmeleri kullanır. Toplama cihazları düşenleri toplayabilir.
- **Kullanım çekirdekleri** bir eşyayla veya boş elle tıklamaları simüle eder; bu etkileşimleri destekleyen hedeflere hizmet eder.

Bir golem kullanırken göreve göre çekirdeğini, malzemesini ve yükseltmelerini seç ve hedeflerine giden bir yol bırak. Cihazlar toplama, dağıtım ve envanter kontrolünü üstlendiğinde golemler kalan etkileşimleri halledebilir.

</Column>