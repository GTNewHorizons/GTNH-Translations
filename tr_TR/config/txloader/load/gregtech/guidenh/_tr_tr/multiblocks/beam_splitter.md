---
item_ids:
  - gregtech:gt.blockmachines:3017
quest_ids:
  - RLJR8nFySzSaZLeCRsabDg==
navigation:
  title: Işın Ayrıştırıcı
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3017
  position: -8001
---
# Işın Ayrıştırıcı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3017" />
</GameScene>
<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />, parçacık ışınlarını filtrelemek ve/veya bölmek için UV kademe bir multibloktur. 

Işın Ayrıştırıcı yalnızca bir ışın girdi kapağı ve dört filtreli ışın çıkış kapağı destekler; ancak çalışmak için enerji veya bakım gerektirmez. 

Işın Ayrıştırıcı tamamen isteğe bağlıdır, ancak [Işın Hattı](./beam_line.md) ve/veya [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) ile birlikte işine yarayabilir. Ayrıca [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md) ve [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) araçlarını [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md) içinde tarif işlemeden önce dene.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | UV |
| Yapı Boyutu (UxGxY) | 9x9x3 |
| Enerji | Yok |
| Overclock | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:3017" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Yapı
Işın Ayrıştırıcı'da kademeli bileşen yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışmasını etkilemez. 

Işın Ayrıştırıcı döndürülebilir veya ters çevrilebilir.

Işın Ayrıştırıcı yalnızca <ItemLink id="gregtech:gt.blockmachines:3014" showIcon="left" /> destekler.

Camın kademesini belirtmek için "glass" alt kanalıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" /> | 1, Ön alt merkez |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 42 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 27, Makinenin her iki ucunun kenarı ve köşesi |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir Kademeli Cam | 9 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, Kontrolcünün üstünde |
| <ItemLink id="gregtech:gt.blockmachines:3014" showIcon="left" /> | 4, Kontrolcünün karşı tarafında, her boşluk 1 blok |

### Duvar paylaşımı

Işın Ayrıştırıcılar kasa ve camdan tasarruf etmek için her bir yüzünü duvar paylaşımıyla kullanabilir. Ancak konum kısıtlamaları nedeniyle ışın girdi kapağı veya filtreli ışın çıkış kapakları paylaşılamaz.

## Kullanım

<GameScene interactive={true} wrap="square" align="right" width="300" height="300">
  <ImportStructure src="/assets/structures/beam_splitter_example_ponder.snbt" />
  <ImportPonder src="/assets/ponders/multiblocks/beam_splitter/beam_splitter_example_ponder.json" />
</GameScene>

Işın Ayrıştırıcı, gelen parçacık ışınını filtreler ve/veya 1-4 parçaya böler ve elle devre dışı bırakılmadıkça asla kapanmaz. Parçacık ışınları makineden geçerken herhangi bir ceza almaz veya enerji/odak kaybetmez. Yalnızca oran, tüm geçerli çıkışlar arasında eşit olarak bölünür. Kesirli oranlar her zaman aşağı yuvarlanır.

Sağdaki sahne, Işın Ayrıştırıcı'nın çalışmasını bir örnekle gösterir.

Işın Ayrıştırıcı, [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) ile mükemmel şekilde tamamlanır; çünkü ikincisi aynı ışın çıkış kapaklarından çok farklı parçacık türleri üretir ve bunların hepsinin aynı [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md) gitmesi israf olurdu.

Parçacık ışınlarını birleştirmenin hiçbir yolu yoktur; bu yüzden tarifler makineler arasında bölünecek ve dolayısıyla parçacıklar da bölünmelidir.

## Kaynaklar
- [GTNH Wiki : Işın Ayrıştırıcı](https://wiki.gtnewhorizons.com/wiki/Beam_Splitter)