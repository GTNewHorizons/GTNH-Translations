---
item_ids:
  - gregtech:gt.blockmachines:15559
navigation:
  title: 행성 가스 흡입기
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15559
categories:
    - 구조물 개편
author: Skorched
date: 2026-05-27
---

# 행성 가스 흡입기
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15559"/>
</GameScene>
<Color id="GREEN">행성 가스 흡입기(PGS)</Color>는 목성, 토성, 천왕성, 해왕성의 가스 거성에서 무한한 양의 가스를 추출하기 위한 IV 티어 멀티블록입니다. <Color id="GREEN">PGS</Color>는 유체 시추기 <ItemImage id="gregtech:gt.blockmachines:149"/>와 유사하지만, 행성 표면 위 높은 곳의 우주 정거장에서 작동한다는 차이가 있습니다. 각 가스 거성에는 네 가지 서로 다른 가스가 있지만, 한 번에 하나만 추출할 수 있습니다. 입력 버스의 프로그래밍된 회로 값을 조정하여 <ItemImage id="gregtech:gt.blockmachines:149"/>의 깊이를 변경하고, 따라서 어떤 가스를 추출할지 결정합니다. 가열 코일 및/또는 에너지 해치를 업그레이드하여 기계의 추출 속도(L/s)를 증가시킵니다. 

<br clear="all"/>

> [!NOTE]
> 다음 변경 사항이 멀티블록에 적용되었습니다(구조물 제외):
> 코일 티어: 더 높은 티어의 코일은 티어당 +10% 속도 증가를 제공합니다(합연산)
> 기본 속도 두 배: 기본 처리 속도가 이전 구조물에 비해 두 배로 증가했습니다
> WAILA 업그레이드: 이제 컨트롤러에 마우스를 올리면 현재 속도 보너스와 코일 티어가 표시됩니다

## 건설
<Color id="GREEN">PGS</Color>에는 하나의 티어 구성 요소가 있습니다. 가열 코일이 기계의 속도 보너스를 결정합니다. 버스/해치는 구조물 어디에서든 사이펀 케이싱을 대체할 수 있지만, 에너지 해치를 포함하여 각각 정확히 하나씩 있어야 합니다. 멀티앰프 및 레이저 에너지 해치는 지원되지 않습니다. 입력 버스에 있는 채굴 파이프는 컨트롤러에 의해 소모되거나 월드에 설치되지 않으므로, <Color id="GREEN">PGS</Color>는 아래의 가스 거성과 직접 시야를 확보할 필요가 없습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "coil"로 구조물을 시각화/건설해 가열 코일의 티어를 지정하십시오. 

