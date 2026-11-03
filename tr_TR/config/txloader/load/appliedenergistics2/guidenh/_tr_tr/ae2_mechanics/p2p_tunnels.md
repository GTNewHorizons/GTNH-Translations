---
navigation:
  title: P2P Tünelleri
  parent: /ae2_mechanics_index.md
  icon: appliedenergistics2:item.ItemMultiPart:460

item_ids:
  - appliedenergistics2:item.ItemMultiPart:460
  - appliedenergistics2:item.ItemMultiPart:461
  - appliedenergistics2:item.ItemMultiPart:462
  - appliedenergistics2:item.ItemMultiPart:463
  - appliedenergistics2:item.ItemMultiPart:466
  - appliedenergistics2:item.ItemMultiPart:467
  - appliedenergistics2:item.ItemMultiPart:468
  - appliedenergistics2:item.ItemMultiPart:470
  - appliedenergistics2:item.ItemMultiPart:471
  - appliedenergistics2:item.ItemMultiPart:472
  - ae2fc:part_fluid_p2p_interface

quest_ids:
  - AAAAAAAAAAAAAAAAAAAAyw==
  - AAAAAAAAAAAAAAAAAAAFMw==
  - _bEWg1FHSmKu9MNhlbDlwA==
  - mk3rQ7LUQjC96FsFvDedKA==
---

# P2P Tünelleri

<GameScene zoom="4" width="300" height="200" interactive={false} allowLayerSlider={false}>
  <ImportStructure src="../assets/structures/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

P2P tünelleri, eşya, sıvı, kızıltaş sinyali, güç, ışık ve [kanallar](../ae2_mechanics/channels.md) gibi şeyleri doğrudan ağla etkileşime girmeden bir ağ üzerinde taşımanın bir yoludur. GTNH'de bunu kalıpları paralelleştirmek için de kullanabilirsin. P2P tünelinin birçok varyantı vardır ancak her biri yalnızca kendi belirli şey türünü taşır. Esasen uzaktaki iki blok yüzünü doğrudan birbirine bağlayan portallar gibi davranırlar. Çift yönlü değillerdir; tanımlı girişler ve çıkışlar vardır.

![Portal](../assets/images/p2p_portal.png)

# <ItemLink id="appliedenergistics2:item.ItemMultiPart:460" showIcon="left"/>

ME P2P Tüneli, AE kanallarını ileten bir P2P Tünelidir. Tüm çıkışlara 32 kanala kadar iletmeni sağlar (tüm çıkışlar girişin kanallarını paylaşır). Diğer P2P Tünellerinden farklı olarak ME P2P Tünelinin kendisi, iletilen ağdan ayrı bir ME Ağı üzerinde çalışmalıdır.

## ME P2P Tünelleri için Basit Kullanım Örneği

Bu örnekte, sarı renkli, kontrolcüsüz küçük bağımsız AE ağı 32 kanalı soldaki kontrolcüden sağa aktarır. Burada her ME terminali bir kanal kullanır.
  <GameScene zoom="4"  width="400">
    <ImportStructure src="../assets/structures/p2p_me.snbt" />
    <IsometricCamera yaw="-60" pitch="30" />
  </GameScene>

## ME P2P Tünelleri için Ölçekli Kullanım Örneği
  
  Bu örnekte, kontrolcülü sarı bağımsız ME ağı kendini ME kanallarını iletmeye adamıştır. P2P, kablolar ya da Kuantum Halkaları aracılığıyla iletilebilir.

<GameScene zoom="3"  width="400">
  <ImportStructure src="../assets/structures/compact_p2p_me.snbt" />
  <IsometricCamera yaw="-60" pitch="30" />
</GameScene>
  
Başka bir örnek için, [Kuantum Halkaları](quantum_bridge.md) ile kullanım da dahil, aşağıdaki ağ şemasına bak:

  ![P2P ve kuantum köprüleri](../assets/images/p2p_quantum_network.png)


## P2P Tüneli Türleri ve Uyumlama

Birçok P2P tüneli türü vardır. Yalnızca ME P2P tüneli doğrudan üretilebilir; diğerleri, belirli eşyalarla diğer P2P tünellerine sağ tıklanarak yapılır:
- P2P Tüneli - ME: Dönüştürmek için herhangi bir [ME Kablosu](../items_blocks/cables.md) ile sağ tıkla.
- P2P Tüneli - Kızıltaş: Dönüştürmek için herhangi bir kızıltaş bileşeniyle sağ tıkla.
- P2P Tüneli - Eşya: Dönüştürmek için bir sandıkla sağ tıkla.
- P2P Tüneli - Sıvı: Dönüştürmek için bir kova, su şişesi ya da herhangi bir <ItemImage id="EnderIO:itemLiquidConduit:0" label="right"/> ile sağ tıkla.
- P2P Tüneli - RF: Dönüştürmek için herhangi bir <ItemImage id="EnderIO:itemPowerConduit:0" label="right"/> ile sağ tıkla.
- P2P Tüneli - Işık: Dönüştürmek için bir meşale veya Parlak taşla sağ tıkla.
- P2P Tüneli - OC: Dönüştürmek için bir <ItemImage id="OpenComputers:cable" label="right"/> ile sağ tıkla.
- P2P Tüneli - Ses: Dönüştürmek için bir Nota Bloğu ile sağ tıkla.
- P2P Tüneli - GT EU: Dönüştürmek için herhangi bir GT Teli veya GT Kablosu ile sağ tıkla.
- P2P Tüneli - ME Arayüzü, <br><RecipesFor id="appliedenergistics2:item.ItemMultiPart:471" />
- P2P Tüneli - ME Çift Arayüzü, <br><RecipesFor id="ae2fc:part_fluid_p2p_interface" />

