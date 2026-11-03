---
navigation:
  parent: /items_blocks_index.md
  title: Terminaller
  icon: appliedenergistics2:item.ItemMultiPart:380
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:380
- appliedenergistics2:item.ItemMultiPart:370
- appliedenergistics2:item.ItemMultiPart:360
- appliedenergistics2:item.ItemMultiPart:340
- appliedenergistics2:item.ItemMultiPart:500
- appliedenergistics2:item.ItemMultiPart:480
- ae2fc:part_level_terminal
- thaumicenergistics:part.base:4632:5
---

# Terminaller

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/terminals.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="appliedenergistics2:tile.BlockInterface" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> vb. bir AE2 ağının dünyayla etkileşim kurmasının birincil yöntemleriyken, Terminaller bir AE2 ağının *seninle* etkileşim kurmasının birincil yöntemidir. Farklı işlevlere sahip birkaç varyantı vardır.

Terminaller, üzerlerine monte edildikleri [Kablolar](cables.md)ın rengini alır.

Bunlar [Kabloların alt parçalarıdır](../ae2_mechanics/cables_subparts.md).

## Terminal Yerleştirme

Bir terminal genellikle birinin yerleştirebileceği ilk [Kabloların alt parçası](../ae2_mechanics/cables_subparts.md) olduğundan, yanlış yapıp terminali ters yerleştirmek yaygındır. İşte yapılması ve yapılmaması gerekenlere bir örnek:

<GameScene width="350" height="250" zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/terminal_placement.snbt" />
  <IsometricCamera yaw="195" pitch="30" />

  <LineAnnotation color="#ff3333" from="2.5 .5 .5" to="4.5 2.5 .5" alwaysOnTop={true} thickness="1"/>
  <LineAnnotation color="#ff3333" from="2.5 2.5 .5" to="4.5 .5 .5" alwaysOnTop={true} thickness="1"/>

  <LineAnnotation color="#33ff33" from="-.5 2.5 .5" to="1 .5 .5" alwaysOnTop={true} thickness="1"/>
  <LineAnnotation color="#33ff33" from="1 .5 .5" to="1.5 1 .5" alwaysOnTop={true} thickness="1"/>
</GameScene>

Hâlâ bir terminal ve bir enerji alıcısı var; ancak artık terminal doğru yönde ve gerçekten ağa bağlı, üstelik hepsi daha küçük bir alana sığıyor.

<a name="terminal-ui"></a>

# Terminal Araması

Arama kutusu Regex ifadelerini kabul eder, yani örneğin Gregtech'teki tüm cevherleri bulmak için "gtceu:.*ore" yazabilirsin. Regex öğrenmek okuyucuya bir alıştırma olarak bırakılmıştır.

# Terminal

<ItemImage id="appliedenergistics2:item.ItemMultiPart:380" scale="4" />

Temel terminalin; [ağının depolamasının](../ae2_mechanics/import_export_storage.md) içeriğini görüntülemene ve erişmene, ayrıca [otomatik üretim](../ae2_mechanics/autocrafting.md) düzeninden bir şeyler talep etmene olanak tanır.

## Arayüz

Temel bir terminalin arayüzünde birkaç bölüm vardır.

Orta bölüm, ağının depolamasına erişim sağlar. Bir şeyler koyabilir ve çıkarabilirsin. Birkaç fare/tuş kısayolu vardır:

*   Sol tık bir küme alır, sağ tık yarım küme alır.
*   Bir eşya, sıvı vb. [otomatik üretilebiliyorsa](../ae2_mechanics/autocrafting.md), "pick block" tuşuna (genellikle orta tık) atadığın şey, üretilecek miktarı belirlemek için bir arayüz açar. Ayrıca `3*64/2` gibi formüller girebilir veya depolamanda 32'ye ulaşmak için gereken sayıda eşya üretmek üzere `=32` yazabilirsin.
*   Shift'e basılı tutmak, görüntülenen eşyaları yerinde dondurur; miktarlar değiştiğinde veya sisteme yeni eşyalar girdiğinde yeniden düzenlenmelerini engeller.
*   Bir kova veya başka bir sıvı kabıyla sağ tıklamak sıvıyı bırakır, terminaldeki bir sıvıya boş bir sıvı kabıyla sol tıklamak sıvıyı çeker.

Sol bölümde şunlar için ayar düğmeleri vardır:

*   Ada, moda ve miktar gibi farklı özniteliklere göre sırala
*   Depolananları, üretilebilirleri veya her ikisini görüntüle
*   Eşyaları, sıvıları veya her ikisini görüntüle
*   Sıralama düzenini değiştir
*   Ayrıntılı terminal ayarları penceresini aç
*   Terminal arayüzünün yüksekliğini değiştir

Sağ tarafta <ItemLink id="appliedenergistics2:item.ItemViewCell" /> için yuvalar vardır.

