---
item_ids:
  - gregtech:gt.blockmachines:14050
navigation:
  title: 엑소 주조소
  parent: multis.md
  icon: gregtech:gt.blockmachines:14050
categories:
    - 새 멀티블록
author: Skorched
date: 2026-05-25
---

# 엑소 주조소
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:14050" />
</GameScene>
<br clear="all"/>
<Color id="GREEN">엑소 주조소</Color>는 액체 금속을 대규모로 주형에 주조하기 위한 UEV 티어 멀티블록입니다. <Color id="GREEN">엑소 주조소</Color>는 <ItemLink id="gregtech:gt.blockmachines:368" /> <ItemImage id="gregtech:gt.blockmachines:368" />의 직접적인 업그레이드입니다. 더 높은 에너지 할인과 훨씬 많은 병렬 처리로 상당히 더 빠르게 작동할 수 있기 때문입니다. 정확한 값은 설치된 모듈의 양과 수에 따라 크게 달라집니다. 총 7개의 모듈이 있으며 각각 기계에 고유한 보너스를 부여하지만, 구조의 티어에 따라 2/3/4개의 슬롯만 있습니다. 모듈은 모두 다를 수 있으며, 잠재적으로 동일하게 사용하여 보너스를 중첩할 수 있습니다. 또한 더 나은 성능을 위한 일회성 보너스를 제공하는 네 가지 모듈 조합이 있습니다.

## 건설:
<Color id="GREEN">엑소 주조소</Color>는 세 가지 티어로 제공됩니다. 이들 사이의 유일한 구조적 차이는 자기 섀시 블록이며, 유일한 기능적 차이는 모듈 슬롯 수(2/3/4)입니다. 버스/해치는 구조 어디에서나 모든 기본 <Color id="GREEN">엑소 주조소</Color> 케이싱을 대체할 수 있습니다. 최소 케이싱 요구 사항은 총 35개 주형에 대해 최대 25개 입력을 지원합니다. <Color id="RED">다중 앰프 및 레이저 에너지 해치</Color>가 지원되지만, <Color id="GREEN">엑소 주조소</Color>는 초냉각기 <ItemImage id="gregtech:gt.foundrycasings:9"/> 또는 헬리오캐스트 보강 <ItemImage id="gregtech:gt.foundrycasings:7" /> 모듈 없이는 에너지 해치의 전압 티어를 초과하여 오버클럭할 수 없습니다. 유지보수나 소음기 해치는 없습니다. 드라이버로 컨트롤러를 우클릭하여 애니메이션을 비활성화할 수 있습니다. 하위 채널 "chassis"와 함께 <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조를 시각화/건설하고 자기 섀시 블록의 티어를 지정하십시오.

컨트롤러 GUI에서 사용할 모듈을 선택한 다음 멀티블록 구조 홀로그램 프로젝터를 사용하여 건설하십시오. 모듈은 중앙 기둥 주위에 고리로 나타나며, 능력치는 컨트롤러 GUI의 "기계 정보 표시" 아래에 요약됩니다. 순서는 기계 작동에 영향을 주지 않습니다. 선택 메뉴에서 모듈을 Shift-좌클릭하여 제거한 다음 <ItemLink id="gregtech:gt.Tool_Vajra" /> <ItemImage id="gregtech:gt.Tool_Vajra" /> 또는 다른 도구로 물리적으로 파괴하십시오.
### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:14050" /> <ItemImage id="gregtech:gt.blockmachines:14050" />
- 548 <ItemLink id="gregtech:gt.blockglass1:7" /> <ItemImage id="gregtech:gt.blockglass1:7" />
- 462-486 <ItemLink id="gregtech:gt.foundrycasings" /> <ItemImage id="gregtech:gt.foundrycasings" />
- 281 <ItemLink id="gregtech:gt.foundrycasings:11" /> <ItemImage id="gregtech:gt.foundrycasings:11" />
- 260 _티어별 자기 섀시_ <ItemImage id="gregtech:gt.foundrycasings:1" />
- 224 <ItemLink id="gregtech:gt.blockframes:132" /> <ItemImage id="gregtech:gt.blockframes:132" />
- 196 <ItemLink id="gregtech:gt.foundrycasings:12" /> <ItemImage id="gregtech:gt.foundrycasings:12" />
- 173 <ItemLink id="gregtech:gt.blockcasings11:7" /><ItemImage id="gregtech:gt.blockcasings11:7" />
- 1+ _에너지 해치(모든 기본 엑소 주조소 케이싱)_ <ItemImage id="gregtech:gt.blockmachines:40" />
- 0+ _입력 버스(모든 기본 엑소 주조소 케이싱)_ <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ _입력 해치(모든 기본 엑소 주조소 케이싱)_ <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ _출력 버스(모든 기본 엑소 주조소 케이싱)_ <ItemImage id="gregtech:gt.blockmachines:80" />

