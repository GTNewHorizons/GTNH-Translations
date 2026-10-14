작업당 연료를 최대 {red:{var:fuel_percent}}% 사용합니다.
이 값의 {red:10}%는 고정값이며, {red:90}%는 공식 y=1-(1-x)^3을 따릅니다(x는 충전율입니다).
정비 문제 하나당 냉각 효율이 {red:20}% 감소합니다.
{red:{var:power}} EU/t를 사용하며, 헬륨 가스가 부족하면 최대 {red:{var:power_penalty}}배까지 증가합니다.
헬륨 가스가 열교환기의 효율을 최대 용량에서 {red:100}%까지 선형으로 높입니다.
원자로는 작업당 헬륨을 {red:{var:helium_lost}}% 잃습니다.
작업을 시작하려면 헬륨이 최소 {red:{var:min_helium}}% 필요합니다.
작업 1회에 걸리는 시간은 원자로 충전율에 따라 달라집니다.
최소 {red:{var:min_time}}초에서 최대 {red:{var:max_time}}초까지 걸립니다.
냉각수, 물 또는 둘 다를 공급하면 레시피 시간이 다음 비율만큼 단축됩니다.
총 레시피 시간 기준 초당 {red:{var:coolant_speedup}}%/{red:{var:water_speedup}}%/{red:{var:total_speedup}}% 단축됩니다.
최대 추가 속도 보너스에 필요한 유체의 양은 TRISO 구체의 수에 비례합니다.
구체당 틱마다 냉각수 {red:{var:coolant_per_ball}}와 증류수 {red:{var:water_per_ball}}가 필요합니다.