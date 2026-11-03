---
navigation:
  parent: /ae2_mechanics_index.md
  title: Ağ Etkileşimleri
  icon: appliedenergistics2:item.ItemMultiPart:16
---

# Ağ Etkileşimleri

# Bağımsız ME Ağları
Vanilla AE2'de ME Ağı, [kablolar](./channels.md) ve kanal taşıyan diğer parçalarla birbirine bağlanan cihazlar grubudur. Teoride tek bir kablo bile bir ağ olabilir.

Bir ME Ağını tanımlayan özellik, tüm kablo ve cihazlarının [kanalları](./channels.md) aynı kontrolcü kümesinden çekmesidir.

Bundan, kablolar veya kanal taşıyan cihazlar aracılığıyla birbirine bağlı olmayan ağların birbirine kanal iletmediği ve dolayısıyla bağımsız ME Ağları olarak ele alınabileceği sonucunu çıkarabilirsin.

* Doğal olarak, fiziksel olarak birbirinden uzakta olan ve [Kablosuz Bağlayıcılar](../items_blocks/wireless_connectors.md) veya bir [Kuantum Halkası](./quantum_bridge.md) ile bağlanmayan iki ağ bağımsızdır.
* Yalnızca <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" showIcon="left"/> veya <ItemLink id="appliedenergistics2:item.ItemMultiPart:120" showIcon="left"/> ile bağlanan iki ME Ağı da bağımsız ağ olarak kabul edilir. Kuvars Lifi enerji iletir ama kanal iletmez; Kablo Çapaları ise ne enerji ne de kanal iletir ve yalnızca bitişik kabloları ayırmak için kullanılır. Farklı renkteki kablolar da birbirine bağlanmaz; ayrıntılar için [Kanallar](./channels.md) sayfasına bak.

# Ağlar Arası Etkileşim
Ağlar yalnızca bağımsız değildir. Birbirleriyle de etkileşebilirler ve bu etkileşimler çok esnek olabilir. Çoğu AE2 otomasyon sisteminin temeli budur. Genel olarak, iki bağımsız ME Ağı birbirini etkilediği sürece bu, ağ etkileşimi sayılabilir. Kanalları [P2P](./p2p_tunnels.md) ile iletmek için bir ME P2P tüneli kullanmak bunun bir örneğidir.

> Ayrıca bak: [Alt Ağlar](./subnetworks.md)

ME Ağları arasındaki etkileşim esas olarak [Arayüzler](../items_blocks/interface.md) ve [Depolama Veriyollarına](../items_blocks/storage_bus.md) bağlıdır; bunların davranışı farklı ağlara farklı roller verir.

## Tipik Okuma Etkileşimi

İki ME Ağı genellikle şöyle bir yapıya sahiptir:

<GameScene zoom="4" width="400" rotateY={0} rotateX={0}>
  <ImportStructure src="../assets/structures/network_interaction_basic_interacton.snbt" />
</GameScene>

Arayüzlerin ve Depolama Veriyollarının çalışma şekli nedeniyle mavi ağ genellikle erişilen taraf, beyaz ağ ise genellikle erişen taraftır. Bu kurulumda mavi ağ, beyaz ağ tarafından büyük bir "kap" olarak görülür ve beyaz ağ ondan [okuyabilir veya ona yazabilir](./import_export_storage.md).

## İç İçe Etkileşim
Yukarıdaki yapı birden çok katman halinde iç içe geçirilebilir. Ancak bu düzenin pratik kullanım alanı dardır ve dikkatsiz kullanım çok büyük miktarda donanım kaynağı tüketebilir.

<GameScene zoom="3" width="400" rotateY={0} rotateX={0}>
  <ImportStructure src="../assets/structures/network_interaction_nesting_interacton.snbt" />
</GameScene>

## Karşılıklı Okuma
İki ağ, Depolama Veriyolları aracılığıyla birbirinin içeriğini okuyabiliyorsa bu iki ME Ağı karşılıklı olarak birbirinden okuyor demektir. Bazı durumlarda bu, özel bir ihtiyaç için teknik bir çözümdür; ancak çoğu durumda yalnızca depolama karmaşasına yol açar ve oyun performansını ciddi şekilde düşürebilir.

<GameScene zoom="3" width="400" rotateY={0} rotateX={0}>
  <ImportStructure src="../assets/structures/network_interaction_network_read.snbt" />
</GameScene>