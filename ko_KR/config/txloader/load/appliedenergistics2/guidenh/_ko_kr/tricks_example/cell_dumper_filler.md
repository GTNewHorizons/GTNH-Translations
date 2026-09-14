---
navigation:
  parent: ../tricks_example_index.md
  title: 셀 비우기 또는 채우기
  icon: appliedenergistics2:tile.BlockIOPort
---

# 셀 비우기 또는 채우기

다음과 같이 궁금할 수 있습니다. "셀의 내용물을 상자나 서랍 배열 또는 배낭에 빠르게 비우거나, 반대로 같은 방식으로 셀을 채우려면 어떻게 해야 할까요?"

해답은 <ItemLink id="appliedenergistics2:tile.BlockIOPort" />과 아이템을 넣거나 가져올 위치를 제한하기 위한 서브넷 구성입니다.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/cell_dumper_filler.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 1">
  (1) IO 포트: GUI 중앙의 화살표 버튼을 사용하여 "네트워크로 데이터 전송" 또는 "저장 셀로 데이터 전송" 중 하나로 설정할 수 있습니다.
  가속 카드 3개가 설치되어 있습니다.
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:30" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0.7 0" max="1 1 1">
  (2) 저장 버스: 기본 설정 상태입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="0 1 0" max="1 2 1">
  채우거나 비우려는 것을 이곳에 놓습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 0.35 0.35" max="2.3 0.65 0.65">
  석영 섬유: 에너지원이 다른 네트워크일 때만 필요합니다.
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 0.5" color="#00ff00">
  다른 네트워크나 에너지 수용기와 같은 에너지원에 연결합니다.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:tile.BlockIOPort" /> (1)은 GUI 중앙의 화살표 버튼을 사용하여 "네트워크로 데이터 전송" 또는 "저장 셀로 데이터 전송" 중 하나로 설정할 수 있습니다.
  최대 속도를 위해 가속 카드 3개가 설치되어 있습니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2)은 기본 설정 상태입니다.

## 작동 방식

### "네트워크로 전송" 모드

1. <ItemLink id="appliedenergistics2:tile.BlockIOPort" />은 삽입된 [저장 셀](../items_blocks/storage_cells.md)의 내용물을 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)로 비우려고 합니다.
2. 서브넷에 있는 유일한 저장소는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />이며, 앞에 놓은 곳에 따라 아이템이나 유체 등을 저장합니다.
* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" />은 [에너지](../ae2_mechanics/energy.md)를 충분히 비축하여, 게임 틱마다 수많은 아이템을 전송하는 데 전력을 소모하더라도 네트워크의 에너지가 고갈되지 않도록 합니다.

### "저장 셀로 전송" 모드

1. <ItemLink id="appliedenergistics2:tile.BlockIOPort" />은 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)의 내용물을 삽입된 [저장 셀](../items_blocks/storage_cells.md)로 비우려고 합니다.
2. 서브넷에 있는 유일한 저장소는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />이며, 앞에 놓은 곳에서 아이템이나 유체 등을 가져옵니다.
* <ItemLink id="appliedenergistics2:tile.BlockEnergyCell" />은 [에너지](../ae2_mechanics/energy.md)를 충분히 비축하여, 게임 틱마다 수많은 아이템을 전송하는 데 전력을 소모하더라도 네트워크의 에너지가 고갈되지 않도록 합니다.