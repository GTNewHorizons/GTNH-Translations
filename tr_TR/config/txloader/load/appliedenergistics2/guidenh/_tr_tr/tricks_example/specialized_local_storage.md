---
navigation:
  parent: ../tricks_example_index.md
  title: Özelleştirilmiş Yerel Depolama
  icon: appliedenergistics2:tile.BlockDrive
---

# Özelleştirilmiş Yerel Depolama

[Arayüzün özel davranışlarından](../items_blocks/interface.md#special-interactions) birini kullanan bir
[alt ağ](../ae2_mechanics/subnetworks.md), depolamasının içeriğini ana ağa sunabilir; ana ağın depolamasını
göremez ve yalnızca 1 [kanal](../ae2_mechanics/channels.md) kaplar.

Bu, bir çiftlikte yerel depolama için kullanışlıdır; böylece eşyalar ana depolamana taşmaz.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/local_storage.snbt" />

  <BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
  (1) Eşya içe aktarmanın bir yolu (bu durumda bir arayüz)
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
  (2) Sürücü: İçinde birkaç hücre var. Hücreler, çiftliğin ürettiği şeylere göre filtrelenmelidir.
  Hücrelerde Eşit Dağıtım Kartları ve Taşma İmha Kartları olabilir.
  <Row><ItemImage id="appliedenergistics2:item.ItemBasicStorageCell.4k" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:69" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:68" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
  (3) Üretim Terminali: Alt ağdaki Sürücünün içeriğini görebilir, ancak ana ağındaki depolamanın içeriğini göremez.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
  (4) Arayüz #2: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
  (5) Depolama Veriyolu: Önceliği ana depolamadan yüksek ayarlanmış, çiftliğin ürettiği şeylere göre filtrelenebilir.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
  Üretim Terminali: Hem ana ağın depolamasının içeriğini *hem de* alt ağı görebilir.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* İlk <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1), sahip olduğun çiftlikten eşyaları basitçe kabul eder ve alt ağa iter.
* <ItemLink id="appliedenergistics2:tile.BlockDrive" /> (2) içinde birkaç [hücre](../items_blocks/storage_cells.md) vardır. Hücreler,
  çiftliğin ürettiği şeylere göre [bölümlendirilmelidir](../items_blocks/cell_workbench.md).
Hücrelerde <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:69" /> ve <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" /> olabilir.
* İkinci <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (4) varsayılan yapılandırmasındadır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> öğesinin [önceliği](../ae2_mechanics/import_export_storage.md#storage-priority) ana depolamadan
  yüksek ayarlanmıştır. Çiftliğin ürettiği şeylere göre filtrelenebilir.

## Nasıl Çalışır

* Alt ağdaki <ItemLink id="appliedenergistics2:tile.BlockInterface" />, ana ağdaki <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> öğesine
<ItemLink id="appliedenergistics2:tile.BlockDrive" /> içeriğini gösterir. Bu, depolama veriyolunun doğrudan sürücüdeki hücrelerden eşya çekebileceği ve onlara eşya itebileceği anlamına gelir.
* Depolama veriyolu yüksek [önceliğe](../ae2_mechanics/import_export_storage.md#storage-priority) ayarlanmıştır, böylece eşyalar ana depolaman yerine tercihen
  alt ağa geri konur.
* Önemlisi, alt ağdaki hücreler dolduğunda eşyalar ana ağa taşmaz. Çiftlik, tıkanmadan bozulan bir türse
bunun yerine fazla eşyaları silmek için <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:68" /> kullanılabilir.
* Çiftlik birden fazla eşya üretiyorsa <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:69" />, bir eşyanın tüm hücreleri doldurup
diğer eşyaların depolanmasını engellemesini önleyebilir.