---
item_ids:
  - Thaumcraft:WandCasting
  - Thaumcraft:blockStoneDevice:11
navigation:
  title: Asalar, Vis ve Düğümler
  parent: ./index.md
  icon: 'Thaumcraft:WandCasting'
  position: 70
---

# Asalar, Vis ve Düğümler

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

**<ItemImage id='Thaumcraft:WandCasting:0:{rod:"wood",cap:"iron"}' /> Asalar**, Thaumcraft'ta <Color color="#B7A0D6">Vis</Color> depolar ve kullanır; gizemli üretimi, büyülü tesislerin etkinleştirilmesini ve asa odaklarının kullanılmasını sağlar.<br>Araştırma ilerledikçe yeni tarifleri ve tesisleri desteklemek için asa kapasitesini, Vis indirimlerini ve enerji kaynağını iyileştirmen gerekir.

GTNH'de asa üretimi ayrıca **Twilight Forest kupaları ve teknolojik materyaller** gerektirir.<br>
Daha gelişmiş asalar daha büyük kapasite sunar, bu yüzden yükseltme hem yeni materyaller elde etmeyi hem de bir sonraki asayı üretmek için gereken Vis'i azaltmayı içerir.

Bu sayfa asa özelliklerini ve üretim gereksinimlerini, ayrıca düğümler, aspekt küreleri ve Centi-Vis gibi enerji kaynaklarını ele alır. Aspektler ve araştırma puanları için [Thaumcraft Temelleri](./thaumcraft_basics.md) sayfasına bak.

## Asa Bileşenleri ve Kullanımları

Asalar bir **gövde ya da uzun asa çekirdeği** ve **uçlardan** oluşur. Gövde esas olarak Vis kapasitesini, uçlar ise esas olarak maliyet çarpanını belirler. Bazı ek bileşenler otomatik şarj veya enerji dönüşümü de sağlar.

<Color color="#B7A0D6">Kapasite, altı ilkel aspektin her biri için ayrı ayrı hesaplanır.</Color> "50 Vis" kapasitesi, her ilkel aspekten 50 Vis'e kadar depolanabileceği anlamına gelir.

| Tür | Gizemli Üretim | Asa Odakları | Temel Özellikler |
| --- | --- | --- | --- |
| Asa | Evet | Evet | Üretim, tesislerle etkileşim ve odak kullanımı için uygundur |
| Saltanat Asası | Evet | Hayır | Aynı sıradan gövdeyle kapasite %50 artar, ayrıca Vis maliyetinde 10 puanlık indirim daha sağlanır |
| Uzun Asa | Hayır | Evet | Genellikle daha büyük kapasiteli bir uzun asa çekirdeği kullanır; odaklar ve tesis etkileşimleri içindir |

Saltanat asasının ek kapasitesi ve indirimi, onu Gizemli Çalışma Tezgahında bulundurmak için uygun kılar.<br>
Uzun asalar daha büyük kapasite sunar ancak gizemli üretimde kullanılamaz.

Uzun asa kapasitesi kullanılan çekirdeğe bağlıdır. Örneğin Büyük Ağaç Uzun Asa Çekirdeği 125 Vis, Silverwood Uzun Asa Çekirdeği 250 Vis, altı element uzun asa çekirdeği ise 175 Vis tutar.

**Asa odakları** madencilik, savaş ve hareket gibi etkin yetenekler sağlar; uzun asa çekirdeği ise uzun asanın kapasitesini belirleyen bileşendir.<br>
## Asa Üretim Gereksinimleri

GTNH'de asa üretimi ayrıca vida ve Twilight Forest boss kupası gerektirir; materyaller bileşenin tarif kademesine göre belirlenir.

| Tarif Kademesi | Vida Materyali | Boss Kupası | Tipik Edinme Aşaması |
| --- | --- | --- | --- |
| 0 (LV) | Alüminyum | <ItemLink id="TwilightForest:item.nagaScale" showIcon="left" /> | LV |
| 1 (MV) | Paslanmaz Çelik | <ItemLink id="dreamcraft:LichBone" showIcon="left" /> | MV |
| 2 (HV) | Enerjik Alaşım | <ItemLink id="dreamcraft:LichBone" showIcon="left" /> | MV |
| 3 (EV) | Vibrant Alaşım | <ItemLink id="TwilightForest:item.fieryBlood" showIcon="left" /> | HV |
| 4 (IV) | Tungsten Çeliği | <ItemLink id="TwilightForest:item.fieryTears" showIcon="left" /> | EV |
| 5 (LuV) | Enderyum (YB) | <ItemLink id="TwilightForest:item.carminite" showIcon="left" /> | EV |
| 6 (ZPM) | Oriharukon | <ItemLink id="TwilightForest:item.carminite" showIcon="left" /> | EV |
| 7 (UV) | Osmiridyum | <ItemLink id="dreamcraft:SnowQueenBlood" showIcon="left" /> | IV |

Sıradan Ahşap, Büyük Ağaç, altı element ve Silverwood gövdelerinin standart tarifleri sırasıyla 0, 1, 2 ve 3. kademe materyalleri kullanır. Bu kademeler asa tariflerini gruplar; daha yüksek kademelerdeki bazı materyaller, aynı adı taşıyan gerilim aşamasına ulaşmadan daha erken elde edilebilir.

Sıradan bir asanın montaj Vis maliyeti **gövdenin taban maliyeti + gövdenin uç maliyet artışı × ucun montaj katsayısıdır** ve her ilkel aspekt için aynı miktar gerekir. Saltanat asaları ayrıca gövdenin saltanat çarpanını uygular.<br>
Örneğin Büyük Ağaç 20 + 5 × uç katsayısını kullanır. Altın uçların katsayısı 2'dir, bu yüzden bir asa montajı her aspekten 30 Vis, karşılık gelen saltanat asası ise her birinden 60 Vis gerektirir. Materyal miktarları ve ek mod gövde parametreleri için NEI'ye bak.

## Vis İndirimleri ve Gelişmiş Asalar

<Color color="#B7A0D6">Vis indirimleri</Color> gelişmiş asaların üretiminde önemlidir.

- Uçlar | Asanın taban maliyet çarpanını belirler; bazı uçlar yalnızca belirli aspektlerde indirim sağlar
- Ekipman ve tılsımlar | Uygun yuvalarda takıldığında ilgili aspektler için Vis indirimi sağlar
- Saltanat Asaları | Uç ve ekipman etkilerine ek olarak maliyetleri 10 puan daha düşürür

Temel ekipmanlar arasında <ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> %5 indirim, <ItemLink id="Thaumcraft:ItemChestplateRobe" showIcon="left" /> ve <ItemLink id="Thaumcraft:ItemLeggingsRobe" showIcon="left" /> %2'şer, <ItemLink id="Thaumcraft:ItemBootsRobe" showIcon="left" /> ise %1 indirim sağlar. Dört parça birlikte %10 sağlar.

<ItemLink id="WitchingGadgets:item.WG_AdvancedRobeChest" showIcon="left" /> ve <ItemLink id="WitchingGadgets:item.WG_AdvancedRobeLegs" showIcon="left" /> sırasıyla %5 ve %4 indirim sağlar ve üretim maliyetlerini daha da düşürür.

Genel olarak gerçek maliyet **tarif gereksinimi × (uç maliyet çarpanı − ekipman indirimi − saltanat asası indirimi)** şeklindedir ve çarpan en az 0,1 olabilir. Ekipman ve saltanat asası etkileri yüzde puanı olarak çıkarılır.

Pratik bir örnek, taban montaj maliyeti her ilkel aspekten 60 Vis olan Altın Uçlu Büyük Ağaç Saltanat Asasıdır.<br>
Altın Uçlu Büyük Ağaç Asa 50 Vis kapasiteye sahiptir. Temel dört parçalı setin %10 indirimiyle bile saltanat asasını üretmek 54 Vis gerektirir ve bu kapasiteyi aşar.<br>
Aynı gövdeyi kullanan daha ucuz bir kombinasyon ya da ek indirimler bu gereksinimin üstesinden gelebilir.

Thaumic Machina'nın **Vis Kanalları** yükseltmesi, ekipman ve saltanat asası indirimleri uygulanmadan önce uç maliyet çarpanını 0,9 ile çarpar.<br>
Örneğin Thaumium uçların %90 çarpanı %81 olur; temel dört parçalı set ve bir saltanat asasıyla %61'e iner.

## Asa Uçları

