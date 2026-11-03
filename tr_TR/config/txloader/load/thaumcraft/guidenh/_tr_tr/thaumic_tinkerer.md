---
item_ids:
  - ThaumicTinkerer:enchanter
  - ThaumicTinkerer:repairer
  - ThaumicTinkerer:spellCloth
  - ThaumicTinkerer:kamiResource:0
  - ThaumicTinkerer:ichorPickGem
  - ThaumicTinkerer:ichorclothChestGem
navigation:
  title: Thaumic Tinkerer
  parent: ./index.md
  icon: 'ThaumicTinkerer:enchanter'
  position: 20
---

# Thaumic Tinkerer

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**Thaumic Tinkerer (TT)**, Thaumcraft'a özelleştirilebilir büyüleme, dayanıklılık onarımı, blok taşıma, aşılanmış ekinler ve çok çeşitli işlevsel cihazlar ekler.<br>
Daha sonra <Color color="#B7A0D6">KAMI</Color> araştırması Ichor üzerine kurularak Ichorcloth zırhı, Ichorium aletleri, ışınlanma cihazları ve daha fazlasını sunar.

İçeriği ekipman yükseltmelerini, malzeme üretimini ve üs inşasını destekler. Osmotic Enchanter ve Thaumic Restorer mevcut ekipman ve esans sistemlerine uyum sağlar;<br>
aşılanmış ekinler aspekt kombinasyonlarıyla yetiştirilir, KAMI ise void malzemelerinden, Osmiridyum'dan ve daha yüksek asa Vis kapasitesinden daha fazla yararlanır.

NH birçok araştırma ön koşulunu ve tarifini yeniden yazıyor, bu yüzden güncel malzemeleri NEI'de kontrol et. Bu sayfa cihaz mekaniklerine, kullanımlarına ve NH'ye özgü değişikliklere odaklanır.

## Osmotic Enchanter

<GameScene interactive={true} wrap="square" align="right" width="240" height="220" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/osmotic_enchanter.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<ItemLink id="ThaumicTinkerer:enchanter" showIcon="left" />, TT tarafından eklenen güçlü bir büyüleme masasıdır.<br>
Bir asanın Vis'ini kullanarak ekipmana uygulanacak büyüleri ve seviyeleri seçmeni sağlar.<br>
Farklı büyüler farklı temel aspektler gerektirir ve maliyetler yüksek seviyelerde hızla artar.

**Çevredeki sütunlar**

Büyüleyici, **yakında 6 sütun** gerektirir. Bunların tabanları büyüleyiciyle aynı yükseklikte ve hem X hem Z ekseninde **4 blok** içinde olmalıdır.<br>
Her sütun dikey olarak üst üste dizilmiş **2–12 <ItemLink id="Thaumcraft:blockCosmeticSolid:0" showIcon="left" />** içerir ve tepesinde <ItemLink id="Thaumcraft:ItemResource:1" showIcon="left" /> bulunur.

Sahne, her sütunda iki totem bulunan bir düzeni gösteriyor.<br>
Menzil ve yükseklik koşullarını karşılayan diğer konumlar da çalışır; sütunların sabit bir altıgen düzeninde olması gerekmez.

**Eşyalar ve güç kaynağı**

- Eşya **büyüsüz** olmalı ve seçilen büyünün gerektirdiği eşya türüne ve büyülenebilirliğe sahip olmalıdır.
- Arayüz yalnızca eşyaya uygulanabilen ve araştırma gereksinimleri karşılanmış kayıtlı büyüleri sunar. İpek Dokunuş ile Servet arasındaki uyumsuzluk gibi kısıtlamalar hâlâ geçerlidir.
- Asanın uçlarının temel Vis tüketim değiştiricisi **%100 veya daha az** olmalıdır. Demir ve bakır uçlar uygun değildir; asalar da kabul edilmez.
- Vis işlem sırasında kademeli olarak emilir, bu yüzden toplam gereksinim asanın mevcut rezervini aşabilir. Yetersiz kalırsa asayı çıkar, şarj et ve Vis sağlamaya devam etmek için geri koy.
- Büyüleyici çalışırken eşya kilitlenir; çıkarılması veya seçilen büyülerin değiştirilmesi engellenir. Geçersiz sütunlar işlemi keser.

