---
navigation:
  title: Işın Hattı
  parent: ./multiblocks_index.md
  icon: gtnhlanth:particle:5
  position: -7001
---
# Işın Hattı
<GameScene interactive={true} wrap="square" align="right" width="220" height="200">
  <ImportStructure src="/assets/structures/beamline.snbt" />
</GameScene>

**Işın Hattı**, yonga plakalarını bir foton ışını ve ultra hassas maskelerle kazıyan, birbirine zincirlenmiş dört ZPM kademe multibloktan oluşan bir sistemdir.

Hat, yedi farklı kaynak malzemeden birini kullanarak parçacık ışını üreten [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) ile başlar.  
Ardından [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">Lineer Hızlandırıcı (LINAC)</ItemLink>](./linear_accelerator.md) parçacık ışınını hızlandırarak odak kaybı karşılığında toplam enerjisini artırır.  
[<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md) parçacık ışınını daha da hızlandırır ve sonunda yüksek hızlı parçacıkların radyasyonundan bir foton ışını üretir.  
[<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md) foton ışınını yakalar ve yonga plakalarının üzerine dikkatlice odaklayarak onları kazır. 

Her multiblok kendi gücünü gerektirir, ancak bunun çoğu nihai tarifin işleme hızını artırmak için Sinkrotron'da toplanmalıdır. Diğer tek girdi, LINAC ve Sinkrotron için soğutucudur; ikisi de onu tamamen sıcak soğutucuya geri dönüştürür.

Işın Hattı, yonga plakası kazımak için alternatif bir yöntem olabilir. [<ItemLink id="gregtech:gt.blockmachines:3004" showIcon="left">Aşırı Yoğunluklu Lazer Kazıyıcı (HILE)</ItemLink>](./hyper_intensity_laser_engraver.md) ile karşılaştırıldığında Işın Hattı, inşa edildiği andan itibaren Çok Amperli/Lazer Kapakları kullanarak ciddi hız aşırtma yapma (HILE bunu UEV+ üzerinde yapabilir) ve [<ItemLink id="gregtech:gt.blockmachines:1169" showIcon="left">Büyük Kimyasal Reaktör (BKR)</ItemLink>](./large_chemical_reactor.md) gibi ara işlemlere olan ihtiyacı ortadan kaldırma gibi avantajlar sunar; ancak inşa etmek için çok miktarda malzeme gerektirir ve tüm yonga plakalarını üretmek için toplam **5** farklı Işın Hattı multibloku inşa edilmelidir. Ayrıca BKR'yi atlayarak indiyum ve Güneştaşı tasarrufu sağlasa da bunun yerine malzeme olarak boraks ve lantan kullanır.

| Özellik | Ayrıntılar |
| --- | --- |
| Kilit Açma Kademesi | ZPM |
| Yapı Boyutu (UxGxY) | Değişir |
| Güç | Değişir |
| Hız Aşırtma | Değişir |
| Bakım | Bakım Gerekli |
| Kirlilik | Kirlilik üretmez |

## Üretim ve İnşa

Işın Hattı multibloklarının nasıl üretileceğini ve inşa edileceğini görmek için her multiblokun belgelerine bakabilirsin.
- [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md)
- [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left" />](./linear_accelerator.md)
- [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md)
- [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)

### Üretim

Işın Hattı, farklı Işın Hattı multiblokları arasında bağlantı kurmak için <ItemLink id="gregtech:gt.blockmachines:10503" showIcon="left" />, <ItemLink id="gregtech:gt.blockmachines:10504" showIcon="left" /> ve <ItemLink id="gregtech:gt.blockmachines:10502" showIcon="left" /> gerektirir.

<RecipesFor id="gregtech:gt.blockmachines:10503" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gregtech:gt.blockmachines:10504" handlerBlacklist="gt.recipe.scanner" />

<RecipesFor id="gregtech:gt.blockmachines:10502" handlerBlacklist="bq_quest" />

### Yapı
Işın Hattı'nın çalışması için 4 multibloku sırayla <ItemLink id="gregtech:gt.blockmachines:10502" showIcon="left" /> kullanarak bağla. Boruların renklendirilmesi gerekmez ancak kesişemez veya bükülemez.

1. [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left" />](./linear_accelerator.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md)
1. [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)

> [!WARNING]
> TÜM Işın Hattı multiblokları çalışmak için <ItemLink id="bartworks:BW_TieredGlass:3" showIcon="left">LuV+ Kademe Cam Blok</ItemLink> gerektirir.

İsteğe bağlı olarak, parçacık ışınını gerektiği gibi yönlendirmek veya optimize etmek için UV+ üzerinde [<ItemLink id="gregtech:gt.blockmachines:3016" showIcon="left" />](./beam_mirror.md), [<ItemLink id="gregtech:gt.blockmachines:3017" showIcon="left" />](./beam_splitter.md) ve/veya [<ItemLink id="gregtech:gt.blockmachines:3018" showIcon="left" />](./beam_stabilizer.md) kullanabilirsin. Bunlar aslında yalnızca [<ItemLink id="gregtech:gt.blockmachines:3013" showIcon="left" />](./large_hadron_collider.md) için yardımcı olur ancak Işın Hattı ile de tamamen uyumludurlar.

## Kullanım

### Tarifler

<RecipeUsage id="gregtech:gt.blockmachines:10508" handlerId="gtnhlanth.recipe.tc" wrap="square" align="right" />

NEI'deki Işın Hattı (daha doğrusu [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md)) tariflerinde girdi olarak yalnızca bir foton, bir maske ve katkılı yonga plakaları, çıktı olarak da kazınmış yonga plakaları bulunur. Ancak foton semboliktir ve tarif için gerçek bir eşya ya da girdi değildir. Yalnızca nihai parçacık ışınının elektron ışını ya da başka bir şey değil, özellikle foton ışını olması gerektiğini belirtmek için oradadır. 

Ayrıca tarifin altında parçacık ışınının özelliklerine ilişkin birkaç ek gereksinim listelenmiştir. Enerji belirli bir aralıkta olmalı, odak belirli bir değere eşit veya ondan büyük olmalı ve temel miktar ya da oran tarifin işleme hızını belirler.

Tarifi işlemek için Işın Hattı multibloklarını tarifin gerektirdiği koşulları karşılayacak şekilde yönetmelisin.

#### İş Akışı
Işın Hattı tariflerini işlemenin genel iş akışı aşağıda listelenmiştir ve izleyen alt bölümlerde her bir multiblok hakkında çok daha ayrıntılı olarak açıklanmıştır. 

1. [<ItemLink id="gregtech:gt.blockmachines:10506" showIcon="left" />](./source_chamber.md) parçacık ışınının başlangıç değerlerini girdiye ya da kaynak malzemeye ve makinenin gerilimine göre belirler. Her malzemenin oluşturabileceği parçacıklar hakkında daha fazla ayrıntı için makinenin kılavuzuna bak.  
  &b✓ Enerji  &b✓ Odak  &b✓ Oran
1. [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">Lineer Hızlandırıcı (LINAC)</ItemLink>](./linear_accelerator.md) parçacık ışınını hızlandırarak odak kaybı karşılığında genel enerjisini artırır.  
  Etkiyi güçlendirmek ve daha yüksek enerji seviyelerine ulaşmak için LINAC'ın uzunluğunu artır ya da ona daha fazla güç ver.  
  İşlem sırasında odağı mümkün olduğunca korumak için soğutma sıvıları sağla. Soğutma sıvısı ısınmış halde geri döner ve uygun işlemden sonra geri dönüştürülebilir.  
  &a↑ Enerji  &c↓ Odak  &7→ Oran
1. [<ItemLink id="gregtech:gt.blockmachines:10507" showIcon="left" />](./synchrotron.md) parçacık ışınını tekrar hızlandırır ve sonunda yüksek hızlı parçacıkların radyasyonundan bir foton ışını üretir.  
  Işın enerjisini yüksek tutmak ve ışın oranını daha verimli artırmak için anten kasalarını yükselt.  
  İşlem sırasında odağı tekrar mümkün olduğunca korumak için soğutma sıvıları sağla. Soğutma sıvısı ısınmış halde geri döner ve uygun işlemden sonra geri dönüştürülebilir.  
  Güç kaynağını artırmak, ışının enerjisini ve odağını azaltmadan oranını artırır; bu da Işın Hattı'nın yalnızca Sinkrotron'un Enerji Kapaklarının kademesini ve verimini artırarak kolayca yükseltilebilmesini sağlar.  
  Sinkrotron'un enerji kapaklarını yükseltmek, tarif işleme sürelerini belirleyen ışın oranını artırmanın tek yoludur.  
  &c↓ Enerji  &c↓ Odak  &a↑ Oran
1. [<ItemLink id="gregtech:gt.blockmachines:10508" showIcon="left" />](./target_chamber.md) nihai foton ışınını yakalar ve gerçek lazer kazımasını yapar.  
  Hedef Odası, ışın Sinkrotron'dan ayrıldıktan sonra özelliklerinden hiçbirini değiştirmez. Yalnızca ışın enerjisinin ve ışın odağının tarif gereksinimlerini karşıladığını kontrol eder ve tarifin süresini belirlemek için ışın oranını kullanır.

### Üretilebilir Yonga Plakaları
Işın enerjisi, odak ve oran gereksinimlerinin geniş aralığı, tek bir Işın Hattı'nın olası tüm tarifler için yeterli olmadığı anlamına gelir. 

En azından, farklı [<ItemLink id="gregtech:gt.blockmachines:10505" showIcon="left">LINAC</ItemLink>](./linear_accelerator.md) uzunluklarına, enerji kapaklarına ve soğutucuya sahip beş Işın Hattı bulunmalıdır. Aşağıdaki tablo, Işın Hattı'nın işleyebileceği tarifleri gruplara göre listeler.

| Gruba Göre Çıktı || Min Güç | Işın Enerjisi || Min Odak |
| --- | --- | --- | --- | --- | --- |
| ^^ | ^^ | Min | Maks | ^^ |
| 1 | <ItemLink id="gregtech:gt.metaitem.03:32036" showIcon="left" /> | 1,920 EU/t (EV) | 0.5 eV | 4 eV | 35 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32038" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 40 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32060" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 25 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32062" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 30 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32064" showIcon="left" /> | 1,920 EU/t (EV) | 2 eV | 4 eV | 30 |
| 2 | <ItemLink id="gregtech:gt.metaitem.03:32046" showIcon="left" /> | 1,920 EU/t (EV) | 3 eV | 10 eV | 45 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32056" showIcon="left" /> | 1,920 EU/t (EV) | 3 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32054" showIcon="left" /> | 1,920 EU/t (EV) | 5 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32050" showIcon="left" /> | 1,920 EU/t (EV) | 5 eV | 10 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32044" showIcon="left" /> | 1,920 EU/t (EV) | 6 eV | 12 eV | 45 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32040" showIcon="left" /> | 1,920 EU/t (EV) | 7 eV | 12 eV | 40 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32042" showIcon="left" /> | 1,920 EU/t (EV) | 8 eV | 10 eV | 40 |
| 3 | <ItemLink id="gregtech:gt.metaitem.03:32048" showIcon="left" /> | 1,920 EU/t (EV) | 100 eV | 200 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32052" showIcon="left" /> | 1,920 EU/t (EV) | 100 eV | 200 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32058" showIcon="left" /> | 1,920 EU/t (EV) | 190 eV | 200 eV | 50 |
| 4 | <ItemLink id="gregtech:gt.metaitem.01:32714" showIcon="left" /> | 30,720 EU/t (LuV) | 1,000 eV | 3,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32160" showIcon="left" /> | 1,920 EU/t (EV) | 1,000 eV | 4,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32070" showIcon="left" /> | 30,720 EU/t (LuV) | 1,000 eV | 3,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32071" showIcon="left" /> | 30,720 EU/t (LuV) | 2,000 eV | 7,000 eV | 50 |
| 5 | <ItemLink id="gregtech:gt.metaitem.03:32162" showIcon="left" /> | 1,920 EU/t (EV) | 1,500 eV | 10,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32164" showIcon="left" /> | 1,920 EU/t (EV) | 3,200 eV | 9,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32266" showIcon="left" /> | 1,920 EU/t (EV) | 6,000 eV | 14,000 eV | 50 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32068" showIcon="left" /> | 30,720 EU/t (LuV) | 3,000 eV | 9,000 eV | 55 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.01:32668" showIcon="left" /> | 30,720 EU/t (LuV) | 5,000 eV | 12,000 eV | 60 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32071" showIcon="left">Kristal SoC (Ce:LuAG)</ItemLink> | 30,720 EU/t (LuV) | 5,000 eV | 12,000 eV | 60 |
| ^^ | <ItemLink id="gregtech:gt.metaitem.03:32068" showIcon="left">Ham Gelişmiş Kristal Çip (Ce:LuAG)</ItemLink> | 30,720 EU/t (LuV) | 6,000 eV | 14,000 eV | 70 |
{: widths="10, 300, 110, 65, 65, 50"}

Gördüğün gibi - işleme için enerji aralıklarına göre düzenlenmiş 5 grup vardır:
- Grup 1 (2-4 eV)
- Grup 2 (8-10 eV)
- Grup 3 (190-200 eV)
- Grup 4 (2,000-3,000 eV)
- Grup 5 (6,000-9,000 eV)

Işın Hatlarının verimini ölçeklemek için yalnızca Sinkrotron'daki enerji kapaklarını yükselt. Diğer değişkenlerin çoğu özellikle belirli bir enerji aralığında kalmak veya minimum odağın üzerinde olmak üzere tasarlanmıştır.  
Hedef Odasının gerilimi yalnızca bir minimum gereksinimdir ve makinenin çalışması üzerinde hiçbir etkisi yoktur, çünkü ışının oranını değil yalnızca enerjisini artırır.

> [!TIP]
> Fark etmiş olabilirsin, ancak Grup 2'deki <ItemLink id="gregtech:gt.metaitem.03:32046" showIcon="left" /> ve <ItemLink id="gregtech:gt.metaitem.03:32056" showIcon="left" />, Grup 1'in enerjisi 3 eV'den büyükse Grup 1'e de dahil edilebilir! Sadece minimum odak gereksinimlerine dikkat et.

## Kaynaklar
- [GTNH Wiki : Beam Line](https://wiki.gtnewhorizons.com/wiki/Beam_Line)