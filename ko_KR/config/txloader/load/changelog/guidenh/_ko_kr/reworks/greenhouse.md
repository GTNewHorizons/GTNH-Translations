---
item_ids:
  - gregtech:gt.blockmachines:12792
navigation:
  title: 익스트림 산업용 온실
  parent: reworks.md
  icon: gregtech:gt.blockmachines:12792
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-16
---

# 익스트림 산업용 온실

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:12792"/>
</GameScene>
<Color id="GREEN">익스트림 산업용 온실(EIG)</Color>은 거대한 농장 없이 수천 개의 작물을 재배하기 위한 IV 티어 멀티블록입니다. 모든 씨앗은 기계 내부에서 재배 및 수확되며 실제 세계에 배치되지 않으므로 TPS를 절약하고 물류를 단순화합니다. <Color id="GREEN">EIG</Color>의 용량은 에너지 해치의 티어, 따라서 유리의 티어에 의해 결정됩니다. <Color id="RED">CropsNH</Color> 씨앗은 지원되지 않으며 대신 산업용 농장에서 재배해야 합니다. 물은 항상 필요하며, 씨앗이 1000개를 초과하면 Weed-EX가 필요합니다. 그렇지 않으면 작업할 때마다 약 1%의 씨앗이 소멸됩니다. 비료는 선택 사항이며 수확당 총 작물 수를 증가시킵니다. 

<br clear="all"/>

> [!NOTE]
> 이제 <Color id="GREEN">EIG</Color>는 겉보기도... 음, 온실처럼 보일 뿐만 아니라 자동 토지 준비 기능까지 갖추었습니다! 구조물 검사가 완료되면 흙을 자동으로 경작하고 내부에 물 블록을 배치합니다.
> 또한 이제 다른 멀티블록과 동일한 방식으로 자동 배치를 완전히 지원합니다!<ItemImage id="structurelib:item.structurelib.constructableTrigger" />


## 건설
<Color id="GREEN">EIG</Color>에는 티어가 적용되는 구성 요소가 하나 있습니다. 유리가 에너지 해치의 최대 티어를 결정합니다. 버스/해치는 구조물 어디에서든 무균 농장 케이싱을 대체할 수 있습니다. <Color id="RED">멀티 앰프 및 레이저 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 일반 에너지 해치를 사용할 수 있습니다. <Color id="GREEN">EIG</Color> 내부의 흙 블록은 RandomThings 모드의 비료 처리된 흙이어야 하며, 램프는 ProjectRed Illumination 모드의 보라색 램프여야 합니다. 램프는 다른 색상일 수 없지만, 전원을 공급하거나 반전할 수 있습니다. 구조물이 형성되면 흙은 경작되고 물은 무료로 생성되므로 수동으로 배치할 필요가 없습니다. 물 공급에는 입력 해치보다 <ItemLink id="gregtech:gt.blockmachines:12972" /> <ItemImage id="gregtech:gt.blockmachines:12972" /> 사용을 권장합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용해 하위 채널 "glass"로 구조물을 시각화/건설하여 유리의 티어를 지정하십시오. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:12792" /> <ItemImage id="gregtech:gt.blockmachines:12792"/>
- 티어 유리 102개(전압 티어와 일치) <ItemImage id="bartworks:BW_GlasBlocks:15" />
- 70-85개 <ItemLink id="miscutils:gtplusplus.blockcasings.2:15" /> <ItemImage id="miscutils:gtplusplus.blockcasings.2:15" />
- 33개 <ItemLink id="gregtech:gt.blockframes:316" /> <ItemImage id="gregtech:gt.blockframes:316" />
- 21개 <ItemLink id="RandomThings:fertilizedDirt" /> <ItemImage id="RandomThings:fertilizedDirt" />
- 보라색 램프 3개(ProjectRed Illumination, 일반 또는 반전)

- 에너지 해치 1개 이상(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 정비 해치 1개(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 0개 이상(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 입력 해치 0개 이상(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 버스 0개 이상(모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">EIG</Color>는 케이싱, 유리, 프레임 박스, 버스/해치를 절약하기 위해 각 측면을 벽 공유할 수 있습니다. 여기에는 물을 공급하기 위한 저수조 해치도 포함됩니다. 

## 사용법
<Color id="GREEN">EIG</Color>에는 아래에 나열된 세 가지 작동 모드가 있습니다. 컨트롤러 내부의 설정 메뉴에서 모드를 전환하거나, 스크루드라이버로 컨트롤러를 우클릭하여 전환할 수 있습니다. 기계가 비활성화된 동안에는 현재 모드에 관계없이 컨트롤러의 GUI를 통해 씨앗을 넣거나 꺼낼 수 있습니다. 작동 모드는 추가 씨앗을 생성하지 않고 제품만 생성합니다.

- <Color id="GREEN">입력</Color> - 입력 버스를 통해 EIG에 씨앗(및 필요한 블록)을 넣습니다. 전력을 소비하지 않습니다.
- <Color id="RED">작동</Color> - 씨앗을 재배하고 작물을 수확합니다. 에너지 해치 1개로 1A의 전력을 소비하거나, 에너지 해치 2개로 4A의 전력을 소비합니다.
- <Color id="BLUE">출력</Color> - 출력 버스를 통해 EIG에서 씨앗(및 필요한 블록)을 꺼냅니다. 전력을 소비하지 않습니다.

설정 메뉴의 IC2 모드는 GTNH 2.9에서 폐지되기 전까지 IC2 씨앗 주머니용이었습니다. 이제는 습도 모드와 함께 아무 기능도 하지 않으며, 기계를 작동하려면 비활성화해야 합니다. CropsNH 씨앗은 지원되지 않으며 대신 산업용 농장에서 재배해야 합니다.