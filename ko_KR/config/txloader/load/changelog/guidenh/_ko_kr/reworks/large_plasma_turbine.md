---
item_ids:
  - gregtech:gt.blockmachines:15528
navigation:
  title: 대형 플라즈마 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15528
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대형 플라즈마 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15528"/>
</GameScene>
<Color id="GREEN">대형 플라즈마 터빈(LPT)</Color>은 플라즈마로 전력을 생성하는 LuV 티어 멀티블록입니다. <Color id="GREEN">LPT</Color>는 최대 4A의 전력을 훨씬 높은 효율로 출력하므로 싱글블록 플라즈마 생성기에서 곧바로 업그레이드한 것입니다. 그러나 기계가 작동하려면 컨트롤러 안에 터빈을 넣어야 하고, 플라즈마 입력 속도를 신중하게 조절해야 하며, 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 터빈은 네 가지 크기와 다양한 재질로 제공되며 각각 고유한 효율 보너스와 최적 유량(L/s)을 가집니다. 전력은 플라즈마가 액체로 응축되면서 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수면 폭발합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">LPT</Color>를 자동 전환하면 연료를 절약할 수 있습니다.

<Color id="GREEN">LPT</Color>는 XL 터보 플라즈마 터빈 <ItemImage id="gregtech:gt.blockmachines:15523"/>으로 대체되며, 이는 16개의 <Color id="GREEN">LPT</Color>만큼 많은 플라즈마를 소비하고 많은 전력을 생산하지만 터빈은 12개만 필요로 합니다. 또한 본격적인 전력 생성을 위한 다중 암페어 및 레이저 에너지 해치를 지원합니다.

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br />

> [!NOTE]
> 구조 자체만 변경되었으며, 멀티블록의 핵심 기능은 이전과 동일합니다.

## 건설
<Color id="GREEN">LPT</Color>에는 티어별 구성 요소가 없습니다. 유지보수 해치, 입력 해치, 출력 해치는 구조물 뒤쪽 절반의 모든 터빈 케이싱을 대체할 수 있습니다. 다이너모 해치는 구조물 맨 뒤쪽 중앙 케이싱으로 제한되며 4A를 초과할 수 없습니다. 소음기 해치는 없으므로 포함하지 마십시오. 컨트롤러 바로 앞의 9개 블록은 반드시 공기여야 합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조를 시각화하거나 건설하십시오.

