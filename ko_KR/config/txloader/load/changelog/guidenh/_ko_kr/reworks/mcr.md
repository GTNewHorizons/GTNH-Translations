---
navigation:
  title: 거대 화학 반응기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15515
categories:
    - 구조 개편
author: Skorched
date: 2026-05-23
---

# 거대 화학 반응기 

<GameScene wrap="square">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15515"/>
</GameScene>
<Color id="GREEN">거대 화학 반응기</Color>는 더 크고 더 발전된 화학 반응을 수행하기 위한 LuV 티어 멀티블록입니다. <Color id="GREEN">MCR</Color>은 <Color id="RED">256</Color>개의 병렬 처리를 제공하고, 본격적인 오버클럭을 위한 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>를 지원하며, <Color id="BLUE">무제한</Color> 티어 건너뛰기를 가지므로 대형 화학 반응기<ItemImage id="gregtech:gt.blockmachines:1169"/>에서 직접 업그레이드한 것입니다. 즉, 전력이 충분하기만 하면 전압에 관계없이 모든 레시피를 실행할 수 있습니다. 확장성이 매우 뛰어나므로 몇 개만 건설하게 될 것입니다. 

<br clear="all"/>

> [!NOTE]
> 거대 화학 반응기의 주요 변경 사항은 다음과 같습니다:
> - 해치 제한이 제거되어 이제 케이싱의 어디에나 어떤 해치든 배치할 수 있습니다! (구조물당 에너지 해치는 여전히 하나로 제한됩니다)
> - <ItemLink id="gregtech:gt.blockmachines:1169" />와 구별하기 위한 새로운 오버레이 텍스처가 있습니다.
> - (선택 사항인) <ItemLink id="gregtech:gt.blockcasings5:13" /> <ItemImage id="gregtech:gt.blockcasings5:13" />는 이제 기계가 작동 중일 때 빛납니다.


## 건설
<Color id="GREEN">MCR</Color>에는 하나의 티어 구성 요소가 있습니다. 유리는 에너지 해치의 최대 티어를 결정하지만, 앰프에는 제한이 없습니다. 원한다면 핵융합 코일 블록을 영구 가열 코일로 교체할 수 있습니다. 버스/해치는 구조물 어디에서나 화학적으로 불활성인 기계 케이싱을 대체할 수 있습니다. <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>는 본격적인 오버클럭을 위해 지원되지만, 후자는 최소 UV 티어 유리가 필요합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "glass"를 사용해 유리의 티어를 지정하면서 구조물을 시각화/건설하십시오. 
### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15515"/><ItemImage id="gregtech:gt.blockmachines:15515"/>
- 0-79 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 64 티어 유리 <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 28 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings4:7"/><ItemImage id="gregtech:gt.blockcasings4:7"/>
- 1+ 에너지 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ 입력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (모든 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />
### 벽 공유
<Color id="GREEN">MCRs</Color>는 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 병렬 처리나 오버클럭이 아직 남아 있는 동안 기계가 가능한 한 많은 앰프를 끌어오므로 에너지 해치는 공유하지 마십시오. 
## 사용법
<Color id="GREEN">MCR</Color>은 256개의 병렬 처리를 제공하고, 본격적인 오버클럭을 위한 다중 앰프 및 레이저 에너지 해치를 지원하며, 무제한 티어 건너뛰기를 가지므로 대형 화학 반응기에서 직접 업그레이드한 것입니다. 즉, 전력이 충분하기만 하면 전압에 관계없이 모든 레시피를 실행할 수 있습니다.