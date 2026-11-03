---
navigation:
  parent: /items_blocks_index.md
  title: P2P Tünelleri
  icon: appliedenergistics2:item.ItemMultiPart:460
categories:
- devices
---

# Noktadan Noktaya Tüneller

P2P tüneli kullanımı ve davranışı [AE2 Mekanikleri - P2P Tünelleri](../ae2_mechanics/p2p_tunnels.md) sayfasında anlatılmaktadır.

<Row>
<ItemImage id="appliedenergistics2:item.ItemMultiPart:460" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:461" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:462" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:463" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:466" scale="4" />
</Row>
<Row>
<ItemImage id="appliedenergistics2:item.ItemMultiPart:467" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:468" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:470" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:471" scale="4" />
<ItemImage id="appliedenergistics2:item.ItemMultiPart:472" scale="4" />
</Row>

P2P tünelleri eşyaları, sıvıları, Kızıltaş sinyallerini, enerjiyi, ışığı ve [kanalları](../ae2_mechanics/channels.md) bir ağ üzerinden doğrudan onunla etkileşime girmeden aktarır. Her varyant tek bir şey türünü taşır. İki blok yüzünü uzaktan birbirine bağlayan portallar gibi davranırlar; çift yönlü bir bağlantı yerine tanımlı giriş ve çıkış uçları vardır.

![Portal](../assets/images/p2p_portal.png)

Örneğin, bir Eşya P2P tüneline bakan bir huni, sanki diğer uçtaki varile doğrudan bağlıymış gibi davranır. Yan yana duran iki varil, tünel üzerinden eşya aktarmaz.

<GameScene width="300" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_hopper_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene width="300" height="200" zoom="4" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_barrel_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Türler ve Uyumlama

<GameScene width="400" zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

Tüm ME P2P tünelleri doğrudan üretilebilir. Yani, uyumlamak için herhangi bir P2P tüneline uygun eşyayla sağ tıkla:

- ME P2P: herhangi bir [kablo](cables.md)
- Kızıltaş P2P: bir Kızıltaş bileşeni
- Eşya P2P: bir sandık veya huni
- Sıvı P2P: bir demir kova veya cam şişe
- Enerji P2P: bir enerji kabı
- Işık P2P: bir meşale veya Parlak taş

ME P2P kanalları başka bir ME P2P tünelinden geçemez. Enerji P2P tünelleri, kendi [enerji](../ae2_mechanics/energy.md) tüketimleri üzerinden taşınan FE/E'nin %2,5'ini fiilen vergilendirir.

## Yaygın Kullanımlar

ME P2P tünelleri, çok sayıda [kanalı](../ae2_mechanics/channels.md) verimli şekilde taşımak için yaygın olarak kullanılır. Sekiz giriş tüneli bir kontrolcüden 256 (8 x 32) kanal alabilir ve sekiz çıkış tüneli bunları başka bir yere iletebilir; her uç yalnızca bir kanal tüketir. Tüneller özel bir [alt ağa](../ae2_mechanics/subnetworks.md) yerleştirilebildiğinden ana ağda kanal tüketmeleri gerekmez.

<GameScene width="350" height="300" zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/structures/p2p_compact_channels.snbt" />
  <IsometricCamera yaw="120" pitch="30" />
</GameScene>

## İç İçe Yerleştirme

ME P2P kanalları diğer ME P2P tünellerinden geçemez, bu yüzden süresiz olarak iç içe yerleştirilemezler. Diğer tünel türleri ME P2P tünellerinden geçebilir; örneğin aynı düzenekteki bir Kızıltaş P2P tüneli hâlâ çalışır.

<GameScene width="350" height="300" zoom="3" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_nesting.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

## Bağlama

<GameScene zoom="6" showBackground={false}>
  <ImportStructure src="../assets/structures/p2p_linking_frequency.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

P2P tünellerini bağlamak için bir <ItemLink id="appliedenergistics2:item.ToolMemoryCard" /> kullan. Bağlantı frekansı, her tünelin arkasında 2x2 renk dizisi olarak gösterilir.

- Yeni bir frekans oluşturmak için bir tünele Shift-sağ tıkla.
- Ayarları, bir yükseltme kartını veya bir frekansı yapıştırmak için sağ tıkla.

Shift-sağ tıklanan tünel giriştir; sağ tıklanan tünel çıkıştır. Birden fazla çıkışa izin verilir, ancak ME P2P kanalları her çıkışa kopyalanmak yerine aralarında paylaştırılır.

## Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:460" />

# P2P Tünelleri
P2P Tünellerinin kullanımı ve davranışı için [AE2 Mekanikleri - P2P Tünelleri](../ae2_mechanics/p2p_tunnels.md) sayfasına bak.
