---
navigation:
  parent: ../tricks_example_index.md
  title: 충전기 자동화
  icon: appliedenergistics2:tile.BlockCharger
---

# 충전기 자동화

이 구성은 <ItemLink id="appliedenergistics2:tile.BlockInterface" />를 사용하므로 [자동 조합](../ae2_mechanics/autocrafting.md) 시스템과 함께 작동하도록 설계되었습니다. 독립형 <ItemLink id="appliedenergistics2:tile.BlockCharger" />에는 호퍼, 상자 또는 다른 아이템 파이프를 사용하십시오.

<ItemLink id="appliedenergistics2:tile.BlockInterface" />가 충전기에 재료를 보냅니다. [파이프 서브넷](pipe_subnet.md) 또는 다른 아이템 파이프가 충전된 결과물을 인터페이스로 반환합니다.

<GameScene>
  <ImportStructure src="../assets/structures/charger_automation.snbt" />
  <BlockAnnotation pos="1 0 0">
  (1) ME 인터페이스: 관련 패턴이 포함된 기본 설정입니다. 전력도 공급합니다.

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="충전기 패턴" />
  </BlockAnnotation>
  <BoxAnnotation min="0.25 1 0.25" max="0.75 1.3 0.75">
  (2) 임포트 버스: 기본 설정입니다.
  </BoxAnnotation>
  <BoxAnnotation min="1.15 1 0.15" max="1.85 1.25 0.85">
  (3) 스토리지 버스: 기본 설정입니다.
  </BoxAnnotation>
</GameScene>

## 설정

* <ItemLink id="appliedenergistics2:tile.BlockInterface" /> (1)는 기본 설정이며, 관련 <ItemLink id="appliedenergistics2:item.ItemEncodedUltimatePattern" />을 포함하고 있습니다. 또한 [케이블](../items_blocks/cables.md)처럼 <ItemLink id="appliedenergistics2:tile.BlockCharger" />에 전력을 공급합니다.

  <FloatingImage src="../assets/images/charger_pattern.png" displayWidth="150" title="충전기 패턴" />

* <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" /> (2)는 기본 설정입니다.
* <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" /> (3)는 기본 설정입니다.

## 작동 방식

1. <ItemLink id="appliedenergistics2:tile.BlockInterface" />가 <ItemLink id="appliedenergistics2:tile.BlockCharger" />에 재료를 보냅니다.
2. 충전기가 아이템을 충전합니다.
3. 초록색 서브넷의 <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />가 결과물을 꺼내 [네트워크 저장소](../ae2_mechanics/import_export_storage.md)에 저장하려고 합니다.
4. 초록색 서브넷에서 유일한 저장소는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />이며, 결과물을 ME 인터페이스로 돌려보낸 다음 메인 네트워크로 보냅니다.