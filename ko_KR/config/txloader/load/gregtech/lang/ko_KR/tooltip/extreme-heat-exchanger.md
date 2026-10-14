입력: {red:용암}, {red:고온 냉각수}, {red:고온 태양염} 또는 {red:플라즈마}
출력: {blue:파호이호이 용암}, {blue:IC2 냉각수}, {blue:저온 태양염} 또는 {blue:용융 금속}
작동 과정에서 증류수를 {white:SH 증기} 또는 {white:SC 증기}로 변환합니다
고온 유체의 입력 속도가 특정 {light_purple:기준치}를 초과하면 {white:SC 증기}를 출력합니다
증류수가 떨어지면 즉시 폭발합니다
{gray:{hr}}
{red:용암} | SC 기준치 {light_purple:80,000 {var:unit}/s} | 최대 입력 {red:160,000 {var:unit}/s} | 최대 출력 {white:640,000 {var:unit}/t SC 증기}
{red:고온 냉각수} | SC 기준치 {light_purple:8,000 {var:unit}/s} | 최대 입력 {red:128,000 {var:unit}/s} | 최대 출력 {white:1,280,000 {var:unit}/t SC 증기}
{red:고온 태양염} | SC 기준치 {light_purple:1,600 {var:unit}/s} | 최대 입력 {red:3,200 {var:unit}/s} | 최대 출력 {white:160,000 {var:unit}/t SC 증기}
{gray:{hr}}
{red:플라즈마}는 입력 속도와 관계없이 항상 {white:고밀도 SC 증기}를 출력합니다
최대 입력 및 출력 속도는 플라즈마의 밀도(EU/L)에 따라 달라집니다
{gray:{hr}}
컨트롤러의 회로는 증기 생산량을 희생해 SC 기준치를 낮춥니다
회로 설정값이 1을 초과할 때마다 SC 기준치가 {light_purple:-150 {var:unit}/s} 낮아지고 증기 출력량이 {white:-1.5%} 감소합니다