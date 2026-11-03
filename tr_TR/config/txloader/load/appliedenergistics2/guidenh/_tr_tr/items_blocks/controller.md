---
navigation:
  parent: /items_blocks_index.md
  title: ME Kontrolcü
  icon: appliedenergistics2:tile.BlockController
categories:
- ağ altyapısı
item_ids:
- appliedenergistics2:tile.BlockController
- appliedenergistics2:tile.BlockCreativeEnergyController
---

# Kontrolcü

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockController" meta="1" nbt='{inv:{},proxy:{p:0,g:6L,k:-1L},orientation_up:"UP",id:"BlockController",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />
  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyController" meta="1" nbt='{inv:{},proxy:{p:0,g:11L,k:-1L},orientation_up:"UP",id:"BlockCreativeEnergyController",orientation_forward:"EAST",internalCurrentPower:"9.22337203685477E14d"}' scale="4" />
</Row>

Kontrolcü, bir [ME ağı](../ae2_mechanics/me_network_connections.md) için yönlendirme merkezidir. O olmadan ağ geçicidir ve en fazla sekiz kanal kullanan [cihazı](../ae2_mechanics/devices.md) destekler. Bir ağ birden fazla kontrolcü grubu içeremez. Her kontrolcü yüzü 32 [kanal](../ae2_mechanics/channels.md) sağlar.

Her kontrolcü bloğu 6 AE/t tüketir ve 8000 AE depolar; bu nedenle büyük ağlar ek enerji depolamasına ihtiyaç duyabilir. Bkz. [Enerji](../ae2_mechanics/energy.md).

Kontrolcüler bu kurallar dahilinde serbest biçimli multibloklardır:

1. Bir ağdaki tüm kontrolcü blokları bağlı olmalıdır.
2. Kontrolcü 7x7x7 blok içine sığmalıdır.
3. Kontrolcü blokları en fazla bir eksen boyunca bitişik olabilir; bunun ihlali kontrolcüyü devre dışı bırakır.

<GameScene width="400" height="200" zoom="2" showBackground={false}>
  <ImportStructure src="../assets/structures/controllers.snbt" />
  <IsometricCamera yaw="195" pitch="25" />
</GameScene>

Enerji verildiğinde ve geçerli olduğunda kontrolcü parlar ve renkler arasında geçiş yapar. Sağ tıklandığında, bir <ItemLink id="appliedenergistics2:item.ToolNetworkTool" /> ile aynı GUI'yi açar.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockController" />

