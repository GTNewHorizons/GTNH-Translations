---
navigation:
  parent: /ae2_mechanics_index.md
  title: Otomatik Üretim
  icon: appliedenergistics2:item.ItemEncodedPattern
---

# Otomatik Üretim

### Büyük Konu

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/autocraft_setup_greebles.snbt" />
  <Block id="minecraft:furnace" x="9" y="1" z="0" facing="north" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Otomatik üretim, AE2'nin temel işlevlerinden biridir. Her alt bileşenin doğru miktarını elle üretip *sıradan biri* gibi uğraşmak yerine ME sisteminden bunu senin için yapmasını isteyebilirsin. Ya da eşyaları otomatik üretip bir yere aktarabilirsin. Ya da akıllı, kendiliğinden ortaya çıkan davranışlarla belirli miktarlarda eşyayı stokta tutabilirsin. Sıvılarla da çalışır; Thaumcraft esansı gibi ek mod materyal türleri için belirli eklentilerin varsa, o materyallerle de çalışır. Oldukça harika.

Oldukça karmaşık bir konu, o yüzden kemerini bağla ve başlayalım.

Bir otomatik üretim düzeneği 3 şeyden oluşur:
- Üretim isteğini gönderen şey
- Üretim CPU'su
- <ItemLink id="appliedenergistics2:tile.BlockInterface" />.

Süreç şöyle işler:

1.  Bir şey bir üretim isteği oluşturur. Bu, terminalde otomatik üretilebilir bir şeye tıklayan sen olabilirsin; ya da dışa aktarmak/stoklamak üzere ayarlandıkları eşyalardan birini isteyen, üretim kartlı bir dışa aktarma veriyolu veya arayüz olabilir.

*   (**ÖNEMLİ:** Stokta zaten bulunan bir şeyin üretimini istemek için "blok seç"e (genellikle orta fare tuşu) atadığın tuşu kullan; bu, envanter sıralama modlarıyla çakışabilir),

2.  ME sistemi, isteği yerine getirmek için gereken bileşenleri ve ön koşul üretim adımlarını hesaplar ve bunları seçilen üretim CPU'sunda saklar

3.  İlgili [kalıba](../items_blocks/patterns.md) sahip <ItemLink id="appliedenergistics2:tile.BlockInterface" />, kalıpta belirtilen bileşenleri bitişikteki herhangi bir envantere iter.
    Üretim tezgâhı tarifi ("üretim kalıbı") söz konusuysa bu, bir <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> olur.
    Üretim dışı bir tarif ("işleme kalıbı") söz konusuysa bu, başka bir blok, makine ya da özenli bir kızıltaş kontrollü düzenek olur.

4.  Üretimin sonucu bir şekilde sisteme döner: içe aktarma veriyoluyla, arayüzle ya da sonucu bir arayüze geri iterek.
    **Bir "eşyanın sisteme girmesi" olayının gerçekleşmesi gerektiğini unutma; sonucu üzerinde <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> bulunan bir sandığa boruyla gönderemezsin.**

5.  Bu üretim, istekteki başka bir üretimin ön koşuluysa eşyalar o üretim CPU'sunda saklanır ve ardından o üretimde kullanılır.

## Özyinelemeli Tarifler

Otomatik üretim algoritmasının *baş edemediği* şeylerden biri özyinelemeli tariflerdir. Örneğin, Botania mana havuzuna kızıltaş atarak elde edilen "1 kızıltaş tozu = 2 kızıltaş tozu" gibi çoğaltma tarifleri. Ancak [bu tariflerle baş etmenin bir yolu var.](../tricks_example/recursive_crafting_setup.md)

# Kalıplar

<ItemImage id="appliedenergistics2:item.ItemEncodedPattern" scale="4" />

Kalıplar, <ItemLink id="appliedenergistics2:item.ItemMultiPart:340" /> içinde boş kalıplardan üretilir.

Farklı işler için birkaç farklı kalıp türü vardır:

*   <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" /> türü kalıplar, üretim tezgâhında yapılan tarifleri kodlar. Doğrudan bir <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" /> içine konularak bileşenler verildiğinde sonucu üretmesi sağlanabilir, ancak asıl kullanımları moleküler montajcının yanındaki bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> içindedir.
    ME Arayüzleri bu durumda özel davranır ve ilgili kalıbı bileşenlerle birlikte bitişikteki birleştiricilere gönderir.
    Birleştiriciler üretim sonuçlarını bitişik envanterlere otomatik olarak attığından, bir arayüzün üzerindeki bir montajcı, üretim kalıplarını otomatikleştirmek için yeterlidir.

***

