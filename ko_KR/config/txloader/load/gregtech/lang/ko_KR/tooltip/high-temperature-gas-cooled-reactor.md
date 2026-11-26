작업당 최대 {color_amount:{var:fuel_percent}%}의 {color_name:Fuel}을 사용합니다.
작업을 시작하려면 최소 {color_amount:{var:min_helium}%}의 {color_key:Helium}이(가) 필요합니다.
{color_key:Helium}은(는) 최대 용량에서 열교환기 효율을 {color_amount:100%}까지 선형적으로 증가시킵니다.
원자로는 작업당 저장된 {color_key:Helium}의 {color_amount:{var:helium_lost}%}를 잃습니다.
{color_eu_usage:{var:power} {EU/t}}를 사용하며, {color_key:Helium}이(가) 부족할 때 최대 {color_amount:{var:power_penalty}x}까지 증가합니다.
{hr}
작업 시간은 원자로 충전율에 따라 달라집니다.
최소 {color_amount:{var:min_time}s}에서 최대 {color_amount:{var:max_time}s}까지입니다.
이 값의 {color_amount:10%}는 고정값이며, {color_amount:90%}는 공식 {aqua:y = 1 - (1 - x)^3}을 따릅니다({white:x}는 충전율 %입니다).
정비 문제 하나당 효율이 {color_amount:20%} 감소합니다.
{hr}
{color_key:Coolant}, {color_key:Water} 또는 둘 다를 공급하면 조합법을 다음 비율만큼 가속합니다.
총 조합법 시간 기준 초당 {color_amount:{var:coolant_speedup}%} / {color_amount:{var:water_speedup}%} / {color_amount:{var:total_speedup}%} 단축됩니다.
최대 보너스에 필요한 유체의 양은 {color_key:TRISO Balls}의 수에 비례합니다.
구체당 틱당 {color_amount:{var:coolant_per_ball}} {color_key:Coolant} 및 {color_amount:{var:water_per_ball}} {color_key:Distilled Water}입니다.