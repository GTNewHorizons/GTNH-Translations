---
navigation:
  parent: ../tricks_example_index.md
  title: 화로 자동화
  icon: minecraft:furnace
---

# 화로 자동화

이 방법은 <ItemLink id="appliedenergistics2:tile.BlockInterface" />를 사용하므로 [자동 제작](../ae2_mechanics/autocrafting.md) 구성에 통합하는 것을 전제로 합니다. 화로를 독립적으로 자동화하려는 경우에는 호퍼와 상자 등을 사용하면 됩니다.

<ItemLink id="minecraft:furnace" />의 자동화는 [충전기](charger_automation.md)처럼 단순한 기계의 자동화보다 조금 더 복잡합니다. 화로에는 서로 다른 두 면에서 아이템을 입력하고, 세 번째 면에서 아이템을 추출해야 합니다. 제련할 아이템은 위쪽 면으로 밀어 넣어야 하며, 연료는 측면으로 밀어 넣고, 결과물은 아래쪽으로 꺼내야 합니다.

위쪽에 <ItemLink id="appliedenergistics2:tile.BlockInterface" />를 설치하고, 측면에 연료를 계속 밀어 넣는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />를 설치하며, 아래쪽에 결과물을 네트워크로 가져오는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />를 설치하는 방식으로 구현할 수 있습니다. 그러나 이 방법은 [채널](../ae2_mechanics/channels.md)을 3개 사용합니다.

채널 1개만 사용하여 구현하는 방법은 다음과 같습니다.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/furnace_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
  (1) ME 인터페이스: 서투스 석영 렌치를 사용한 방향형 변형이며, 관련 처리 패턴이 설정되어 있습니다.

  <FloatingImage src="../assets/images/furnace_pattern.png" displayWidth="150" title="Iron Pattern" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
  (2) 인터페이스: 기본 설정입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
  (3) 저장 버스 1번: 석탄으로 필터링되어 있습니다.
  <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
  (4) 저장 버스 2번: 반전 카드를 사용하여 석탄을 블랙리스트로 필터링합니다.
  <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  주 네트워크로
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1)은 관련 <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />이 설정된 기본 구성입니다.
    석영 렌치를 사용하면 방향을 지정할 수 있습니다.

  ![철 패턴](../assets/images/furnace_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2)는 기본 구성입니다.
* 첫 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3)는 석탄 또는 사용하려는 연료로 필터링되어 있습니다.
* 두 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (4)는 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:31" />을 사용하여 현재 사용하는 연료를 블랙리스트로 필터링합니다.

## 작동 원리

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />가 재료를 인터페이스 안으로 밀어 넣습니다.
   (실제로는 최적화를 위해 저장 버스를 공급기의 면을 확장한 것처럼 취급하여, 저장 버스를 통해 직접 밀어 넣습니다. 아이템이 실제로 인터페이스 안으로 들어가지는 않습니다.)
2. 인터페이스는 아무것도 저장하지 않도록 설정되어 있으므로 재료를 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)로 밀어 넣으려고 합니다.
3. 초록색 서브넷에 있는 유일한 저장소는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />입니다. 석탄으로 필터링된 버스는 측면을 통해 석탄을 화로의 연료 슬롯에 넣습니다.
    석탄이 아닌 것으로 필터링된 버스는 위쪽 면을 통해 제련할 아이템을 위쪽 슬롯에 넣습니다.
4. 화로가 제련 작업을 수행합니다.
5. 호퍼가 화로의 아래쪽에서 결과물을 꺼내 공급기의 반환 슬롯에 넣고, 결과물을 주 네트워크로 돌려보냅니다.