### 벽 공유:
<Color id="GREEN">엑소 주조소</Color>는 케이싱, 모듈 구성 요소, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 하지만 에너지 해치는 공유하지 마십시오. 병렬 처리나 오버클럭이 아직 남아 있는 동안 기계가 가능한 한 많은 앰프를 끌어오기 때문입니다.

# 모듈:
<Color id="GREEN">엑소 주조소</Color>는 모듈 없이 <Color id="RED">150%</Color> 속도로 작동하고 전압 티어당 <Color id="BLUE">16</Color>개의 병렬 처리를 제공합니다. 이는 아래 표에서 볼 수 있습니다. 또한 헬리오캐스트 보강 <ItemImage id="gregtech:gt.foundrycasings:7" /> 모듈 없이는 UIV+ 레시피를 실행할 수 없습니다. 이는 최대 속도의 <Color id="RED">대량 고체화기</Color>보다 느리고 덜 효율적이며 더 제한적이지만, 이는 기계의 기본 능력치일 뿐이며 설치된 모든 모듈로 크게 향상됩니다. 병렬 처리를 결정하기 위한 유효 전압은 오버클럭처럼 에너지 해치의 티어에 의해 제한되지 않지만, 앰프 수와 관계없이 여러 에너지 해치가 있어야 합니다.

다음 표에서 "SCB"는 <Color id="BLUE">초고밀도 주조 분지</Color> 모듈을, "SCB+"는 조합 보너스가 적용된 동일 모듈을 의미하며, 둘 다 이 섹션 뒷부분에서 설명합니다.
### 병렬 처리:

|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |------------- |
| 기본 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |
| SCB 1개 | 28 | 56 | 84 | 112 | 140 | 168 | 196 | 224 | 252 | 280 | 308 | 336 | 364 | 392 | 420 |
| SCB 2개 | 40 | 80 | 120 | 160 | 200 | 240 | 280 | 320 | 360 | 400 | 440 | 480 | 520 | 560 | 600 |
| SCB+ 1개 | 34 | 68 | 102 | 136 | 170 | 204 | 238 | 272 | 306 | 340 | 374 | 408 | 442 | 476 | 510 |
| SCB+ 2개 | 46 | 92 | 138 | 184 | 230 | 276 | 322 | 368 | 414 | 460 | 506 | 552 | 598 | 644 | 690 |

총 7개의 모듈이 있고 구조의 티어에 따라 2/3/4개의 모듈 슬롯이 있습니다. 컨트롤러 GUI에서 사용할 모듈을 선택하십시오. 모듈은 모두 다를 수 있으며, 잠재적으로 동일하게 사용하여 보너스를 중첩할 수 있습니다. 유일한 예외는 초냉각기 <ItemImage id="gregtech:gt.foundrycasings:9" />, 자각형 오버클로커 <ItemImage id="gregtech:gt.foundrycasings:5" />, 범용 붕괴기 <ItemImage id="gregtech:gt.foundrycasings:4" /> 모듈로, 모두 <Color id="GREEN">엑소 주조소</Color>당 1개로 제한됩니다.

헬리오캐스트 보강 <ItemImage id="gregtech:gt.foundrycasings:7" /> 및 자각형 오버클럭 <ItemImage id="gregtech:gt.foundrycasings:5" /> 모듈은 둘 다 기계의 오버클럭 계수를 증가시키며, 이는 모든 오버클럭마다 속도 보너스를 단순히 증가시키는 독특한 메커니즘입니다. 예를 들어, 불완전 오버클럭은 2배 속도를 위해 4배 전력을 소비하지만, 오버클럭 계수를 0.35만큼 증가시키면 엑소 주조소가 대신 2.35배 속도를 위해 4배 전력을 소비하게 합니다.

