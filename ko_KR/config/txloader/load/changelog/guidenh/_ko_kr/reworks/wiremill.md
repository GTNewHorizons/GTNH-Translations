---
item_ids:
  - gregtech:gt.blockmachines:15511
navigation:
  title: 산업용 전선 공장
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15511
categories:
    - 구조 개편
author: Skorched
date: 2026-05-26
---

# 산업용 전선 공장

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15511"/>
</GameScene>
<Color id="GREEN">산업용 전선 공장(IWF)</Color>은 금속에서 전선을 뽑아내기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">IWF</Color>는 아이템 파이프 케이싱 티어에 따라 최대 400%의 속도 보너스를 얻고, 일반적으로 필요한 EU/t의 75%만 사용하며, 전압 티어당 4개의 병렬 처리를 제공하기 때문에 단일블록 전선 인발기의 직접적인 업그레이드입니다. 동일한 기계 내에서 서로 다른 프로그래밍된 회로를 사용하려면 IWF에서 입력 분리를 활성화해야 합니다.

<br clear="all"/>

> [!NOTE]
> 멀티블록에는 다음과 같은 변경 사항이 적용되었습니다(구조 제외):
> - 티어별 아이템 파이프: 아이템 파이프 케이싱 티어에 따라 50~400%(이전 최대 300%)의 속도 보너스
> - 구조: 케이싱을 위한 공간이 늘어나 더 많은 버스와 해치를 설치할 수 있습니다.

## 건설
<Color id="GREEN">IWF </Color>에는 티어형 구성 요소가 하나 있습니다. 아이템 파이프 케이싱이 기계의 속도 보너스를 결정합니다. 유리는 어떤 티어든 가능하며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조 어디에서든 어떤 케이싱이든 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 설치할 수 있습니다. 해당 구성 요소의 티어를 지정하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />을(를) 사용하여 하위 채널 "item_pipe"와 "glass"로 구조를 시각화/건설하십시오.
### 필요 항목:

- 1 <ItemLink id="gregtech:gt.blockmachines:15511" /> <ItemImage id="gregtech:gt.blockmachines:15511" />
- 14-35 <ItemLink id="miscutils:miscutils.blockcasings:6" /> <ItemImage id="miscutils:miscutils.blockcasings:6" />
- 15 티어 유리(아무 티어)
- 3 아이템 파이프 케이싱 <ItemImage id="gregtech:gt.blockcasings11:5" />
- 1+ 에너지 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유:
<Color id="GREEN">IWF</Color>는 케이싱, 유리, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.
## 사용법

| 티어 | 아이템 파이프 케이싱 | 속도 보너스 |
| --------------- | --------------- | --------------- |
| 1 | 주석 | 50% |
| 2 | 황동 | 100% |
| 3 | 일렉트럼 | 150% |
| 4 | 백금 | 200% |
| 5 | 오스뮴 | 250% |
| 6 | 퀀티움 | 300% |
| 7 | 플럭스드 일렉트럼 | 350% |
| 8 | 블랙 플루토늄 | 400% |

----------


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |


### 입력 분리
<Color id="GREEN">IWF</Color>에서 입력 분리를 활성화하여 프로그래밍된 회로를 포함한, 서로 다른 입력 버스에 있는 __고체__ 재료가 동일한 레시피에 사용되지 않도록 해야 합니다. 즉, 많은 입력 버스를 갖춘 단일 <Color id="GREEN">IWF</Color>가 여러 가지 서로 다른 회로를 동시에 지원할 수 있습니다.