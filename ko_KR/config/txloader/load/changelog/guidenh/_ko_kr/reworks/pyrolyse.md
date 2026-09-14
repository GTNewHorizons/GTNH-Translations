---
item_ids:
  - gregtech:gt.blockmachines:15546
navigation:
  title: 열분해 오븐
  parent: reworks.md
  icon: gregtech:gt.blockmachines:15546
categories:
    - 구조 리워크
author: Skorched
date: 2026-05-27
---

# 열분해 오븐
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15546"/>
</GameScene>
<Color id="GREEN">열분해 오븐(PO)</Color>은 MV 티어 멀티블록으로, 원목을 목탄으로 태우며 하나의 액체 부산물(예: 석탄 가스, 목재 가스, 목초액, 목타르, 목탄 부산물)을 선택할 수 있습니다. <Color id="GREEN">열분해 오븐</Color>은 전기로 작동하고 충분한 전력이 있으면 오버클럭할 수 있기 때문에 기본 코크스 오븐 <ItemImage id="gregtech:gt.blockmachines:236"/>의 직접적인 업그레이드입니다. 또한 가열 코일의 티어에 따라 선형적으로 증가하는 속도 보너스를 얻습니다. 액체 부산물은 에틸렌, 벤젠, 톨루엔과 같은 유기 화합물을 생산하는 데 유용합니다. 초기에는 더 느리지만, 열분해 오븐은 더 잘 확장되고 액체 부산물이 진행에 중요하기 때문에 일반적으로 고급 코크스 오븐 <ItemImage id="Railcraft:machine.alpha:12"/>보다 권장됩니다. 둘 모두 EV에서 산업용 코크스 오븐 <ItemImage id="gregtech:gt.blockmachines:15543"/>로 대체됩니다. 
<br clear="all"/>

> [!NOTE]
> 이 멀티블록의 유일한 변경점은 구조 자체에 있습니다

## 건설
<Color id="GREEN">열분해 오븐</Color>에는 티어가 있는 구성 요소가 하나 있습니다. 가열 코일은 기계의 열용량을 결정하며, 구조가 형성되려면 모두 같은 티어여야 합니다. 에너지 해치, 유지보수 해치, 출력 버스/해치는 구조의 하단 층에 있는 어떤 열분해 오븐 케이싱이든 대체할 수 있습니다. 소음기 해치와 입력 버스/해치는 구조의 상단 층에 있는 어떤 열분해 오븐 케이싱이든 대체할 수 있습니다. <Color id="RED">멀티 앰프 및 레이저 에너지 해치</Color>는 지원되지 않지만, EBF와 거의 모든 GregTech 멀티블록과 마찬가지로 오버클러킹을 위해 여러 개의 일반 에너지 해치를 사용할 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용해 하위 채널 "coil"로 구조를 시각화/건설하여 가열 코일의 티어를 지정할 수 있습니다. 

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15546"/><ItemImage id="gregtech:gt.blockmachines:15546"/>
- 60-68 <ItemLink id="gregtech:gt.blockcasingsNH:2"/><ItemImage id="gregtech:gt.blockcasingsNH:2"/>
- 12 가열 코일(티어별) <ItemImage id="gregtech:gt.blockcasings5:11"/>
- 8 <ItemLink id="gregtech:gt.blockcasings2:13"/><ItemImage id="gregtech:gt.blockcasings2:13"/>
- 4 <ItemLink id="gregtech:gt.blockcasings3:14"/><ItemImage id="gregtech:gt.blockcasings3:14"/>
- 2 <ItemLink id="gregtech:gt.blockframes:305"/><ItemImage id="gregtech:gt.blockframes:305"/>
- 1+ 에너지 해치 (하단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40" />
- 1 유지보수 해치 (하단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90" />
- 1 소음기 해치 (상단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:91" />
- 0+ 입력 버스 (상단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70" />
- 0+ 입력 해치 (상단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:50" />
- 0+ 출력 버스 (하단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80" />
- 0+ 출력 해치 (하단 층의 아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:60" />

### 벽 공유
<Color id="GREEN">열분해 오븐</Color>은 케이싱, 프레임 박스, 버스/해치를 절약하기 위해 각 면을 벽 공유할 수 있습니다. 위 이미지에서 볼 수 있듯이 가열 코일의 최대 절반까지 포함됩니다. 가열 코일이 구조에서 가장 비싼 부분이므로 이 방법을 적극 권장합니다. 

## 사용법
<Color id="GREEN">열분해 오븐</Color>은 가열 코일의 티어에 따라 선형적으로 증가하는 속도 보너스를 얻습니다. 더 구체적으로, 처리 속도는 백동 코일에서 50%로 시작하며 그보다 높은 가열 코일 티어마다 50%씩 증가합니다. 이는 다음 표에서 볼 수 있습니다. 기본 처리 시간이 16초이고 오버클럭이 없는 레시피의 소요 시간을 참고로 제공합니다. 속도 보너스는 EU/t가 동일하게 유지되므로 열분해 오븐의 전력 소비를 증가시키지 않습니다. 오히려 더 짧은 시간 동안 작동하므로 실제로 총 EU 소비량을 감소시킵니다. 

| 가열 코일 | 속도 | 예시 | 총 EU |
| --------------- | --------------- | --------------- | --------------- |
| 백동 | 50% | 32.00s | 200% |
| 칸탈 | 100% | 16.00s | 100% |
| 니크롬 | 150% | 10.67s | 66.7% |
| TPV 합금 | 200% | 8.00s | 50.0% |
| HSS-G | 250% | 6.40s | 40.0% |
| HSS-S | 300% | 5.33s | 33.3% |
| 나콰다 | 350% | 4.57s | 28.6% |
| 나콰다 합금 | 400% | 4.00s | 25.0% |
| 트리늄 | 450% | 3.56s | 22.2% |
| 일렉트럼 플럭스 | 500% | 3.20s | 20.0% |
| 각성한 드라코늄 | 550% | 2.91s | 18.2% |
| 인피니티 | 600% | 2.67s | 16.7% |
| 하이포젠 | 650% | 2.46s | 15.4% |
| 이터널 | 700% | 2.29s | 14.3% |

<Color id="GREEN">열분해 오븐</Color>은 주로 원목을 목탄으로 태우는 데 사용되며, 입력 버스나 컨트롤러의 프로그래밍된 회로로 결정되는 하나의 액체 부산물을 선택할 수 있습니다. 가장 흔한 선택은 목탄 부산물인데, 이는 증류탑 <ItemImage id="gregtech:gt.blockmachines:1126"/>에서 디메틸벤젠, 목재 가스, 목초액, 목타르로 분해되기 때문입니다. 또 다른 흔한 선택은 니트로벤젠을 더 직접적이고 효율적으로 만들기 위한 목타르입니다. 또한 16개의 원목당 1,000L의 질소 가스를 사용해 기계의 처리 속도를 두 배로 높이는 옵션이 있으며, 이 역시 입력 버스나 컨트롤러의 프로그래밍된 회로로 결정됩니다.