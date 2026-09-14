---
item_ids:
  - gregtech:gt.blockmachines:15518
navigation:
  title: 흡열 냉동기
  parent: multis.md
  icon: gregtech:gt.blockmachines:15518
categories:
    - 신규 멀티블록
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 흡열 냉동기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15518" />
</GameScene>
<Color id="GREEN">흡열 냉동기(EnF)</Color>는 뜨거운 주괴와 유체를 대량으로 냉각하기 위한 ZPM 티어 멀티블록입니다. <Color id="GREEN">ENF</Color>는 <ItemLink id="gregtech:gt.blockmachines:1002"/><ItemImage id="gregtech:gt.blockmachines:1002"/>에서 직접 업그레이드한 기계입니다. 최대 <Color id="BLUE">1,200%</Color> 속도로 작동하고, <Color id="RED">256</Color> 병렬 처리를 제공하며, 강력한 오버클럭을 위한 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>를 지원하고, 무제한 티어 스킵이 가능하기 때문입니다. <Color id="GREEN">EnF</Color>는 메가 진공 냉동기를 대체합니다. 즉, 충분한 전력만 있다면 전압 티어에 관계없이 모든 레시피를 실행할 수 있습니다. 속도는 작동 중 천천히 최대 1.5배까지 증가하고, 유휴 상태에서는 다시 1.0배로 감소합니다. 선택적으로, 컨트롤러 GUI에서 크라이오테움 냉각을 활성화하면 젤리드 크라이오테움 250-375 L/s를 소비하는 대가로 속도 계수가 증가하는 비율이 5배가 됩니다. 인피니티 냉각 케이싱으로 구조를 업그레이드하면 아공간 냉각이 해금되며, 이는 엑조틱 냉각재를 대가로 기계 속도와 젤리드 크라이오테움 소비율을 모두 추가로 배가합니다. EnF는 256 병렬 처리(4회 이상 오버클럭)를 최대한 활용하거나 아공간 냉각을 사용할 수 있을 때만 극저온 냉동기 <ItemImage id="gregtech:gt.blockmachines:15565"/>보다 더 뛰어난 성능을 발휘합니다. 또한 [극저온 냉동기](../reworks/cryogenic_freezer.md)는 이러한 새로운 변경 사항에 맞춰 병렬 처리량이 두 배(8->16)로, 속도가 더 높게(220%->300%) 상향되었다는 점도 주목할 만합니다.

<br clear="all"/>

## 건설:
<Color id="GREEN">EnF</Color>는 두 티어로 제공되지만, 두 구조의 유일한 차이는 T2 구조에 추가되는 인피니티 냉각 케이싱 <ItemImage id="gregtech:gt.blockcasings8:14"/>입니다. 유리는 아무 티어나 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조 어디에서든 아무 냉동기 케이싱을 대체할 수 있습니다. 유리 티어에 관계없이 강력한 오버클럭을 위한 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>가 지원됩니다. 구조를 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오. 하위 채널 "glass"로 유리 티어를 지정하고, 한 스택에 든 프로젝터 수로 기계 티어를 지정합니다.

208개의 인피니티 냉각 케이싱을 건설하려면 인피니티 255k (L), 시공간 240k (L), 하이포젠 59.9k (L)가 필요합니다. Mk-IV 핵융합 원자로 레시피에 의존하기보다는 차원 초월 플라즈마 단조기 <ItemImage id="gregtech:gt.blockmachines:1004"/>에서 하이포젠을 제작할 수 있을 때까지 기다리는 것이 권장됩니다.
### T1 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15518"/><ItemImage id="gregtech:gt.blockmachines:15518"/>
- 750-773 <ItemLink id="gregtech:gt.blockcasings14:4"/><ItemImage id="gregtech:gt.blockcasings14:4"/>
- 351 <ItemLink id="gregtech:gt.blockcasings2:1"/><ItemImage id="gregtech:gt.blockcasings2:1"/>
- 148 <ItemLink id="gregtech:gt.blockreinforced:3"/><ItemImage id="gregtech:gt.blockreinforced:3"/>
- 148 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 146 <ItemLink id="gregtech:gt.blockframes:389"/><ItemImage id="gregtech:gt.blockframes:389"/>
- 135 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 51 <ItemLink id="gregtech:gt.blockcasings10:9"/><ItemImage id="gregtech:gt.blockcasings10:9"/>
- 40 <ItemLink id="gregtech:gt.sheetmetal:390"/><ItemImage id="gregtech:gt.sheetmetal:390"/>
- 18 티어 유리 (아무 종류) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 1+ 에너지 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 유지보수 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ 입력 버스 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ 입력 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ 출력 버스 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ 출력 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:60"/>

### T2 요구 사항:

