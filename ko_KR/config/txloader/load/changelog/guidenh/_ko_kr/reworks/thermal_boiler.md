---
item_ids:
  - gregtech:gt.blockmachines:15557
navigation:
  title: 열 보일러
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15557
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 열 보일러

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15557"/>
</GameScene>
<Color id="GREEN">열 보일러</Color>는 용암, 파호이호이 용암, 뜨거운 냉각수 또는 뜨거운 태양염의 열로 물을 증기로 증발시키는 IV 티어 멀티블록입니다. 또한 용암 또는 파호이호이 용암에서 몇 가지 부산물을 수집하지만, 컨트롤러 내부에 용암 필터가 있을 때만 그렇습니다. <Color id="GREEN">열 보일러</Color>는 전력이나 연료를 소비하지 않지만, 충분한 물이 공급되지 않으면 폭발할 위험이 있습니다. 네 가지 뜨거운 유체 레시피는 모두 고정되어 있으므로 입출력 속도에 유연성이 없습니다. 뜨거운 유체의 100%는 항상 더 차가운 등가물로 재활용되며, 최대 효율에서 증기의 100%는 [대형 증기 터빈](./large_steam_turbine.md)에 의해 증류수로 다시 재활용되어 지속 가능한 폐쇄 루프 시스템을 이룹니다. 또는 물 저수조 해치를 입력으로 사용하고 초과 증류수는 폐기하십시오. <Color id="GREEN">열 보일러</Color>는 LuV에서 극한 열교환기 <ItemImage id="gregtech:gt.blockmachines:32017"/> 및 Whakawhiti Wera XL <ItemImage id="gregtech:gt.blockmachines:31079"/>로 대체되지만, 증기 처리량 측면에서만 그렇습니다.

<Color id="GREEN">열 보일러</Color>는 대형 열교환기(LHE) <ItemImage id="gregtech:gt.blockmachines:1154"/>와 매우 유사합니다. 차이점은 LHE가 더 높은 처리량을 가지고, 부산물이 없으며, 증류수만 사용하고, 파호이호이 용암을 받지 않는다는 것입니다. 다시 말해, 탄탈럼, 텅스텐산염 또는 금과 같은 자원에는 <Color id="GREEN">열 보일러</Color>를 사용하고, 전력에는 LHE를 사용하십시오.

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit)
<br clear="all"/>

> [!NOTE]
> 이 멀티블록의 구조만 변경되었으며, 작동 방식은 동일합니다.