Osmotic Enchanter, merkezde sıradan bir Büyüleme Masası ve çevresinde Obsidyen Totemler, Thaumium Plakalar ve Spellbinding Cloth kullanılarak infüzyon yoluyla yapılır.<br>
Tarifin kararsızlığı **12**'dir ve araştırma **3 Delilik** ekler.

**Spellbinding Cloth**

<ItemLink id="ThaumicTinkerer:spellCloth" showIcon="left" /> ile bir eşyayı üretim tarifinde birleştirmek eşyanın büyülerini kaldırır ve kombinasyonu yeniden tasarlamanı sağlar.

> [!WARNING]
> Spellbinding Cloth, eşyanın mevcut büyülerini kaldırır. Nadir büyüleri veya tekrar elde edilmesi zor etkileri olan ekipmanlarda kullanmadan önce hangilerini saklamak istediğini kontrol et.

## Faydalı Büyüler

Thaumic Tinkerer'ın büyü araştırmaları kendi araştırma sekmesinde görünür. Bu büyüleri Osmotic Enchanter'da seçebilmek için ilgili araştırmayı tamamla.<br>
Kazma, savaş veya hareket üzerinde etkilidirler, bu yüzden onları ekipmanın kullanım amacına göre seç.

**Madencilik ve hasat**

- **Tunnel**: Düz bir çizgide tekrar tekrar kazarken kazma hızını artırır; tüneller için kullanışlıdır.
- **Shatter**: Yüksek sertlikteki bloklara karşı kazma hızını artırır.
- **Disintegrate**: Taş, toprak ve netherrack gibi alete uygun sıradan bloklara karşı çok yüksek kazma hızı sağlar. Diğer hedeflere karşı etkinliği düşer ve dayanıklılık tüketimini ikiye katlar.
- **Flaming Touch**: Tahta blokların hızlı kazılmasında uzmanlaşır; diğer hedeflere karşı etkinliği düşer ve dayanıklılık tüketimini o da ikiye katlar.

**Savaş ve hareket**

- **Vampirism**: Bir saldırıyla verilen hasarın bir kısmını kullanıcı için iyileşmeye dönüştürür.
- **Quick Draw**: Yayın gerilme hızını artırır.
- **Ascent Boost**: Zıplama yüksekliğini artırmak için pantolona uygulanır.
- **Slow Fall**: Düşme hızını ve düşme hasarını azaltmak için botlara uygulanır; eğilmek etkiyi geçici olarak devre dışı bırakır.

Diğer savaş büyüleri arasında Dispersed Strikes, Focused Strikes, Final Strike, Valiance, Pounce ve Shockwave bulunur. Araştırma girdileri etkilerini ve uygulanabilecekleri ekipmanı açıklar.<br>
Dayanıklılık tüketimi yüksek kazma büyüleri, onarım tesisleri veya kırılmaz Ichorium aletleriyle iyi uyum sağlar.

## Dayanıklılık Onarımı ve Durum Koruması

**Thaumic Restorer**

<ItemLink id="ThaumicTinkerer:repairer" showIcon="left" />, içine konan eşyaları <Color color="#B7A0D6">Instrumentum esansı</Color> kullanarak onarır. Her Instrumentum puanı **8 dayanıklılık** geri kazandırır.

Esansı, onarıcının bağlantı yüzüne Instrumentum stoğuna bağlı tüplerle ver. Hakikat Gözlüğü kalan hasarı gösterir ve onarıcı onarım yaparken kızıltaş sinyali yayar.

