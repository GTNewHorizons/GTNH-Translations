---
navigation:
  parent: ../tricks_example_index.md
  title: 레벨 이미터 자동 재고 보충
  icon: appliedenergistics2:item.ItemMultiPart:280
---

# 레벨 이미터 자동 재고 보충

"필요할 때마다 더 제작하면서 특정 아이템을 일정량 재고로 유지하려면 어떻게 해야 할까?"라는 의문이 생길 수 있습니다.

<ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />를 사용하여 네트워크의 [자동 제작](../ae2_mechanics/autocrafting.md)에 새 아이템을 자동으로 요청하는 방법이 있습니다. 이 설정은 한 가지 아이템을 대량으로 유지하기 위한 것입니다.

물론 레벨 이미터와 레드스톤 카드를 제외하여 네트워크에서 아이템을 계속 제작하도록 만들 수도 있습니다.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
  (1) 수출 버스: 원하는 아이템으로 필터링합니다. 레드스톤 카드와 제작 카드가 장착되어 있습니다. 레드스톤 모드는
  "신호가 있으면 활성화", 제작 동작은 "비축된 아이템을 사용하지 않음"으로 설정합니다.
  <Row><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:26" scale="2" /> <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
  (2) 레벨 이미터: 원하는 아이템과 수량으로 설정하고, "수량이 제한보다 적을 때 신호 출력"으로 설정합니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
  (3) 인터페이스: 기본 설정으로 둡니다.
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  주 네트워크로
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" /> (1)은 원하는 아이템으로 필터링합니다. 레드스톤 카드와 제작 카드가 장착되어 있습니다.
  "레드스톤 모드"는 "신호가 있으면 활성화", "제작 동작"은 "비축된 아이템을 사용하지 않음"으로 설정합니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" /> (2)는 원하는 아이템과 수량으로 설정하고, "수량이 제한보다 적을 때 신호 출력"으로 설정합니다.
* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (3)은 기본 설정으로 둡니다.

## 작동 방식

1. [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에 있는 원하는 아이템의 수량이 <ItemLink id="appliedenergistics2:item.ItemMultiPart:280" />에 지정된 수량보다 적으면 레드스톤 신호를 출력합니다.
2. 레드스톤 신호를 받으면 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />이 있고 비축된 아이템을 사용하지 않도록 설정되어 있으므로, <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />이 네트워크의 [자동 제작](../ae2_mechanics/autocrafting.md)에 원하는 아이템을 더 제작하도록 요청한 다음 해당 아이템을 내보냅니다.
3. <ItemLink id="appliedenergistics2:tile.BlockInterface" />에 아이템이 주입되고 내부 인벤토리에 어떤 아이템도 보관하도록 설정되어 있지 않으면, 해당 아이템을 네트워크 저장소로 밀어 넣습니다.