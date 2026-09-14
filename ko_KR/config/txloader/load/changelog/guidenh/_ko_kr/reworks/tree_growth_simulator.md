---
item_ids:
  - gregtech:gt.blockmachines:15541
navigation:
  title: 나무 성장 시뮬레이터
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15541
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---

# 나무 성장 시뮬레이터

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15541"/>
</GameScene>
<Color id="GREEN">나무 성장 시뮬레이터 (TGS)</Color>는 나무를 디지털 방식으로 자동으로 성장 및 수확하는 IV 티어 멀티블록입니다. <Color id="GREEN">TGS</Color>는 훨씬 빠르고 효율적이기 때문에 EnderIO 농장 스테이션 <ItemImage id="EnderIO:blockFarmStation"/> 또는 작물 관리기 <ItemImage id="gregtech:gt.blockmachines:28001"/>에서 직접 업그레이드한 것입니다. 나무는 또한 렉을 방지하기 위해 실제로 세계에 배치되지 않습니다. <Color id="GREEN">TGS</Color>는 컨트롤러에 묘목 하나, 입력 버스에 수확할 대상을 지정하는 특정 GregTech 도구, 그리고 전력만 필요로 합니다. 톱은 통나무를 생산하고, 가지 절단기는 묘목을 생산하며, 가위는 잎을, 칼은 과일을 생산합니다. 일부 나무는 다른 나무보다 자연적으로 더 많은 자원을 생산합니다. 레시피 길이는 5초로 고정되어 있지만, 더 많은 전력과 더 좋은 도구는 반복당 출력 수를 상당히 배수할 수 있습니다.
<br clear="all"/>

> [!NOTE]
> 멀티블록에 다음과 같은 변경 사항이 적용되었습니다 (구조 제외):
> - 새로운 구조적 이점: 목재와 잎이 자동 배치되므로 신경 쓸 필요가 없으며, 흙이 잔디로 변환됩니다.

## 건설
<Color id="GREEN">TGS</Color>에는 티어가 있는 부품이 없습니다. 유리는 어떤 티어든 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물 어디에서나 케이싱을 대체할 수 있습니다. 스토킹 입력 버스와 조합 입력 버스는 지원되지 않습니다. 멀티앰프 및 레이저 에너지 해치도 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 참나무 통나무와 잎은 구조물이 형성되면 무료로 생성되므로 수동으로 배치할 필요가 없습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "glass"로 구조물을 시각화/건설하여 유리의 티어를 지정하십시오.

### 필요 재료:
- 1 <ItemLink id="gregtech:gt.blockmachines:15541"/><ItemImage id="gregtech:gt.blockmachines:15541"/>
- 60 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 57 티어 유리 (아무거나) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 45-55 <ItemLink id="miscutils:gtplusplus.blockcasings.2:15"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:15"/>
- 25 흙 <ItemImage id="minecraft:dirt"/> / 잔디 <ItemImage id="minecraft:grass"/>
- 1+ 에너지 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">TGS</Color>는 케이싱, 프레임 상자, 유리, 버스/해치를 절약하기 위해 각 측면을 벽 공유할 수 있습니다. 어떤 레시피도 1A 이상의 전력을 사용하지 않으므로 <u>__두__</u> 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.

## 사용법
<Color id="GREEN">TGS</Color>는 나무를 성장 및 수확하는 데 훨씬 빠르고 효율적이기 때문에 EnderIO 농장 스테이션 또는 작물 관리기에서 직접 업그레이드한 것입니다. 레시피 길이는 5초로 고정되어 있지만, 생산량을 확장하기 위해 에너지 해치의 티어에 따른 출력 배율이 있습니다. 기본 출력은 재배하는 나무의 종류에 따라 다르지만, 일반적으로 통나무 5개, 묘목 5개, 잎 2개, 과일 2개입니다.

### 배율:
| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 5 | 9 | 17 | 29 | 45 | 65 | 89 | 117 | 149 | 185 | 225 | 269 | 317 | 369 | 425 |

입력 버스에 있는 도구가 <Color id="GREEN">TGS</Color>가 생산하는 특정 출력을 결정합니다. 동일한 입력 버스에 여러 도구를, 심지어 다른 종류의 도구를 넣어 여러 출력을 동시에 수집할 수 있습니다. 일부 도구는 다른 도구보다 우수하며 출력에 두 번째 배율을 적용합니다. 지원되는 도구와 그 배율은 아래에 나열되어 있습니다. 에너지가 떨어진 전동 도구는 회수를 위해 출력 버스로 전달됩니다.

- 통나무 - 톱 (x1), 원형 톱 (x2), 전기톱 (x4)
- 묘목 - 가지 절단기 (x1), 접목기 (x4)
- 잎 - 가위 (x1), 전선 절단기 (x2), 자동 전지가위 (x4)
- 과일 - 칼 (x1)

## 자동화
<Color id="GREEN">TGS</Color>를 효과적으로 사용할 때의 어려움은 전동 도구를 다른 제품과 분리하고, 재충전한 후, 기계에 다시 넣는 것입니다. GregTech의 도구 충전 방법(배터리 버퍼, 터보 충전기 등)은 내용물을 추출할 수 있게 하지 않으므로 자동화에 사용할 수 없습니다.

대안으로, 내구성이 매우 높은 비전동 도구를 여러 개 사용하십시오. 자원을 덜 생산할 수 있지만 교체할 필요가 거의 없습니다. 오리하루콘, 오리칼쿰, 드라코늄은 모두 좋은 선택입니다. 전동 도구를 여러 개 사용하더라도 자주 재충전할 필요가 없습니다.

자동화 방법은 여기에 쉽게 보여주기에는 다소 복잡하므로, 더 많은 정보를 원하시면 [위키](https://wiki.gtnewhorizons.com/wiki/Tree_Growth_Simulator)를 방문하십시오.