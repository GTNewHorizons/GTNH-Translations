---
item_ids:
  - gregtech:gt.blockmachines:15552
navigation:
  title: 산업용 성형 프레스
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15552
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 산업용 성형 프레스

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15552"/>
</GameScene>
<Color id="GREEN">산업용 성형 프레스(Industrial Forming Press, IFP)</Color>는 금속을 주형에 압착하는 EV 티어 멀티블록입니다. <Color id="GREEN">IFP</Color>는 <Color id="BLUE">600%</Color> 속도로 작동하고 전압 티어당 <Color id="RED">6</Color>개의 병렬 처리를 제공하므로 단일블록 성형 프레스의 직접적인 상위 버전입니다. 동일한 기계 안에서 서로 다른 주형과 프로그래밍된 회로를 사용하려면 <Color id="GREEN">IFP</Color>에서 입력 분리를 활성화해야 합니다.

<br clear="all"/>

> [!NOTE]
> 멀티블록에 다음과 같은 변경 사항이 적용되었습니다(구조물 제외):
> - 기계 분리: 절곡과 성형 기능이 두 개의 별도 멀티블록으로 분리되었습니다([산업용 절곡 기계](bending.md) 참조)
> - 병렬 처리 증가: 전압 티어당 4 -> 6

## 건설
<Color id="GREEN">IFP</Color>에는 티어별 부품이 없습니다. 버스와 해치는 구조물 어디에서든 금속 가공 기계 케이싱을 대체할 수 있습니다. <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설할 수 있습니다.

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15552"/>
- 5-20 <ItemLink id="miscutils:miscutils.blockcasings:4"/><ItemImage id="miscutils:miscutils.blockcasings:4"/>
- 6 <ItemLink id="gregtech:gt.blockframes:28"/><ItemImage id="gregtech:gt.blockframes:28"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 5 <ItemLink id="gregtech:gt.blockcasings12:14"/><ItemImage id="gregtech:gt.blockcasings12:14"/>
- 1 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 1개 이상 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1개 정비 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1개 소음기 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">IFP</Color>는 각 면을 벽 공유하여 케이싱, 성형 코어, 버스와 해치를 절약할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에서 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.

## 사용법
<Color id="GREEN">IFP</Color>는 600% 속도로 작동하고 전압 티어당 6개의 병렬 처리를 제공하므로 단일블록 성형 프레스의 직접적인 상위 버전이며, 이는 다음 표에서 볼 수 있습니다.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 |

서로 다른 입력 버스에 있는 SOLID 재료가 동일한 레시피에 사용되는 것을 방지하려면, 주형이나 프로그래밍된 회로를 포함하여 <Color id="GREEN">IFP</Color>에서 입력 분리를 활성화해야 합니다. 즉, 여러 개의 입력 버스를 갖춘 단일 <Color id="GREEN">IFP</Color>가 다양한 주형이나 프로그래밍된 회로를 동시에 지원할 수 있습니다. 다만 금속 가공 기계 케이싱의 최소 개수 이상을 유지하는 것을 잊지 마십시오. 판 주형(운모 기반 시트용)과 네 개의 AE2 회로 프레스는 충돌 없이 동일한 입력 버스를 차지할 수 있습니다.