## 초고밀도 주조 분지 <ItemImage id="gregtech:gt.foundrycasings:8"/>
SCB 모듈(UEV)은 기본 전압 티어당 16개 병렬 처리에 더해 전압 티어당 12개 병렬 처리를 추가하고, 최소 케이싱 수를 36개 줄입니다. 이는 전압 티어당 총 28개 병렬 처리와 총 35개 주형을 위한 61개 입력을 위한 충분한 공간입니다. 엑소 주조소당 SCB 모듈 수에는 제한이 없습니다. SCB를 간소화된 주조기 모듈과 조합하면 최적 생산이 해금되며, 이는 전압 티어당 +6개 병렬 처리 및 +75% 속도의 일회성 보너스입니다.

### 필요:
- 64 <ItemLink id="gregtech:gt.foundrycasings:8" /> <ItemImage id="gregtech:gt.foundrycasings:8" />
- 64 <ItemLink id="gregtech:gt.blockcasings10:13" /> <ItemImage id="gregtech:gt.blockcasings10:13" />
- 36 <ItemLink id="gregtech:gt.foundrycasings" /> <ItemImage id="gregtech:gt.foundrycasings" />
- 32 <ItemLink id="gregtech:gt.blockcasings10:14" /> <ItemImage id="gregtech:gt.blockcasings10:14" />
- 30 <ItemLink id="gregtech:gt.blockframes:75" /> <ItemImage id="gregtech:gt.blockframes:75" />
- 8 <ItemLink id="bartworks:bw.werkstoffblockscasing.01:10109"/> <ItemImage id="bartworks:bw.werkstoffblockscasing.01:10109"/>
- 8 <ItemLink id="gregtech:bw.sheetmetal:10109" /> <ItemImage id="gregtech:bw.sheetmetal:10109" />
- 6 <ItemLink id="gregtech:gt.sheetmetal:75" /> <ItemImage id="gregtech:gt.sheetmetal:75" />
- 4 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:10109"/> <ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:10109"/>

## 프로토볼트 안정기 <ItemImage id="gregtech:gt.foundrycasings:6" />
PVS 모듈(UEV)은 레시피의 기본 EU/t 비용에서 10%를 빼고 결과에 0.8을 곱합니다. 이는 다음 방정식에서 볼 수 있습니다. 즉 PVS 하나로 28% EU/t 할인, 둘로 49% EU/t 할인입니다. 이는 레시피 길이가 변경되지 않으므로 엑소 주조소의 속도를 증가시키지 않는다는 점에 유의하십시오. 가산 보너스는 헬리오캐스트 보강 모듈과 중첩되고, 곱셈 보너스는 범용 붕괴기 모듈과 중첩됩니다. 엑소 주조소당 PVS 모듈 수에는 제한이 없습니다. PVS를 자각형 오버클로커 모듈과 조합하면 조화 효율이 해금되며, 이는 -50% EU/t 및 +0.1 오버클럭 계수의 일회성 보너스입니다.
<Latex formula="\text{EU/t} = (100\% - \sum \text{AddBonus}) \times \prod \text{MultBonus}"/>

| 모듈   | 전력 소비(EU/t)    |
|--------------- | --------------- |
| PVS 1개   | $$(100\% - 10\%) \times 0.8 = 72\%$$   |
| PVS 2개   | $$(100\% - 20\%) \times 0.8^2 = 51\%$$   |
| PVS+ 1개   | $$(100\% - 60\%) \times 0.8 = 32\%$$   |
| PVS+ 2개   | $$(100\% - 70\%) \times 0.8^2 = 19\%$$   |

### 필요:
- 64 <ItemLink id="gregtech:gt.foundrycasings:6" /><ItemImage id="gregtech:gt.foundrycasings:6" />
- 32 <ItemLink id="gregtech:gt.blockframes:73" /><ItemImage id="gregtech:gt.blockframes:73" />
- 28 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.2:3" /> <ItemImage id="miscutils:gtplusplus.blockspecialcasings.2:3"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:112" /><ItemImage id="gregtech:gt.sheetmetal:112"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:391" /><ItemImage id="gregtech:gt.sheetmetal:391"/>
- 16 <ItemLink id="gregtech:gt.sheetmetal:69" /><ItemImage id="gregtech:gt.sheetmetal:69"/>
- 4 <ItemLink id="gregtech:gt.sheetmetal:112" /><ItemImage id="gregtech:gt.sheetmetal:112"/>
- 4 <ItemLink id="gregtech:gt.blockcasings11:5" /><ItemImage id="gregtech:gt.blockcasings11:5" />

