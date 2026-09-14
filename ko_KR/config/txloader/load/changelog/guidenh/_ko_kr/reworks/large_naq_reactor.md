---
item_ids:
  - gregtech:gt.blockmachines:15537
navigation:
  title: 대형 나콰다 반응로
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15537
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대형 나콰다 반응로

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15537"/>
</GameScene>
<Color id="GREEN">대형 나콰다 반응로 (LNR)</Color>는 나콰다 기반 액체 연료에서 전력을 생산하기 위한 ZPM 티어 멀티블록입니다. <Color id="GREEN">LNR</Color>은 연료를 EU로 직접 변환하며, 예열 기간이 없고, 터빈을 사용하지 않습니다. 유일한 과제는 입력 요구 사항을 충족하는 것입니다: 입력 해치에는 어느 시점에도 단 한 종류의 연료만 있을 수 있으며, <Color id="GREEN">LNR</Color>에 전력을 출력하려면 2,400 L/s의 액체 공기를 공급해야 합니다. 선택적으로, 기계의 효율을 높이기 위한 냉각제 및/또는 기계의 전체 처리량을 높이기 위한 여기된 액체를 공급할 수 있습니다. 단일 <Color id="GREEN">LNR</Color>은 (가장 높은 티어의 액체를 사용할 경우) 최대 665B EU/t를 생성할 수 있으며, 이는 더 높은 전압 티어로 매우 잘 확장된다는 뜻입니다. <Color id="GREEN">LNR</Color>은 다이슨 스웜 지상 유닛 <ItemImage id="gregtech:gt.blockmachines:14001"/> 또는 준안정 반물질 안정화 시퀀서(SSASS) <ItemImage id="gregtech:gt.blockmachines:32027"/>로 대체됩니다.

나콰다 기반 액체 연료(나콰 연료)의 처음 두 티어는 각각 핵융합로와 대형 화학 반응로에서 제작됩니다. 나머지 네 티어는 모두 고급 필드 제한 코일을 사용하여 새로운 레시피를 해금하는 [나콰다 연료 정제소](./naq_refinery.md)에서 제작됩니다. Mk-V 연료는 별 연료를 제작하는 데도 사용되며, 고갈된 Mk-V 및 Mk-VI 연료는 SSASS에서 활성화 안정화에 사용됩니다. 중성자 활성화기 <ItemImage id="gregtech:gt.blockmachines:32013"/>는 나콰 연료의 붕괴를 상당히 가속할 수 있지만, 전력은 전혀 생성하지 않습니다.

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일하게 유지됩니다.

## 건설
<Color id="GREEN">LNR</Color>에는 티어 부품이 없습니다. 버스/해치는 구조물 어디에서든 모든 나콰다 반응로 케이싱을 대체할 수 있습니다. 네 가지 서로 다른 입력 유체를 담으려면 비축 입력 해치를 적극 권장합니다. 본격적인 전력 생성을 위해 다중 앰프 및 레이저 다이너모 해치를 지원하지만, 하나만 사용할 수 있습니다. <Color id="GREEN">LNR</Color>은 다이너모 해치가 현재 전력 출력의 100%를 감당할 수 없으면 정지하므로, 고앰프 레이저 다이너모 해치를 사용하는 것이 사실상 필수입니다. 구조물을 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>을 사용하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15537"/><ItemImage id="gregtech:gt.blockmachines:15537"/>
- 130-141 <ItemLink id="gregtech:gt.blockcasings13:15"/><ItemImage id="gregtech:gt.blockcasings13:15"/>
- 81 <ItemLink id="GoodGenerator:MAR_Casing"/><ItemImage id="GoodGenerator:MAR_Casing"/>
- 32 <ItemLink id="GoodGenerator:radiationProtectionSteelFrame"/><ItemImage id="GoodGenerator:radiationProtectionSteelFrame"/>
- 1 다이너모 해치 (모든 반응로 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 유지보수 해치 (모든 반응로 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0+ 입력 해치 (모든 반응로 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 해치 (모든 반응로 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<FloatingImage src="../assets/reworks/lnr_wallshare.png" displayWidth="128" align="right">
  <ImageAnnotation>
    이중 벽 공유 반응로의 예시
  </ImageAnnotation>
</FloatingImage>
<Color id="GREEN">LNR</Color>은 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 측면이나 구조물 중앙의 구체를 벽 공유할 수 있습니다. 여기에는 동시에 2-4대의 기계를 지원할 만큼 충분한 처리량이 있는 경우 레이저 다이너모 해치도 포함됩니다. 위 이미지는 두 대의 기계를 보여주지만, 원한다면 남은 축에 세 번째 기계를 배치할 수 있습니다 (레이저 거울 필요). 

## 사용법
다른 발전기 멀티블록과 비교하면 <Color id="GREEN">LNR</Color>은 사용하기 매우 간단합니다. <Color id="GREEN">LNR</Color>은 연료를 EU로 직접 변환하며, 예열 기간이 없고, 터빈을 사용하지 않습니다. 유일한 과제는 다음 입력 요구 사항을 충족하는 것입니다:

- 입력 해치에는 어느 시점에도 단 한 종류의 연료만 있을 수 있으며, 그렇지 않으면 기계가 폭발합니다.
- <Color id="GREEN">LNR</Color>에 전력을 출력하려면 2,400 L/s의 액체 공기를 공급해야 하며, 그렇지 않으면 연료가 소멸합니다.
- 다이너모 해치는 현재 전력 출력의 100%를 감당할 수 있을 만큼 충분히 커야 하며, 그렇지 않으면 기계가 정지합니다.

## 냉각제
선택적으로, <Color id="GREEN">LNR</Color>의 효율을 높이기 위해 냉각제를 제공할 수 있습니다. 다음 각 유체는 연료 소비율을 증가시키거나 레시피 길이를 줄이지 않으면서 현재 EU/t를 배로 증가시킵니다. 냉각제는 기계에 확실히 이점만 됩니다. 냉각제는 중첩되지 않으므로 두 종류 이상 사용할 수 없습니다. 

| 냉각제 | 효율 | 양 |
| --------------- | --------------- | --------------- |
| IC2 냉각제 | 105% | 1,000 L/s |
| 슈퍼 냉각제 | 150% | 1,000 L/s |
| 크라이오테움 | 275% | 1,000 L/s |
| 타키온이 풍부한 시간 유체 | 500% | 20 L/s |

## 부스터
선택적으로, <Color id="GREEN">LNR</Color>의 처리량을 높이기 위해 부스터를 제공할 수 있습니다. 다음 각 유체는 병렬 처리와 유사하게 현재 EU/t와 소비되는 연료 양을 배로 증가시킵니다. 이는 산소나 냉각제 소비를 증가시키지 않습니다. 부스터는 추가 기계를 남발하는 것을 확실히 줄여 줍니다. 부스터는 중첩되지 않으므로 두 종류 이상 사용할 수 없습니다. 

| 부스터 | 배율 | 양 |
| --------------- | --------------- | --------------- |
| 용융 세슘 | 2x | 180 L/s |
| 용융 우라늄-235 | 3x | 180 L/s |
| 용융 나콰다 | 4x | 20 L/s |
| 용융 원자 분리 촉매 | 16x | 20 L/s |
| 공간 확장 유체 | 64x | 20 L/s |