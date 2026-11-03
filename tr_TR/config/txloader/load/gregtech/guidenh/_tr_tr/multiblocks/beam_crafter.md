---
item_ids:
  - gregtech:gt.blockmachines:3015
quest_ids:
  - xTkeDXIZSlmRkde8LZgzLw==
navigation:
  title: Işın Üreticisi
  parent: ./large_hadron_collider.md
  icon: gregtech:gt.blockmachines:3015
  position: -8001
---
# Işın Üreticisi

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3015" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" />, üretim tarifleri için parçacık ışınlarını yakalayan UV kademesinde bir multibloktur.

Gerekirse, [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md), [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) ve/veya [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) kullanarak [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) sonrasındaki parçacık ışınlarının akışını kontrol et.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | UV |
| Yapı Boyutu (GxUxY) | 11x17x5 |
| Güç | Her tür kapak kullanılabilir; Çok Amperli ve Lazer Kapaklar dahil |
| Hız Aşırtma | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

### Üretim

<RecipesFor id="gregtech:gt.blockmachines:3015" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gtnhlanth:casing.shielded_accelerator" handlerBlacklist="bq_quest" />

<RecipesFor id="gregtech:gt.blockcasings3:10" handlerBlacklist="bq_quest" />

<RecipesFor id="gregtech:gt.blockmachines:10503" handlerBlacklist="gt.recipe.scanner" />

### Yapı

Işın Üreticisinin kademeli bileşeni yoktur. Cam herhangi bir kademeden olabilir ve makinenin çalışmasını etkilemez.

Işın Üreticisi döndürülebilir veya ters çevrilebilir.

<ItemLink id="gregtech:gt.blockmachines:2715" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:2714" showIcon="left" />, Işın Üreticisi ile uyumlu değildir; bu yüzden normal veya stoklamalı giriş yolu ve girdi kapakları kullan.

Çok Amperli ve Lazer Enerji Kapakları desteklenir, ancak makineyi **hız aşırtma** uygulamazlar.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek üzere "glass" alt kanalını ver.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3015" showIcon="left" /> | 1, Ön orta, 1. katman |
| <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> | 0-225 |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi bir kademeli cam | 26 |
| <ItemLink id="gregtech:gt.blockcasings3:10" showIcon="left" /> | 16 |
| <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" /> | 2, Yapının her iki ucunun ortası |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 1+, Herhangi bir <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, Herhangi bir <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, Herhangi bir <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1+, Herhangi bir <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Çıkış Kapağı | 0+, Herhangi bir <ItemLink id="gtnhlanth:casing.shielded_accelerator" showIcon="left" /> yerine geçebilir |

### Duvar Paylaşımı

Işın Üreticileri kasa ve camdan tasarruf etmek için her bir yüzünü duvar paylaşımıyla kullanabilir. Ancak konumlarındaki kısıtlamalar nedeniyle ışın giriş kapaklarını paylaşmak mümkün değildir.

## Kullanım
Işın Üreticisi, [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) zincirinin son adımıdır ve tarifler için çıkış parçacık ışınlarından bir veya daha fazlasını yakalar. Daha açıkçası, her parçacık türünden kalıcı olarak 2B'ye kadar tamponlar ve bunları yalnızca bir tarif gerektirdiğinde tüketir.

Pasif bozunma yoktur ve parçacıkların hangi ışın giriş kapağından girdiği önemli değildir. **Ancak parçacıklar tampona yalnızca Işın Üreticisi etkin biçimde bir tarifi işlerken eklenir.**

Işın Üreticisi tarifleri, geçerli herhangi bir girdi alır almaz hemen başlar ve yalnızca makine gereken parçacıklardan yeterince aldığında tamamlanır; tıpkı [<ItemLink id="gregtech:gt.blockmachines:15331" showIcon="left" />](./research_station.md) hesaplama gücü tüketmesi gibi. Bu nedenle tariflerin süresi, parçacıkların tüketilme hızıyla kesin olarak belirlenir. Tamponda yeterli parçacık depolanmışsa anlık olabilir veya LHC'nin çarpışma enerjisi gereken parçacıkları üretmeye yetmiyorsa sonsuza kadar sürebilir.

Mevcut tüm tarifler, gereksinimleri ve iki parçacığı da kendi başına üretebilen modül(ler) ile birlikte aşağıdaki tabloda listelenmiştir. "Yok" sütunu, gereken parçacıkları üretmek için yalnızca bir [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) kullanıldığını belirtir - LHC gerekmez.

