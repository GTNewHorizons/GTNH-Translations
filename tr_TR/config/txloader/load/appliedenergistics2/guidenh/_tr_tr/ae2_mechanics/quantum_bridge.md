---
navigation:
  parent: /ae2_mechanics_index.md
  title: Kuantum Halkası
  icon: appliedenergistics2:tile.BlockQuantumLinkChamber
item_ids:
- appliedenergistics2:tile.BlockQuantumRing
- appliedenergistics2:tile.BlockQuantumLinkChamber
---
# Kuantum Halkası

Kuantum Halkası, kanalları kablosuz olarak iletmeye yönelik vanilla AE2 çözümüdür. Yalnızca kablosuz kanal iletimini desteklemekle kalmaz, boyutlar arası da bağlantı kurabilir. Bir AE2 bileşeni için enerji tüketimi oldukça yüksektir; bu, AE sistemini ilk açtığın gerilim kademesinde güç ızgaranı zorlayabilir, bu yüzden güç ihtiyaçlarını önceden hesapla.

Referans olarak, her bir Kuantum Halkası çifti yaklaşık 1000 EU/t tüketir.

# Kuantum Düğümlü Tekillik
Bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:48" showIcon="left" />, bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:47" showIcon="left" /> bölünerek oluşturulur. Bir Kuantum Halkası çiftini bağlamak için kullanılabilen benzersiz NBT verisine sahiptirler.

Sonuç olarak, doğrudan Yaratıcı moddan alınan Kuantum Düğümlü Tekillikler, geçerli eşleştirilmiş NBT verisinden yoksun oldukları için etkisizdir.

Kuantum Düğümlü Tekillikler elde etmek için önce bir <ItemLink id="appliedenergistics2:tile.BlockCondenser" showIcon="left" /> öğesini Tekillik çıktı moduna geçirmeli ve bir <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:38" showIcon="left" /> doldurmalısın. Bir tekillik elde ettikten sonra, onu bir Ender İncisi Tozu ile birlikte yere bırak ve yakınlarda bir patlama tetikle. Patlama, karşılıklı eşleşen bir Kuantum Düğümlü Tekillik grubu oluşturur. Farklı Kuantum Halkası sistemlerini ayırt etmek ve karışıklığı önlemek için bunları bir örs kullanarak yeniden adlandırabilirsin.

Not: Patlayıcılar yine de hasara ve arazi tahribatına neden olur, bu yüzden lütfen önemli alanlardan uzak dur. Büyük bir arazi alanını yok etmek istemiyorsan AE2, düğümlü tekillikler oluşturmak için <ItemLink id="appliedenergistics2:tile.BlockTinyTNT" showIcon="left" /> da sunar. Yalnızca çok küçük bir arazi alanını yok eder ve hasar vermez.

# Multiblok Yapı
Kuantum Halkası, <ItemLink id="appliedenergistics2:tile.BlockQuantumRing" showIcon="left" /> ve <ItemLink id="appliedenergistics2:tile.BlockQuantumLinkChamber" showIcon="left" /> oluşan bir multiblok yapıdır. Çalışan bir Kuantum Halkası iletim sistemi, bu multiblok yapıların bir çiftinden oluşur. Yapılar kurulduktan sonra, her birine yeterli enerji sağlayarak ve eşleştirilmiş bir Kuantum Düğümlü Tekillik grubundan birini her bir Kuantum Bağlantı Odasına yerleştirerek iki Kuantum Halkasını bağlayabilirsin.

Genellikle bir çiftteki Kuantum Halkalarından biri uzakta bulunur. Sistemi çalışır durumda tutmak için, iki Kuantum Halkasının da bulunduğu yığınları yüklemeli ve her iki taraftaki güç beslemesini aynı anda sürdürmelisin. Kurulmuş ve başarıyla bağlanmış Kuantum Halkaları doğrudan ME Ağından güç çekebilir, ancak çok oyunculu sunucular veya başka nedenlerden kaynaklanan yığın yükleme ve enerji beslemesi dalgalanmalarını hafifletmek için uzaktaki Kuantum Halkası için özel ve bağımsız bir güç kaynağı sağladığından emin ol. Bir <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" showIcon="left" />, <ItemLink id="appliedenergistics2:tile.BlockDenseEnergyCell" showIcon="left" /> veya <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyCell" showIcon="left" /> kullanabilirsin. Ayrıca doğrudan küçük bir GT jeneratörü bağlayabilirsin, ancak güç çıktısı, Kuantum Halkası başlatma dizisini (önyükleme botları) başarıyla tamamlayıp ME Ağından güç çekmeye geçene kadar bu ihtiyacı karşılayacak kadar büyük olmalıdır.

Kuantum Halkasında yalnızca her bir taraftaki merkez blok [kablolara](../items_blocks/cables.md) bağlanabilir. Bir Kuantum Halkası çifti en fazla 32 kanal iletebilir.

<GameScene zoom="3" width="600">
  <ImportStructure src="../assets/structures/quantum_bridge.snbt" />
</GameScene>