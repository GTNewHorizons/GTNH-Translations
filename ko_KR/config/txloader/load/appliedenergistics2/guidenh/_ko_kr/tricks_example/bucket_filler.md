---
navigation:
  parent: ../tricks_example_index.md
  title: 양동이 채우기 장치
  icon: minecraft:water_bucket
---

# 양동이 채우기 장치

[양동이 비우기 장치](bucket_emptier.md)도 참고하십시오.

<ItemLink id="appliedenergistics2:tile.BlockInterface" />를 사용하므로 [자동 제작](../ae2_mechanics/autocrafting.md) 구성에 통합하도록 만들어졌다는 점에 유의하십시오.

때로는 생활이 불편하여 유체 자체가 아닌 유체가 담긴 양동이가 필요할 때가 있습니다. 경우에 따라 기계가 이를 대신해 줄 수도 있습니다
(예: Thermal Expansion의 유체 변환기). 하지만 언제나 편리하게 처리해 주는 모드가 설치되어 있으리라는 보장은 없습니다. 다행히도
바닐라 Minecraft에는 조금 덜 편리하지만 이를 처리할 방법인 <ItemLink id="minecraft:dispenser" />가 있습니다.

**다만 [패턴 인코딩 터미널](../items_blocks/terminals.md#pattern-encoding-terminal)의 유체 대체 기능을 사용하면
양동이 대신 유체 자체를 제작법에 사용할 수 있으므로, 이러한 과정을 거칠 필요가 없는 경우가 많다는 점에 유의하십시오.**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/structures/bucket_filler.snbt" />

  <BoxAnnotation color="#dddddd" min="2 1 0" max="3 2 1">
  (1) ME 인터페이스: 관련 처리 패턴을 넣고 제작 잠금을 "레드스톤 신호가 있을 때"로 설정합니다.

  <Row>
    <FloatingImage src="../assets/images/water_fill_pattern.png" displayWidth="150" />
    <FloatingImage src="../assets/images/lava_fill_pattern.png" displayWidth="150" />
  </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1.1 0.1" max="3.2 1.9 0.9">
  (2) 인터페이스: 기본 설정입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.1 1.1 0.8" max="3.9 1.9 1">
  (3) 저장 버스 #1: 기본 설정입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.05 1.05 0.8" max="4.95 1.95 1">
  (4) 형성 평면: 반전 카드를 사용하여 양동이를 블랙리스트로 필터링합니다.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3.2 2 1.2" max="3.8 2.2 1.8">
  (5) 입력 버스: 반전 카드를 사용하여 양동이를 블랙리스트로 필터링합니다.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.1 2 0.1" max="2.9 2.2 0.9">
  (6) 저장 버스 #2: 기본 설정입니다.
  </BoxAnnotation>

  <DiamondAnnotation pos="0 1.5 0.5" color="#00ff00">
  주 네트워크로
  </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1)에 관련 <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />을 넣고 제작 잠금을 "레드스톤 신호가 있을 때"로 설정합니다.
  
    ![충전기 패턴](../assets/images/water_fill_pattern.png)
    ![충전기 패턴](../assets/images/lava_fill_pattern.png)

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (2)는 기본 설정입니다.
* 첫 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3)는 기본 설정입니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" /> (4)는 반전 카드를 사용하여 양동이를 블랙리스트로 필터링합니다.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (5)는 반전 카드를 사용하여 양동이를 블랙리스트로 필터링합니다.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="appliedenergistics2:item.ItemMultiMaterial:31" scale="2" /></Row>
* 두 번째 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (6)는 기본 설정입니다.

## 작동 원리

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />가 재료를 인터페이스 안으로 밀어 넣습니다.
   (실제로는 최적화를 위해 저장 버스와 형성 평면을 공급자의 면이 확장된 것처럼 통과하여 직접 밀어 넣습니다. 재료가 실제로 인터페이스 안으로 들어가지는 않습니다.)
2. [파이프 서브넷](pipe_subnet.md#providing-to-multiple-places)에 설명된 방식과 <ItemLink id="appliedenergistics2:item.ItemMultiPart:320" />를 통해
   양동이는 <ItemLink id="minecraft:dispenser" /> 안으로 들어가고, 형성 평면이 유체를 배치합니다.
3. <ItemLink id="minecraft:comparator" />가 발사기 안의 양동이를 감지하여 발사기에 전력을 공급하는 동시에 ME 인터페이스를 잠급니다.
4. 발사기가 양동이로 유체를 퍼 올리면 발사기 안에 유체가 담긴 양동이가 들어 있게 됩니다.
5. <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />가 발사기에서 유체가 담긴 양동이를 꺼내고,
   <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />를 통해 ME 인터페이스에 저장하여 주 네트워크로 돌려보냅니다.
6. 비교기가 발사기가 비어 있음을 감지하여 공급자의 잠금을 해제합니다.