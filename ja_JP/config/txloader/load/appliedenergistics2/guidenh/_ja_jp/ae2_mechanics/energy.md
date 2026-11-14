---
navigation:
  parent: /ae2_mechanics_index.md
  title: 電力
  icon: appliedenergistics2:tile.BlockDenseEnergyCell
item_ids:
- appliedenergistics2:tile.BlockEnergyCell
- appliedenergistics2:tile.BlockDenseEnergyCell
- appliedenergistics2:tile.BlockCreativeEnergyCell
---

# 電力

## エネルギーバッファ

MEネットワークは稼働に電力が必要です。ネットワークの全体でエネルギーバッファを共有します。AEの端末は、アイテムの入出と同様にネットワークから直接電力を消費します。<ItemLink id="appliedenergistics2:tile.BlockVibrationChamber" showIcon="left" />、<ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" showIcon="left" />、<ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" />はネットワークに電力を供給します。<ItemLink id="appliedenergistics2:item.ToolNetworkTool" showIcon="left" />でネットワークのどこかに対し右クリックをすると、 電力統計を見ることができます。

ストレージと配分はネットワーク単位で処理されるため、実質ネットワーク内での輸送速度に制限はありません。端末は必要な分だけ電力を消費し、エネルギー受容体はネットワークの電力容量の速度で電力を引き入れます。その実際の上限は合計容量です。このバッファは[エネルギーセル](../items_blocks/energy_cells.md)を使用することで拡張できます。

## 電力搬入

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockEnergyAcceptor" meta="0" nbt='{inv:{},orientation_up:"UP",id:"BlockEnergyAcceptor",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockController" meta="1" nbt='{inv:{},proxy:{p:0,g:6L,k:-1L},orientation_up:"UP",id:"BlockController",orientation_forward:"EAST",internalCurrentPower:0.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyController" meta="1" nbt='{inv:{},proxy:{p:0,g:11L,k:-1L},orientation_up:"UP",id:"BlockCreativeEnergyController",orientation_forward:"EAST",internalCurrentPower:"9.22337203685477E14d"}' scale="4" />

   <BlockImage id="appliedenergistics2:tile.BlockCableBus" nbt='{__guidenh_encoded_keys_v1:[0:{v:{id:"appliedenergistics2:item.ItemMultiPart",Count:1b,Damage:36s},k:"def:6"},1:{v:{id:"appliedenergistics2:item.ItemMultiPart",Count:1b,Damage:690s},k:"def:1"},2:{v:{},k:"extra:6"},3:{v:{},k:"extra:1"}],id:"BlockCableBus",hasRedstone:2}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockVibrationChamber" meta="0" nbt='{inv:{item0:{}},proxy:{p:0,g:12L,k:-1L},burnSpeed:100,orientation_up:"UP",burnTime:0.0d,id:"BlockVibrationChamber",maxBurnTime:0.0d,orientation_forward:"NORTH"}' scale="4" />
</Row>

AE2は内部的にはFE、RF、EUといった規格を使用していません。代わりに引き入れるときに独自の規格であるAEに変換しています。この変換は一方向で、GTNHではAEをEUに変換することはできません。AE以外の電力は、<ItemLink id="appliedenergistics2:tile.BlockEnergyAcceptor" showIcon="left" />や<ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" />によって変換できますが、コントローラーの面は専ら[チャンネル](./channels.md)に充てた方が良いでしょう。外部から電力を引き入れることに他に、<ItemLink id="appliedenergistics2:item.ItemMultiPart:690" showIcon="left" />や<ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyController" showIcon="left" />を使用することでAEを無限にできます。

<GameScene zoom="3" rotateY={200} width="400">
    <ImportStructure src="../assets/structures/energy_receive.snbt" />
</GameScene>
<ItemLink id="appliedenergistics2:tile.BlockVibrationChamber" showIcon="left" />で発電することもできますが、AE2は主にGregTechやIndustrialCraft 2のような他の工業MODで発電するように設計されています。

そのため、拠点の電力基盤を整える際、AE2ネットワークは、電力を大量消費するマルチブロックとして捉える方が良いでしょう。

AEへの変換比率：

*   2 FE/RF = 1 AE
*   1 EU  = 2 AE

## Energy Storage

<Row>
  <BlockImage id="appliedenergistics2:tile.BlockEnergyCell" meta="7" nbt='{proxy:{p:0,g:14L,k:-1L},id:"BlockEnergyCell",internalCurrentPower:200000.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockDenseEnergyCell" meta="7" nbt='{proxy:{p:0,g:15L,k:-1L},id:"BlockDenseEnergyCell",internalCurrentPower:1600000.0d}' scale="4" />

  <BlockImage id="appliedenergistics2:tile.BlockCreativeEnergyCell" scale="4" />
</Row>

明らかですが、ネットワークは1Tickの間には蓄電量以上の電力を受け入れたり消費したりすることはできません。800AEしか蓄電できないネットワークでは、端末は合計で800AEまでしか使えず、エネルギー受容体は1Tickに最大でも800AEまでしか引き入れられません。

これはおかしな挙動の原因の一つです。例えば、エネルギー受容体、ドライブ、ターミナルを一つづつ、そして少しの端末だけのネットワークがあったとして、インベントリいっぱいの丸石を挿入します。すると、ネットワークは十分な電力バッファが無いため、いくらかの丸石は挿入に失敗してネットワークは電力不足に陥り、その後再起動します。

これは[空間IO](./spatial_io.md)を使用するときに顕著です。なぜなら、[空間送信鉄塔](../items_blocks/spatial_pylon.md)のセットアップ開始には莫大な電力が必要なためです。これの解決策は、エネルギーセルの追加です。

* 全てのケーブル、端末などのパーツは25AEの蓄電量を持ちます。

* <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" />は8000AEの微小な蓄電量を持ちます。

* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" showIcon="left" />は200,000AEを蓄電できます。ほとんどの場合、これが一つあればピーク時の電力需要にも応えられます。

* <ItemLink id="appliedenergistics2:tile.BlockDenseEnergyCell" showIcon="left" />は1,600,000AEを蓄電できます。これは蓄えた電力だけでネットワークを稼働する際や、大規模な[空間IO](./spatial_io.md)の莫大な電力需要を叶えるために使用できます。

* <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyCell" showIcon="left" />はUHV以上の終盤のアイテムで、無制限の電力を供給します。

* <ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyController" showIcon="left" />は究極のMEコントローラーで、<ItemLink id="appliedenergistics2:tile.BlockController" showIcon="left" />と<ItemLink id="appliedenergistics2:tile.BlockCreativeEnergyCell" showIcon="left" />を1ブロックに纏めたものです。