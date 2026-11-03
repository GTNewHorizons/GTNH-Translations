---
navigation:
  parent: /items_blocks_index.md
  title: ME Yok Etme Düzlemi
  icon: appliedenergistics2:item.ItemMultiPart:300
categories:
- devices
item_ids:
- appliedenergistics2:item.ItemMultiPart:300
- appliedenergistics2:item.ItemMultiPart:301
---

# ME Yok Etme Düzlemi

<GameScene zoom="8" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/annihilation_plane.snbt" />
</GameScene>

Yok Etme Düzlemi blokları kırabilir ve eşyaları toplayabilir. Eşyaları [ağ depolamasına](../ae2_mechanics/import_export_storage.md) yerleştirir ve bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> gibi çalışır. Normal koşullarda bir bloğu kırdıktan sonra hedef konumun yakınındaki eşyaları aktif olarak toplar. Doğrudan düzlemle çarpışan eşyalar için yalnızca düzlemin yüzeyindeki çarpışma menzili içindeki eşyaları toplar.

Yok Etme Düzlemi yalnızca belirli koşulları karşılayan blokları kırabilir. Örneğin havayı, sıvıları, ana kayayı, uç portallarını, uç portalı çerçevelerini veya komut bloklarını kıramaz. Bloğun ayrıca negatif olmayan bir sertliğe sahip olması ve kazma izni kontrolünden geçmesi gerekir.

Bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> ile bu büyüyle büyülenmiş aletler aynı şekilde davranır, ancak enerji maliyeti Yok Etme Düzlemininkinin 16 katıdır.

Yok Etme Düzlemi bir [kablo alt parçasıdır](../ae2_mechanics/cables_subparts.md).

**CHUNK TALEBİNDE SAHTE OYUNCULARI ETKİNLEŞTİRMEYİ UNUTMA**

## Filtreleme

Yok Etme Düzlemi bir bloğu yalnızca bloğun düşen eşyaları ağında depolanabiliyorsa kırar veya bir eşyayı yalnızca ağında depolanabiliyorsa toplar. Bu, birini filtrelemek için *ağında nelerin depolanabileceğini kısıtlaman gerektiği* anlamına gelir; büyük olasılıkla onu bir [alt ağa](../ae2_mechanics/subnetworks.md) koyarak. Bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> veya [hücreleri](storage_cells.md) [bölümlemek](cell_workbench.md) bunu başarabilir.

<GameScene width="300" height="200" zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
    Hedef bloktan düşen eşyaları filtrele.
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
    Düşen eşyalar için depolamayı bölümle.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Yok Etme Düzlemi *eşya düşüşlerine göre* filtreleme yapar. Bu nedenle yalnızca <ItemLink id="etfuturum:amethyst_cluster_2:6" /> kırmak istiyorsan düzlem İpeksi Dokunuş ile büyülenmelidir. Tam büyümemiş ametist tomurcukları hiçbir şey düşürmez ve ağ her zaman "hiçbir şeyi" depolayabilir, bu yüzden normal bir Yok Etme Düzlemi onları kırmaya devam eder.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:300" />