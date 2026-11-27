입자 빔을 전기장에 통과시켜 더 높은 에너지로 가속합니다
따라서 전기적으로 중성인 {color_mechanic:입자}는 영향을 받지 않습니다
{lang:gtnhlanth.tt.beaminfo}
{hr}
작동하려면 {aqua:길이 * 1,000 {var:fluidUnit}/s}의 {aqua:냉각수}가 필요하며, {red:뜨거운 냉각수}로 반환됩니다
{lang:gtnhlanth.tt.coolant.oxygen}
{lang:gtnhlanth.tt.coolant.nitrogen}
{lang:gtnhlanth.tt.coolant.coolant}
{lang:gtnhlanth.tt.coolant.Scoolant}
{hr}
길이/전력을 높이면 {blue:출력 빔 에너지}는 증가하지만 {dark_green:출력 빔 초점}은 감소합니다
낮은 온도의 {aqua:냉각수}를 사용하면 {dark_green:빔 초점}을 더 효과적으로 유지합니다
{hr}
{blue:출력 빔 에너지}{color_formula: = max(}{color_note:V}{white:, 50) * 10^}{color_note:IE}
여기서 {color_note:V}{color_formula: = 0.25 * (Length - 1) * cbrt({color_eu_usage:{EU/t} 제공됨})}
그리고 {color_note:IE}{color_formula: = 1 + min({blue:입력 빔 에너지}, 7500) / }{blue:최대 입자 에너지}
{hr}
{dark_green:출력 빔 초점}{color_formula: = (dark_green:입력 빔 초점} + {color_note:기계 초점})/2} (조건: {dark_green:입력 빔 초점}{color_formula: > {color_note:기계 초점}})
{dark_green:출력 빔 초점}{color_formula: = {dark_green:입력 빔 초점} * {color_note:기계 초점}/100} (조건: {dark_green:입력 빔 초점}{color_formula: <= {color_note:기계 초점}})
여기서 {color_note:기계 초점}{color_formula: = min(90, max(5, (-0.9 * (Length-1) * 1.1^(0.2 * {aqua:냉각수 온도}) + 110)))}