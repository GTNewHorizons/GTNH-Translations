---
item_ids:
  - gregtech:gt.blockmachines:15553
navigation:
  title: 산업용 절곡기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15553
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 산업용 절곡기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15553"/>
</GameScene>

<Color id="GREEN">산업용 절곡기(IBM)</Color>는 주괴를 플레이트로 절곡하기 위한 EV 티어 멀티블록입니다. <Color id="GREEN">IBM</Color>은 <Color id="RED">600%</Color> 속도로 작동하고 전압 티어당 <Color id="BLUE">6</Color>개의 병렬 처리를 제공하므로 단일블록 절곡기에서 직접 업그레이드한 기계입니다. 동일한 기계 내에서 서로 다른 프로그래밍된 회로를 사용하려면 <Color id="GREEN">IBM</Color>에서 입력 분리를 활성화해야 합니다.

<br clear="all"/>

> [!NOTE]
> 다음 변경 사항이 멀티블록에 적용되었습니다(구조물 제외):
> - 기계 분리: 절곡 및 성형 기능이 두 개의 별도 멀티블록으로 분리되었습니다([산업용 성형 프레스 참조](forming.md))
> - 병렬 처리 증가: 전압 티어당 4 -> 6

## 건설
<Color id="GREEN">IBM</Color>에는 티어가 있는 구성 요소가 없습니다. 버스/해치는 구조물 어디에서나 임의의 금속 가공 기계 케이싱을 대체할 수 있습니다. <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설할 수 있습니다.

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15553"/>
- 4-15 <ItemLink id="miscutils:miscutils.blockcasings:4"/><ItemImage id="miscutils:miscutils.blockcasings:4"/>
- 9 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 6 <ItemLink id="gregtech:gt.blockframes:28"/><ItemImage id="gregtech:gt.blockframes:28"/>
- 3 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 에너지 해치 1개 이상 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 출력 버스 0개 이상 (임의의 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">IBM</Color>들은 케이싱, 프레임 박스, 스탬핑 코어, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로, 기계 <u>__두 대__</u> 사이에서 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.

## 사용법
<Color id="GREEN">IBM</Color>은 다음 표에서 볼 수 있듯이 600% 속도로 작동하고 전압 티어당 6개의 병렬 처리를 제공하므로 단일블록 절곡기에서 직접 업그레이드한 기계입니다.

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |


<Color id="GREEN">IBM</Color>에서 입력 분리를 활성화하여, 프로그래밍된 회로를 포함해 서로 다른 입력 버스에 있는 SOLID 재료가 동일한 레시피에 사용되지 않도록 해야 합니다. 즉, 많은 입력 버스를 갖춘 단일 <Color id="GREEN">IBM</Color>이 여러 가지 서로 다른 프로그래밍된 회로를 동시에 지원할 수 있습니다. 금속 가공 기계 케이싱의 최소 개수 이상을 유지하는 것을 잊지 마십시오.

절곡기 레시피에서 가장 흔히 사용되는 프로그래밍된 회로는 1, 2, 3, 4, 5, 9, 10입니다.