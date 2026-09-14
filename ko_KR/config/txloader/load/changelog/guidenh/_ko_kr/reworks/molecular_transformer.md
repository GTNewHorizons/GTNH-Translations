---
item_ids:
  - gregtech:gt.blockmachines:15558
navigation:
  title: 분자 변환기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15558
categories:
    - 구조 개편
author: Skorched
date: 2026-05-23
---

# 분자 변환기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15558"/>
</GameScene>
<Color id="GREEN">분자 변환기</Color>는 아이템의 분자 구조를 바꾸어 새로운 아이템을 생산하는 LuV 티어 멀티블록입니다. <Color id="GREEN">분자 변환기</Color>에는 싱글블록 등가물이나 확장을 위한 티어별 보너스가 없습니다. 18개 레시피 각각은 작동에 전력만 필요한 일대일 변환입니다. <Color id="GREEN">분자 변환기</Color>는 가장 흔히 발광석을 Sunnarium으로 변환하는 데 사용되지만, 꿀벌, 진공 원자로, 핵융합 원자로가 모두 훨씬 더 좋은 공급원입니다. 그래핀 처리량도 그만한 가치가 없습니다. 

<br clear="all"/>

> [!NOTE]
> 이 버전에서 이 멀티블록에 가해진 유일한 변경은 구조였습니다

## 건설
<Color id="GREEN">분자 변환기</Color>에는 티어별 구성 요소가 없습니다. 유리는 아무 티어나 가능하며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조 어디에서든 모든 분자 격납 케이싱을 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 하위 채널 "glass"로 구조를 시각화/건설하여 유리의 티어를 지정하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15558" /> <ItemImage id="gregtech:gt.blockmachines:15558" />
- 95-104 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:11" /> <ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:11" />
- 35 <ItemLink id="GoodGenerator:speedingPipe" /> <ItemImage id="GoodGenerator:speedingPipe" />
- 30 티어 유리 (아무거나) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 14 <ItemLink id="gregtech:gt.blockcasings8:7" /> <ItemImage id="gregtech:gt.blockcasings8:7" />
- 1+ 에너지 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">분자 변환기</Color>는 각 면을 벽 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 여기에는 좌우 측면의 이리듐 케이싱이나 뒤쪽의 유리가 포함됩니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__one__</u> 에너지 해치를 <u>__two__</u> 기계 사이에 공유할 수 있습니다. 

## 사용법
분자 변환기를 사용하는 데 특별히 독특한 점은 없습니다. 확장을 위한 티어별 보너스가 없으며 불완전한 오버클럭만 있습니다