Otomasyon, hasarlı eşyaları yerleştirebilir ve onarım tamamlandığında çıkarabilir; bu da ekipman toplama, onarma ve yeniden tedarik döngüsünü destekler.<br>
Eşyaları onarılabilirliklerine göre kabul eder; **Tinkers' Construct aletleri onarılamaz**.

Esans depolama ve dağıtımı için [Simya ve Esans](./alchemy_essentia.md) sayfasına bak.

**Talisman of Remedium**

Takılı ve etkin olduğunda <ItemLink id="ThaumicTinkerer:cleansingTalisman" showIcon="left" /> birkaç olumsuz durum etkisini emer ve bunları kaldırmak için dayanıklılığını tüketir. Yüksek dayanıklılık maliyetiyle bazı Delilik ile ilgili etkilerle de baş edebilir.

**Wand Focus: Mending**

<ItemLink id="ThaumicTinkerer:focusHeal" showIcon="left" /> sürekli kullanımda asa Vis'ini tüketerek kullanıcıyı yavaşça iyileştirir. Savaşlar arasında toparlanmak için kullanışlıdır ve ilgili Vis rezervlerini gerektirir.

## Taşıma, Toplama ve Cihaz Arayüzleri

**Wand Focus: Dislocation**

<ItemLink id="ThaumicTinkerer:focusDislocation" showIcon="left" /> bir bloğu alır, depolar ve başka bir yere yerleştirir. Kaplar, fırınlar ve bazı yaratık doğurucuları da taşınabilir. Vis, blok alınırken harcanır; geri yerleştirmek ek Vis maliyeti getirmez.

Tile entity içeren bloklar sıradan blokların **5 katı** Vis tüketir; yaratık doğurucuları ise **20 katı**.<br>
Odak belirli blokları taşıyamaz; bunlar arasında aura düğümleri, bazı AE blokları, demetlenmiş kanallar, güçlendirilmiş esans kavanozları ve diğer özel cihazlar bulunur.

**Transvector Interface ve Dislocator**

- Bir hedef bloğa bağlanmış <ItemLink id="ThaumicTinkerer:interface" showIcon="left" />, onun eşya, sıvı ve diğer arayüzlerini genişletir.<br>
**4 blok** menzil içinde <ItemLink id="ThaumicTinkerer:connector" showIcon="left" /> ile bağla. Hedefin ilgili yeteneklerini paylaşır ve bir cihazın çevresinde ek bağlantı noktaları sağlar.
<br>
- <ItemLink id="ThaumicTinkerer:dislocator" showIcon="left" />, kızıltaşla tetiklendiğinde önündeki bloğu bağlı konumdaki blokla değiştirir ve o konumlardaki varlıkları da taşır.<br>
Bağlama menzili **16 blok**tur ve yönü bir asayla ayarlanabilir.

**Çekiciler ve otomatik alet kullanımı**

- <ItemLink id="ThaumicTinkerer:magnet" showIcon="left" /> düşen eşyaları etkiler, Corporeal Attractor ise canlı yaratıkları etkiler. Mavi mod çeker, kırmızı mod iter;<br>
menzil kızıltaş sinyal gücünün yarısıdır ve en fazla **7.5 blok**tur. Corporeal Attractor ayrıca yaratık türlerini filtrelemek ve yetişkinleri yavrulardan ayırmak için Ruh Kalıpları kullanır.
<br>
- <ItemLink id="ThaumicTinkerer:animationTablet" showIcon="left" />, içine konan alet veya eşyayla sol tık ya da sağ tık eylemlerini sürekli veya kızıltaş kontrolünde gerçekleştirir.<br>
Alet türü ve dayanıklılık, hasat yaparken, blok yerleştirirken veya diğer otomatik eylemleri gerçekleştirirken çalışmasını etkiler.

Bu cihazlar mevcut lojistik ve kızıltaş kontrollerini tamamlar. Toplama, envanter izleme ve üretim desteği hakkında daha fazlası için [Büyülü Otomasyon](./magic_automation.md) sayfasına bak.

## Aydınlatma, Hareket ve Taşınabilir Cihazlar

