---
item_ids:
  - gregtech:gt.blockmachines:3011
quest_ids:
  - 3SzKMSj0StOAOzVmInDjZQ==
navigation:
  title: Büyük Varil Bira Fabrikası
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:3011
  position: -3001
---
# Büyük Varil Bira Fabrikası
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:3011" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:3011" showIcon="left">Büyük Varil Bira Fabrikası (BBB)</ItemLink>, seri bira üretimi için HV kademesi bir multibloktur. BBB, %150 hızda çalıştığı ve gerilim kademesi başına 4 paralel sunduğu için tek bloklu bira fabrikasının doğrudan yükseltmesidir. BBB esas olarak [<ItemLink id="gregtech:gt.blockmachines:12712" showIcon="left" />](./bacterial_vat.md) için biyokütle ve bakteri üretmekte kullanılır.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | HV |
| Yapı Boyutu (BxGxY) | 3x3x5 |
| Güç | Normal |
| Overclock | Kusurlu |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:3011" />

<RecipesFor id="gregtech:gt.blockcasings10:15" />

<RecipesFor id="gregtech:gt.blockframes:305" />

### Yapı
BBB'nin kademeli bileşeni yoktur. Cam her kademede olabilir ve makinenin çalışmasına etkisi yoktur.

Çok amperli ve lazer enerji kapakları desteklenmez, ancak overclock/paralel için birden fazla normal enerji kapağı olabilir.

BBB döndürülebilir veya ters çevrilebilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan; camın kademesini belirtmek için "glass" alt kanalını kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:3011" showIcon="left" /> | 1, Ön orta, 3. katman |
| <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> | 14-22 |
| <ItemLink id="gregtech:gt.blockframes:305" showIcon="left" /> | 4, 1. katmanın her köşesi |
| <ItemImage id="bartworks:BW_TieredGlass" />Herhangi Bir Kademeli Cam | 6 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Yalnızca Normal Kapaklara izin verilir</Tooltip> | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:90" noTooltip />Bakım Kapağı | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 0+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:61" noTooltip />Çıkış Kapağı | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings10:15" showIcon="left" /> yerini alabilir |

### Duvar Paylaşımı
BBB'ler kasa, çerçeve kutusu, cam ve veriyolu/kapak tasarrufu için her kenarını duvar paylaşımına açabilir.

Hiçbir tarif 1A'dan fazla güç kullanmaz, bu yüzden bir enerji kapağını iki makine arasında paylaşmak mümkündür.

## Kullanım
BBB, [Bira Fabrikası](/singleblock/brewery.md) tariflerini %150 hızda işleyebilir.

Paraleller aşağıdaki tabloda görüldüğü gibi gerilim kademesi başına 4 artar:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paralel | 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |
{: widths="60"}

Tek bir Enerji Kapağı makineye 2A sağlayabilse bile makine tarifi kapak başına 1A kullanarak işler. Bu nedenle 2A sağlayan tek bir Enerji Kapağı aynı kademedeki tarifleri paralel olarak işleyemez.

## Kaynaklar
- [GTNH Wiki : Büyük Varil Bira Fabrikası](https://wiki.gtnewhorizons.com/wiki/Big_Barrel_Brewery)