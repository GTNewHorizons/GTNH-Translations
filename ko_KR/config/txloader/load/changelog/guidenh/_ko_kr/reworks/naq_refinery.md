---
item_ids:
  - gregtech:gt.blockmachines:15536
navigation:
  title: 나콰다 연료 정제소
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15536
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 나콰다 연료 정제소
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15536"/>
</GameScene>
<Color id="GREEN">나콰다 연료 정제소(NFR)</Color>는 Mk-III+ 나콰다 기반 액체 연료를 제조하기 위한 UHV 티어 멀티블록이며, 이 연료는 전력 생산을 위해 대형 나콰다 원자로(LNR) <ItemImage id="gregtech:gt.blockmachines:15537"/>에서 거의 전적으로 사용됩니다. 모든 연료에는 더 효율적으로 제조하기 위한 대체 레시피가 최소 하나씩 있지만, 더 비싼 재료가 필요합니다. <Color id="GREEN">NFR</Color>은 입력 전압을 높여서 오버클럭할 수 없고, 필드 제한 코일을 업그레이드해야만 오버클럭할 수 있습니다. 사용 가능한 티어는 네 가지이며, 각 티어는 새로운 레시피를 해금하고, 더 낮은 티어의 레시피에 대해 추가 완벽 오버클럭을 수행하며, 4개의 병렬 처리를 제공합니다. 

NFR을 포함한 전력 계획용 스프레드시트는 [여기](https://docs.google.com/spreadsheets/d/1FTFdfmY_UWbTbFOyNzARKeI90pbHvPBH6M3JHJmaC-E/edit?gid=589078529#gid=589078529)에서 찾을 수 있습니다.
<br clear="all"/>

> [!NOTE]
> 구조물을 제외하고 멀티블록에 다음과 같은 변경 사항이 적용되었습니다:
> - 해치 자유 배치: 해치는 더 이상 유리와 인접한 위치로 제한되지 않습니다.
> - 병렬 처리 증가: 증가한 코일 비용을 보상하기 위해 코일 티어당 병렬 처리가 +4 증가합니다.

## 건설
<Color id="GREEN">NFR</Color>에는 티어가 있는 구성 요소가 하나 있습니다. 필드 제한 코일이 사용 가능한 레시피, 완벽 오버클럭 횟수, 병렬 처리 수를 결정합니다. 버스/해치는 구조물 어디에서든 나콰다 연료 정제소 케이싱을 대체할 수 있습니다. <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>가 지원되지만, 입력 전압을 높여도 기계가 오버클럭되지 않습니다. 유지보수 해치는 없습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설하십시오. 한 스택에 보관된 프로젝터 수가 코일의 티어를 결정합니다. 

### 필요 재료:
- 1개 <ItemLink id="gregtech:gt.blockmachines:15536"/><ItemImage id="gregtech:gt.blockmachines:15536"/>
- 0-483개 <ItemLink id="GoodGenerator:FRF_Casings"/><ItemImage id="GoodGenerator:FRF_Casings"/>
- 192개 <ItemLink id="GoodGenerator:fieldRestrictingGlass"/><ItemImage id="GoodGenerator:fieldRestrictingGlass"/>
- 124개 <ItemLink id="gregtech:gt.blockcasings8:5"/><ItemImage id="gregtech:gt.blockcasings8:5"/>
- 72개 필드 제한 코일 (티어형)<ItemImage id="GoodGenerator:FRF_Coil_1"/>
- 64개 <ItemLink id="GoodGenerator:radiationProtectionSteelFrame"/><ItemImage id="GoodGenerator:radiationProtectionSteelFrame"/>
- 1개 이상의 에너지 해치 (정제소 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 0개 이상의 입력 버스 (정제소 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0개 이상의 입력 해치 (정제소 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상의 출력 해치 (정제소 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">NFR</Color>은 각 면을 벽 공유하여 케이싱, 유리, 버스/해치를 절약할 수 있습니다. EU/t 수치가 고정되어 있기 때문에 에너지 해치도 포함되지만, 필드 제한 코일은 포함되지 않습니다. 

## 사용법
모든 <Color id="GREEN">NFR</Color> 레시피에는 최소 티어의 필드 제한 코일이 필요합니다. 모든 티어는 4개의 병렬 처리를 제공하며, 최소 티어를 초과하는 모든 티어는 추가 완벽 오버클럭을 제공합니다. 예를 들어, Mk-IV 나콰다 기반 액체 연료는 최소 2티어 코일이 필요하지만, 4티어 코일을 갖춘 <Color id="GREEN">NFR</Color>은 해당 레시피를 16개의 병렬 처리와 두 번의 완벽 오버클럭으로 실행할 수 있습니다. 따라서 항상 가능한 한 가장 높은 티어의 코일로 업그레이드하는 것이 권장됩니다.