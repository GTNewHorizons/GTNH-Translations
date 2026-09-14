---
item_ids:
  - gregtech:gt.blockmachines:15542
navigation:
  title: 대형 선별기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15542
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 대형 선별기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15542"/>
</GameScene>
<Color id="GREEN">대형 선별기</Color>는 보석과 광물을 선별하기 위한 HV 티어 멀티블록입니다. <Color id="GREEN">대형 선별기</Color>는 <Color id="RED">500%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="BLUE">75%</Color>만 사용하며, 전압 티어당 <Color id="GREEN">4</Color>개의 병렬 처리를 제공하므로 단일블록 선별기에서 직접 업그레이드한 기계입니다. 다른 용도가 없는 가루와 액체는 상시 선별하는 것이 권장됩니다. 
<br clear="all"/>

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일하게 유지됩니다.

## 건설
<Color id="GREEN">대형 선별기</Color>에는 티어별 구성 요소가 없습니다. 버스/해치는 구조물의 어느 위치에서든 임의의 케이싱을 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 사용할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15542"/><ItemImage id="gregtech:gt.blockmachines:15542"/>
- 45-59 <ItemLink id="miscutils:gtplusplus.blockcasings.2:5"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:5"/>
- 19 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:6"/>
- 16 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 에너지 해치 1개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 입력 해치 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 버스 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:80" />
- 출력 해치 0개 이상 (케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">대형 선별기</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로, <u>__두__</u> 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">대형 선별기</Color>는 500% 속도로 작동하고 일반적으로 필요한 EU/t의 75%만 사용하며 전압 티어당 4개의 병렬 처리를 제공하므로, 다음 표에서 볼 수 있듯이 단일블록 선별기에서 직접 업그레이드한 기계입니다.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


GTNH에는 선별기에서만 사용되고 다른 용도가 전혀 없는 가루와 액체가 몇 가지 있습니다. 이러한 것들은 ME 스톡킹 버스/해치, 또는 분할 저장 셀과 스티키 카드를 사용하는 AE2 서브네트워크에 넣는 것이 매우 권장됩니다.