---
item_ids:
  - Thaumcraft:ItemEldritchObject:0
  - Thaumcraft:ItemEldritchObject:2
  - Thaumcraft:ItemEldritchObject:3
  - Thaumcraft:ItemSanityChecker
  - Thaumcraft:ItemSanitySoap
  - Thaumcraft:ItemBathSalts
  - WarpTheory:item.warptheory.paper
  - WarpTheory:item.warptheory.cleanser
navigation:
  title: Delilik ve Eldritch Bilgisi
  parent: ./index.md
  icon: 'Thaumcraft:ItemEldritchObject:0'
  position: 30
---

# Delilik ve Eldritch Bilgisi

<Column width="600" align="center" gap="8">

<Column width="300" align="center" wrap="top-bottom" gap="0">
  <FloatingImage src="/assets/images/thaumcraft_logo.png" x="50" y="132" width="2078" height="445" displayWidth="300" wrap="inline" title="Thaumcraft" />
</Column>

Eldritch bilgisi dünyanın en derin sırlarını araştırır, ancak öğrencilerini sık sık yoldan çıkarır.<br>
Yasak araştırmalara dalmak yavaş yavaş <Color color="#B7A0D6">Delilik</Color> biriktirir.<br>
Beraberinde getirdiği fısıltılar, halüsinasyonlar ve fiziksel değişimler de <Color color="#B7A0D6">Eldritch Çalışmaları</Color>'nda keşiflere yol açabilir.

Eldritch Çalışmaları; Hiçlik Metali, ilksel enerji ve Dış Topraklar'ın keşfini kapsar ve Gelişmiş Simya Fırını, İlksel Asa Çekirdeği ile sonraki KAMI araştırmalarına bağlanır.
GTNH'nin **Warp Theory** modu Delilik olaylarını genişletir ve kalıcı Delilik ile başa çıkma yolları sunar.

## Deliliğin Kaynakları ve Türleri

Thaumonomicon'da mor yasak bilgi uyarılarıyla işaretlenmiş araştırmalar başlıca Delilik kaynağıdır.<br>
Belirli eşyaları üretmek, bazı yiyecekleri yemek ve büyülü araçları kullanmak da Delilik ekleyebilir; araştırma girdilerindeki ve eşya ipuçlarındaki ilgili işaretlere bak.

| Tür | Özellikler | Tedavi |
| --- | --- | --- |
| **Geçici Delilik** | Delilik kontrolleri sırasında yavaş yavaş kaybolur | Bekle veya Dezenfektan Sabun gibi eşyalarla kaldır |
| **Yapışkan Delilik** | Doğal olarak kaybolmaz; normal Deliliğe de denir | Dezenfektan Sabun'ın azaltma şansı vardır; eklentilerdeki temizleyici eşyalar da kaldırabilir |
| **Kalıcı Delilik** | Sıradan Dezenfektan Sabun kaldıramaz | NH'de Saf Gözyaşı ve Arındırma Tılsımı gibi eşyalar kaldırabilir |

**Warping** özelliğine sahip ekipmanlar da olay hesaplamalarına Delilik ekler.<br>
Bu katkı hâlihazırda takılı veya elde tutulan eşyalardan gelir ve eşyalar çıkarıldığında kaybolur; temizleyici eşyalar özelliği ekipmanın kendisinden kaldırmaz.

**Deliliğini Kontrol Etmek**

GTNH'nin IGI katmanı Deliliği doğrudan gösterebilir. Ayrıca şu eşyalarla da kontrol edebilirsin:

- <ItemLink id="WarpTheory:item.warptheory.paper" showIcon="left" />: Kullanıldığında sohbette kalıcı, yapışkan ve geçici Delilik miktarlarını tam olarak gösterir. Renk değişimleri, yanma ve diğer tepkiler de tehlike seviyesini belirtir.
- <ItemLink id="Thaumcraft:ItemSanityChecker" showIcon="left" />: Elde tutulduğunda bir Delilik çubuğu gösterir. Koyu mor kalıcı Deliliği, açık mor yapışkan Deliliği, pembe ise geçici Deliliği temsil eder. Çubuk toplam 100'de doludur; daha yüksek değerleri kontrol etmek için turnusol kağıdı kullan.

## Delilik Olayları ve Zamanlayıcı

Thaumcraft'ın kendi Delilik olayları arasında Doğal Olmayan Açlık, Güneşin Gazabı, bulanık görüş, artan Vis maliyetleri ve yoğun siste beliren Eldritch Muhafızları bulunur. Bazı fısıltılar araştırma puanı veya yeni keşifler de verir.

