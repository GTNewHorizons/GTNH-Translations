---
item_ids:
  - gregtech:gt.blockmachines:236
  - gregtech:gt.blockmachines:237
  - gregtech:gt.blockcasings12:0
navigation:
  title: 코크스 오븐
  parent: reworks.md
  icon: gregtech:gt.blockmachines:236
categories:
    - 구조물 리워크
author: Skorched
date: 2026-05-27
---

# 코크스 오븐
<GameScene wrap="square" align="right">
  <ImportStructureLib controller="gregtech:gt.blockmachines:236"/>
</GameScene>
<Color id="GREEN">코크스 오븐</Color>은 통나무를 숯으로 태우고 석탄을 코크스로 정제하는 돌 티어 멀티블록입니다. 이 과정은 통나무/석탄 하나당 90초가 걸리며 부산물로 크레오소트 오일을 생산합니다. 크레오소트 오일은 화로, 레일크래프트 보일러, 대형 보일러 등에서 연료로 사용할 수 있습니다. 또한 횃불을 매우 효율적으로 제작하는 데 사용할 수 있으며, 증류기, 양조기, 증류탑에서 윤활유를 만들 수도 있습니다. 코크스 오븐은 MV에서 열분해 오븐 <ItemImage id="gregtech:gt.blockmachines:15543"/>과 고급 코크스 오븐 <ItemImage id="Railcraft:machine.alpha:12"/>으로 대체됩니다. 

<br clear="all"/>

> [!NOTE]
> 멀티블록에 다음과 같은 변경 사항이 적용되었습니다(구조물 제외):
> 새로운 자동화: 코크스 오븐은 이제 자동화를 위해 특수한 코크스 오븐 해치를 사용합니다
> 벽 공유: 이제 GT 멀티블록이므로 벽을 공유할 수 있습니다!

## 건설
<Color id="GREEN">코크스 오븐</Color>은 코크스 오븐 벽돌로 둘러싸인 속이 빈 정육면체이며 한쪽 면에 컨트롤러가 있습니다. 컨트롤러의 GUI를 통해 <Color id="GREEN">코크스 오븐</Color>과 수동으로 상호작용하거나, <Color id="RED">코크스 오븐 해치</Color> <ItemImage id="gregtech:gt.blockmachines:237"/>를 사용하여 입력 삽입과 출력 추출을 자동화할 수 있습니다. <Color id="RED">코크스 오븐 해치</Color>는 구조물 어디에 있는 벽돌이든 대체할 수 있으며, 입력, 출력(아이템), 출력(유체)의 세 가지 모드 중 하나로 작동합니다. 드라이버로 해치를 우클릭하면 모드가 전환되고, 렌치로 우클릭하면 해치가 회전합니다. 코크스 오븐 해치는 자체 내부 인벤토리가 없으므로 파괴해도 아이템을 떨어뜨리거나 유체를 삭제하지 않습니다. 그런 동작은 컨트롤러만 수행합니다. <ItemLink id="structurelib:item.structurelib.constructableTrigger"/><ItemImage id="structurelib:item.structurelib.constructableTrigger"/>를 사용하여 구조물을 시각화/건설할 수 있습니다.

해치 세 개가 달린 <Color id="GREEN">코크스 오븐</Color>을 건설하려면 코크스 오븐 벽돌(주괴) 114개, 철 54개, 청동 18개가 필요합니다. 벽돌은 모래 190개, 점토 114개, 나무 틀 38회 사용으로 만들어집니다. 하지만 초반에 추가 코크스 오븐을 건설하기 위해 이보다 훨씬 많은 양을 모아 두는 것을 강력히 권장합니다.

### 필요 재료:
- 1 <ItemLink id="gregtech:gt.blockmachines:236"/><ItemImage id="gregtech:gt.blockmachines:236"/>
- 0-25 <ItemLink id="gregtech:gt.blockmachines:237"/><ItemImage id="gregtech:gt.blockmachines:237"/>
- 0+ <ItemLink id="gregtech:gt.blockcasings12"/><ItemImage id="gregtech:gt.blockcasings12"/>

### 벽 공유
<FloatingImage src="../assets/reworks/coke_oven_wallshare.png" displayWidth="128" align="right">
  <ImageAnnotation>
    네 개가 벽을 공유한 코크스 오븐의 예시
  </ImageAnnotation>
</FloatingImage>
<Color id="GREEN">코크스 오븐</Color>은 각 면의 벽을 공유하여 코크스 오븐 벽돌과 코크스 오븐 해치를 절약할 수 있습니다. 이는 상당한 양의 자원을 절약하고 필요한 해치 수를 줄여 주므로 강력히 권장합니다. 예를 들어 오른쪽 이미지는 구조물 중앙에 있는 동일한 코크스 오븐 해치를 모두 사용하는 네 개의 개별 코크스 오븐을 보여 줍니다. 

