---
item_ids:
  - gregtech:gt.blockmachines:31087
navigation:
  title: 증기 화덕
  parent: multis.md
  icon: gregtech:gt.blockmachines:31087
categories:
    - 새 멀티블록
author: Skorched
date: 2026-05-25
---

# 증기 화덕
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31087" />
</GameScene>
<Color id="GREEN">증기 화덕</Color>은 원재료를 제련, 고온 제련, 훈연하기 위한 증기 티어 멀티블록입니다. <Color id="GREEN">증기 화덕</Color>은 125% 속도로 작동하고, 일반적으로 필요한 증기의 62.5%만 사용하며, 8개의 병렬 처리를 제공하므로 단일블록 증기 화로의 직접적인 업그레이드입니다. 이 기계에는 기본(T1)과 고압(T2) 두 가지 티어가 있습니다. 다른 증기 시대 멀티블록과 마찬가지로 고압 버전은 두 배 빠르게 작동하기 위해 두 배의 증기를 소비합니다. 선택할 수 있는 세 가지 모드도 있습니다. 기본 <Color id="GREEN">제련</Color> 모드는 제한이나 추가 이점 없이 모든 레시피를 처리할 수 있습니다. <Color id="RED">고온 제련</Color> 모드는 기계를 광석/금속으로 제한하는 대신 속도와 증기 사용량이 두 배가 됩니다. <Color id="BLUE">훈연</Color> 모드는 기계를 음식 아이템으로 제한하는 대신 속도와 증기 사용량이 두 배가 됩니다. <Color id="GREEN">증기 화덕</Color>은 HV에서 <ItemLink id="gregtech:gt.blockmachines:1003"/> <ItemImage id="gregtech:gt.blockmachines:1003"/>로 대체됩니다. 
<br clear="all"/>

## 건설:
기본 증기 화덕과 고압 증기 화덕의 유일한 구조적 차이는 케이싱의 재질입니다. 증기는 다른 증기 티어 멀티블록과 마찬가지로 <ItemLink id="gregtech:gt.blockmachines:31040" /> <ItemImage id="gregtech:gt.blockmachines:31040" /> (입력 해치가 아닙니다)를 통해서만 받아들여집니다. 증기 입력 및 출력 버스는 인접한 인벤토리로 자동으로 밀어 넣거나 인접한 인벤토리에서 자동으로 당겨오지 않으므로 자동화를 위해서는 호퍼, EnderIO 아이템 도관 또는 컨베이어 모듈이 필요합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조를 시각화/건설하십시오. 한 스택에 보관된 투영기의 수가 기계의 티어를 결정합니다 (1=기본, 2=고압).

판이 <ItemLink id="gregtech:gt.blockmachines:112" /> <ItemImage id="gregtech:gt.blockmachines:112" />에서 만들어지고 막대가 줄로 만들어진다고 가정하면, 기본 <Color id="GREEN">증기 화덕</Color>(필요한 해치 포함)은 건설하는 데 청동 주괴 395개와 벽돌 블록 9개가 필요합니다. 고압 <Color id="GREEN">증기 화덕</Color>은 건설하는 데 강철 주괴 359개, 청동 주괴 63개, 벽돌 블록 3개가 필요합니다. 
### 요구 사항:
<Row gap="20" alignItems="center">
<Column gap="8" alignItems="center">
__기본(T1) 요구 사항:__
  - 1 <ItemLink id="gregtech:gt.blockmachines:31087" /><ItemImage id="gregtech:gt.blockmachines:31087" />
  - 2-6 <ItemLink id="gregtech:gt.blockcasings:10" /><ItemImage id="gregtech:gt.blockcasings:10" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:2" /><ItemImage id="gregtech:gt.blockcasings2:2" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:12" /><ItemImage id="gregtech:gt.blockcasings2:12" />
  - 3 <ItemLink id="gregtech:gt.blockcasings3:13" /><ItemImage id="gregtech:gt.blockcasings3:13"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31040"/><ItemImage id="gregtech:gt.blockmachines:31040"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31046" /><ItemImage id="gregtech:gt.blockmachines:31046"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31047" /><ItemImage id="gregtech:gt.blockmachines:31047"/>
