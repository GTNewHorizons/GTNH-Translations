---
navigation:
  parent: ../tricks_example_index.md
  title: Hücre Boşaltıcı veya Doldurucu
  icon: appliedenergistics2:tile.BlockIOPort
---

# Hücre Boşaltıcı veya Doldurucu

“Bir hücreyi bir sandığa, çekmece dizisine veya sırt çantasına hızlıca nasıl boşaltırım ya da tam tersine aynı yerden nasıl doldururum?” diye sorabilirsin.

Cevap, bir <ItemLink id="appliedenergistics2:tile.BlockIOPort" /> ve eşyaları nereye koyabileceğini veya nereden çekebileceğini kısıtlamak için biraz alt ağ kullanmaktır.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/cell_dumper_filler.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 1">
  (1) İo Bağlantı Noktası: GUI'nin ortasındaki ok düğmesiyle "Verileri Ağa Aktar" veya "Verileri Depolama Hücresine Aktar" olarak ayarlanabilir. 3 hızlandırma kartı vardır.
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0.7 0" max="1 1 1">
  (2) Depolama Veriyolu: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="0 1 0" max="1 2 1">
  Doldurmak veya boşaltmak istediğin şeyi buraya yerleştir.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 0.35 0.35" max="2.3 0.65 0.65">
  Kuvars Lifi: Yalnızca enerji kaynağı başka bir ağsa gerekir.
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 0.5" color="#00ff00">
  Başka bir ağ veya enerji alıcısı gibi bir enerji kaynağına.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockIOPort" /> (1), GUI'nin ortasındaki ok düğmesiyle "Verileri Ağa Aktar" veya "Verileri Depolama Hücresine Aktar" olarak ayarlanabilir. Maksimum hız için 3 hızlandırma kartı vardır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

### "Ağa Aktarma" Modunda

1. <ItemLink id="appliedenergistics2:tile.BlockIOPort" />, yerleştirilen [depolama hücresinin](../items_blocks/storage_cells.md) içeriğini [ağ deposuna](../ae2_mechanics/import_export_storage.md) boşaltmaya çalışır.
2. Alt ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> veriyoludur; önüne koyduğun şeydeki eşyaları, sıvıları vb. depolar.
* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" />, oyun tick'i başına bu kadar çok eşya aktarmanın güç çekişinden ağın tükenmemesi için yeterince büyük bir [enerji](../ae2_mechanics/energy.md) tamponu sağlar.

### "Depolama Hücresine Aktarma" Modunda

1. <ItemLink id="appliedenergistics2:tile.BlockIOPort" />, [ağın deposunun](../ae2_mechanics/import_export_storage.md) içeriğini yerleştirilen [depolama hücresine](../items_blocks/storage_cells.md) boşaltmaya çalışır.
2. Alt ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> veriyoludur; önüne koyduğun şeyden eşyaları, sıvıları vb. çeker.
* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" />, oyun tick'i başına bu kadar çok eşya aktarmanın güç çekişinden ağın tükenmemesi için yeterince büyük bir [enerji](../ae2_mechanics/energy.md) tamponu sağlar.