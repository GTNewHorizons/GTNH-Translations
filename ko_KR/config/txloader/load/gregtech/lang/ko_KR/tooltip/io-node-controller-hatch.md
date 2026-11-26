기계 유형: {color_machine_type:BEC 해치}
{color_mode:일시정지 제어}
해치가 레드스톤 신호를 받으면 {color_key:{item:gregtech:gt.blockmachines:15757}}의 작동을 일시적으로 정지시킵니다
노드는 즉시 일시정지할 수 있으며, 다음 단계에 진입할 때 일시정지할 수도 있습니다
일시정지된 노드는 응축수를 소비하지 않고 오염물질로 인해 실패하지 않지만, 전력은 계속 소비합니다
또한 새 조합법을 시작할 수 있지만, 아무 진행도 없이 즉시 대기 상태가 됩니다
{hr}
{color_mode:병렬 제어}
조합법을 처리할 때 {color_key:{item:gregtech:gt.blockmachines:15757}}의 최대 병렬 수를 제어합니다
{color_mechanic:가수} 값은 수신한 레드스톤 신호의 세기를 기반으로 합니다
{color_mechanic:지수} 값은 제공된 고스트 회로 번호를 기반으로 합니다
{color_parallel:병렬}{color_formula: = 가수 × 16^지수}
여러 {color_key:{item:gregtech:gt.blockmachines:15759}}를 사용할 수 있으며, 각각의 {color_parallel:병렬} 값은 모두 합산됩니다