- **Asandan Vis çekilmesi**, sonraki üretimi ve savaşı etkiler.
- **Envanter eşyalarının yer değiştirmesi veya karışması**, beraberinde rastgele ışınlanma ve olağandışı hareket.
- **Zehir, Wither, Körlük** ve diğer etkiler ya da Ateş Yarasalarının ve düşman yaratıkların ortaya çıkması.
- Kalıcı hasara yol açan olaylar, örneğin **geri sayımlı patlamalar, yakındaki blokların bozulması ve bir Wither çağırma**.

Olaylar rastgele kontrollerle tetiklenir. Mevcut olaylar ayrıca Delilik gücüne, zamanlayıcıya ve ayarlara bağlıdır.<br>
Aşağıdaki tablo, NH'nin varsayılan ayarlarındaki bazı olay eşiklerini listeler. Bir olayı seçmek için kullanılan **etkin güç**, mevcut Deliliğe ve zamanlayıcıya bağlıdır; yüz plakası gibi ekipmanlar bunu azaltabilir.

| Etkin Güç Eşiği | Ek Risk |
| --- | --- |
| 50 | Asandan Vis çekilmesi |
| 125 | Envanter eşyalarının yer değiştirmesi |
| 130 | Rastgele ışınlanma |
| 150 | Envanter eşyalarının karışması |
| 160 | Geri sayımlı patlama |
| 180 | Yakındaki blokların bozulması |
| 200 | Bir Wither çağırma |

Blok bozulması, olayın dönüştürebileceği blokları, bitkileri ve yaprakları etkiler; geri sayımlı patlamalar ve Wither'lar yakındaki yapılara daha fazla hasar verebilir.<br>
Delilik biriktirirken nerede durduğun da bu olayların ne kadar hasar verebileceğini belirler.

**2.9'da olay sönümü**

Yeni Delilik kazanmayı bıraktıktan sonra olaylar yavaş yavaş zayıflar; sıradan rastgele olaylar zamanlayıcı bitince durur.<br>
**Tekrar Delilik kazanmak zamanlayıcıyı yeniden etkinleştirir.** Yasak araştırmalar, ilgili üretimler ve diğer kaynaklar bu sessiz dönemi sona erdirebilir.<br>
Warping özelliğine sahip ekipmanlar olay gücünü etkiler ancak **zamanlayıcıyı sıfırlamaz**. Olaylar durduktan sonra mevcut yapışkan ve kalıcı Delilik kalır.

> [!WARNING]
> Yüksek Delilik olayları patlamalara, arazi hasarına veya oyuncunun yakınında bir Wither çağrılmasına neden olabilir. Büyük miktarda Delilik kazanırken, Eldritch keşiflerini beklerken veya geri tepmeli temizleyici eşyalar kullanırken önemli makinelerden, depolardan ve diğer oyuncuların yapılarından uzak dur.

## Delilik Kalkanı ve Belirti Giderme

<Color color="#B7A0D6">Delilik Kalkanı</Color>, süresi boyunca sıradan Delilik olaylarını engeller. Mevcut Deliliğin kalır; bu da onu üretim yaparken, keşfe çıkarken veya günlük işlerle uğraşırken olayları bastırmak için kullanışlı kılar.

**Arındırıcı Banyo Tuzları ve Gizemli Spa**

<ItemLink id="Thaumcraft:ItemBathSalts" showIcon="left" /> eşyasını suya atmak Arındırıcı Sıvı oluşturur. İçinde banyo yapmak Delilik Kalkanı verir; daha yüksek kalıcı Delilik koruma süresini kısaltır.

Bir <ItemLink id="Thaumcraft:blockStoneDevice:12" showIcon="left" />, su ve Arındırıcı Banyo Tuzları kullanarak üstündeki alandaki Arındırıcı Sıvıyı yeniler; üssünde korumayı yenilemenin pratik bir yolunu sunar.

Botania'nın <ItemLink id='Botania:brewFlask:0:{brewKey:"warpWard"}' showIcon="left" /> eşyası da Delilik Kalkanı sağlar. Normal bir şişeden alınan her doz 10 dakika koruma verir.

Takılı bir <ItemLink id="WarpTheory:item.warptheory.portableshower" showIcon="left" /> süresi dolduğunda Delilik Kalkanını yeniden uygular; Warping özellikli ekipmanı düzenli olarak giydiğinde kullanışlıdır.

<ItemLink id="thaumicbases:rosehipSyrup" showIcon="left" /> bulanık görüş, Doğal Olmayan Açlık ve Vis Tükenmesi gibi etkilerin seviyesini düşürür ve zaten en düşük seviyedeyse onları kaldırır. Bazı sıradan olumsuz iksir etkilerini de tedavi eder.

## Deliliği Azaltma ve Kaldırma

**Dezenfektan Sabun**