**Aydınlatma ve karartma**

<ItemLink id="ThaumicTinkerer:brightNitor" showIcon="left" />, envanterde saklıyken bile taşıyıcısının etrafındaki alanı aydınlatır; bu da onu mağaralarda ve sabit aydınlatması olmayan alanlarda kullanışlı kılar.

<ItemLink id="ThaumicTinkerer:gaseousLightItem" showIcon="left" /> ve <ItemLink id="ThaumicTinkerer:gaseousShadowItem" showIcon="left" />, çevredeki alanı sırasıyla aydınlatan veya karartan yayılan gazlar salar.

<ItemLink id="ThaumicTinkerer:gasRemover" showIcon="left" />, yakındaki her iki gaz türünü de dağıtarak zaten hazırlanmış bir alanı değiştirmeni sağlar.

**Hareket ve depolama**

- <ItemLink id="ThaumicTinkerer:focusFlight" showIcon="left" />, kullanıcıyı havaya kaldırmak için Vis tüketir; kısa mesafeli hareket ve engelleri aşma imkânı sağlar.
- <ItemLink id="ThaumicTinkerer:focusEnderChest" showIcon="left" />, Ender depolamasına uzaktan erişim sağlar. EnderStorage entegrasyonuyla bir Ender Sandığı'nın renk kombinasyonuna da bağlanabilir.
- Takılı ve etkin olduğunda <ItemLink id="ThaumicTinkerer:xpTalisman" showIcon="left" /> yakındaki deneyim kürelerini toplar. Envanterdeki cam şişeler, depolanan deneyimi depolama ve aktarım için Büyü Şişeleri'ne dönüştürmek üzere kullanılabilir.
- <ItemLink id="ThaumicTinkerer:revealingHelm" showIcon="left" />, Thaumium kask korumasını Hakikat Gözlüğü'nün gözlem yetenekleriyle birleştirir; bu yetenekleri kullanırken baş korumasını korur.

## Elementel Ateş

Thaumic Tinkerer'ın altı elementel ateşi, çevre dönüşümünde ve daha sonraki Aşılanmış Tohumlar araştırmasında rol oynar.

- <ItemLink id="ThaumicTinkerer:fireFire" showIcon="left" />: Bazı sıradan blokları Nether karşılıklarına dönüştürür; örneğin taşı netherrack'e.
- <ItemLink id="ThaumicTinkerer:fireWater" showIcon="left" />: Bazı Nether arazileri dahil olmak üzere araziyi su, buz ve kara doğru dönüştürür.
- <ItemLink id="ThaumicTinkerer:fireAir" showIcon="left" />: Bazı blokları çöl karşılıklarına dönüştürür.
- <ItemLink id="ThaumicTinkerer:fireEarth" showIcon="left" />: Taşı, kırıktaşı ve diğer blokları toprağa çevirir; ayrıca çakılı kile dönüştürmek gibi ek dönüşümler yapar.
- <ItemLink id="ThaumicTinkerer:fireOrder" showIcon="left" />: Mevcut sürümde kullanılabilir blok dönüşümü sonucu yoktur, ancak araştırması Aşılanmış Tohumlar için ön koşul olmayı sürdürür.
- <ItemLink id="ThaumicTinkerer:fireChaos" showIcon="left" />: Diğer elementel ateşlerin büyüsünü kaldırarak onları sıradan ateşe dönüştürür.

> [!WARNING]
> NH, elementel ateşin varsayılan olarak yayılmasına ve blokları dönüştürmesine izin verir. Etki alanını kontrol et ve üslerin, çiftliklerin, tahta binaların veya önemli tesislerin yakınında salmaktan kaçın. Perditio Imbued Fire'ın bıraktığı sıradan ateş de yanmaya devam edebilir.

## Aşılanmış Ekinler