## 간소화된 주조기 <ItemImage id="gregtech:gt.foundrycasings:10" />
SC 모듈(UEV)은 기본 150% 속도에 더해 엑소 주조소의 기본 속도를 150% 증가시킵니다. 이는 다음 방정식에서 볼 수 있습니다. 즉 SC 하나로 총 300% 속도, 둘로 450% 속도입니다. 가산 보너스는 헬리오캐스트 보강 모듈과 중첩되고, 범용 붕괴기 모듈의 곱셈 보너스는 이후에 적용됩니다. 엑소 주조소당 SC 모듈 수에는 제한이 없습니다. SC를 초고밀도 주조 분지 모듈과 조합하면 최적 생산이 해금되며, 이는 전압 티어당 +6개 병렬 처리 및 +75% 속도의 일회성 보너스입니다.
<Latex formula="(150\% + \sum \text{AddBonus}) \times \prod \text{MultBonus}" />

| 모듈   | 속도    |
|--------------- | --------------- |
| SC 1개   | $$(150\% + 150\%) \times 1 = 300\%$$   |
| SC 2개   | $$(150\% + 300\%) \times 1 = 450\%$$   |
| SC+ 1개   | $$(150\% + 225\%) \times 1 = 375\%$$   |
| SC+ 2개   | $$(150\% + 375\%) \times 1 = 525\%$$   |

### 필요:
- 64 <ItemLink id="gregtech:gt.foundrycasings:10" /><ItemImage id="gregtech:gt.foundrycasings:10" />
- 28 <ItemLink id="gregtech:gt.blockframes:974" /><ItemImage id="gregtech:gt.blockframes:974" />
- 24 <ItemLink id="gregtech:gt.blockframes:329" /><ItemImage id="gregtech:gt.blockframes:329" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:974" /><ItemImage id="gregtech:gt.sheetmetal:974" />
- 12 <ItemLink id="miscutils:gtplusplus.blockcasings.5:3" /><ItemImage id="miscutils:gtplusplus.blockcasings.5:3" />
- 12 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:13" /><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:13" />

## 초냉각기 <ItemImage id="gregtech:gt.foundrycasings:9" />
HC 모듈(UIV)은 기계가 작동하는 동안 냉각제를 소비하여 에너지 해치의 전압 티어를 초과하는 최대 오버클럭 수를 증가시킵니다. 냉각제는 엑소 주조소가 아닌 모듈 자체의 입력 해치를 통해 공급하십시오. 추가 오버클럭 수는 다음 표에서 볼 수 있듯이 제공된 냉각제의 종류에 따라 달라집니다. 엑소 주조소당 HC 모듈은 1개로 제한됩니다. HC를 범용 붕괴기 모듈과 조합하면 실현된 잠재력이 해금되며, 이는 이터니티를 최대 3회의 추가 오버클럭을 위한 냉각제로 사용할 수 있게 하고, 전력 소비를 2배로 곱하며, 속도를 2배로 곱하는 일회성 보너스입니다.
| 냉각제 | 유량 | 오버클럭 |
| --------------- | --------------- | --------------- |
| 초냉각제 | 100 L/s | +1 |
| 시공간 | 50 L/s | +2 |
| 이터니티* | 25 L/s | +3 |

