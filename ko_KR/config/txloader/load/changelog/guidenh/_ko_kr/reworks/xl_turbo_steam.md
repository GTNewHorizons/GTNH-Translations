---
item_ids:
  - gregtech:gt.blockmachines:15519
navigation:
  title: XL 터보 증기 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15519
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# XL 터보 증기 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15519"/>
</GameScene>
<Color id="GREEN">XL 터보 증기 터빈(XLST)</Color>은 증기로부터 막대한 전력을 생산하기 위한 EV 티어 멀티블록입니다. <Color id="GREEN">XLST</Color>는 대형 증기 터빈 <ItemImage id="gregtech:gt.blockmachines:15524"/>의 직접적인 업그레이드입니다. 왜냐하면 단 12개의 터빈으로 <Color id="RED">16배</Color>의 처리량을 가지며, <Color id="GREEN">멀티앰프 및 레이저 다이나모 해치</Color>를 지원하고, 일반 증기와 고밀도 증기를 모두 처리하며, 기계가 작동 중일 때 다이나모 해치가 파괴되어도 폭발하지 않기 때문입니다. 그러나 기계가 작동하려면 터빈이 모두 동일해야 하며, 최적 유량을 초과하면 더 가혹한 페널티가 있고, 기계가 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">XLST</Color>를 자동으로 토글하여 연료를 절약하십시오.

고밀도 증기 변종은 극한 열교환기 <ItemImage id="gregtech:gt.blockmachines:32017"/>에서 플라즈마를 사용해야만 얻을 수 있으며, 일반 증기 변종보다 연료 밀도가 1,000배 높습니다. 즉, 최적 유량의 1/1000만으로도 동일한 양의 전력을 생산할 수 있습니다. 

