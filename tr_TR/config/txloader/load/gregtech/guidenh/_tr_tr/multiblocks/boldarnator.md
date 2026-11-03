---
item_ids:
  - gregtech:gt.blockmachines:15556
quest_ids:
  - AAAAAAAAAAAAAAAAAAABhQ==
navigation:
  title: Boldarnator
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15556
  position: -5001
---
# Boldarnator
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15556" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15556" showIcon="left" />, temel kayaları oluşturmak ve toplamak için IV kademe bir multibloktur.

Boldarnator, [tek bloklu kaya kırıcıya](/singleblock/rock_breaker.md) göre doğrudan bir yükseltmedir: %300 hızda çalışır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve gerilim kademesi başına 8 paralel sunar.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit açma kademesi | IV |
| Yapı Boyutu (UxGxY) | 5x7x5 |
| Güç | Normal |
| Overclock | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | 100 gibbl/s kirlilik üretir ve Egzoz Çıkışı gerektirir |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:15556" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="miscutils:gtplusplus.blockcasings.2" />

<RecipesFor id="gregtech:gt.blockframes:81" />

### Yapı

Boldarnator'ın kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasına etkisi yoktur.

Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock için birden fazla normal enerji kapağı bulunabilir.

Lav ve su, yapı oluşturulduğunda ücretsiz olarak oluşturulur ve bu nedenle elle yerleştirilmeleri GEREKMEZ.

Boldarnator döndürülebilir veya çevrilebilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> aracını "glass" alt kanalıyla kullanarak camın kademesini belirt.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15556" showIcon="left" /> | 1, Ön orta, 3. katman |
| <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> | 50-55 |
| <ItemLink id="gregtech:gt.blockframes:81" showIcon="left" /> | 36 |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi Bir Kademeli Cam | 12 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Egzoz Çıkışı | 1+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1+, herhangi bir <ItemLink id="miscutils:gtplusplus.blockcasings.2" showIcon="left" /> yerine geçebilir |

### Duvar Paylaşımı

Boldarnator'lar kasa, cam, çerçeve kutusu ve veriyolu/kapak tasarrufu için her bir yüzünü duvar paylaşımıyla birleştirebilir. Buna her iki yandaki tanklar da dahildir, ancak önce kontrolcülerden biri yatay olarak ters çevrilmeden sıvılar değiştirilemez (İngiliz anahtarıyla eğilip sağ tıkla).

Hiçbir tarif 0,5A'dan fazla güç kullanmaz, bu yüzden bir enerji kapağı dört makine arasında paylaşılabilir.

## Kullanım

Boldarnator; <ItemLink id="minecraft:cobblestone" showIcon="left" />, <ItemLink id="minecraft:stone" showIcon="left" />, <ItemLink id="minecraft:netherrack" showIcon="left" />, <ItemLink id="Botania:stone:1" showIcon="left" />, <ItemLink id="etfuturum:cobbled_deepslate" showIcon="left" />, <ItemLink id="minecraft:obsidian" showIcon="left" /> oluşturabilir ve <ItemLink id="thaumicbases:genLeaves:2" showIcon="left" /> ile <ItemLink id="thaumicbases:genLeaves:3" showIcon="left" /> davranışlarını (altındaki bloğu kendi karşılık gelen bloğuna dönüştürür; örneğin <ItemLink id="minecraft:soul_sand" showIcon="left" />, <ItemLink id="minecraft:quartz_ore" showIcon="left" /> ve <ItemLink id="minecraft:end_stone" showIcon="left" />), her işlemde %10 yaprak tüketme şansı karşılığında taklit edebilir.

Boldarnator gerilim kademesi başına 8 paralel sunar. Aşağıdaki tablo, kademe başına paralelleri ve her bloğun işlem hızını gösterir.

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paralel sayısı | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |
| <ItemLink id="minecraft:cobblestone" showIcon="left" />/s | 4 | 20 | 88 | 128 | 400 | 960 | 2,240 | 3,840 | 8,640 | 19,200 | 42,240 | 46,080 | 99,840 | 215,040 | 460,800 |
| <ItemLink id="minecraft:stone" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="minecraft:netherrack" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="Botania:stone:1" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="etfuturum:cobbled_deepslate" showIcon="left" />/s | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ | ^^ |
| <ItemLink id="minecraft:obsidian" showIcon="left" />/s | 0.5 | 2.4 | 10 | 15 | 38 | 96 | 225 | 640 | 1,440 | 3,200 | 5,280 | 5,760 | 12,480 | 26,880 | 57,600 |
{: widths="90"}

Boldarnator'ın işleyebileceği tarifleri NEI'de kontrol edebilirsin. İşlem için hangi eşyaların gerektiğini, işlem sırasında tüketilenler ve tüketilmeyenler dahil gösterir. Şu anda eşya tüketen 4 tarif var:
1. <ItemLink id="minecraft:obsidian" showIcon="left" /> - İşlem başına 1 Kızıltaş tüketir.
1. <ItemLink id="minecraft:netherrack" showIcon="left" /> - İşlem başına 1 Parlak taş tüketir.
1. <ItemLink id="thaumicbases:genLeaves:2" showIcon="left" /> - İşlem başına %10 şansla yaprak tüketir.
1. <ItemLink id="thaumicbases:genLeaves:3" showIcon="left" /> - İşlem başına %10 şansla yaprak tüketir.

## Kaynaklar

- [GTNH Wiki : Boldarnator](https://wiki.gtnewhorizons.com/wiki/Boldarnator)