<ItemLink id='ThaumicTinkerer:infusedSeeds:0:{mainAspect:{Aspects:[{key:"aer",amount:1}]},aspectTendencies:{Aspects:[]}}' showIcon="left" /> bir ana aspekt ve temel aspekt eğilimleri taşır. Her ana aspektin farklı bir ganimet havuzu vardır; aspekt kombinasyonları belirli malzemeler üreten ekinler yetiştirmeni sağlar.

Aşılanmış Tohumlar araştırması altı elementel ateş araştırma girdisinin tümünü gerektirir. Altı temel tohum, merkezde Buğday Tohumları ve **ilgili aspekten 4 kristal kümesi** kullanılarak infüzyon yoluyla yapılır.<br>
Her tarif **32 Messis, 32 Meto ve ilgili temel aspekten 16 esans** gerektirir ve kararsızlığı **4**'tür. Bileşik aspekt tohumları daha ileri yetiştirmeyle elde edilir.

Tohumlar sıradan tarım arazisine ekilebilir ve onu Aşılanmış Tarım Arazisi'ne dönüştürür. Büyüme en az **ışık seviyesi 9** gerektirir. Olgun ekinleri hasat etmek tohum ve ilgili ganimeti verir; ekin yaprakları toprakta aspekt kalıntısı bırakır.

Olgun bir ekin hasat edildiğinde yaprakları ana aspektini altındaki tarım arazisinde bırakır. Tarım arazisi toplamda en fazla **20 puan** kalıntı tutar; fazla kalıntı bazı aspektlerin rastgele azalmasına neden olur.

Olgun bir ekin hasat edildiğinde ana aspekti topraktaki bir aspektle birleşebilir ve düşen tohumu yeni bir bileşik aspekt tohumuna dönüştürebilir.<br>
Örneğin <Color color="#B7A0D6">Aer + Ignis = Lux</Color>. Birikmiş Aer kalıntısı olan toprakta Ignis ekinleri yetiştirmek, hasatta Lux tohumları verebilir. Daha ileri aspekt kombinasyonlarını takip etmek daha karmaşık ana aspektlere götürür.

**Temel aspekt eğilimleri**

Eğilimler büyümeyi, verimi ve mutasyonu etkiler. Bir ekin toplamda en fazla **50 eğilim puanı** taşıyabilir; fazla puanlar bazı eğilimlerin rastgele azalmasına neden olur.

| Eğilim | Ana Etki |
| --- | --- |
| Aqua | Büyümeyi hızlandırır |
| Terra | Olgun bir ekinin hasadından sonra yapraklarının toprakta bıraktığı kalıntıyı artırır |
| Ignis | Bileşik aspekt tohumu üretme şansını artırır |
| Ordo | Ganimet zar atışlarının sayısını artırır |
| Perditio | Tohum düşüşlerini artırır |
| Aer | Bitişik ekinlerden eğilim kazanımını hızlandırır |

Bileşik aspekt ekinleri, bitişik temel ekinlerden ilgili eğilimi kazanabilir; bu yöntemle eğilim başına en fazla **5 puan**. Bitişik bileşik ekinler de kendi aralarında eğilim aktarır; daha yüksek değerler bu takas yoluyla daha ileri yetiştirme gerektirir.

**Ganimet ve NEI**

Thaumic Tinkerer, Aşılanmış Tohumlar için NEI ganimet araması sağlar; belirli bir aspekt ekininin olası çıktılarını ve olasılıklarını gösterir. Bu olasılıklar ganimet havuzundan gelir; Ordo eğilimi de hasat başına ganimet zar atışı sayısını etkiler.

- **Dört doğal elementin** ekinleri ilgili Aşılanmış Tahılı üretir; bu tahıl simyada Aer, Ignis, Aqua ve Terra iksirleri yapmak için kullanılabilir.
- **Ordo ve Perditio** ekinleri sırasıyla cam ve kum üretir.
- **Cognitio** ganimet havuzunda kâğıt, kitap, kitaplık ve Bilgi Parçaları bulunur.
- **Alienis** ganimet havuzunda Ender İncisi, Ender Gözü ve Void Tohumları bulunur.
- Diğer bileşik aspektlerin kendi ganimet havuzları vardır. Yetiştirmek için uygun bir ana aspekt bulmak üzere hedef eşyanın tariflerini NEI'de ara.