<ItemLink id="Thaumcraft:ItemSanitySoap" showIcon="left" /> kullanım animasyonunu tamamlamak tüm geçici Deliliği kaldırır ve yapışkan Deliliği 1 azaltma şansı vardır.

- Temel şans **%33**'tür.
- Delilik Kalkanı **25 puan** ekler.
- Arındırıcı Sıvı içinde durmak bir **25 puan** daha ekler; her iki koşul da sağlanırsa bu **%83** olur.

Animasyon bitene kadar sabunu kullanmaya devam et. Büyük miktarda yapışkan Deliliği kaldırırken Arındırıcı Sıvı içinde kullanmak malzeme tasarrufu sağlar.

**Thaumic Insurgence sabunları**

Thaumic Insurgence ek temizleme seçenekleri sunar:

- <ItemLink id="thaumicinsurgence:item.ItemSanitySoapAlpha" showIcon="left" /> (α sabunu): Ayrıca geçici Deliliği kaldırır ve yapışkan Deliliği 1 azaltma şansı vardır; temel şansı %50 ile daha yüksektir. Delilik Kalkanı ve Arındırıcı Sıvı bunu %100'e çıkarır.

- <ItemLink id="thaumicinsurgence:item.ItemSanitySoapBeta" showIcon="left" />: Başarılı olduğunda **1 kalıcı Deliliği 2 yapışkan Deliliğe** dönüştürür; bunlar daha sonra normal veya α sabunu ile kaldırılabilir. Temel şans %10'dur; Delilik Kalkanı ve Arındırıcı Sıvı her biri 15 puan ekler. Başarısızlık 2 geçici Delilik ekler.

**Saf Olmayan Gözyaşı**

<ItemLink id="WarpTheory:item.warptheory.cleanserminor" showIcon="left" />, kalıcı, yapışkan ve geçici Deliliğinin toplamı **en az 50** olduğunda 5 Delilik kaldırır.<br>
Önce geçici Deliliği, sonra yapışkan Deliliği, en son kalıcı Deliliği kaldırır. Yüksek Deliliği düşürebilir, ancak toplam eşiğin altına düştüğünde temizlemeye devam edemez. Araştırması Eldritch İdrakı, Gizemli Turnusol Kağıdı ve diğer önkoşulları gerektirir.

**Saf Gözyaşı**

<ItemLink id="WarpTheory:item.warptheory.cleanser" showIcon="left" /> biriktirilmiş tüm geçici, yapışkan ve kalıcı Deliliği tek seferde kaldırır.<br>
Güçlü etkisi nedeniyle araştırması Eldritch Vahyi, Ichor ve diğer önkoşulların arkasındadır ve zorlu malzeme gereksinimleri vardır.

**Deliliğini Temizle** görevi Saf Gözyaşı elde etmenin başka bir yolunu sunar. İlgili araştırmayı tamamlamamış olsan bile gerekli teslimleri ve ödülleri kontrol et.

> [!WARNING]
> Saf Gözyaşı, temizlemeden önceki Deliliğine bağlı olarak bir dizi geri tepme olayı sıraya koyar. **Delilik Kalkanı bu geri tepmeyi engelleyemez.** Kullandıktan sonra, yoğunlaşmış olaylar bitene kadar üssünden uzak dur.

**Arındırma Tılsımı**

Takılı bir <ItemLink id="WarpTheory:item.warptheory.amulet" showIcon="left" /> düzenli olarak Deliliği azaltmayı dener ve kalıcı Deliliği de yavaş yavaş kaldırır. Sürekli temizlik için uygundur.

Temizleme süreci yine de sıradan Delilik olaylarını sıraya koyar. Delilik Kalkanı bu olayları geciktirir; koruma bittikten sonra devam edebilirler; temizlik yaparken uygun bir yer seç.

## Eldritch Araştırmalarını Keşfetmek

İki Eldritch keşfi, Thaumcraft Delilik olayları sırasındaki rastgele kontrollerden gelir. **Oyuncunun kalıcı ve yapışkan Deliliğinin toplamını** kullanırlar:

- **Eldritch İdrakı**: Toplam **25'ten büyük** olduğunda açılabilir; Thaumonomicon'daki Eldritch sekmesini ortaya çıkarır ve Hiçlik Metali ile Akıl Sağlığı Ölçer gibi araştırma yollarını açar.
- **Eldritch Vahyi**: Toplam **50'den büyük** olduğunda açılabilir. Gözü Açmak ve bazı gelişmiş Eldritch araştırmaları için önkoşuldur.

Geçici Delilik ve ekipman Deliliği bu eşiklere sayılmaz. Gerekli miktara ulaşmak yine de rastgele bir kontrolü beklemen anlamına gelir, bu yüzden gereken süre değişir.

**Delilik Kalkanı bu kontrolü engeller.** Düzenli olarak Taşınabilir Duş takıyorsan veya başka bir koruma kaynağı sürdürüyorsan, onu çıkar ve Delilik olaylarına hazırlanmış bir alanda bekle.<br>
Keşifleri aldıktan sonra Deliliğini azaltabilirsin; açılan araştırmalar kullanılabilir kalır.

## Kızıl Tarikat ve Gözü Açmak

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_obelisk.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Sıradan Eldritch Dikilitaşı

</Column>

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/crimson_cult_obelisk.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Kızıl Tarikat Dikilitaşı

</Column>

</Column>

Keşfe çıkarken iki tür Eldritch Dikilitaşı bulabilirsin. Kızıl Tarikat dikilitaşlarının yakınında Kızıl Rahipler ve Kızıl Şövalyeler bulunabilir ve onları yenmek <ItemLink id="Thaumcraft:ItemEldritchObject:1" showIcon="left" /> kazanmanı sağlayabilir.<br>

İlgili düşmanları taramak araştırma ipuçlarının ortaya çıkmasına yardımcı olur. Kitabı elinde tut ve okumak için sağ tıkla; **Kızıl Tarikat** açılır.<br>
Kızıl Şövalyeler yakın dövüşte savaşır, Kızıl Rahipler ise menzilli büyü kullanır.

(Kızıl Rahipler kışkırtılmadan saldırmaz. Bazı rahipleri sağ bırakmak Kızıl Şövalyelerin sürekli doğmasını sağlar ve <ItemLink id="Thaumcraft:ItemEldritchObject:1" showIcon="left" /> elde etme fırsatlarını büyük ölçüde artırır.)

Ayin alanının çevresinde Eldritch Muhafızları da belirebilir. Bu bölgeler Kızıl Ayinler, Eldritch Gözleri ve ilgili taramalar için faydalı kaynaklardır.

**Kızıl Tarikat** ve **Eldritch Vahyi**ni tamamladıktan sonra Dış Topraklar'a erişim kazanmak için **Gözü Açmak** araştırmasını yapabilirsin.

Ayin, her iki türden de olsa doğal olarak oluşmuş sağlam bir Eldritch Dikilitaşı, tabanında Eldritch Sunağı ve üstünde Uğursuz Düğüm korunmuş olmasını gerektirir.<br>
Sunakta **4 <ItemLink id="Thaumcraft:ItemEldritchObject:0" showIcon="left" />** yerleştir, ardından bir asa ile sağ tıklayarak bir Eldritch Portalı aç.<br>
Ayinin temel gereksinimi, altı ilksel aspektin her birinden **100 Vis**'tir. **Gizemli üretim Vis indirimleri geçerlidir.**

Eldritch Gözleri, Eldritch Muhafızlarından düşebilir veya Gözü Açmak araştırmasını bitirdikten sonra İnfüzyon ile yapılabilir.<br>
Sunağın üstündeki düğüm portalın açılmasına katılır; onu şişelemek veya dönüştürmek ayini etkiler.

Gadomancy, bir Düğüm Manipülatörü ve bir Yönlendirme Odağı kullanılarak inşa edilen yapay bir giriş olan **Hiçlik Yürüyücülerinin Kapısı**nı sunar.<br>
Ayrıca Eldritch Gözleri ve asa Vis'i gerektirir. İlgili araştırma yapısını gösterir.

> [!WARNING]
> Hiçlik Yürüyücülerinin Kapısı yalnızca tek bir varlığın geçmesine izin verir, ardından giriş kaybolur. Başka bir dönüş yolu hazırla ya da ayrılmadan önce Dış Topraklar mücadelesini tamamlamaya hazır ol.

## Dış Topraklar'ı Keşfetmek

<Color color="#B7A0D6">Dış Topraklar</Color>, Antik Taş'tan inşa edilmiş ayrı bir labirenttir. Koridorlar; düşmanlar, Antik Küpler, araştırma ipuçları ve boss alanları içeren odaları birbirine bağlar. Bir sefer genellikle anahtar odasını bulmayı, bir Rünlü Tablet elde etmeyi, bir boss odasını açmayı ve bir İlksel İnci ile geri dönmeyi içerir.

Bir Eldritch Portalı'ndan girmek **Dış Topraklar** araştırmasını verir. Özel bloklar ve glifler daha fazla araştırma ipucu ortaya çıkarır; bir inci elde etmek Thaumonomicon'da ek Eldritch ve eklenti araştırma yolları açar.

**Labirent ve araştırma ipuçları**

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_key_room.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

<Column width="120" align="center" gap="0">

Anahtar Odası

</Column>

</Column>

