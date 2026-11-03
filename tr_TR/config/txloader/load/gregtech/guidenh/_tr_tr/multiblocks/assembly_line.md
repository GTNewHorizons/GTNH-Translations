---
item_ids:
  - gregtech:gt.blockmachines:1170
quest_ids:
  - AAAAAAAAAAAAAAAAAAAFhA==
navigation:
  title: Montaj Hattı
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:1170
  position: -5001
---

# Montaj Hattı

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:1170" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" /> (assline veya AL), LuV+ kademe bileşenleri üretmek için kullanılan IV kademe bir multibloktur. 

Makine bir dizi dilim halinde inşa edilir ve girdiler NEI'de göründükleri tam sırayla yerleştirilmelidir. 

Tarifler ayrıca örtük değildir ve <ItemLink id="gregtech:gt.metaitem.01:32708" showIcon="left" /> ile AL'ye açıkça paylaşılmalıdır. Bu, oyuncunun bu noktaya kadar karşılaştığı multiblokların hiçbirine benzemez ve otomasyon için daha gelişmiş teknikler gerektirir. Normal montajcı tarifleri için [<ItemLink id="gregtech:gt.blockmachines:32018" showIcon="left" />](./precise_auto_assembler_mt_3662.md) veya [<ItemLink id="gregtech:gt.blockmachines:876" showIcon="left" />](./large_scale_auto_assembler_v101.md) sayfalarına bak. 

AL, paralel işleme ve çok amperli ve lazer enerji kapakları desteğiyle genellikle [<ItemLink id="gregtech:gt.blockmachines:13532" showIcon="left" />](./advanced_assembly_line.md) tarafından geride bırakılır, ancak AAL kademe atlaması yapamadığı için AL'nin kademe atlaması AAL'nin AL'nin yerini tamamen almasını engeller.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | IV |
| Yapı Boyutu(UxGxY) | 3x5-16x4 |
| Güç | Normal |
| Hız Aşırtma | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

### Üretim
<RecipesFor id="gregtech:gt.blockmachines:1170" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gregtech:gt.blockcasings2" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="gregtech:gt.blockcasings2:5" />

<RecipesFor id="gregtech:gt.blockcasings2:9" />

### Yapı

AL, her birinin alt-orta kısmında tek bir benzersiz girdi tutan bir giriş yolu bulunan bir dizi dilim halinde inşa edilir. Bu nedenle gereken toplam dilim sayısı, tarifteki toplam girdi sayısına bağlıdır. Örneğin LuV motorun beş katı girdisi vardır ve bu yüzden üretimi için beş dilim gerekir. Malzemelerin yerleştirilme sırası, NEI'de göründükleri sıranın aynısıdır.

AL döndürülebilir ve aynalanabilir; kontrolcü ilk dilimde bulunur.

Cam herhangi bir kademede olabilir ve makinenin çalışmasına hiçbir etkisi yoktur. 

Çok amperli ve lazer enerji kapakları desteklenmez, ancak hız aşırtma için birden fazla normal enerji kapağı olabilir. AL yalnızca BİR kez kademe atlayabilir (yani IV enerji kapakları en fazla LuV tariflerini çalıştırabilir). 

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek için "glass", dilim sayısını belirtmek için "length" alt kanalını ver $$(\text{Slices} = \text{Length} + 4)$$.

Giriş yolları herhangi bir kademede olabilir, ancak sınırlı kapasiteleri (1 yuva) otomasyon için çok yararlı olduğundan <ItemLink id="gregtech:gt.blockmachines:70" showIcon="left" /> kullanman önerilir. 

Otomatik çekmeye ayarlanmış <ItemLink id="gregtech:gt.blockmachines:2711" showIcon="left" /> ve bağlantılı giriş yolları, dilim başına birden fazla eşya tipini görünür kılıyorsa <Color id="red">**Kırmızı: ÇALIŞMAZ**</Color>. 

Maksimum uzunlukta çıkış yolu, son giriş yolunun yerine değil, son dilimin 1. katmanındaki bir sağlam çelik makine gövdesinin yerine geçmelidir. 

Hiçbir tarif dörtten fazla sıvı kullanmadığı için yalnızca dört girdi kapağı gerekir ve <ItemImage id="gregtech:gt.blockmachines:200" noTooltip /> Dörtlü girdi kapakları <Color id="red">**Kırmızı: ÇALIŞMAZ**</Color>, ancak gerekirse girdi kapakları arasında boşluklar olabilir.

#### Temel Yapı (Minimum gereksinimler)
| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" /> | İlk dilim, 3. katman |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir kademeli cam | 10, 2. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 8, 3. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-12, 1. katmanın her iki yanı ve 4. katmanın ortası |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 5, 2. katmanın ortası |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 5, 3. katmanın ortası |
| <ItemImage id="gregtech:gt.blockmachines:145" noTooltip />Veri Erişim Kapağı | 1, 3. katmanın her iki yanında herhangi bir yer, ancak ilk dilimde <Color id="red">**Kırmızı: OLAMAZ**</Color> |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Enerji Kapağı Etiketi: Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, 4. katmandaki herhangi bir makine gövdesi |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, 1. katmanın herhangi bir yan gövdesi |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 5, 1. katmanın ortası |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, 1. katmanın herhangi bir yan gövdesi |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1, son dilimin 1. katman yan gövdesi |

#### Her Ek Dilim