Uzun süreli hasat için tohumları ve eğilimlerini, toprak kalıntısını ve yetişme konumlarını koru; yetiştirme ve üretim için uygun ekim alanları ata.

## KAMI Araştırmasını Açma

<Color color="#B7A0D6">KAMI</Color> için ana giriş noktası **Ichor** araştırmasıdır. Ön koşulları ana Thaumcraft kategorilerini ve ilgili Thaumic Tinkerer araştırmalarını kapsar. Bunları tamamlamak Ichorcloth, Ichorium ve gelişmiş cihazlarına giden yolu açar.

Ichor araştırmasını açmak zahmetlidir ve çoğu zaman araştırmacıyı 300+ Delilik ile bırakır, bu yüzden uygun Delilik koruması hazırla.

Kilitli kalanları görmek ve gizli ön koşulları belirlemek için `NEI`'de Ichor tarifinin ön koşullarını kontrol et. Görev kitabı ayrıca Thaumium Crowbar ve Cursed Spirit's Blade gibi kolayca gözden kaçan araştırmaları vurgular.

## Ichor, Ichorcloth ve Ichorium

**Boyutsal parçalar**

<ItemLink id="ThaumicTinkerer:kamiResource:6" showIcon="left" /> ve <ItemLink id="ThaumicTinkerer:kamiResource:7" showIcon="left" /> Ichor için önemli bileşenlerdir.

- **Nether**'da bir oyuncu tarafından öldürülen Zombi Pigmanlar **1/16** şansla Nether Parçası düşürür.
- **End**'de bir oyuncu tarafından öldürülen Endermanlar **1/32** şansla Ender Parçası düşürür.
- NH ayrıca boyutsal parçalar için infüzyon tarifleri sunar; bunlarda çeşitli Forbidden Magic parçaları, aşılanmış parçalar ve ilgili merkez bileşenler kullanılır. Arıcılık, sürekli tedarik için başka bir yol sunar.

Düşüşler ilgili boyutu ve oyuncu öldürmesini gerektirir; bir yaratık tedariki tasarlarken bu koşulları hesaba kat.<br>
İlgili yaratıkları gerekli boyutlarında işleyen bir `EEC` de parça üretir.

**Ichor**

<ItemLink id="ThaumicTinkerer:kamiResource:0" showIcon="left" /> bir Nether Yıldızı'nın infüzyonuyla yapılır.

Tarif, merkezde bir Nether Yıldızı kullanır; çevresinde Kusursuz Elmas, Nether Parçası, Ender Gözü ve Ender Parçası bulunur ve **2 Ichor** üretir.<br>
Esans gereksinimleri **32 Humanus, 32 Lux, 64 Spiritus, 16 Alienis ve 16 Ordo** olup kararsızlığı **10**'dur. Ichor araştırmasının kendisi **5 Delilik** ekler.

**Ichorcloth ve Ichorium**

- <ItemLink id="ThaumicTinkerer:kamiResource:1" showIcon="left" /> Ichor, Büyülü Kumaş, Hiçlik Metali Folyo, Osmiridyum Folyo ve Kusursuz Elmasları birleştirir. Ichorcloth Cübbeleri ve uyandırılmış yükseltmeleri için ana malzemedir.
- **Ichorium**, Ichor, hiçlik metali, Osmiridyum ve Kusursuz Elmasları birleştirir. GT'nin Ichorium külçeleri ve malzeme formları plaka, vida, halka ve çeşitli alet bileşenleri yapmak için kullanılır.

Her iki esrarengiz üretim tarifi de **altı temel aspekten 125 Vis** gerektirir. Asa kapasitesi ve Vis indirimleri gerçekte hangi tarifleri üretebileceğini etkiler. İlgili ekipman ve indirim kaynakları için [Asalar, Vis ve Düğümler](./wands_vis_nodes.md) sayfasına bak.

