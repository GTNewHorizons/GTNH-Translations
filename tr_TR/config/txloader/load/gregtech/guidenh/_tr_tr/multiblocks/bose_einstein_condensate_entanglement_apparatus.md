---
item_ids:
  - gregtech:gt.blockmachines:15754
quest_ids:
  - So7OhYd8SVO3_Jl370cogA==
navigation:
  title: Bose-Einstein Yoğuşması Dolanıklık Aparatı
  parent: ./bose_einstein_condensate_line.md
  icon: gregtech:gt.blockmachines:15754
  position: -11001
---
# Bose-Einstein Yoğuşması Dolanıklık Aparatı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15754" />
</GameScene>

<ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left" />, [BEC Hattı](./bose_einstein_condensate_line.md) içinde sıvıları dolanık yoğuşmaya dönüştüren UIV kademe bir Multibloktur--bir Girdi Kapağı'na benzer. 

Dolanıklık Aparatı hız aşırtma yapmaz, ancak sağlanan güç miktarına göre mümkün olduğunca fazla işlem yapabilmek için sınırsız paralele sahiptir.  
Ciddi işlem hacmi için çok amperli ve lazer enerji kapakları desteklenir ve Dolanıklık Aparatı farklı sıvıları aynı anda dolanıklaştırabilir, ancak işlem süresi her zaman etkin tariflerin en uzun süresi olacaktır.  
Tariflerdeki EU kotası, her ek paralel için gereken EU/t'dir; ancak paralel başına gerçekte tüketilen EU/t bu değerin yalnızca %5'idir.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | UIV |
| Yapı Boyutu (UxGxY) | 34x19x19 |
| Güç | Her Enerji Kapağı kullanılabilir, Çok Amperli ve Lazer Kapakları dahil |
| Hız Aşırtma | Yok |
| Bakım | Bakım gerekmez |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa
### Üretim
<RecipesFor id="gregtech:gt.blockmachines:15754" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:3" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:2" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:4" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:1" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockglass1:9" handlerBlacklist="gt.recipe.researchStation" />

<RecipesFor id="gregtech:gt.blockcasings.bec:5" handlerBlacklist="gt.recipe.researchStation" />

### Yapı

Dolanıklık Aparatı'nın kademeli bileşenleri yoktur. 

Dolanıklık Aparatı döndürülebilir veya çevrilebilir.

Ciddi işlem hacmi için çok amperli ve lazer enerji kapakları desteklenir. 

Yapıyı görselleştirmek/inşa etmek için <ItemLink id="structurelib:item.structurelib.constructableTrigger" showIcon="left" /> kullan.

| Bileşen | Miktar ve yerleşim |
| --- | --- |
| <ItemLink id="gregtech:gt.blockmachines:15754" showIcon="left" /> | 1, Ön orta, 10. katman |
| <ItemLink id="gregtech:gt.blockcasings.bec:3" showIcon="left" /> | 236 |
| <ItemLink id="gregtech:gt.blockcasings.bec:2" showIcon="left" /> | 232 |
| <ItemLink id="gregtech:gt.blockcasings.bec" showIcon="left" /> | 216 |
| <ItemLink id="gregtech:gt.blockcasings.bec:4" showIcon="left" /> | 184 |
| <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> | 136-158 |
| <ItemLink id="gregtech:gt.blockglass1:9" showIcon="left" /> | 148 |
| <ItemLink id="gregtech:gt.blockcasings.bec:5" showIcon="left" /> | 101 |
| <ItemImage id="gregtech:gt.blockmachines:41" noTooltip /><Tooltip label="Energy Hatch">Enerji Kapağı Etiketi: Normal, Çok Amperli, Lazer kullanılabilir</Tooltip> | 1+, Kontrolcü çevresindeki herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemImage id="gregtech:gt.blockmachines:51" noTooltip />Girdi Kapağı | 1+, Kontrolcü çevresindeki herhangi bir <ItemLink id="gregtech:gt.blockcasings.bec:1" showIcon="left" /> yerine geçebilir |
| <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> | 1, Arka orta |

