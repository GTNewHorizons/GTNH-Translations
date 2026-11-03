---
navigation:
  parent: ../tricks_example_index.md
  title: Fırın Otomasyonu
  icon: minecraft:furnace
---

# Fırın Otomasyonu

Bunun bir <ItemLink id="appliedenergistics2:tile.BlockInterface" /> kullandığını, dolayısıyla [otomatik üretim](../ae2_mechanics/autocrafting.md)
düzeneğine entegre olacak şekilde tasarlandığını unutma. Yalnızca bir fırını tek başına otomatikleştirmek istiyorsan hunileri, sandıkları ve benzerlerini kullan.

Bir <ItemLink id="minecraft:furnace" /> otomasyonu, [şarj cihazı](charger_automation.md) gibi daha basit makinelerin otomasyonundan biraz daha karmaşıktır.
Bir fırın iki ayrı yönden giriş ve üçüncü bir yönden çekiş gerektirir. Eritilecek eşya üst yüzeye itilmeli,
yakıt bir yan yüze itilmeli ve sonuç alttan çekilmelidir. 

Bu, üstte bir <ItemLink id="appliedenergistics2:tile.BlockInterface" />
ile, yanda sürekli yakıt itmek için bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> ve altta sonuçları ağa aktarmak için bir <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />
ile yapılabilir. Ancak bu 3 [kanal](../ae2_mechanics/channels.md) kullanır.

İşte yalnızca 1 kanalla nasıl yapabileceğin:

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/furnace_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
  (1) ME Arayüzü: İlgili işleme kalıplarıyla birlikte, certus kuvars anahtarı kullanılarak yapılmış yönlü varyantı.

  <FloatingImage src="../assets/images/furnace_pattern.png" displayWidth="150" title="Demir Kalıbı" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
  (2) Arayüz: Varsayılan yapılandırmasında.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
  (3) Depolama Veriyolu #1: Kömüre filtrelenmiş.
  <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
  (4) Depolama Veriyolu #2: Bir ters çevirici kart kullanılarak kömürü kara listeye alacak şekilde filtrelenmiş.
  <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  Ana Ağa
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Yapılandırmalar

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1), ilgili <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" /> kalıplarıyla birlikte varsayılan yapılandırmasındadır.
    Üzerinde bir kuvars anahtarı kullanılarak yönlü hale getirilir.

  ![Demir Kalıbı](../assets/images/furnace_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2) varsayılan yapılandırmasındadır.
* İlk <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3), kömüre veya kullanmak istediğin yakıta filtrelenmiştir.
* İkinci <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (4), bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" /> kullanılarak kullandığın yakıtı kara listeye alacak şekilde filtrelenmiştir.

## Nasıl Çalışır

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />, malzemeleri arayüze iter.
   (Aslında bir optimizasyon olarak, doğrudan depolama veriyolları üzerinden, onlar sağlayıcının yüzlerinin uzantısıymış gibi iter. Eşyalar aslında hiçbir zaman arayüze girmez.)
2. Arayüz hiçbir şey depolamayacak şekilde ayarlanmıştır, bu yüzden malzemeleri [ağ depolamasına](../ae2_mechanics/import_export_storage.md) itmeye çalışır.
3. Yeşil alt ağdaki tek depolama <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> veriyollarıdır. Kömüre filtrelenmiş veriyolu, kömürü yan yüzden fırının yakıt yuvasına koyar.
    Kömür dışındakilere filtrelenmiş veriyolu, eritilecek eşyaları üst yüzden üst yuvaya koyar.
4. Fırın fırınlığını yapar
5. Huni, sonuçları fırının altından çeker ve sağlayıcının dönüş yuvalarına koyarak onları ana ağa geri döndürür.