대형 열 교환기 32개에 해당합니다.
입력은 {color_hot:용암}, {color_hot:뜨거운 냉각수}, 또는 {color_hot:뜨거운 태양염}입니다.
출력은 {color_cold:파호이호이 용암}, {color_cold:IC2 냉각수}, 또는 {color_cold:차가운 태양염}입니다.
이 과정에서 증류수를 {color_steam:증기} 또는 {color_steam:SH 증기}로 변환합니다.
뜨거운 유체의 입력 속도가 특정 {light_purple:임계값}을 초과하면 {color_steam:SH 증기}를 출력합니다.
증류수가 떨어지면 즉시 폭발합니다.
{hr}
{color_hot:용암} | SH 임계값 {light_purple:{var:lava_threshold} {L}/s} | 최대 입력 {color_hot:{var:lava_max_input} {L}/s} | 최대 출력 {color_steam:{var:lava_max_output} {L}/t SH 증기}
{color_hot:뜨거운 냉각수} | SH 임계값 {light_purple:{var:coolant_threshold} {L}/s} | 최대 입력 {color_hot:{var:coolant_max_input} {L}/s} | 최대 출력 {color_steam:{var:coolant_max_output} {L}/t SH 증기}
{color_hot:뜨거운 태양염} | SH 임계값 {light_purple:{var:salt_threshold} {L}/s} | 최대 입력 {color_hot:{var:salt_max_input} {L}/s} | 최대 출력 {color_steam:{var:salt_max_output} {L}/t SH 증기}
{hr}
컨트롤러의 회로는 증기를 대가로 SH 임계값을 낮춥니다.
{var:min_circuit}개를 초과하는 회로마다 SH 임계값 {light_purple:-{var:threshold_reduction}%} 및 증기 출력 {color_loss:-{var:steam_penalty}%}