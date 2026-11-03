---
navigation:
  parent: /items_blocks_index.md
  title: ME Sürücüsü
  icon: appliedenergistics2:tile.BlockDrive
categories:
- devices
item_ids:
- appliedenergistics2:tile.BlockDrive
---

# ME Sürücüsü

<ItemImage id="appliedenergistics2:tile.BlockDrive" scale="4" />

ME Sürücüsü, [depolama hücrelerini](storage_cells.md) barındıran bir [cihazdır](../ae2_mechanics/devices.md). Sürücünün içindeki hücreler [ağ deposu](../ae2_mechanics/import_export_storage.md) sayılır ve tek tek hücreler için on yuvaya sahiptir.

Hücreler huniler veya AE2 veriyolları gibi herhangi bir lojistik yöntemle yerleştirilebilir ya da çıkarılabilir.

Sürücü, <ItemLink id="appliedenergistics2:item.ToolCertusQuartzWrench" /> ile döndürülebilir.

## Hücre Durum LED'leri

Sürücüdeki hücrelerin LED'leri mevcut durumlarını gösterir:

| Renk | Durum |
| :--- | :--- |
| Yeşil | Boş |
| Mavi | Eşya içeriyor |
| Turuncu | [Türler](../ae2_mechanics/bytes_and_types.md) dolu; yeni tür eklenemez |
| Kırmızı | [Baytlar](../ae2_mechanics/bytes_and_types.md) dolu; yeni eşya eklenemez |
| Siyah | Güç yok veya sürücünün [kanalı](../ae2_mechanics/channels.md) yok |

## Öncelik

Öncelik ayarlamak için GUI'nin sağ üst köşesindeki anahtara tıkla. Ağa giren eşyalar en yüksek öncelikli depolama konumunu tercih eder. İki konum aynı önceliğe sahipse eşyayı zaten içeren konum tercih edilir. [Hücre Çalışma Tezgahı](cell_workbench.md) ile bölümlendirilmiş hücreler, öncelikler eşitken bölümlerindeki eşyaları hâlihazırda içeriyor sayılır. Depodan çıkan eşyalar önce en düşük öncelikli konumdan çekilir. Böylece normal içe ve dışa aktarma sırasında yüksek öncelikli depo dolar, düşük öncelikli depo boşalır.

## Tarif

<RecipeFor id="appliedenergistics2:tile.BlockDrive" />