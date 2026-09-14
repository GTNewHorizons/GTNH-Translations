---
item_ids:
  - gregtech:gt.blockmachines:15539
navigation:
  title: 산업용 분쇄 스택
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15539
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---

# 산업용 분쇄 스택

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15539"/>
</GameScene>

<Color id="GREEN">산업용 분쇄 스택 (IMS)</Color>은 아이템을 분쇄하고 갈아서 가루로 만드는 EV 티어 멀티블록입니다. <Color id="GREEN">IMS</Color>는 두 티어로 제공되고 규모에 따른 보너스를 가지므로 단일블록 분쇄기와 증기 분쇄기의 직접적인 상위 버전입니다. T1 구조는 <Color id="BLUE">160%</Color> 속도로 작동하며 전압 티어당 <Color id="RED">2</Color>개의 병렬 처리를 제공합니다. T2 구조는 <Color id="BLUE">640%</Color> 속도로 작동하며 전압 티어당 <Color id="RED">8</Color>개의 병렬 처리를 제공합니다. <Color id="GREEN">IMS</Color>는 분쇄 업그레이드 칩 <ItemImage id="miscutils:MU-metaitem.01:32152"/>을 컨트롤러에 삽입하거나, 칩을 손에 들고 컨트롤러를 우클릭하여 업그레이드할 수 있습니다.
<br clear="all"/>

> [!NOTE]
> 구조를 제외하고 멀티블록에 다음과 같은 변경 사항이 적용되었습니다:
> - T1은 어떤 방식으로도 변경되지 않았습니다.
> - T2: 새로운 구조, 속도 증가(160->640%)

## 건설
<Color id="GREEN">IMS</Color>는 두 티어로 제공됩니다. T1 구조에는 티어 구성 요소가 없으며, 버스/해치는 구조의 어느 위치에서든 모든 케이싱을 대체할 수 있습니다. T2 구조에도 티어 구성 요소가 없으며, 버스/해치는 구조의 어느 위치에서든 모든 분쇄 스택 케이싱을 대체할 수 있습니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 구조를 시각화하거나 건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오. 하위 채널 "glass"는 유리의 티어를 지정하고, 한 스택에 든 프로젝터 수는 건설할 티어를 지정합니다. 

### T1 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15539"/><ItemImage id="gregtech:gt.blockmachines:15539"/>
- 26-44 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 에너지 해치 1개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:70" />
- 출력 버스 0개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:80" />

### T2 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15539"/><ItemImage id="gregtech:gt.blockmachines:15539"/>
- 69-87 <ItemLink id="miscutils:miscutils.blockcasings:7"/><ItemImage id="miscutils:miscutils.blockcasings:7"/>
- 20 <ItemLink id="gregtech:gt.blockframes:372"/><ItemImage id="gregtech:gt.blockframes:372"/>
- 18 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 티어 유리 8개 (아무 티어나) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 6 <ItemLink id="gregtech:gt.blockcasings3:10"/><ItemImage id="gregtech:gt.blockcasings3:10"/>
- 에너지 해치 1개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:40" />
- 유지보수 해치 1개 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:70" />
- 출력 버스 0개 이상 (어떤 케이싱이든) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">IMS</Color>는 케이싱, 프레임 박스, 유리, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로, <u>__두__</u> 기계 사이에서 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">IMS</Color>는 두 티어로 제공되고 규모에 따른 보너스를 가지므로 단일블록 분쇄기와 증기 분쇄기의 직접적인 상위 버전입니다. T1 구조는 160% 속도로 작동하며 전압 티어당 2개의 병렬 처리를 제공합니다. T2 구조는 640% 속도로 작동하며 전압 티어당 8개의 병렬 처리를 제공합니다. IMS는 <ItemLink id="miscutils:MU-metaitem.01:32152"/><ItemImage id="miscutils:MU-metaitem.01:32152"/>를 컨트롤러에 삽입하거나, 칩을 손에 들고 컨트롤러를 우클릭하여 업그레이드할 수 있습니다. 칩은 즉시 소모되며 회수할 수 없습니다. 

### 병렬 처리:

|   | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| T1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 |
| T2 | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |