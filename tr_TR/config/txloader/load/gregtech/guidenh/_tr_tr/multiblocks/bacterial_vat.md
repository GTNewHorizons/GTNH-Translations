---
item_ids:
  - gregtech:gt.blockmachines:12712
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKAQ==
navigation:
  title: Bakteriyel Küvet
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:12712
  position: -3001
---
# Bakteriyel Küvet

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12712" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" /> (BV), sıvıları toplu halde fermente etmek için kullanılan HV kademesi multibloklardan biridir.

Küvetin içindeki bakteriler organik bileşikleri yeni bir şeye ayrıştırır; örneğin Saccharomyces Escherichia üzüm suyunu şaraba dönüştürür. Bakteri türü ve dolayısıyla tarif, makinenin kontrolcü bloğunun içine kültür içeren bir petri kabı yerleştirilerek belirlenir.

Fermantasyon sürecinin kendisi çevrenin taşıma kapasitesine sıkı sıkıya bağlıdır; bu da maksimum büyüme ve verimlilik için çıkış kapağının mümkün olduğunca %50 dolulukta kalması gerektiği anlamına gelir.

BV, UV'de ilerlemek için zorunlu olsa da oyuncu gerekli tüm sıvıları daha sonra Kuantum kuvvetiyle çalışan [<ItemLink id="gregtech:gt.blockmachines:31151" showIcon="left" />](./quantum_force_transformer.md) makinesinde üretebilir.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılış Kademesi | HV |
| Yapı Boyutu (UxGxY) | 5x5x4 |
| Güç | Normal |
| Hız Aşırtmalar | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

### Üretim
<RecipesFor id="gregtech:gt.blockmachines:12712" />

<RecipesFor id="gregtech:gt.blockcasings4:1" />

<ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> atlanabilir ve yalnızca radyasyon gerektiren tarifler için gereklidir.

<RecipesFor id="gregtech:gt.blockmachines:12713" />

### Yapı

BV'nin kademeli tek bir bileşeni vardır. Cam, **maksimum tarif kademesini belirler, ancak maksimum enerji kapağı kademesini belirlemez**.

BV döndürülebilir veya çevrilebilir.

Çok amperli ve lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı bulunabilir.

Yalnızca bir çıkış kapağı ve bir radyo kapağına izin verilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> öğesini "glass" alt kanalıyla kullanarak camın kademesini belirt.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" /> | 1, Ön alt orta |
| <ItemLink id="gregtech:gt.blockcasings4:1" showIcon="left" /> | 19-45, 1. ve 4. katmanın tamamı |
| <ItemImage id="bartworks:BW_TieredGlass" /><Color id="blue">Kademeli</Color> Cam | 32, 2. ve 3. katman, merkezi içi boş olacak şekilde |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, Herhangi bir kasanın yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, Herhangi bir kasanın yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 0+, Herhangi bir kasanın yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 1+, Herhangi bir kasanın yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 0+, Herhangi bir kasanın yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Çıkış Kapağı | 1, Herhangi bir kasanın yerine geçebilir |
| <ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> | 0-1, Herhangi bir kasanın yerine geçebilir |

### Duvar Paylaşımı

BV'ler cam, kasa ve yol/kapak tasarrufu sağlamak için her bir yüzünü duvar paylaşımıyla kullanabilir. Bu, otomasyon düzeneklerini basitleştirmeye ve radyoaktif malzemelerden tasarruf etmeye yardımcı olan çıkış kapağı ile radyo kapağı için de geçerlidir. Dört makine arasında paylaşım yapılıyorsa bir kapak üste, diğeri alta konabilir.

Hiçbir tarif 1A'dan fazla güç kullanmadığından bir enerji kapağı iki makine arasında paylaşılabilir.

## Kullanım
BV tariflerinin çalışması için 4 gereksinim vardır: Cam Kademesi, Gerilim, Kültür ve Radyoaktiflik.

Bu gereksinimleri NEI'de kontrol edebilirsin. Örneğin aşağıdaki tarif şunları gerektirir:
- EV+ Cam Kademesi
- HV+ Gerilim
- En az 83 sievert gerekir
- <ItemImage id="bartworks:BioLabParts" nbt='tag:{Name:"Binni Bacteria"}' label="right" /> gerektirir

<RecipeFor id="NotEnoughItems:neiFluidDisplay:94" />

Bunun, çalışması için en az EV kademesi cam gerektirmesine rağmen bir HV tarifi olduğunu unutma.

### Kültür
Tüm BV tarifleri, kontrolcü bloğunun içinde kültür içeren belirli bir petri kabı gerektirir. Petri kapları, biyoteknolojiyle ilgili tüm tarifler için kullanılan HV+ tek bloklu makinesi olan [<ItemImage id="gregtech:gt.blockmachines:12699" noTooltip />Bio Lab](/singleblock/bio_lab.md) makinesinden elde edilir.

Kültür içeren bir petri kabının nasıl üretileceği hakkında daha fazla bilgi için [<ItemImage id="gregtech:gt.blockmachines:12699" noTooltip />Bio Lab](/singleblock/bio_lab.md) rehberine bakabilirsin.

### Radyo Kapağı
Birkaç egzotik ve yabancı bakteri türü hayatta kalmak için radyasyon gerektirir; bu da radyoaktif malzemelerin çubuklarını veya uzun çubuklarını içeren bir radyo kapağı aracılığıyla sağlanır.

<ItemLink id="gregtech:gt.blockmachines:12713" showIcon="left" /> bir giriş yoluna benzer, ancak tarif çalışsın ya da çalışmasın eşyaları sürekli tüketir. Neyse ki radyo kapağı bir makine kontrolcü kapağı ile istediğin zaman devre dışı bırakılabilir.

Radyo kapağının içindeki radyoaktif malzeme, radyasyonun sievert (sv) cinsinden gücünü belirler, ancak yerleşik radyasyon panjuru bunu isteğe bağlı bir miktarda azaltabilir. Sievert değerini azaltmanın, belirli bir tarif için tam bir miktara ihtiyaç duymak dışında bir faydası yoktur; çünkü yüksek sievertli malzemelerin yaşam ömrü genellikle daha kısadır.

Radyasyon panjurunu, radyo kapağı arayüzünün sol üst köşesindeki tornavida düğmesine<FloatingImage src="gregtech:textures/gui/overlay_button/screwdriver.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} /> tıklayarak kontrol edebilirsin.

Farklı malzemelerin yaşam ömürleri de farklıdır, ancak çoğu oldukça kısadır. Aşağıdaki tablo, birçok radyoaktif malzemeden birkaçını güç, yaşam ömrü ve kütleye göre listeler.

<Column width="380">
  | Malzeme | Güç | Yaşam ömrü | Kütle |
  |----------|----------|-----------|------|
  | <ItemLink id="gregtech:gt.metaitem.01:23090" showIcon="left" /> | 83 sv | 198.80 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22090" showIcon="left" /> | ^^ | 397.60 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23096" showIcon="left" /> | 90 sv | 98.75 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22096" showIcon="left" /> | ^^ | 197.50 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23097" showIcon="left" /> | 92 sv | 80.850 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23098" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.02:22097" showIcon="left" /> | ^^ | 161.70 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22098" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.01:23100" showIcon="left" /> | 94 sv | 66.20 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23101" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.02:22100" showIcon="left" /> | ^^ | 132.40 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22101" showIcon="left" /> | ^^ | ^^ | ^^ |
  | <ItemLink id="gregtech:gt.metaitem.01:23103" showIcon="left" /> | 95 sv | 59.90 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22103" showIcon="left" /> | ^^ | 119.80 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23324" showIcon="left" /> | 130 sv | 14.40 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22324" showIcon="left" /> | ^^ | 28.80 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23326" showIcon="left" /> | 140 sv | 10.65 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22326" showIcon="left" /> | ^^ | 21.70 s | 2 kg |
  | <ItemLink id="gregtech:gt.metaitem.01:23327" showIcon="left" /> | 150 sv | 7.85 s | 1 kg |
  | <ItemLink id="gregtech:gt.metaitem.02:22327" showIcon="left" /> | ^^ | 15.70 s | 2 kg |
  {: widths="200, 60, 60, 60"}
</Column>

Ses susturmayı, kapak arayüzündeki ses düğmesine tıklayarak veya radyo kapağına çekiçle sağ tıklayarak aktifleştirebilirsin.

### Çıktı oranı

BV, bakterilerin çoğalması için sınırlı bir taşıma kapasitesine (K) sahip kapalı bir sistemdir. Tüm kapalı sistemler sigmoidal bir popülasyon eğrisi izler; yani büyüme hızı, küçük başlangıç popülasyonu nedeniyle başlangıçta yavaştır, popülasyon büyüdükçe artar ve ardından çevredeki sınırlı kaynaklar kısıtlayıcı bir etken haline geldikçe yeniden yavaşlar. **Kapalı bir sistemdeki maksimum büyüme K/2'de gerçekleşir**.

BV'deki çıkış kapağının boyutu, bakteri kültürünün taşıma kapasitesine (K) eşdeğerdir. Çıkış kapağı boşken veya neredeyse doluyken çok az büyüme gerçekleşir. İdeal olarak, maksimum büyüme ve verimlilik için çıkış kapağı mümkün olduğunca %50 dolulukta kalır. Daha spesifik olarak, hem girdi HEM de çıktı sıvıları, çıkış kapağının K/2'ye veya yarı doluluğa ne kadar yakın olduğuna bağlı olarak x1,001'e kadar çarpılır. Katı bileşenler ve kültür etkilenmez. Çarpan (m), aşağıdaki denklemle hesaplanır; burada Fill%, maksimum kapasiteye göre mevcut sıvı seviyesidir.

<Latex formula="m=\lceil -4,000\times(\text{Fill}\% - 0.5)^2\rceil + 1,001" />

Bu denklem, sigmoidal popülasyon eğrisinin türevini yansıtmak için kuadratiktir. Ancak tavan operatörü, K/2 çevresine küçük bir tampon ekleyerek maksimum çarpana yakın değerleri yukarı yuvarlar; bu da x1,001 kazancı elde etmek için çıkış kapağının tam olarak %50 dolulukta olması gerekmediği anlamına gelir. Daha büyük çıkış kapaklarının tamponu daha büyüktür, ancak başlangıçta K/2'ye ulaşmak için daha fazla sıvı gerektirir. Çok küçük bir çıkış kapağıyla başlayıp daha fazla çıktı sıvısı elde edildikçe daha büyük boyutlara geçmen önerilir. Aşağıdaki tablo, tüm farklı çıkış kapaklarını ve maksimum x1,001 çarpanını (m) kazanmak için gereken eşiklerini listeler. Grafik, yüzde doluluk seviyesine göre genel ilişkiyi görsel olarak gösterir.

<Row>
  <Column width="310">
| Kapak | Minimum | K/2 | Maksimum | Aralık |
| --- | --- | --- | --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:60" showIcon="left" scale="0.8"> ULV</ItemLink> | 3,874 L | 4,000 L | 4,126 L | 252 L |
| <ItemLink id="gregtech:gt.blockmachines:61" showIcon="left" scale="0.8"> LV</ItemLink> | 7,748 L | 8,000 L | 8,252 L | 504 L |
| <ItemLink id="gregtech:gt.blockmachines:62" showIcon="left" scale="0.8"> MV</ItemLink> | 15,495 L | 16,000 L | 16,505 L | 1,010 L |
| <ItemLink id="gregtech:gt.blockmachines:63" showIcon="left" scale="0.8"> HV</ItemLink> | 30,989 L | 32,000 L | 33,011 L | 2,022 L |
| <ItemLink id="gregtech:gt.blockmachines:64" showIcon="left" scale="0.8"> EV</ItemLink> | 61,977 L | 64,000 L | 66,023 L | 4,046 L |
| <ItemLink id="gregtech:gt.blockmachines:65" showIcon="left" scale="0.8"> IV</ItemLink> | 123,953 L | 128,000 L | 132,047 L | 8,094 L |
| <ItemLink id="gregtech:gt.blockmachines:66" showIcon="left" scale="0.8"> LuV</ItemLink> | 247,905 L | 256,000 L | 264,095 L | 16,190 L |
| <ItemLink id="gregtech:gt.blockmachines:67" showIcon="left" scale="0.8"> ZPM</ItemLink> | 495,810 L | 512,000 L | 528,190 L | 32,380 L |
| <ItemLink id="gregtech:gt.blockmachines:68" showIcon="left" scale="0.8"> UV</ItemLink> | 991,619 L | 1,024,000 L | 1,056,381 L | 64,762 L |
| <ItemLink id="gregtech:gt.blockmachines:69" showIcon="left" scale="0.8"> UHV</ItemLink> | 1,983,237 L | 2,048,000 L | 2,112,763 L | 129,526 L |
| <ItemLink id="gregtech:gt.blockmachines:12103" showIcon="left" scale="0.8"> UEV</ItemLink> | 3,966,474 L | 4,096,000 L | 4,225,526 L | 259,052 L |
| <ItemLink id="gregtech:gt.blockmachines:12104" showIcon="left" scale="0.8"> UIV</ItemLink> | 7,932,947 L | 8,192,000 L | 8,451,053 L | 518,106 L |
| <ItemLink id="gregtech:gt.blockmachines:12105" showIcon="left" scale="0.8"> UMV</ItemLink> | 15,865,893 L | 16,384,000 L | 16,902,107 L | 1,036,214 L |
| <ItemLink id="gregtech:gt.blockmachines:12106" showIcon="left" scale="0.8"> UXV</ItemLink> | 31,731,785 L | 32,768,000 L | 33,804,215 L | 2,072,430 L |
| <ItemLink id="gregtech:gt.blockmachines:12737" showIcon="left" scale="0.8"> Dev</ItemLink> | 48,418,862 L | 50,000,000 L | 51,581,138 L | 3,162,276 L |
{: widths="55, 85, 85, 85, 75"}
</Column>
<FunctionGraph xRange="0..100" xLabel="Fill %" yLabel="Multiplier" width="220">
  <Plot expr="(-4000 * (x/100 - 0.5)^2) + 1001" />
</FunctionGraph>
</Row>

Çarpanın (m) bir tarifin en başında hesaplandığını unutma. BV sürekli çalışırken bu önemlidir çünkü önceki tarifin çıktısı, bir sonrakinin çarpanının (m) hesaplanmasında etkili olur. İdeal olarak, maksimum çarpanı garanti etmek için optimal üretim aralığı çıktı sıvısı miktarından büyük olmalıdır.

## Kaynaklar
- [GTNH Wiki - Bakteriyel Küvet](https://wiki.gtnewhorizons.com/wiki/Bacterial_Vat)