*   <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> türü kalıplar, otomatik üretimdeki esnekliğin büyük kısmını sağlar. En genelleştirilmiş türdürler; kısaca "bir arayüz bu bileşenleri bitişik envanterlere iterse, ME sistemi bu eşyaları yakın ya da uzak bir gelecekte bir noktada alacaktır" derler. Neredeyse tüm modlu makinelerle, fırınlarla ve benzerleriyle otomatik üretimi bu şekilde yaparsın. Kullanımları o kadar geneldir ki bileşenleri itmekle sonucu almak arasında ne olduğuyla ilgilenmezler; bu sayede gerçekten tuhaf şeyler yapabilirsin: bileşenleri, eşyaları ayıklayan, sonsuz üreten çiftliklerden başka bileşenler alan karmaşık bir fabrika üretim zincirine sokabilirsin, hatta Bee Movie senaryosunun tamamını yazdırabilirsin; ME sistemi, kalıbın belirttiği sonucu aldığı sürece umursamaz. Hatta bileşenlerin sonuçla herhangi bir ilgisi olup olmamasını bile umursamaz. Ona "1 kiraz ağacı tahtası = 1 Nether Yıldızı" diyebilir ve kiraz ağacı tahtası aldığında wither çiftliğinin bir wither öldürmesini sağlayabilirsin; işe yarar.

Kaynak ayrıca yalnızca tünel kalıbı düzeneklerinde kullanılan bir işleme kalıbı varyantı olan <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" /> öğesini de kaydeder.

Aynı kalıplara sahip birden fazla <ItemLink id="appliedenergistics2:tile.BlockInterface" /> desteklenir ve paralel çalışır. Ayrıca bir kalıp, örneğin 1 kırıktaş = 1 taş yerine 8 kırıktaş = 8 taş diyebilir; arayüz her işlemde eritme düzeneğine tek seferde bir yerine 8 kırıktaş ekler.

Ağa bağlı bir [Kalıp Optimizasyon Matrisi](../items_blocks/pattern_optimization_matrix.md) ile üretim onay ekranı, kalıp yığın boyutlarını optimize edebilir. Arayüzde ayrıca **Kalıp optimizasyonuna izin ver** seçeneğinin etkin olması gerekir.

## "Kalıbın" En Genel Biçimi

Aslında işleme kalıbından bile daha "genel" bir "kalıp" biçimi vardır. Üretim kartlı bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />, bir şey üretmek için kızıltaş sinyali yayacak şekilde ayarlanabilir. Bu "kalıp" bileşenleri tanımlamaz, hatta onları umursamaz bile.
Tek söylediği şudur: "Bu seviye vericisinden kızıltaş yayarsan, ME sistemi bu eşyayı yakın ya da uzak bir gelecekte bir noktada alacaktır." Bu genellikle girdi bileşeni gerektirmeyen sonsuz çiftlikleri etkinleştirip devre dışı bırakmak ya da kırıktaş çoğaltan bir makinen varsa "1 kırıktaş = 2 kırıktaş" gibi özyinelemeli tarifleri (standart otomatik üretimin anlayamayacağı tarifler) işleyen bir sistemi etkinleştirmek için kullanılır.

# Üretim CPU'su

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Üretim CPU'ları üretim isteklerini/işlerini yönetir. Çok adımlı üretim işleri yürütülürken ara bileşenleri saklarlar; işlerin ne kadar büyük olabileceğini ve bir dereceye kadar ne kadar hızlı tamamlanacağını etkilerler. Multiblokturlar ve en az 1 üretim deposu bulunan dikdörtgen prizmalar olmalıdırlar.

Üretim CPU'ları şunlardan yapılır:

*   (Gerekli) [Üretim depoları](../items_blocks/crafting_cpu.md); tüm standart hücre boyutlarında (1k, 4k, 16k, 64k, 256k) bulunur. Bir üretimde yer alan bileşenleri ve ara bileşenleri saklarlar; bu yüzden daha fazla bileşenli üretim işlerini kaldırabilmesi için CPU'da daha büyük ya da daha çok depo gerekir.
*   (İsteğe bağlı) <ItemLink id="appliedenergistics2:tile.BlockAdvancedCraftingUnit" /> birimleri, sistemin arayüzlerden bileşen yığınlarını daha sık göndermesini sağlar.
    Bu sayede, örneğin 6 moleküler birleştiriciyle çevrili bir arayüz, bileşenleri tek bir birleştirici yerine 6'sına birden gönderebilir (ve böylece hepsini kullanabilir).
*   (İsteğe bağlı) <ItemLink id="appliedenergistics2:tile.BlockCraftingMonitor" /> birimleri, CPU'nun o anda işlediği işi gösterir. <ItemLink id="appliedenergistics2:item.ToolColorApplicator" /> ile renklendirilebilirler.
*   (İsteğe bağlı) <ItemLink id="appliedenergistics2:tile.BlockCraftingUnit" /> birimleri, CPU'yu dikdörtgen prizma yapmak için boşluğu doldurur.

Her üretim CPU'su 1 istek veya iş işler; bu yüzden aynı anda hem hesaplama işlemcisi hem de 256 düz taş istemek istiyorsan 2 CPU multibloğuna ihtiyacın var.

Oyunculardan, otomasyondan (dışa aktarma veriyolları ve arayüzler) ya da her ikisinden gelen istekleri işleyecek şekilde ayarlanabilirler.

# ME Arayüzleri

<Row>
<BlockImage id="appliedenergistics2:tile.BlockInterface" scale="4" />

