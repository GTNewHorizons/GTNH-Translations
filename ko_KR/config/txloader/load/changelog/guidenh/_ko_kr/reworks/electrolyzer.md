---
item_ids:
  - gregtech:gt.blockmachines:15514
navigation:
  title: 산업용 전해조
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15514
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 산업용 전해조

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15514"/>
</GameScene>
<Color id="GREEN">산업용 전해조</Color>는 가루와 액체를 하위 화합물 또는 구성 원소로 전기분해하는 IV 티어 멀티블록입니다(예: 메테인을 탄소와 수소로). <Color id="GREEN">산업용 전해조</Color>는 단일블록 전해조에서 바로 업그레이드한 형태인데, 이는 280% 속도로 작동하고, 일반적으로 필요한 EU/t의 90%만 사용하며, 전압 티어당 4개의 병렬 처리를 제공하기 때문입니다. 

<br clear="all"/>

> [!NOTE]
> 이전 버전에서 바뀐 점은 (구조 자체를 제외하면) 이제 전압 티어당 4개의 병렬 처리를 지원한다는 것뿐입니다. 이상입니다!

## 건설
<Color id="GREEN">산업용 전해조</Color>에는 티어별 부품이 없습니다. 버스/해치는 구조물 어디에서든 전해조 케이싱을 대체할 수 있습니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조물을 시각화/건설하십시오.

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15514" /> <ItemImage id="gregtech:gt.blockmachines:15514" />
- 6-43 <ItemLink id="miscutils:miscutils.blockcasings:5" /> <ItemImage id="miscutils:miscutils.blockcasings:5" />
- 12 <ItemLink id="miscutils:blockFrameGtPotin" /> <ItemImage id="miscutils:blockFrameGtPotin" />
- 4 <ItemLink id="gregtech:gt.blockcasings11" /> <ItemImage id="gregtech:gt.blockcasings11" />
- 4 <ItemLink id="gregtech:gt.blockcasings11:1" /> <ItemImage id="gregtech:gt.blockcasings11:1" />
- 1개 이상 에너지 해치(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1개 정비 해치(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1개 소음기 해치(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0개 이상 출력 해치(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">산업용 전해조</Color>는 각 면을 벽 공유하여 케이싱, 프레임 박스, 버스/해치를 절약할 수 있습니다. 여기에는 양쪽의 아이템 파이프 케이싱도 포함되지만, 먼저 컨트롤러 중 하나를 수평으로 뒤집지 않으면 교체할 수 없습니다(렌치를 들고 웅크린 채 우클릭). 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">산업용 전해조</Color>는 <Color id="GREEN">280%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="BLUE">90%</Color>만 사용하며, 다음 표에서 볼 수 있듯이 전압 티어당 <Color color="#ed6401">4</Color>개의 병렬 처리를 제공하므로 단일블록 전해조에서 바로 업그레이드한 형태입니다. 


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |