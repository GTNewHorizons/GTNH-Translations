아이템을 {gold:{item:gregtech:gt.blockmachines:15756}} 안팎으로 순간이동시킵니다.
레시피 로직은 다른 모든 다중 블록 구조물과 동일합니다.
레시피를 시작할 때 응축물이 반드시 있어야 하는 것은 아닙니다.
{gold:{item:gregtech:gt.blockmachines:15481}}을 사용하여 {gold:{item:gregtech:gt.blockmachines:15756}}에 연결합니다.
{dark_gray:{hr}}
레시피의 각 아이템 슬롯에는 해당 나나이트 티어가 있습니다.
순간이동 노드가 아이템 슬롯의 처리를 진행하려면 해당 슬롯과 같거나 더 높은 티어의 나나이트를 받아야 합니다.
초과 나나이트는 레시피 제작 속도를 선형적으로 높입니다.
요청된 티어보다 높은 티어의 나나이트를 공급하면 진행 속도가 {italic:2^(provided tier - requested tier)}배 느려집니다.
이 다중 블록 구조물은 일시 정지되거나, 진행이 멈추거나, 속도가 느려져도 EU/t가 일정하게 유지됩니다.
병렬로 제작하는 레시피가 하나 늘어날 때마다 소비 EU/t가 선형적으로 증가합니다.
이 다중 블록 구조물은 오버클럭되지 않습니다.
{dark_gray:{hr}}
정확한 레시피 소요 시간을 보장하도록 매개변수에서 최소 및 최대 병렬 처리 수를 설정할 수 있습니다.
자동화 속도가 느릴 때는 {gold:{lang:GT5U.gui.text.bec-speed-divisor}} 매개변수를 사용하여 레시피 속도를 강제로 낮출 수 있습니다.
{dark_gray:{hr}}
{gold:{item:gregtech:gt.blockmachines:15758}}을 사용하면 순간이동 노드가 요청하는 나나이트를 감지할 수 있습니다.
{gold:{item:gregtech:gt.blockmachines:15759}}을 사용하면 순간이동 노드를 일시적으로 정지할 수 있습니다.