## 사용법
<Color id="GREEN">코크스 오븐</Color>은 주로 통나무를 숯으로 태우는 데 사용되지만, 다음 표에서 볼 수 있듯 몇 가지 다른 용도도 있습니다. 분재 나무는 초반에 상당한 양의 통나무를 모으는 훌륭한 방법입니다. 바닐라 묘목을 작물 막대기에 우클릭하여 분재를 만들 수 있습니다. 가문비나무와 정글나무가 수확할 때마다 더 많이 생산되므로 가장 좋습니다. 또 다른 방법은 Tinker's Construct의 벌목 도끼를 제작하여 신성한 참나무나 한 번에 수천 개의 통나무를 떨어뜨리는 거대한 나무를 반복해서 수확하는 것입니다. 신성한 참나무는 신성한 샘 바이옴에서 자연적으로 생성되며, 그 묘목은 퀘스트 북에서 퀘스트 보상으로 얻을 수 있습니다.

<Color id="GREEN">코크스 오븐</Color>은 석탄을 코크스로 정제하는 데에도 사용됩니다. 차이점은 코크스는 연소 시간이 두 배이고 벽돌 용광로 <ItemImage id="gregtech:gt.blockmachines:140"/>에서 철을 강철로 33% 더 빠르게 제련할 수 있다는 것입니다. 선인장 코크스와 설탕 코크스는 매우 유사한 재생 가능한 대안이지만 에너지 밀도는 훨씬 낮습니다. 사용 가능한 모든 레시피의 요약은 다음 표를 참조하십시오. NEI에서도 확인할 수 있습니다. 

| 시간 | 입력 (연소 시간) | 출력 (연소 시간) | 부산물 (연소 시간) |
| --------------- | --------------- | --------------- | --------------- |
| 90초 | 통나무 1개 (300) | 숯 1개 (1,600) | 크레오소트 오일 250L (1,600) |
| 90초 | 석탄 1개 (1,600) | 코크스 1개 (3,200) | 크레오소트 오일 500L (3,200) |
| 810초 | 석탄 블록 (16,000) | 코크스 블록 1개 (32,000) | 크레오소트 오일 4,500L (28,800) |
| 25초 | 선인장 1개 (50) | 선인장 숯 1개 (400) | 크레오소트 오일 30L (192) |
| 25초 | 선인장 숯 1개 (400) | 선인장 코크스 1개 (800) | 크레오소트 오일 30L (192) |
| 25초 | 사탕수수 1개 (50) | 설탕 숯 1개 (400) | 크레오소트 오일 30L (192) |
| 25초 | 설탕 숯 1개 (400) | 설탕 코크스 1개 (800) | 크레오소트 오일 30L (192) |


## 크레오소트 오일
<Color id="GREEN">크레오소트 오일</Color>은 거의 모든 코크스 오븐 레시피의 부산물입니다. 양동이, 유체 셀, 소성 탱크, 슈퍼 탱크로 크레오소트 오일을 수동으로 추출하거나, 코크스 오븐 해치에 연결된 유체 파이프로 자동으로 추출할 수 있습니다. 크레오소트 오일은 레일크래프트 탱크, 슈퍼 탱크 또는 다른 어떤 유체 탱크에든 저장할 수 있습니다. 크레오소트 오일은 바닐라 화로, 레일크래프트 보일러, 대형 보일러를 비롯한 여러 곳에서 연료로 사용할 수 있습니다. 또한 횃불을 매우 효율적으로 제작하는 데 사용할 수 있으며, 증류기, 양조기, 증류탑에서 윤활유를 만들 수도 있습니다.

코크스 오븐은 크레오소트 오일이나 숯/코크스를 넣을 공간이 없으면 자동으로 처리를 중단합니다. 따라서 계속 작동시키려면 수시로 비워 주어야 합니다. 이는 수동으로도 자동으로도 할 수 있습니다. 후자에 대한 안내는 다음 항목을 참조하십시오. 컨트롤러를 부수고 다시 설치하면 크레오소트 오일을 즉시 삭제할 수도 있습니다. 

# 자동화
코크스 오븐은 다음 영상에서 볼 수 있듯 코크스 오븐 해치로 완전히 자동화할 수 있습니다. 코크스 오븐 해치는 인접한 인벤토리에서 자동으로 끌어올 수는 없지만 자동으로 밀어낼 수는 있으므로, 실제로 필요한 것은 호퍼나 컨베이어 모듈뿐입니다. 후자를 사용하는 경우 컨베이어 모듈을 IMPORT로 설정하십시오. 인벤토리 자체가 아니라 아이템 파이프에 부착되어 있을 가능성이 크기 때문입니다. 

<GameScene width="420" height="280" zoom={3} interactive={true}>
  <ImportStructure src="../assets/reworks/coke_oven.snbt" />
  <ImportPonder src="../assets/reworks/coke_oven.json"/>
</GameScene>