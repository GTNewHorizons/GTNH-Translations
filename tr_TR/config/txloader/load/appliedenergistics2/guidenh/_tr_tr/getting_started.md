---
navigation:
  title: Başlarken
  position: 10
  parent: /index.md
---

# Hızlı Başlangıç

# Basit Depolama Ağı
AE2'ye kolayca başlaman için önce AE2'nin temel işlevini, yani depolamayı gerçekleştirecek basit bir depolama ağı kuralım.

## Ön Koşullar
Applied Energistics 2 adeta uzaylı teknolojisidir. Dünyanın dört bir yanına dağılmış [Meteorlar](./ae2_mechanics/meteorites.md) bulabilirsin. Merkezlerinde bir <ItemLink id="appliedenergistics2:tile.BlockSkyChest" showIcon="true"/> bulunabilir. Bu sandıkların içinde temel AE2 eşyalarını bulma şansın var: <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:13" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:14" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:15" showIcon="true"/> ve <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:19" showIcon="true"/>. AE2 bileşenlerini ve bloklarını üretmek için bunlara ihtiyacın var. GTNH'de AE2 ayrıca GregTech'e entegre edilmiştir, bu yüzden bir AE sistemi kurmadan önce EV kademesine ulaşmalı ve Titanyum elde etmelisin.

## Materyaller
Bir AE sistemi kurmak için gereken teknolojik seviyeye ulaştığında, ayrıca şu materyallere de ihtiyacın olacak:
- <ItemImage id="gregtech:gt.blockores2:516" label="right"/>
  - AE eşyalarını ve bloklarını üretmek için önemli ham materyaller olan <ItemImage id="gregtech:gt.metaitem.01:2516"  label="right"/> ve <ItemImage id="gregtech:gt.metaitem.01:8516" label="right"/> eşyalarını bundan elde etmemiz gerekiyor.
- <ItemImage id="gregtech:gt.blockores2:28" label="right"/>
  - Birçok AE bloğu, üretim için <ItemImage id="gregtech:gt.metaitem.01:17028" label="right" /> gerektirir.
- <ItemImage id="minecraft:redstone" label="right" />, <ItemImage id="minecraft:diamond" label="right"/> ve <ItemImage id="dreamcraft:CircuitHV"  label="right"/> gibi diğer temel materyaller. EV kademesine giderken bu materyallerle mutlaka karşılaşmışsındır, bu yüzden burada ayrıntıya girilmeyecek.

## Kurulum
Her şey hazır olduğunda, aşağıdaki basit depolama ağını kuralım. Şu sahneyi oluşturman gerekiyor.

<GameScene zoom="5" interactive={true} width="400" height="300">
  <ImportStructure src="../assets/structures/getting_started.snbt" />
  <IsometricCamera yaw="200" pitch="30" />
  <BlockAnnotation pos="5 0 0" color="#e5e90c" alwaysOnTop={true}>
  <Color color="#e5e90c">Bu, gösterim amacıyla yerleştirilmiş bir Hata Ayıklama Jeneratörü'dür ve Hayatta Kalma modunda elde edilemez. Normal kullanım için lütfen güç ızgarana bağla.</Color>
  </BlockAnnotation>
</GameScene>

Sahnedeki AE sistemi, güç için soldaki GT güç ızgarasından yararlanır. Bu AE sistemi temel eşya depolama işlevini gerçekleştirir:
- <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="true"/> tüm ağa [Kanallar](./ae2_mechanics/channels.md) sağlar.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" showIcon="true"/> ağdaki tüm bileşenleri birbirine bağlar.
- Depolama alanı sağlamak için <ItemLink id="appliedenergistics2:tile.BlockDrive" showIcon="true"/> içine bir <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" showIcon="true"/> yerleştirilmiştir.
- Bir sandığın depolama alanını AE ağına entegre etmek için sandığın yanına bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" showIcon="true"/> yerleştirilmiştir.
- Bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" showIcon="true"/>, oyuncuların AE ağının iç alanıyla etkileşime girmesi için kanal sağlar.

Artık AE depolama ağını açmak için terminale sağ tıklayabilir, tıpkı normalde bir sandık kullanıyormuş gibi terminalden eşya ekleyip çıkarabilirsin. Sandığa elle koyduğun eşyalar da AE terminalinde görüntülenir. Bu noktada başarıyla bir AE depolama ağı kurdun, ancak bu AE ağları için buzdağının yalnızca görünen kısmı. Daha fazla içerik için lütfen bu rehberi keşfetmeye devam et.

[Eşyalar ve Bloklar](items_blocks_index.md)

[AE2 Mekanikleri](ae2_mechanics_index.md)

[İpuçları ve Pratik Örnekler](tricks_example_index.md)