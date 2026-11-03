---
item_ids:
  - gregtech:gt.blockmachines:15755
quest_ids:
  - 0U_ex_O9TKWF-ShWD_4UuQ==
navigation:
  title: Bose-Einstein Yoğuşuk Muhafaza Alanı
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15755
  position: -11001
---
# Bose-Einstein Yoğuşuk Muhafaza Alanı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15755" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left" />, [BEC Hattı](./bose_einstein_condensate_line.md) içinde dolanık yoğuşuk depolamak için kullanılan UIV kademesi bir multibloktur; bir sıvı tankına benzer. 

Dolanık yoğuşuk, [<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Dolanıklık Cihazı</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md) içinde üretilir ve BEC kapakları aracılığıyla Muhafaza Alanına aktarılır.

Depolanan yoğuşuk, mevcut ağdaki tüm [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizilerine</ItemLink>](./bose_einstein_condensate_observation_array.md) maruz kalır ve makineden yalnızca bir tarif için İo Düğümü tarafından talep edildiğinde çıkar.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | UIV |
| Yapı Boyutu (UxGxY) | 45x45x17 |
| Güç | Her tür kapak kullanılabilir, Çok Amperli ve Lazer Kapakları dahil |
| Overclock | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve Yapım
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:15755" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

### Yapı

Muhafaza Alanının kademeli bileşenleri yoktur. 

Makinenin kapasitesini büyük ölçüde artırmak için çok amperli ve lazer enerji kapakları desteklenir. 

Muhafaza Alanı döndürülebilir veya çevrilebilir.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

Muhafaza Alanına özgü olan <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" />, GUI'sinde ayarlanan koşul doğruysa Kızıltaş sinyali yayar.  
Belirli bir dolanık yoğuşuk türünü belirtmek için bir filtre, bir karşılaştırma operatörü ve bir eşik değeri vardır.  
Örneğin, dolanık sonsuzluk yoğuşuğu 100.000L'ye eşit veya daha büyükse Kızıltaş sinyali yay. Tüm depolanan yoğuşukları toplamak için filtreyi boş bırak.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left" /> | 1, Ön orta, 3. katman |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 1236 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 1045 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 896 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 568 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 508 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 439-442 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 324-343 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 1+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1-4, 9. katmanın dört yanının her birindeki <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçer |
| <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> | 0+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |

### Duvar Paylaşımı

Muhafaza Alanı, çok sayıda bloktan tasarruf etmek için her bir yüzünü duvar paylaşımıyla kullanabilir; ancak GUI üzerinden tek bir Muhafaza Alanıyla kapasite neredeyse sonsuza kadar artırılabildiği için genellikle birden fazla inşa edilmez.

## Kullanım

Muhafaza Alanı, [BEC Hattı](./bose_einstein_condensate_line.md) içindeki ikinci adımdır ve bir tarif için [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">İo Düğümü</ItemLink>](./bose_einstein_condensate_teleportation_node.md) tarafından talep edilene kadar dolanık yoğuşuk depolar. Yoğuşuk Muhafaza Alanına girer ve oradan çıkar; her iki yönde de akış, yapının yanlarındaki BEC kapakları üzerinden gerçekleşir ve mevcut ağdaki tüm [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizilerine</ItemLink>](./bose_einstein_condensate_observation_array.md) maruz kalır. İsteğe bağlı olarak, bir diyot ve sıvı filtresine benzer şekilde yoğuşuk akışının yönünü filtrelemek ve sınırlamak için bir [<ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left">Maxwell Kapısı</ItemLink>](./bose_einstein_condensate_maxwell_gate.md) kullan.

Muhafaza Alanının alan gücü, kontrolcünün GUI'sinde "Edit Parameter" düğmesine tıklanarak<FloatingImage src="gtnhintergalactic:textures/gui/overlay_button/options.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} />(veya OpenComputers ile) elle ayarlanır ve hem maksimum kapasiteyi hem de makinenin pasif güç tüketimini belirler; her 1 birim alan gücü, 1 EU/t maliyetle maksimum kapasiteyi 1L artırır. Depolamayı yoğuşuk türüne göre filtrelemek veya bölümlemek mümkün değildir.

Maksimum kapasite yalnızca yumuşak bir üst sınırdır; fazla yoğuşuk yine de Muhafaza Alanına girebilir, ancak seviye maksimum kapasitenin altına düşene kadar her saniye tüm yoğuşuğun %11'i yok edilir. Bu ceza tüm depolanan yoğuşuklara eşit şekilde uygulanır ve hiçbirini diğerlerine göre asla önceliklendirmez.  
Alan gücünü gerçekten yüksek ayarlayarak ya da yoğuşuk seviyeleri çok yükseldiğinde filtresiz bir <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> kullanıp makine kontrolcü kapağıyla [<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Dolanıklık Cihazını</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md) devre dışı bırakarak bu cezadan kaçın.

> [!CAUTION]
> Muhafaza Alanının gücü herhangi bir nedenle kesilirse veya elle devre dışı bırakılırsa tüm içeriğini yok eder. Kullanımdayken, kapatılması kesinlikle gerekmedikçe her zaman çalışır durumda tut.

Aynı ağda birden fazla Muhafaza Alanı varsa, ağa verilen yoğuşuk toplam alan güçleriyle orantılı olarak bölünür.  
Örneğin, bir Muhafaza Alanının alan gücü 150.000, diğerininki 50.000 ise ilki yoğuşuğun %75'ini, ikincisi ise yalnızca %25'ini alır.

### OpenComputers Entegrasyonu

Muhafaza Alanı OpenComputers ile otomatikleştirilebilir ve aşağıda görüldüğü gibi standart GregTech multibloklarına kıyasla birkaç ek fonksiyona/metoda sahiptir. Bunlar, yok edilmeye karşı ek koruma olarak mevcut yoğuşuk seviyelerine göre Muhafaza Alanının alan gücünü dinamik olarak değiştirmek için kullanılabilir.

```lua
-- Muhafaza Alanı için mevcut tüm yöntemleri listele
local component = require('component')
local bec_storage = component.bec_storage

for k,v in pairs(bec_storage) do print(k,v) end

-- Depolanan tüm yoğuşuğu, sıvı adlarını miktarlara eşleyen bir tablo olarak döndürür
bec_storage.getStoredCondensate()

-- Muhafaza Alanının alan gücünü sayı olarak döndürür
bec_storage.getFieldStrength()

-- Muhafaza Alanının alan gücünü bir sayıdan ayarlar
bec_storage.setFieldStrength(strength)
```
```lua
---@meta

-- OpenComputers `bec_storage` bileşeni için sahte tanım.

---@class BecStorageComponentProxy: ComponentProxy
BecStorageComponentProxy = {}

---**Mevcut** Muhafaza Alanında depolanan tüm yoğuşukları getir.
---@return table[string, number] depolanan yoğuşukların tablosu.
function BecStorageComponentProxy.getStoredCondensate() end

---Bağlı Muhafaza Alanının mevcut alan gücünü getir.
---@return number mevcut alan gücü.
function BecStorageComponentProxy.getFieldStrength() end
  
---Muhafaza Alanının alan gücünü yapılandır. 0'ın altındaki sayı 1 olarak yorumlanır.
---@param  strength number
function BecStorageComponentProxy.setFieldStrength(strength) end
```

## Kaynaklar
- [GTNH Wiki : Bose-Einstein Yoğuşuk Muhafaza Alanı](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Containment_Field)