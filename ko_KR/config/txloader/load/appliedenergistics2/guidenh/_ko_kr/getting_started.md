---
navigation:
  title: 시작하기
  position: 10
  parent: /index.md
---

# 빠른 시작

# 간단한 저장 네트워크
AE2를 쉽게 시작하려면 먼저 AE2의 기본 기능인 저장을 구현할 수 있는 간단한 저장 네트워크를 구축해 보겠습니다.

## 사전 준비
Applied Energistics 2는 사실상 외계 기술입니다. 세계 곳곳에 흩어져 있는 [운석](./ae2_mechanics/meteorites.md)을 찾을 수 있습니다. 운석 중심에는 <ItemLink id="appliedenergistics2:tile.BlockSkyChest" showIcon="true"/>가 있을 수 있습니다. 이 상자 안에서는 AE2의 핵심 아이템인 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:13" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:14" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:15" showIcon="true"/>, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:19" showIcon="true"/>를 얻을 수 있습니다. AE2의 부품과 블록을 제작하려면 이 아이템들이 필요합니다. GTNH에서는 AE2가 GregTech에도 통합되어 있으므로 AE 시스템을 구축하려면 먼저 EV 티어에 도달하고 티타늄을 얻어야 합니다.

## 재료
AE 시스템을 구축하는 데 필요한 기술 수준에 도달하면 다음 재료도 필요합니다.
- <ItemImage id="gregtech:gt.blockores2:516" label="right"/>
  - 여기에서 <ItemImage id="gregtech:gt.metaitem.01:2516"  label="right"/> 및 <ItemImage id="gregtech:gt.metaitem.01:8516" label="right"/>를 얻어야 합니다. 이들은 AE 아이템과 블록을 제작하는 데 중요한 원재료입니다.
- <ItemImage id="gregtech:gt.blockores2:28" label="right"/>
  - 많은 AE 블록을 제작하려면 <ItemImage id="gregtech:gt.metaitem.01:17028" label="right" />가 필요합니다.
- <ItemImage id="minecraft:redstone" label="right" />, <ItemImage id="minecraft:diamond" label="right"/>, <ItemImage id="dreamcraft:CircuitHV"  label="right"/>와 같은 기타 기본 재료도 필요합니다. EV 티어로 진행하는 동안 이미 이 재료들을 접했을 것이므로 여기서는 자세히 설명하지 않겠습니다.

## 건설
모든 준비가 끝났다면 아래와 같이 간단한 저장 네트워크를 구축해 보겠습니다. 다음 장면을 구성해야 합니다.

<GameScene zoom="5" interactive={true} width="400" height="300">
  <ImportStructure src="../assets/structures/getting_started.snbt" />
  <IsometricCamera yaw="200" pitch="30" />
  <BlockAnnotation pos="5 0 0" color="#e5e90c" alwaysOnTop={true}>
  <Color color="#e5e90c">이것은 시연을 위해 배치된 디버그 발전기이며, 서바이벌 모드에서는 얻을 수 없습니다. 일반적으로 사용하려면 전력망에 연결하십시오.</Color>
  </BlockAnnotation>
</GameScene>

장면의 AE 시스템은 왼쪽에 있는 GT 전력망에서 전력을 공급받습니다. 이 AE 시스템은 다음과 같은 기본 아이템 저장 기능을 구현합니다.
- <ItemLink id="appliedenergistics2:tile.BlockController" showIcon="true"/>는 전체 네트워크에 [채널](./ae2_mechanics/channels.md)을 제공합니다.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:36" showIcon="true"/>는 네트워크의 모든 구성 요소를 연결합니다.
- 저장 공간을 제공하기 위해 <ItemLink id="appliedenergistics2:item.ItemBasicStorageCell.1k" showIcon="true"/>를 <ItemLink id="appliedenergistics2:tile.BlockDrive" showIcon="true"/> 안에 넣습니다.
- 상자의 저장 공간을 AE 네트워크에 통합하려면 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" showIcon="true"/>를 상자에 부착합니다.
- <ItemLink id="appliedenergistics2:item.ItemMultiPart:380" showIcon="true"/>는 플레이어가 AE 네트워크의 내부 저장 공간과 상호작용할 수 있는 채널을 제공합니다.

이제 터미널을 마우스 오른쪽 버튼으로 클릭하여 AE 저장 네트워크를 열 수 있습니다. 일반적으로 상자를 사용하는 것처럼 터미널에 아이템을 넣거나 꺼낼 수 있습니다. 상자에 직접 넣은 아이템도 AE 터미널에 표시됩니다. 이로써 AE 저장 네트워크를 성공적으로 구축했지만, 이는 AE 네트워크라는 빙산의 일각에 불과합니다. 더 많은 내용을 확인하려면 이 가이드를 계속 살펴보십시오.

[아이템과 블록](items_blocks_index.md)

[AE2 메커니즘](ae2_mechanics_index.md)

[팁과 실용적인 예시](tricks_example_index.md)