---
item_ids:
  - gregtech:gt.blockmachines:15533
navigation:
  title: 대형 연소 엔진
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15533
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대형 연소 엔진
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15533"/>
</GameScene>
<Color id="GREEN">대형 연소 엔진(LCE)</Color>은 가연성 연료로 전력을 생산하는 EV 티어 멀티블록입니다. <Color id="GREEN">LCE</Color>는 단일블록 연소 발전기에서 직접 업그레이드한 것으로, 연료 효율이 훨씬 높고 1A를 초과하는 전력을 출력할 수 있습니다. 하지만 <Color id="GREEN">LCE</Color>는 작동하려면 윤활유 1,000 L/h를 공급해야 하며, 선택적으로 기계를 부스트하기 위해 산소 40 L/s를 공급할 수 있습니다. 부스트는 최대 전력 출력을 3배로 만들고 연료 효율을 100%에서 150%로 증가시키므로 적극 권장합니다. 전력은 기계 뒷면의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수지 마십시오. 그렇지 않으면 폭발합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">LCE</Color>를 자동 전환하여 연료를 절약하십시오. <Color id="GREEN">LCE</Color>는 IV에서 익스트림 연소 엔진 <ItemImage id="gregtech:gt.blockmachines:15534"/> 및 범용 화학 연료 엔진 <ItemImage id="gregtech:gt.blockmachines:15535"/>으로 대체됩니다. 

[GTNH 전력 계획기](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 구조 자체만 변경되었으며, 멀티블록의 핵심 기능은 이전과 동일합니다.

## 건설
<Color id="GREEN">LCE</Color>에는 티어별 구성 요소가 없습니다. 정비 해치와 소음기 해치는 기어박스 케이싱에 닿지 않는 안정적인 티타늄 기계 케이싱을 대체할 수 있습니다. 입력 해치(들)는 기어박스 케이싱에 닿아 있는 안정적인 티타늄 기계 케이싱을 대체할 수 있습니다. 4중 입력 해치는 필요한 모든 유체를 주입하는 데 유용할 수 있습니다. 다이너모 해치는 컨트롤러 반대편인 구조물 오른쪽의 중앙 케이싱으로 제한되며, 4A를 초과할 수 없습니다. 또한 엔진 흡기 케이싱 앞에는 반드시 공기가 있어야 합니다. 구조물을 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15533"/><ItemImage id="gregtech:gt.blockmachines:15533"/>
- 21 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 19 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 10-15 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 8 <ItemLink id="gregtech:gt.blockcasings4:13"/><ItemImage id="gregtech:gt.blockcasings4:13"/>
- 4 <ItemLink id="gregtech:gt.blockcasings2:4"/><ItemImage id="gregtech:gt.blockcasings2:4"/>
- 1 다이너모 해치(오른쪽 중앙 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 정비 해치(기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ 입력 해치(기어박스 옆이 아닌 아무 티타늄 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />

### 벽 공유
<Color id="GREEN">LCE</Color>들은 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 입력 해치는 위치 제한 때문에 여기에 포함되지 않습니다. 

## 사용법
<Color id="GREEN">LCE</Color>는 가연성 디젤 연료로 전력을 생산합니다. 가장 많이 쓰이는 연료는 경질 연료, 디젤, 세탄 부스트 디젤입니다. 제트 연료 A와 고옥탄 가솔린도 상당히 흔하지만, 일반적으로는 대신 익스트림 연소 엔진이나 범용 화학 연료 엔진에서 사용됩니다. 마지막 두 연료는 에너지 값이 너무 높아 기본 모드에서는 사용할 수 없습니다. 

<Color id="GREEN">LCE</Color>에는 아래에 나열된 두 가지 작동 모드가 있습니다. 기계는 사용 가능한 입력에 따라 자동으로 두 모드 사이를 전환합니다. 부스트는 최대 EU/t를 3배로 만들고 연료 효율을 100%에서 150%로 증가시키므로 적극 권장합니다. 산소를 유지하는 것은 어렵지 않습니다. 간단히 사탕무 또는 스위드 농장을 짓고 설탕을 전기분해하십시오.

_기본_
- 입력: 연료 + 윤활유 1,000 L/h
- 출력: 연료 효율 100%에서 최대 2,048 EU/t.

_부스트_
- 입력: 연료 + 윤활유 1,000 L/h + 산소 40 L/s
- 출력: 연료 효율 150%에서 최대 6,144 EU/t.

<Color id="GREEN">LCE</Color>에는 기계의 전력 출력에 정비례하는 자체 효율 값도 있습니다. <Color id="GREEN">LCE</Color>의 효율은 기계가 작동하는 동안 선형으로 증가하며, 기계가 유휴 상태가 되면 거의 즉시 0%로 초기화됩니다. 최대 효율에 도달하는 데 33초(기본) 또는 100초(부스트)가 걸립니다. 컨트롤러에 휴대용 스캐너를 사용하거나 WAILA의 효율 값을 확인하여 현재 효율을 볼 수 있습니다.

<Color id="GREEN">LCE</Color>는 가능한 한 오래 가동해야 하지만 영원히 가동해서는 안 됩니다. 다이너모 해치가 가득 차면 추가 EU가 소멸되기 때문입니다. 해결책은 라포트로닉 슈퍼커패시터 또는 배터리 버퍼에 연결된 RS 래치로 <Color id="GREEN">LCE</Color>를 자동 전환하는 것입니다.