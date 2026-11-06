---
item_ids:
  - gregtech:gt.blockmachines:15756
quest_ids:
  - KV1vw68JTb-KiHQzBEPzBw==
navigation:
  title: Bose-Einstein Yoğunlaşması Gözlem Dizisi
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15756
  position: -11001
---
# Bose-Einstein Yoğunlaşması Gözlem Dizisi

<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15756" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left" />, [BEC Hattı](./bose_einstein_condensate_line.md) içindeki bağlı herhangi bir [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Nodes</ItemLink>](./bose_einstein_condensate_teleportation_node.md) düğümüne güç, yoğunlaşma ve nanit sağlayan UIV kademe bir Multiblok'tur. 

Gözlem Dizisi aslında bir Montajcı değil, sadece büyük bir yönlendiricidir çünkü hiçbir Tarif işlemez ve kendisi yoğunlaşma tutmaz. Yalnızca IO Node'ların okuyabilmesi için yerel olarak nanit depolar ve talep üzerine [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Muhafaza Alanları</ItemLink>](./bose_einstein_condensate_containment_field.md) ile IO Node'lar arasında yoğunlaşma aktarır. 

Aynı Gözlem Dizisi'ne görüş hattı bağlayıcı kapakları aracılığıyla 16 adede kadar IO Node bağlanabilir, ancak aynı anda farklı Tarifler çalıştırmanız önerilmez çünkü bu cezalar getirebilir ve muhtemelen çıktıları hiçliğe gönderebilir. IO Node'ların kendi Enerji Kapakları yoktur, bu yüzden bireysel güç maliyetleri toplanır ve Gözlem Dizisi tarafından karşılanır; bu da ciddi verim için çok amperli ve lazer Enerji Kapaklarını destekler.

BEC tarifleri NEI'de [<ItemLink id="gregtech:gt.blockmachines:1170" showIcon="left" />](./assembly_line.md) tarifleri olarak görünür, ancak takip edilmesi gereken katı bir eşya veya yoğunlaşma sırası yoktur. Bunun yerine, katı girdi sayılarına eşit sayıda, eşit uzunlukta belirli sayıda adım içerirler. Adımlar tam olarak kesin duraklar değildir, ancak her biri çalışmak için belirli bir nanit kademesi veya daha iyisini talep eder ve istenen kademeyi aşmak IO Node'un işlem hızını önemli ölçüde düşürür.  
Nanitler aslında hiç tüketilmez, ancak her zaman istenen nanitle tam olarak eşleşmesi için Gözlem Dizisi'nden hızla değiştirilmeleri gerekir.  
Nanit sırası her Tarif için sabittir ancak Tarifler arasında değişir, bu yüzden herhangi bir otomasyon yönteminin son derece hassas ve esnek olması gerekir.

| Özellik | Ayrıntılar |
| --- | --- |
| Açılma Kademesi | UIV |
| Yapı Boyutu (UxGxY) | 61x31x31 |
| Güç | Her Kapak kullanılabilir, Çok Amperli ve Lazer Kapakları dahil |
| Hız Aşımı | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim

<RecipesFor id="gregtech:gt.blockmachines:15756" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:6" handlerBlacklist="gt.recipe.researchStation" />

### Yapı

Gözlem Dizisi'nde kademeli bileşenler yoktur ve döndürülebilir veya ters çevrilebilir.

Her <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" />, bağlanabilmeleri için doğrudan bir [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) düğümüne bakmalıdır, ancak aralarında kablo yoktur ve gerekirse 128 blok mesafeye kadar uzakta olabilirler. 

Ciddi verim için çok amperli ve lazer Enerji Kapakları desteklenir. 

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

<ItemLink id="gregtech:gt.blockmachines:9415" showIcon="left" /> esasen yalnızca nanitler için bir Giriş Yolu'dur ve aynı anda 2.147.483.647'ye kadar tutabilir.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left" /> | 1, Ön orta, 16. Katman |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 1700 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 1515 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 1444-1458 |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 838 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 790 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 664 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 560 |
| <ItemLink id="gregtech:gt.blockcasings.bec:6" showIcon="left" /> | 464 |
| <ItemLink id="gregtech:gt.blockmachines:9415" showIcon="left" /> | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine kullanılabilir |
| <ItemLink id="gregtech:gt.blockmachines:15481" showIcon="left" /> | 1+, Her halkanın kenarının ortasında <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> yerine kullanılabilir |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1-2, Makinenin sol veya sağ ucundaki orta kısımda <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> yerine geçer |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Normal, Çok Amperli, Lazer kullanabilir</Tooltip> | 1+, Herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine kullanılabilir |

### Duvar Paylaşımı

Duvar paylaşımı kullanmak az sayıda kasa tasarrufu sağlar, ancak karşılığında 4 [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) bağlantısını kaybedersin (2 gözlem dizisi olduğu için toplamda 8) ve yoğunlaşma kapakları paylaşılamaz.

## Kullanım

Gözlem Dizisi, bağlı [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Node</ItemLink>](./bose_einstein_condensate_teleportation_node.md) düğümlerine güç, yoğunlaşma ve nanit sağlayan bir yönlendirici olarak çalışır. Gözlem Dizisi'ne 16 adede kadar IO Node bağlanabilir.  
Montajcı olarak listelenmesine rağmen, Gözlem Dizisi'ni büyük bir yönlendirici, IO Node'u ise Montajcı olarak düşün çünkü Tarifleri asıl işleyen ikincisidir.