| Kayıt Adı | Uç | Montaj Katsayısı | Taban Vis Maliyeti | Özellikler |
| --- | --- | --- | --- | --- |
| Dünyevi Çelik | <ItemLink id="ForbiddenMagic:WandCaps:2" showIcon="left" /> | 1 | 180% | — |
| iron | <ItemLink id="Thaumcraft:WandCap:0" showIcon="left" /> | 0 | 110% | Düğüm Koruyucu uygulanmaz |
| Bakır | <ItemLink id="Thaumcraft:WandCap:3" showIcon="left" /> | 1 | 110% | Düzen ve Entropi maliyeti %100 |
| gold | <ItemLink id="Thaumcraft:WandCap:1" showIcon="left" /> | 2 | 100% | — |
| Gümüş | <ItemLink id="Thaumcraft:WandCap:4" showIcon="left" /> | 3 | 100% | Hava, Toprak, Ateş ve Su maliyeti %95 |
| SOJOURNER | <ItemLink id="ThaumicExploration:sojournerCap" showIcon="left" /> | 5 | 95% | Elde tutulduğunda yakındaki düğümlerden pasif olarak Vis çeker |
| MECHANIST | <ItemLink id="ThaumicExploration:mechanistCap" showIcon="left" /> | 5 | 95% | Düğümlerden Vis çekme hızını artırır |
| cloth | <ItemLink id="TaintedMagic:ItemWandCap:1" showIcon="left" /> | 3 | 95% | — |
| thaumium | <ItemLink id="Thaumcraft:WandCap:2" showIcon="left" /> | 5 | 90% | — |
| manasteel | <ItemLink id="ForbiddenMagic:WandCaps:3" showIcon="left" /> | 6 | 85% | Yaşayanodun veya Dreamwood gövdeyle eşleştirildiğinde Mana dönüşüm maliyetlerini düşürür |
| vinteum | <ItemLink id="ForbiddenMagic:WandCaps:1" showIcon="left" /> | 5 | 90% | — |
| alchemical | <ItemLink id="ForbiddenMagic:WandCaps:0" showIcon="left" /> | 6 | 90% | Su maliyeti %80; Kan veya Kan Aşılanmış Ahşap gövdeyle LP dönüşüm maliyetlerini düşürür; asa saldırıları Zayıflık uygular |
| shadowcloth | <ItemLink id="TaintedMagic:ItemWandCap:3" showIcon="left" /> | 5 | 85% | — |
| thauminite | <ItemLink id="thaumicbases:resource:2" showIcon="left" /> | 6 | 85% | — |
| blood_iron | <ItemLink id="BloodArsenal:wand_caps:0" showIcon="left" /> | 6 | 85% | Su maliyeti %80; Kan Aşılanmış Ahşap gövdeyle LP dönüşüm maliyetlerini daha da düşürür |
| hiçlik | <ItemLink id="Thaumcraft:WandCap:7" showIcon="left" /> | 7 | 80% | — |
| elementium | <ItemLink id="ForbiddenMagic:WandCaps:5" showIcon="left" /> | 7 | 70% | Yaşayanodun veya Dreamwood gövdeyle eşleştirildiğinde Mana dönüşüm maliyetlerini düşürür |
| crimsoncloth | <ItemLink id="TaintedMagic:ItemWandCap:2" showIcon="left" /> | 6 | 80% | — |
| shadowmetal | <ItemLink id="TaintedMagic:ItemWandCap:0" showIcon="left" /> | 8 | 70% | — |
| ICHOR | <ItemLink id="ThaumicTinkerer:kamiResource:4" showIcon="left" /> | 8 | 70% | — |

2.9 sürümü bazı Forbidden Magic asa bileşenlerini güçlendirdi. İlgili değişiklikler için "2.9'da Yenilikler" altındaki "Asa Bileşeni Güçlendirmeleri" bölümüne bak.

### Bileşen Değişimi ve Asa Yükseltmeleri

Salis Arcana, **uçları ve gövdeleri veya uzun asa çekirdeklerini değiştirme** araştırmasını ekler; ilgili tarifler NEI'de bulunur. Değişim yeni bileşeni tüketir ve eskisini yok eder; hedef asayı doğrudan monte etmekle aynı Vis gereksinimini taşır.<br>
Kalıcı yükseltmeler korunur ve saltanat asası bileşenlerini değiştirmek yeni bir saltanat asası üretmek için gereken İlkel Tılsım'dan da tasarruf ettirir. Değişim bir asayı, saltanat asasını veya uzun asayı başka bir türe dönüştüremez.<br>
Asa yükseltmeleri infüzyon yoluyla takılır. Her yükseltme asa başına bir kez takılabilir ve farklı yükseltmeler bir arada bulunabilir.

- Şarj Tamponu: kapasiteyi %25 artırır
- Vis Kanalları: ekipman ve saltanat asası indirimlerinden önce uçların Vis maliyetini 0,9 ile çarpar
- Temas Deşarjı: asayla yapılan yakın dövüş saldırıları, sıradan zırhı yok sayan büyülü hasar vermek için Vis tüketir

## Vis Kaynakları

| Kaynak veya Tesis | Sağladığı Şey | Özellikler |
| --- | --- | --- |
| Sıradan aura düğümlerinden doğrudan çekme | Düğümde depolanan ilkel aspekt Vis'i | Kullanımı kolaydır ancak düğümün aspektleri, rezervi ve yenilenme hızıyla sınırlıdır |
| Aspekt küreleri | İlgili ilkel aspektin Vis'i | El çubuğundaki bir asa, o aspekt için yeri varsa yakındaki küreleri emebilir |
| İlkel Mantarlar | Olgun bitkiler hasat edildiğinde açığa çıkan aspekt küreleri | Rastgele aspekt çıktısı olan yenilenebilir bir ek kaynak |
| Özel gövdeler veya uzun asa çekirdekleri | Bileşenin belirlediği otomatik şarj veya dönüşüm | Yalnızca tek bir aspekti doldurabilir ya da düşük bir rezerv seviyesine kadar şarj edebilir |
| Asa Şarj Kaidesi | Bir asayı şarj etmek için yakındaki düğümlerden Vis çeker | Üs içi şarj için uygundur; bileşik aspekt kullanmak ek bir cihaz gerektirir |
| Enerjilendirilmiş düğümler ve Centi-Vis ağları | Sürekli Centi-Vis çıktısı | Sabit cihazlara güç verir ve uygun şarj tesisleri aracılığıyla asaları şarj edebilir |
| Esans Dinamosu | Esansı Centi-Vis'e dönüştürür | Bir tedarik ağı, şarj tesisleri ve ilgili materyallerin sürekli tedarikini gerektirir |

