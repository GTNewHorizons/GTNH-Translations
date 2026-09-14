---
item_ids:
  - gregtech:gt.blockmachines:15534
navigation:
  title: 익스트림 연소 엔진
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15534
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 익스트림 연소 엔진

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15534"/>
</GameScene>
<Color id="GREEN">익스트림 연소 엔진(ECE)</Color>은 가연성 연료로 전력을 생산하는 IV 티어 멀티블록입니다. <Color id="GREEN">ECE</Color>는 <Color id="GREEN">대형 연소 엔진</Color>의 직접적인 업그레이드로, 5배 이상의 전력을 출력할 수 있습니다. 하지만 <Color id="GREEN">ECE</Color>가 작동하려면 8,000 L/h의 윤활유가 공급되어야 하며, 선택적으로 기계를 부스트하기 위해 40 L/s의 액체 산소가 필요합니다. 부스트는 최대 전력 출력을 3배로 늘리고 연료 효율을 100%에서 150%로 증가시키므로 적극 권장합니다. 전력은 기계 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수지 마십시오. 그렇지 않으면 폭발합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">ECE</Color>를 자동으로 켜고 끄면 연료를 절약할 수 있습니다. <Color id="GREEN">ECE</Color>는 생산할 수 있는 전력량에 제한이 없는 범용 화학 연료 엔진 <ItemImage id="gregtech:gt.blockmachines:15535"/>로 대체됩니다.

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 이 멀티블록에서 변경된 점은 구조뿐이며, 핵심 기능은 이전과 동일합니다

## 건설
<Color id="GREEN">ECE</Color>는 티어 구성 요소가 없습니다. 정비 해치와 소음기 해치는 기어박스 케이싱에 닿지 않은 견고한 텅스텐강 기계 케이싱을 대체할 수 있습니다. 입력 해치(들)는 기어박스 케이싱에 닿아 있는 텅스텐강 터빈 케이싱을 대체할 수 있습니다. 4중 입력 해치는 필요한 모든 유체를 투입하는 데 유용할 수 있습니다. 다이너모 해치는 구조물 오른쪽, 컨트롤러 반대편의 중앙 케이싱으로 제한되며 4A를 초과할 수 없습니다. 또한 익스트림 엔진 흡기 케이싱 위에는 공기가 필수로 있어야 합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15534"/><ItemImage id="gregtech:gt.blockmachines:15534"/>
- 30-33 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 32 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 30 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 12 <ItemLink id="gregtech:gt.blockcasings3:15"/><ItemImage id="gregtech:gt.blockcasings3:15"/>
- 12 <ItemLink id="gregtech:gt.blockcasings8:4"/><ItemImage id="gregtech:gt.blockcasings8:4"/>
- 4-7 <ItemLink id="gregtech:gt.blockcasings4:12"/><ItemImage id="gregtech:gt.blockcasings4:12"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 다이너모 해치 1개 (오른쪽 중앙 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 정비 해치 1개 (기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개 (기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 해치 1개 이상 (기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />

### 벽 공유
<Color id="GREEN">ECE들</Color>은 케이싱을 절약하기 위해 각 면을 벽 공유할 수 있습니다. 단, 입력 해치는 위치 제한 때문에 포함되지 않습니다. 

## 사용법
<Color id="GREEN">ECE</Color>는 제한된 종류의 가연성 디젤 연료로 전력을 생산합니다. 다음 표는 사용 가능한 옵션과 밀도(EU/L)를 나열합니다. 가장 인기 있는 옵션은 제트 연료 A와 고옥탄 가솔린입니다. 둘 다 일반적으로 범용 화학 연료 엔진에서도 사용됩니다.
| 디젤 연료 | EU/L | 기본 소비율 | 부스트 소비율 |
| --------------- | --------------- | --------------- | --------------- |
| 제트 연료 No.3 | 1,824 | 5.98 L/t | 12.0 L/t |
| 제트 연료 A | 1,248 | 4.85 L/t | 9.70 L/t |
| 고옥탄 가솔린 | 2,500 | 4.36 L/t | 8.72 L/5 |


<Color id="GREEN">ECE</Color>에는 아래에 나열된 두 가지 작동 모드가 있습니다. 기계는 사용 가능한 입력에 따라 자동으로 두 모드 사이를 전환합니다. 부스트는 최대 EU/t를 3배로 늘리고 연료 효율을 100%에서 150%로 증가시키므로 적극 권장합니다. 액체 산소를 유지하는 것은 어렵지 않습니다. 전용 진공 냉동기 <ItemImage id="gregtech:gt.blockmachines:1002"/> 또는 [행성 가스 사이펀](./siphon.md) <ItemImage id="gregtech:gt.blockmachines:15559"/>를 건설하면 됩니다.

_기본_
- 입력: 연료 + 8,000 L/h 윤활유.
- 출력: 연료 효율 100%에서 최대 10,900 EU/t.

_부스트_
- 입력: 연료 + 8,000 L/h 윤활유 + 40 L/s 액체 산소.
- 출력: 연료 효율 150%에서 최대 32,700 EU/t.

<Color id="GREEN">ECE</Color>에는 기계의 전력 출력에 정비례하는 자체 효율 값도 있습니다. <Color id="GREEN">ECE</Color>의 효율은 기계가 작동하는 동안 선형으로 증가하며, 기계가 유휴 상태가 되면 거의 즉시 0%로 초기화됩니다. 최대 효율에 도달하는 데 25초(기본) 또는 75초(부스트)가 걸립니다. 컨트롤러에 휴대용 스캐너 <ItemImage id="gregtech:gt.metaitem.01:32762"/>를 사용하거나 WAILA에서 효율 값을 확인하여 현재 효율을 볼 수 있습니다.

<Color id="GREEN">ECE</Color>는 가능한 한 오래 작동해야 하지만, 다이너모 해치가 가득 차면 추가 EU가 소멸되므로 영원히 작동해서는 안 됩니다. 해결책은 라포트로닉 슈퍼커패시터 또는 배터리 버퍼에 연결된 RS 래치로 <Color id="GREEN">ECE</Color>를 자동으로 켜고 끄는 것입니다.