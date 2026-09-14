---
item_ids:
  - gregtech:gt.blockmachines:15752
navigation:
  title: L.A.T.E.X.
  parent: multis.md
  icon: gregtech:gt.blockmachines:15752
categories:
    - 신규 멀티블록
author: Skorched
date: 2026-05-25
---

# L.A.T.E.X.
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:15752" />
</GameScene>
<Color id="GREEN">적층 도포 및 열 외장 전문가(LATEX)</Color>는 이름이 길기로 유명한, 케이블 코팅용 HV 티어 멀티블록입니다. <Color id="GREEN">LATEX</Color>는 케이블 코팅용 단일블록 조립기의 직접적인 업그레이드입니다. <Color id="GREEN">200%</Color> 속도로 작동하고, 일반적으로 필요한 EU/t의 <Color id="RED">85%</Color>만 사용하며, 전압 티어당 <Color id="BLUE">8</Color>개의 병렬을 제공하기 때문입니다. 또한 아이템 파이프 케이싱의 티어에 따라 6.25%의 고무 할인이 추가되며, 컨트롤러 내부에 탄성 특이점을 삽입하여 병렬 수를 두 배로 늘리고, 고무 할인 25%를 추가로 얻고, 멀티앰프 및 레이저 에너지 해치를 사용할 수 있는 능력을 해금할 수 있는 특별한 기회도 있습니다. 
<br clear="all"/>

## 건설:
LATEX에는 티어별 구성 요소가 하나 있습니다. 아이템 파이프 케이싱이 기계의 전체 고무 할인을 결정합니다. 버스/해치는 구조물의 어느 위치에서든 어떤 케이싱이든 대체할 수 있습니다. 유리는 구조물이 형성되려면 티어별이어야 하지만, 기계 작동에는 아무런 영향을 주지 않습니다. 멀티앰프 및 레이저 에너지 해치는 컨트롤러에 탄성 특이점이 있지 않으면 지원되지 않습니다. 다만 오버클럭을 위해 여러 개의 일반 에너지 해치를 둘 수 있습니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger" /><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 하위 채널 "item_pipe"와 "glass"로 구조물을 시각화/건설함으로써 해당 구성 요소의 티어를 지정하십시오. 

### 요구 사항:
- 1 <ItemLink id="gregtech:gt.blockmachines:15752" /><ItemImage id="gregtech:gt.blockmachines:15752"/>
- 14-36 <ItemLink id="gregtech:gt.blockcasings8"/> <ItemImage id="gregtech:gt.blockcasings8"/>
- 32 티어별 유리(아무 종류) <ItemImage id="bartworks:BW_GlasBlocks:15"/>
- 16 <ItemLink id="gregtech:gt.blockframes:649"/><ItemImage id="gregtech:gt.blockframes:649"/>
- 6 아이템 파이프 케이싱(티어별)<ItemImage id="gregtech:gt.blockcasings11:5"/>
- 1+ 에너지 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:40"/>
- 1 유지보수 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:90"/>
- 0+ 입력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:70"/>
- 0+ 입력 해치(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:50"/>
- 0+ 출력 버스(아무 케이싱) <ItemImage id="gregtech:gt.blockmachines:80"/>
### 월쉐어링:
<Color id="GREEN">LATEX들</Color>은 각 면을 월쉐어하여 케이싱, 유리, 프레임 박스, 버스/해치를 절약할 수 있습니다. 어떤 레시피도 1A를 초과하는 전력을 사용하지 않으므로 <u>__하나__</u>의 에너지 해치를 <u>__두__</u> 대의 기계 사이에서 공유할 수 있습니다. 

## 사용법:
<Color id="GREEN">LATEX</Color>는 케이블 코팅용 단일블록 조립기의 직접적인 업그레이드입니다. 다음 표에서 볼 수 있듯이 200% 속도로 작동하고, 일반적으로 필요한 EU/t의 85%만 사용하며, 전압 티어당 8개의 병렬을 제공하기 때문입니다. 아이템 파이프 케이싱의 티어에 따라 6.25%의 고무 폴리머 할인도 추가됩니다. 

### 병렬:
|  | LV | MV | HV | EV | IV | LuV | ZPM | UV | UHV | UEV | UIV | UMV | UXV | MAX | MAX+ |
| --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |--------------- |
|  | 8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 | 104 | 112 | 120 |
| ES | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240 |

> [!NOTE]
> 여기서 "ES"는 컨트롤러에 탄성 특이점이 있다는 뜻입니다

| 아이템 파이프 케이싱   | 고무 할인    |
|--------------- | --------------- |
| 주석   | 6.25%   |
| 황동   | 12.50%   |
| 일렉트럼   | 18.75%   |
| 백금   | 25.00%   |
| 오스뮴   | 31.25%   |
| 퀀티움   | 37.50%   |
| 플럭스드 일렉트럼   | 43.75%   |
| 블랙 플루토늄   | 50.00%   |


## 탄성 특이점
<Color id="GREEN">LATEX</Color> 컨트롤러에 탄성 특이점을 삽입하면 병렬 수가 두 배로 늘어나고, 고무 할인 25%를 추가로 얻으며, 멀티앰프 및 레이저 에너지 해치를 사용할 수 있는 능력이 해금됩니다. 즉, 최대 240개의 병렬과 75%의 고무 폴리머 할인입니다. 탄성 특이점 자체는 다이어 제작대에서 제작되지만, 이를 구성하는 다섯 특이점은 모두 뉴트로니움 압축기 또는 유사안정 블랙홀 격납 필드에서 제작됩니다. 즉, 이 업그레이드는 UV 전까지 설치할 수 없고, 기계 간에 특이점을 공유할 수 없습니다. 각 특이점의 비용은 아래와 같습니다(각 113,771,520L).

- 고무 특이점 - 초고밀도 고무 시트 12,345장 또는 개별 고무 시트 790,080장.
- 실리콘 고무 특이점 - 초고밀도 실리콘 고무 시트 12,345장 또는 개별 실리콘 고무 시트 790,080장.
- 폴리염화비닐 특이점 - 초고밀도 폴리염화비닐 시트 12,345장 또는 개별 폴리염화비닐 시트 790,080장.
- 스티렌 부타디엔 고무 특이점 - 초고밀도 스티렌 부타디엔 고무 시트 12,345장 또는 개별 스티렌 부타디엔 고무 시트 790,080장.
- 폴리페닐렌 설파이드 특이점 - 초고밀도 폴리페닐렌 설파이드 시트 12,345장 또는 개별 폴리페닐렌 설파이드 시트 790,080장.