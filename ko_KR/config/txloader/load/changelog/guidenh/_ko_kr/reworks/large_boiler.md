---
item_ids:
  - gregtech:gt.blockmachines:15529
  - gregtech:gt.blockmachines:15530
  - gregtech:gt.blockmachines:15531
  - gregtech:gt.blockmachines:15532
navigation:
  title: 대형 보일러
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15529
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---

# 대형 보일러

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15529"/>
</GameScene>
<Color id="GREEN">대형 보일러</Color>는 가연성 연료를 연소시켜 물을 증기 또는 과열 증기로 증발시키는 MV 티어 멀티블록입니다. 대형 보일러는 더 좋은 재료가 해금됨에 따라 효율과 처리량을 더욱 향상시키기 위한 네 가지 티어가 있습니다. 밀도가 높은 연료는 더 오래 연소될 뿐만 아니라 총 연소 시간에 비례하는 보너스 틱도 받습니다. 이 보일러는 고체 및 유체 연료를 모두 받을 수 있어 25% 출력 증가를 제공합니다. <Color id="GREEN">대형 보일러</Color>는 궁극적으로 Railcraft 보일러 <ItemImage id="Railcraft:machine.beta:5"/>를 대체하지만, 청동 버전은 최대 처리량이 약간 더 낮습니다. 

[GTNH 전력 계획기](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit)
<br clear="all"/>

> [!NOTE]
> 이전 보일러에서의 변경 사항은 다음과 같습니다 (새 구조 제외):
> - 기본 출력이 20% 증가했습니다.
> - 디젤 연료의 25% 연소 시간 너프가 제거되었습니다.
> - 고체와 유체를 동시에 소비하여 25% 증가 효과를 받을 수 있습니다.
> - 고밀도 디젤 연료가 허용 연료에 추가되었습니다.
> - 보너스 공식이 $$\log(\text{Burn Time} \div 16,000) \times 0.025$$로 변경되었습니다.
> - 보일러는 이제 꺼져 있을 때 초당 0.2%씩 효율을 잃습니다.

## 건설
<Color id="GREEN">대형 보일러</Color>는 네 가지 티어로 제공되지만, 이들 사이의 유일한 구조적 차이는 케이싱 종류와 컨트롤러 자체입니다. 입력 및 출력 해치는 구조물의 어느 위치에 있든 파이프 케이싱에만 설치할 수 있으며, 나머지 버스/해치는 구조물의 어느 위치에 있든 일반 케이싱에만 설치할 수 있습니다. 전력을 소비하지 않으므로 에너지 해치는 없습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>을 사용하여 구조물을 시각화하거나 건설하십시오.

판이 구부리기 기계에서 만들어지고 막대가 줄로 만들어졌다고 가정하면, 대형 청동 보일러 <ItemImage id="gregtech:gt.blockmachines:15529"/>를 건설하는 데 청동 주괴 382개와 벽돌 블록 33개가 필요하지만, 마지막 두 파이프 케이싱을 ULV 입력 해치로 교체하면 총량이 청동 주괴 342개로 줄어듭니다. 대형 강철 보일러 <ItemImage id="gregtech:gt.blockmachines:15530"/>는 막대가 압출기에서 만들어지고 마지막 두 파이프 케이싱이 ULV 입력 해치로 교체되면 건설하는 데 강철 주괴 362개가 필요합니다. 

### 필요:
- 대형 보일러 (티어 컨트롤러) 1개 <ItemImage id="gregtech:gt.blockmachines:15529"/>
- 기계 케이싱 (티어별) 24-36개 <ItemImage id="gregtech:gt.blockcasings:10"/>
- 화실 케이싱 (티어별) 3-11개 <ItemImage id="gregtech:gt.blockcasings3:13"/>
- 파이프 케이싱 (티어별) 0-2개 <ItemImage id="gregtech:gt.blockcasings2:12"/>
- 유지보수 해치 (케이싱 무관) 1개 <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 (케이싱 무관) 1개 <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 버스 (케이싱 무관) 1개 이상 <ItemImage id="gregtech:gt.blockmachines:70" />
- 입력 해치 (케이싱 무관) 0개 이상 <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 해치 (케이싱 무관) 0개 이상 <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">대형 보일러</Color>는 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 여기에는 연료와 물을 위한 입력 버스/해치뿐만 아니라, 공유된 모든 기계의 결합 출력을 담을 만큼 충분히 큰 경우 증기를 위한 출력 해치도 포함됩니다. 

## 사용법
<Color id="GREEN">대형 보일러</Color>는 가연성 연료를 연소시켜 물을 증기 또는 과열(SH) 증기로 증발시킵니다. 밀도가 높은 연료는 자연히 더 오래 연소되며, 총 연소 시간에 비례하는 보너스 틱도 받습니다. 연소 시간이 400 미만인 고체 연료는 대형 청동 보일러에서 허용되지 않으며, 연소 시간이 1,000 미만인 고체 연료는 대형 강철 보일러에서 허용되지 않습니다. 고체 슈퍼 연료와 마법 고체 슈퍼 연료는 대형 티타늄 보일러 또는 대형 텅스텐강 보일러에서 허용되는 유일한 연료입니다.

<Color id="GREEN">대형 보일러</Color>는 작동하지 않을 때 초당 0.2%의 비율로 효율을 잃으므로 높은 가동률을 목표로 하는 것이 이상적입니다. 연소 시간이 긴 연료에는 다음 공식에 따라 보너스가 부여됩니다:

<Latex formula="\text{Time Bonus} = \log (\text{Burn Time} \div 16,000) \times 0.025"/>

물이 소비되는 속도와 증기가 생산되는 속도는 기계의 티어에 따라 고정됩니다. 그러나 대형 청동 보일러 <ItemImage id="gregtech:gt.blockmachines:15529"/>와 대형 강철 보일러 <ItemImage id="gregtech:gt.blockmachines:15530"/>는 일반 증기를 생산하는 반면, 대형 티타늄 보일러 <ItemImage id="gregtech:gt.blockmachines:15531"/>와 대형 텅스텐강 보일러 <ItemImage id="gregtech:gt.blockmachines:15532"/>는 과열(SH) 증기를 생산합니다. [대형 증기 터빈](large_steam_turbine.md)<ItemImage id="gregtech:gt.blockmachines:15524"/>의 출력을 대형 보일러로 다시 순환시킨다면 일반 물 대신 증류수를 사용할 수 있습니다. 유지보수 문제가 하나씩 있을 때마다 생산되는 증기량이 10% 감소합니다.

선택적으로, 컨트롤러 내부에 프로그램된 회로를 배치하여 값당 총 증기 출력을 1,000 L/s 감소시킬 수 있습니다. 예를 들어, 프로그램된 회로 3은 증기 출력을 3,000 L/s 감소시킵니다. LST에서는 더 많은 증기가 항상 더 많은 전력을 생산하므로, 터빈의 최적 유량을 초과하더라도 이것이 유용한 경우는 거의 없습니다. 

| 대형 보일러 | 티어 | 물 | 증기 |
| --------------- | --------------- | --------------- | --------------- |
| 청동 | MV | 5.00 L/t | 800 L/t |
| 강철 | HV | 12.50 L/t | 2,000 L/t |
| 티타늄 | EV | 16.67 L/t | 2,666 L/t (SH) |
| 텅스텐강 | IV | 66.67 L/t | 10,666 L/t (SH) |