[GTNH 전력 계획기](https://docs.google.com/spreadsheets/d/1FTFdfmY_UWbTbFOyNzARKeI90pbHvPBH6M3JHJmaC-E/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 이 멀티블록의 구조만 변경되었으며, 작동 방식은 동일합니다

## 건설

<Color id="GREEN">XLST</Color>에는 티어별 구성 요소가 없습니다. 유리는 어떤 티어든 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 솔레노이드 코일은 반드시 MV여야 하며 역시 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물 어디에서든 터빈 케이싱을 대체할 수 있습니다. <Color id="GREEN">멀티앰프 및 레이저 다이나모 해치</Color>는 대규모 전력 생성을 위해 지원되며, 여러 개를 설치할 수 있습니다. 머플러 해치는 없으므로 포함하지 마십시오. 터빈은 입력 버스나 컨트롤러의 GUI를 통해 삽입하십시오. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "glass"로 구조물을 시각화/건설하여 유리의 티어를 지정하십시오.

### 필요:
- XL 터보 증기 터빈 컨트롤러 1개 (유형에 따라 다름)<ItemImage id="gregtech:gt.blockmachines:15519"/>
- 372-439 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:1"/>
- 파이프 케이싱 100개 (유형에 따라 다름) <ItemImage id="gregtech:gt.blockcasings2:13"/>
- 티어 유리 36개 (아무거나)
- 프레임 박스 34개 (유형에 따라 다름) <ItemImage id="gregtech:gt.blockframes:305"/>
- 20 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 다이나모 해치 1개 (아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 유지보수 해치 1개 (아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 입력 버스 1개 이상 (아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 입력 해치 1개 이상 (아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 해치 1개 이상 (아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">XLST</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 입력 해치는 공유하지 마십시오. 왜냐하면 연료가 <Color id="GREEN">XLST</Color>들 사이에 균등하게 분배되지 않기 때문입니다. 하나가 모든 것을 소비하고 다른 하나는 아무것도 받지 못합니다. 

## 사용법
<Color id="GREEN">XLST</Color>에는 아래에 나열된 두 가지 작동 모드가 있지만, 두 모드 간의 정량적 차이는 상단에 링크된 계획기를 참조하십시오. 전자는 증기 생산량이 낮은 초중반 게임에서 더 좋고, 후자는 효율보다 전력 출력이 더 중요한 후반 게임에서 더 좋습니다. 컨트롤러에 스크루드라이버를 사용하여 모드를 전환하십시오.

- 타이트 피팅 모드 - 높은 효율, 낮은 최적 유량(전력).
- 루즈 피팅 모드 - 낮은 효율, 높은 최적 유량(전력).

<Color id="GREEN">XLST</Color>의 속도는 작동 중일 때 선형적으로 100%까지 증가하고 비활성화되면 다시 0%로 감소합니다. 속도는 기계의 전력 출력에 정비례하며 터빈 크기/재질에 관계없이 최대값에 도달하는 데 50초가 걸립니다. <Color id="GREEN">XLST</Color>가 비활성화되거나, 터빈이 제거되거나, 구조물이 파괴되거나, 연료가 떨어지면 속도가 매우 빠르게 감소합니다. 컨트롤러에 휴대용 스캐너 <ItemImage id="gregtech:gt.metaitem.01:32762"/>를 사용하거나 WAILA에서 "efficiency" 값을 확인하여 터빈의 현재 속도를 볼 수 있습니다. 

## 최적 유량
증기가 <Color id="GREEN">XLST</Color>로 들어오는 유량(L/t)은 매우 중요합니다. 증기가 너무 적으면 잠재 전력의 일부만 생성되고, 너무 많으면 엄청난 양의 연료가 낭비됩니다. 이상적으로는 증기가 터빈의 최적 유량으로 <Color id="GREEN">XLST</Color>에 들어가야 하며, 이는 크기/재질 및 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 확인할 수 있지만, L/t 단위의 최적 유량($$\dot{m}^*$$)은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재질과 관련된 승수이고, size는 1=소형에서 4=대형 사이의 상수이며, $$\eta_0$$는 터빈의 기본 효율입니다. 이는 대형 증기 터빈의 최적 유량의 정확히 16배이며, 증기가 고밀도인 경우 유량은 1,000으로 나뉩니다.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 800">
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 승수
  - $$\text{size}$$: 터빈 크기에 따른 범위 (1:4)의 상수
</Latex>
<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 2,400 \times 1.1^{20(\eta_0 - 0.8)}">
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 승수
  - $$\text{size}$$: 터빈 크기에 따른 범위 (1:4)의 상수
  - $$\eta_0$$: 터빈의 기본 효율
</Latex>

일부 터빈의 최적 유량은 증기의 연료 밀도가 0.5 EU/L로 매우 낮기 때문에 엄청나게 높습니다. 특히 <Color id="GREEN">XLST</Color>가 루즈 모드일 때 그렇습니다. 고밀도 증기를 사용하지 않는 경우, 사실상 AE2 유체 P2P 터널을 사용해야 합니다. 이 터널은 실질적으로 전송 제한이 없고 온도나 열용량에 대한 걱정이 없습니다.
| 연료   | EU/L    |
|--------------- | --------------- |
| 증기   | 0.5   |
| 과열 (SH) 증기   | 1.0   |
| 초임계 (SC) 증기   | 1.0   |
| 고밀도 증기   | 500   |
| 고밀도 과열 (SH) 증기 | 1,000 |
| 고밀도 초임계 (SC) 증기 | 1,000 |

## 전력
<Color id="GREEN">XLST</Color>에서 생성되는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$)에 따라 달라집니다. 최적 유량을 초과하면 효율이 떨어질 뿐만 아니라 생성되는 총 전력량도 감소합니다. 오버플로 티어는 기계 작동에 영향을 주지 않습니다. 컨트롤러를 바라보면서 WAILA를 통해 또는 산업 정보 패널로 기계의 현재 전력 출력을 확인하십시오.

전력은 구조물 어디에서든 레이저 또는 멀티앰프 다이나모 해치에서 추출됩니다. 다이나모의 버퍼에서 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC)가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">XLST</Color>는 폭발하지 않습니다. 추가 EU는 단순히 소멸됩니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">XLST</Color>를 자동으로 토글하는 것이 매우 권장됩니다.

# 터빈
기계가 작동하려면 12개의 터빈이 모두 정확히 동일해야 합니다. 터빈은 네 가지 크기와 다양한 재질로 제공되며, 각각 고유한 효율 보너스와 최적 유량을 가집니다. 여기에 모두 나열하기에는 너무 많은 조합이 있지만, 상단에 링크된 계획기에는 모든 관련 정보와 모든 연료에 대한 모든 터빈의 전력 출력 및 수명을 결정하는 계산기까지 있습니다.

- 소형 터빈은 긴 마그날륨 막대기로 제작됩니다 (LV부터 사용 가능)
- 일반 터빈은 긴 티타늄 막대기로 제작됩니다 (달 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>에 다녀온 후 HV 끝자락에서 사용 가능)
- 대형 터빈은 긴 텅스텐강 막대기로 제작됩니다 (텅스텐 처리 라인 이후 IV에서 사용 가능)
- 거대 터빈은 긴 아메리슘 막대기로 제작됩니다 (핵융합로 Mk-II <ItemImage id="gregtech:gt.blockmachines:32020"/>를 건설한 후 ZPM에서 사용 가능)

## 내구도
터빈은 생성된 전력에 비례하여 서서히 내구도를 잃습니다. 터빈의 총 내구도는 재질에 따라 다르며 0%에 도달하면 즉시 소멸됩니다. 터빈은 입력 버스를 통해 컨트롤러에 자동으로 삽입할 수 있지만 자동으로 추출할 수는 없습니다.

다음 방정식은 <Color id="GREEN">XLST</Color>의 현재 전력 출력으로부터 터빈의 수명(시간)을 계산합니다. 루즈 피팅 모드는 더 높은 전력 출력으로 인한 수명 감소를 보상하기 위해 25%의 내구도 증가를 제공하며, 터빈은 대형 증기 터빈보다 여기서 훨씬 오래 지속됩니다. 터빈은 일반적으로 수백 시간(또는 그 이상)의 수명을 가지므로 자주 교체할 필요가 없습니다. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- 루즈 피팅 모드에서는 수명 결과에 1.25를 곱하십시오.