---
item_ids:
  - gregtech:gt.blockmachines:15566
navigation:
  title: 산업용 혼합 기계
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15566
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 산업용 혼합 기계

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15566"/>
</GameScene>
<Color id="GREEN">산업용 혼합 기계</Color>는 합금과 기타 가루 혼합물을 혼합하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">IMM</Color>은 최대 <Color id="RED">900%</Color> 속도로 작동하고 전압 티어당 <Color id="BLUE">8</Color>개의 병렬 처리를 제공하므로 단일블록 혼합기와 증기 블렌더의 직접 업그레이드판입니다. UIV+ 유리를 사용하면 <Color id="GREEN">IMM</Color>이 일반 에너지 해치 대신 멀티앰프 에너지 해치 하나를 가질 수 있습니다. 동일한 기계 내에서 서로 다른 프로그래밍된 회로를 사용하려면 <Color id="GREEN">IMM</Color>에서 입력 분리를 활성화해야 합니다. 

<br clear="all"/>

> [!NOTE]
> 이전 산업용 혼합기에서의 변경 사항은 다음과 같습니다(새 구조물 제외):
> - 티어별 아이템 파이프: 아이템 파이프 케이싱 티어에 따라 200-900% 속도!
> - 새로운 케이싱: 더 멋져 보입니다!
> - 멀티앰프 해치: 이제 인피니티 유리 이상에서 해금됩니다!

## 건설
<Color id="GREEN">IMM</Color>에는 티어별 구성 요소가 하나 있습니다. 아이템 파이프 케이싱이 기계의 속도 보너스를 결정합니다. 유리는 어떤 티어든 사용할 수 있으며 기계 작동에 영향을 주지 않지만, UIV+ 유리를 사용하면 IMM이 일반 에너지 해치 대신 멀티앰프 에너지 해치 하나를 가질 수 있습니다. 버스/해치는 구조물의 어느 위치에서든 모든 혼합기 케이싱을 대체할 수 있습니다. 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 하위 채널 "item_pipe"와 "glass"로 해당 구성 요소의 티어를 지정하여 구조물을 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하십시오. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15566" /> <ItemImage id="gregtech:gt.blockmachines:15566" />
- 5-45 <ItemLink id="gregtech:gt.blockcasings12:13" /> <ItemImage id="gregtech:gt.blockcasings12:13" />
- 30 티어별 유리 (아무 티어)
- 24 <ItemLink id="gregtech:gt.sheetmetal:316" /> <ItemImage id="gregtech:gt.sheetmetal:316" />
- 10 아이템 파이프 케이싱 <ItemImage id="gregtech:gt.blockcasings11" />
- 5 <ItemLink id="gregtech:gt.blockcasings4:11" /> <ItemImage id="gregtech:gt.blockcasings4:11" />
- 1+ 에너지 해치 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (혼합기 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">IMM</Color>들은 케이싱, 판금, 버스/해치를 절약하기 위해 각 면의 벽을 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로, 멀티앰프 에너지 해치를 사용하지 않는 한 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 간에 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">IMM</Color>은 최대 900% 속도로 작동하고 전압 티어당 8개의 병렬 처리를 제공하므로, 다음 표에서 볼 수 있듯이 단일블록 혼합기와 증기 블렌더의 직접 업그레이드판입니다. UIV+ 유리를 사용하면 <Color id="GREEN">IMM</Color>이 일반 에너지 해치 대신 멀티앰프 에너지 해치 하나를 가질 수 있습니다. 

### 병렬 처리:

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |

### 속도:
| 티어 | 아이템 파이프 케이싱 | 속도 |
| --------------- | --------------- | --------------- |
| 1 | 주석 | 200% |
| 2 | 황동 | 300% |
| 3 | 일렉트럼 | 400% |
| 4 | 백금 | 500% |
| 5 | 오스뮴 | 600% |
| 6 | 퀀티움 | 700% |
| 7 | 플럭스드 일렉트럼 | 800% |
| 8 | 블랙 플루토늄 | 900% |