Aç düğümler, Ruhani Parçalar ve Güçlendirici arılar, kalıcı bir enerji kaynağı için düğümleri yetiştirme veya özelleştirme yolları sunar.

## Vishroom'lar, İlkel Mantarlar ve Aspekt Küreleri

<ItemLink id="Thaumcraft:blockCustomPlant:5" showIcon="left" /> Thaumcraft'ın Vishroom'udur ve <ItemLink id="thaumicbases:ashroom" showIcon="left" /> için bir bileşendir. **İlkel Mantarlar, olgunlaştıklarında hasat edilince Vis küreleri bırakan bitkilerdir.**

İlkel Mantar simya tarifi, katalizörü olarak bir Vishroom ile birlikte <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"perditio"}' scale="0.75" /> Entropi ve <ItemImage id='aspectrecipeindex:aspect:1:{Aspect:"messis"}' scale="0.75" /> Mahsul aspektlerini kullanır.<br>
Miktarlar için NEI'ye ve ilgili araştırmaya bak. Olgun bir bitkiyi sol tıkla kırmak, bitkinin kendisini ve her biri 1 Vis sağlayan 8–20 rastgele ilkel aspekt küresi düşürür. Bitki daha sonra yeniden dikilebilir.

İlkel Mantarların büyümesi zaman alır, altlarında tam bir destek bloğu olmalıdır ve üstlerinde en az 9 ışık seviyesi gerekir.<br>
Sağ tıkla hasat edilemezler ve olgunlaşmadan kırılmaları aynı Vis verimini sağlamaz. Onları yetiştirip hasat etmek tekrarlanabilir bir Vis kaynağı sunar.

Yaratıklar öldüklerinde aspekt küreleri de bırakabilir; bunlar, el çubuğunda ilgili aspekte yer olan bir asa tarafından emilir.

Sıradan element gövdeleri genellikle yalnızca tek bir aspekte ve kapasitelerinin yalnızca küçük bir bölümüne kadar şarj olur.<br>
Botania entegrasyon gövdeleri, şarj gereksinimleri karşılandığı ve Mana mevcut olduğu sürece Mana'yı Vis'e dönüştürebilir.

## Düğümleri Gözlemleme ve Rezervlerini Okuma

**Aura düğümleri** dünyadaki büyülü enerji yoğunlaşmalarıdır. Taranabilir ve asalar için Vis kaynağı olarak kullanılabilir. Bir <ItemLink id="Thaumcraft:ItemThaumometer" showIcon="left" /> ile gözlemlemek veya <ItemLink id="Thaumcraft:ItemGoggles" showIcon="left" /> takmak düğümlerin tanımlanmasını kolaylaştırır.

Bir düğümü incelerken dört tür bilgiyi göz önünde bulundur:

| Bilgi | Neyi Belirler |
| --- | --- |
| Aspekt bileşimi | Hangi ilkel aspektleri doğrudan sağlayabildiği ve başka kullanımlar için bileşik aspekt içerip içermediği |
| Mevcut rezerv | Hemen çekilebilecek Vis miktarı |
| Taban kapasite | Normal yenilenmesinin geri getirebileceği miktar; enerjilendirilmiş düğüm çıktısını da etkiler |
| Tür ve kalite | Özel davranış, yenilenme hızı ve dönüşüm sonrası performans |

NH'nin düğüm kayıtları daha önce taranan düğümleri yönetmeye yardımcı olur ve varsayılan olarak I tuşuyla açılabilir.

### Düğüm Türleri

Düğümlerin altı ana türü vardır. Tür bir sıralama değil, özel davranışı tanımlar; aynı türdeki düğümler farklı kalitelere ve aspekt bileşimlerine sahip olabilir.

<Column width="500" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_types.png" x="0" y="140" width="2170" height="440" displayWidth="500" wrap="inline" title="Aura Düğüm Türleri" />
</Column>

| Tür | Çekirdek Görünümü | Özellikler ve Dikkat Edilecekler |
| --- | --- | --- |
| Normal | Beyaz, kararlı çekirdekli | En yaygın sıradan düğüm; ek tür etkisi yoktur |
| Uğursuz | Koyu mor | Genellikle obsidyen totemler ve Eldritch yapılarıyla ilişkilidir; yakındaki biyomları değiştirir ve tehlikeli yaratıklar doğurabilir |
| Saf | Beyaz girdap | Genellikle Silverwood ağaçlarında bulunur; yakındaki biyomları Büyülü Orman'a çevirebilir ve Yozlaşma'yı sınırlamaya yardımcı olur |
| Lekeli | Mor pus | Lekeli Toprak ile ilişkilidir; Yozlaşma'yı ve ilgili tehlikeleri yayar |
| Kararsız | Beyaz, sürekli nabız atan çekirdekli | Aspekt küreleri salar ve Vis kaybeder; istikrarlı uzun vadeli enerji kaynağı olarak uygun değildir |
| Aç | Beyaz halka | Yakındaki varlıkları ve eşyaları içine çekip yutar, blokları yok eder; kapasitesi ona aspektli eşyalar verilerek yetiştirilebilir |

