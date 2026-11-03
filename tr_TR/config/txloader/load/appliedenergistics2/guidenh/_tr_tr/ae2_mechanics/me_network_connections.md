---
navigation:
  parent: /ae2_mechanics_index.md
  title: Ağ Bağlantıları
  icon: appliedenergistics2:item.ItemMultiPart:16
quest_ids:
  - AAAAAAAAAAAAAAAAAAAFMQ==
  - tM8pT_W3RCqZNDAovERxFg==
---

# Ağ Bağlantıları

Aynı ME Ağı içinde, farklı bölgelerdeki cihazlar kablolu ya da kablosuz olarak çeşitli şekillerde birbirine bağlanabilir.

## Kablolu Bağlantılar
* Aynı ME Ağındaki cihazlar, kanalları iletmek için kablolarla bağlanabilir ya da kanalları cihazların kendileri üzerinden bitişikteki kablolara ve cihazlara iletebilir. Bir cihaz üzerinden en fazla 8 kanal iletilebilir; bu, standart bir kabloya eşdeğerdir.

* Kablolu bağlantılarda kanallar **ME P2P Tünelleri** kullanılarak iletilebilir. Daha fazla ayrıntı için [P2P](./p2p_tunnels.md) sayfasına bak.

* GTNH'de ME Kapakları/Veriyolları (<ItemLink id="gregtech:gt.blockmachines:2718" showIcon="left"/>, <ItemLink id="gregtech:gt.blockmachines:2717" showIcon="left"/>, <ItemLink id="gregtech:gt.blockmachines:2710" showIcon="left"/> veya <ItemLink id="gregtech:gt.blockmachines:2713" showIcon="left"/> vb.) <ItemLink id="gregtech:gt.metatool.01:26" showIcon="left"/> ile sağ tıklanarak bitişik bağlantı moduna geçirilebilir. Bu, tıpkı AE cihazları gibi bitişik ME Kapaklarına/Veriyollarına, AE cihazlarına veya kablolara kanal iletmelerini sağlar. Bu bağlantı yöntemi de en fazla 8
kanal iletir.

## Kablosuz Bağlantılar
* GTNH, <ItemLink id="appliedenergistics2:tile.BlockWirelessConnector" showIcon="left"/> ve <ItemLink id="appliedenergistics2:tile.BlockWirelessHub" showIcon="left"/> öğelerini sağlayan AE2 Stuff eklentisini içerir. Bir çift, kablosuz olarak 32 kanala kadar iletebilir ancak <Color id="RED">boyutlar arası bağlantı kuramaz</Color>. <ItemLink id="appliedenergistics2:item.ToolWirelessKit" showIcon="left"/> kullanılarak eşleştirilebilirler. İlki 1'e 1 bağlantılar içindir; ikincisi ise [P2P Tünelleri](./p2p_tunnels.md) gibi 1'den çoğa bağlantı yapabilir. Kablosuz bağlayıcılar, bir ME ağını ilk kurduğun aşamada güç ızgarana ağır bir
yük bindirebilir; bu yüzden güç tüketimini önceden hesapla. Belirli bilgiler için görev kitabındaki "<QuestLink id="AAAAAAAAAAAAAAAAAAAFMQ==" />" sayfasına bak.

* Vanilla AE2, ağları kablosuz bağlamanın bir yolunu sunar: Kuantum Halkası. Her çift, kablosuz olarak 32 kanala kadar iletebilir ve <Color id="GREEN">boyutlar arası bağlantı kurabilir</Color>. Ayrıntılar için [Kuantum Halkası](./quantum_bridge.md) sayfasına bak.

* <ItemLink id="RIO:tile.remote_interface" showIcon="left"/> RemoteIO modundan bir bloktur. Uzak Arayüz, bir <ItemLink id="ThaumicTinkerer:interface" showIcon="left" /> gibi davranır; bir bloğu uzaktan vekâleten temsil edebilir ve vekillik yaparken hedef bloğun tüm işlevlerini kazanır. Ayrıca <Color id="GREEN">boyutlar arası bağlantı kurabilir</Color>. Üretim maliyeti, boyutlar arası ağ çözümleri arasında en yüksek teknoloji gereksinimlerine sahiptir; <ItemLink id="dreamcraft:CircuitIV" showIcon="left"/> ve <ItemLink id="gregtech:gt.metaitem.01:32654" showIcon="left"/> üretme yeteneğini gerektirir.
  * Elinde bir <ItemLink id="RIO:item.chip.location" showIcon="left"/> varken (üretim sırasında devre kartı herhangi bir devre kartı olarak damgalanmalıdır), ME Kontrolcüsüne Shift+Sağ tıkla.
  * Uzak Arayüzü hedefe yerleştir, Konum Çipini tut ve hedefi yüklemek için arayüz bloğuna sağ tıkla.
  * Elinde bir <ItemLink id="RIO:item.chip.transfer:20" showIcon="left"/> varken Uzak Arayüze sağ tıkla. Bu işlemlerden sonra Uzak Arayüz kanal iletebilir.