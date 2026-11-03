---
item_ids:
  - gregtech:gt.blockmachines:3018
quest_ids:
  - RLJR8nFySzSaZLeCRsabDg==
navigation:
  title: Işın Dengeleyici
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3018
  position: -8001
---
# Işın Dengeleyici
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3018" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />, parçacık ışınlarını geçici olarak tamponlayan ve özel bir hızda yeniden serbest bırakan UV kademesindeki bir multibloktur. Işın Dengeleyici çalışmak için güç veya bakım gerektirmez ve içinden geçen parçacık ışınları da herhangi bir ceza görmez veya enerji/odak kaybetmez. Yalnızca hız, kontrolcünün GUI'sinde ayarlanan değere düşürülür, ancak hiçbir şey kaybolmaz. 

Işın Dengeleyici tamamen isteğe bağlıdır, ancak [Işın Hattı](./beam_line.md) ve/veya [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) ile yardımcı olabilir. [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md) ve [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) araçlarını da dene; sonra [<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />](./beam_crafter.md) içinde tarifleri işle.

| Özellik | Ayrıntılar |
| --- | --- |
| Açıldığı kademe | UV |
| Yapı Boyutu (U×G×Y) | 11x7x7 |
| Güç | Yok |
| Overclock | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:3018" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings3:10" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

### Yapı

Işın Dengeleyicinin kademeli bileşenleri yoktur. Cam herhangi bir kademede olabilir ve makinenin çalışması üzerinde etkisi yoktur. 

Işın Dengeleyici döndürülebilir veya çevrilebilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek için "glass" alt kanalını ver.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" /> | 1, ön orta, 3. katman |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 95 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 15 |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir Kademeli Cam | 9 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 1, kontrolcünün üstünde |
| <ItemLink id="gregtech:gt.blockmachines:10504" showIcon="left" /> | 1, kontrolcünün karşı tarafının ortasında |

### Duvar Paylaşımı
Işın Dengeleyiciler kasalardan tasarruf etmek için her bir kenarını duvar paylaşımına açabilir. Ancak konumlarındaki kısıtlamalar nedeniyle ışın girdi kapağı veya ışın çıkış kapağı paylaşılamaz.

## Kullanım
Işın Dengeleyici parçacık ışınlarını geçici olarak tamponlar ve özel bir hızda yeniden serbest bırakır. Çalışmak için güç veya bakım gerektirmez ve manuel olarak devre dışı bırakılmadıkça asla kapanmaz. Parçacık ışınları makineden geçerken herhangi bir ceza görmez veya enerji/odak kaybetmez. Yalnızca hız, kontrolcünün GUI'sinde ayarlanan değere düşürülür, ancak hiçbir şey kaybolmaz.  
Örneğin hızı 100 olan bir elektron ışını, hedef ışın hızı 40 olan bir Işın Dengeleyiciye girerse makine önce hızı 40 olan iki ışın, ardından hızı 20 olan bir ışın verir.

Tamponun maksimum kapasitesi 100k parçacıktır ve aynı parçacık türü, enerji veya odağa sahip olmayan parçacık ışınlarını yok sayar. Farklı olabilecek tek değer girdi ışın hızıdır; bu da Işın Dengeleyicinin, parçacık ışınlarını makineye girmeden önce filtrelemek için [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) kullanabileceği anlamına gelir. Makine devre dışıyken tampona parçacık eklenmez veya tampondan parçacık çıkarılmaz.

## Kaynaklar
- [GTNH Wiki : Işın Dengeleyici](https://wiki.gtnewhorizons.com/wiki/Beam_Stabilizer)