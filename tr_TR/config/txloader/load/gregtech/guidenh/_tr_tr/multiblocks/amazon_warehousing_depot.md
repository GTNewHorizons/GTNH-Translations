---
item_ids:
  - gregtech:gt.blockmachines:15513
quest_ids:
  - AAAAAAAAAAAAAAAAAAAH9w==
navigation:
  title: Amazon Depolama Tesisi
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15513
  position: -5001
---

# Amazon Depolama Tesisi
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15513" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15513" showIcon="left" />(AWD), çeşitli eşyaları paketleyip paket açmak için kullanılan IV kademesinde bir multibloktur.

AWD, tek blok paketleyici ve paket açıcıya doğrudan bir yükseltmedir; çünkü her iki tarif türünü de işleyebilir, %900'e kadar hızda çalışır, normalde gereken EU/t'nin yalnızca %75'ini kullanır ve gerilim kademesi başına 16 paralel sunar.

Aynı makinede farklı şemalar kullanmak için AWD'de giriş ayrıştırması etkinleştirilmelidir.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | IV |
| Yapı Boyutu (U×G×Y) | 3x5x3 |
| Güç | Normal |
| Overclock | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | 40 gibbl/s kirlilik üretir ve Egzoz Çıkışı gerektirir |

## Üretim ve İnşa

### Üretim

<RecipesFor id="gregtech:gt.blockmachines:15513" handlerBlacklist="codechicken.nei.recipe.ShapelessRecipeHandler" />

<RecipesFor id="miscutils:gtplusplus.blockcasings.3:9" />

<RecipesFor id="gregtech:gt.blockframes:32" 
handlerBlacklist="neicustomdiagram.diagramgroup.gregtech.materialtools, neicustomdiagram.diagramgroup.gregtech.materialparts" />

### Yapı

AWD'nin tek kademeli bileşeni vardır: makinenin hız bonusunu belirleyen boru muhafazası blokları.

Cam her kademeden olabilir ve makinenin çalışmasını etkilemez.

AWD döndürülebilir veya aynalanabilir.

Çok amperli ve lazer enerji kapakları desteklenmez; ancak overclock için birden fazla normal enerji kapağı kullanılabilir. Bu bileşenlerin kademesini belirtmek için "item_pipe" ve "glass" alt kanallarıyla yapıyı görselleştirmek/inşa etmek üzere <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Adet ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15513" showIcon="left" /> | 1, Ön sağ, 2. katman |
| <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> | 4-15 |
| <ItemImage id="gregtech:gt.blockcasings11" /><Color id="blue">Kademeli</Color> Boru Muhafazası | 3 |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi Bir Kademeli Cam | 3 |
| <ItemLink id="gregtech:gt.blockframes:32" showIcon="left" /> | 2 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:91" noTooltip />Egzoz Çıkışı | 1+, <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1+, <ItemLink id="miscutils:gtplusplus.blockcasings.3:9" showIcon="left" /> yerine geçebilir |

### Duvar Paylaşımı

AWD'ler kasa, çerçeve kutusu ve veriyolu/kapak tasarrufu için sağ taraf dışında (kontrolcü engel oluyor) her kenarında duvar paylaşımı yapabilir. Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden bir enerji kapağını iki makine arasında paylaşmak mümkündür.

## Kullanım

AWD'nin aşağıda listelenen iki çalışma modu vardır. Modlar arasında kontrolcünün GUI'sinden veya kontrolcüye tornavidayla sağ tıklayarak geçiş yap. Paketleyici modu, [<ItemLink id="gregtech:gt.blockmachines:15563" showIcon="left" />](./electric_implosion_compressor.md) çıktısı olan minik ve küçük toz yığınları ile hurda kutuları oluşturmak için kullanışlıdır. Paket açıcı modu ise eski [<ItemLink id="gregtech:gt.blockmachines:13106" showIcon="left" />](./lapotronic_supercapacitor.md) kapasitörleri gibi belirli eşyaları geri dönüştürmek için hoş bir ekstradır.

- Paketleyici - YALNIZCA paketleyici tariflerini çalıştırır.
- Paket Açıcı - YALNIZCA paket açıcı tariflerini çalıştırır.

Farklı giriş yollarındaki KATI bileşenlerin, şemalar dahil, aynı tarifte kullanılmasını önlemek için AWD'de giriş ayrıştırması<FloatingImage src="gregtech:textures/gui/overlay_button/input_separation_on.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={3.0} scaleY={3.0} /> etkinleştirilmelidir. Bu, birçok giriş yoluna sahip tek bir AWD'nin aynı anda birçok farklı şemayı destekleyebileceği anlamına gelir. Yalnızca minimum tedarik deposu kasası sayısının üzerinde kalmayı unutma.

### Boru Muhafazasıyla Hız Yükseltmeleri

AWD, daha yüksek kademeli Boru Muhafazası kullanılarak yükseltilebilir. Her Boru Muhafazasının hız bonusu aşağıda listelenmiştir. 

| Boru Muhafazası | Hız |
| --- | --- |
| <ItemLink id="gregtech:gt.blockcasings11" showIcon="left" /> | 200% |
| <ItemLink id="gregtech:gt.blockcasings11:1" showIcon="left" /> | 300% |
| <ItemLink id="gregtech:gt.blockcasings11:2" showIcon="left" /> | 400% |
| <ItemLink id="gregtech:gt.blockcasings11:3" showIcon="left" /> | 500% |
| <ItemLink id="gregtech:gt.blockcasings11:4" showIcon="left" /> | 600% |
| <ItemLink id="gregtech:gt.blockcasings11:5" showIcon="left" /> | 700% |
| <ItemLink id="gregtech:gt.blockcasings11:6" showIcon="left" /> | 800% |
| <ItemLink id="gregtech:gt.blockcasings11:7" showIcon="left" /> | 900% |

## Kaynaklar

- [GTNH Wiki: Amazon Depolama Tesisi](https://wiki.gtnewhorizons.com/wiki/Amazon_Warehousing_Depot)