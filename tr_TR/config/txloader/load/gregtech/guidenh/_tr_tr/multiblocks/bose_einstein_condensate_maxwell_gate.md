---
item_ids:
  - gregtech:gt.blockmachines:15760
quest_ids:
  - HvtY6xu3RAKjwhAZCTwK8A==
navigation:
  title: Bose-Einstein Yoğuşması Maxwell Geçidi
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15760
  position: -11001
---
# Bose-Einstein Yoğuşması Maxwell Geçidi
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15760" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left" />, [BEC Hattı](./bose_einstein_condensate_line.md)'nda yoğuşma akışını yalnızca tek yönde sınırlamak için UIV kademesinde bir Multibloktur--ME depolama veriyoluna benzer. 

Maxwell Geçidi bir BEC ağında herhangi bir yere yerleştirilebilir ve onu etkili bir şekilde, yapının her iki yanındaki <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" />'ya bağlanan iki ayrı alt ağa böler. Sol ağdaki her şey sağ ağa açıktır, ancak tersi geçerli değildir. 

Maxwell Geçidi ayrıca belirli yoğuşmalar için filtreleme yapabilir ve etkinken, ağlardan birinin durumundan bağımsız olarak yalnızca 1A UIV tüketir. 

Filtreyi, kontrolcünün GUI'sinde manuel olarak veya girdi kapaklarını istenen yoğuşmanın orijinal sıvısıyla doldurarak ayarla.

> [!WARNING]
> Bu rehberde "Sol Ağ" maruz bırakılan ağ, "Sağ Ağ" ise izleyen ağ anlamına gelir. Terimler açıklama kolaylığı için birleştirilmiştir.
>
> Makinenin yönünü ve ters çevrilme durumunu kontrol etmelisin - `sol` ve `sağ` terimleri varsayılan makine oluşumuna dayanır - kontrolcüyü ters çevirmek yönü değiştirir.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | UIV |
| Yapı Boyutu (Uzunluk x Genişlik x Yükseklik) | 11x17x11 |
| Güç | Herhangi bir Kapak kullanılabilir; Çoklu Amper ve Lazer Kapakları dahil |
| Hız Aşırtmalar | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

> [!TIP]
> Maxwell Geçidi'nin yönünü kontrolcü animasyonuna bakarak kontrol edebilirsin - girdi ağından çıktı ağına hareket eden bazı "akışlar" gösterir.

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:15760" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Yapı

Maxwell Geçidi'nde kademeli bileşen yoktur; döndürülebilir veya ters çevrilebilir.

Enerji Kapağı, yapının herhangi bir yerindeki elektromanyetik olarak yalıtılmış herhangi bir kasanın yerini alabilir. 

Çoklu amper ve lazer enerji kapakları desteklenir, ancak zaten her zaman yalnızca 1A UIV (33.554.432 EU/t) tüketir.  
Güç kademesi önemli değildir; bu yüzden 4A UEV, 16A UHV veya başka bir şey sağlayabilirsin.

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left" /> | 1, Ön merkez, 6. katman |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 148 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 92 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 75-90 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 84 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 70 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 68 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 40 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 24 |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 2, Sol ve sağ kasanın her birinin merkezinde |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Enerji Kapağı">Normal, Çoklu Amper, Lazer kullanılabilir</Tooltip> | 1+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerini alabilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 0+, herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerini alabilir |

### Duvar Paylaşımı

Maxwell Geçidi birkaç blok tasarrufu için her bir kenarını duvar paylaşımına açabilir ve iki makine arasında 1 Enerji Kapağı paylaşabilir.

## Kullanım

Maxwell Geçidi veya BEC Diyodu, yoğuşma maruziyetini/görünürlüğünü kontrol etmek için [BEC Hattı](./bose_einstein_condensate_line.md)'nda isteğe bağlı bir adımdır. Maxwell Geçidi kendisi hiçbir yoğuşmayı itmez, çekmez veya tamponlamaz.

Maxwell Geçidi bir BEC ağında herhangi bir yere yerleştirilebilir ve onu etkili bir şekilde, yapının her iki yanındaki <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" />'ya bağlanan iki ayrı alt ağa böler. Sol ağdaki her şey sağ ağdaki her şeye açıktır, ancak tersi geçerli değildir.

