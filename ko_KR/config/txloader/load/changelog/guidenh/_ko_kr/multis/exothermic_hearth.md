---
item_ids:
  - gregtech:gt.blockmachines:15517
navigation:
  title: 발열 화로
  parent: multis.md
  icon: gregtech:gt.blockmachines:15517
categories:
    - 새 멀티블록
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 발열 화로
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15517" />
</GameScene>
<Color id="GREEN">발열 화로(ExH)</Color>는 가루를 주괴로 대량 제련하고, 실리콘 단결정을 제작하며, 다양한 재료를 가열하기 위한 ZPM 티어 멀티블록입니다. 이전 메가 전기 용광로를 대체합니다. <Color id="GREEN">발열 화로</Color>는 전기 용광로 <ItemImage id="gregtech:gt.blockmachines:1000"/>의 직접 업그레이드입니다. 최대 <Color id="RED">512</Color>개의 병렬 처리를 제공하고, 본격적인 오버클럭을 위한 <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>를 지원하며, <Color id="BLUE">무제한 티어 스킵</Color>을 지원하기 때문입니다. 즉, 전력과 열이 충분하다면 전압 티어와 관계없이 모든 레시피를 실행할 수 있습니다. 사용 가능한 병렬 처리 수는 작동 중 천천히 512까지 증가하고, 대기 중에는 다시 256까지 감소합니다. 선택적으로 컨트롤러 GUI에서 파이로테움 가열을 활성화하면 250-500 L/s의 블레이징 파이로테움을 소모하는 대신 병렬 처리가 증가하는 속도를 6배로 높일 수 있습니다. <Color id="GREEN">발열 화로</Color>는 레시피 요구치보다 900K 초과할 때마다 5% 에너지 할인을 얻고, 1,800K 초과할 때마다 완벽 오버클럭 1회를 얻습니다. 발열 화로는 512 병렬 처리(오버클럭 4회 이상)를 최대한 활용할 수 있을 때만 볼카누스 <ItemImage id="gregtech:gt.blockmachines:963"/>보다 더 뛰어난 성능을 냅니다.
<br clear="all"/>

## 건설:
<Color id="GREEN">발열 화로</Color>에는 두 가지 티어 구성 요소가 있습니다. 가열 코일은 레시피의 최대 티어, 에너지 할인, 완벽 오버클럭 수를 결정합니다. 유리는 에너지 해치의 최대 티어를 결정합니다. UMV 티어 유리는 모든 제한을 제거합니다. 버스/해치는 구조물 어디에서든 모든 화로 케이싱을 대체할 수 있습니다. 단, 소음기 해치는 구조물 상단 층의 중앙 케이싱에만 제한됩니다. 멀티앰프 및 레이저 에너지 해치를 지원하지만, 후자는 최소 UV 티어 유리가 필요합니다. 멀티블록 구조 홀로그램 프로젝터를 사용해 하위 채널 "coil"과 "glass"로 해당 구성 요소의 티어를 지정하여 구조물을 시각화/건설하십시오. 
### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15517"/><ItemImage id="gregtech:gt.blockmachines:15517"/>
- 1,800-1,918 <ItemLink id="gregtech:gt.blockcasings14:3"/><ItemImage id="gregtech:gt.blockcasings14:3"/>
- 925 <ItemLink id="gregtech:gt.blockcasings:11"/><ItemImage id="gregtech:gt.blockcasings:11"/>
- 860 가열 코일(티어별) <ItemImage id="gregtech:gt.blockcasings5:11"/>
- 780 <ItemLink id="miscutils:gtplusplus.blockcasings.2:11"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:11"/>
- 426 <ItemLink id="gregtech:gt.blockcasings8:10"/><ItemImage id="gregtech:gt.blockcasings8:10"/>
- 332 티어 유리 <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 308 <ItemLink id="gregtech:gt.blockcasings11:7"/><ItemImage id="gregtech:gt.blockcasings11:7"/>
- 280 <ItemLink id="miscutils:miscutils.blockcasings:14"/><ItemImage id="miscutils:miscutils.blockcasings:14"/>
- 131 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 56 <ItemLink id="gregtech:gt.blockframes:163"/><ItemImage id="gregtech:gt.blockframes:163"/>
- 1개 이상 에너지 해치(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 <ItemLink id="gregtech:gt.blockmachines:90"/> (모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:90"/>
- 1 소음기 해치(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:91"/>
- 0개 이상 입력 버스(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:70"/>
- 0개 이상 입력 해치(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:70"/>
- 0개 이상 출력 버스(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:80"/>
- 0개 이상 출력 해치(모든 화로 케이싱)<ItemImage id="gregtech:gt.blockmachines:60"/>

### 벽 공유:
<Color id="GREEN">발열 화로들</Color>은 케이싱과 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 가열 코일과 유리는 포함되지 않습니다. 
## 사용법:
<Color id="GREEN">발열 화로</Color>는 최대 512 병렬 처리, 본격적인 오버클럭을 위한 멀티앰프 및 레이저 에너지 해치 지원, 무제한 티어 스킵을 제공하므로 전기 용광로의 직접 업그레이드입니다. 즉, 전력과 열이 충분하다면 전압 티어와 관계없이 모든 레시피를 실행할 수 있습니다. 예를 들어 ZPM 256A 레이저 에너지 해치는 열 용량이 충분히 높다면 UIV 레시피를 실행할 수 있습니다. 유리 티어는 에너지 해치의 전압 티어만 제한하며, 레시피의 전압 티어는 제한하지 않습니다.

사용 가능한 병렬 처리 수는 아래에서 볼 수 있듯이 작동 중 천천히 512까지 증가하고, 대기 중에는 다시 256까지 감소합니다. 최대 512 병렬 처리에 도달하려면 30분 동안 연속 작동해야 하지만, 모두 잃는 데는 4분 16초밖에 걸리지 않습니다. 선택적으로 컨트롤러 GUI에서 파이로테움 가열을 활성화하면 250-500 L/s의 블레이징 파이로테움을 소모하는 대신 병렬 처리가 증가하는 속도를 6배로 높일 수 있습니다. 소비율은 추가 병렬 처리 수에 비례해 선형적으로 증가하지만, 대신 발열 화로가 단 5분 만에 최대 512 병렬 처리에 도달할 수 있게 합니다. 파이로테움 가열이 활성화된 상태에서 블레이징 파이로테움이 바닥나면 기계가 즉시 정지하고 현재 레시피를 소멸시킵니다.

- 작동 중 5초당 +0.711 병렬 처리(파이로테움 가열 비활성화), 최대까지 30분
- 작동 중 5초당 +4.267 병렬 처리(파이로테움 가열 활성화), 최대까지 5분
- 대기 중 초당 -1 병렬 처리, 최소까지 4.26분

## 열 용량
마지막으로, <Color id="GREEN">발열 화로</Color>는 레시피 요구치보다 900K 초과할 때마다 5% 에너지 할인을 얻고, 1,800K 초과할 때마다 완벽 오버클럭 1회를 얻습니다. 또한 MV보다 높은 전압 티어마다 +100K 열 보너스가 있습니다.