Bu P2P varyantlarının kullanımı ve özellikleri temel olarak ME P2P Tüneli ile aynıdır, <Color id="YELLOW">ancak bazı tünel türlerinin tuhaflıkları vardır</Color>:

- Lojistik tipi P2P Tünelleri, girdiyi tüm çıkışlara olabildiğince **eşit dağıtmaya** çalışır.
- Eşya ve Sıvı P2P Tünellerinde yerleşik itme veya çekme yoktur. İki ucu bir P2P Tüneliyle basitçe bağlamak içeriği taşımaz; içeriğin aktarılması için giriş ucunda bir itme kuvveti (örneğin huni, elektrikli pompa vb.) ya da çıkış ucunda bir çekme kuvveti sağlamalısın.
- Sıvı P2P Tünelleri çift yönlü aktarım yapabilir, ancak yine de yalnızca bir giriş olabilir.
- GT EU P2P Tünelini kullanmak, tıpkı modern Enerji P2P Tünelleri gibi, çıkıştan amper başına %5 gerilim vergisi alır. Örneğin giriş 8192V 16A ise karşılık gelen çıkış 7782V 16A olur.

## <ItemLink id="appliedenergistics2:item.ItemMultiPart:471" showIcon="left"/> ve <ItemLink id="ae2fc:part_fluid_p2p_interface" showIcon="left"/>
Bunlar GTNH tarafından eklenen iki yeni P2P Tünelidir. İletim için değil, Arayüz/Çift Arayüz gibi kalıp materyallerini itmek için kullanılırlar. Bu nedenle aşağıdaki sahnede kırmızıyla işaretlenen kullanım geçersizdir; kalıplar P2P Tüneli - Arayüz/Çift Arayüz ile çıkış uçlarına iletilemez. Bunun yerine **giriş ucuna** yerleştirilmelidirler. Şu anda hem giriş hem çıkış uçları bitişik bloklara kalıp materyalleri itebilir. Bir bağlantı noktası doğrudan materyal kabul edemeyen bir bloğa bakıyorsa göz ardı edilir. Her panel, bir [Arayüz](../items_blocks/interface.md) / [Çift Arayüz](../items_blocks/interface.md) temel işlevlerine sahiptir. Her P2P Tüneli - Arayüz/Çift Arayüzün engelleme modu tek tek ayarlanmalıdır. Her P2P Tüneli - Arayüz/Çift Arayüz, fiilen giriş ucuyla aynı kalıpları içerir.

Onları kullanarak kalıp materyallerini paralelleştirmek için kalıbı yalnızca giriş ucuna koyman yeterlidir; böylece fiziksel paralellik elde edersin. 

  <GameScene zoom="3" showBackground={false} width="400" height="200">
    <ImportStructure src="../assets/structures/p2p_interface.snbt" />
    <TextAnnotation pos="0.5 2 5.5" color="#ff0000" text="Placing patterns in this interface will not work properly."/>
    <TextAnnotation pos="4.5 1.7 5" color="#00ff00" text="Place patterns in this input end to send materials to available ports." maxWidth="180"/>
  </GameScene>

# İç İçe Yerleştirme
Ancak bunu tek bir kablodan sonsuz kanal göndermek için kullanamazsın. Bir ME P2P tünelinin kanalı başka bir ME P2P tünelinden geçmez; bu yüzden onları özyinelemeli olarak iç içe yerleştiremezsin. Kırmızı kablolardaki ME P2P tünellerinin dış katmanının çevrimdışı olduğunu görebilirsin. Bunun yalnızca ME P2P tünelleri için geçerli olduğunu unutma; Kızıltaş P2P tünellerinin sorunsuz çalışmasından da görüldüğü gibi diğer P2P tüneli türleri bir ME P2P tünelinden geçebilir.

<GameScene zoom="3" width="600" height="300" align="center" allowLayerSlider={false} >
    <ImportStructure src="../assets/structures/p2p_nesting_mechanics.snbt" />
    <ImportPonder src="../assets/ponder/p2p_nesting.json" />
</GameScene>

# Bağlama

Bir P2P tüneli bağlantısının uçları bir <ItemLink id="appliedenergistics2:item.ToolMemoryCard" showIcon="left"/> kullanılarak bağlanabilir. Shift-sağ tıkladığın tünel giriş, sağ tıkladığın tünel çıkış olur. Birden fazla çıkışın olabilir, ancak ME P2P tünellerinde girişte akan kanallar çıkışlar arasında bölünür; yani kanalları çoğaltamazsın.

# Tarif

<RecipeFor id="appliedenergistics2:item.ItemMultiPart:460" />