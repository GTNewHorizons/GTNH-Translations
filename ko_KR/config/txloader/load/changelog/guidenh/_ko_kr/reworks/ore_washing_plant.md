---
item_ids:
  - gregtech:gt.blockmachines:15550
navigation:
  title: 광석 세척 공장
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15550
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---

# 광석 세척 공장

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15550"/>
</GameScene>
<Color id="GREEN">광석 세척 공장(OWP)</Color>은 분쇄된 광석을 세척하거나 간이 세척하기 위한 EV 티어 멀티블록입니다. 세척과 간이 세척의 차이는 후자가 훨씬 빠르지만 광석에서 어떤 부산물도 생성하지 않는다는 점입니다. <Color id="GREEN">OWP</Color>는 단일블록 광석 세척기와 간이 세척기의 직접적인 상위 버전입니다. 두 종류의 레시피를 모두 처리할 수 있고, <Color id="RED">500%</Color> 속도로 작동하며, 전압 티어당 <Color id="BLUE">4</Color>개의 병렬 처리를 제공하기 때문입니다. 
<br clear="all"/>

> [!NOTE]
> 멀티블록에는 (구조를 제외하고) 다음과 같은 변경 사항이 적용되었습니다:
> - 분리: 이 멀티블록은 __더 이상__ 화학조 레시피를 처리하지 않습니다. 대신 [산업용 화학조](./chem_bath.md)를 참조하십시오.

## 건설
<Color id="GREEN">OWP</Color>에는 티어별 부품이 없습니다. 버스/해치는 구조물의 어느 위치에서든 어떤 케이싱이든 대체할 수 있습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 물은 기계를 초기 구동하기 위한 일회성 비용이며, 저수조 해치 또는 입력 해치를 통해 구조물에 투입됩니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15550"/><ItemImage id="gregtech:gt.blockmachines:15550"/>
- 70-85 <ItemLink id="miscutils:gtplusplus.blockcasings.2:4"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:4"/>
- 15 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1+ 에너지 해치 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ 출력 버스 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">OWP</Color>는 각 면의 벽을 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 여기에는 물을 공급하기 위한 저수조 해치도 포함됩니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 두 기계 간에 하나의 에너지 해치를 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">OWP</Color>는 단일블록 광석 세척기와 간이 세척기의 직접적인 상위 버전입니다. 두 종류의 레시피를 모두 처리할 수 있고, 500% 속도로 작동하며, 전압 티어당 4개의 병렬 처리를 제공하기 때문입니다.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


<Color id="GREEN">OWP</Color>에는 아래에 나열된 두 가지 작동 모드가 있습니다. 컨트롤러의 GUI에서 모드를 전환하십시오. 광석 세척기 모드는 매우 빠르고 부산물을 생성하므로 광석 처리 설비에 특히 유용합니다.

- 광석 세척기 - 분쇄된 광석을 각각 200L의 물로 세척합니다. 부산물을 생성합니다.
- 간이 세척기 - 분쇄된 광석과 불순한 가루를 각각 100L의 물로 세척합니다. 부산물을 생성하지 않습니다.