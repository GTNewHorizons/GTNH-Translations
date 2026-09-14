---
item_ids:
  - gregtech:gt.blockmachines:15549
navigation:
  title: 산업용 압출기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15549
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---
# 산업용 압출기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15549"/>
</GameScene>
<Color id="GREEN">산업용 압출기 (IEM)</Color>는 금속을 다양한 형상과 부품으로 압출하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">IEM</Color>은 <Color id="BLUE">350%</Color> 속도로 작동하고 전압 티어당 <Color id="RED">6</Color>개의 병렬 처리를 제공하므로 단일블록 압출기에서 직접 업그레이드한 기계입니다. 압출 버스 <ItemImage id="gregtech:gt.blockmachines:31785"/>에는 압출기 형상을 위한 설정 가능한 고스트 슬롯이 있으며, 이 슬롯은 자신의 버스에 있는 아이템에만 적용되므로 한 기계가 필요한 만큼 많은 레시피를 처리할 수 있습니다. 

<br clear="all"/>

> [!NOTE]
> 멀티블록에는 (구조물 외에도) 다음과 같은 변경 사항이 적용되었습니다:
> 병렬 처리: 전압 티어당 4 -> 6으로 증가

## 건설
<Color id="GREEN">IEM</Color>에는 티어 구성 요소가 없습니다. 버스/해치는 구조물 어디에서든 어떤 케이싱이든 대체할 수 있습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>을 사용하여 구조물을 시각화/건설하십시오.

<Color id="GREEN">IEM</Color>의 고유 기능은 압출 버스로, 이는 실질적으로 압출기 형상을 위한 설정 가능한 고스트 슬롯이 있는 입력 버스입니다. 형상 슬롯을 Shift-클릭하면 사용 가능한 모든 옵션이 있는 메뉴가 열립니다. 형상은 입력 분리 설정과 관계없이 자신의 버스에 있는 아이템에만 적용됩니다. 압출 버스는 내부 용량을 늘리기 위한 네 가지 티어가 있으며, 결국 제작 입력 버퍼로 대체됩니다. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15549"/><ItemImage id="gregtech:gt.blockmachines:15549"/>
- 8-33 <ItemLink id="gregtech:gt.blockcasings10:3"/><ItemImage id="gregtech:gt.blockcasings10:3"/>
- 24 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 3-7 <ItemLink id="gregtech:gt.blockcasings4:1"/><ItemImage id="gregtech:gt.blockcasings4:1"/>
- 1+ 에너지 해치 (아무 컨테인먼트 또는 스테인리스 강 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (아무 컨테인먼트 또는 스테인리스 강 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (아무 컨테인먼트 또는 스테인리스 강 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 압출 버스 (아무 컨테인먼트 케이싱)
- 0+ 입력 버스 (아무 컨테인먼트 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 버스 (아무 컨테인먼트 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">IEM</Color>은 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 간에 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">IEM</Color>은 350% 속도로 작동하고 전압 티어당 6개의 병렬 처리를 제공하므로 단일블록 압출기에서 직접 업그레이드한 기계이며, 다음 표에서 볼 수 있습니다. 
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |


<Color id="GREEN">IEM</Color>에서는 입력 분리가 영구적으로 활성화되어 있어, 서로 다른 입력 버스에 있는 SOLID 재료가 동일한 레시피에 사용되는 것을 방지합니다. 여기에는 모든 압출기 형상도 포함됩니다. 즉, 많은 압출/입력 버스를 갖춘 단일 <Color id="GREEN">IEM</Color>이 여러 가지 압출기 형상을 동시에 지원할 수 있습니다. 다만 최소 개수의 컨테인먼트 및 스테인리스 강 케이싱 이상을 유지하는 것을 잊지 마십시오.