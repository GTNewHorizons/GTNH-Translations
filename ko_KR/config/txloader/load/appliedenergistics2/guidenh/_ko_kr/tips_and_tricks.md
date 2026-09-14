---
navigation:
  title: 팁과 요령
  position: 20
---

# 팁과 요령

여러 가지 소소한 권장 사항입니다.

* Optifine을 제거하십시오.
* 확대 및 주석 숨기기/표시 버튼이 있는 가이드북 장면은 회전하거나 확대할 수 있습니다.
* 네트워크를 나무 형태로 유지하고 루프를 피하십시오.
* 네트워크를 통해 [채널](ae2_mechanics/channels.md)이 라우팅되는 방식을 잘 이해하고 있지 않다면, 완전한 블록 형태의 [장치](ae2_mechanics/devices.md)는 8개 이하의 그룹으로 유지하십시오.
* 목재 한 종류를 선택하여 모든 [패턴](items_blocks/patterns.md)에 사용하십시오. 대체를 활성화하면 작동하는 경우도 있지만, 어디서나 같은 목재 종류를 사용하면 번거로움을 크게 줄일 수 있습니다.
* [에너지 셀](items_blocks/energy_cells.md)을 추가하여 네트워크가 전력 급증을 감당할 수 있도록 하십시오.
* <ItemLink id="appliedenergistics2:tile.BlockCondenser" />에서는 물을 사용할 수 있습니다.
* 네트워크를 깔끔하게 유지하는 가장 좋은 방법은 검이나 갑옷 같은 무작위 몹 전리품을 넣지 않는 것입니다. 인챈트와 내구도의 각 고유한 조합은 또 하나의 [종류](ae2_mechanics/bytes_and_types.md)가 됩니다.
* [처리 패턴](items_blocks/patterns.md)의 결과를 반환할 때는 <ItemLink id="appliedenergistics2:item.ItemMultiPart:240" />, <ItemLink id="appliedenergistics2:tile.BlockInterface" /> 또는 인터페이스 반환 슬롯 등을 통해 "아이템이 시스템에 들어오는" 이벤트가 발생해야 합니다. <ItemLink id="appliedenergistics2:item.ItemMultiPart:220" />가 설치된 상자에 결과를 파이프로 바로 넣을 수는 없습니다.
* <ItemLink id="appliedenergistics2:tile.BlockInterface" />는 완성된 레시피 배치를 인접한 인벤토리로 밀어 넣습니다. 이를 사용하면 기계가 일부만 완성된 배치를 받지 않도록 할 수 있지만, 재료를 여러 장소로 보내야 하는 경우도 있습니다. 여러 인터페이스를 사용하거나 <ItemLink id="appliedenergistics2:tile.BlockInterface" />를 [파이프 서브넷](tricks_example/pipe_subnet.md)으로 사용하면 이를 구현할 수 있습니다.