### 필요:
- 64 <ItemLink id="gregtech:gt.sheetmetal:389" /> <ItemImage id="gregtech:gt.sheetmetal:389" />
- 48 <ItemLink id="gregtech:gt.blockframes:394" /><ItemImage id="gregtech:gt.blockframes:394" />
- 36 <ItemLink id="gregtech:gt.foundrycasings:9" /><ItemImage id="gregtech:gt.foundrycasings:9"/>
- 20 <ItemLink id="gregtech:gt.blockcasings8:14" /> <ItemImage id="gregtech:gt.blockcasings8:14" />
- 19 <ItemLink id="miscutils:gtplusplus.blockcasings.3:10"/><ItemImage id="miscutils:gtplusplus.blockcasings.3:10" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:985" /><ItemImage id="gregtech:gt.sheetmetal:985"/>
- 1 입력 해치(모든 극저온 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />

## 헬리오캐스트 보강 <ItemImage id="gregtech:gt.foundrycasings:7" />
HR 모듈(UIV)은 엑소 주조소의 UIV+ 레시피를 해금합니다. 여기에는 하이포젠, 이터니티, 유니버시움 또는 마그마터를 사용하는 모든 유체 고체화기 레시피와 초월적으로 강화된 붕규산 유리 및 호킹 복사 재정렬 집속 유리가 포함됩니다. 엑소 주조소당 HR 모듈 수에는 제한이 없습니다. HR을 자기 자신과 조합하면 초안정 코어가 해금되며, 이는 다음 표에서 볼 수 있듯이 총 HR 모듈 수에 기반한 규모 보너스입니다.

| 모듈   | 보너스    |
|--------------- | --------------- |
| $$\geq$$ HR 1개   | UIV+ 레시피 해금   |
| $$\geq$$ HR 2개   | HR당 +75% 속도   |
| $$\geq$$ HR 3개  | HR당 전압 티어당 +6 병렬 처리, 0.1 오버클럭 계수   |
| HR 4개   | +2 오버클럭   |

### 필요:
- 32 <ItemLink id="tectech:gt.godforgecasing:3" /><ItemImage id="tectech:gt.godforgecasing:3" />
- 24 <ItemLink id="gregtech:gt.blockframes:147" /><ItemImage id="gregtech:gt.blockframes:147" />
- 16 <ItemLink id="gregtech:gt.sheetmetal:588" /><ItemImage id="gregtech:gt.sheetmetal:588" />
- 16 <ItemLink id="tectech:tile.spatiallyTranscendentGravitationalLens" /> <ItemImage id="tectech:tile.spatiallyTranscendentGravitationalLens"/>
- 12 <ItemLink id="gregtech:gt.foundrycasings:7" /><ItemImage id="gregtech:gt.foundrycasings:7" />
- 12 <ItemLink id="gregtech:gt.blockframes:581"/><ItemImage id="gregtech:gt.blockframes:582"/>
- 12 <ItemLink id="gregtech:gt.blockframes:149"/><ItemImage id="gregtech:gt.blockframes:149"/>
- 12 <ItemLink id="gregtech:gt.blockframes:148"/><ItemImage id="gregtech:gt.blockframes:148"/>
- 12 <ItemLink id="gregtech:gt.blockframes:588"/><ItemImage id="gregtech:gt.blockframes:588"/>

## 자각형 오버클로커 <ItemImage id="gregtech:gt.foundrycasings:5"/>
SO 모듈(UMV)은 기계의 오버클럭 계수를 0.35만큼 증가시킵니다. 이는 다음 표에서 볼 수 있듯이 모든 불완전 오버클럭이 추가로 35% 속도를 제공한다는 뜻입니다. 엑소 주조소당 SO 모듈은 1개로 제한됩니다. SO를 프로토볼트 안정기 모듈과 조합하면 조화 효율이 해금되며, 이는 -50% EU/t 및 +0.1 오버클럭 계수의 일회성 보너스입니다.
| 속도 | OC 1회 | OC 2회 | OC 3회 | OC 4회 | OC 5회 |
| --------------- | --------------- | --------------- | --------------- | --------------- |--------------- |
| 기본 | 200% | 400% | 800% | 1,600% | 3,200% |
| $$\geq$$ HR 3개 | 210% | 441% | 926% | 1,945% | 4,084% |
| SO 1개 | 235% | 552% | 1,298% | 3,050% | 7,167% |
| SO+ 1개 | 245% | 600% | 1,471% | 3,603% | 8,827% |

### 필요:
- 72 <ItemLink id="GoodGenerator:magneticFluxCasing"/><ItemImage id="GoodGenerator:magneticFluxCasing"/>
- 48 <ItemLink id="GoodGenerator:gravityStabilizationCasing"/><ItemImage id="GoodGenerator:gravityStabilizationCasing"/>
- 40 <ItemLink id="gregtech:gt.foundrycasings:5"/><ItemImage id="gregtech:gt.foundrycasings:5"/>
- 36 <ItemLink id="GoodGenerator:antimatterContainmentCasing"/><ItemImage id="GoodGenerator:antimatterContainmentCasing"/>
- 24 <ItemLink id="gregtech:gt.foundrycasings:1"/> <ItemImage id="gregtech:gt.foundrycasings:1"/>
- 16 <ItemLink id="gregtech:gt.blockframes:327"/> <ItemImage id="gregtech:gt.blockframes:327"/>

## 범용 붕괴기 <ItemImage id="gregtech:gt.foundrycasings:4"/>
UC 모듈(UXV)은 전력 소비를 4배로 곱하고, 속도를 2배로 곱하며, 최소 케이싱 수를 20개 증가시킵니다. 이는 사실상 강제 불완전 오버클럭이며, 총 35개 주형에 대해 5개 입력만을 위한 공간을 남깁니다. 엑소 주조소당 UC 모듈은 1개로 제한됩니다. UC를 초냉각기 모듈과 조합하면 실현된 잠재력이 해금되며, 이는 이터니티를 최대 3회의 추가 오버클럭을 위한 냉각제로 사용할 수 있게 하고, 전력 소비를 2배로 곱하며, 속도를 2배로 곱하는 일회성 보너스입니다.

### 필요:
- 72 <ItemLink id="tectech:gt.blockcasingsBA0:11"/> <ItemImage id="tectech:gt.blockcasingsBA0:11"/>
- 48 <ItemLink id="tectech:gt.blockcasingsBA0:10"/><ItemImage id="tectech:gt.blockcasingsBA0:10"/>
- 40 <ItemLink id="gregtech:gt.blockframes:583" /> <ItemImage id="gregtech:gt.blockframes:583" />
- 28 <ItemLink id="gregtech:gt.blockmetal9:6"/><ItemImage id="gregtech:gt.blockmetal9:6"/>
- 28 <ItemLink id="gregtech:gt.blockmetal9:7"/><ItemImage id="gregtech:gt.blockmetal9:7"/>
- 16 <ItemLink id="gregtech:gt.blockframes:139"/><ItemImage id="gregtech:gt.blockframes:139"/>
- 8 <ItemLink id="gregtech:gt.blockframes:585"/><ItemImage id="gregtech:gt.blockframes:585"/>
- 8 <ItemLink id="gregtech:gt.blockframes:586"/><ItemImage id="gregtech:gt.blockframes:586"/>
- 4 <ItemLink id="gregtech:gt.foundrycasings:4"/><ItemImage id="gregtech:gt.foundrycasings:4"/>
- 4 <ItemLink id="gregtech:gt.blockmetal9:13"/><ItemImage id="gregtech:gt.blockmetal9:13"/>

## 조합
엑소 주조소에 추가 보너스를 제공하는 네 가지 고유 모듈 조합이 있습니다. 이들은 모두 위의 모듈 하위 섹션에서 설명했지만, 참고를 위해 여기에 요약합니다. 이 보너스는 각 모듈이 두 개씩 있어도 한 번만 적용됩니다. 예를 들어, ECB 두 개와 SC 두 개를 가져도 최적 생산의 보너스는 두 배가 되지 않습니다.

- 최적 생산: 초고밀도 주조 분지 + 간소화된 주조 - 전압 티어당 +6 병렬 처리, +75% 속도
- 조화 효율: 프로토볼트 안정기 + 자각형 오버클로커 - -50% EU/t, +0.1 오버클럭 계수
- 초안정 코어: 헬리오캐스트 보강 + 헬리오캐스트 보강 - HR 수에 따라 달라짐(전용 섹션 참조)
- 실현된 잠재력: 범용 붕괴기 + 초냉각기 - 이터니티 냉각제 해금, EU/t 2배, 속도 2배

## 최적 구성
가능한 모듈 조합은 많으며, 어떤 것이 가장 효과적인지 완전히 명확하지는 않습니다. 이들 모두 중에서 선택하는 데 도움이 되도록, 다음 표는 게임의 여러 단계에서 나머지보다 두드러지는 몇 가지를 비교합니다. 해치 공간은 에너지 해치 하나만 가정하며, 상대 처리량은 다음 방정식으로 계산됩니다. 여기서 N은 레시피보다 높은 전압 티어 수입니다.
<Latex formula="\text{Throughput} = \text{Parallels} \times \text{Speed} \times (\text{OC Factor})^N \times 2^{\text{Bonus OC}}" />

UIV+ 레시피를 실행하려면 최소 하나의 HR 모듈이 필요하지만, 가장 최적의 구성에 항상 그것이 있는 것은 아닙니다. 따라서 최소 두 개의 엑소 주조소를 두고 전압 티어에 따라 레시피를 나누는 것이 권장됩니다.

각 전압 티어별 특정 최적 구성은 [위키 페이지!](https://wiki.gtnewhorizons.com/wiki/Exo-Foundry)의 하단 섹션을 확인하십시오.