- 1 <ItemLink id="gregtech:gt.blockmachines:15518"/><ItemImage id="gregtech:gt.blockmachines:15518"/>
- 750-773 <ItemLink id="gregtech:gt.blockcasings14:4"/><ItemImage id="gregtech:gt.blockcasings14:4"/>
- 208 <ItemLink id="gregtech:gt.blockcasings8:14"/><ItemImage id="gregtech:gt.blockcasings8:14"/>
- 148 <ItemLink id="gregtech:gt.blockreinforced:3"/><ItemImage id="gregtech:gt.blockreinforced:3"/>
- 148 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 146 <ItemLink id="gregtech:gt.blockframes:389"/><ItemImage id="gregtech:gt.blockframes:389"/>
- 143 <ItemLink id="gregtech:gt.blockcasings2:1"/><ItemImage id="gregtech:gt.blockcasings2:1"/>
- 135 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 51 <ItemLink id="gregtech:gt.blockcasings10:9"/><ItemImage id="gregtech:gt.blockcasings10:9"/>
- 40 <ItemLink id="gregtech:gt.sheetmetal:390"/><ItemImage id="gregtech:gt.sheetmetal:390"/>
- 18 티어 유리 (아무 종류) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 1+ 에너지 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 유지보수 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ 입력 버스 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ 입력 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ 출력 버스 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:80"/>
- 0+ 출력 해치 (아무 냉동기 케이싱) <ItemImage id="gregtech:gt.blockmachines:60"/>

### 벽 공유:
<Color id="GREEN">EnF들</Color>은 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 단, 인피니티 냉각 케이싱은 여기에 포함되지 않습니다.

## 사용법:
<Color id="GREEN">EnF</Color>는 최대 1,200% 속도로 작동하고, 256 병렬 처리를 제공하며, 강력한 오버클럭을 위한 다중 앰프 및 레이저 에너지 해치를 지원하고, 무제한 티어 스킵이 가능하므로 진공 냉동기에서 직접 업그레이드한 기계입니다. 즉, 충분한 전력만 있다면 전압 티어에 관계없이 모든 레시피를 실행할 수 있습니다. 예를 들어, ZPM 256A 레이저 에너지 해치는 UIV 레시피를 실행할 수 있습니다.

<Color id="GREEN">EnF</Color>의 속도 계수는 아래에서 볼 수 있듯이 작동 중 최대 1.5배까지 증가하고, 유휴 상태에서는 다시 1.0배로 감소합니다. 최대 속도 계수에 도달하려면 5분 동안 연속으로 작동해야 하지만, 이를 모두 잃는 데는 20초밖에 걸리지 않습니다. 선택적으로, 컨트롤러 GUI에서 크라이오테움 냉각을 활성화하면 젤리드 크라이오테움 250-375 L/s를 소비하는 대가로 속도 계수가 증가하는 비율을 5배로 만들 수 있습니다. 소비율은 속도 계수에 선형으로 비례하지만, 대신 <Color id="GREEN">EnF</Color>가 단 1분 만에 최대 1.5배 속도 계수에 도달할 수 있게 해줍니다. 크라이오테움 냉각이 활성화된 상태에서 젤리드 크라이오테움이 바닥나면 기계가 즉시 정지하고 현재 레시피를 소멸시킵니다.

- 작동 중 5초당 속도 계수 +0.00833 (크라이오테움 냉각 비활성화), 최대까지 5분
- 작동 중 5초당 속도 계수 +0.04167 (크라이오테움 냉각 활성화), 최대까지 1분
- 유휴 상태에서 초당 속도 계수 -0.025, 최소까지 20초

## 아공간 냉각
인피니티 냉각 케이싱으로 <Color id="GREEN">EnF</Color> 구조를 업그레이드하면 아공간 냉각이 해금되며, 이는 엑조틱 냉각재를 대가로 기계 속도를 즉시 배가합니다. 크라이오테움 냉각이 활성화된 경우, 속도 증가는 젤리드 크라이오테움 소비율에도 적용됩니다. 이것은 앞서 설명한 1.5배 속도 계수와 곱연산으로 중첩되어 최대 1,200% 속도에 도달한다는 점에 유의하십시오. 이 속도 증가는 즉시 적용되므로 최대 도달 시간은 크라이오테움 냉각 없이 5분, 크라이오테움 냉각 사용 시 1분으로 동일합니다. 엑조틱 냉각재는 중첩되지 않으며, 공급한 뒤 바닥나면 기계가 즉시 정지하고 현재 레시피를 소멸시킵니다.

| 엑조틱 냉각재 | 입력 속도 | 속도 증가 | 최대 속도 | 젤리드 크라이오테움 |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| 없음 | 0 L/s | 1.0x | 150% | 250 - 375 L/s |
| 용융 인피니티 | 20 L/s | 2.0x | 300% | 500 - 750 L/s |
| 용융 시공간 | 20 L/s | 4.0x | 600% | 1,000 - 1,500 L/s |
| 용융 이터니티 | 20 L/s | 8.0x | 1,200% | 1,500 - 3,000 L/s |