**Ichorium asa bileşenleri**

<ItemLink id="ThaumicTinkerer:kamiResource:4" showIcon="left" /> tüm temel aspektler için **%30** Vis indirimi sağlar. <ItemLink id="ThaumicTinkerer:kamiResource:5" showIcon="left" /> bir asaya **temel aspekt başına 1000 Vis** kapasitesi verir.

Bu yol, büyük esrarengiz tarifleri ve sürekli odak kullanımını destekler. Uçlar, çekirdek ve bitmiş asa, her biri kendi araştırmasını ve üretimini gerektirir.

## Ichorcloth Zırhı ve Uyandırma

Sıradan Ichorcloth zırhı <ItemLink id="ThaumicTinkerer:ichorclothHelm" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorclothChest" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorclothLegs" showIcon="left" /> ve <ItemLink id="ThaumicTinkerer:ichorclothBoots" showIcon="left" /> parçalarından oluşur.<br>
Bu parçalar dayanıklılık kaybetmez. İnfüzyon, ek hareket, koruma ve gözlem yetenekleri kazandırmak için onları uyandırabilir.

- <ItemLink id="ThaumicTinkerer:ichorclothHelmGem" showIcon="left" />: Gözlem yetenekleri, su altında nefes alma, su altında net görüş ve açken bile devam eden can yenilenmesi sağlar.
- <ItemLink id="ThaumicTinkerer:ichorclothChestGem" showIcon="left" />: Sürekli uçuş, düşme koruması ve sıradan mermilere karşı koruma sağlar.
- <ItemLink id="ThaumicTinkerer:ichorclothLegsGem" showIcon="left" />: Ateş koruması sağlar ve gelen ateş hasarını iyileşmeye dönüştürür.
- <ItemLink id="ThaumicTinkerer:ichorclothBootsGem" showIcon="left" />: Hareketi, zıplamayı ve boşluklar arasında erişimi iyileştirir, bir blokluk yükseltilere otomatik adım atmayı sağlar ve Kazma Hızı ile düşme koruması verir.

Uyandırılmış zırh etkileri, varsayılanı `U` olan **Toggle Awakened Armor** tuş atamasıyla kontrol edilir.<br>
NH, uyandırılmış pantolonların otomatik ışık yerleştirmesini varsayılan olarak devre dışı bırakır; uyandırılmış botların giyenin altındaki toprağı çime dönüştürme yeteneğini korur.

Uyandırma tarifleri gelişmiş mücevherler, Ichorium bileşenleri ve diğer büyülü cihazları kullanır ve yüksek kararsızlığa sahiptir.<br>
Malzeme üretimi oturduktan sonra kararlı bir İnfüzyon Sunağı ve yeterli esans rezervi gerekir. Sunak tedariki ve kararlılık için [İnfüzyon Üretimi](./infusion_crafting.md) sayfasına bak.

## Ichorium Aletleri ve Bedrock Boyutu

<ItemLink id="ThaumicTinkerer:ichorPick" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorShovel" showIcon="left" />, <ItemLink id="ThaumicTinkerer:ichorAxe" showIcon="left" /> ve <ItemLink id="ThaumicTinkerer:ichorSword" showIcon="left" /> dayanıklılık kaybetmez ve daha fazla uyandırılabilir.

Uyandırılmış bir aletin çalışma modunu değiştirmek için eğilip sağ tıkla:

- <ItemLink id="ThaumicTinkerer:ichorPickGem" showIcon="left" />: Tek blok, **5×5 alan** ve **10 blokluk çizgi** madenciliği; ayrıca bedrock kırma yeteneği.
- <ItemLink id="ThaumicTinkerer:ichorShovelGem" showIcon="left" />: Tek blok, **5×5 alan** ve aynı blok türünde dikey sütun madenciliği.
- <ItemLink id="ThaumicTinkerer:ichorAxeGem" showIcon="left" />: Tek blok, **5×5 alan** ve tüm ağacı kesme.
- <ItemLink id="ThaumicTinkerer:ichorSwordGem" showIcon="left" />: Tek hedefli saldırılar, aynı türdeki yakın yaratıklara alan saldırıları ve Ruh Kalpleri veren bir mod.

