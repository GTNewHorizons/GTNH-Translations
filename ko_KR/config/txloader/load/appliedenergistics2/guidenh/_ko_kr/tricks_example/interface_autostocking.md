---
navigation:
  parent: ../tricks_example_index.md
  title: 인터페이스 자동 재고 보충
  icon: appliedenergistics2:tile.BlockInterface
---

# 인터페이스 자동 재고 보충

"다양한 아이템을 일정량 재고로 유지하면서, 필요할 때 더 제작하려면 어떻게 해야 합니까?"라고 질문할 수 있습니다.

한 가지 방법은 <ItemLink id="appliedenergistics2:tile.BlockInterface" />와 <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />를 사용하여 네트워크의 [자동 제작](../ae2_mechanics/autocrafting.md)에 새 아이템을 자동으로 요청하는 것입니다. 이 구성은 다양한 아이템을 소량씩 유지하는 데 더 적합합니다.

이 시연용 구성은 너무 넓어지지 않도록 일부만 만들었지만, 일반 [케이블](../items_blocks/cables.md)의 [채널](../ae2_mechanics/channels.md) 8개를 모두 사용하려면 <ItemLink id="appliedenergistics2:tile.BlockInterface" /> 4개와 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> 4개를 사용하는 것이 가장 효율적일 가능성이 높습니다.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/interface_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
  (1) 인터페이스: 원하는 아이템을 내부에 유지하도록 설정합니다. 제작 카드가 들어 있습니다.
  <ItemImage id="appliedenergistics2:item.ItemMultiMaterial:53" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
  (2) 저장 버스: "입출력 모드"를 "추출만"으로 설정합니다.
  </BoxAnnotation>

  <DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
  주 네트워크로
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 구성

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1)는 원하는 아이템을 내부에 유지하도록 설정합니다. 원하는 아이템을 상단 슬롯에 클릭하거나 NEI에서 상단 슬롯으로 끌어 넣은 다음, 슬롯 위의 렌치 아이콘을 클릭하여 수량을 설정합니다. 제작 카드가 들어 있습니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2)는 "입출력 모드"가 "추출만"으로 설정되도록 구성합니다.

## 작동 원리

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />가 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에서 설정된 아이템을 충분히 가져올 수 없고, <ItemLink id="appliedenergistics2:item.ItemMultiMaterial:53" />가 들어 있다면 네트워크의 [자동 제작](../ae2_mechanics/autocrafting.md)에 해당 아이템을 더 제작하도록 요청합니다.
2. <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />를 통해 네트워크가 인터페이스의 내용물에 접근할 수 있습니다.