### Duvar Paylaşımı

Dolanıklık Aparatı birkaç blok tasarrufu için her bir kenarını duvar paylaşımına açabilir; ancak sınırsız paralel ile işlemesini süresiz ölçekleyebilme yeteneği ve aynı anda birden fazla tarif çalıştırabilme yeteneği sayesinde genellikle birden fazla inşa edilmez.

## Kullanım

Dolanıklık Aparatı veya BEC Jeneratörü, [BEC Hattı](./bose_einstein_condensate_line.md) içindeki ilk adımdır ve güç harcayarak sıvıları dolanık yoğuşmaya dönüştürür. Dolanıklık Aparatı hız aşırtma yapmaz, ancak sağlanan güç miktarına göre mümkün olduğunca fazla işlem yapabilmek için sınırsız paralele sahiptir.

Sıvıyı yapının önündeki bir Girdi Kapağı aracılığıyla aktar.  
Dolanıklık Aparatı farklı sıvıları aynı anda dolanıklaştırabilir, ancak işlem süresi her zaman etkin tariflerin en uzun süresi olacaktır.  
Örneğin, eriyik nötronyum (20 tick) ve eriyik uzayzaman (60 tick) aynı anda mevcutsa ve ikisini de desteklemeye yetecek güç varsa işlem süresi 60 tick olur, çünkü bu ikisinin en uzunudur. İkisini de desteklemeye yetecek güç yoksa öncelik, renkli kapaklar, konum vb. ile Standart Multiblok sırasını izler.

Dolanık yoğuşma, yapının arkasındaki <ItemLink id="gregtech:gt.blockmachines:15476" showIcon="left" /> aracılığıyla çıkar ve [<ItemLink id="gregtech:gt.blockmachines:15755" showIcon="left">Muhafaza Alanları</ItemLink>](./bose_einstein_condensate_containment_field.md) içinde depolanır; ta ki [<ItemLink id="gregtech:gt.blockmachines:15756" showIcon="left">Gözlem Dizisi</ItemLink>](./bose_einstein_condensate_observation_array.md) onu tarifler için [<ItemLink id="gregtech:gt.blockmachines:15757" showIcon="left">IO Düğümleri</ItemLink>](./bose_einstein_condensate_teleportation_node.md) içine çekene kadar. Ancak asıl zorluk, Dolanıklık Aparatı'nın işlemeye başlamadan önce yoğuşma için yeterli boş alan olup olmadığını kontrol etmemesidir. Dikkatli olunmazsa istemeden ağın depolamasını taşırıp yoğuşmayı hiçliğe gönderebilir. Çözüm, seviyeler çok yükselirse Dolanıklık Aparatı'nı geçici olarak devre dışı bırakmak için Muhafaza Alanı üzerinde bir <ItemLink id="gregtech:gt.blockmachines:15761" showIcon="left" /> kullanmak ya da OpenComputers ile Muhafaza Alanı'nın alan gücünü dinamik olarak ayarlamaktır.

Aynı ağda birden fazla Muhafaza Alanı varsa Dolanıklık Aparatı'ndan gelen yoğuşma, toplam alan güçlerine orantılı olarak bölünür. Örneğin, bir Muhafaza Alanı 150.000 alan gücüne, diğeri 50.000 alan gücüne sahipse ilki yoğuşmanın %75'ini, ikincisi ise yoğuşmanın yalnızca %25'ini alır.

### Tarifler

