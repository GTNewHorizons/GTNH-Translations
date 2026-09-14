---
item_ids:
  - gregtech:gt.blockmachines:15527
navigation:
  title: 대형 가스 터빈
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15527
categories:
    - 구조 개편
author: Skorched
date: 2026-05-27
---

# 대형 가스 터빈

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15527"/>
</GameScene>
<Color id="GREEN">대형 가스 터빈(LGT)</Color>는 EV 티어 멀티블록으로, 가스로부터 전력을 생산합니다. <Color id="GREEN">대형 가스 터빈</Color>은 단일블록 가스 터빈의 직접적인 상위 업그레이드이며, 훨씬 높은 효율로 최대 4A의 전력을 출력합니다. 그러나 기계가 작동하려면 터빈을 컨트롤러 내부에 배치해야 하고, 연료 입력 속도를 신중하게 조절해야 하며, 완전히 예열되려면 최소 50초 동안 작동해야 합니다. 터빈은 네 가지 크기와 여러 재질로 제공되며, 각각 고유한 효율 보너스와 최적 유량(L/t)을 가집니다. 전력은 가스가 오염으로 변환됨에 따라 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수면 폭발합니다. 라포트로닉 슈퍼커패시터 <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 LGT를 자동으로 켜고 꺼서 연료를 절약하십시오.

<Color id="GREEN">LGT</Color>는 XL 터보 가스 터빈으로 대체되며, 이는 16개의 <Color id="GREEN">LGT</Color>만큼 가스를 소비하고 전력을 생산하지만 12개의 터빈만 필요로 합니다. 또한 본격적인 전력 생산을 위한 다중 암페어 및 레이저 에너지 해치를 지원합니다. 터빈 없이 환경을 오염시키지 않고 가스를 산화시켜 전기를 생산하는 고체 산화물 연료 전지도 있습니다. 그러나 작동 중 100 L/s의 산소를 필요로 하고, 일반적으로 100% 효율로 고정되며, 오버플로를 지원하지 않고, XL 변형도 없습니다. 