Orta bölümün sağ üst köşesi (çekiç düğmesi), [otomatik üretim](../ae2_mechanics/autocrafting.md) durum arayüzünü açar; böylece otomatik üretimlerinin ilerlemesini ve her bir [Üretim CPU'sunun](crafting_cpu.md) ne yaptığını görebilirsin.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:380" />

<a name="crafting-terminal-ui"></a>

# Üretim Terminali

<ItemImage id="appliedenergistics2:item.ItemMultiPart:360" scale="4" />

Üretim Terminali normal bir terminale benzer; tüm ayarları ve bölümleri aynıdır, ancak [ağ depolamasından](../ae2_mechanics/import_export_storage.md) otomatik olarak yenilenecek bir üretim ızgarası eklenmiştir. Çıktıya shift tıklarken dikkatli ol!

Terminalini en kısa sürede bir üretim terminaline yükseltmelisin.

## Arayüz

Üretim terminali, normal terminalle aynı arayüze sahiptir, ancak ortasına bir üretim ızgarası eklenmiştir.

Üretim ızgarasını ağ depolamasına veya envanterine boşaltmak için 2 ek düğme vardır.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:360" />

<a name="pattern-encoding-terminal-ui"></a>

# Kalıp Kodlama Terminali

<ItemImage id="appliedenergistics2:item.ItemMultiPart:340" scale="4" />

Kalıp Kodlama Terminali normal bir terminale benzer; tüm ayarları ve bölümleri aynıdır, ancak ek bir [kalıp](patterns.md) kodlama arayüzü vardır. Üretim terminalinin arayüzüne benzer, ancak bu üretim ızgarası gerçekte üretim yapmaz.

Bir üretim terminaline ek olarak bunlardan birine sahip olmalısın.

## Arayüz

Üretim terminali, normal terminalle aynı arayüze sahiptir, ancak ek bir [kalıp](patterns.md) kodlama arayüzü vardır.

Kalıp kodlama arayüzünde birkaç bölüm vardır:

<ItemLink id="appliedenergistics2:item.ItemMultiMaterial:52" /> eklemek için bir yuva.

Kalıbı kodlamak için büyük bir ok.

Kodlanmış kalıplar için bir yuva. Düzenlemek için önceden kodlanmış bir kalıbı bu yuvaya yerleştir, ardından "kodla" okuna tıkla.

Kodlanacak kalıp tipini şunlar arasında değiştirmek için sağda 2 sekme

*   Üretim
*   İşleme

Orta arayüz, kodlanacak kalıbın tipine göre değişir:

*   Üretim modunda:
    *   Tarifi oluşturmak için malzemelere sol tıkla veya NEI'den sürükle. Malzemeyi kaldırmak için sağ tıkla.
    *   Muadilleri etkinleştirmek, herhangi bir tahta tipinden çubuk üretmek gibi şeylere olanak tanır. Bu yalnızca kesinlikle gerekli olduğunda kullanılmalıdır.
    *   Sıvı muadilleri, sıvı dolu kovalar yerine depolanmış sıvıları kullanmaya olanak tanır.
    *   Ayrıca doğrudan NEI tarif ekranından bir kalıp kodlayabilirsin.

*   İşleme modunda:
    *   Tarifin girdilerini ve çıktılarını belirtmek için malzemelere sol tıkla veya sağ tıkla ya da NEI'den sürükle.
    *   Bir sıvıyı kova veya tank eşyası yerine malzeme olarak ayarlamak için bir sıvı kabıyla (kova veya sıvı tankı gibi) sağ tıkla.
    *   Bir küme tutarken sol tık tüm kümeyi yerleştirir, sağ tık bir eşya yerleştirir. Mevcut bir malzeme kümesine sol tıklamak tüm kümeyi kaldırır, sağ tık ise kümeyi 1 azaltır. "pick block" tuşuna (genellikle orta tık) atadığın şey, eşyanın veya sıvının kesin miktarını belirlemeni sağlar.
    *   Çıktı yuvalarında birincil bir çıktı ve otomatik üretim algoritmasının bilmesini isteyebileceğin tüm ikincil çıktılar için yer vardır.
    *   Hem girdi hem de çıktı yuvaları kaydırılabilir, böylece 81 farklı malzeme ve 26 ikincil çıktıya sahip olabilirsin
    *   Ayrıca doğrudan NEI tarif ekranından bir kalıp kodlayabilirsin.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:340" />

<a name="pattern-access-terminal-ui"></a>

# ME Arayüz Terminali

<ItemImage id="appliedenergistics2:item.ItemMultiPart:480" scale="4" />

ME Arayüz Terminali belirli bir sorunu çözer: <ItemLink id="appliedenergistics2:tile.BlockInterface" /> ve <ItemLink id="appliedenergistics2:tile.BlockMolecularAssembler" />'den oluşan yoğun bir kulede, yeni kalıplar eklemek için bir arayüze fiziksel olarak erişemezsin. Ayrıca bir [kalıp](patterns.md) eklemek için üssünün içinde yürümekten kurtarır. ME Arayüz Terminali, ağdaki her ME Arayüzüne erişim sağlar.

## Arayüz

Bu terminal, diğer tüm terminallerden farklı bir arayüze sahiptir.

Terminal yüksekliği ve hangi ME Arayüzlerinin gösterileceğine dair ayarları vardır.

Terminaldeki her satır belirli bir ME Arayüzüne karşılık gelir.

Terminaldeki ME Arayüzleri, bağlı oldukları bloklara göre veya bir örs ile ya da bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:21" /> ile onlara verdiğin ada göre sıralanır.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:480" />