{gold:{item:gregtech:gt.blockmachines:15756}} 안팎으로 아이템을 순간이동시킵니다.
레시피 작동 방식은 다른 모든 다중 블록과 같습니다.
레시피를 시작할 때 응축물이 없어도 됩니다.
{gold:{item:gregtech:gt.blockmachines:15481}}을 사용해 {gold:{item:gregtech:gt.blockmachines:15756}}에 연결하십시오.
{dark_gray:{hr}}
레시피의 각 아이템 슬롯에는 해당 나노머신 티어가 있습니다.
순간이동 노드가 아이템 슬롯을 처리하려면 같은 티어 또는 더 높은 티어의 나노머신을 받아야 합니다.
나노머신이 남으면 레시피 제작 속도가 선형적으로 증가합니다.
요구된 것보다 높은 티어의 나노머신을 제공하면 진행 속도가 {italic:2^(provided tier - requested tier)}배 느려집니다.
이 다중 블록은 일시 정지, 정체 또는 속도 저하 상태에서도 {EU/t}가 일정하게 유지됩니다.
병렬로 제작하는 레시피 수가 늘어날수록 소비되는 {EU/t}가 선형적으로 증가합니다.
이 다중 블록은 오버클럭되지 않습니다.
{dark_gray:{hr}}
정확한 레시피 처리 시간을 보장하도록 매개변수에서 최소 및 최대 병렬 수를 설정할 수 있습니다.
느린 자동화 속도에 맞춰 {gold:{lang:GT5U.gui.text.bec-speed-divisor}} 매개변수로 레시피 속도를 강제로 늦출 수 있습니다.
{dark_gray:{hr}}
{gold:{item:gregtech:gt.blockmachines:15758}}을 사용해 순간이동 노드가 요청한 나노머신을 감지할 수 있습니다.
{gold:{item:gregtech:gt.blockmachines:15759}}을 사용해 순간이동 노드를 일시적으로 정지할 수 있습니다.