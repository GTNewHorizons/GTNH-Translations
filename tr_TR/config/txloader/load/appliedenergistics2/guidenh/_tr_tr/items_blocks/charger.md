---
navigation:
  parent: /items_blocks_index.md
  title: Şarj Cihazı
  icon: appliedenergistics2:tile.BlockCharger
categories:
- machines
item_ids:
- appliedenergistics2:tile.BlockCharger
---

# Şarj Cihazı

<ItemImage id="appliedenergistics2:tile.BlockCharger" scale="4" />

Şarj Cihazı, desteklediği araçları ve <ItemLink id="gregtech:gt.metaitem.01:8516" /> eşyasını şarj edebilir.

Güç, üst veya alt tarafından verilmelidir. Hem AE2 [kabloları](cables.md) hem de diğer modların enerji kabloları kullanılabilir. Şarj Cihazı hem AE2 enerjisini (AE) hem de Forge Energy (FE) kabul eder. Eşyalar her taraftan yerleştirilip çıkarılabilir. Yalnızca tamamlanmış ürünler çıkarılır, bu yüzden filtreleme gerekmez. <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> otomasyon için cihazı döndürmekte kullanılabilir.

<ItemImage id="gregtech:gt.metaitem.01:8516" /><ItemLink id="gregtech:gt.metaitem.01:8516" /> şarj edilerek <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:1" /> haline getirilebilir veya <ItemLink id="minecraft:compass" showIcon="left"/> bir <ItemLink id="appliedenergistics2:tile.BlockSkyCompass" showIcon="left"/> dönüştürülebilir.

~~Üst veya alt tarafa bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:46" /> yerleştirip el krankıyla sağ tıklamak, eşyaların elle şarj edilmesini sağlar.~~

## Basit Otomasyon

Aşağıda gösterildiği gibi, Şarj Cihazı'nın dönebilme Yeteneği sayesinde şu şekilde yarı otomatik hale getirilebilir:

<GameScene zoom="4" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockCharger" />