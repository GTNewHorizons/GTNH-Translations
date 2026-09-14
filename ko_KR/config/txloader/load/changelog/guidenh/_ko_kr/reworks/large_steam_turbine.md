---
item_ids:
  - gregtech:gt.blockmachines:15524
navigation:
  title: 대형 증기 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15524
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대형 증기 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15524"/>
</GameScene>
<Color id="GREEN">대형 증기 터빈 (LST)</Color>는 증기로 전력을 생성하는 HV 티어 멀티블록입니다. <Color id="GREEN">LST</Color>는 훨씬 높은 효율로 최대 4A의 전력을 출력하므로 단일블록 증기 터빈의 직접적인 업그레이드입니다. 그러나 기계가 작동하려면 컨트롤러 안에 터빈을 넣어야 하고, 증기 입력 속도를 신중하게 조절해야 하며, 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 터빈은 네 가지 크기와 다양한 재료로 제공되며, 각각 고유한 효율 보너스와 최적 유량(L/t)을 가집니다. 증기가 출력 해치에서 증류수로 응축됨에 따라 전력은 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수면 폭발합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">LST</Color>를 자동으로 켜고 끄면 연료를 절약할 수 있습니다.

<Color id="RED">대형 고압 증기 터빈 (LST-HP)</Color> <ItemImage id="gregtech:gt.blockmachines:15525"/>와 <Color id="BLUE">대형 초임계 증기 터빈 (LST-SC)</Color> <ItemImage id="gregtech:gt.blockmachines:15526"/>는 각각 과열 증기와 초임계 증기만 처리한다는 점을 제외하면 LST와 거의 동일합니다. 초임계 증기는 동일한 최적 유량에서 일반 증기의 두 배 EU를 생성하고 과열 증기로 변환됩니다. 과열 증기는 동일한 최적 유량에서 일반 증기의 두 배 EU를 생성하고 일반 증기로 변환됩니다.

[GTNH 전력 플래너](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)

<Color id="GREEN">LST</Color>는 16개의 <Color id="GREEN">LST</Color>만큼 많은 증기를 소비하고 그만큼 많은 전력을 생산하지만 터빈은 12개만 필요로 하는 [XL 터보 증기 터빈](./xl_turbo_steam.md)으로 대체됩니다. 또한 본격적인 전력 생성을 위한 <Color id="GREEN">다중 앰프 및 레이저 에너지 해치</Color>를 지원하며 HP 및 SC 변형으로 제공됩니다. 
<br clear="all"/>

> [!NOTE]
> 구조만 변경되었으며, 그 외의 메커니즘은 변경되지 않았습니다.

## 건설
<Color id="GREEN">LST</Color>에는 티어 부품이 없습니다. 유지보수 해치, 입력 해치, 출력 해치는 구조물 뒤쪽 절반의 모든 터빈 케이싱을 대체할 수 있습니다. 다이너모 해치는 구조물 맨 뒤 중앙 케이싱으로 제한되며 4A보다 클 수 없습니다. 소음기 해치는 없으므로 포함하지 마십시오. 컨트롤러 바로 앞의 9개 블록은 반드시 공기여야 합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조를 시각화/건설하십시오.

대형 터빈 고유의 부품으로 터빈 하우징 <ItemImage id="gregtech:gt.blockmachines:31025"/>이 있으며, 이는 컨트롤러 내부의 터빈이 파손되면 자동으로 교체할 여분 터빈을 보관하는 사실상의 ULV 입력 버스입니다. 완전히 선택 사항이며 UV에 해금되지만, 가동 시간을 최대화하는 데 도움이 됩니다.

