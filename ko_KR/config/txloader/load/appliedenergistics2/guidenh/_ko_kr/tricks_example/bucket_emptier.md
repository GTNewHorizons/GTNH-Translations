---
navigation:
  parent: ../tricks_example_index.md
  title: 양동이 비우개
  icon: minecraft:bucket
---

# 양동이 비우개

[양동이 채우개](bucket_filler.md)도 참고하십시오.

<ItemLink id="appliedenergistics2:tile.BlockInterface" />를 사용하므로 [자동 제작](../ae2_mechanics/autocrafting.md) 설비에 통합하여 사용하도록 설계되었습니다.

때로는 불편한 상황이 발생하여 유체 자체가 필요하지만, 유체를 양동이에 담긴 형태로만 만들 수 있을 때가 있습니다. 어떤 기계는 이러한 작업을 대신해 주기도 합니다
(예: Thermal Expansion의 유체 변환기). 하지만 언제나 편리하게 처리해 주는 모드가 설치되어 있으리라는 보장은 없습니다. 다행히도
바닐라 Minecraft에는 조금 덜 편리하지만 이러한 작업을 수행하는 방법이 있으며, 바로 <ItemLink id="minecraft:dispenser" />입니다.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/bucket_emptier.snbt" />

  <BoxAnnotation color="#dddddd" min="2 1 0" max="3 2 1">
  (1) ME 인터페이스: "레드스톤 신호가 있을 때" 제작 잠금으로 설정하고 차단 모드를 켠 뒤, 관련 가공 패턴을 넣습니다.

  <Row>
    <FloatingImage src="../assets/images/water_empty_pattern.png" displayWidth="150" />
    <FloatingImage src="../assets/images/lava_empty_pattern.png" displayWidth="150" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.1 2 0.1" max="2.9 2.2 0.9">
  (2) 인터페이스: 기본 설정입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.1 2 1.1" max="3.9 2.2 1.9">
  (3) 저장 버스 1번: 기본 설정입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.05 1.05 0.8" max="4.95 1.95 1">
  (4) 소멸 평면: 설정할 GUI가 없습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.2 1.2 0.8" max="3.8 1.8 1">
  (5) 가져오기 버스: 양동이로 필터링되어 있습니다.
  <ItemImage id="minecraft:bucket" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1.1 0.1" max="3.2 1.9 0.9">
  (6) 저장 버스 2번: 기본 설정입니다.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 1.5 0.5" color="#00ff00">
  주 네트워크로
  </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1)은 "레드스톤 신호가 있을 때" 제작 잠금으로 설정하고 차단 모드를 켠 뒤,
  관련 <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />을 넣습니다.
  
    ![충전기 패턴](../assets/images/water_empty_pattern.png)
    ![충전기 패턴](../assets/images/lava_empty_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2)는 기본 설정입니다.
* 첫 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3)은 기본 설정입니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:300" /> (4)은 GUI가 없으며 설정할 수 없습니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (5)는 양동이로 필터링되어 있습니다.
  <ItemImage id="minecraft:bucket" scale="2" />
* 두 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (6)은 기본 설정입니다.

## 작동 방식

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />가 재료를 인터페이스로 밀어 넣습니다.
   (실제로는 최적화를 위해 공급기의 면에 연결된 확장 기능인 것처럼 저장 버스를 통해 직접 밀어 넣습니다. 따라서 아이템이 실제로 인터페이스 안으로 들어가지는 않습니다.)
2. [파이프 서브넷](pipe_subnet.md#providing-to-multiple-places)에 설명된 메커니즘을 통해 양동이가 <ItemLink id="minecraft:dispenser" />에 들어갑니다.
3. <ItemLink id="minecraft:comparator" />가 디스펜서 안의 양동이를 감지하여 디스펜서에 전원을 공급하는 동시에 ME 인터페이스를 잠급니다.
4. 디스펜서가 양동이에서 유체를 내보내면, 디스펜서 안에는 빈 양동이가 남습니다.
5. <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />가 디스펜서에서 빈 양동이를 꺼낸 뒤, <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />를 통해 ME 인터페이스에 저장하여 주 네트워크로 돌려보냅니다.
6. 비교기가 디스펜서가 비어 있는 것을 감지하면 공급기의 잠금이 해제됩니다.