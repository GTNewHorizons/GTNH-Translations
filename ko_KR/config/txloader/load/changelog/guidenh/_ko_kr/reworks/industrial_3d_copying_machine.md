---
item_ids:
  - gregtech:gt.blockmachines:15554
navigation:
  title: 산업용 3D 복사기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15554
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 산업용 3D 복사기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15554"/>
</GameScene>
<Color id="GREEN">산업용 3D 복사기</Color>는 블록을 장식 변형으로 조각하는 EV 티어 멀티블록입니다. <Color id="GREEN">산업용 3D 복사기</Color>는 단일블록 자동 조각기에서 직접 업그레이드한 기계로, <Color id="RED">300%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="BLUE">75%</Color>만 사용하며, 전압 티어당 <Color id="GREEN">16</Color>개의 병렬 처리를 제공합니다. 대상 블록은 입력 버스나 컨트롤러에 있는 프로그램된 회로로 선택하거나, 조각 버스를 사용하는 경우 블록 자체로 선택합니다. 
<br clear="all"/>

> [!NOTE]
> 새 구조물 외에는 이 멀티블록에 기계적 변경 사항이 없습니다.

## 건설
<Color id="GREEN">산업용 3D 복사기</Color>에는 티어 구성 요소가 없습니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 가열 코일은 반드시 백동이어야 하며, 역시 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물의 어느 위치에서든 견고한 프린터 케이싱을 대체할 수 있습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>을 사용하여 하위 채널 "glass"로 구조물을 시각화/건설해 유리의 티어를 지정할 수 있습니다.

<Color id="GREEN">산업용 3D 복사기</Color>만의 특징은 조각 버스로, 이는 사실상 대상 블록을 지정하기 위한 슬롯이 하나 더 추가된 대형 입력 버스입니다. 대상 블록을 조각 버스 안에 실제로 배치해야 하므로, 일반 입력 버스에서 프로그램된 회로를 사용하는 것보다 좋은 대안은 아닙니다. 조각 버스에는 세 가지 티어(LV, MV, HV)가 있으며, 유일한 차이는 슬롯 수(32, 48, 64)입니다. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15554"/><ItemImage id="gregtech:gt.blockmachines:15554"/>
- 40-48 <ItemLink id="miscutils:gtplusplus.blockcasings.5:5"/><ItemImage id="miscutils:gtplusplus.blockcasings.5:5"/>
- 37 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 18 티어 유리 (아무 것이나) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1 <ItemLink id="IC2:blockFenceIron"/><ItemImage id="IC2:blockFenceIron"/>
- 1 <ItemLink id="gregtech:gt.blockcasings5"/><ItemImage id="gregtech:gt.blockcasings5"/>
- 1+ 에너지 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 조각 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:31778"/>
- 0+ 출력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">산업용 3D 복사기</Color>는 케이싱, 프레임 박스, 유리, 버스/해치를 절약하기 위해 각 면의 벽을 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 기계 사이에서 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">산업용 3D 복사기</Color>는 단일블록 자동 조각기에서 직접 업그레이드한 기계로, 300% 속도로 작동하고, 일반적으로 필요한 EU/t의 75%만 사용하며, 전압 티어당 16개의 병렬 처리를 제공합니다. 이는 다음 표에서 볼 수 있습니다.

### 병렬 처리:

| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| -------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |


모든 조각 레시피는 기본 지속 시간이 1.0초이며, 오버클럭이나 속도 보너스가 적용되기 전에는 16 EU/t(LV)를 소비합니다. <Color id="GREEN">산업용 3D 복사기</Color>는 조각 버스를 사용하지 않는 한 레시피의 출력을 결정하기 위해 프로그램된 회로를 사용합니다. 조각 버스를 사용하는 경우에는 대신 대상 블록이 필요합니다. 후자는 권장되지 않습니다. 왜냐하면 반드시 제작해서 조각 버스 안에 실제로 배치해야 하며--NEI에서 끌어다 놓는 것은 작동하지 않기 때문입니다. 대상 블록이 지정되지 않으면 기계는 다음으로 사용 가능한 조각 레시피를 기본값으로 사용합니다.