---
navigation:
  parent: ../tricks_example_index.md
  title: Seviye Vericisi ile Otomatik Stoklama
  icon: appliedenergistics2:item.ItemMultiPart:280
---

# Seviye Vericisi ile Otomatik Stoklama

Şöyle sorulabilir: "Bir eşyadan belirli bir miktarı stokta nasıl tutarım ve gerektiğinde nasıl daha fazlasını üretirim?"

Bir çözüm, ağının [otomatik üretiminden](../ae2_mechanics/autocrafting.md) otomatik olarak yeni eşya talep etmek için bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> ve <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> kullanmaktır. Bu kurulum tek bir eşyadan büyük miktarda bulundurmaya yöneliktir.

Elbette seviye vericisini ve Kızıltaş kartını atlayarak ağının sürekli üretim yapmasını sağlayabilirsin.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
  (1) Dışa Aktarma Veriyolu: İstenen eşyaya filtrelenmiştir. Kızıltaş Kartı ve Üretim Kartı vardır. Kızıltaş modu
  "Sinyalle etkin" olarak, üretim davranışı "Stoktaki eşyaları kullanma" olarak ayarlanmıştır.
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
  (2) Seviye Vericisi: İstenen eşya ve miktarla yapılandırılmış, "Seviyeler sınırın altına düştüğünde yay" olarak ayarlanmıştır.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
  (3) Arayüz: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> (1) istenen eşyaya filtrelenmiştir. Bir Kızıltaş kartı ve bir üretim kartı vardır.
  "Kızıltaş Modu" "Sinyalle etkin" olarak, "Üretim Davranışı" "Stoktaki eşyaları kullanma" olarak ayarlanmıştır.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (2) istenen eşya ve miktarla yapılandırılmış ve "Seviyeler sınırın altına düştüğünde yay" olarak ayarlanmıştır.
* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (3) varsayılan yapılandırmasındadır.

## Nasıl Çalışır

1. [Ağ deposundaki](../ae2_mechanics/import_export_storage.md) istenen eşya miktarı
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> içinde belirtilen miktarın altındaysa, bir Kızıltaş sinyali yayar.
2. Bir Kızıltaş sinyali aldığında (<ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> sayesinde ve stoktaki eşyaları kullanmama ayarıyla birlikte),
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> ağın [otomatik üretiminden](../ae2_mechanics/autocrafting.md) istenen eşyadan daha fazla üretmesini
   ister, ardından onu dışa aktarır.
3. İçine bir eşya itildiğinde (ve dahili envanterinde bir şey bulunacak şekilde yapılandırılmadığında),
   <ItemLink id="appliedenergistics2:tile.BlockInterface" /> o eşyayı ağ deposuna iter.