> [!WARNING]
> Alan ve çizgi madenciliği aynı anda birkaç bloğu etkiler. Uyandırılmış aletleri üssünün veya cihazlarının yakınında kullanmadan önce, saklamak istediğin blokları kırmamak için mevcut modu ve yönü kontrol et.

**Bedrock Boyutu**

Uyandırılmış Ichorium Kazması'nın bedrock kırma yeteneği **Bedrock Boyutu**'na erişim de sağlar. Dünya'da **Y=0–4** aralığında eğilerek bedrock kazmak bir giriş oluşturur. İçeride bedrock ve içindeki dikey cevher damarlarını kazmaya devam edebilirsin.

Bu boyut özel bir madencilik alanı sağlar. GTNH cevher içeriğini ayarlar; geleneksel madenciler önce çalışacak alana ihtiyaç duyar, bu yüzden bedrock temizlemek için uygun bir yöntem planla.

Görev kitabı, çıkışın seni yakındaki yüzeye veya blokların içine yerleştirebileceği konusunda uyarır. Giriş ve çıkış noktalarının değişmesinden kaynaklanan sorunları azaltmak için girmeden önce dönüş yöntemleri, kazma aletleri ve konum kayıtları hazırla.

## KAMI İnşaat ve Işınlanma Cihazları

**Büyük miktarlarda blok depolama ve yerleştirme**

- Bir blok türüne bağlandıktan sonra <ItemLink id="ThaumicTinkerer:blockTalisman" showIcon="left" /> envanterdeki eşleşen blokları bir yığının ötesinde emer ve kullanım için bir yığın bırakır. Tek türden 2 milyardan fazla blok depolar ve bunları kaplara bırakabilir veya dünyaya yerleştirebilir.
- <ItemLink id="ThaumicTinkerer:placementMirror" showIcon="left" /> seçilen bir alanda blokları önizler ve yerleştirir. Malzemeler envanterden veya gerekli bloğu tutan Siyah Delik Yüzükleri'nden gelebilir.
- <ItemLink id="ThaumicTinkerer:protoclay" showIcon="left" />, taşıyıcının Uyandırılmış Ichorium aletleri arasında geçiş yaparak mevcut hedef için uygun aleti kullanır.
- <ItemLink id="ThaumicTinkerer:ichorPouch" showIcon="left" /> Focus Pouch işlevlerini korurken geniş bir taşınabilir envanter sağlar. NH, Witchery'nin rüya boyutunda kullanımını engeller.

**Göksel Geçitler ve Geri Çağırma**

<ItemLink id="ThaumicTinkerer:warpGate" showIcon="left" />, başka bir geçidin konumunu kaydetmek için bir <ItemLink id="ThaumicTinkerer:skyPearl" showIcon="left" /> kullanır. Her geçit **10 hedef** tutar; üsleri, maden alanlarını ve sık kullanılan diğer konumları birbirine bağlar.

Bir Göksel İnciyi hedef geçide bağla ve tek yönlü bağlantı oluşturmak için kalkış geçidine yerleştir. Dönüş rotası, her iki uçta da yapılandırılmış bir inci gerektirir. Geçidin arayüzü ayrıca diğer geçitlerden gelen bağlantıları kısıtlayabilir.

<ItemLink id="ThaumicTinkerer:focusRecall" showIcon="left" />, kısayol çubuğundaki bağlı bir Göksel İnciyi kullanır ve kullanıcıyı hedefine ışınlamak için Vis tüketir; sabit bir ışınlanma ağını taşınabilir bir eve dönüş yoluna dönüştürür.

</Column>