### 필요:
- 1 <ItemLink id="gregtech:gt.blockmachines:15559"/><ItemImage id="gregtech:gt.blockmachines:15559"/>
- 184 <ItemLink id="gtnhintergalactic:gassiphoncasing"/><ItemImage id="gtnhintergalactic:gassiphoncasing"/>
- 93 <ItemLink id="gregtech:gt.blockframes:316"/><ItemImage id="gregtech:gt.blockframes:316"/>
- 12 가열 코일(티어별) <ItemLink id="gregtech:gt.blockcasings5:13"/><ItemImage id="gregtech:gt.blockcasings5:13"/>
- 6 <ItemLink id="bartworks:bw.werkstoffblockscasingadvanced.01:88"/><ItemImage id="bartworks:bw.werkstoffblockscasingadvanced.01:88"/>
- 1 에너지 해치(케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치(케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치(케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스(케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 출력 해치(케이싱 아무 곳) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
PGS는 케이싱, 가열 코일, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 어떤 레시피도 1A 이상의 전력을 사용하지 않으므로, <u>__하나__</u>의 에너지 해치를 <u>__둘__</u> 또는 심지어 <u>__넷__</u>의 기계 간에 공유할 수 있습니다.

## 우주 정거장
<Color id="GREEN">PGS</Color>는 가스 거성을 공전하는 우주 정거장 위에 건설해야 합니다. <Color id="BLUE">우주 정거장</Color>은 로켓을 우주로 발사하고, 행성을 클릭한 뒤, 화면 오른쪽에 "여기에 우주 정거장을 생성할 수 있습니다!"라고 표시된 곳의 CREATE 버튼을 눌러 건설합니다. 각 가스 거성의 우주 정거장 비용은 아래에 나열되어 있습니다. 플레이어는 버튼을 누르려면 필요한 재료를 인벤토리(배낭이나 압축 상자가 아님)에 가지고 있어야 합니다. 그러면 우주 정거장은 달과 유사하게 은하 지도에서 행성 주위를 도는 위성으로 나타납니다.

- 목성 - EV 기계 외장 1개, EV 회로 4개, 유리판 6개, 장식용 니켈 블록 231개
- 토성 - LuV 기계 외장 1개, LuV 회로 4개, 유리판 6개, 장식용 미스릴 블록 231개
- 천왕성 - LuV 기계 외장 1개, LuV 회로 4개, 유리판 6개, 장식용 텅스텐 블록 231개
- 해왕성 - ZPM 기계 외장 1개, ZPM 회로 4개, 유리판 6개, 장식용 아다만타이트 블록 231개

NEI나 은하 지도에는 표시되지 않지만, 각 가스 거성에는 연관된 티어가 있습니다. 플레이어는 어떤 로켓으로든 우주 정거장을 생성할 수 있음에도 불구하고, 로켓의 티어가 너무 낮으면 가스 거성의 우주 정거장을 보거나 이동할 수 없습니다. 

<Color id="BLUE">우주 정거장</Color>은 처음에는 매우 작고 중력 효과가 매우 어색합니다. 그러나 플레이어는 원하는 만큼 크게 만들 수 있으며, 우주로 날아가는 것을 막기 위해 몇몇 벽/지붕을 지을 수 있습니다. 우주 정거장에는 산소도 없으므로 여분의 산소 탱크 몇 개를 가져오거나, 더 영구적인 해결책을 위해 산소 수집기와 산소 압축기를 가져오십시오. 우주 정거장을 떠나려면 발사대에서 로켓을 발사하십시오. 연료를 가득 채운 로켓은 왕복 비행에 충분한 연료를 가지고 있지만, 만일을 대비해 연료 로더와 여분의 로켓 연료를 가져가는 것도 나쁘지 않습니다. 

## 사용법
<Color id="GREEN">PGS</Color>는 목성, 토성, 천왕성, 해왕성의 가스 거성에서 무한한 양의 가스를 추출합니다. 그러나 한 번에 하나의 가스만 추출할 수 있고, 각 가스에는 최소 전압 티어가 있으며, 오버클럭은 에너지 해치 자체를 업그레이드해야만 할 수 있습니다. 입력 버스의 프로그래밍된 회로 값을 조정하여 <Color id="GREEN">PGS</Color>의 깊이를 변경하고, 따라서 가스 거성에서 어떤 가스를 추출할지 결정합니다.

깊이는 기계에 들어가는 입력도 결정합니다. 입력 버스에 필요한 채굴 파이프 수는 $$\text{Depth} \times 64$$이며, 기본 EU/t는 $$\text{Depth} \times 4^{T+2}$$입니다. 여기서 $$T$$는 가스 거성의 티어입니다. 예를 들어, 목성에서 헬륨을 펌프질하려면 채굴 파이프 128개가 필요하고 기본 전력 소비는 2,048 EU/t 또는 1A EV입니다. 오버클럭은 전압에 관계없이 항상 암페어 수를 동일하게 유지합니다.

가스가 추출되는 속도(L/s)는 다음 표에서 볼 수 있듯이 가스 거성, 가스 유형, 사용 가능한 전력에 따라 달라집니다. <Color id="GREEN">PGS</Color>는 200% 속도로 작동하며 가열 코일 티어당 +10% 속도 보너스를 얻지만, 후자는 나열된 속도에 포함되지 않습니다. 

| 가열 코일   | 속도    |
|--------------- | --------------- |
| 백동   | 210%   |
| 칸탈   | 220%   |
| 니크롬   | 230%   |
| TPV 합금   | 240%   |
| HSS-G   | 250%   |
| HSS-S   | 260%    |
| 나콰다   | 270%   |
| 나콰다 합금   | 280%   |
| 트리늄   | 290%   |
| 플럭스드 일렉트럼   | 300%   |
| 각성한 드라코늄   | 310%   |
| 인피니티   | 320%   |
| 하이포젠   | 330%   |
| 이터널   | 340%   |