### 필요 항목:
- 1개의 대형 증기 터빈 (해당 유형) <ItemImage id="gregtech:gt.blockmachines:15524"/>
- 14개의 프레임 박스 (터빈 유형에 따름) <ItemImage id="gregtech:gt.blockframes:32"/>
- 8-14개의 터빈 케이싱 (터빈 유형에 따름) <ItemImage id="gregtech:gt.blockframes:32"/>
- 12개의 파이프 케이싱 (터빈 유형에 따름) <ItemImage id="gregtech:gt.blockcasings2:13"/>
- 1개의 다이너모 해치 (뒤 중앙 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1개의 유지보수 해치 (뒤쪽 터빈 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 0개 이상의 입력 해치 (뒤쪽 터빈 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0개 이상의 출력 해치 (뒤쪽 터빈 케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">LST</Color>들은 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 그러나 연료가 <Color id="GREEN">LST</Color>들 사이에 균등하게 분배되지 않으므로 입력 해치를 공유하지 마십시오. 한쪽이 모든 것을 소비하고 다른 쪽은 아무것도 받지 못합니다. 해치 위치 제한 때문에 어차피 그렇게 하기는 어렵습니다.

----------

## 사용법
<Color id="GREEN">LST</Color>에는 아래에 나열된 두 가지 작동 모드가 있지만, 두 모드 간의 정량적 차이는 상단에 링크된 플래너를 참조하십시오. 전자는 증기 생산량이 낮은 초중반 게임에 더 좋고, 후자는 효율보다 전력 출력이 더 중요한 후반 게임에 더 좋습니다. 컨트롤러에 드라이버를 사용하여 모드를 전환합니다.

- 타이트 피팅 모드 - 높은 효율, 낮은 최적 유량(전력).
- 루즈 피팅 모드 - 낮은 효율, 높은 최적 유량(전력).

<Color id="GREEN">LST</Color>의 속도는 작동 중에는 100%까지 선형적으로 증가하고, 비작동 중에는 다시 0%로 감소합니다. 속도는 기계의 전력 출력에 정비례하며, 터빈 크기/재료에 관계없이 최대값에 도달하는 데 50초가 걸립니다. <Color id="GREEN">LST</Color>가 비활성화되거나, 터빈이 제거되거나, 구조물이 파괴되거나, 연료가 떨어지면 속도가 매우 빠르게 감소합니다. 컨트롤러에 휴대용 스캐너 <ItemImage id="gregtech:gt.metaitem.01:32762"/>를 사용하거나 WAILA의 "효율" 값을 확인하여 터빈의 현재 속도를 볼 수 있습니다.

## 최적 유량
증기가 <Color id="GREEN">LST</Color>로 들어가는 속도(L/t)는 매우 중요합니다. 증기가 너무 적으면 잠재 전력의 일부만 생성되고, 너무 많으면 엄청난 양의 연료가 낭비됩니다. 이상적으로는 터빈의 최적 유량으로 <Color id="GREEN">LST</Color>에 증기가 들어가야 하며, 이 유량은 크기/재료와 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 확인할 수 있지만, L/t 단위의 최적 유량($$\dot{m}^*$$ )은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재료와 연관된 배수이고, size는 1=소형에서 4=거대 사이의 상수이며, $$\eta_0$$는 터빈의 <u>기본</u> 효율입니다.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 50">
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재료 배수
  - $$\text{size}$$: 터빈 크기에 따른 (1:4) 범위의 상수
</Latex>

<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 150 \times 1.1^{20(\eta_0 - 0.8)}">
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재료 배수
  - $$\text{size}$$: 터빈 크기에 따른 (1:4) 범위의 상수
  - $$\eta_0$$: 터빈의 기본 효율
</Latex>

일부 터빈의 최적 유량은 증기의 연료 밀도가 0.5 EU/L로 매우 낮기 때문에, 특히 <Color id="GREEN">LST</Color>가 루즈 모드일 때 믿을 수 없을 정도로 높습니다. 플레이어는 증가한 수요를 충족하기 위해 유체 조절기를 업그레이드하거나 두 번째 입력 해치를 추가해야 할 수 있습니다. 결국에는 전송 한도가 사실상 없고 온도나 열용량을 걱정할 필요가 없는 AE2 유체 P2P 터널 <ItemImage id="appliedenergistics2:item.ItemMultiPart:463"/>로 전환해야 합니다.

## 전력 및 오버플로
<Color id="GREEN">LST</Color>에서 생성되는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$)에 따라 달라집니다. 최적 유량을 초과하면 터빈의 오버플로 티어($$T$$)에 따라 추가 전력이 생성되지만 효율은 점차 감소합니다. 총 오버플로 티어는 세 개뿐이며, 전적으로 터빈 재료에 따라 결정됩니다. 더 높은 오버플로 티어는 최대 유량($$\dot{m}_{max}$$)도 증가시킵니다. NEI를 통해 터빈의 오버플로 티어를, WAILA를 통해 기계의 현재 전력 출력을 확인하십시오.

전력은 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수지 마십시오. 그렇지 않으면 <Color id="GREEN">LST</Color>가 폭발합니다. 다이너모 버퍼의 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC) <ItemImage id="gregtech:gt.blockmachines:13106"/>가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">LST</Color>는 폭발하지 않습니다. 추가 EU는 단순히 소멸합니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">LST</Color>를 자동으로 켜고 끄는 것을 강력히 권장합니다.

### 대형 증기 터빈:
<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 0.5 \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (T+1)} \Biggr) \times 0.5 \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
  - $$T$$: 오버플로 티어
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1)">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}_{max}$$: 최대 유량
  - $$T$$: 오버플로 티어
