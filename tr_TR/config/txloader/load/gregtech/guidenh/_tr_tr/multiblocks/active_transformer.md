---
item_ids:
  - gregtech:gt.blockmachines:15300
quest_ids:
  - AAAAAAAAAAAAAAAAAAAKqw==
  - AAAAAAAAAAAAAAAAAAAKqg==
navigation:
  title: Aktif Trafo
  parent: ./multiblocks_index.md
  icon: gregtech:gt.blockmachines:15300
  position: -7001
---

# Aktif Trafo

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15300" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15300" showIcon="left" /> (AT), gücü herhangi bir gerilim kademesinden herhangi bir başka gerilim kademesine neredeyse sınırsız amperaj akışıyla dönüştüren ZPM kademesinde bir multibloktur. 

AT, tek bloklu trafoların ve düşürücü konvertörlerin doğrudan yükseltmesidir; çünkü çok amperli ve lazer enerji/dinamo kapaklarını destekler, yeni bir makine inşa etmeden girdi/çıktı gerilimini değiştirebilir ve farklı gerilimlerde birden fazla girdi/çıktı destekler. 

Tek dezavantajı, makineden geçen tüm EU için %0,004 güç kaybı olmasıdır. 

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | ZPM |
| Yapı Boyutu | 3×3×3 |
| Güç | Herhangi bir Kapak kullanılabilir, Çok Amperli ve Lazer Kapakları dahil |
| Hız Aşırtma | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |


## Üretim ve İnşa

### Üretim
<RecipesFor id="gregtech:gt.blockmachines:15300" handlerId="gt.recipe.assembler"/>

<RecipesFor id="tectech:gt.blockcasingsTT" handlerId="gt.recipe.assembler" />

AT, 1 adet <ItemLink id="gregtech:gt.blockcasings:15" showIcon="left" /> gerektirir (Bunun tariflerini görmek için eşya bağlantısının üzerine gelirken <KeyBind id="nei.options.keys.recipe.recipe" /> tuşuna basabilirsin). Bunu mevcut süperiletken kademene uyan tariflerle üretebilirsin.

### Yapı
AT her yönde döndürülebilir, yukarı ve aşağı dahil.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15300" showIcon="left" /> | 1, Ön orta, 2. katman. |
| <ItemLink id="tectech:gt.blockcasingsTT" showIcon="left" /> | 5-24 |
| <ItemLink id="gregtech:gt.blockcasings:15" showIcon="left" /> | 1, Yapının merkezi |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 1+, Herhangi bir kasa. |
| <ItemImage id="gregtech:gt.blockmachines:31" noTooltip /><Tooltip label="Dynamo Hatch">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 0+, Herhangi bir kasa. |

### Duvar Paylaşımı

AT'ler kasa tasarrufu yapmak ve hatta gücü bölüşmek için her bir yüzünü duvar paylaşımıyla kullanabilir. Tam kapasitede, girdi EU/t aynı enerji kapağını veya lazer hedef kapağını paylaşan AT'ler arasında eşit olarak bölünür. Biri doluysa veya artık güç tüketmiyorsa fark kalan AT'ler arasında paylaştırılır.

## Kullanım
AT, Enerji Kapaklarından güç alır ve gücü Dinamo Kapakları aracılığıyla çıkarır; tıpkı [<ItemLink id="gregtech:gt.blockmachines:13106" showIcon="left" />](./lapotronic_supercapacitor.md) gibi. Gerilim ve amperaj ÖNEMLİ DEĞİLDİR. 

Bu, girdi/çıktı gerilimin ve amperajının tamamen yalnızca Enerji/Dinamo Kapaklarının gerilimine ve maksimum amperajına bağlı olduğu ve fazla gücün yok edilmediği veya yeni güç üretilmediği anlamına gelir.

AT'ler birden fazla girdi ve çıktıya sahip olabildiğinden, birden fazla güç kaynağını tek bir birimde birleştirebilir veya birleştirilmiş gücü birkaç Dinamo Kapağı ya da Lazer Kaynağı Kapağı aracılığıyla birden fazla makineye dağıtabilir.

<ItemLink id="gregtech:gt.blockmachines:15466" showIcon="left" /> UHV+ seviyesinde kullanılabilir hale gelene kadar AT çoğunlukla lazer güç hatlarını yönlendirmek için kullanılır.

## Kaynaklar
- [GTNH Wiki: Active Transformer](https://wiki.gtnewhorizons.com/wiki/Active_Transformer)