- <ItemLink id="Thaumcraft:blockEldritch:5" showIcon="left" /> ve <ItemLink id="Thaumcraft:blockCosmeticSolid:11" showIcon="left" />: Dış Topraklar'a girdikten sonra **Dış Topraklar'daki Vahiyler**i keşfetmek ve labirent hakkında daha fazla bilgi edinmek için bunları tara.
- **Kütüphaneler ve diğer özel odalar**: Düzenleri sıradan koridorlardan farklıdır ve araştırmayla ilgili özel bloklar ve ganimet içerir.
- **Antik Küpler**: Koridorlarda ve odalarda bulunur, kırıldığında ganimet bırakır. Boss odalarının çevresinde daha kaliteli küpler de görünebilir.
- **Anahtar odaları**: Merkezi taş kaidenin üzerinde, Eldritch Muhafızları tarafından korunan bir Rünlü Tablet süzülür. Bu odalar doğal olarak oluşan tabletlerin kaynağıdır.
- **Boss odası girişleri**: Bir Antik Kilitleme Mekanizması etkinleşmek için Rünlü Tablet gerektirir.

Labirentteki düşmanlar arasında Eldritch Muhafızları, Sürünen Kabuklar ve Eldritch Yengeçleri bulunur. Dar koridorlar menzilli saldırıları ve hareketi etkiler; yoğun sis, olumsuz etkiler ve dallanan yollar da keşfi yavaşlatabilir.

Dış Topraklar, yaygın yaratıcı uçuş biçimlerini ve Thaumcraft havada süzülmesini kısıtlar; bu yüzden koridorlar boyunca yükseklik değişimleri önemlidir.<br>
Girişi, keşfedilen dalları ve boss odalarını işaretlemek geri dönüş yolunu bulmana yardımcı olur.

## Rünlü Tabletler ve Antik Kilitleme Mekanizmaları

Bir <ItemLink id="Thaumcraft:ItemEldritchObject:2" showIcon="left" />, bir Dış Topraklar boss odasını açmanın anahtarıdır.<br>
Doğal olarak oluşan tabletler, bu iş için ayrılmış anahtar odalarının merkezinde görünür. Bulmak için labirenti ara, sonra onu bir boss odası girişine götür.

Gözü Açmak'ı tamamladıktan sonra **Rünlü Tablet** araştırmasını yapabilir ve İnfüzyon ile tablet üretebilirsin. Araştırmanın kendisi 5 Delilik ekler ve tarifin kararsızlığı **10**'dur.

Ana bileşenler şunlardır:

- <ItemLink id="DraconicEvolution:infoTablet" showIcon="left" /> merkezi bileşen olarak.
- **2 Eldritch Gözü** ve **4 Hiçlik Tohumu**.
- <ItemLink id="ThaumicExploration:pureZombieBrain" showIcon="left" />.
- <ItemLink id="Automagy:crystalBrain:3" showIcon="left" />.

<Column width="240" align="right" wrap="square" alignItems="center" gap="4">

<GameScene interactive={true} width="240" height="280" showBackground={false} allowLayerSlider={false} gridButtonEnabled={false}>
  <ImportStructure src="/assets/structures/eldritch_boss_door.snbt" />
  <IsometricCamera yaw="90" pitch="0" />
</GameScene>

<Column width="120" align="center" gap="0">

Boss Odası Kapısı

</Column>

</Column>

Esans gereksinimleri **128 Praecantatio, 64 Alienis, 64 Cognitio, 32 Iter, 32 Tenebrae ve 32 Vacuos**'tur.<br>
Üretilmiş tabletler, malzemelere ve Esans tedarikine sahip olduğunda kullanışlıdır; her seferde anahtar odası aramak için harcanan süreyi azaltır.

**Kullanım ve tüketim**

Kilitleme mekanizmasına bir tabletle sağ tıklamak **1 tablet** tüketir. Kısa bir şarj süresinden sonra mekanizma odayı dönüştürür ve mücadelesini oluşturur.

Her mekanizma yalnızca bir kez etkinleştirilebilir. Daha fazla tablet elde ettikten sonra yeni labirentlerde açılmamış boss odaları ara.<br>
Dış Topraklar mücadeleleri arasında bir Eldritch Yapıtı, bir Eldritch Bekçisi, Kızıl Tarikat ve Lekelenme bulunur. Oda türü dünya oluşumu tarafından belirlenir.

## Dış Topraklar'daki Boss Mücadeleleri

**Eldritch Yapıtı**

Yapıtın iki savaş formu vardır. Başlangıçtaki bedenini yenilgiye uğratacak bir saldırı, onun kafasını dökmesine ve kafasız bir forma geçerek savaşa devam etmesine neden olur.<br>
Kafasını kaybetmesi ayrıca bir patlamaya neden olur. İlksel İnci elde etmek için dönüşmüş bedeni yenilgiye uğrat.

