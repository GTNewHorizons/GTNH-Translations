---
navigation:
  parent: /items_blocks_index.md
  title: Üretim CPU'su Multibloğu (Depolama, Yardımcı İşlemci, Monitör, Birim)
  icon: appliedenergistics2:tile.BlockSingularityCraftingStorage
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockCraftingUnit
- appliedenergistics2:tile.BlockCraftingMonitor
- appliedenergistics2:tile.BlockCraftingUnit:1
- appliedenergistics2:tile.BlockCraftingUnit:2
- appliedenergistics2:tile.BlockCraftingUnit:3
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:0
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:1
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:2
- appliedenergistics2:tile.BlockAdvancedCraftingUnit:3
- appliedenergistics2:tile.BlockCraftingStorage
- appliedenergistics2:tile.BlockCraftingStorage:1
- appliedenergistics2:tile.BlockCraftingStorage:2
- appliedenergistics2:tile.BlockCraftingStorage:3
- appliedenergistics2:tile.BlockAdvancedCraftingStorage
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:1
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:2
- appliedenergistics2:tile.BlockAdvancedCraftingStorage:3
- appliedenergistics2:tile.BlockSingularityCraftingStorage
---

# Üretim CPU'su

<GameScene width="350" height="220" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingMonitor" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:0" scale="4" />
</Row>

Üretim CPU'ları üretim isteklerini ve işlerini yönetir. Çok adımlı üretim işleri sürerken ara ürünleri depolar; işlerin maksimum boyutunu ve bir dereceye kadar ne kadar hızlı tamamlandıklarını etkiler. Daha fazla ayrıntı için [otomatik üretime](../ae2_mechanics/autocrafting.md) bak.

Etkin işinin ilerlemesini görmek için bir Üretim CPU'suna sağ tıklayarak üretim durumu arayüzünü aç.

## Ayarlar

*   Bir Üretim CPU'su istekleri yalnızca oyunculardan, yalnızca otomasyondan (ör. bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> ile bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />) veya her ikisinden de kabul edebilir.

## İnşaat

Üretim CPU'ları multibloktur ve boşluksuz, katı dikdörtgen prizmalar olmalıdır. Birkaç bileşenden oluşurlar.

Her CPU en az bir Üretim Deposu bloğu içermelidir; geçerli en küçük CPU tek bir 1k Üretim Deposu bloğudur.

# Üretim Birimi

<BlockImage id="appliedenergistics2:tile.BlockCraftingUnit" scale="4" />

(İsteğe bağlı) Üretim Birimleri, yeterli başka bileşen olmadığında CPU'nun katı dikdörtgen prizma olarak kalması için boşlukları doldurur. Ayrıca diğer bileşenlerin üretiminde malzeme olarak kullanılır.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingUnit" />

# Üretim Deposu

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:0" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:2" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCraftingStorage:3" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:0" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:1" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:2" scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:3" scale="4" />
</Row>

(Gerekli) Üretim Deposu tüm standart hücre boyutlarında mevcuttur: 1k, 4k, 16k, 64k ve 256k. Bir üretim işinin bileşenlerini ve ara ürünlerini depolar; bu yüzden daha fazla bileşen içeren işler daha büyük veya ek depolama blokları gerektirir.

<Column>
  <Row>
    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:0" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:1" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:2" />

    <RecipeFor id="appliedenergistics2:tile.BlockCraftingStorage:3" />
  </Row>

  <Row>
    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:1" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:2" />

    <RecipeFor id="appliedenergistics2:tile.BlockAdvancedCraftingStorage:3" />
  </Row>
</Column>

# Üretim Yardımcı İşlem Birimi

<BlockImage id="appliedenergistics2:tile.BlockCraftingUnit:1" scale="4" />

(İsteğe bağlı) Üretim Yardımcı İşlem Birimleri CPU'nun işlem hızını artırır; sistemin bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> üzerinden bileşen gruplarını daha sık göndermesini ve hızlı makinelere ayak uydurmasını sağlar. Örneğin, <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />lerle çevrili bir arayüz grupları tek bir Montajcının işleyebileceğinden daha hızlı gönderebildiğinde, grupları Montajcılar arasında dağıtır.

Bazı karmaşık tariflerde, kitap rafları için aynı anda tahta ve kitap üretmek gibi paralel çalışabilecek birden fazla adım vardır. Bir CPU'ya sağ tıklayarak veya bir [terminalde](terminals.md) çekiç simgesini kullanarak açılan üretim durumu arayüzünde bu adımlar “zamanlandı” olarak görünür. Her Yardımcı İşlem Birimi, bu türden bir ek adımın paralel çalışmasına izin verir; o adım “üretiliyor” olarak görünür. Pratikte Yardımcı İşlem Birimleri genellikle paralel tarif adımı sayısından çok, grup ekleme hızı için eklenir.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingUnit:1" />

# Üretim Monitörü

<BlockImage id="appliedenergistics2:tile.BlockCraftingMonitor" scale="4" />

(İsteğe bağlı) Bir Üretim Monitörü, CPU'nun o anda yürüttüğü işi gösterir. Ekranı bir <ItemLink id="appliedenergistics2:item.ToolColorApplicator" /> ile boyanabilir.

<RecipeFor id="appliedenergistics2:tile.BlockCraftingMonitor" />