<GameScene interactive={true} wrap="square" align="right" width="170" height="130">
  <Block id="gregtech:gt.blockmachines:71" />
  <Block id="gregtech:gt.blockcasings2" x="-1"/>
  <Block id="gregtech:gt.blockcasings2" x="1"/>
  <Block id="gregtech:gt.blockcasings2:5" y="1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="-1" />
  <Block id="gregtech:gt.blockglass1:10" y="1" x="1" />
  <Block id="gregtech:gt.blockcasings2:9" y="2" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="-1" />
  <Block id="gregtech:gt.blockcasings3:10" y="2" x="1" />
  <Block id="gregtech:gt.blockcasings2" y="3"/>
</GameScene>

Her ek dilim (1 uzunluk) şu blokları gerektirir:

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir kademeli cam | 2, 2. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 2, 3. katmanın her iki yanı |
| <ItemLink id="gregtech:gt.blockcasings2" showIcon="left" /> | 0-3, 1. katmanın her iki yanı ve 4. katmanın ortası |
| <ItemLink id="gregtech:gt.blockcasings2:5" showIcon="left" /> | 1, 2. katmanın ortası |
| <ItemLink id="gregtech:gt.blockcasings2:9" showIcon="left" /> | 1, 3. katmanın ortası |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Enerji Kapağı Etiketi: Yalnızca Normal Kapaklara izin verilir</Tooltip> | 0+, 4. katmandaki herhangi bir makine gövdesi |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1, 1. katmanın ortası |

AL dilimlerini uzattığında <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu'nun son dilime taşınması gerektiğini unutma.

### Duvar Paylaşımı

AL'ler gövde, cam ve yol/kapaklardan tasarruf etmek için her bir yanını duvar paylaşımına açabilir. Buna girdi kapakları, bakım kapakları, veri erişim kapakları ve çıkış yolları dahildir. Bir veri erişim kapağını paylaşmak, TPS tasarrufu ve gereken veri çubuğu sayısını azaltmak için özellikle değerlidir.

## Kullanım

### Tarifleri Taramak

Bir tarifin girdilerini AL'ye (ve doğru sırada) yerleştirmek, makinenin işlemeye başlaması için yeterli değildir. Tariflerin, tek bloklu bir tarayıcıda gerekli bilgiyle taranmış <ItemLink id="gregtech:gt.metaitem.01:32708" showIcon="left" /> aracılığıyla AL ile açıkça paylaşılması gerekir.

Örneğin bir <ItemLink id="gregtech:gt.metaitem.01:32606" showIcon="left" /> için tarifi taramak üzere, aşağıdaki tarifte görüldüğü gibi hem bir IV motor hem de bir veri çubuğunu tarayıcıya yerleştir. Çıktı, özellikle LuV motorları için olan bir veri çubuğudur ve AL'deki Veri Erişim Kapağına konur. IV motor bu işlemde tüketilir. Tüm veri çubuğu tarifleri ve bunlar için taranacak eşyalar NEI aracılığıyla görülebilir. Tariflerin GTNH güncellemeleriyle değişebileceğini ve oyuncunun veri çubuklarını güncellemesini gerektirebileceğini unutma.

<Recipe id="gregtech:gt.metaitem.01:32606" handlerId="gt.recipe.scanner" /> 

Oyunun ilerleyen kısımlarında tarayıcının yerini [<ItemLink id="gregtech:gt.blockmachines:15331" showIcon="left" />](./research_station.md) ve [<ItemLink id="gregtech:gt.blockmachines:15311" showIcon="left" />](./quantum_computer.md) alır. Bu multiblokların ikisi, yani Araştırma İstasyonu ve Kuantum Bilgisayarı, GTNH'deki en gelişmiş eşyalardan bazılarının tariflerini açmak için birlikte çalışır.

### Veri Erişim Kapakları
Aşağıda listelenen dört tür veri erişim kapağı vardır. AL başına yalnızca bir tane olabilir, ancak makineler arasında güvenle duvar paylaşımı yapılabilir.

- <ItemLink id="gregtech:gt.blockmachines:145" showIcon="left" /> - En fazla dört veri çubuğu tutar
- <ItemLink id="gregtech:gt.blockmachines:146" showIcon="left" /> - En fazla on altı veri çubuğu tutar
- <ItemLink id="gregtech:gt.blockmachines:147" showIcon="left" /> - En fazla on altı veri çubuğu tutar ve veri çubuklarının girdi/çıktısına izin verir.
- <ItemLink id="gregtech:gt.blockmachines:15442" showIcon="left" /> - Bir [<ItemLink id="gregtech:gt.blockmachines:15313" showIcon="left" />](./data_bank.md) içinden herhangi sayıda veri çubuğu okur.

### Sorun Giderme

1. **Geçerli Tarif Bulunamadı.** Bu hatanın eksik eşyalar, eksik sıvılar, yanlış sıradaki malzemeler, birden fazla çıkış yolu gibi pek çok nedeni olabilir. Tüm eşyaların doğru giriş yolu/kapağında olduğunu kontrol et.
1. **Veri Çubuğu Bulunamadı.** Kontrolcü hiçbir veri çubuğu bulamıyor. Ya veri erişim kapağı boş ya da veri çubukları bir tarifle taranmamış. Shift tuşunu basılı tutmak, AE2 şablonuna benzer şekilde veri çubuğunun hangi eşyayla tarandığını gösterir.
1. **Tarifler üst üste biniyor.** Muhtemelen şablonları saklayan bir arayüze engelleme kartı takmayı ya da engelleme modunu aktifleştirmeyi unuttun.

## Kaynaklar

- [GTNH Wiki: Montaj Hattı](https://wiki.gtnewhorizons.com/wiki/Assembly_Line)