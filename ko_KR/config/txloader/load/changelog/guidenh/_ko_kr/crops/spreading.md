---
navigation:
  title: 작물 확산
  parent: crops.md
  icon: cropsnh:cropSticks
categories:
    - crops
author: Skorched
date: 2026-05-21
---

# 작물 확산
> [!NOTE]
> 이 페이지에서는 [작물 기초](basics.md)를 이미 읽었거나 작물과 능력치의 기본 사항을 알고 있다고 가정합니다.
원하는 작물을 얻었다고 가정해 보겠습니다. 작물 하나만으로는 부족할 수 있지만, 밭을 만들기 위해 작물의 능력치를 수백 번이나 다시 맞추는 일은 번거롭습니다! 이럴 때 <Color id="GREEN">작물 확산</Color>을 활용할 수 있습니다.

자, 여러분. 선생님은 잠시 자리를 비웠으니 영상으로 넘어가겠습니다!
<GameScene width="420" height="280" zoom={2.5} interactive={true}>
  <ImportStructure src="../assets/crops/spreading.snbt" />
  <ImportPonder src="../assets/crops/spreading.json" />
</GameScene>

# 설명:
영상을 보고 싶지 않거나 더 자세한 내용이 필요하신 분들을 위해, 교과서식 설명을 준비했습니다.

## 확산
작물을 확산시키려면, 작물이 자랄 수 있는 유효한 흙 블록 위에 작물이 놓여 있어야 하며, 인접한 곳에 교차된 작물 막대(같은 자리에 두 번 설치한 작물 막대)가 있어야 합니다. 작물이 하층 토양을 요구한다면, 새 작물이 자랄 자리에도 해당 조건을 충족하는 블록이 있어야 합니다. 이러한 조건은 NEI의 "작물" 페이지에서 확인할 수 있습니다:
<RecipeFor id="minecraft:log" input="cropsnh:genericSeed" float="left" wrap="square"/>
작물이 인접한 작물 막대 위에서 자랄 수 있다면, 해당 작물은 다른 작물 막대 위로 확산되어 복제됩니다.

새 작물의 능력치는 비료를 주지 않은 경우 (-2:+4), 비료를 준 경우 (+0:+4) 범위에서 결정됩니다. 따라서 관리되는 밭의 비옥한 흙에 작물 하나를 심고 충분히 기다리면, 최대 능력치(31/31/31)의 작물을 반드시 얻을 수 있습니다.
<br clear="all" />
## 잡초
흙에 위드엑스 <ItemImage id="cropsnh:weedEX" />를 사용하지 않았다면, 잡초는 겹쳐진 작물 막대든 아니든 <Color id="RED">***모든***</Color> 작물 막대에서 자라려고 합니다. 잡초는 골칫거리입니다. 잡초가 퍼지면서 작물밭을 뒤덮고 다음과 같은 다른 문제도 일으키기 때문입니다...

## 병충해
이전 구현과 달리, 잡초는 다른 작물을 **파괴하지 않고** 대신 <Color id="RED">병들게</Color> 합니다. 병든 작물은 생산물을 내놓지 못하며, <Color id="GREEN">식물 치료제</Color> <ItemImage id="cropsnh:plantCure" />를 사용해 치료해야 합니다.