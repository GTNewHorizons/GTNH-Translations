---
navigation:
  parent: /items_blocks_index.md
  title: ME Sandığı
  icon: appliedenergistics2:tile.BlockChest
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockChest
---

# ME Sandığı

<BlockImage id="appliedenergistics2:tile.BlockChest" meta="0" nbt='{inv:{item0:{},item1:{id:"appliedenergistics2:item.ItemBasicStorageCell.1k",Count:1b,tag:{ic:1L,it:1s,__guidenh_encoded_keys_v1:[0:{v:1L,k:"@0"},1:{v:{Craft:0b,Cnt:1L,id:"minecraft:stone",Count:0b,Damage:0s,Req:0L},k:"#0"}]},Damage:0s}},proxy:{p:0,g:341L,k:-1L},orientation_up:"UP",SORT_BY:"NAME",terminalSettings:[0:{uuid_l:-8061629327903583552L,uuid_m:-937944366173238364L,savedString:"""",map:[]}],VIEW_MODE:"ALL",paintedColor:16b,id:"BlockChest",priority:0,SORT_DIRECTION:"ASCENDING",orientation_forward:"NORTH",internalCurrentPower:40.0d}' scale="4" />

ME Sandığı, içinde bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" />, bir <ItemLink id="appliedenergistics2:tile.BlockDrive" /> ve bir <ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" /> bulunduran minyatür bir ağ gibidir. Küçük bir ağ depolaması olarak kullanılabilir, ancak işlevselliği yalnızca tek bir [depolama hücresi](storage_cells.md) tutabilmesi nedeniyle sınırlıdır.

Özellikle içindeki hücrelerle tek tek etkileşim kurmak için kullanışlıdır. İçine entegre edilmiş terminal yalnızca sandığın içindeki hücrelere erişebilirken, normal bir ağdaki [cihazlar](../ae2_mechanics/devices.md) ME Sandığı da dahil olmak üzere herhangi bir [ağ depolamasına](../ae2_mechanics/import_export_storage.md) erişebilir.

İki GUI'si vardır; hangi GUI'nin açılacağı tarafa göre değişir. Üst taraftaki terminalle etkileşime geçmek terminal arayüzünü açar. Bir depolama veriyolu, hücre yuvası olmayan herhangi bir taraftan ME Sandığı içindeki hücrelerin depolamasına erişebilir. Lojistik sistemler ona yalnızca eşya ekleyebilir, ondan eşya çekemez. Diğer taraflarla etkileşime geçmek, bir depolama hücresi yerleştirme ve önceliğini ayarlama GUI'sini açar. Eşya lojistik sistemleri hücreyi yalnızca hücre yuvası olan taraftan çıkarabilir.

<ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> kullanılarak döndürülebilir.

Yalnızca küçük bir AE enerji tamponuna sahiptir; bu nedenle bir [enerji hücresi](energy_cells.md) olmadan aynı anda çok fazla eşya girişi ve çıkışı yapmaya çalışmak enerjisinin tükenmesine yol açabilir.

Terminal, <ItemLink id="appliedenergistics2:item.ToolColorApplicator" /> kullanılarak boyanabilir.

<GameScene width="250" height="100" zoom="4" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/chest_color.snbt" />
  <IsometricCamera yaw="105" pitch="30" />
</GameScene>

## Ayarlar

ME Sandığı <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" /> ve <ItemLink id="appliedenergistics2:item.ItemMultiPart:360" /> ile aynı ayarlara sahiptir, ancak <ItemLink id="appliedenergistics2:item.ItemViewCell" /> desteklemez.

## Hücre Durumu LED'leri

Sandığın içindeki hücreler durumlarını LED'leri aracılığıyla gösterebilir:

| Renk | Durum |
| :--- | :--- |
| Yeşil | Boş |
| Mavi | Eşya içeriyor |
| Turuncu | [Türler](../ae2_mechanics/bytes_and_types.md) dolu, yeni tür eklenemiyor |
| Kırmızı | [Baytlar](../ae2_mechanics/bytes_and_types.md) dolu, yeni eşya eklenemiyor |
| Siyah | Enerji yok veya sandıkta [kanal](../ae2_mechanics/channels.md) eksik |

## Öncelik

Öncelik, GUI'nin sağ üst köşesindeki İngiliz anahtarına tıklanarak ayarlanabilir. Ağa giren eşyalar tercihen en yüksek önceliğe sahip depolama konumuna girer. İki depolama konumu aynı önceliğe sahipse, eşyayı zaten içeren konum tercih edilir. [Biçimlendirmeye](cell_workbench.md) sahip bir hücre, öncelikler eşit olduğunda eşyayı zaten içeriyor kabul edilir. Depolamadan çıkarılan eşyalar tercihen en düşük önceliğe sahip konumdan çıkarılır. Bu öncelik sistemi, eşya girişi ve çıkışı sırasında yüksek öncelikli depolama konumlarının doldurulmasına, düşük öncelikli konumların ise boşaltılmasına neden olur.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockChest" />