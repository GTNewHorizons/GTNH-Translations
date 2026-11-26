HIP 유닛은 작동 중에 가열됩니다
최대 열에 도달하면 {color_danger:{bold:과열!}} 상태가 됩니다
이는 기계를 완전히 식혀야만 해결됩니다
{color_danger:과열} 상태에서는 레시피가 크게 느려집니다
{hr}
일부 레시피는 HIP를 {bold:필요로 합니다}
이러한 레시피 중 하나가 시작될 때 기계가 {color_danger:과열} 상태라면, 해당 레시피는 무효화됩니다!
현재 열은 {color_name:열 센서 해치}를 사용하여 확인하십시오
{hr}
더 고급 코일은 더 나은 열 제어를 가능하게 합니다 - 유닛이 과열되기까지 더 오래 걸립니다
유닛은 작동 중 매초 {color_hot:가열}되며, 가열량은 {color_hot:({var:heat}% x {var:coil_factor} ^ (코일 티어 - 1))}입니다
유닛은 작동하지 않는 동안 매초 {color_cold:냉각}되며, 냉각량은 기본 {color_cold:{var:base_cooling}%}입니다
냉각 속도는 작동한 이후 매초마다 추가로 {color_cold:{var:cooling_increase}%}씩 증가합니다
{hr}
동일 전압의 단일블록 기계 속도는 {color_speed:{var:speed}%}입니다 ({color_danger:과열 시 {var:overheated_speed}%})
일반적으로 필요한 {EU/t}의 {color_eu_usage:{var:eu}%}를 사용합니다 ({color_danger:과열 시 {var:overheated_eu}%})
{color_parallel:{var:parallels}}개의 병렬 처리가 {color_tier:전압} 티어당 적용됩니다 ({color_danger:과열 시 {var:overheated_parallels}})