| Tarif | Kademe | Parçacık 1 || Parçacık 2 || Modüller |||||
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | Tür | Miktar | Tür | Miktar | Yok | CMS | ATLAS | ALICE | LHCb |
| <ItemLink id="miscutils:dustNeptunium238" showIcon="left" /> | EV | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="miscutils:particleBase:24" showIcon="left" />(1) | LuV | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 120 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 720 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="miscutils:particleBase:24" showIcon="left" />(64) | ^^ | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 5 | <ItemLink id="gtnhlanth:particle:6" showIcon="left" /> | 3 | &c✗ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32300" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 20 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="ExtraUtilities:unstableingot:2" showIcon="left" /> | ZPM | <ItemLink id="gtnhlanth:particle:1" showIcon="left" /> | 5 | <ItemLink id="gtnhlanth:particle:2" showIcon="left" /> | 5 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:1306" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 2 | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 2 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32301" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 20 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="miscutils:itemDustRadioactiveMineralMix" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="miscutils:MU-metaitem.01:32105" showIcon="left" /> | UV | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 250 | &a✓ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:11" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 3000 | <ItemLink id="gtnhlanth:particle:5" showIcon="left" /> | 3000 | &a✓ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32302" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 20 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:12" showIcon="left">ATLAS Casing</ItemLink> | UHV | <ItemLink id="gtnhlanth:particle:7" showIcon="left" /> | 900 | <ItemLink id="gtnhlanth:particle:7" showIcon="left" /> | 900 | &c✗ | &a✓ | &a✓ | &c✗ | &c✗ |
| <ItemImage id="bartworks:BioLabParts" nbt='tag:{Name:"Xenoxene Xenoxsis"}' label="right" format='&7Xenoxene Petri Dish' /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:13" showIcon="left">ALICE Casing</ItemLink> | UEV | <ItemLink id="gtnhlanth:particle:9" showIcon="left" /> | 450 | <ItemLink id="gtnhlanth:particle:9" showIcon="left" /> | 450 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.blockcasings13:14" showIcon="left">LHCb Casing</ItemLink> | UIV | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 750 | <ItemLink id="gtnhlanth:particle:14" showIcon="left" /> | 750 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.01:32417" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:8" showIcon="left" /> | 50 | <ItemLink id="gtnhlanth:particle:10" showIcon="left" /> | 30 | &c✗ | &c✗ | &a✓ | &c✗ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32270" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 20 | &c✗ | &c✗ | &c✗ | &c✗ | &a✓ |
| <ItemLink id="gregtech:gt.metaitem.03:32235" showIcon="left" /> | UMV | <ItemLink id="gtnhlanth:particle:11" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:13" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32236" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:12" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:13" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32238" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:16" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32237" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 1000 | <ItemLink id="gtnhlanth:particle:15" showIcon="left" /> | 1000 | &c✗ | &c✗ | &a✓ | &a✓ | &c✗ |
| <ItemLink id="gregtech:gt.metaitem.03:32239" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 200 | <ItemLink id="gtnhlanth:particle:17" showIcon="left" /> | 200 | &c✗ | &c✗ | &a✓ | &c✗ | &a✓ |
| <ItemLink id="gregtech:gt.metaitem.03:32240" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 25 | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 25 | &c✗ | &c✗ | &a✓ | &c✗ | &a✓ |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:183" showIcon="left" /> | ^^ | <ItemLink id="gtnhlanth:particle:4" showIcon="left" /> | 50 | <ItemLink id="gtnhlanth:particle:3" showIcon="left" /> | 5 | &c✗ | &c✗ | &c✗ | &c✗ | &a✓ |
{: widths="200, 30, 90, 40, 90, 40, 32, 32, 32, 32, 32"}

CMS modülü yalnızca bilinmeyen parçacıklara ait iki tarif gibi birkaç temel tarifi destekler. ATLAS modülü neredeyse her tarifi destekler çünkü çok geniş bir parçacık havuzuna sahiptir, ancak bu aynı zamanda belirli bir parçacığı elde etmeyi zorlaştırır. ALICE modülü de oldukça esnektir, ancak daha yoğun üretimler için havuzu çok daha küçüktür. LHCb modülü, ZPIC yonga plakası ve kararlı bozon muhafaza birimi gibi en gelişmiş tarifleri destekler ve en nadir iki parçacıkta daha yüksek verim sağlar.

## Kaynaklar

- [GTNH Wiki : Işın Üreticisi](https://wiki.gtnewhorizons.com/wiki/Beam_Crafter)