Her tarif tek bir girdi sıvısı, dolanıklık için bir EU kotası ve sabit bir süreden oluşur.  
Kota, paralel başına gereken EU/t'dir; ancak paralel başına gerçekte tüketilen EU/t bu değerin yalnızca %5'idir.  
Örneğin nötronyumun kotası 7.864.320 EU'dur; bu, işlem hacmindeki her 7.864.320 EU/t'nin ek bir paralel kazandırdığı, ancak her birinin yalnızca 393.216 EU/t tükettiği anlamına gelir.  
Süreler, pasif yoğuşma üretimini teşvik etmek ve daha sonra bir [<ItemLink id="gregtech:gt.blockmachines:15760" showIcon="left">Maxwell Geçidi</ItemLink>](./bose_einstein_condensate_maxwell_gate.md) ile doğru olanları filtrelemek için çok uzundur.

| Dolanık Yoğuşma | Paralel Başına | Süre | Güç |||
| --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | ^^ | Paralel Başına Gerekli || Paralel Başına Tüketilen |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:941" showIcon="left">Nötronyum</ItemLink> | 144 L | 30 sn | 7.864.320 EU/t | 1A UEV | 393.216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:942" showIcon="left">Kozmik Nötronyum</ItemLink> | 144 L | 30 sn | 7.864.320 EU/t | 1A UEV | 393.216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:943" showIcon="left">Katmankayamsı</ItemLink> | 144 L | 30 sn | 7.864.320 EU/t | 1A UEV | 393.216 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:944" showIcon="left">Kromatik Cam</ItemLink> | 144 L | 30 sn | 31.457.280 EU/t | 1A UIV | 1.572.864 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:945" showIcon="left">Göksel Tungsten</ItemLink> | 144 L | 30 sn | 31.457.280 EU/t | 1A UIV | 1.572.864 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:946" showIcon="left">Sonsuzluk</ItemLink> | 144 L | 30 sn | 125.829.120 EU/t | 1A UMV | 6.291.456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:949" showIcon="left">Boyutsal Olarak Kaydırılmış Süperakışkan</ItemLink> | 1.000 L | 60 sn | 125.829.120 EU/t | 1A UMV | 6.291.456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:950" showIcon="left">Kayıpsız Fonon Transfer Ortası</ItemLink> | 1.000 L | 90 sn | 125.829.120 EU/t | 1A UMV | 6.291.456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:951" showIcon="left">Dejenere Kuark Gluon Plazma</ItemLink> | 1.000 L | 120 sn | 125.829.120 EU/t | 1A UMV | 6.291.456 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:947" showIcon="left">Hipojen</ItemLink> | 144 L | 60 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:948" showIcon="left">Aşkın Metal</ItemLink> | 144 L | 60 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:952" showIcon="left">Uzayzaman</ItemLink> | 144 L | 120 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:953" showIcon="left">Takyon Zengin Zamansal Sıvı</ItemLink> | 144 L | 120 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:954" showIcon="left">Uzamsal Olarak Genişletilmiş Sıvı</ItemLink> | 144 L | 120 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:955" showIcon="left">Sınırsız Kozmik Lehim</ItemLink> | 1.000 L | 120 sn | 503.316.480 EU/t | 1A UXV | 25.165.824 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:956" showIcon="left">MHDCSM</ItemLink> | 144 L | 180 sn | 2.013.265.920 EU/t | 1A MAX | 100.663.296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:957" showIcon="left">Magmadde</ItemLink> | 144 L | 180 sn | 2.013.265.920 EU/t | 1A MAX | 100.663.296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:958" showIcon="left">Universium</ItemLink> | 144 L | 180 sn | 2.013.265.920 EU/t | 1A MAX | 100.663.296 EU/t |
| <ItemLink id="NotEnoughItems:neiFluidDisplay:959" showIcon="left">Ebediyet</ItemLink> | 144 L | 180 sn | 2.013.265.920 EU/t | 1A MAX | 100.663.296 EU/t |
{: widths="220,60,60, 120, 40, 120"}


## Kaynaklar
- [GTNH Wiki : Bose-Einstein Condensate Entanglement Apparatus](https://wiki.gtnewhorizons.com/wiki/Bose-Einstein_Condensate_Entanglement_Apparatus)