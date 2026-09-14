---
item_ids:
  - gregtech:gt.blockmachines:31088
navigation:
  title: 대형 중화 엔진
  parent: multis.md
  icon: gregtech:gt.blockmachines:31088
categories:
    - 새로운 멀티블록
author: Skorched
date: 2026-05-25
---

# 대형 중화 엔진
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:31088" />
</GameScene>
<Color id="GREEN">대형 중화 엔진 (LNE)</Color>은 더 높은 전압 티어 요구 사항을 위한 EV 티어 멀티블록 산 발전기입니다. <Color id="GREEN">LNE</Color>는 최대 <Color id="BLUE">500%</Color>의 효율을 제공하고, 1A 이상의 전력을 출력할 수 있으며, 연료 소비율을 설정할 수 있기 때문에 단일블록 산 발전기에서 직접 업그레이드한 것입니다. <Color color="#55ffff">염기</Color>를 사용하여 기계의 효율을 향상시킬 수 있습니다. 전력은 뒤쪽의 다이나모 해치를 통해 추출되며, <Color id="GREEN">멀티앰프 및 레이저 에너지 해치</Color>가 지원됩니다. <Color id="GREEN">LNE</Color>는 <Color id="RED">독성 잔류물</Color>이라는 자체 위험 시스템을 가지고 있습니다. 이것이 컨트롤러의 용량을 초과하면, 멀티블록은 <Color id="RED">폭발합니다!</Color> <ItemLink id="gregtech:gt.blockmachines:13106"/> <ItemImage id="gregtech:gt.blockmachines:13106"/>에 연결된 RS 래치로 <Color id="GREEN">LNE</Color>를 자동으로 토글하여 연료를 절약하십시오.
<br clear="all"/>

## 건설:
<Color id="GREEN">LNE</Color>에는 하나의 티어 구성 요소가 있습니다. 사용된 "메인 케이싱"이 기계의 티어를 결정하며, 이는 다시 기계의 기본 감쇠와 용량을 결정합니다. 입력 해치, 입력 버스, 다이나모, 그리고 독성 잔류물 센서 해치(추후 설명)는 모든 "메인" 케이싱을 대체할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/> <ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설하십시오.
| 티어 | 케이싱 |
| -------------- | --------------- |
| 1 | 강화된 무생물 기계 케이싱 <ItemImage id="gregtech:gt.blockcasings12:5"/> |
| 2 | 정밀 고정 기계 케이싱 <ItemImage id="gregtech:gt.blockcasings12:6"/> |
| 3 | 궁극의 정적 기계 케이싱 <ItemImage id="gregtech:gt.blockcasings12:7"/> |

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:31088"/> <ItemImage id="gregtech:gt.blockmachines:31088"/>
- 34 <ItemLink id="gregtech:gt.blockframes:473"/><ItemImage id="gregtech:gt.blockframes:473"/>
- 30-46 티어별 "메인" 케이싱 <ItemImage id="gregtech:gt.blockcasings12:5"/>
- 15 <ItemLink id="gregtech:gt.blockcasings8:1"/><ItemImage id="gregtech:gt.blockcasings8:1"/>
- 1+ 다이나모 해치 (모든 티어 케이싱) <ItemImage id="gregtech:gt.blockmachines:15230"/>
- 1+ 입력 해치 (모든 티어 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ <ItemLink id="gregtech:gt.blockmachines:3019"/> (모든 티어 케이싱)<ItemImage id="gregtech:gt.blockmachines:3019"/>
- 0+ 입력 버스 (모든 티어 케이싱) <ItemImage id="gregtech:gt.blockmachines:70"/>

### 벽 공유:
<Color id="GREEN">LNE</Color>는 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다.

## 사용법:
<Color id="GREEN">LNE</Color>는 산으로부터 전력을 생성합니다. 다양한 종류의 산이 사용 가능하며, 사용 가능한 많은 산의 EU 값이 조정되었으므로, 기존에 즐겨 쓰던 산들을 다시 확인해 볼 가치가 충분합니다. 이와 함께, 완전히 새로운 <ItemLink id="gregtech:gt.metaitem.01:2177"/><ItemImage id="gregtech:gt.metaitem.01:2177"/>를 포함하여 몇 가지 새로운 산 라인이 추가되었습니다.

### 염기 부스팅
<Color id="GREEN">LNE</Color>는 아래 표에 따라 입력 버스에 염기를 넣어 산 연료의 효율을 높일 수 있습니다. 이 염기들은 입력 버스에 들어온 순서대로 하나씩 소모됩니다.
| 염기 | 효율 | 사용 속도 |
| --------------- | --------------- | --------------- |
| 수산화 나트륨 | 150% | 분당 60 |
| 수산화 칼륨 | 190% | 분당 24 |
| 수산화 세슘 | 250% | 분당 6 |
| 수산화 프랑슘 | 500% | 분당 5 |

### 감쇠 부스팅
<Color id="GREEN">LNE</Color>는 입력 버스에 <Color id="RED">로봇 팔</Color>을 넣어 감쇠 부스트를 증가시킬 수 있습니다. 감쇠 부스트는 <Color id="GREEN">IV</Color> 이하인 경우 $$1.2^{\text{Arm Tier}}$$로, <Color color="#ff55ff">LuV</Color> 이상인 경우 $$1.4^{\text{Arm Tier}}$$로 계산됩니다. 최대 16개까지 여러 로봇 팔을 삽입하여 해당 감쇠 부스트에 $$\sqrt{\text{Arm Count}}$$를 곱할 수 있습니다. 매분마다 <Color id="GREEN">LNE</Color>는 __하나의__ 로봇 팔을 소멸시킬 확률이 있으며, 이는 다음으로 계산됩니다.
<Latex formula="\text{Void Chance} = \frac{\text{Arm Count}}{45 \times (1+\text{Arm Tier})}"/>

### 독성 잔류물
<Color id="GREEN">LNE</Color>는 산을 연소하여 <Color id="RED">독성 잔류물</Color>을 생성합니다. 잔류물의 양이 기계의 용량을 초과하면, 기계가 폭발합니다. 매 틱마다, 독성 잔류물은 다음 방정식에 따라 증가__하고__ 감소합니다:
<Latex formula="\text{+Residue}=\text{Residue Rate} \times \text{Fuel Consumption(L)} \times \text{Random}(0.5:15)">
  - <Latex formula="\text{Residue Rate} = 0.05 \times \text{Base Fuel Value (EU/L)}^{0.8}"/>
</Latex>
<Latex formula="\text{-Residue}=\text{Base Decay} \times \text{Decay Boost} \times (\text{Toxic Residue})^{0.08}"/>
잔류물은 <Color id="GREEN">LNE</Color>가 비활성화되면 10배 더 느리게 감쇠하므로, 방정식에 항상 직접 의존해서는 안 됩니다.

## 독성 잔류물 센서 해치 <ItemImage id="gregtech:gt.blockmachines:3019"/>
<Color id="GREEN">독성 잔류물 센서 해치</Color>는 모든 티어 케이싱을 대체할 수 있으며, 위험 시스템과 관련하여 발전기의 자동화를 더 쉽게 할 수 있게 해줍니다. 발전기의 <Color id="RED">독성 잔류물</Color>을 읽으며, 특정 임계값에 따라 레드스톤 입력을 허용하는 설정을 구성할 수 있는 GUI가 있습니다.