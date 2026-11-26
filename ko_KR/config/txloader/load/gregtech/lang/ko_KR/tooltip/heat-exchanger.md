뜨거운 유체: {color_hot:{fluid:lava}}, {color_hot:{fluid:ic2hotcoolant}}, {color_hot:{fluid:molten.solarsalthot}}
냉각 결과: {color_cold:{fluid:ic2pahoehoelava}}, {color_cold:{fluid:ic2coolant}}, {color_cold:{fluid:molten.solarsaltcold}}
{color_name:증류수}를 {color_steam:증기}로 변환합니다.
뜨거운 유체 입력이 {color_note:SH 임계값}에 도달하면 대신 {color_steam:과열 증기}를 절반만 생성합니다.
{color_danger:증류수 없이 {var:explode_seconds}초가 지나면 폭발합니다}
{hr}
{color_hot:{fluid:lava}}: SH 임계값 {color_hot:{var:lava_threshold} {L}/s}, 최대 입력 {color_hot:{var:lava_max_input} {L}/s}, 최대 출력 {color_steam:{var:lava_max_output} {L}/t의 SH 증기}
{color_hot:{fluid:ic2hotcoolant}}: SH 임계값 {color_hot:{var:coolant_threshold} {L}/s}, 최대 입력 {color_hot:{var:coolant_max_input} {L}/s}, 최대 출력 {color_steam:{var:coolant_max_output} {L}/t의 SH 증기}
{color_hot:{fluid:molten.solarsalthot}}: SH 임계값 {color_hot:{var:salt_threshold} {L}/s}, 최대 입력 {color_hot:{var:salt_max_input} {L}/s}, 최대 출력 {color_steam:{var:salt_max_output} {L}/t의 SH 증기}
{hr}
컨트롤러에 있는 {color_name:프로그래밍된 회로}는 {var:min_circuit}보다 높은 값마다 SH 임계값을 {color_amount:{var:threshold_reduction}%}만큼, 증기 출력을 {color_loss:{var:steam_penalty}%}만큼 낮춥니다.