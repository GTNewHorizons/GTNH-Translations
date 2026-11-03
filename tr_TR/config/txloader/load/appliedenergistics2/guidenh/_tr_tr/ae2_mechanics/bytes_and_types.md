---
navigation:
  parent: /ae2_mechanics_index.md
  title: Baytlar ve Tipler
  icon: appliedenergistics2:item.ItemExtremeStorageCell.Universe
---

# Baytlar ve Tipler

<Column>
  <Row>
    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />

    <ItemImage id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />
  </Row>
</Column>

[Depolama Hücreleri](../items_blocks/storage_cells.md) hem *bayt* hem de *tip* ile tanımlanır. Baytlar, gerçek bilgisayarındaki gibi, bir depolama hücresindeki toplam "şey" miktarının bir ölçüsüdür. Tipler ise bir hücrede kaç farklı, hani, *tip* şeyin depolandığının ölçüsüdür. Her tip benzersiz bir eşyayı temsil eder; yani 4.096 kırıktaş 1 tiptir, ama farklı büyülere sahip 16 farklı kılıç 16 tiptir.

Her depolama hücresi sabit miktarda veri depolayabilir. Her tip başlangıçta bir miktar bayt tüketir (bu, hücre boyutuna göre değişir) ve her eşya bir bit depolama tüketir; yani sekiz eşya bir bayt, 64'lük dolu bir küme de 8 bayt tüketir; eşyanın bir ME ağı dışında nasıl kümelendiğinden bağımsız olarak. Örneğin, 64 aynı eyer 64 taştan daha fazla yer kaplamaz.

Tekrar edelim, her eşya 1 bittir, yani 8 eşya 1 bayta eşittir. Sıvı hücrelerde bu, bayt başına 2.048 mB'dir.

Birçok kişi bir hücrenin tutabileceği sınırlı tip sayısından şikayet eder, ama bu ***gerekli bir sınırlamadır***.
Hücreler verilerini eşyanın kendi üzerindeki bir NBT etiketinde saklar, bu da onları oldukça dengeli kılar. Ancak bu, bir hücreye çok fazla veri koymanın oyuncuya çok fazla veri gönderilmesine yol açabileceği ve vanilla Minecraft'taki "Book Banning" etkisine benzer bir etki yaratabileceği anlamına gelir.
Ayrıca, sisteminde çok fazla farklı tip olması sıralama ve eşya işleme üzerindeki yükü artırır. Yine de bu sınırlama sonuçta pek kısıtlayıcı olmuyor. Depolama hücrelerini barındıran blokları düşün: hücrelerle dolu tek bir <ItemLink id="appliedenergistics2:tile.BlockDrive" /> yuvası 630 tiptir ki bu, tonlarca benzersiz kümelenemeyen eşya depolamadığın sürece aslında epey fazladır.

Bu nedenle tipler, bir yaratık çiftliğinden gelen yüzlerce rastgele hasarlı zırhı ve aleti doğrudan ME sistemine boşaltmanı "kesinlikle caydırmak" için vardır. Benzersiz hasara ve büyülere sahip her zırh parçası ayrı bir kayıt olarak depolanmak zorundadır, bu da şişmeye neden olur. Bunları sisteme dokunmadan önce eşya akışından filtrelemen önerilir.

Doğrudan en üst kademe depolama hücrelerinin tarifine yönelmek genellikle en iyi fikir değildir, çünkü daha fazla kaynak kullanır ama ekstra tip depolaması vermez. Bu da her hücre boyutunun geç oyunda bile işe yaradığı anlamına gelir, çünkü hepsinin ödünleşimleri vardır.

Aşağıda farklı depolama hücresi kademelerini, ne kadar depoladıklarını ve tarif maliyetlerinin kaba bir tahminini karşılaştıran bir tablo bulunuyor.

## Depolama Hücresi İçerikleri ve Maliyet

| Hücre | Bayt | Tip | Tip Başına Bayt |
| --- | ---: | ---: | ---: |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />        |      1.024 | 63 |       8 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />        |      4.096 | 63 |      32 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />       |     16.384 | 63 |     128 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />       |     65.536 | 63 |     512 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />   |    262.144 | 63 |   2.048 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />  |  1.048.576 | 63 |   8.192 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />  |  4.194.304 | 63 |  32.768 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" /> | 16.777.216 | 63 | 131.072 |

Aşağıda bu hücrelerin tarifleri ve bu tariflerde kullanılan bileşenler yer alıyor:

<Column>
  <Row>
    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:35" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:37" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:57" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:59" />
  </Row>

  <Row>
    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:35" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:37" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:57" handlerId="gt.recipe.circuitassembler" />

    <RecipeFor id="appliedenergistics2:item.ItemMultiMaterial:59" handlerId="gt.recipe.circuitassembler" />
  </Row>
</Column>

## Değişen Tip Sayısıyla Depolama Kapasitesi

Tiplerin başlangıç maliyeti öyle ki, 1 tip tutan bir hücre, 63 tipin tamamının kullanıldığı bir hücrenin 2x katı kadarını tutabilir.

| Hücre | 1 Tip Kullanımdaki Hücrenin Toplam Kapasitesi | 63 Tip Kullanımdaki Hücrenin Toplam Kapasitesi |
| --- | ---: | ---: |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" scale="4" />            |       8.128 |      4.160 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="4" />            |      32.512 |     16.640 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.16k" scale="4" />           |     130.048 |     66.560 |
| <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.64k" scale="4" />           |     520.192 |    266.240 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.256k" scale="4" />       |   2.080.768 |  1.064.960 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.1024k" scale="4" />      |   8.323.072 |  4.259.840 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.4096k" scale="4" />      |  33.292.288 | 17.039.360 |
| <ItemLink id="appliedenergistics2:item.ItemAdvancedStorageCell.16384k" scale="4" />     | 133.169.152 | 68.157.440 |

![1 Tipli Bir Hücre](../assets/images/1_type_cell.png)

![63 Tipli Bir Hücre](../assets/images/63_type_cell.png)