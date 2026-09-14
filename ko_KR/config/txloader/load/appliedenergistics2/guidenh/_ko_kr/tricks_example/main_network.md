---
navigation:
  parent: ../tricks_example_index.md
  title: "주 네트워크" 예시
  icon: appliedenergistics2:tile.BlockController
---

# "주 네트워크" 예시

다른 많은 구성에서는 "주 네트워크"를 참조합니다. 또한 이 모든 [장치](../ae2_mechanics/devices.md)가 어떻게 기능하는 시스템으로 결합되는지 궁금할 수 있습니다. 다음은 한 가지 예시입니다.

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/structures/small_base_network.snbt" />

  <BoxAnnotation color="#33dd33" min="3 1 5" max="7 7 9">
  ME 인터페이스와 조립기를 크게 모아 두면 제작 패턴을 배치할 공간이 많이 생깁니다.
  체크무늬 배치를 사용하면 인터페이스가 여러 조립기를 병렬로 활용하면서도 전체 구성을 작게 유지할 수 있습니다.
  8개 단위로 그룹화하면 채널이 잘못 연결될 수 없습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 10 13" max="5 11 14">
  실제로 그렇게 큰 컨트롤러는 필요하지 않습니다. 다른 사람의 기지에서 보이는 거대한 고리와 정육면체 형태의 설계는
  대부분 멋있어 보이기 위한 것입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 12 13" max="4 13 14">
  모든 훌륭한 네트워크에는 에너지 셀이 있어야 합니다. 게임 틱당 더 많은 에너지를 입력하고
  전력 변동을 완화할 수 있기 때문입니다.
  </BoxAnnotation>
    
  <BoxAnnotation color="#33dd33" min="4 1 2" max="7 4 4">
  다른 모드의 전력원, 예를 들어 반응로나 태양광 패널, 발전기 등을 사용하는 것이 좋습니다.
  진동 챔버도 그럭저럭 괜찮지만, AE2는 모드팩에서 사용하도록 설계되었으므로 기지의 주 발전기를 사용하십시오.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 1 15" max="8 3 16">
  외장재를 사용하면 벽 뒤의 장치를 숨길 수 있습니다.
  </BoxAnnotation>
  <BoxAnnotation color="#33dd33" min="3 3 15" max="5 10 16">
  외장재를 사용하면 벽 뒤의 장치를 숨길 수 있습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8 9 13" max="10 10 14">
  일반 저장소에 드라이브 베이와 셀이 그렇게 많이 필요하지는 않습니다. 4k 또는 16k 셀을 장착한 드라이브
  2~4개 분량이면 거의 항상 충분합니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 13" max="7 11 14">
  대량 저장에는 특정 아이템으로 필터링한 대형 셀을 별도의 드라이브에 넣고, 더 높은 우선순위를 설정하는 것이 좋습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="3 9 10" max="4 13 11.7">
  인터페이스 기반 자동 보충입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 10 6" max="5 12 9">
  충전기 자동화 구성을 여러 충전기로 확장한 형태입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="2 9 2" max="5 10 5">
  파이프 서브넷을 사용하여 각인기를 연결하는 프로세서 자동화입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="6 9 3" max="7 11 4">
  파이프 서브넷을 사용하여 각인기를 연결하는 프로세서 자동화입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="8.2 9.2 7.2" max="8.8 10 7.8">
  무선 액세스 포인트는 범위가 구형이므로 가운데에 배치합니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 1 14" max="15 5 16">
  일반적으로 대규모 작업을 위한 대형 제작 CPU를 1~2개 두고, 대형 CPU가 사용 중일 때 보조 작업을 처리할
  소형 CPU를 몇 개 마련합니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="10 3 5" max="11 4 6">
  장치가 8개를 초과하는 경우, 서브넷에 자체 컨트롤러가 필요할 때도 있습니다. 예를 들어 8곳을 초과하는 장소로
  분배하는 경우가 그렇습니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="11 1 7" max="14 4 9">
  조약돌 농장입니다.
  </BoxAnnotation>

  <BoxAnnotation color="#33dd33" min="12 1 10.3" max="14.7 3.7 12.7">
  물에 던지기 자동화입니다.
  </BoxAnnotation>

  <IsometricCamera yaw="220" pitch="15" />
</GameScene>