Bu dönüşüm savaşın ritmini böler; yakın mesafede savaşırken patlamaya ve sonraki saldırılara dikkat et.

**Eldritch Bekçisi**

Bekçi ağırlıklı olarak menzilli Eldritch mermileriyle saldırır ve Wither, Zayıflık ve diğer etkileri uygulayabilir.<br>
Ek soğurma canıyla ortaya çıkar. Bu kalkanı tüketmek bir çılgınlığı tetikler; onu kısa süreliğine dokunulmaz yapar ve bir kuvvet alanı oluşturur.

Mermilerinden ve kuvvet alanından kaçmak için yeterli alan bırak. Bekçiyi yenmek bir İlksel İnci ve bir Nadir Hazine Çuvalı verir.

**Kızıl Tarikat**

Odanın merkezindeki Kızıl Portalı sürekli Kızıl Şövalyeler ve Rahipler, ardından bir Kızıl Praetor çağırır. Praetor yakındaki tarikat üyelerinin sağlığını yeniler; önce onunla ilgilenmek kalan düşmanları temizlemeyi kolaylaştırır.

Portalın, praetor ortaya çıkmadan önce güçlü bir can yenilenmesi vardır. **Bu odadaki İlksel İnci, yenilgiye uğratılması gereken Kızıl Portalı'ndan düşer.** Praetor ayrıca bir Nadir Hazine Çuvalı düşürür.

**Lekelenme**

Bu odalar lekeli arazi ve Dev Leke Dokunaçları da dahil olmak üzere birkaç dokunaç içerir. Saldırıları ve lekeli çevre hareketi aksatır; bu yüzden onları temizlerken ayak basışına ve diğer dokunaçlardan gelen saldırılara dikkat et.

Yenilen son Dev Leke Dokunacı bir İlksel İnci düşürür. Yalnızca birini yenmek odada başka Dev Leke Dokunaçları bırakabilir.

Dış Topraklar seferi sırasında Delilik Kalkanını koru ki savaş esnasında ek Delilik olayları azalsın. Mücadeleyi tamamladıktan sonra ayrılmak için dönüş portalını kullan.

### Hiçlik Metali ve İlksel Enerji

**Hiçlik Metali**

Eldritch İdrakı ve Thaumium araştırmasından sonra Hiçlik Metali araştırmasını yapabilirsin. <ItemLink id="Thaumcraft:ItemResource:17" showIcon="left" />, <ItemLink id="Thaumcraft:ItemResource:16" showIcon="left" /> yapımında kullanılır ve ayrıca Eldritch Gözleri, Rünlü Tabletler ve çeşitli eklenti cihazları için gereklidir.

Hiçlik Metali birkaç yol açar:

- **Hiçlik Metali aletleri ve zırhı**: Bazı aletler ve ekipmanlar kendi dayanıklılığını onarır ve Warping özelliğine sahiptir.
- **Hiçlik Metali asa uçları**: Asa Vis maliyetlerini azaltır ve daha ileri asa yükseltmelerini destekler.
- **Gelişmiş Esans depolaması**: Tek tek aspektler için depolama kapasitesini genişletir ve daha büyük simya ve infüzyon tariflerini destekler.
- **Hiçlik Thaumaturge Cübbeleri**: Korumayı, Vis indirimlerini ve Hakikat Gözlüğü'nünkiler gibi yetenekleri birleştirir.
- **Eklenti malzeme yolları**: Gölge Metali, Gölge Kale ekipmanı ve İlksel ekipman araştırmaları Hiçlik Metali keşiflerinin üzerine inşa edilmeye devam eder.

**İlksel enerji ve İlksel Asa Çekirdeği**

<ItemLink id="Thaumcraft:ItemResource:15" showIcon="left" />, Eldritch üretiminde önemli bir bileşendir; Eldritch Gözleri, İlksel Kırıcı ve birkaç gelişmiş büyülü tarif için kullanılır.

**Asa Odağı: İlksel**, çevreye hasar verebilen güçlü ilksel enerji küreleri fırlatır. Hem odak hem de küreleri, İlksel Asa Çekirdeği'nin tarama önkoşullarının bir parçasıdır.<br>
Asa çekirdeği, birkaç elemental asa çekirdeği araştırmasının üzerine inşa edilir. Kapasitesi, şarjı ve önkoşulları için [Asalar, Vis ve Düğümler](./wands_vis_nodes.md) sayfasına bak.

## İlksel İnciler ve Araştırma Kullanımları

Bir <ItemLink id="Thaumcraft:ItemEldritchObject:3" showIcon="left" />, Dış Topraklar'dan gelen önemli bir ödül ve daha gelişmiş Eldritch cihazları geliştirmek için kilit bir malzemedir.<br>
Onu taramak **İlksel İnci** araştırmasını ortaya çıkarır; bu da Gelişmiş Simya Fırını, İlksel Kırıcı, İlksel Düğüm Manipülasyonu ve birkaç eklenti araştırma yoluna bağlanır.