> [!WARNING]
> Aç düğümler eşyaları yutar, oyunculara zarar verir ve yakındaki blokları etkiler. Değerli eşyalar, düşen eşyalar ve üretim tesisleri kaybolabilir. Onları ayrı ve korunaklı bir alanda yetiştir ve değiştir.

## Düğüm Kalitesi ve Doğal Yenilenme

Düğüm kalitesi Normal, Parlak, Soluk veya Solan olabilir. Kalite yenilenmeyi tanımlar ve türden bağımsızdır; bir Saf düğüm aynı zamanda Parlak olabilir.

<Column width="400" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/aura_node_states.png" displayWidth="400" wrap="inline" title="Aura Düğüm Kalitesi" />
</Column>

| Kalite | Doğal Yenilenme | Görünüm |
| --- | --- | --- |
| Normal | Kabaca her 30 saniyede bir yenilenme olayı | Ek kalite adı yok |
| Parlak | Kabaca her 20 saniyede bir yenilenme olayı | Normal bir düğümden daha canlı |
| Soluk | Kabaca her 45 saniyede bir yenilenme olayı | Daha sönük |
| Solan | Vis'i doğal olarak yenilemez | Çok sönük ve sürekli titrer |

### Düğümlerden Çekim ve Düğüm Koruyucu

Asalar düğümlerden doğrudan ilkel aspekt çekebilir ancak bileşik aspektleri doğrudan depolayamaz. Yalnızca bileşik aspekt içeren bir düğüm, başka bir kullanım yöntemi gerektirir.

**Gelişmiş Düğüm Çekimi** ve **Usta Düğüm Çekimi**, çekim hızını sırasıyla normal hızın iki ve üç katına çıkarır.<br>
Bunlar aktarım hızını iyileştirir; düğümün doğal yenilenme hızını veya aspekt kapasitesini artırmaz.

**Düğüm Koruyucu**, normal çekim sırasında her aspekten en az 1 puan bırakarak düğümün tükenmesinden kaynaklanan hasar riskini azaltır.<br>
İstisnalar vardır: eğilmek korumayı atlar ve sıradan Ahşap gövde veya Demir uç kullanan düşük seviye asalar buna güvenemez.

> [!WARNING]
> Bir aspekti sıfıra kadar çekmek o aspekti yok edebilir veya düğümün kalitesine zarar verebilir. Her aspekti tüketmek düğümün kaybolmasına da neden olabilir.

## Düğümleri Taşıma, Sabitleme ve Yetiştirme

**Kavanozdaki düğümler** düğümleri taşımanın bir yolunu sunar. Kavanoza koymak hasar riski taşır ve kavanozlanmış düğümler Vis'i doğal olarak yenilemez, bu yüzden her an çekim yapılabilecek taşınabilir piller olarak işlev göremezler.

Kavanoza koymadan önce düğümün mevcut durumunu ve nasıl mühürlenip serbest bırakılacağını anlatan araştırmayı göz önünde bulundur. Üssüne taşındıktan sonra yakındaki düğüm etkileşimleri ve tehlikeli düğüm türleri de dikkat gerektirir.

- <ItemLink id="Thaumcraft:blockStoneDevice:9" showIcon="left" />: sabitlenen düğümün ve diğer düğümlerin birbirinden Vis çekmesini engeller, doğal yenilenmeyi yarıya indirir ve belirli olumsuz durumları kademeli olarak onarır
- <ItemLink id="Thaumcraft:blockStoneDevice:10" showIcon="left" />: düğümü tükenmeye karşı korurken daha az kararlı komşularından Vis çekmesine izin verir; doğal yenilenmeyi büyük ölçüde bastırır ve planlı düğüm yetiştirmeye daha uygundur

Düğüm Dengeleyicileri düğümün altında durur. **Bir dengeleyiciye kızıltaş uygulamak onu devre dışı bırakır**; düğümün üstündeki Düğüm Dönüştürücünün aksine, o etkinleşmek için kızıltaş gerektirir.

Daha büyük düğümler daha küçük komşularından Vis çekebilir; Aç düğümler ise tüketilen eşyaların aspektlerini emerek büyüyebilir.<br>
Yetiştirme zaman ve uygun koşullar gerektirir; herhangi iki düğümü yan yana koymak onları illa birleştirmez. Düğüm kalitesi, dengeleyiciler ve eşyalardaki aspektler bir yöntemin amaçlanan kullanıma uygun olup olmadığını etkiler.

## Düğüm Manipülatörleri ve Kalite Onarımı

<ItemLink id="thaumicbases:nodeManipulator" showIcon="left" /> ve **Düğüm Manipülatörü Odakları** düğümleri etkin biçimde değiştirme yolları sunar.<br>
Farklı odakların farklı etkileri vardır ve bunlar ilgili araştırmalarında açıklanır.