## 건설
<Color id="GREEN">열 보일러</Color>에는 티어 부품이 없습니다. 유지보수 해치와 소음기 해치는 구조의 어느 위치에서든 열 격납 케이싱을 대체할 수 있습니다. 입력 및 출력 해치는 구조의 어느 위치에서든 열 처리 케이싱 또는 견고한 텅스텐강 기계 케이싱을 대체할 수 있습니다. 이들은 서로 균등하게 나뉠 필요도 없고 특정한 방식으로 배치될 필요도 없습니다. 항상 충분한 물을 공급하기 위해 저수조 해치를 사용하는 것이 매우 권장되지만, 그렇지 않다면 뜨거운 유체와 물은 동일한 입력 해치로 들어갈 수 있으며, 차가운 유체와 증기도 동일한 출력 해치에서 기계를 나갈 수 있습니다. 기계가 전력을 소비하지 않으므로 에너지 해치는 없습니다. 구조를 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오.

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15557"/><ItemImage id="gregtech:gt.blockmachines:15557"/>
- 20-25 <ItemLink id="miscutils:gtplusplus.blockcasings.2:11"/><ItemImage id="miscutils:gtplusplus.blockcasings.2:11"/>
- 10-17 <ItemLink id="gregtech:gt.blockcasings4"/><ItemImage id="gregtech:gt.blockcasings4"/>
- 10-17 <ItemLink id="miscutils:gtplusplus.blockcasings.2"/><ItemImage id="miscutils:gtplusplus.blockcasings.2"/>
- 16 <ItemLink id="miscutils:blockFrameGtMaragingSteel350"/><ItemImage id="miscutils:blockFrameGtMaragingSteel350"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 6 <ItemLink id="gregtech:gt.blockcasings2:12"/><ItemImage id="gregtech:gt.blockcasings2:12"/>
- 유지보수 해치 1개(아무 열 격납 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 소음기 해치 1개(아무 열 격납 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 입력 해치 1개 이상(아무 열 처리 또는 텅스텐강 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 버스 0개 이상(아무 열 처리 또는 텅스텐강 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 출력 해치 1개 이상(아무 열 처리 또는 텅스텐강 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">열 보일러</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 입출력 속도는 모두 고정되어 있으므로 입력 또는 출력 해치를 공유해도 문제가 없습니다. 모든 <Color id="GREEN">열 보일러</Color>가 여전히 충분한 물을 공급받고, 출력 해치가 결합된 증기 출력을 감당할 만큼 충분히 큰지 확인하십시오(10,000 L/t SH 증기의 경우 LV+).

## 사용
<Color id="GREEN">열 보일러</Color>는 용암, 파호이호이 용암, 뜨거운 냉각수 또는 뜨거운 태양염의 열로 물을 증기로 증발시킵니다. 필요하다면 증류수도 사용할 수 있습니다. <Color id="GREEN">열 보일러</Color>는 전력을 소비하지 않지만, 물 없이 10초 넘게 작동하면 폭발합니다. 작동 중에 물을 추가하거나 컨트롤러를 부수어도 전혀 문제가 없습니다. 물 없이는 증기가 생성되지 않습니다.

<Color id="GREEN">열 보일러</Color>는 자체 효율 값을 가지며, 이는 증기 출력 속도에 정비례하므로 폐쇄 루프 시스템에서 기계로 다시 재활용되는 증류수의 양에도 정비례합니다. <Color id="GREEN">열 보일러</Color>의 효율은 기계가 작동하는 동안 선형적으로 증가하며, 대기 상태가 되면 거의 즉시 0%로 초기화됩니다. 최대 효율에 도달하는 데 약 42초가 걸리므로 뜨거운 유체를 꾸준히 공급하는 것이 매우 중요합니다. 유지보수 문제는 각각 최대 효율을 10%씩 감소시킵니다.

## 열 교환
<Color id="GREEN">열 보일러</Color>는 1초에 한 번 뜨거운 유체를 더 차가운 형태로, 물을 증기로 변환합니다. 생성되는 증기의 종류는 뜨거운 유체의 종류에만 엄격히 의존하며, 입력 속도에 따라 변하지 않습니다. 모두 고정된 값이기 때문입니다. 초과 입력은 소비되지 않습니다.

## 부산물
<Color id="GREEN">열 보일러</Color>는 주로 용암 또는 파호이호이 용암에서 부산물을 생성하는 데 사용됩니다. 흑요석을 제외한 부산물은 생성될 기회라도 얻으려면 컨트롤러 내부에 용암 필터가 필요합니다. 용암 필터는 100의 내구도로 시작하며, 각 작업마다 1/30 확률로 내구도를 1 잃습니다. 즉, 용암 필터의 평균 수명은 3,000회 작업 또는 50분입니다. 뜨거운 냉각수와 뜨거운 태양염은 부산물을 생성하지 않으므로 용암 필터가 필요하지 않습니다. 용암 필터의 유무와 관계없이 증기는 여전히 생성됩니다.

용암 공급원에는 영원히 타는 항아리 <ItemImage id="ThaumicExploration:everburnUrn"/>, Ross128b의 유체 시추기 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Rb"/>, 또는 끓는 벌집에서 얻는 인광 <ItemImage id="Forestry:beeCombs:2"/>이 있습니다. 이 세 가지 옵션 중에서 영원히 타는 항아리가 가장 좋습니다. 전력이 필요 없고 <Color id="GREEN">열 보일러</Color>와 같은 위치에 둘 수 있기 때문입니다.

## 전력
주 목적은 아니지만, <Color id="GREEN">열 보일러</Color>에서 생성된 증기는 아래 나열된 순서대로 일련의 [대형 증기 터빈](./large_steam_turbine.md)으로 전력을 생산하는 데 사용됩니다. 두 종류의 증기는 동일한 전환 비율을 가지므로, 하나의 출력이 다음 것의 입력으로 직접 들어갈 수 있습니다. 최대 효율에서는 증기의 100%가 증류수로 다시 재활용되어 지속 가능한 폐쇄 루프 시스템을 이룹니다. 나중에는 각각의 XL 터보 변형을 대신 사용할 수 있습니다. SH 증기는 동일한 최적 유량에서 일반 증기보다 2배 더 많은 EU를 생성합니다.

- 대형 고압 증기 터빈은 SH 증기로 전력을 생산하고 이를 1:1 비율로 일반 증기로 변환합니다.
- 대형 증기 터빈은 일반 증기로 전력을 생산하고 이를 160:1 비율로 증류수로 변환합니다.

증기 처리량이 증기 밸브나 유체 파이프에 너무 높다면, 대신 유체 P2P 터널을 사용하십시오. 이들은 전송 제한이 없으며 모든 출력 연결 간에 모든 유체를 균등하게 분배합니다.