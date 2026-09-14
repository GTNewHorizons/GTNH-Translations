---
item_ids:
  - gregtech:gt.blockmachines:15560
navigation:
  title: 부유 선별 셀 조절기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15560
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 부유 선별 셀 조절기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15560"/>
</GameScene>
<Color id="GREEN">부유 선별 셀 조절기(FCR)</Color>는 분쇄된 광석, 소나무 오일, 에틸 크산테이트 가루로부터 금속 부유물을 생산하는 LuV 티어 멀티블록입니다. 그런 다음 금속 부유물은 희귀 금속 복합재를 얻기 위해 진공로 또는 Utupu-Tanuri <ItemImage id="gregtech:gt.blockmachines:995"/>로 보내집니다. <Color id="GREEN">FCR</Color>은 처음 실행한 레시피에 영구적으로 고정되므로 한 종류의 재료만 처리할 수 있지만, 완벽한 오버클럭 덕분에 확장성이 좋습니다. 
<br clear="all"/>

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일합니다

## 건설
<Color id="GREEN">FCR</Color>에는 티어 부품이 없습니다. 버스/해치는 구조물 하단 층의 인코넬 강화 케이싱을 대체할 수 있습니다. 다중 앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 물은 구조물이 완성되면 무료로 생성되므로 수동으로 설치할 필요가 없습니다. 구조물을 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오. 

### 필요 항목:
- 1개 <ItemLink id="gregtech:gt.blockmachines:15560"/><ItemImage id="gregtech:gt.blockmachines:15560"/>
- 90-121개 <ItemLink id="miscutils:gtplusplus.blockcasings.3:1"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:1"/>
- 31개 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:9"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:9"/>
- 20개 <ItemLink id="miscutils:blockFrameGtStaballoy"/><ItemImage id="miscutils:blockFrameGtStaballoy"/>
- 8개 <ItemLink id="miscutils:blockFrameGtInconel690"/><ItemImage id="miscutils:blockFrameGtInconel690"/>
- 1개 이상 에너지 해치(하단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1개 유지보수 해치(하단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 입력 버스(하단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치(하단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 해치(하단 케이싱 중 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">FCR</Color>은 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계 사이에 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">FCR</Color>은 분쇄된 광석, 소나무 오일, 에틸 크산테이트 가루로부터 금속 부유물을 생산하는 데에만 사용됩니다. 그런 다음 금속 부유물은 희귀 금속 복합재를 얻기 위해 진공로 또는 Utupu-Tanuri로 보내집니다. 소나무 오일과 에틸 크산테이트 가루는 둘 다 ExxonMobil 화학 공장 <ItemImage id="gregtech:gt.blockmachines:998"/>에서 제조됩니다. 두 레시피는 충돌하지 않으므로 같은 기계에서 제조할 수 있습니다. 섬아연석 부유물은 인듐 가루에 매우 가치가 있고, 모나자이트 부유물은 란타넘/루테튬 가루에 매우 가치가 있으며, 네더랙 부유물은 네더라이트 라인에서 필수입니다.

<Color id="GREEN">FCR</Color>은 처음 실행한 레시피에 영구적으로 고정되므로 한 종류의 재료만 처리할 수 있습니다. 컨트롤러를 부숴도 초기화되지 않습니다. 이 동작은 회로 조립 라인 <ItemImage id="gregtech:gt.blockmachines:12735"/>와 유사하지만, 각인은 전혀 필요하지 않습니다.