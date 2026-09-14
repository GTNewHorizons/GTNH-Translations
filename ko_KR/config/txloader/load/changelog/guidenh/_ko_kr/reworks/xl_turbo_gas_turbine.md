---
item_ids:
  - gregtech:gt.blockmachines:15522
navigation:
  title: XL 터보 가스 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15522
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# XL 터보 가스 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15522"/>
</GameScene>
<Color id="GREEN">XL 터보 가스 터빈 (XLGT)</Color>은 가스로부터 막대한 전력을 생산하는 LuV 티어 멀티블록입니다. <Color id="GREEN">XLGT</Color>는 대형 가스 터빈의 직접적인 업그레이드입니다. 단 12개의 터빈으로 처리량이 16배이고, 멀티앰프 및 레이저 다이너모 해치를 지원하며, 기계가 작동 중일 때 다이너모 해치가 파손되어도 폭발하지 않기 때문입니다. 하지만 기계가 작동하려면 터빈이 모두 동일해야 하고, 최적 유량을 초과할 때 더 가혹한 패널티가 있으며, 벤젠은 블랙리스트에 등록되어 있고, 기계가 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">XLGT</Color>를 자동으로 토글하여 연료를 절약하십시오. 

[GTNH 전력 플래너](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 이 멀티블록은 구조만 변경되었으며, 작동 방식은 동일합니다

## 건설
<Color id="GREEN">XLGT</Color>에는 티어 부품이 없습니다. 유리는 아무 티어나 가능하며 기계 작동에 영향을 주지 않습니다. 솔레노이드 코일은 반드시 MV여야 하며, 역시 기계 작동에 영향을 주지 않습니다. 버스/해치는 구조물 어디에서나 모든 터빈 케이싱을 대체할 수 있습니다. <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>가 본격적인 전력 생성을 위해 지원되며, 여러 개를 설치할 수 있습니다. 입력 버스 또는 컨트롤러의 GUI를 통해 터빈을 삽입하십시오. 유리의 티어를 지정하는 하위 채널 "glass"와 함께 구조를 시각화/건설하려면 <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15522"/><ItemImage id="gregtech:gt.blockmachines:15522"/>
- 340-345 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1:3"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1:3"/>
- 104 티어 유리(아무 티어) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 80 <ItemLink id="gregtech:gt.blockframes:306"/><ItemImage id="gregtech:gt.blockframes:306"/>
- 76 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 20 <ItemLink id="gregtech:gt.blockcasings.cyclotron_coils"/><ItemImage id="gregtech:gt.blockcasings.cyclotron_coils"/>
- 16 <ItemLink id="miscutils:gtplusplus.blockspecialcasings.1"/><ItemImage id="miscutils:gtplusplus.blockspecialcasings.1"/>
- 7 <ItemLink id="gregtech:gt.blockcasings2:3"/><ItemImage id="gregtech:gt.blockcasings2:3"/>
- 1+ 다이너모 해치(모든 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 1 정비 해치(모든 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 4 머플러 해치(모든 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 1+ 입력 버스(모든 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 1+ 입력 해치(모든 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />

### 벽 공유
<Color id="GREEN">XLGT들</Color>은 각 면을 벽 공유하여 케이싱, 프레임 상자, 유리, 버스/해치를 절약할 수 있습니다. 하지만 입력 해치는 공유하지 마십시오. 연료가 <Color id="GREEN">XLGT들</Color> 사이에 균등하게 분배되지 않아 하나가 전부를 소비하고 다른 하나는 아무것도 받지 못하기 때문입니다. 

## 사용법
가스가 <Color id="GREEN">XLGT</Color>로 들어가는 속도(L/t)는 매우 중요합니다. 가스가 너무 적으면 잠재 전력의 일부만 생성되고, 너무 많으면 막대한 양의 연료가 낭비됩니다. 이상적으로는 가스가 터빈의 최적 유량으로 <Color id="GREEN">XLGT</Color>에 들어가야 하며, 이 유량은 크기/재질과 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 확인할 수 있지만, L/t 단위의 최적 유량($$\dot{m}^*$$)은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재질과 관련된 승수이고, size는 1=소형에서 4=초대형 사이의 상수이며, $$\eta_0$$는 터빈의 기본 효율입니다. 이 값들은 대형 가스 터빈의 최적 유량의 정확히 16배라는 점에 유의하십시오.

<Latex formula="\dot{m}^* (\text{Tight}) = k \times \text{size} \times 800 \div EU/L">
  여기서:
  - $$\dot{m}^*$$: 최적 연료 유량
  - $$k$$: 재질 승수
  - size: 터빈 크기에 따른 상수(1=소형, 4=초대형)
</Latex>
<Latex formula="\dot{m}^* (\text{Loose}) = k \times \text{size} \times 1,600 \div EU/L \times 1.05^{20(\eta_0 - 0.8)}">
  여기서:
  - $$\dot{m}^*$$: 최적 연료 유량
  - $$k$$: 재질 승수
  - size: 터빈 크기에 따른 상수(1=소형, 4=초대형)
  - $$\eta_0$$: 기본 효율
</Latex>

타이트 피팅 모드에서 최적 유량을 계산하는 더 빠르고 쉬운 방법은 NEI에서 확인할 수 있는 최적 가스 EU/t를 아래 표에 나열된 가스의 밀도로 나눈 다음, 그 결과에 16을 곱하는 것입니다. 일부는 밀도가 매우 낮아 최적 유량이 매우 높습니다. 특히 <Color id="GREEN">XLGT</Color>가 루즈 모드일 때 그렇습니다. 플레이어는 증가한 수요를 충족하기 위해 유체 레귤레이터를 업그레이드하거나 두 번째 입력 해치를 추가해야 할 수 있습니다. 결국에는 사실상 전송 제한이 없고 온도나 열용량을 고려하지 않는 AE2 유체 P2P 터널로 전환해야 합니다. 

> [!IMPORTANT]
> 벤젠은 <Color id="GREEN">XLGT</Color>에서 블랙리스트에 등록되어 있습니다

## 전력
<Color id="GREEN">XLGT</Color>가 생성하는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$)에 따라 달라집니다. 최적 유량을 초과하면 효율이 떨어질 뿐만 아니라 생성되는 총 전력량도 감소합니다. 오버플로 티어는 기계 작동에 영향을 주지 않습니다. 컨트롤러를 바라본 상태에서 WAILA를 통해, 또는 산업 정보 패널을 통해 기계의 현재 전력 출력을 확인할 수 있습니다.

전력은 구조물 어디에나 있는 레이저 또는 멀티앰프 다이너모 해치에서 추출됩니다. 다이너모의 버퍼에 있는 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC)가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">XLGT</Color>는 폭발하지 않습니다. 추가 EU는 단순히 소멸됩니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">XLGT</Color>를 자동으로 토글하는 것을 적극 권장합니다.

<Latex formula="EU/t = \dot{m} \times \Biggl( 1 - \frac{| \dot{m} - \dot{m}^* |}{\dot{m}^*} \Biggr) \times EU/L \times \eta">
  여기서:
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 터빈 효율
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times 1.25">
  여기서:
  - $$\dot{m}_{max}$$: 최대 유량
  - $$\dot{m}^*$$: 최적 유량
</Latex>

# 터빈
12개의 터빈은 기계가 작동하려면 모두 정확히 동일해야 합니다. 터빈은 네 가지 크기와 다양한 재질로 제공되며, 각각 고유한 효율 보너스와 최적 유량을 가집니다. 모든 조합을 여기에 나열하기에는 너무 많지만, 상단에 링크된 플래너에는 모든 관련 정보와 어떤 연료를 사용하든 모든 터빈의 전력 출력과 수명을 계산할 수 있는 계산기까지 있습니다.

- 소형 터빈은 긴 마그날륨 막대로 제작됩니다(LV부터 사용 가능)
- 일반 터빈은 긴 티타늄 막대로 제작됩니다(달에 다녀온 후 HV 말기에 사용 가능 <ItemImage id="gtneioreplugin:blockDimensionDisplay_Mo"/>)
- 대형 터빈은 긴 텅스텐강 막대로 제작됩니다(텅스텐 처리 라인 이후 IV에서 사용 가능)
- 초대형 터빈은 긴 아메리슘 막대로 제작됩니다(퓨전 리액터 Mk-II를 건설한 후 ZPM에서 사용 가능 <ItemImage id="gregtech:gt.blockmachines:32020"/>)

## 내구도
터빈은 생성된 전력에 비례하여 서서히 내구도를 잃습니다. 터빈의 총 내구도는 재질에 따라 달라지며, 0%에 도달하면 즉시 소멸합니다. 터빈은 입력 버스를 통해 컨트롤러에 자동으로 삽입할 수 있지만, 자동으로 추출할 수는 없습니다.

다음 방정식은 <Color id="GREEN">XLGT</Color>의 현재 전력 출력으로부터 터빈의 수명(시간)을 계산합니다. 루즈 피팅 모드는 더 높은 전력 출력으로 인한 수명 감소를 보상하기 위해 내구도 25% 증가를 제공하며, 터빈은 대형 증기 터빈보다 여기서 훨씬 오래 지속된다는 점에 유의하십시오. 터빈은 일반적으로 수백 시간(또는 그 이상)의 수명을 가지므로 자주 교체할 필요가 없습니다. 

<Latex formula="\text{Lifespan } (h) = \frac{50\times \text{Durability}}{36 \times \text{min}(0.04 \times EU/t,(0.2 \times EU/t)^{0.6})}"/>

- 루즈 피팅 모드에서는 수명 결과에 1.25를 곱하십시오.