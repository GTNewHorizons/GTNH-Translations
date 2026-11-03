---
navigation:
  parent: /items_blocks_index.md
  title: Cepheler
  icon: appliedenergistics2:item.ItemFacade:0:{itemname:"stone",x:[1,0,],modid:"minecraft"}
  position: 110
categories:
- network infrastructure
item_ids:
- appliedenergistics2:item.ItemFacade
---

# Cepheler

Cepheler üssünü daha temiz göstermek için kullanılabilir. Her iki kablo boyutunu da kaplayabilir ve birçok blok türünden yapılabilir.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/facades_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Bir kablonun tüm yüzlerini kaplayabilirler ancak [alt parçaların](../ae2_mechanics/cables_subparts.md) ve kablo bağlantılarının yine de içlerinden dışarı çıkmasına izin verirler.

<GameScene zoom="6"  interactive={true}>
  <ImportStructure src="../assets/structures/facades_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

İyi kullanıldığında üssünün estetiğini iyileştirebilir veya her yüzünde farklı doku olan bloklar inşa etmeni sağlayabilir.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/structures/facades_3.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Cepheleri Gizleme

Elinde <a href="network_tool.md">Ağ Aracı</a> tutarken cepheler gizlenir.

Gizli cephelerin arkasındaki bloklarla, cepheleri önce kaldırmadan etkileşime geçebilirsin.

## Tarif

Dokusunu istediğin bloğu, ortada kalacak şekilde 4 <ItemLink id="appliedenergistics2:item.ItemMultiPart:120" /> ile çevrele.

<RecipeFor id='appliedenergistics2:item.ItemFacade:0:{itemname:"stone",x:[1,0,],modid:"minecraft"}'/>