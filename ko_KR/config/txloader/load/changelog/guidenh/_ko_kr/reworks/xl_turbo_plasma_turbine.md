---
item_ids:
  - gregtech:gt.blockmachines:15523
navigation:
  title: XL 터보 플라즈마 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15523
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# XL 터보 플라즈마 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15523"/>
</GameScene>
<Color id="GREEN">XL 터보 플라즈마 터빈(XLPT)</Color>은 플라즈마로부터 막대한 전력을 생산하기 위한 ZPM 티어 멀티블록입니다. <Color id="GREEN">XLPT</Color>는 단 12개의 터빈으로 16배의 처리량을 가지며, 다중 앰프 및 레이저 다이너모 해치를 지원하고, 기계가 작동 중일 때 다이너모 해치가 파괴되어도 폭발하지 않기 때문에 대형 플라즈마 터빈에서 직접 업그레이드한 것입니다. 그러나 기계가 작동하려면 터빈이 모두 동일해야 하며, 최적 유량을 초과할 때 더 가혹한 페널티가 있고, 밀도가 낮은 연료를 사용할 때 페널티가 있으며, 기계가 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">XLPT</Color>를 자동으로 켜고 끄면 연료를 절약할 수 있습니다. 
<br clear="all"/>


[GTNH 전력 플래너](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일합니다.

## 건설
<Color id="GREEN">XLPT</Color>에는 티어 부품이 없습니다. 유리는 어떤 티어든 사용할 수 있으며 기계 작동에 영향을 주지 않습니다. 가열 코일은 반드시 나콰다여야 하며 역시 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물 어디에서든 터빈 케이싱을 대체할 수 있습니다. 본격적인 전력 생산을 위해 <Color id="GREEN">다중 앰프 및 레이저 다이너모 해치</Color>가 지원되며, 여러 개를 둘 수 있습니다. 소음기 해치는 없으므로 포함하지 마십시오. 터빈은 입력 버스나 컨트롤러의 GUI를 통해 넣으십시오. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용해 하위 채널 "glass"로 구조를 시각화/건설하여 유리의 티어를 지정하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15523"/><ItemImage id="gregtech:gt.blockmachines:15523"/>
- 330-351 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:4"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:4"/>
- 100 <ItemLink id="gregtech:gt.blockcasings5:5"/><ItemImage id="gregtech:gt.blockcasings5:5"/>
- 72 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 36 티어 유리(아무거나) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 32 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1개 이상 다이너모 해치(아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1개 정비 해치(아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1개 이상 입력 버스(아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1개 이상 입력 해치(아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 1개 이상 출력 해치(아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">XLPT</Color>는 케이싱, 가열 코일, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 입력 해치는 공유하지 마십시오. 연료가 <Color id="GREEN">XLPT</Color>들 사이에 균등하게 분배되지 않아 하나가 전부 소비하고 다른 하나는 아무것도 받지 못합니다. 

## 사용법
<Color id="GREEN">XLPT</Color>에는 아래에 나열된 두 가지 작동 모드가 있습니다. 다만 두 모드의 정량적 차이는 상단에 링크된 플래너를 참조하십시오. 전자는 연료 생산이 낮은 초중반 게임에 더 좋고, 후자는 효율보다 전력 출력이 더 중요한 후반 게임에 더 좋습니다. 컨트롤러에 스크루드라이버를 사용해 모드를 전환하십시오.

- 밀착 장착 모드 - 높은 효율, 낮은 최적 유량(전력).
- 느슨한 장착 모드 - 낮은 효율, 높은 최적 유량(전력).

<Color id="GREEN">XLPT</Color>의 속도는 작동 중에는 100%까지 선형적으로 증가하고, 비작동 중에는 다시 0%로 감소합니다. 속도는 기계의 전력 출력에 정비례하며, 터빈 크기/재질에 관계없이 최대값에 도달하는 데 50초가 걸립니다. <Color id="GREEN">XLPT</Color>가 비활성화되거나, 터빈이 제거되거나, 구조물이 파괴되거나, 연료가 바닥나면 속도가 극도로 빠르게 감소합니다. 컨트롤러에 휴대용 스캐너 <ItemImage id="gregtech:gt.metaitem.01:32762"/>를 사용하거나 WAILA의 "efficiency" 값을 확인하여 터빈의 현재 속도를 볼 수 있습니다. 

## 최적 유량
플라즈마가 <Color id="GREEN">XLPT</Color>로 들어가는 속도(L/s)는 매우 중요합니다. 플라즈마가 너무 적으면 잠재 전력의 일부만 생산되고, 너무 많으면 엄청난 양의 연료가 낭비됩니다. 이상적으로는 플라즈마가 터빈의 최적 유량으로 <Color id="GREEN">XLPT</Color>에 들어가야 하며, 이는 크기/재질과 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 볼 수 있지만, L/s 단위의 최적 유량($$\dot{m}^*$$)은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재질과 관련된 배율이고, size는 1=소형에서 4=초대형 사이의 상수이며, $$\eta_0$$는 터빈의 기본 효율입니다. 이는 [대형 플라즈마 터빈](./large_plasma_turbine.md)의 최적 유량에 정확히 16배입니다. 

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 16,000 \div EU/L">
  여기서:
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 배율
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 32,000 \div EU/L \times 1.03^{20(\eta_0 - 0.8)}">
  여기서:
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 배율
  - $$\eta_0$$: 기본 효율
</Latex>

일부 플라즈마는 밀도가 약간 낮아 최적 유량이 더 높습니다. 특히 <Color id="GREEN">XLPT</Color>가 느슨한 모드일 때 그렇습니다. 플레이어는 증가한 수요를 맞추기 위해 유체 레귤레이터를 업그레이드하거나 두 번째 입력 해치를 추가해야 할 수 있습니다. 결국 사실상 전송 제한이 없고 온도나 열용량을 고려하지 않는 AE2 유체 P2P 터널로 전환해야 합니다. 

> [!IMPORTANT]
> 밀도가 낮은 연료를 사용하면 다음 방정식에서 볼 수 있듯이 전력 페널티가 있습니다.

<Latex formula="\epsilon = \frac{(\text{EU/L} \div 200,000)^2}{\text{Optimal EU/t (Tight)}}"/>

## 전력
<Color id="GREEN">XLPT</Color>에서 생성되는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$), 밀도 페널티($$\epsilon$$)에 따라 달라집니다. 최적 유량을 초과하면 효율이 낮아질 뿐만 아니라 생성되는 총 전력량도 줄어듭니다. 오버플로 티어는 기계 작동에 영향을 주지 않습니다. 컨트롤러를 보면서 WAILA를 통해 또는 산업 정보 패널로 기계의 현재 전력 출력을 확인하십시오.

전력은 구조물 어디에서든 레이저 또는 다중 앰프 다이너모 해치에서 추출됩니다. 다이너모 버퍼의 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC)가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">XLPT</Color>는 폭발하지 않습니다. 추가 EU는 그냥 소멸됩니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">XLPT</Color>를 자동으로 켜고 끄는 것을 적극 권장합니다.

<Latex formula="EU/t = \dot{m} \times \Biggl( 1 - \frac{| \dot{m} - \dot{m}^* |}{\dot{m}^*} \Biggr) \times EU/L \times \eta \times \epsilon \div 20">
  여기서:
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 터빈 효율
  - $$\epsilon$$: 밀도 페널티
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times 1.25">
  여기서:
  - $$\dot{m}_{max}$$: 최대 유량
  - $$\dot{m}^*$$: 최적 유량
</Latex>

# 터빈
기계가 작동하려면 12개의 터빈이 모두 정확히 동일해야 합니다. 터빈은 네 가지 크기와 다양한 재질로 제공되며 각각 고유한 효율 보너스와 최적 유량을 가집니다. 너무 많은 조합이 있어 모두 여기에 나열할 수는 없지만, 상단에 링크된 플래너에 모든 관련 정보와 어떤 터빈이 어떤 연료를 사용할 때의 전력 출력 및 수명을 결정하는 계산기까지 있습니다.

- 소형 터빈은 긴 마그날륨 막대로 제작합니다(LV만 되어도 사용 가능).
- 일반 터빈은 긴 티타늄 막대로 제작합니다(달 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>에 간 뒤 HV 끝자락에서 사용 가능).
- 대형 터빈은 긴 텅스텐강 막대로 제작합니다(텅스텐 처리 라인 이후 IV에서 사용 가능).
- 초대형 터빈은 긴 아메리슘 막대로 제작합니다(핵융합로 Mk-II <ItemImage id="gregtech:gt.blockmachines:32020"/>를 건설한 뒤 ZPM에서 사용 가능).

## 내구도
터빈은 생성된 전력에 비례해 서서히 내구도를 잃습니다. 터빈의 총 내구도는 재질에 따라 다르며 0%가 되는 즉시 완전히 소멸합니다. 터빈은 입력 버스를 통해 컨트롤러에 자동으로 삽입할 수 있지만 자동으로 추출할 수는 없습니다.

다음 방정식은 <Color id="GREEN">XLPT</Color>의 현재 전력 출력으로부터 터빈의 수명(시간)을 계산합니다. 느슨한 장착 모드는 더 높은 전력 출력으로 인한 수명 감소를 보상하기 위해 25% 내구도 보너스를 제공하며, 터빈은 대형 증기 터빈보다 여기서 훨씬 오래갑니다. 터빈은 일반적으로 수백 시간(또는 그 이상)의 수명을 가지므로 그렇게 자주 교체할 필요가 없습니다. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- 느슨한 장착 모드에서는 수명 결과에 1.25를 곱하십시오.