| Manipülatör Odağı | Kullanım |
| --- | --- |
| <ItemLink id="thaumicbases:nodeFoci:8" showIcon="left" /> | Solan ve Soluk kaliteleri onarır, Kararsız türüyle de ilgilenebilir |
| <ItemLink id="thaumicbases:nodeFoci:0" showIcon="left" /> | Normal kaliteyi Parlak'a yükseltir |
| <ItemLink id="thaumicbases:nodeFoci:7" showIcon="left" /> | Eksik Vis'i doldurur ve şarjı iyileştirir |
| <ItemLink id="thaumicbases:nodeFoci:2" showIcon="left" /> | Tüketimden sonra bir miktar Vis'i geri getirme şansı vardır, kapasiteyi artırmaz |

Manipülatör doğrudan düğümün üstünde durur ve takılı odağı aracılığıyla çalışır. Mevcut uygulamada, sabitleme odağının Solan kaliteyi Soluk'a onarması yaklaşık 5 dakika, Soluk'u Normal'e onarması yaklaşık 10 dakika sürer.<br>
Parlatma odağının Normal kaliteyi Parlak'a çevirmesi yaklaşık 20 dakika sürer. Bu süreler düğümün yüklü kalması ve oyunun normal hızda çalışması varsayımına dayanır.

Kaliteyi iyileştirmek yenilenmeyi artırır ve sonraki enerjilendirilmiş düğüm çıktısını iyileştirebilir, ancak aspekt türü eklemez veya taban kapasiteyi artırmaz.

Düğüm Manipülatörü ve Düğüm Dönüştürücü aynı anda düğümün üstündeki konumu kaplar, bu yüzden kalite ayarı ve sonraki dönüşüm ayrı aşamalardır.

### Taban Aspektleri Değiştirme ve Rastgele Düğüm Değişimi

Bir düğümün taban aspektlerini değiştirmek için <ItemLink id="gadomancy:BlockNodeManipulator:5" showIcon="left" /> da kullanabilirsin. Önceki manipülatörden farklı olarak **aspekt bileşimini, taban miktarlarını, kaliteyi veya türü rastgele değiştirir**.

| Olası Değişiklik | Neyi Değiştirir |
| --- | --- |
| Bileşik aspektleri ayırma | Bir bileşik aspektin taban miktarını bileşen aspektlerine aktarır |
| Aspektleri birleştirme | Bileşik aspektler oluşturmak için taban bileşimi değiştirir |
| Aspekt ekleme | Eksik ilkel aspektleri ekler |
| Kaliteyi değiştirme | Kalite iyileşebilir veya kötüleşebilir |
| Türü değiştirme | Ek Büyüyen türü de dahil olmak üzere başka bir tür üretebilir |

Her değişiklik, manipülatöre **her ilkel aspekten toplamda en az 70 Vis'in sağlanmasını** gerektirir; bu, içine yerleştirilen asa veya uzun asa tarafından ödenir.

Taban aspektleri değiştirmek uygun olmayan bileşimlere sahip düğümlere yardımcı olabilir, ancak rastgele değişiklikler olumsuz sonuçlar da doğurabilir.<br>
Altı aspektin tamamına sahip bir enerji kaynağı elde etmek için yapay düğüm özelleştirmesi, düğüm arıları ve kalite ayarının materyallerini, zamanını ve risklerini karşılaştır.

> [!WARNING]
> Düğüm Manipülatörünün rastgele değişiklikleri kaliteyi düşürebilir veya düğümün türünü değiştirebilir. Bir düğüm üzerinde kullanmadan önce bu riskleri değerlendir.

### Ruhani Parçalar ve Yapay Düğümler

<ItemLink id="ThaumicHorizons:synthNode" showIcon="left" /> yapay bir Vis kabıdır.<br>
Doğal düğümlerden farklı olarak **aspekt türleri ve kapasiteleri materyaller kullanılarak ayarlanabilir, ancak Vis'i kendi başına yenilemez** ve harici bir Centi-Vis tedariki gerektirir.

<ItemLink id="Thaumcraft:ItemWispEssence" showIcon="left" /> kapasitesini artırır. Her Ruhani Öz, kendi aspektinin kapasitesine 4 puan ekler ancak eklenen kapasiteyi doldurmaz.

Parçaya bileşik aspektler de eklenebilir. Bunları şarj etmek, tedarik ağının bileşen ilkel aspektlerini sağlamasını gerektirir; eksik tedarik bileşik aspekti tamamen şarj edemez.

**Ruhani Parçalar sıradan düğümleri özelleştirmek için de kullanılabilir.** Centi-Vis ile şarj edildikten sonra bir parça, kavanozlanmış bir düğüme mühürlenip sıradan bir aura düğümü olarak serbest bırakılabilir. Bu, materyallerle tanımlanmış bir bileşimi, doğal olarak yenilenebilen veya daha fazla değiştirilebilen bir düğüme dönüştürür.

Bu yöntem ilk şarj için enerjilendirilmiş bir düğüm veya <ItemLink id="ThaumicHorizons:essentiaDynamo" showIcon="left" /> gibi mevcut bir Centi-Vis kaynağı gerektirir.<br>
Bir Esans Dinamosu Centi-Vis üretmek için esans tüketir; asa Vis'ini tüketen bir dinamo ise enerji aktarır.

### Güçlendirici Arılar ve Düğüm Yetiştirme

Güçlendirici arılar arıcılığı büyülü enerji üretimine taşır. Etkiler, bölge genleri ve kovan çarpanlarından etkilenerek kovanın etkin çalışma alanı içinde işler; arının gerçekte miras aldığı etki genini kontrol et.

- Güçlendirme: bir aspektin taban kapasitesini ve mevcut rezervini rastgele artırır ve yeni aspektler ekleyebilir
- Gençleştirme: bu etkiyle kapasiteyi artırmadan mevcut Vis'i doldurur
- Nexus: kaliteyi Solan'dan Parlak'a kademeli olarak iyileştirir ve Kararsız türüyle de ilgilenebilir

Güçlendirici arılar aspektleri rastgele seçer; Nexus arılarının kalite iyileştirmeleri ise kapasite artışını tamamlayarak sonraki enerji çıktısını iyileştirebilir.<br>
Arı etkileri hedef düğüme ulaşmalıdır ve yetiştirme sürekli çalışma gerektirir.<br>
Kavanozlanmış düğümler bu şekilde yetiştirilebilir ancak Ruhani Parçalar gibi yapay kaplar hariçtir. Özelleştirilmiş bir düğümün, düğüm arıları onu etkileyebilmeden önce kavanozlama yoluyla dönüştürülmesi gerekir.

Endüstriyel Arı Evi hızlandırması yetiştirme hızını büyük ölçüde değiştirebilir. Arıcılık mekaniği, genetik ve hızlandırma gereksinimleri için Forestry içeriğine bak; bu sayfa onların düğümler üzerindeki etkilerine odaklanır.

### Enerjilendirilmiş Düğümler ve Centi-Vis

**Enerjilendirilmiş düğümler**, düğüm kullanımını kademeli çekim için Vis depolamaktan sürekli <Color color="#B7A0D6">Centi-Vis (CV)</Color> üretmeye dönüştürür.<br>
1 CV, 0,01 Vis'e eşittir ve düğümün gösterilen çıktısı oyun tiki başına ne kadar CV sağladığını belirtir.

<ItemLink id="Thaumcraft:blockStoneDevice:11" showIcon="left" /> dönüşümü gerçekleştirir. Düğümün altındaki dengeleyici işlem boyunca çalışmalıdır; düğümün üstündeki dönüştürücü ise kızıltaş ile etkinleştirilir. Dönüşümden sonra her iki tesis de gereken çalışma durumunda kalmalıdır.

**Dönüşüm, düğümün taban aspekt miktarlarını kullanır.** Bileşik aspektler de ilkel aspekt çıktısına katkıda bulunabilir, bu yüzden bileşik aspekt içeren bir düğüm yalnızca ilkel aspekt içeren bir düğümden illa daha kötü değildir.

Çıktı, düğümün rezerviyle doğru orantılı olarak artmaz. Aspektler önce ilkel aspektlere ayrıştırılır. Her ilkel aspekt için farklı kaynaklardan gelen en büyük katkı kullanılır, bunlar toplanmaz. Ardından kalite çarpanı uygulanır ve sonuç aşağı yuvarlanır; sonrasında karekök alınır ve tekrar aşağı yuvarlanır.

Örneğin Normal kalitede bir düğüm 100 Ateş ve 100 Enerji içerir. Enerji, Ateş ve Düzen'e ayrışır, bu yüzden etkin Ateş miktarı 200 değil 100 olarak kalır ve Ateş ile Düzen'in her biri 10 CV/t verir.<br>
Bu nedenle gösterilen tüm aspekt miktarlarını toplamak doğru çıktıyı vermez.

Parlak, Normal, Soluk ve Solan için kalite çarpanları sırasıyla 1,2, 1, 0,8 ve 0,5'tir ve karekök alınmadan önce uygulanır. Daha büyük düğümler genellikle daha fazla Centi-Vis sağlar.

**Enerjilendirilmiş düğümlerden asayla doğrudan çekim yapılamaz ve sıradan düğümler gibi yenilenmezler.** Enerjiyi Vis Röleleri ve ilgili cihazlar aracılığıyla sağlarlar. Çıktı altı aspektin her biri için ayrı ayrı sınırlı kalır, bu yüzden yüksek toplam çıktı eksik bir aspekti telafi edemez.

> [!WARNING]
> Enerjilendirilmiş bir düğümün altındaki dengeleyiciyi devre dışı bırakmak veya kırmak patlamaya ve Flux kirliliğine neden olur. Kurulumu sökmek için önce dengeleyiciyi etkin tutarak **dönüştürücünün** kızıltaş sinyalini kaldır. Tesisleri sökmeden önce düğüm tamamen sıradan biçimine dönene kadar bekle. Geri dönen düğüm tükenmiştir ve hâlâ hasar riski taşır, bu yüzden tekrar tekrar açıp kapatmaktan kaçın.

### Centi-Vis Ağları ve Otomatik Asa Şarjı

<ItemLink id="Thaumcraft:blockMetalDevice:14" showIcon="left" /> Centi-Vis iletir. Düğümler ve röleler arasındaki bağlantılar en fazla 8 blok mesafe ve engelsiz görüş hattı gerektirir. Röleler, tedariki üssün çevresindeki cihazlara uzatmak için diğer rölelere bağlanabilir.

Ağ bir ağaç yapısı kullanır: her rölenin bir üst kaynağı vardır ve birden çok alt cihaza tedarik sağlayabilir. Mesafe, bağlantılar ve her aspekt için mevcut çıktı bir cihazın enerji alıp almayacağını belirler.

| Şarj Tesisi | Kullanım |
| --- | --- |
| <ItemLink id="Thaumcraft:blockStoneDevice:5" showIcon="left" /> | Yerleştirilmiş bir asayı yakındaki sıradan düğümleri kullanarak otomatik şarj eder; GTNH ayrıca Centi-Vis ağından şarjı etkinleştirir |
| <ItemLink id="Thaumcraft:blockStoneDevice:8" showIcon="left" /> | Kaidenin sıradan düğümlerdeki bileşik aspektleri kullanmasını sağlar, dönüşüm kayıpları vardır |
| <ItemLink id="Thaumcraft:blockMetalDevice:2" showIcon="left" /> | Bir Gizemli Çalışma Tezgahının üstünde durur ve içindeki asayı şarj etmek için Centi-Vis kullanır |

Asa Şarj Kaideleri ve Tezgah Şarj Röleleri, düğüm enerjisini üste günlük üretim için kullanılabilir hale getirir.<br>
Sürekli kullanım için düğüm çıktısını, ağ bağlantılarını, asa kapasitesini ve üretim maliyetlerini birlikte değerlendir.

## Sık Karşılaşılan Sorunlar

| Belirti | Neye Bakmalısın |
| --- | --- |
| Uçlar ve gövde hazır ama asa üretilemiyor | Araştırmayı, Twilight Forest kupalarını, vida materyallerini ve gerçek Vis maliyetini kontrol et |
| Asa dolu ama gelişmiş bir asa üretemiyor | Her aspektin gerçek gereksinimini kapasiteyle karşılaştır; uç, ekipman ve saltanat asası indirimlerini kontrol et |
| İndirim ekipmanına rağmen Vis maliyetleri beklenenden yüksek | Demir uçlar maliyet cezası uygular ve farklı uçlar farklı aspektler için farklı çarpanlar kullanabilir |
| Bir uzun asa yüksek kapasiteli ama tezgahta kullanılamıyor | Uzun asalar gizemli üretimi desteklemez; bir asa veya saltanat asası kullan |
| Düğümde Vis var ama asa çekemiyor | Bileşik aspekt, kavanozlanmış düğüm veya zaten enerjilendirilmiş düğüm olup olmadığını kontrol et |
| Bir düğüm çok yavaş yenileniyor | Kaliteyi, dengeleyici etkilerini ve yakındaki düğümleri kontrol et; Solan kalite doğal olarak yenilenmez |
| Düğüm Koruyucu araştırmasına rağmen düğüm tükeniyor | Eğilip eğilmediğini veya sıradan Ahşap gövde ya da Demir uç gibi düşük kaliteli bileşenleri kontrol et |
| Dikilen Vishroom'lar Vis küresi üretmiyor | Vishroom bir bileşendir; olgun İlkel Mantarları hasat et ve boş kapasitesi olan bir asanın küreleri emmesini sağla |
| Ruhani Parçanın kapasitesi var ama asa Vis çekemiyor | Kapasite, mevcut rezerv değildir; önce eksiksiz Centi-Vis tedarikini sağla |
| Yapay düğüm kavanozlamadan sonra beklenenden küçük | Kavanozlama mevcut şarjlı miktarları kullanır; mühürlemeden önce gerçek rezervleri kontrol et |
| Güçlendirici arılarla yetiştirilen bir düğümün aspektleri dengesiz | Etki aspektleri rastgele artırır; yüksek toplam kapasite gerekli altı aspektin tamamının bulunduğunu garanti etmez |
| Düğüm dönüşümünden sonra orijinal tedarik yöntemi çalışmayı bırakıyor | Enerjilendirilmiş düğümler Centi-Vis ağları kullanır ve bunlardan asayla doğrudan çekim yapılamaz |
| Centi-Vis cihazları aralıklı çalışıyor | Ağ bağlantılarını, yüklü parçaları, aspekt çıktısını ve diğer cihazların rekabet eden tüketimini kontrol et |

</Column>