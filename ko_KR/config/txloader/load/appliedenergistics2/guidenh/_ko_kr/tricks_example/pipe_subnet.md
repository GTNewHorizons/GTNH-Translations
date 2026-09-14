---
navigation:
  parent: /tricks_example_index.md
  title: 아이템/유체 "파이프" 서브넷
  icon: appliedenergistics2:item.ItemMultiPart:220
---

# 아이템/유체 "파이프" 서브넷

AE2 [장치](../ae2_mechanics/devices.md)를 사용하여 아이템 및 유체 파이프를 간단하게 구현하는 방법입니다. 아이템이나 유체 파이프를 사용할 만한 모든 상황에서 유용합니다.
여기에는 조합 결과를 <ItemLink id="appliedenergistics2:tile.BlockInterface" />로 반환하는 것도 포함됩니다.

일반적으로 이를 구현하는 방법은 두 가지입니다.

## 임포트 버스 -> 저장 버스

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) 임포트 버스: 필터를 설정할 수 있습니다.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) 저장 버스: 필터를 설정할 수 있습니다. 이 저장 버스와 목적지로 사용하려는 다른 저장 버스는
    네트워크에서 유일한 저장소여야 합니다.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    원본
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    목적지
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

원본 인벤토리에 연결된 <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (1)는 아이템이나 유체를 임포트한 후 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에 저장하려고 합니다.
네트워크에서 유일한 저장소가 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (2)이므로(이것이 주 네트워크가 아닌 서브넷을 사용하는 이유입니다), 아이템이나 유체가 목적지 인벤토리에 들어가 전송됩니다. 에너지는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" />를 통해 공급됩니다.
임포트 버스와 저장 버스 모두 필터를 설정할 수 있지만, 필터를 설정하지 않으면 접근할 수 있는 모든 것을 전송합니다.
이 구성은 여러 개의 임포트 버스와 저장 버스에도 사용할 수 있습니다.

## 저장 버스 -> 익스포트 버스

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/storage_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    (1) 저장 버스: 필터를 설정할 수 있습니다. 이 저장 버스와 원본으로 사용하려는 다른 저장 버스는
    네트워크에서 유일한 저장소여야 합니다.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    (2) 익스포트 버스: 반드시 필터를 설정해야 합니다.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
    원본
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
    목적지
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

목적지 인벤토리에 연결된 <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />는 필터에 설정된 아이템을 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에서 가져오려고 합니다.
네트워크에서 유일한 저장소가 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />이므로(이것이 주 네트워크가 아닌 서브넷을 사용하는 이유입니다), 아이템이나 유체가 원본 인벤토리에서 가져와져 전송됩니다. 에너지는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:140" />를 통해 공급됩니다.
익스포트 버스는 작동하려면 반드시 필터를 설정해야 하므로, 익스포트 버스에 필터를 설정해야만 이 구성이 작동합니다.
이 구성은 여러 개의 저장 버스와 익스포트 버스에도 사용할 수 있습니다.

## 작동하지 않는 구성 (임포트 버스 -> 익스포트 버스)

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_export_pipe.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dd3333" thickness="1">
    임포트 버스: 네트워크에 저장소가 없으므로 임포트할 대상이 없습니다.
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dd3333" thickness="1">
    (2) 익스포트 버스: 네트워크에 저장소가 없으므로 익스포트할 것이 없습니다.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
    원본
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
    목적지
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

임포트 버스와 익스포트 버스만으로 구성된 구성은 작동하지 않습니다. 임포트 버스는 원본 인벤토리에서 아이템이나 유체를 가져와 네트워크 저장소에 저장하려고 합니다. 익스포트 버스는 네트워크 저장소에서 아이템이나 유체를 가져와 목적지 인벤토리에 넣으려고 합니다. 그러나 이 네트워크에는 **저장소가 없으므로**, 임포트 버스는 임포트할 수 없고 익스포트 버스는 익스포트할 수 없어 아무 일도 일어나지 않습니다.

## 한 면을 통한 입력 및 출력

