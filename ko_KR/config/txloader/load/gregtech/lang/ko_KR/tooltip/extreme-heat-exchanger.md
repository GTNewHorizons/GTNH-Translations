입력은 {color_hot:용암}, {color_hot:고온 냉각수}, {color_hot:고온 태양염} 또는 {color_hot:플라즈마}입니다
출력은 {color_cold:파호이호이 용암}, {color_cold:IC2 냉각수}, {color_cold:저온 태양염} 또는 {color_cold:용융 금속}입니다
이 과정에서 증류수를 {color_steam:SH 증기} 또는 {color_steam:SC 증기}로 변환합니다
고온 유체의 입력 속도가 특정 {color_mechanic:기준치}를 초과하면 {color_steam:SC 증기}를 출력합니다
{color_danger:증류수가 떨어지면 즉시 폭발합니다}
{hr}
{color_hot:용암} | SC 기준치 {color_mechanic:80,000 {L}/s} | 최대 입력 {color_hot:160,000 {L}/s} | 최대 출력 {color_steam:640,000 {L}/t SC 증기}
{color_hot:고온 냉각수} | SC 기준치 {color_mechanic:8,000 {L}/s} | 최대 입력 {color_hot:128,000 {L}/s} | 최대 출력 {color_steam:1,280,000 {L}/t SC 증기}
{color_hot:고온 태양염} | SC 기준치 {color_mechanic:1,600 {L}/s} | 최대 입력 {color_hot:3,200 {L}/s} | 최대 출력 {color_steam:160,000 {L}/t SC 증기}
{hr}
{color_hot:플라즈마}는 입력 속도와 관계없이 항상 {color_steam:고밀도 SC 증기}를 출력합니다
최대 입력 및 출력 속도는 플라즈마의 밀도({EU}/{L})에 따라 달라집니다
{hr}
컨트롤러의 회로는 증기를 희생하여 SC 기준치를 낮춥니다
1을 초과하는 회로마다 SC 기준치가 {color_mechanic:-150 {L}/s} 낮아지고 증기 출력이 {color_steam:-1.5%} 감소합니다