</Latex>

### 대형 고압 증기 터빈:
<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
</Latex>
<Latex formula="\text{EU/t} (> \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (T+2)} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
  - $$T$$: 오버플로 티어
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1.5)">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}_{max}$$: 최대 유량
  - $$T$$: 오버플로 티어
</Latex>

### 대형 초임계 증기 터빈:
<Latex formula="\text{EU/t} = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times 1.0 \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (0.5T + 1.5)">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}_{max}$$: 최대 유량
  - $$T$$: 오버플로 티어
</Latex>

## 터빈
기계가 작동하려면 컨트롤러의 GUI 안에 터빈을 넣어야 합니다. 터빈은 네 가지 크기와 다양한 재료로 제공되며, 각각 고유한 효율 보너스와 최적 유량을 가집니다. 여기에 모두 나열하기에는 경우의 수가 너무 많지만, 상단에 링크된 플래너에는 모든 관련 정보와 어떤 연료를 사용하든 모든 터빈의 전력 출력과 수명을 계산할 수 있는 계산기까지 있습니다.

- 소형 터빈은 긴 마그날륨 막대로 제작됩니다 (LV부터 사용 가능)
- 일반 터빈은 긴 티타늄 막대로 제작됩니다 (달에 다녀온 후 HV 말기에 사용 가능 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- 대형 터빈은 긴 텅스텐강 막대로 제작됩니다 (텅스텐 처리 라인 이후 IV에서 사용 가능)
- 거대 터빈은 긴 아메리슘 막대로 제작됩니다 (핵융합로 Mk-II <ItemImage id="gregtech:gt.blockmachines:32020"/>를 건설한 후 ZPM에서 사용 가능)

## 내구도
터빈은 생성된 전력에 비례하여 내구도를 서서히 잃습니다. 터빈의 총 내구도는 재료에 따라 달라지며, 0%에 도달하면 즉시 소멸합니다. 터빈은 컨트롤러에 직접 넣거나 뺄 수 없지만, 터빈 하우징은 60초마다 컨트롤러가 비어 있는지 확인하여 새 터빈을 넣습니다. 필요에 따라 하우징에 드라이버를 사용하여 간격을 줄이고, 머신 컨트롤러 커버로 <Color id="GREEN">LST</Color>를 다시 활성화하십시오.

다음 방정식은 <Color id="GREEN">LST</Color>의 현재 전력 출력으로부터 터빈의 수명(시간)을 계산합니다. 루즈 피팅 모드는 더 높은 전력 출력으로 인한 수명 감소를 보상하기 위해 내구도를 25% 증가시킵니다. 터빈은 일반적으로 수백 시간(또는 그 이상)의 수명을 가지므로 자주 교체할 필요가 없습니다.

<Latex formula="\text{Lifespan} (h) = \frac{\text{Durability}}{36 \times \text{min}(0.2 \times \text{EU/t}, (\text{EU/t})^{0.6})}"/>

- 루즈 피팅 모드에서는 수명 결과에 1.25를 곱하십시오.