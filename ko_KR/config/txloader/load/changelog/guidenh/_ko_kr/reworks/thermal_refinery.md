---
item_ids:
  - gregtech:gt.blockmachines:15538
navigation:
  title: 대형 열 정련기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15538
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-23
---

# 대형 열 정련기

&lt;GameScene wrap="square" align="right"&gt;
  &lt;ImportStructureLib controller="gregtech:gt.blockmachines:15538"/&gt;
&lt;/GameScene&gt;
<Color id="GREEN">대형 열 정련기(LTR)</Color>는 분쇄된 광석을 정련하고 고갈된 연료봉을 재활용하기 위한 EV 티어 멀티블록입니다. <Color id="GREEN">LTR</Color>은 단일블록 열 원심분리기의 직접적인 업그레이드로, 최대 <Color id="RED">320%</Color> 속도로 작동하고 일반적으로 필요한 EU/t의 최소 <Color id="BLUE">39%</Color>만 사용하며, 전압 티어당 <Color color="#ed6401">8</Color>개의 병렬 처리와 솔레노이드 티어당 2개의 병렬 처리를 제공합니다. 또한 각 가열 코일 티어는 5%의 속도 보너스(합연산)와 5%의 EU/t 절감(곱연산)을 제공합니다.

<br clear="all"/>

> [!NOTE]
> 새로운 구조물 외에도 멀티블록에 다음과 같은 변경 사항이 적용되었습니다:
> - 티어별 코일: 티어당 5%의 합연산 속도 보너스, 티어당 5%의 곱연산 전력 감소
> - 티어별 솔레노이드: 솔레노이드 티어당 2개의 병렬 처리

## 건설
<Color id="GREEN">LTR</Color>은 두 가지 티어 구성 요소를 가집니다. <Color id="RED">가열 코일</Color>은 기계의 속도 보너스와 에너지 절감을 증가시킵니다. <Color id="BLUE">솔레노이드</Color>는 병렬 처리 수를 증가시킵니다. 유리는 어떤 티어든 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물의 어느 위치에 있는 열 처리 케이싱이든 대체할 수 있습니다. 멀티 앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭킹을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 하위 채널 "coil", "solenoid", "glass"로 구조물을 시각화/건설해 해당 구성 요소의 티어를 지정하십시오.

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15538" /> <ItemImage id="gregtech:gt.blockmachines:15538" />
- 85-92 <ItemLink id="miscutils:gtplusplus.blockcasings.2" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2" />
- 20 <ItemLink id="gregtech:gt.blockframes:348" /> <ItemImage id="gregtech:gt.blockframes:348" />
- 가열 코일 16개 <ItemImage id="gregtech:gt.blockcasings5:11" />
- 솔레노이드 초전도 코일 6개 <ItemImage id="gregtech:gt.blockcasings.cyclotron_coils:10" />
- 티어별 유리 6개(아무 종류) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 4 <ItemLink id="gregtech:gt.blockcasings:11" /> <ItemImage id="gregtech:gt.blockcasings:11" />
- 에너지 해치 1개 이상(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:70" />
- 입력 해치 0개 이상(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 버스 0개 이상(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">LTR</Color>은 케이싱, 유리, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 많은 레시피가 2A의 전력을 사용하므로, 최소한 플럭스드 일렉트럼 코일 없이는 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 사이에서 공유하는 것이 불가능합니다.

## 사용법
<Color id="GREEN">LTR</Color>은 단일블록 열 원심분리기의 직접적인 업그레이드로, 최대 <Color id="RED">320%</Color> 속도로 작동하고 일반적으로 필요한 EU/t의 최소 <Color id="BLUE">39%</Color>만 사용하며, 전압 티어당 <Color color="#ed6401">8</Color>개의 병렬 처리와 솔레노이드 티어당 <Color id="GREEN">2</Color>개의 병렬 처리를 제공합니다. 이는 다음 표에서 볼 수 있습니다. 또한 각 가열 코일 티어는 5%의 속도 보너스(합연산)와 5%의 EU/t 절감(곱연산)을 제공합니다.
### 가열 코일:
|  코일 | 속도 | EU/t |
| --------------- | --------------- | --------------- |
| 큐프로니켈 | 255% | 76.0% |
| 칸탈 | 260% | 72.2% |
| 니크롬 | 265% | 68.6% |
| TPV 합금 | 270% | 65.2% |
| HSS-G | 275% | 61.9% |
| HSS-S | 280% | 58.8% |
| 나쿼다 | 285% | 55.9% |
| 나쿼다 합금 | 290% | 53.1% |
| 트리늄 | 295% | 50.4% |
| 플럭스드 일렉트럼 | 300% | 47.9% |
| 각성한 드라코늄 | 305% | 45.5% |
| 인피니티 | 310% | 43.2% |
| 하이포젠 | 315% | 41.1% |
| 이터널 | 320% | 39.0% |

### 솔레노이드:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
|--------------- | -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| MV | 12 | 20 | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 |
| HV | 14 | 22 | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 |
| EV | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 |
| IV | 18 | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 | 106 | 114 | 122 | 130 |
| LuV | 20 | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 | 132 |
| ZPM | 22 | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 | 134 |
| UV | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 | 136 |
| UHV | 26 | 34 | 42 | 50 | 58 | 66 | 74 | 82 | 90 | 98 | 106 | 114 | 122 | 130 | 138 |
| UEV | 28 | 36 | 44 | 52 | 60 | 68 | 76 | 84 | 92 | 100 | 108 | 116 | 124 | 132 | 140 |
| UIV | 30 | 38 | 46 | 54 | 62 | 70 | 78 | 86 | 94 | 102 | 110 | 118 | 126 | 134 | 142 |
| UMV | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 | 128 | 136 | 144 |