입력을 받을 수 있고 한 면을 통해 출력을 가져올 수 있는 기계가 있다고 가정해 보겠습니다. (<ItemLink id="appliedenergistics2:tile.BlockCharger" />와 같은 기계입니다.)
두 가지 파이프 서브넷 방법을 결합하면 재료를 밀어 넣고 결과를 꺼낼 수 있습니다.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/import_storage_export_pipe.snbt" />
  <BoxAnnotation min="4 1 1" max="5 1.3 2" color="#dddddd" thickness="1">
    (1) 임포트 버스: 필터를 설정할 수 있습니다.
  </BoxAnnotation>
  <BoxAnnotation min="2 1 1" max="3 1.3 2" color="#dddddd" thickness="1">
    (2) 저장 버스: 필터를 설정할 수 있습니다. 이 저장 버스와 아이템을 밀어 넣고 꺼내려는 다른 저장 버스는
    네트워크에서 유일한 저장소여야 합니다.
  </BoxAnnotation>
  <BoxAnnotation min="2 0 1" max="3 1 2" color="#dddddd" thickness="1">
    (3) 아이템을 밀어 넣고 꺼내려는 대상: 여기서는 충전기입니다.
  </BoxAnnotation>
  <BoxAnnotation min="0 1 1" max="1 1.3 2" color="#dddddd" thickness="1">
    (4) 익스포트 버스: 반드시 필터를 설정해야 합니다.
  </BoxAnnotation>
  <DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
    원본
  </DiamondAnnotation>
  <DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
    목적지
  </DiamondAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 인터페이스

임포트 버스와 익스포트 버스 외에도 아이템을 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에 넣고 꺼낼 수 있는 [장치](../ae2_mechanics/devices.md)가 있습니다!
여기서 중요한 것은 <ItemLink id="appliedenergistics2:tile.BlockInterface" />입니다. 인터페이스에 재고로 설정되지 않은 아이템이 삽입되면 인터페이스는 해당 아이템을 네트워크 저장소로 밀어 넣습니다. 이를 임포트 버스 -> 저장 버스 파이프와 비슷한 방식으로 활용할 수 있습니다. 인터페이스의 재고에 아이템을 설정하면 저장 버스 -> 익스포트 버스 파이프와 비슷하게 네트워크 저장소에서 해당 아이템을 가져옵니다. 인터페이스마다 재고로 설정할 것과 설정하지 않을 것을 지정할 수 있으므로, 어떤 이유로든 원한다면 저장 버스를 통해 원격으로 아이템을 넣고 꺼낼 수 있습니다.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/interface_pipes.snbt" />
  <BoxAnnotation min="3.7 0 0" max="4 1 1" color="#dddddd" thickness="1">
    인터페이스
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 1" color="#dddddd" thickness="1">
    저장 버스
  </BoxAnnotation>
  <BoxAnnotation min="3.7 0 2" max="4 1 3" color="#dddddd" thickness="1">
    저장 버스
  </BoxAnnotation>
  <BoxAnnotation min="0 1 2" max="1 1.3 3" color="#dddddd" thickness="1">
    인터페이스
  </BoxAnnotation>
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## 일대다 및 다대일 (그리고 다대다)

물론 <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />나 <ItemLink id="appliedenergistics2:item.ItemMultiPart:260" />, <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />을 하나만 사용할 필요는 없습니다.

<GameScene zoom="3" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/many_to_many_pipe.snbt" />
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>

## 여러 장소에 공급하기

지금까지의 내용을 바탕으로 하나의 <ItemLink id="appliedenergistics2:tile.BlockInterface" />에서 여러 장소로 재료를 보내는 방법을 알아낼 수 있습니다.
예를 들어 여러 기계로 구성된 배열이나 한 기계의 여러 면에 보낼 수 있습니다.

<GameScene zoom="6" showBackground={false} interactive={false}>
  <ImportStructure src="../assets/structures/fluid_interface_storage.snbt" />
  <BoxAnnotation min="2.7 0 1" max="3 1 2" color="#dddddd" thickness="1">
    인터페이스 (평평한 형태여야 하며, 전체 블록이어서는 안 됩니다)
  </BoxAnnotation>
  <BoxAnnotation min="1 0 0" max="1.3 1 4" color="#dddddd" thickness="1">
    저장 버스
  </BoxAnnotation>
  <BoxAnnotation min="0 0 0" max="1 1 4" color="#dddddd" thickness="1">
    패턴을 공급하려는 장소 (여러 기계 또는 한 기계의 여러 면)
  </BoxAnnotation>
  <IsometricCamera yaw="185" pitch="30" />
</GameScene>