---
navigation:
  parent: /ae2_mechanics_index.md
  title: Enerji
  icon: appliedenergistics2:tile.BlockDenseEnergyCell
item_ids:
- appliedenergistics2:tile.BlockEnergyCell
- appliedenergistics2:tile.BlockDenseEnergyCell
- appliedenergistics2:tile.BlockCreativeEnergyCell
---

# Enerji

## Enerji Tamponu

ME ağları çalışmak için enerji gerektirir. Tüm ağ tek bir enerji tamponunu paylaşır. AE cihazları ile eşya ekleme ve çıkarma enerjiyi doğrudan bu ortak havuzdan çekerken, <ItemLink id="appliedenergistics2:tile.BlockVibrationChamber" showIcon="left" />, <ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" showIcon="left" /> ve <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> buraya enerji sağlar. Ağın herhangi bir yerine <ItemLink id="appliedenergistics2:item.ToolNetworkTool" showIcon="left" /> ile sağ tıklayarak ağın enerji istatistiklerini inceleyebilirsin.

Depolama ve dağıtım ağ düzeyinde yönetildiği için ağın kendi içinde etkin olarak hiçbir aktarım hızı sınırı yoktur. Cihazlar ihtiyaç duydukları kadar enerji çekebilir ve Enerji Alıcıları ağın depolayabildiği hızda enerji ekleyebilir. Gerçek sınır toplam depolama kapasitendir. Bu ortak tamponu [Enerji Hücreleri](../items_blocks/energy_cells.md) ile genişletebilirsin.

## Enerji Alma

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockEnergyAcceptor" meta="0" nbt='{inv:{},orientation_up:"UP",id:"BlockEnergyAcceptor",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockController" meta="1" nbt='{inv:{},proxy:{p:0,g:6L,k:-1L},orientation_up:"UP",id:"BlockController",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyController" meta="1" nbt='{inv:{},proxy:{p:0,g:11L,k:-1L},orientation_up:"UP",id:"BlockCreativeEnergyController",orientation_forward:"EAST",internalCurrentPower:"9.22337203685477E14d"}' scale="4" />

   <BlockImage id="appliedenergistics2:tile.BlockCableBus" nbt='{__guidenh_encoded_keys_v1:[0:{v:{id:"appliedenergistics2:item.ItemMultiPart",Count:1b,Damage:36s},k:"def:6"},1:{v:{id:"appliedenergistics2:item.ItemMultiPart",Count:1b,Damage:690s},k:"def:1"},2:{v:{},k:"extra:6"},3:{v:{},k:"extra:1"}],id:"BlockCableBus",hasRedstone:2}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockVibrationChamber" meta="0" nbt='{inv:{item0:{}},proxy:{p:0,g:12L,k:-1L},burnSpeed:100,orientation_up:"UP",burnTime:0.0d,id:"BlockVibrationChamber",maxBurnTime:0.0d,orientation_forward:"NORTH"}' scale="4" />
</Row>

AE2 dahili olarak FE, RF veya EU kullanmaz. Bunun yerine bu enerji sistemlerini kendi birimi olan AE'ye dönüştürür. Bu dönüşüm tek yönlüdür; GTNH'de AE'yi tekrar EU'ya dönüştüremezsin. Harici güç, <ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" showIcon="left" /> ve <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> aracılığıyla AE'ye dönüştürülebilir, ancak kontrolcü yüzleri genellikle [kanallar](./channels.md) için harcanmaya daha uygundur. Harici güç almanın yanı sıra, etkin olarak sınırsız AE için <ItemLink id="appliedenergistics2:item.ItemMultiPart:690" showIcon="left" /> ve <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyController" showIcon="left" /> da kullanabilirsin.

<GameScene zoom="3" rotateY={200} width="400">
    <ImportStructure src="../assets/structures/energy_receive.snbt" />
</GameScene>
Güç, <ItemLink id="appliedenergistics2:tile.BlockVibrationChamber" showIcon="left" /> ile de üretilebilir, ancak AE2 esas olarak GregTech veya IndustrialCraft 2 gibi çok daha iyi güç üretimine sahip teknoloji modlarıyla birlikte çalışmak üzere tasarlanmıştır.

Bu nedenle, üssünün güç altyapısını planlarken AE2 ağını tek bir büyük güç tüketen multiblok olarak düşünmen genellikle en iyisidir.

Dönüşüm oranları şunlardır:

*   2 FE/RF = 1 AE
*   1 EU  = 2 AE

## Enerji Depolama

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockEnergyCell" meta="7" nbt='{proxy:{p:0,g:14L,k:-1L},id:"BlockEnergyCell",internalCurrentPower:200000.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockDenseEnergyCell" meta="7" nbt='{proxy:{p:0,g:15L,k:-1L},id:"BlockDenseEnergyCell",internalCurrentPower:1600000.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyCell" scale="4" />
</Row>

Bariz nedenlerden dolayı bir ağ, bir tick içinde depolayabileceğinden daha fazla enerji alamaz veya tüketemez. Bir ağ yalnızca 800 AE depolayabiliyorsa, cihazları o tick içinde en fazla 800 AE kullanabilir ve bir Enerji Alıcısı o tick içinde en fazla 800 AE ekleyebilir.

Bu, tuhaf davranışların yaygın bir nedenidir. Örneğin, yalnızca bir Enerji Alıcısı, bir Sürücü, bir Terminal ve birkaç cihazdan oluşan minik bir ağ kurup içine dolu bir envanter dolusu kırıktaş boşaltmayı denersen, ağın tüm bu eklemeyi tek bir tick'te kaldıracak kadar tamponlanmış enerjisi olmayabilir. Kırıktaşın bir kısmı eklenemez, ağın enerjisi biter ve ağ yeniden başlayabilir.

Bu durum özellikle [Uzamsal IO](./spatial_io.md) kullanırken belirginleşir, çünkü bir [Uzamsal Sütun](../items_blocks/spatial_pylon.md) düzeneğini başlatmak çok büyük miktarda tamponlanmış enerji gerektirir. Çözüm, Enerji Hücreleri eklemektir.

* Ağdaki her kablo, cihaz veya parça yerleşik 25 AE tampon sağlar.

* <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> 8.000 AE'lik küçük bir dahili tampona sahiptir.

* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" showIcon="left" /> 200.000 AE depolar. Çoğu kullanım durumu için tek bir tanesi sıradan ağ güç dalgalanmalarını soğurmaya yeter.

* <ItemLink id="appliedenergistics2:tile.BlockDenseEnergyCell" showIcon="left" /> 1.600.000 AE depolar. Bir ağı depolanmış güçle çalıştırmak veya büyük [Uzamsal IO](./spatial_io.md) sistemlerinin çok büyük ani tüketimini karşılamak istediğinde kullanışlıdır.

* <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyCell" showIcon="left" /> sınırsız güç sağlayan, oyunun son dönemine ait UHV seviyesinde bir eşyadır.

* <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyController" showIcon="left" /> bir <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" /> ile bir <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyCell" showIcon="left" /> tek blokta birleştiren nihai ME Kontrolcüsüdür.