대형 터빈에만 있는 터빈 하우징 <ItemImage id="gregtech:gt.blockmachines:31025"/>은 사실상 예비 터빈을 보관하는 ULV 입력 버스로, 컨트롤러 내부의 터빈이 파손되면 자동으로 교체합니다. 완전히 선택 사항이며 UV 티어에 해금되지만, 가동 시간을 최대화하는 데 도움이 됩니다.

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15528"/><ItemImage id="gregtech:gt.blockmachines:15528"/>
- 14 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 8-14 <ItemLink id="gregtech:gt.blockcasings4:12"/><ItemImage id="gregtech:gt.blockcasings4:12"/>
- 12 <ItemLink id="gregtech:gt.blockcasings2:15"/><ItemImage id="gregtech:gt.blockcasings2:15"/>
- 다이너모 해치 1개(뒤쪽 중앙 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 유지보수 해치 1개(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 입력 해치 0개 이상(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 해치 0개 이상(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">LPT</Color>는 공간, 케이싱, 해치를 절약하기 위해 각 측면의 벽을 공유할 수 있습니다. 그러나 입력 해치는 공유하지 마십시오. 연료가 <Color id="GREEN">LPT</Color>들 사이에 균등하게 분배되지 않아 한쪽이 전부 소비하고 다른 쪽은 아무것도 받지 못하기 때문입니다. 해치 위치 제한으로 인해 어차피 그렇게 하기는 어렵습니다.

## 사용법
<Color id="GREEN">LPT</Color>에는 아래에 나열된 두 가지 작동 모드가 있지만, 두 모드 간의 수치적 차이는 상단에 링크된 플래너를 참조하십시오. 전자는 플라즈마 생산량이 낮은 게임 초중반에 더 좋고, 후자는 효율보다 전력 출력이 더 중요한 게임 후반에 더 좋습니다. 컨트롤러에 스크류드라이버를 사용하여 모드를 전환하십시오.

- 밀착 장착 모드 - 높은 효율, 낮은 최적 유량(전력).
- 느슨한 장착 모드 - 낮은 효율, 높은 최적 유량(전력).

<Color id="GREEN">LPT</Color>의 속도는 작동 중에는 100%까지 선형적으로 증가하고 비작동 중에는 다시 0%로 감소합니다. 속도는 기계의 전력 출력에 정비례하며, 터빈 크기/재질에 관계없이 최대값에 도달하는 데 50초가 걸립니다. <Color id="GREEN">LPT</Color>가 비활성화되거나, 터빈이 제거되거나, 구조물이 파괴되거나, 연료가 떨어지면 속도가 매우 빠르게 감소합니다. 컨트롤러에 휴대용 스캐너를 사용하거나 WAILA의 "efficiency" 값을 확인하여 터빈의 현재 속도를 볼 수 있습니다.

## 최적 유량
<Color id="GREEN">LPT</Color>에 플라즈마가 들어오는 속도(L/s)는 매우 중요합니다. 플라즈마가 너무 적으면 잠재 전력의 일부만 생성되고, 너무 많으면 엄청난 양의 연료가 낭비됩니다. 이상적으로는 플라즈마가 터빈의 최적 유량으로 <Color id="GREEN">LPT</Color>에 들어가야 하며, 이 유량은 크기/재질과 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 확인할 수 있지만, L/s 단위의 최적 유량($$\dot{m}^*$$)은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재질과 연관된 배수이고, size는 1=소형에서 4=초대형 사이의 상수이며, $$\eta_0$$는 터빈의 기본 효율입니다.

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 1,000 \div EU/L">
  여기서:
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 배수
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 2,000 \div EU/L \times 1.03^{20(\eta_0 - 0.8)}">
  여기서:
  - $$\dot{m}^*$$: 최적 유량
  - $$k$$: 재질 배수
  - $$\eta_0$$: 기본 효율
</Latex>

밀착 장착 모드에서 최적 유량을 계산하는 더 빠르고 쉬운 방법은 최적 플라즈마 EU/t(NEI에서 확인 가능)를 플라즈마 밀도로 나눈 다음 그 결과에 40/3을 곱하는 것입니다. 일부 플라즈마는 밀도가 약간 낮아 최적 유량이 더 높습니다. 특히 <Color id="GREEN">LPT</Color>가 느슨한 장착 모드일 때 그렇습니다. 플레이어는 증가한 수요를 충족하기 위해 유체 조절기를 업그레이드하거나 두 번째 입력 해치를 추가해야 할 수도 있습니다. 결국에는 사실상 전송 한도가 없고 온도나 열용량을 고려하지 않는 AE2 유체 P2P 터널로 전환해야 합니다.

## 전력 및 오버플로
<Color id="GREEN">LPT</Color>에서 생성되는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$)에 따라 달라집니다. 최적 유량을 초과하면 터빈의 오버플로 티어($$T$$)에 따라 추가 전력이 생성되지만 그 효율은 체감합니다. 오버플로 티어는 총 세 개뿐이며, 전적으로 터빈 재질에 따라 결정됩니다. 오버플로 티어가 높을수록 최대 유량($$\dot{m}_{max}$$)도 증가합니다. NEI를 통해 터빈의 오버플로를, WAILA를 통해 기계의 현재 전력 출력을 확인하십시오.

전력은 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수지 마십시오. 그렇지 않으면 <Color id="GREEN">LPT</Color>가 폭발합니다. 다이너모 버퍼의 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC)가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">LPT</Color>는 폭발하지 않습니다. 추가 EU는 단순히 소멸됩니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">LPT</Color>를 자동 전환하는 것을 적극 권장합니다.

<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times EU/L \times \eta \div 20">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
</Latex>
<Latex formula="\text{EU/t} (&gt; \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (3T+1)} \Biggr) \times EU/L \times \eta \div 20">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
  - $$T$$: 오버플로 티어
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (1.5T + 1)">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}_{max}$$: 최대 유량
  - $$T$$ 오버플로 티어
</Latex>

# 터빈
기계가 작동하려면 컨트롤러의 GUI 안에 터빈을 넣어야 합니다. 터빈은 네 가지 크기와 다양한 재질로 제공되며, 각각 고유한 효율 보너스와 최적 유량을 가집니다. 여기에 모두 나열하기에는 조합이 너무 많지만, 상단에 링크된 플래너에는 관련 정보가 모두 있으며 어떤 연료로든 모든 터빈의 전력 출력과 수명을 계산하는 계산기까지 있습니다.

- 소형 터빈은 긴 마그날륨 막대기로 제작됩니다(LV부터 사용 가능).
- 일반 터빈은 긴 티타늄 막대기로 제작됩니다(달에 다녀온 뒤 HV 후반에 사용 가능 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>).
- 대형 터빈은 긴 텅스텐강 막대기로 제작됩니다(텅스텐 처리 라인 이후 IV에서 사용 가능).
- 초대형 터빈은 긴 아메리슘 막대기로 제작됩니다(핵융합 반응로 Mk-II <ItemImage id="gregtech:gt.blockmachines:32020"/>를 건설한 후 ZPM에서 사용 가능).

## 내구도
터빈은 생성된 전력에 비례하여 서서히 내구도를 잃습니다. 터빈의 총 내구도는 재질에 따라 달라지며, 0%에 도달하면 즉시 소멸합니다. 터빈은 입력 버스를 통해 컨트롤러에 자동으로 삽입할 수 있지만, 자동으로 추출할 수는 없습니다.

다음 방정식은 <Color id="GREEN">LPT</Color>의 현재 전력 출력으로부터 터빈의 수명(시간)을 계산합니다. 느슨한 장착 모드는 더 높은 전력 출력으로 인한 수명 감소를 보상하기 위해 내구도를 25% 증가시키며, 터빈은 대형 증기 터빈에서보다 여기서 훨씬 오래 지속됩니다. 터빈은 일반적으로 수백 시간(또는 그 이상)의 수명을 가지므로 자주 교체할 필요가 없습니다.

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(36 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>