**Gelişmiş Simya Fırını**

Gelişmiş Simya Fırını, Ignis, Perditio ve Aqua Centi-Vis kullanarak esans çıkarımının tamponunu ve işleme kapasitesini artırır.<br>
Araştırması ayrıca Esans Damıtma ve Centi-Vis gücü bilgisini gerektirir. Yapıtlar ve fırın hazır olduğunda, büyük infüzyon tariflerinin taleplerini karşılamak için mevcut esans depolamasına ve lojistiğine bağlanabilir.

Bileşenleri, girdileri, çıktıları ve güç kaynağı için [Simya ve Esans](./alchemy_essentia.md) sayfasına bak.

**İlksel Kırıcı**

<ItemLink id="Thaumcraft:ItemPrimalCrusher" showIcon="left" />, Toprak Taşıyıcının Küreği, Çekirdek Kazması ve Hiçlik Metali aletlerinin yeteneklerini birleştirir. **3×3**'lük bir alanda toprak ve taş kazar ve uygun cevherleri Doğal Kümeler'e dönüştürme şansı vardır.<br>
Kendi dayanıklılığını onarır; bu da onu büyük kazılar kadar savaş için de kullanışlı kılar.

**İlksel Eldiven ve eklenti cihazları**

Witching Gadgets'in <ItemLink id="WitchingGadgets:item.WG_PrimordialGlove" showIcon="left" /> eşyası bir aura düğümü barındırır ve onu yuvaya takılı İnfüzyonlu Mücevherleri şarj etmek için kullanır. Yuvaları mücevherleri stabilize eder ve şarj edildikten sonra yeteneklerinin yeniden kullanılmasını sağlar.

İnciler ayrıca gelişmiş yüzükler, İlksel ekipman ve Thaumic Horizons ile Tainted Magic gibi eklentilerin içeriği için kullanılır.<br>
Bu yollar önemli miktarda esans ve gelişmiş malzeme tüketir. İstikrarlı bir inci tedariki, üretim cihazlarını, aletleri ve korumayı ayrı ayrı geliştirmeni sağlar.

### İlksel Düğüm Manipülasyonu

**İlksel Düğüm Manipülasyonu** araştırması, sıradan aura düğümlerini incilerle değiştirmenin bir yolunu sunar. Bir düğümde İlksel İnci kullanmak inciyi tüketir ve düğümün temel aspekt miktarlarını değiştirir; kalitesini iyileştirme şansı vardır.

- **Mevcut ilksel aspektlerin** temel miktarları artabilir veya azalabilir.
- **Eksik ilksel aspektlerin** eklenme şansı vardır.
- **Bileşik aspektlerin** temel miktarları azalabilir.
- **Sönümlenen, Solgun veya Normal kalitedeki** düğümlerin iyileşme şansı vardır.

Bir inci, bu araştırma tamamlanmadan önce bile bir düğümle tepkimeye girebilir; araştırmayı tamamlamak bazı olumlu değişikliklerin şansını artırır. Yerleşik bir inci tedarikiyle bu, hem rastgele sonuçları hem de inci maliyetlerini hesaba katarak düğümleri değiştirmenin başka bir yolunu sunar.

Özel düğümler, Düğüm Manipülatörleri ve Enerjilendirilmiş Düğümler için [Asalar, Vis ve Düğümler](./wands_vis_nodes.md) sayfasına bak.

## İstikrarlı İlksel İnci Tedariki Sağlamak

**İlksel Meyve**

CropsNH'nin **İlksel Meyvesi**, olgunlaştığında hasat edildiğinde inci üretir. İlk mahsulü oluşturmak için tohum olarak Ekin Çubuklarına bir İlksel İnci dik.

- İlksel Meyve melezleme yoluyla elde edilemez, doğal olarak yayılmaz ve diğer bitkilerle çaprazlanamaz.
- İstatistiklerini iyileştirmek **Ekin Gen Çıkarıcısı ve Ekin Sentezleyicisi** gibi cihazlar gerektirir.
- Tercih ettiği biyom etiketleri arasında **End ve Büyülü** bulunur. Mahsul hastalığını önlemek için en az bir uygun biyom etiketi veya yeterli biyom nemi gerekir.
- Uzun bir büyüme döngüsü vardır ve uygun hızlandırma ile istikrarlı bir büyüme ortamına ihtiyaç duyar.

**İnci parçalarını yeniden birleştirme**

GTNH ayrıca bir <ItemLink id="dreamcraft:PrimordialPearlFragment" showIcon="left" /> yolu sunar: bir İlksel İnciyi Dövme Çekiç'te işlemek **3 parça** üretir. İlgili Witching Gadgets araştırması ve infüzyon tarifi daha sonra her parçayı tekrar bir inciye dönüştürür.

