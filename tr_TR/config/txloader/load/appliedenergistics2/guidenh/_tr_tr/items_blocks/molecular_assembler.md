---
navigation:
  parent: /items_blocks_index.md
  title: Moleküler Montajcı
  icon: appliedenergistics2:tile.BlockMolecularAssembler
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockMolecularAssembler
---

# Moleküler Montajcı

<ItemImage id="appliedenergistics2:tile.BlockMolecularAssembler" scale="8" />

Moleküler montajcı eşya girdilerini alır ve yanındaki bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> tarafından ya da içine yerleştirilen bir <ItemLink id="appliedenergistics2:item.ItemEncodedPattern" />, <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> veya <ItemLink id="appliedenergistics2:item.ItemTunnelPattern" /> tarafından tanımlanan işlemi gerçekleştirir. Sonuçları bitişik envanterlere iter.

Aşağıdaki montajcı “1 meşe kütüğü = 4 meşe tahtası” şablonunu içerir. Üstteki huniye meşe kütükleri ver; üretimi yapacak ve ardından meşe tahtalarını alttaki huniye bırakacaktır.

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Ana Kullanım

Moleküler montajcının ana kullanım alanı bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> yanıdır. Arayüz, ilgili şablonu ve malzemeleri yanındaki montajcılara gönderir. Montajcılar sonuçları otomatik olarak yanlarındaki envanterlere (arayüzün dönüş yuvasına) bıraktığından, üretim şablonlarını otomatikleştirmek için arayüzün yanındaki bir montajcı yeterlidir.

<GameScene zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yükseltmeler

Moleküler montajcı <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:30" /> (hızlandırma kartı) destekler.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockMolecularAssembler" />