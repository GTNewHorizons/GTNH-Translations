---
item_ids: 
  - gregtech:gt.blockmachines:15565
navigation:
  title: 극저온 냉동기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15565
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 극저온 냉동기 

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15565"/>
</GameScene>

<Color id="GREEN">극저온 냉동기(CF)</Color>는 뜨거운 주괴와 유체를 대량으로 냉각하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">CF</Color>는 <Color id="BLUE">300%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="GREEN">90%</Color>만 사용하며, 고정 <Color id="RED">16</Color> 병렬 처리를 제공하므로 진공 냉동기의 직접적인 업그레이드입니다. <Color id="GREEN">CF</Color>는 작동 중 전용 크라이오테움 냉각 해치를 통해 차가운 크라이오테움을 10 L/s 소비합니다. 이것이 바닥나면 기계는 즉시 작동이 중단되고 무작위 유지보수 문제가 발생합니다. [흡열 냉장고](../multis/endothermic_fridge.md)는 256 병렬(4회 이상 오버클럭)을 최대한 활용하거나 아공간 냉각을 사용할 수 있을 때만 극저온 냉동기보다 더 나은 성능을 냅니다. 
<br clear="all"/>

> [!NOTE]
> 다음 변경 사항이 멀티블록에 적용되었습니다(구조 제외):
> - 속도 향상: 220% -> 300%
> - 병렬 처리 증가: 8 -> 16

## 건설
<Color id="GREEN">극저온 냉동기</Color>에는 티어별 부품이 없습니다. 버스/해치는 구조물의 어느 위치에서든 어떤 케이싱이든 대체할 수 있습니다. <Color id="RED">멀티앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설하십시오. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15565"/><ItemImage id="gregtech:gt.blockmachines:15565"/>
- 46-56 <ItemLink id="miscutils:gtplusplus.blockcasings.3:10"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:10"/>
- 24 <ItemLink id="miscutils:blockFrameGtGrisium"/><ItemImage id="miscutils:blockFrameGtGrisium"/>
- 1+ <ItemLink id="gregtech:gt.blockmachines:967"/><ItemImage id="gregtech:gt.blockmachines:967"/>
- 1+ 에너지 해치(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치(케이싱 무관) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">극저온 냉동기</Color>는 케이싱, 프레임 박스 및 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__두__</u> 대의 기계 사이에 <u>__하나__</u>의 에너지 해치를 공유할 수 있습니다. 

## 사용법
<Color id="GREEN">극저온 냉동기</Color>는 300% 속도로 작동하고, 일반적으로 필요한 EU/t의 90%만 사용하며, 고정 16 병렬 처리를 제공하므로 진공 냉동기의 직접적인 업그레이드입니다.

<Color id="GREEN">극저온 냉동기</Color>는 작동 중 전용 크라이오테움 냉각 해치를 통해 차가운 크라이오테움을 10 L/s 소비합니다. 이것이 바닥나면 기계는 즉시 작동이 중단되고 무작위 유지보수 문제가 발생합니다. 크라이오테움은 주로 유로파의 진화한 차가운 블레이즈나 크라이오테움 벌에서 얻습니다. 필요하다면 블레이즈 가루로 블리즈 가루를 만들 수도 있습니다.