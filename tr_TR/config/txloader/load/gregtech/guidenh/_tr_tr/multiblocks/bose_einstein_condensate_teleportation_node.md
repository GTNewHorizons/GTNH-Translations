---
item_ids:
  - gregtech:gt.blockmachines:15757
quest_ids:
  - 52NvoXdXSuCp2hCvV_otBA==
navigation:
  title: Bose-Einstein Yoğunlaşması Işınlanma Düğümü
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15757
  position: -11001
---
# Bose-Einstein Yoğunlaşması Işınlanma Düğümü

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15757" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">Bose-Einstein Yoğunlaşması Işınlanma Düğümü (IO Düğümü)</ItemLink>, [BEC Hattı](./bose_einstein_condensate_line.md) içinde eşya yerleştirmek ve çıkarmak için kullanılan UIV kademe bir multibloktur; bir giriş/çıkış veriyoluna benzer. Ancak pratikte eşyalar IO Düğümünden hiç ayrılmaz ve tarifler [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md) yerine yerel olarak işlenir; teknik olarak bir Montajcı IO Düğümüdür ve Gözlem Dizisi aslında yalnızca güç, yoğunlaşma ve nanitler için büyük bir yönlendiricidir.

16 adede kadar IO Düğümü, görüş hattı bağlantı kapakları aracılığıyla aynı Gözlem Dizisine bağlanabilir; ancak aynı anda farklı tarifler çalıştırmak cezalar getirebileceği ve çıkışları potansiyel olarak yok edebileceği için önerilmez.

İsteğe bağlı olarak, o anda gereken nanitin kademesini okumak için <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> veya makineyi duraklatmak için <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> kullan.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | UIV |
| Yapı Boyutu (UxGxY) | 13x7x23 |
| Güç | Yok |
| Overclock | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

> [!NOTE]
> IO Düğümleri Gözlem Dizisi ile çalışır, bu yüzden mekanik açıklamalarının çoğu orada yazılmıştır.
> 
> Bu rehber sana yalnızca IO Düğümünün yapısı, inşası, otomasyon kapakları ve OpenComputers entegrasyonu hakkında bilgi verir.
>
> Genel mekanikler ve ayrıntılı tarifler için lütfen [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md) ve [BEC Hattı](./bose_einstein_condensate_line.md) rehberine bak.

## Üretim ve İnşa
### Üretim

<RecipesFor id="gregtech:gt.blockmachines:15757" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Yapı

IO Düğümünün kademeli bileşeni yoktur ve döndürülebilir veya ters çevrilebilir.

Bağlanmaları için <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> doğrudan [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md) üzerindeki bir tanesine bakmalıdır; ancak aralarında kablo yoktur ve gerekirse 128 blok mesafeye kadar ayrı olabilirler. Yalnızca aralarında opak blok olmadığından emin ol.

Bakım kapağı, hatta enerji kapağı yoktur; çünkü IO Düğümü tüm gücünü Gözlem Dizisinden alır.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left" /> | 1, Ön orta, 12. katman |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 94 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 88 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 56 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 18-48 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 44 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 44 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 32 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 20 |
| <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> | 1, Arka orta kasa |
| <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> | 0+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> | 0+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:71" noTooltip />Giriş Yolu | 1+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:81" noTooltip />Çıkış Yolu | 1+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |

### Duvar Paylaşımı

Bose-Einstein Yoğunlaşması Işınlanma Düğümü duvar paylaşımı yapabilir; ancak birden fazla IO Düğümünün konumu genellikle [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md) ve onun kapak konumu nedeniyle aralıklı olduğundan bu işe yaramaz.

## Kullanım

IO Düğümünde otomasyona yardımcı olabilecek 2 özel kapak vardır: <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" />.

<!-- Bu içerik BEC hattı rehberinden alınmıştır - değişiklik olursa ikisini de güncelle -->
- <ItemLink id="gregtech:gt.blockmachines:15758" showIcon="left" /> : GUI'sindeki ayarlanan koşul doğruysa kızıltaş sinyali yayar.  
  O anda istenen nanitin kademesi için bir karşılaştırma operatörü ve eşik değeri vardır.
- <ItemLink id="gregtech:gt.blockmachines:15759" showIcon="left" /> : kızıltaş sinyali aldığında makineyi ya hemen ya da yeni bir girdi adımına/nanite geçişte duraklatabilir.  
  Makineyi duraklatmak tüm tarif ilerlemesini durdurur ve yoğunlaşmanın yerleştirilmesini engeller; ancak IO Düğümü yine de Gözlem Dizisindeki nanitleri okuyabilir, nanit dedektörü kapaklarını güncellemeye devam eder ve güç tüketmeye devam eder.

### OpenComputers Entegrasyonu
IO Düğümü OpenComputers ile otomatikleştirilebilir ve standart GregTech multibloklarına kıyasla aşağıda görüldüğü gibi birkaç ek işlev/yöntem sunar. Bunlar hız bölenini dinamik olarak değiştirmek ve nanitler, yoğunlaşmalar ile mevcut tarif hakkında bilgi toplamak için kullanılabilir.
```lua
-- IO Düğümü için kullanılabilir tüm yöntemleri listele
local component = require('component')
local bec_io_node = component.bec_io_node

for k,v in pairs(bec_io_node) do print(k,v) end

-- İstenen nanit kademesini {name, tier} tablosu olarak döndürür
bec_io_node.getRequiredTier()

-- Sağlanan nanit kademesini {name, tier} tablosu olarak döndürür
bec_io_node.getProvidedTier()

-- Sağlanan nanit miktarını sayı olarak döndürür
bec_io_node.getAvailableNanites()

-- Gereken yoğunlaşma türlerini ve miktarlarını tablo olarak döndürür
bec_io_node.getRequiredCondensate()

-- Tüketilen yoğunlaşma türlerini ve miktarlarını tablo olarak döndürür
bec_io_node.getConsumedCondensate()

-- Tüm tarif adımlarını tablo olarak döndürür. Her adımda nanit (tablo), başlangıç tick'i (sayı), bitiş tick'i (sayı) ve indeks (sayı) bulunur
bec_io_node.getRecipeSteps()

-- Şu anda uygulanan yavaşlatma miktarını sayı olarak döndürür
bec_io_node.getSlowdowns()

-- IO Düğümünün hız bölenini sayı olarak döndürür
bec_io_node.getManualSlowdown()

-- IO Düğümünün hız bölenini bir sayıdan ayarlar
bec_io_node.setSpeedDivisor(divisor)
```

## Kaynaklar
- [GTNH Wiki: Bose-Einstein Yoğunlaşması Işınlanma Düğümü](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Teleportation_Node)