---
item_ids:
  - gregtech:gt.blockmachines:15568
navigation:
  title: 드론 센터
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15568
categories:
    - 구조물 리워크
author: Skorched
date: 2026-05-23
---

# 드론 센터

<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15568"/>
</GameScene>
<Color id="GREEN">드론 센터</Color>는 주변 기계의 자동 정비 수리, 전력 제어 및 모니터링을 위한 IV 티어 멀티블록입니다. <Color id="RED">드론</Color>은 입력 버스를 통해 삽입되며, <Color id="BLUE">드론 다운링크 모듈</Color> <ItemImage id="gregtech:gt.blockmachines:9401" />이 설치된 범위 내 모든 기계를 정비합니다(정비 해치를 대체합니다). <Color id="GREEN">센터</Color>는 전력을 소비하지 않으며 정비 수리는 무료지만, 매초 드론이 충돌하여 소멸할 약간의 확률이 있습니다. 총 네 티어의 드론이 있으며, 티어가 높을수록 범위가 넓어지고 수명이 길어집니다. T4 드론은 차원을 넘어 작업할 수 있는 능력도 해금합니다. 안타깝게도 드론은 실제로 날아다니거나 드론 센터를 떠나지 않습니다. 
<br clear="all"/>

> [!NOTE]
> 다음은 멀티블록의 주요 변경 사항입니다:
> - 새로운 동기화 로직: 기계 제어가 이제 시야와 관계없이 실제로 작동합니다.
> - 사용자 지정 기계 그룹화: 더 나은 관리를 위해 기계를 사용자 지정 그룹으로 구성합니다.
> - 개선된 스위치 버튼: 스위치 버튼이 이제 그룹별로 모든 기계를 켜고 끕니다.
> - 차원 간 연결: 새로운 T4 드론을 사용하여 차원 연결과 무한 범위를 활성화합니다.
> - 연결 키: T4 드론이 다른 플레이어의 시추 플랜트에 연결되는 것을 방지합니다!
> - 생산 기록기: 공장이 실제로 무엇을 하는지 추적합니다!


## 건설
<Color id="GREEN">드론 센터</Color>에는 티어 구성 요소나 정비 해치, 에너지 해치, 소음기 해치가 없습니다. 필요한 것은 드론을 위한 입력 버스뿐입니다. 헴프크리트는 어떤 색상이든 가능하며 기계 작동에 영향을 주지 않습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /> <ItemImage id="structurelib:item.structurelib.constructableTrigger" />를 사용하여 구조물을 시각화/건설하십시오.

<Color id="GREEN">드론 센터</Color>의 고유 기능은 <Color id="BLUE">드론 다운링크 모듈</Color>로, 다른 기계의 정비 해치를 대체하여 자동 정비 수리, 전력 제어 및 모니터링을 위해 네트워크에 연결합니다. 드론 다운링크 모듈은 활성 드론 센터를 찾을 때까지 10초마다 검색하므로, 렉 스파이크를 피하려면 활성 연결 없이 너무 많이 두지 마십시오. 드론 다운링크 모듈을 우클릭하여 호스트 기계의 이름을 바꾸면 더 쉽게 식별할 수 있습니다. 

### 필요 항목:
- 1 <ItemLink id="gregtech:gt.blockmachines:15568" /> <ItemImage id="gregtech:gt.blockmachines:15568" />
- 61 <ItemLink id="gregtech:gt.blockcasings2:13" /> <ItemImage id="gregtech:gt.blockcasings2:13" />
- 47 <ItemLink id="gregtech:gt.blockframes:305" /> <ItemImage id="gregtech:gt.blockframes:305" />
- 29 <ItemLink id="chisel:hempcrete" /> (모든 색상) <ItemImage id="chisel:hempcrete" /> 
- 28 <ItemLink id="gregtech:gt.blockframes:32" /> <ItemImage id="gregtech:gt.blockframes:32" />
- 20-26 <ItemLink id="gregtech:gt.blockcasings2" /> <ItemImage id="gregtech:gt.blockcasings2" />
- 1+ 입력 버스 (모든 강철 기계 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />

### 벽 공유
기계들은 문제없이 동일한 <Color id="BLUE">드론 다운링크 모듈</Color>을 벽 공유할 수 있습니다. 컨트롤러는 전력 제어 및 모니터링에서 별도로 나타납니다. 

## 사용법
<Color id="RED">드론</Color>은 구조물의 입력 버스를 통해 삽입됩니다. 기계가 시작되면 컨트롤러는 사용 가능한 가장 높은 티어의 드론을 소비하여 <Color id="BLUE">드론 다운링크 모듈</Color>이 설치된 범위 내 모든 기계를 정비합니다. 활성 드론은 매초 무작위 확률에 따라 "충돌"할 때까지 작동합니다. 그렇게 되면 활성 드론은 소멸되고, 사용 가능한 다음으로 높은 티어의 드론이 역할을 대신합니다. 컨트롤러의 WAILA에서 현재 드론의 티어를 확인할 수 있으며, 필요하면 컨트롤러를 부수어 드론을 회수할 수 있습니다. 

### 드론
사용 가능한 드론은 네 티어입니다. 모두 기능적으로 동일하지만, 다음 표에서 볼 수 있듯이 높은 티어일수록 범위가 넓고 평균 수명이 깁니다. T3 및 T4 드론은 심지어 파괴되지 않지만, 자동 테이핑 정비 해치보다 훨씬 늦게 해금됩니다. 차원 간을 활성화하려면 다운링크 모듈이 <Color id="GREEN">드론 센터</Color>와 동일한 키를 가져야 합니다. 

| 티어 | 범위 | 충돌 확률 | 평균 수명 | 차원 간 |
| --------------- | --------------- | --------------- | --------------- | --------------- |
| 1 | 128 | 매초 1 / 28,800 | 8시간 | \u274c |
| 2 | 512 | 매초 1 / 172,800 | 48시간 | \u274c|
| 3 | 4096 | 없음 | 무한 | \u274c|
| 4 | 4096 | 없음 | 무한 | \u2705 |

범위는 <Color id="BLUE">드론 다운링크 모듈</Color>과 <Color id="GREEN">드론 센터</Color> 컨트롤러 사이의 <Color id="RED">유클리드 거리</Color>로 결정됩니다. 좌표로부터 거리를 계산하려면 다음 방정식을 사용하십시오:

<Latex formula="\text{Distance} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}" />

### 전력 제어
<Color id="BLUE">드론 다운링크 모듈</Color>이 설치된 모든 기계는 컨트롤러의 GUI 내 기계 목록에 나타납니다. 기계는 이름을 바꾸고, 월드에서 강조 표시하고, 원격으로 활성화/비활성화할 수 있습니다. 또한 컨트롤러 GUI에는 거리와 관계없이 같은 차원의 모든 기계를 활성화/비활성화하는 버튼이 있습니다. 전력 제어는 정전 후 모든 것을 다시 활성화하거나 <ItemLink id="gregtech:gt.blockmachines:13106" />를 업그레이드/이동할 준비를 할 때 매우 유용합니다.