> [!NOTE]
> BEC hattının genel olarak nasıl çalıştığını ve Gözlem Dizisi'nin BEC Hattı'nda ne yaptığını görmek için [BEC Hattı](./bose_einstein_condensate_line.md) sayfasına bak. Bu rehber yalnızca Gözlem Dizisi'ne özel bilgileri kapsar.

### Yoğunlaşma

Gözlem Dizisi, [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Muhafaza Alanları</ItemLink>](./bose_einstein_condensate_containment_field.md) aksine kendisi hiç yoğunlaşma tutmaz, yalnızca talep üzerine onu Muhafaza Alanından IO Node'a aktarır.

Ağ'da mevcut Tarif tarafından istenmeyen her yoğunlaşma bir kirletici veya yavaşlatıcı olarak kabul edilir. Her kirletici IO Node'un işlem hızını önemli ölçüde düşürür ve Ağ'da aynı anda üçten fazla kirletici olursa Tarif hemen başarısız olur ve hiçliğe gider.  
Bir IO Node'a sağlanan yoğunlaşma artık Ağ'da sayılmaz ve bu yüzden aynı Gözlem Dizisi'nde başka Tarifler işleyen diğer IO Node'ları etkilemez. Ancak bu cezaları tamamen önlemek için yine de aynı anda yalnızca bir Tarif işlemen önerilir.

### Nanitler

<LineChart 
  wrap="square" align="right"
  categories="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
  xAxisLabel="Nanit Sayısı"
>
  <Series name="Δ=0, no unmatched contaminants" data="1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20" />
  <Series name="Δ=3, no unmatched contaminants" data="0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2" />
  <Series name="Δ=0, 2 unmatched contaminants" data="0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6" />
  <Series name="Δ=3, 2 unmatched contaminants" data="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0" />
</LineChart>

Tarifler, katı girdi sayısına eşit sayıda sıralı ve eşit uzunlukta adımda işlenir.  
Örneğin <ItemLink id="gregtech:gt.metaitem.03:32310" />, Tarifinde beş katı girdi olduğu için her biri toplam sürenin 1/5'i olan beş adımda işlenir. 

Adımlar tam olarak kesin duraklar değildir, ancak her biri çalışmak için belirli bir nanit kademesi veya daha iyisini talep eder ve istenen kademeyi aşmak, aşağıdaki denklemlerde ve grafiklerde görüldüğü gibi IO Node'un işlem hızını önemli ölçüde düşürür. 

<Latex formula="\Delta = \text{Nanite Tier Provided} - \text{Nanite Tier Requested}" scale="0.8" />
<Latex formula="d = \text{Max}(1 + \text{Unrequested Contaminant}, \text{Speed Divisor})" scale="0.8" />
<Latex formula="+\text{Progress Ticks/t} = \Biggl\lfloor \frac{\text{Min}(30720, \text{ Nanites Available})}{\text{Active Parallels} \times 2^\Delta \times d } \Biggl\rfloor" scale="0.8" />

Aynı anda yeterli nanit mevcutsa adımları atlamak veya tüm Tarifleri tek bir tick'te tamamlamak mümkündür, ancak 30.720 nanitlik kesin bir üst sınır vardır.

Aşağıdaki tablo her nanitin kademesini gösterir.
| Kademe | Nanit |
| --- | --- |
| 1 | <ItemLink id="gregtech:gt.metaitem.03:4010" showIcon="left" >Karbon</ItemLink>/<ItemLink id="gregtech:gt.metaitem.03:4811" showIcon="left" >Parlak taş</ItemLink> |
| 2 | <ItemLink id="gregtech:gt.metaitem.03:4054" showIcon="left" >Gümüş</ItemLink>/<ItemLink id="gregtech:gt.metaitem.03:4129" showIcon="left" >Nötronyum</ItemLink> |
| 3 | <ItemLink id="gregtech:gt.metaitem.03:4086" showIcon="left" >Altın</ItemLink> |
| 4 | <ItemLink id="gregtech:gt.metaitem.03:4581" showIcon="left" >Aşkın Metal</ItemLink> |
| 5 | <ItemLink id="gregtech:gt.metaitem.03:4147" showIcon="left" >Altı Fazlı Bakır</ItemLink> |
| 6 | <ItemLink id="gregtech:gt.metaitem.03:4585" showIcon="left" >Beyaz Cüce Maddesi</ItemLink> |
| 7 | <ItemLink id="gregtech:gt.metaitem.03:4586" showIcon="left" >Kara Cüce Maddesi</ItemLink> |
| 8 | <ItemLink id="gregtech:gt.metaitem.03:4139" showIcon="left" >Universium</ItemLink> |
| 9 | <ItemLink id="gregtech:gt.metaitem.03:4141" showIcon="left" >Eternity</ItemLink> |
| 10 | <ItemLink id="gregtech:gt.metaitem.03:4143" showIcon="left" >Magmadde</ItemLink> |
{: widths="30" width="220"}

### Tarifler

Her adım için gereken nanitli Tarifleri [BEC Hattı Rehberi - Tarifler](./bose_einstein_condensate_line.md#recipes) bölümünde kontrol edebilirsin.

## Kaynaklar
- [GTNH Wiki : Bose-Einstein Condensate Observation Array](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Observation_Array)