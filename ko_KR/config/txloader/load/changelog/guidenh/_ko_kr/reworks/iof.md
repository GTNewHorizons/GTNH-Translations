---
item_ids:
  - gregtech:gt.blockmachines:15564
navigation:
  title: 통합 광석 공장
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15564
categories:
    - 구조 개편
author: Skorched
date: 2026-05-23
---

# 통합 광석 공장

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15564"/>
</GameScene>
<Color id="GREEN">통합 광석 공장(IOF)</Color>은 모든 광석 처리를 단일 단계로 수행하는 UHV 티어 멀티블록입니다. 기존의 모든 광석 처리 설비를 완전히 대체하고, 전체 처리량을 향상시키며, 렉을 줄이도록 설계되었습니다. <Color id="GREEN">IOF</Color>는 <ItemLink id="gregtech:gt.blockmachines:14003" /> 직후에 해금되며, 이는 플레이어가 막대한 양의 광석을 축적하기 시작하고 이를 모두 가루로 더 쉽고 빠르게 처리할 방법이 필요해지는 시점입니다. <Color id="GREEN">IOF</Color>는 모든 광석 변형(분쇄, 정제 등)을 지원하며, 사용 가능한 병렬 처리가 충분하다면 서로 다른 레시피를 동시에 처리할 수도 있습니다. 총 병렬 처리 수는 입력 전력에 비례하여 선형적으로 증가하며 상한이 없습니다. 부산물은 <Color id="GREEN">IOF</Color>의 현재 모드에 따라 생성됩니다. 일곱 가지 서로 다른 광석 처리 경로(선별, 광석 세척, 화학 욕조 등)를 위해 총 일곱 가지 모드가 있습니다. 
<br clear="all"/>

> [!NOTE]
> 이전 통합 광석 공장에서의 변경 사항은 다음과 같습니다(새 구조물은 포함하지 않음):
> - 레이저 지원: 이제 본격적인 오버클럭킹을 위한 레이저 에너지 해치를 받습니다
> - 모드 버튼: 이제 모드 전환 버튼을 GUI에서 찾을 수 있습니다
> - 유연성: 해치 위치 제한이 크게 줄어들어 배치가 더 유연해졌습니다


## 건설
<Color id="GREEN">IOF</Color>에는 티어 구성 요소가 없습니다. 유리는 아무 티어나 가능하며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물 어디에서든 스테인리스강 기계 케이싱을 대체할 수 있습니다. 본격적인 처리량을 위해 <Color id="RED">멀티 앰프 및 레이저 에너지 해치</Color>가 지원됩니다. 유리의 티어를 지정하려면 하위 채널 "glass"와 함께 <ItemLink id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조를 시각화하거나 건설하십시오.

<ItemLink id="gregtech:gt.blockmachines:32026" />가 구성 부품에 __사용되지 않는다__고 가정하면, 하나의 <Color id="GREEN">IOF</Color>를 건설하는 데 다른 재료들 외에도 7.21k 뉴트로늄, 3.89k 이리듐, 3.03k 코스믹 뉴트로늄, 3.02k 나콰드리아, 880 베드로키움이 필요합니다. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15564" /> <ItemImage id="gregtech:gt.blockmachines:15564" />
- 462 <ItemLink id="gregtech:gt.blockcasings8:7" /> <ItemImage id="gregtech:gt.blockcasings8:7" />
- 0-163 <ItemLink id="gregtech:gt.blockcasings4:1" /> <ItemImage id="gregtech:gt.blockcasings4:1" />
- 96 <ItemLink id="gregtech:gt.sheetmetal:84" /> <ItemImage id="gregtech:gt.sheetmetal:84" />
- 90 티어 유리(아무 티어) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 23 <ItemLink id="gregtech:gt.blockframes:306" /> <ItemImage id="gregtech:gt.blockframes:306" />
- 7 <ItemLink id="gregtech:gt.blockcasings5:8" /> <ItemImage id="gregtech:gt.blockcasings5:8" />
- 7 <ItemLink id="miscutils:gtplusplus.blockcasings.2:6" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:6" />
- 7 <ItemLink id="gregtech:gt.blockcasings3:10" /> <ItemImage id="gregtech:gt.blockcasings3:10" />
- 7 <ItemLink id="miscutils:miscutils.blockcasings" /> <ItemImage id="miscutils:miscutils.blockcasings" />
- 1 에너지 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ 입력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ 입력 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1+ 출력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">IOF</Color>는 케이싱, 판금, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 바닥층을 바로 아래에 거꾸로 놓인 다른 IOF와 겹치는 것이 가장 효과적이며 매우 권장됩니다. 하지만 병렬 처리가 남아 있는 동안 기계가 가능한 한 많은 암페어를 끌어오므로 에너지 해치는 공유하지 마십시오. 

## 사용법
<Color id="GREEN">IOF</Color>는 분쇄, 정제 등 변형을 포함하여 GTNH의 거의 모든 광석을 처리할 수 있습니다. 모든 광석은 고정적으로 30 EU/t, 윤활유 2L, 증류수 200L를 필요로 합니다. 화학 욕조용 과황산나트륨처럼 다른 입력이 있는 레시피는 기본 비용에 더해 해당 입력도 여전히 필요로 합니다. 처리 속도는 제공되는 전력과 기계의 모드에 따라 달라집니다.

아래에 나열된 일곱 가지 서로 다른 광석 처리 경로를 위해 총 일곱 가지 모드가 있습니다. 컨트롤러의 GUI에서 모드를 전환하거나, 스크루드라이버로 컨트롤러를 우클릭하여 전환할 수 있습니다. 스크루드라이버를 들고 컨트롤러를 웅크려 우클릭하면 돌 가루를 자동으로 폐기합니다. 
| 모드 | 소요 시간 | 경로 | 최대 처리량 |
| --------------- | --------------- | --------------- | --------------- |
| 1 | 30초 | 분쇄 -&gt; 광석 세척기 -&gt; 열 원심분리기 -&gt; 분쇄 | 357,914 /초 |
| 2 | 15초 | 분쇄 -&gt; 광석 세척기 -&gt; 분쇄 -&gt; 원심분리기 | 715,828 /초 |
| 3 | 10초 | 분쇄 -&gt; 분쇄 -&gt; 광석 세척기 | 1,073,742 /초 |
| 4 | 20초 | 분쇄 -&gt; 광석 세척기 -&gt; 선별기 | 536,871 /초 |
| 5 | 17초 | 분쇄 -&gt; 화학 욕조 -&gt; 분쇄 -&gt; 원심분리기| 631,613 /초 |
| 6 | 32초 | 분쇄 -&gt; 화학 욕조 -&gt; 열 원심분리기 -&gt; 분쇄 | 335,544 /초 |
| 7 | 1초 | 단조 해머 -&gt; 단조 해머 -&gt; 간이 세척기| 10,737,418 /초 |

모든 광석 처리 레시피는 LV 티어이며, 기본 시간과 전력 비용은 여기에서 비롯됩니다. <Color id="GREEN">IOF</Color>는 전혀 __오버클럭하지 않지만__, 제공되는 30 EU/t마다 병렬 처리 하나를 추가합니다. 기술적으로 병렬 처리 수에는 상한이 없지만, 증류수의 최대 정수 한도 때문에 여전히 10,737,418 또는 322,122,540 EU/t에서 상한이 정해집니다. 즉, 256A UHV를 초과해도 기계 작동에는 영향이 없으며, 한 번에 2B를 초과하는 증류수를 공급하기 위해 ME 스톡킹 입력 해치를 더 추가하는 것도 도움이 되지 않습니다.