---
navigation:
  parent: ../tricks_example_index.md
  title: Arayüz Otomatik Stoklama
  icon: appliedenergistics2:tile.BlockInterface
---

# Arayüz Otomatik Stoklama

Şunu sorabilirsin: "Çeşitli eşyalardan belirli bir miktarı stokta nasıl tutarım ve gerektikçe daha fazlasını nasıl üretirim?"

Bir çözüm, ağının [otomatik üretim](../ae2_mechanics/autocrafting.md) sisteminden otomatik olarak yeni eşya talep etmek için bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> ve bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> kullanmaktır. Bu düzen, çok çeşitli eşyalardan az miktarda bulundurmaya daha uygundur.

Bu gösterim düzeni çok geniş olmasın diye kısa kesilmiştir; [Kablolar](../items_blocks/cables.md) sayfasında anlatıldığı gibi normal bir kablodaki 8 [kanalın](../ae2_mechanics/channels.md) tamamını kullanmak için 4 <ItemLink id="appliedenergistics2:tile.BlockInterface" /> ve 4 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> kullanman büyük olasılıkla en verimlisidir.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/interface_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
  (1) Arayüz Blokları: İstenen eşyaları kendi içlerinde tutacak şekilde ayarlanır. Üretim Kartları vardır.
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
  (2) Depolama Otobüsleri: "Girdi/Çıktı Modu" "Yalnızca Çıkar" olarak ayarlanır.
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1) arayüz blokları, istenen eşyaları kendi içlerinde tutacak şekilde ayarlanır: istenen eşyayı üst yuvalarına tıklayarak veya NEI'den üst yuvalara sürükleyerek, ardından miktarı ayarlamak için yuvaların üzerindeki İngiliz Anahtarı simgesine tıklayarak. İçlerinde <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> bulunur.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2), "Girdi/Çıktı Modu" "Yalnızca Çıkar" olacak şekilde ayarlanır.

## Nasıl Çalışır

1. Bir <ItemLink id="appliedenergistics2:tile.BlockInterface" />, [ağ depolamasından](../ae2_mechanics/import_export_storage.md) yapılandırılmış bir eşyadan yeterince çekemezse (ve içinde <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" /> varsa), ağın [otomatik üretim](../ae2_mechanics/autocrafting.md) sisteminden o eşyadan daha fazla üretmesini talep eder.
2. <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />, ağın arayüzlerin içeriğine erişmesini sağlar.