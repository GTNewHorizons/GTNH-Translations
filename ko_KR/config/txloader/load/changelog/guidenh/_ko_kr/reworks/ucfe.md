---
item_ids:
  - gregtech:gt.blockmachines:15535
navigation:
  title: 범용 화학 연료 엔진
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15535
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 범용 화학 연료 엔진
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15535"/>
</GameScene>
<Color id="GREEN">범용 화학 연료 엔진 (UCFE)</Color>은 거의 모든 종류의 가연성 액체에서 전력을 생산하는 IV 티어 멀티블록입니다. <Color id="GREEN">UCFE</Color>는 대형 가스 터빈 <ItemImage id="gregtech:gt.blockmachines:15527"/>, Rocketdyne F-1A 엔진 <ItemImage id="gregtech:gt.blockmachines:996"/>, 대형 연소 엔진 <ItemImage id="gregtech:gt.blockmachines:15533"/>의 레시피를 EU/t에 상한이 없는 매우 효율적인 하나의 기계로 효과적으로 결합합니다. 유일한 예외는 반유체로, 이들은 여전히 대형 반유체 버너 <ItemImage id="gregtech:gt.blockmachines:31026"/>가 필요합니다. 다른 유일한 입력 요구 사항은 연소 촉진제이며, 이는 연료 효율을 최대 150%까지 향상시킵니다. 로켓 연료는 가스/디젤 연료보다 연소 촉진제를 훨씬 적게 사용합니다.

[GTNH Power Planner ](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 구조 자체만 변경되었으며, 멀티블록의 핵심 기능은 이전과 동일합니다

## 건설
<Color id="GREEN">UCFE</Color>에는 티어 구성 요소가 없습니다. 다이너모 해치는 구조물 뒤쪽 중앙 케이싱에만 설치할 수 있습니다. 나머지 버스/해치는 구조물 어디에 있는 안정적인 티타늄 기계 케이싱이든 대체할 수 있습니다. 대규모 전력 생성을 위해 <Color id="BLUE">멀티앰프 및 레이저 에너지 해치</Color>를 지원합니다. 원한다면 연료와 연소 촉진제를 동일한 입력 해치를 통해 공급할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>을 사용하여 구조물을 시각화/건설하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15535"/><ItemImage id="gregtech:gt.blockmachines:15535"/>
- 100-115 <ItemLink id="gregtech:gt.blockcasings4:2"/><ItemImage id="gregtech:gt.blockcasings4:2"/>
- 72 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 39 <ItemLink id="gregtech:gt.blockcasings8"/><ItemImage id="gregtech:gt.blockcasings8"/>
- 20 <ItemLink id="gregtech:gt.blockcasings4:13"/><ItemImage id="gregtech:gt.blockcasings4:13"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:14"/><ItemImage id="gregtech:gt.blockcasings2:14"/>
- 10 <ItemLink id="gregtech:gt.blockcasings4:3"/><ItemImage id="gregtech:gt.blockcasings4:3"/>
- 1 다이너모 해치 (뒤쪽 중앙 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 유지보수 해치 (모든 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 머플러 해치 (모든 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1개 이상 입력 해치 (모든 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />

### 벽 공유
<Color id="GREEN">UCFE</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 입력 해치는 위치 제한 때문에 포함되지 않습니다. 자원을 최대한 절약하려면 수직으로 벽 공유하는 것이 권장되지만, 이를 위해서는 컨트롤러를 뒤집어야 합니다.

## 사용법
<Color id="GREEN">UCFE</Color>는 매초 입력 해치에 있는 모든 연료와 연소 촉진제를 소비합니다. 생성된 에너지는 다음 1초 동안 다이너모 해치로 전달됩니다. 다이너모 해치의 버퍼가 가득 차면 기계는 즉시 정지합니다. 생성된 총 EU/t가 다이너모 해치의 처리량보다 크면 초과 전력은 소멸됩니다.

툴팁에 적힌 내용과 달리, <Color id="GREEN">UCFE</Color>는 어떤 종류의 예열 기간도 없으며 생성할 수 있는 최대 전력을 즉시 출력합니다. 즉, 연료를 절약하기 위해 라포트로닉 슈퍼커패시터에 연결된 RS 래치가 필요하지 않습니다. 대신, 전력이 95% 미만일 때마다 <Color id="GREEN">UCFE</Color>를 활성화하려면 에너지 감지기 커버와 기계 제어기 커버를 사용하십시오. 

## 연료
<Color id="GREEN">UCFE</Color>는 가스, 디젤, 로켓 연료로 전력을 생성합니다. 가장 인기 있는 선택지는 니트로벤젠, 세탄가 강화 디젤, 고옥탄 가솔린, 고밀도 하이드라진 연료 혼합물, 녹색 로켓 연료입니다. 중유, 원유, 악성 오일과 같은 반유체는 포함되지 않습니다. 이들은 대형 반유체 버너 <ItemImage id="gregtech:gt.blockmachines:31026"/>에서만 연소할 수 있기 때문입니다.

## 연소 촉진제
연료 외에 <Color id="GREEN">UCFE</Color>의 유일한 다른 입력은 연소 촉진제이며, 이는 연소 반응에 필요한 조건을 제공하는 유체 물질입니다. 연소 촉진제는 또한 다음 방정식에 따라 연료 효율을 향상시킵니다. 여기서 $$C$$는 연소되는 연료 유형과 관련된 상수이고, $$R$$은 연료에 대한 연소 촉진제의 비율입니다. 최대 효율은 150%이며, 총 EU/t에 소프트 캡이나 상한이 없습니다.

<Latex formula="EU/t = L/s \times EU/L \times 1.5e^{-C/R} \div 20">
  여기서:
  - $$C$$: 연료 유형과 관련된 상수
  - $$R$$: 연료에 대한 연소 촉진제의 비율
</Latex>

다음 그래프는 두 가지 서로 다른 $$C$$ 값에 대해 효율과 연료에 대한 연소 촉진제의 비율($$R$$) 사이의 관계를 나타냅니다. 로켓 연료는 비율 약 0.5에서 최대치에 도달하므로, 연소 촉진제의 입력 속도는 연료 입력 속도의 50%를 초과해서는 안 됩니다. 그러나 가스/디젤 연료는 비율 약 2.0에서 최대치에 도달하므로, 연소 촉진제의 입력 속도는 연료 입력 속도의 200%를 초과해서는 안 됩니다. 이 관계는 비율이 L/s에만 기반하므로 연료의 에너지 값과 관계없이 성립합니다. 

<FunctionGraph title="Efficiency of Fuels Based on Promoter Ratio" xRange="0..2" domain="0..2" xLabel="Combustion Promotor to Fuel Ratio ($$R$$)" yLabel="Efficiency (%)"> <Plot expr="1.5*e^((-0.04)/x)*100" color="#ff55ff" label="Gas/Diesel Fuels (C=0.04)"/>
<Plot expr="1.5*e^((-0.005)/x)*100" color="#ffff55" label="Rocket Fuels (C=0.005)"/>
</FunctionGraph>