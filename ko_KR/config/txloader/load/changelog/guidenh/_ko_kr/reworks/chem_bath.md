---
item_ids:
  - gregtech:gt.blockmachines:15551
navigation:
  title: 산업용 화학 조욕기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15551
categories:
    - Structure Reworks
author: Skorched
date: 2026-05-27
---

# 산업용 화학 조욕기

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15551"/>
</GameScene>
<Color id="GREEN">산업용 화학 조욕기(ICB)</Color>는 다양한 재료를 화학적으로 조욕하기 위한 EV 티어 멀티블록입니다. <Color id="GREEN">ICB</Color>는 단일블록 화학 조욕기에서 곧바로 업그레이드된 설비로, <Color id="RED">500%</Color> 속도로 작동하며 전압 티어당 <Color id="BLUE">4</Color>개의 병렬 처리를 제공합니다.

<br clear="all"/>

> [!NOTE]
> 이 멀티블록에는 다음과 같은 변경 사항이 적용되었습니다(구조물은 제외):
> - 분리: 광석 세척기가 (이 설비와 같은) 개별 구조물로 분리되었습니다!

## 건설
<Color id="GREEN">ICB</Color>에는 티어 부품이 없습니다. 버스/해치는 구조물 어디에 있는 세척기 케이싱이든 대체할 수 있습니다. <Color id="GREEN">다중 앰페어 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 일반 에너지 해치를 여러 개 둘 수 있습니다. 물은 기계를 초기화하는 데 한 번만 소모되며, 저수조 해치나 입력 해치를 통해 구조물에 공급됩니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오.

### 필요 부품:
- 1 <ItemLink id="gregtech:gt.blockmachines:15551"/><ItemImage id="gregtech:gt.blockmachines:15551"/>
- 30-38 <ItemLink id="miscutils:gtplusplus.blockcasings.2:4"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:4"/>
- 20 <ItemLink id="miscutils:blockFrameGtWatertightSteel"/><ItemImage id="miscutils:blockFrameGtWatertightSteel"/>
- 4 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 2 <ItemLink id="gregtech:gt.blockmetal8:6"/><ItemImage id="gregtech:gt.blockmetal8:6"/>
- 2 <ItemLink id="gregtech:gt.blockmetal2:7"/><ItemImage id="gregtech:gt.blockmetal2:7"/>
- 1개 이상 에너지 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0개 이상 출력 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">ICB</Color>는 각 면을 벽 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 여기에는 물을 공급하기 위한 저수조 해치도 포함됩니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에서 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다.

## 사용법
<Color id="GREEN">ICB</Color>는 단일블록 화학 조욕기에서 곧바로 업그레이드된 설비로, 다음 표에서 볼 수 있듯이 500% 속도로 작동하며 전압 티어당 4개의 병렬 처리를 제공합니다.


| LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
| 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 |