Yeniden birleştirme araştırması İlksel İnci ve Ichor ile ilgili önkoşulları gerektirir. Tarifi Eldritch Gözleri, Ichor malzemeleri, Aurora Blokları ve büyük miktarda esans tüketir; kararsızlığı **20**'dir.<br>
Bu yol bir inciyi birkaç taneye dönüştürür; eksiksiz bir Ichor malzeme tedarikine ve infüzyon altyapısına sahip olduğunda uygundur.

## İnci Diriltme ve Aşırı İlksel İnci

**Witching Gadgets'te İnci Diriltme**

İlksel ekipman için bazı Witching Gadgets tarifleri inciden enerji çeker ve geride bir <ItemLink id="WitchingGadgets:item.WG_Material:12" showIcon="left" /> bırakır.<br>
**İnci Diriltme** araştırmasını tamamladıktan sonra infüzyon onu tekrar bir İlksel İnciye dönüştürebilir.

Tarif, altı ilksel aspektin her birinden bir parça ve bir <ItemLink id="Thaumcraft:blockCrystal:6" showIcon="left" /> kullanır. **Her ilksel aspektten 64 esans** ve **384 Praecantatio** gerektirir; kararsızlığı **10**'dur.<br>
İlksel Eldivenler, silahlar ve zırh üretirken bu artık inciler malzeme tedarikine geri kazandırılabilir.

**Aşırı İlksel İnci**

<ItemLink id="Avaritia:big_pearl" showIcon="left" />, Avaritia'nın Thaumcraft ile entegrasyonundan gelir ve İlksel İnci araştırmasından sonra açılır.<br>
İnfüzyonu merkezi bileşen olarak bir sıradan İlksel İnci ve çevresinde **7 tane daha** kullanır; toplamda **8 inci** tüketir.

Bu infüzyonun kararsızlığı **12**'dir ve altı ilksel aspektin her birinden, Alienis ve Praecantatio'dan 64'er esans ile 32 Terminus gerektirir. Seri üretim, ilgili esans rezervlerini ve sunak kararlılığını gerektirir.

Sonraki tariflerde katalizör olarak kullanıldığında Aşırı İlksel İnci korunabilir. Akaşik Kayıt ve birkaç Sonsuzluk ekipman tarifi için kullanılır. Yığılmaz; aynı anda birkaç inci gerektiren tarifler o kadar ayrı inciye ihtiyaç duyar.

## Daha Fazla Koruma: İlksel Zırh

**İlksel Zırh**; <ItemLink id="WitchingGadgets:item.WG_PrimordialHelm" showIcon="left" />, <ItemLink id="WitchingGadgets:item.WG_PrimordialChest" showIcon="left" />, <ItemLink id="WitchingGadgets:item.WG_PrimordialLegs" showIcon="left" /> ve <ItemLink id="WitchingGadgets:item.WG_PrimordialBoots" showIcon="left" /> parçalarından oluşur.<br>
Malzeme yolu Gölge Kale ekipmanı, Hiçlik Metali ve incileri kullanır; bu da gelişmiş büyülü koruma geliştirirken onu değerlendirmeye değer kılar.

Her parça, elinde tutarken gizlice sağ tıklayarak bağımsız şekilde bir **ilksel yakınlığa** ayarlanabilir. Aynı aspekte ayarlanmış birkaç parça, bazı yeteneklerin gerektirdiği eşya sayılarını da karşılar.

- **Aer yakınlığı**: Mermileri yansıtır; en az iki Aer'e ayarlanmış parça yaratıcı uçuş sağlar.
- **Terra yakınlığı**: Yaralandığında yenilenme verir; botlar ayrıca geri savrulma direnci sağlar.
- **Ignis yakınlığı**: Seni otomatik olarak söndürür ve ateş ile patlama hasarını azaltır; kask Gece Görüşü sağlayabilir.
- **Aqua yakınlığı**: Birkaç olumsuz etkiyi kaldırır; kask Su Altında Nefes Alma ve su altında Gece Görüşü sağlayabilir.
- **Ordo yakınlığı**: Yenilenme sağlar ve Thaumcraft'ın Delilikle ilgili olumsuz durum etkilerinin seviyesini ve süresini azaltır.
- **Perditio yakınlığı**: Vurulduğunda saldırganlara Körlük ve Yavaşlık uygular.

İlksel Kask ayrıca Warp Theory olaylarının etkin gücünü azaltır. Düzenli olarak giyerken, ekipmanının katkıda bulunduğu Deliliği yönetmek için Taşınabilir Duş gibi bir korumayla birleştir.

</Column>