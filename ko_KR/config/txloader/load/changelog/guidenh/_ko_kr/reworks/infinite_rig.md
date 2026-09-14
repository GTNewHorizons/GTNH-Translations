---
item_ids:
  - gregtech:gt.blockmachines:15567
navigation:
  title: 무한 유체 시추기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15567
categories:
    - 구조물 리워크
author: Skorched
date: 2026-05-27
---

# 무한 유체 시추기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15567"/>
</GameScene>
<Color id="GREEN">무한 유체 시추기(IFDR)</Color>는 기반암 아래의 거대한 유체 저장소를 채취하기 위한 UHV 티어 멀티블록입니다. 유체 저장소는 일반 청크 8x8 크기이며, 특히 행성이나 차원이 다를 때 유체의 종류와 양이 크게 다릅니다. 탐사 스캐너로 기반암을 우클릭하거나 지진 탐사기를 사용하여 유체 저장소를 탐사하고 그 정보를 Journey Map에 추가하십시오. <Color id="GREEN">IFDR</Color>은 전체 저장소에 걸쳐 무한한 양의 유체를 채취할 수 있습니다. 유체가 추출되는 속도는 최소 전압 티어보다 높은 전압 티어의 수와 작동 범위 내 남은 유체 양에 따라 결정됩니다. 장거리 유체 파이프라인, ME 양자 링, 또는 엔더 탱크를 사용하여 기지로/기지에서 유체를 운송하십시오. 
<br clear="all"/>

> [!NOTE]
> 구조물 외에 멀티블록에 다음과 같은 변경 사항이 적용되었습니다: 
> - 병렬 증가: UHV보다 높은 에너지 티어마다 병렬 +2

## 건설
<Color id="GREEN">IFDR</Color>에는 티어 부품이 없습니다. 컨트롤러 및/또는 입력 버스에 채굴 파이프를 넣으십시오. 채굴 파이프는 구조물의 중앙 블록 아래 월드에 실제로 생성되며, 기반암까지 곧바로 내려가면서 경로에 있는 모든 것을 파괴합니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않으며, 일반 에너지 해치는 단 하나만 허용됩니다. <Color id="GREEN">IFDR</Color>의 각 티어는 작동에 최소 전압도 필요로 합니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 비를 맞으면 폭발하지 않도록 기계에 덮개를 씌우는 것을 잊지 마십시오! <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오. 

### 필요 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15567"/><ItemImage id="gregtech:gt.blockmachines:15567"/>
- 90-103 <ItemLink id="gregtech:gt.blockcasings8:2"/><ItemImage id="gregtech:gt.blockcasings8:2"/>
- 38 <ItemLink id="gregtech:gt.blockframes:129"/><ItemImage id="gregtech:gt.blockframes:129"/>
- 20 티어 유리 (아무 종류) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings8:7"/><ItemImage id="gregtech:gt.blockcasings8:7"/>
- 12 <ItemLink id="tectech:gt.blockcasingsTT:3"/><ItemImage id="tectech:gt.blockcasingsTT:3"/>
- 9 <ItemLink id="gregtech:gt.blockcasings9"/><ItemImage id="gregtech:gt.blockcasings9"/>
- 8 <ItemLink id="gregtech:gt.sheetmetal:397"/><ItemImage id="gregtech:gt.sheetmetal:397"/>
- 1 에너지 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 정비 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0-1 입력 버스 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 해치 (아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">IFDR</Color>들은 각 면을 벽 공유하여 케이싱, 프레임 박스, 버스/해치를 절약할 수 있습니다. <Color id="GREEN">IFDR</Color>은 전력을 0.875A만 소비하므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계가 공유할 수 있습니다. 

## 사용법
활성화되면 <Color id="GREEN">IFDR</Color>은 먼저 채굴 파이프를 기반암을 향해 곧바로 아래로 전개합니다. 이는 기계의 현재 y좌표에 따라 몇 초가 걸릴 수 있습니다. 필요하다면 컨트롤러 GUI 안의 "채굴 파이프 중단 및 회수" 버튼을 눌러 과정을 즉시 중지하십시오. 출력 버스는 구조물에 추가할 수 없으므로 채굴 파이프는 컨트롤러 내부의 슬롯으로 반환됩니다. 채굴 파이프를 전개하거나 회수하는 동안에는 유체가 채취되지 않습니다.

프로그래밍된 회로를 사용하여 거의 고갈된 유체 저장소/청크를 무시하십시오. <Color id="GREEN">IFDR</Color>은 작업(사이클)당 리터 수가 프로그래밍된 회로 번호보다 적을 때마다 자동으로 멈추고 채굴 파이프를 회수합니다.

<Color id="GREEN">무한 유체 시추기</Color>는 다음 표에서 볼 수 있듯이 UHV보다 높은 에너지 해치 티어마다 병렬 2를 제공하기 때문에 다른 시추기들과 다릅니다. 전력 패널에는 병렬이 하나만 표시될 수 있지만 펌프 속도는 그에 따라 증가해야 합니다. 

|   | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |
| 병렬 | 1 | 3 | 5 | 7 | 9 | 11 | 13 |