[<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left">Dolanıklık Aparatı</ItemLink>](./bose_einstein_condensate_entanglement_apparatus.md)'nın yoğuşmayı bir Maxwell Geçidi üzerinden bir [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Muhafaza Alanı</ItemLink>](./bose_einstein_condensate_containment_field.md)'na itebilmesi için Dolanıklık Aparatı __**mutlaka**__ sağ ağda ve Muhafaza Alanı __**mutlaka**__ sol ağda olmalıdır; aşağıdaki görselde olduğu gibi.  
Eşit dağıtım kuralları hâlâ geçerlidir; birden fazla Muhafaza Alanı mevcutsa yoğuşma, toplam alan güçleriyle orantılı olarak bölünür.

[<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md)'nin bir Muhafaza Alanından yoğuşmayı bir Maxwell Geçidi üzerinden çekebilmesi için Gözlem Dizisi __**mutlaka**__ sağ ağda ve Muhafaza Alanı __**mutlaka**__ sol ağda olmalıdır; aşağıdaki görselde olduğu gibi.  
Kirletici cezaları hâlâ geçerlidir; talep edilmemiş her yoğuşma işlem hızını önemli ölçüde yavaşlatır ve ağda aynı anda üçten fazla kirletici bulunursa tarif derhal başarısız olur ve boşa gider.  

![Geçerli ve geçersiz Maxwell Geçidi kurulumları - Fox'tan görsel](/assets/images/multiblocks/bec_diode_setup.png)

Maxwell Geçidi varsayılan olarak tüm yoğuşmanın geçmesine izin verir, ancak belirli yoğuşmalar için de filtre uygulayabilir.  
Filtreyi, kontrolcünün GUI'sinde <FloatingImage src="gtnhintergalactic:textures/gui/overlay_button/options.png" wrap="inline" x={0} y={0} w={16} h={16} scaleX={4.0} scaleY={4.0} /> veya girdi kapaklarını istenen yoğuşmanın orijinal sıvısıyla doldurarak manuel olarak ayarla. 

Filtreleme, pasif yoğuşma üretimi için özellikle kullanışlıdır ve kirleticilerin Gözlem Dizisi'ne maruz kalmasını önler. Bu olmadan, yoğuşmanın talep üzerine istenmesi gerekirdi; Dolanıklık Aparatı hız aşırtılamadığı için bu çok uzun sürebilir.

### OpenComputers Entegrasyonu
Maxwell Geçidi OpenComputers ile otomatikleştirilebilir ve aşağıda görüldüğü gibi standart GregTech multibloklarına kıyasla birkaç ek işlev/yönteme sahiptir. Bunlar, gerçek sıvıları ve girdi kapaklarını kullanmak yerine yoğuşma filtresini bir betikle dinamik olarak değiştirmek için kullanılabilir.

```lua
-- Maxwell Geçidi için mevcut tüm yöntemleri listele
local component = require('component')
local bec_diode = component.bec_diode

for k,v in pairs(bec_diode) do print(k,v) end

-- Mevcut yoğuşma filtresinin sıvı adını döndürür
bec_diode.getCondensateFilter()

-- Yoğuşma filtresini verilen sıvı adına ayarlar
bec_diode.setCondensateFilter('name')
```

Aşağıdaki tablo, OpenComputers'ın kullandığı sıvı adını ve hangi yoğuşmanın eşleştiğini gösterir. 
| Yoğuşma | OC'deki Adlar |
| --- | --- |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:941" showIcon="left" /> | entangled_neutronium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:942" showIcon="left" /> | entangled_cosmicneutronium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:943" showIcon="left" /> | entangled_bedrockium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:944" showIcon="left" /> | entangled_chromaticglass |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:945" showIcon="left" /> | entangled_celestialtungsten |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:946" showIcon="left" /> | entangled_infinity |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:947" showIcon="left" /> | entangled_hypogen |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:948" showIcon="left" /> | entangled_transcendentmetal |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:949" showIcon="left" /> | entangled_dimshiftedsuperfluid |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:950" showIcon="left" /> | entangled_phononmedium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:951" showIcon="left" /> | entangled_quarkgluonplasma |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:952" showIcon="left" /> | entangled_spacetime |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:953" showIcon="left" /> | entangled_time |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:954" showIcon="left" /> | entangled_space |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:955" showIcon="left" /> | entangled_cosmicsolder |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:956" showIcon="left" /> | entangled_mhdcsm |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:957" showIcon="left" /> | entangled_Magmadde |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:958" showIcon="left" /> | entangled_universium |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:959" showIcon="left" /> | entangled_eternity |


## Kaynaklar
- [GTNH Wiki : Bose-Einstein Yoğuşması Maxwell Geçidi](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Maxwell_Gate)