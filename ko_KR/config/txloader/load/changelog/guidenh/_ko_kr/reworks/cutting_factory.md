---
item_ids:
  - gregtech:gt.blockmachines:15540
navigation:
  title: 산업용 절단 공장
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15540
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---
# 산업용 절단 공장

<GameScene wrap="square" align="right">
  <ImportStructure src="../assets/reworks/cutting.snbt"/>
</GameScene>

<Color id="GREEN">산업용 절단 공장(ICF)</Color>은 막대, 웨이퍼, 블록 등을 절단하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">ICF</Color>는 단일블록 절단기에서 바로 업그레이드한 기계로, 최대 <Color id="BLUE">450%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="RED">60%</Color>만 소모하며, 전압 티어당 최대 <Color id="GREEN">6</Color>개의 병렬 처리를 제공합니다. 정확한 보너스와 에너지 해치의 최대 티어는 컨트롤러에 장착된 톱날의 티어에 따라 달라집니다. 톱날은 하나만 필요하며 네 가지 티어 모두 내구도가 무한합니다. 즉, 기계를 업그레이드하는 데 한 번만 비용을 지불하면 됩니다. 초월 금속 톱날 <ItemImage id="gregtech:gt.metaitem.01:32105"/>은 가장 강력하며, 일반 에너지 해치 대신 다중 앰프 에너지 해치 하나를 사용할 수 있게 해줍니다. 동일한 기계 안에서 서로 다른 프로그램 회로 및/또는 비소모품을 사용하려면 <Color id="GREEN">ICF</Color>에서 입력 분리를 활성화해야 합니다.
<br clear="all"/>

> [!NOTE]
> 멀티블록에 다음과 같은 변경 사항이 적용되었습니다(구조 제외):
> - 병렬 처리: 이제 전압 티어와 무관하며, 사용된 톱날에 연동됩니다(최대 6개, 이전 4개)
> - 속도: 마찬가지로 톱날에 연동됩니다(최대 450%, 이전 300%)
> - 전력: 역시 톱날에 연동됩니다(최소 60%, 이전 75%)

## 건설
<Color id="GREEN">ICF</Color>에는 티어별 부품이 없습니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 아무런 영향을 주지 않습니다. 버스/해치는 구조물 어디에서든 케이싱을 대체할 수 있습니다. <Color id="RED">레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. 초월 금속 톱날을 사용하는 경우 <Color id="GREEN">다중 앰프 에너지 해치</Color> 하나를 허용합니다. 컨트롤러에 스크루드라이버를 사용하면 애니메이션을 비활성화할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "glass"로 구조물을 시각화/건설하면 유리의 티어를 지정할 수 있습니다.

### 필요 부품:
- 1 <ItemLink id="gregtech:gt.blockmachines:15540"/><ItemImage id="gregtech:gt.blockmachines:15540"/>
- 10-30 <ItemLink id="miscutils:gtplusplus.blockcasings.2:13"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:13"/>
- 18 <ItemLink id="miscutils:blockFrameGtTantalumCarbide"/><ItemImage id="miscutils:blockFrameGtTantalumCarbide"/>
- 13 <ItemLink id="gregtech:gt.sheetmetal:334"/><ItemImage id="gregtech:gt.sheetmetal:334"/>
- 1개 이상 에너지 해치 (모든 프레임, 티어는 톱날에 의해 제한됨) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 프레임) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (모든 프레임) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0개 이상 입력 버스 (모든 프레임) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상 입력 해치 (모든 프레임) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상 출력 버스 (모든 프레임) <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유
<Color id="GREEN">ICF</Color>는 케이싱, 프레임 박스, 유리, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유하는 것이 가능합니다.

## 사용법
<Color id="GREEN">ICF</Color>는 단일블록 절단기에서 바로 업그레이드한 기계로, 최대 450% 속도로 작동하고, 일반적으로 필요한 EU/t의 60%만 소모하며, 전압 티어당 최대 6개의 병렬 처리를 제공합니다. 정확한 보너스와 에너지 해치의 최대 티어는 컨트롤러에 장착된 톱날의 티어에 따라 달라집니다.

<Color id="GREEN">ICF</Color>에서 레시피를 실행하려면 컨트롤러에 톱날이 필요합니다. 네 가지 티어 모두 내구도가 무한합니다. 즉, 기계를 업그레이드하는 데 한 번만 비용을 지불하면 됩니다. 컨트롤러에 여러 개를 겹쳐 넣어도 기계 작동에는 아무런 영향이 없습니다. 초월 금속 톱날은 가장 강력하며, 일반 에너지 해치 대신 다중 앰프 에너지 해치 하나를 사용할 수 있게 해줍니다.

<Color id="GREEN">ICF</Color>에서 입력 분리를 활성화하면 서로 다른 입력 버스에 있는 고체 재료가 동일한 레시피에 사용되는 것을 막을 수 있습니다. 여기에는 프로그램 회로나 슬라이서 블레이드도 포함됩니다. 즉, 입력 버스가 여러 개인 <Color id="GREEN">ICF</Color> 하나로 여러 가지 프로그램 회로를 동시에 지원할 수 있습니다. 최소 절단 공장 프레임 개수 이상을 유지하는 것만 잊지 마십시오. 액체 재료는 입력 해치에 색상이 지정되지 않은 한 입력 분리 여부와 관계없이 항상 공유됩니다.