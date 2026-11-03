---
item_ids:
  - gregtech:gt.blockmachines:3016
quest_ids:
  - _xupoCqbT52qN_3zQonWNg==
navigation:
  title: Işın Aynası
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3016
  position: -8001
---
# Işın Aynası
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3016" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />, parçacık ışınlarını 90° veya 180° açılarla büken bir UV kademesi multibloğudur.

Işın Aynası yalnızca bir ışın girdi kapağını ve bir ışın çıkış kapağını destekler, ancak çalışmak için hiçbir güç veya bakım gerektirmez. Parçacık ışınları da makineden geçerken herhangi bir ceza almaz veya istatistiklerinden hiçbirini kaybetmez.

Işın Aynası tamamen isteğe bağlıdır, ancak [Işın Hattı](./beam_line.md) ve/veya [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) ile yardımcı olabilir. [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) ve [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) öğelerine bak; bunlar, tarifleri [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md) içinde işlemeden önce ışınları değiştirmene yarar.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | UV |
| Yapı Boyutu (UxGxY) | 5x3x5 (90°) |
| ^^ | 5x3x6 (180°) |
| Güç | Yok |
| Overclock | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:3016" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Yapı
Işın Aynası'nın kademeli bileşeni yoktur.

Cam herhangi bir kademede olabilir ve makinenin çalışması üzerinde hiçbir etkisi yoktur.

Işın Aynası döndürülebilir veya ters çevrilebilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek için "glass" alt kanalını ve açıyı belirtmek için projektör yığın boyutunu kullan (90° için 1, 180° için 2).

<ContentTabs>
  <Tab title="90° Yapı">
  | Bileşen | Miktar ve yerleşim |
  | --- | --- |
  | <ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" /> | 1, Ön alt orta |
  | <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 31 |
  | <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 9, Makinenin her iki ucunu kaplar |
  | <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir kademeli cam | 5 |
  | <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Kontrolcünün üstünde |
  | <ItemImage id="gregtech:gt.blockmachines:10504" noTooltip /><Tooltip label="Işın Çıkış Kapağı">Normal/Filtreli ikisi de desteklenir</Tooltip> | 1, Kontrolcünün karşısındaki tarafın üstü, arkası cama bakacak şekilde döndürülmeli |
  </Tab>

  <Tab title="180° Yapı">
  | Bileşen | Miktar ve yerleşim |
  | --- | --- |
  | <ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" /> | 1, Ön alt orta |
  | <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 52 |
  | <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 9, Makinenin her iki ucunu kaplar |
  | <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir kademeli cam | 8 |
  | <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Kontrolcünün üstünde |
  | <ItemImage id="gregtech:gt.blockmachines:10504" noTooltip /><Tooltip label="Işın Çıkış Kapağı">Normal/Filtreli ikisi de desteklenir</Tooltip> | 1, Kontrolcünün karşısındaki tarafın üstü, arkası cama bakacak şekilde döndürülmeli |
  </Tab>
</ContentTabs>


### Duvar Paylaşımı

Işın Aynaları kasa tasarrufu için her bir yüzünde duvar paylaşımı yapabilir. Işın çıkış kapakları birbirine çok yakın olduğu için [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) çıktılarını bükmek için paylaşım kullanışlıdır.

## Kaynaklar

- [GTNH Wiki : Işın Aynası](https://wiki.gtnewhorizons.com/wiki/Beam_Mirror)