<BlockImage id="appliedenergistics2:tile.BlockInterface" meta="0" nbt='{LOCK_CRAFTING_MODE:"NONE",orientation_up:"DOWN",BLOCK:"NO",PATTERN_OPTIMIZATION:"YES",waitingToSend:[],priority:0,orientation_forward:"SOUTH",INSERTION_MODE:"DEFAULT",inv:{item0:{},item2:{},item1:{},item8:{},item7:{},item4:{},item3:{},item6:{},item5:{}},proxy:{p:0,g:457L,k:-1L},ADVANCED_BLOCKING_MODE:"DEFAULT",id:"BlockInterface",pointAt:1,SMART_BLOCK:"NO",FUZZY_MODE:"IGNORE_ALL",INTERFACE_TERMINAL:"YES"}' />

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/cable_interface.snbt" />
</GameScene>
</Row>

<ItemLink id="appliedenergistics2:tile.BlockInterface" /> arayüzleri, otomatik üretim sisteminin dünyayla etkileşim kurmasının birincil yoludur. [Kalıplarındaki](../items_blocks/patterns.md) bileşenleri bitişik envanterlere iteler ve içlerine eşya eklenerek bu eşyalar ağa aktarılabilir. Bir makinenin çıktısını, <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> kullanarak ağa çekmek yerine yakındaki bir arayüze (genellikle bileşenleri iten arayüze) boruyla geri vermek çoğu zaman bir kanaldan tasarruf ettirir.

Dikkat: Bileşenleri doğrudan bir üretim CPU'sundaki [üretim deposundan](../items_blocks/crafting_cpu.md#crafting-storage) ittikleri için bileşenler hiçbir zaman gerçekte envanterlerinde bulunmaz; bu yüzden onlardan boruyla çekiş yapamazsın. Arayüzün başka bir envantere (örneğin bir varile) itmesini, sonra da oradan boru çekmeni sağlamalısın.

Ayrıca dikkat: Arayüz TÜM bileşenleri tek seferde itmek zorundadır; yarım yığınlar gönderemez. Bunu kendi lehine kullanabilirsin.

ME Arayüzleri, [alt ağlardaki](subnetworks.md) arayüzlerle özel bir etkileşime girer: Arayüz değiştirilmemişse (istek yuvalarında hiçbir şey yoksa) arayüzü tamamen atlar ve doğrudan o alt ağın [depolamasına](../ae2_mechanics/import_export_storage.md) iter; arayüzü atlar, onu tarif yığınlarıyla doldurmaz ve daha da önemlisi depolamada yer açılana kadar sonraki yığını eklemez.

Aynı kalıplara sahip birden fazla arayüz desteklenir ve paralel çalışır.

ME Arayüzleri yığınlarını tüm yüzlerine dönüşümlü olarak göndermeye çalışır; böylece bağlı tüm makineleri paralel kullanır.

## Varyantlar

Bu sürümde yeni AE2'de bulunan normal, yönlü ve düz arayüz blokları yoktur. Arayüz bloğu ağa bağlanır ve yüzlerinden içe/dışa aktarım yapar; düz arayüz ise kompakt yerleşime olanak tanıyan ve ön yüzünde ağ bağlantısı sunmayan bir kablo alt parçasıdır. Normal ve düz arayüzler üretim ızgarasında birbirine dönüştürülebilir.

## Ayarlar

ME Arayüzlerinin çeşitli modları vardır:

*   **Engelleme Modu**, makinede zaten bileşen varsa arayüzün yeni bir bileşen yığını itmesini durdurur.
*   **Üretimi Kilitle**, arayüzü çeşitli kızıltaş koşullarında ya da önceki üretimin sonucu o belirli arayüze eklenene kadar kilitleyebilir.
*   Arayüz, <ItemLink id="appliedenergistics2:item.ItemMultiPart:480" /> üzerinde gösterilebilir veya gizlenebilir.

## Öncelik

Öncelikler, GUI'nin sağ üst köşesindeki anahtara tıklanarak ayarlanır. Aynı eşya için birkaç [kalıp](../items_blocks/patterns.md) varsa, ağın yüksek öncelikli kalıbın bileşenlerine sahip olmaması dışında, yüksek öncelikli arayüzdeki kalıplar düşük öncelikli arayüzdeki kalıplara tercih edilir.

# Moleküler Birleştiriciler

<BlockImage id="appliedenergistics2:tile.BlockMolecularAssembler" scale="4" />

<ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />, kendisine verilen eşyaları alır ve bitişikteki bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> tarafından ya da içine yerleştirilen <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" /> tarafından tanımlanan işlemi gerçekleştirir,
ardından sonucu bitişik envanterlere iter.

Asıl kullanımları bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> yanındadır. ME Arayüzleri bu durumda özel davranır
ve ilgili kalıbın bilgisini bileşenlerle birlikte bitişikteki birleştiricilere gönderir. Birleştiriciler üretim sonuçlarını bitişik envanterlere (ve böylece arayüzün dönüş yuvalarına) otomatik olarak attığından, bir arayüzün üzerindeki bir montajcı
üretim kalıplarını otomatikleştirmek için yeterlidir.

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