[GTNH Power Planner](https://docs.google.com/spreadsheets/d/1KDitUw4xMIhlRBaEzPe62n_0hlhH37H9E1voBPCXKN4/edit?gid=589078529#gid=589078529)
<br clear="all"/>

> [!NOTE]
> 구조만 변경되었으며, 멀티블록의 작동 방식은 동일합니다.

## 건설
<Color id="GREEN">LGT</Color>에는 티어별 구성 요소가 없습니다. 정비 해치, 머플러 해치, 입력 해치, 출력 해치는 구조물 뒤쪽 절반의 모든 터빈 케이싱을 대체할 수 있습니다. 다이너모 해치는 구조물의 맨 뒤쪽 중앙 케이싱으로 제한되며 4A를 초과할 수 없습니다. 컨트롤러 바로 앞의 9개 블록은 반드시 공기여야 합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화하거나 건설하십시오.

대형 터빈의 고유 기능은 터빈 하우징으로, 이는 사실상 ULV 입력 버스이며, 내부 터빈이 파손되면 컨트롤러 내부의 터빈을 자동으로 교체하는 예비 터빈을 보관합니다. 완전히 선택 사항이며 UV 티어에서 해금되지만, 가동 시간을 최대화하는 데 도움이 됩니다. 

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15527"/><ItemImage id="gregtech:gt.blockmachines:15527"/>
- 14 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 8-13 <ItemLink id="gregtech:gt.blockcasings4:10"/><ItemImage id="gregtech:gt.blockcasings4:10"/>
- 12 <ItemLink id="gregtech:gt.blockcasings11"/><ItemImage id="gregtech:gt.blockcasings11"/>
- 다이너모 해치 1개(뒤쪽 중앙 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:30"/>
- 정비 해치 1개(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 0개 이상 <ItemLink id="gregtech:gt.blockmachines:31025"/><ItemImage id="gregtech:gt.blockmachines:31025"/>
- 입력 해치 0개 이상(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 출력 해치 0개 이상(뒤쪽 아무 터빈 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">LGT</Color>는 케이싱, 프레임 박스, 해치를 절약하기 위해 각 측면을 벽 공유할 수 있습니다. 그러나 <Color id="GREEN">LGT</Color>들 사이에 연료가 균등하게 분배되지 않으므로 입력 해치를 공유해서는 안 됩니다. 하나가 전부 소비하고 다른 하나는 아무것도 받지 못합니다. 해치 위치에 대한 제한 때문에 어차피 그것을 달성하기는 어렵습니다. 

## 사용법
<Color id="GREEN">LGT</Color>에는 아래에 나열된 두 가지 작동 모드가 있지만, 두 모드 간의 수치화할 수 있는 차이는 상단에 링크된 계획표를 참조하십시오. 전자는 가스 생산량이 적은 초중반 게임에서 더 좋고, 후자는 효율보다 전력 출력이 더 중요한 후반 게임에서 더 좋습니다. 컨트롤러에 스크루드라이버를 사용하여 모드를 전환하십시오.

- 밀착 장착 모드 - 높은 효율, 낮은 최적 유량(전력).
- 느슨한 장착 모드 - 낮은 효율, 높은 최적 유량(전력).

<Color id="GREEN">LGT</Color>의 속도는 작동 중에는 100%까지 선형적으로 증가하고, 비작동 중에는 다시 0%로 감소합니다. 속도는 기계의 전력 출력에 정비례하며, 터빈 크기/재질에 관계없이 최대값에 도달하는 데 50초가 걸립니다. <Color id="GREEN">LGT</Color>가 비활성화되거나, 터빈이 제거되거나, 구조물이 파괴되거나, 연료가 떨어지면 속도가 매우 빠르게 감소합니다. 컨트롤러에 휴대용 스캐너 <ItemImage id="gregtech:gt.metaitem.01:32762"/>를 사용하거나 WAILA의 "efficiency" 값을 확인하여 터빈의 현재 속도를 볼 수 있습니다. 

## 최적 유량
가스가 <Color id="GREEN">LGT</Color>로 들어오는 속도(L/t)는 매우 중요합니다. 가스가 너무 적으면 잠재 전력의 일부만 생산되고, 너무 많으면 막대한 양의 연료가 낭비됩니다. 이상적으로는 가스가 터빈의 최적 유량으로 <Color id="GREEN">LGT</Color>에 들어가며, 이는 크기/재질과 기계의 작동 모드에 따라 크게 달라집니다. NEI에서 확인할 수 있지만, L/t 단위의 최적 유량($$\dot{m}$$)은 다음 방정식으로 계산됩니다. 여기서 $$k$$는 각 재질에 연관된 계수, size는 1=소형에서 4=거대 사이의 상수, EU/L은 가스의 밀도, $$\eta_0$$는 터빈의 기본 효율입니다. 

<Latex formula="\dot{m}^* \text{Tight} = k \times \text{size} \times 50 \div EU/L">
  여기서:
  - $$\dot{m}^* =$$ 최적 유량
  - $$k =$$ 재질 계수
  - size = 터빈 크기(1=소형, 4=거대)
</Latex>
<Latex formula="\dot{m}^* \text{Loose} = k \times \text{size} \times 100 \div EU/L \times 1.05^{20(\eta_0 - 0.8)}">
  여기서:
  - $$\dot{m}^* =$$ 최적 유량
  - $$k =$$ 재질 계수
  - size = 터빈 크기(1=소형, 4=거대)
  - $$\eta_0 =$$ 기본 효율
</Latex>

밀착 장착 모드에서 최적 유량을 계산하는 더 빠르고 쉬운 방법은 NEI에서 확인할 수 있는 최적 가스 EU/t를 가스 밀도로 나눈 뒤, 그 결과를 2로 나누는 것입니다. 일부는 밀도가 매우 낮아 최적 유량이 매우 높으며, 특히 <Color id="GREEN">LGT</Color>가 느슨한 장착 모드일 때 그렇습니다. 플레이어는 증가한 수요를 충족하기 위해 유체 조절기를 업그레이드하거나 두 번째 입력 해치를 추가해야 할 수도 있습니다. 결국에는 사실상 전송 제한이 없고 온도나 열용량을 고려하지 않는 AE2 유체 P2P 터널로 전환해야 합니다. 

## 전력 및 오버플로
<Color id="GREEN">LGT</Color>가 생산하는 전력은 현재 유량($$\dot{m}$$), 최적 유량($$\dot{m}^*$$), 터빈의 효율($$\eta$$)에 따라 달라집니다. 최적 유량을 초과하면 터빈의 오버플로 티어($$T$$)에 따라 수익이 체감하면서 추가 전력이 생성됩니다. 오버플로 티어는 총 세 개뿐이며 전적으로 터빈 재질에 따라 결정됩니다. 오버플로 티어가 높을수록 최대 유량($$\dot{m}_{max}$$)도 증가합니다. NEI를 통해 터빈의 오버플로 티어를, WAILA를 통해 기계의 현재 전력 출력을 확인하십시오.

전력은 구조물 뒤쪽의 4A 다이너모 해치에서 추출됩니다. 기계가 작동 중일 때 다이너모 해치를 부수지 마십시오. 그렇지 않으면 <Color id="GREEN">LGT</Color>가 폭발합니다. 다이너모 버퍼의 최대 EU/t 또는 총 EU를 초과해도 완전히 안전합니다. 연결된 배터리 버퍼나 라포트로닉 슈퍼커패시터(LSC)가 가득 차서 EU가 갈 곳이 없어도 <Color id="GREEN">LGT</Color>는 폭발하지 않습니다. 추가 EU는 단순히 소멸됩니다. 연료 낭비를 피하려면 레드스톤 RS 래치로 <Color id="GREEN">LGT</Color>를 자동으로 켜고 끄는 것을 적극 권장합니다.


<Latex formula="\text{EU/t} (\leq \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^*} \Biggr) \times EU/L \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
</Latex>
<Latex formula="\text{EU/t} (&gt; \dot{m}^*) = \dot{m} \times \Biggl( 1 - \frac{|\dot{m} - \dot{m}^*|}{\dot{m}^* \times (3T-1)} \Biggr) \times EU/L \times \eta">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}^*$$: 최적 유량
  - $$\eta$$: 효율
  - $$T$$: 오버플로 티어
</Latex>

<Latex formula="\dot{m}_{max} = \lfloor \dot{m}^* \rfloor \times (1.5T)">
  - $$\dot{m}$$: 현재 유량
  - $$\dot{m}_{max}$$: 최대 유량
  - $$T$$ 오버플로 티어
</Latex>