</Column>
<Column gap="8" alignItems="center">
__고압(T2) 요구 사항:__
  - 1 <ItemLink id="gregtech:gt.blockmachines:31087" /><ItemImage id="gregtech:gt.blockmachines:31087" />
  - 2-6 <ItemLink id="gregtech:gt.blockcasings2" /><ItemImage id="gregtech:gt.blockcasings2" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:3" /><ItemImage id="gregtech:gt.blockcasings2:3" />
  - 4 <ItemLink id="gregtech:gt.blockcasings2:13" /><ItemImage id="gregtech:gt.blockcasings2:13" />
  - 3 <ItemLink id="gregtech:gt.blockcasings3:14" /><ItemImage id="gregtech:gt.blockcasings3:14"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31040"/><ItemImage id="gregtech:gt.blockmachines:31040"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31046" /><ItemImage id="gregtech:gt.blockmachines:31046"/>
  - 1+ <ItemLink id="gregtech:gt.blockmachines:31047" /><ItemImage id="gregtech:gt.blockmachines:31047"/>
</Column>
</Row>

### 벽 공유:
<Color id="GREEN">증기 화덕</Color>은 각 면을 벽 공유하여 케이싱과 버스/해치를 절약할 수 있습니다. 이는 상당한 양의 청동과 강철을 절약하므로 적극 권장합니다. 공유는 같은 종류의 케이싱을 사용하는 다른 증기 티어 멀티블록과도 작동합니다. 

## 사용법:
<Color id="GREEN">증기 화덕</Color>은 <Color id="GREEN">125%</Color> 속도로 작동하고, 일반적으로 필요한 증기의 <Color id="BLUE">62.5%</Color>만 사용하며, <Color id="RED">8</Color>개의 병렬 처리를 제공하므로 단일블록 증기 화로의 직접적인 업그레이드입니다. 고압(T2)으로 업그레이드하면 다음 표에서 볼 수 있듯이 처리 속도와 증기 소비량이 모두 두 배가 됩니다. 단일블록 기계에 비해 큰 이점이 있으므로 HV까지 <Color id="GREEN">증기 화덕</Color>을 사용할 것으로 예상됩니다.

<Color id="GREEN">증기 화덕</Color>에는 아래에 나열된 세 가지 고유 모드가 있어 특정 레시피에 특화하여 기계의 처리량을 더욱 높일 수 있습니다. 이 모드들은 바닐라 화로, 용광로, 훈연기를 모방한다는 점에 유의하십시오. 컨트롤러의 GUI에서 모드를 전환하거나, 컨트롤러에 드라이버를 사용하여 전환하십시오.

- <Color id="GREEN">제련</Color> - 제한이나 추가 이점이 없습니다. 기본 범용 모드입니다.
- <Color id="RED">고온 제련</Color> - 속도와 증기 소비량이 두 배가 되는 대신 광석/금속으로 제한됩니다.
- <Color id="BLUE">훈연</Color> - 속도와 증기 소비량이 두 배가 되는 대신 날음식으로 제한됩니다.

다음 표는 <Color id="GREEN">증기 화덕</Color>의 두 티어와 세 가지 모드 각각의 증기 소비량 및 속도를 요약합니다. 참고로, 바닐라 화로는 초당 0.10개의 아이템을 처리하고, 바닐라 용광로/훈연기는 초당 0.20개의 아이템을 처리합니다. 
### __기본(T1)__
|  | <Color id="GREEN">제련</Color> | <Color id="RED">고온 제련</Color> | <Color id="BLUE">훈연</Color> |
| --------------- | --------------- | --------------- | --------------- |
| 최대 증기 | 800 L/s | 1,600 L/s | 1,600 L/s |
| 최대 속도 | 0.78개/s | 1.54개/s | 1.54개/s |

### __고압(T2)__

|  | <Color id="GREEN">제련</Color> | <Color id="RED">고온 제련</Color> | <Color id="BLUE">훈연</Color> |
| --------------- | --------------- | --------------- | --------------- |
| 최대 증기 | 1,600 L/s | 3,200 L/s | 3,200 L/s |
| 최대 속도 | 1.54개/s | 3.08개/s | 3.08개/s |