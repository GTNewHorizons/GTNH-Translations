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
> 이 페이지는 이미 [작물 기초](basics.md)를 읽었거나, 작물과 그 능력치의 기초에 익숙하다고 가정합니다.
원하는 작물을 얻었다고 가정해 보겠습니다. 작물 하나로는 충분하지 않을 가능성이 크지만, 밭을 만들기 위해 작물의 능력치를 수백 번 다시 설정하는 것은 지루한 일입니다! 이때 <Color id="GREEN">작물 확산</Color>을 활용할 수 있습니다.

자, 여러분, 선생님이 자리를 비우셨으니 영상을 재생하겠습니다!
<GameScene width="420" height="280" zoom={2.5} interactive={true}>
  <ImportStructure src="../assets/crops/spreading.snbt" />
  <ImportPonder src="../assets/crops/spreading.json" />
</GameScene>

# 설명:
영상을 보고 싶지 않거나 더 자세한 설명이 필요한 분들을 위해, 교과서식 설명을 준비했습니다:

## 확산
작물을 확산시키려면, 인접한 곳에 교차된 작물 막대(같은 위치에 두 번 설치됨)가 있어야 하며, 그 아래에 대상 작물에 유효한 토양 블록이 있어야 합니다. 작물에 하위 토양 요구 사항이 있다면, 새 작물 대상 블록에도 이것이 있어야 합니다. 이러한 요구 사항은 NEI의 "작물" 페이지에서 확인할 수 있습니다:
<RecipeFor id="minecraft:log" input="cropsnh:genericSeed" float="left" wrap="square"/>
작물이 이 인접한 작물 막대에서 자랄 수 있다면, 다른 작물 막대 세트로 자신을 복제하며 확산을 시도합니다.

새 작물의 능력치는 비료를 주지 않은 경우 (-2:+4) 범위이고, 비료를 준 경우 (+0:+4) 범위입니다. 따라서 비료를 준 흙으로 관리되는 밭에 단일 작물로 시작하면, 충분한 시간이 주어졌을 때 최대 능력치(31/31/31) 작물을 얻는 것이 보장됩니다.
<br clear="all" />
## 잡초
토양에 제초제 <ItemImage id="cropsnh:weedEX" />를 처리하지 않았다면, 잡초는 겹쳐 놓았든 아니든 <Color id="RED">***어떠한***</Color> 작물 막대에서도 항상 자라려고 시도합니다. 잡초는 골칫거리입니다. 이들은 다시 퍼져 나가 작물 밭을 집어삼키고 다음과 같은 다른 문제를 일으키기 때문입니다...

## 질병
예전 구현과 달리, 잡초는 다른 작물을 **파괴하지 않으며**, 대신 <Color id="RED">병들게</Color> 만듭니다. 병든 작물은 산출물을 제공할 수 없으며, <Color id="GREEN">식물 치료제</Color> <ItemImage id="cropsnh:plantCure" />를 사용해 치료해야 합니다.