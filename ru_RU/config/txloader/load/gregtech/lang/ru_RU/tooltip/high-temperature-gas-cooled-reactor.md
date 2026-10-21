Расходует до {color_amount:{var:fuel_percent}%} {color_name:топлива} за операцию
Для запуска нужно минимум {color_amount:{var:min_helium}%} {color_key:гелия}
{color_key:Гелий} линейно повышает эффективность теплообменников вплоть до {color_amount:100%} при полном запасе
Реактор теряет {color_amount:{var:helium_lost}%} запаса {color_key:гелия} за операцию
Потребляет {color_eu_usage:{var:power} {EU/t}}, до {color_amount:{var:power_penalty}x} больше при нехватке {color_key:гелия}
{hr}
Длительность операции зависит от заполненности реактора
От {color_amount:{var:min_time} с} до {color_amount:{var:max_time} с}
{color_amount:10%} этого значения фиксированы, {color_amount:90%} зависят от формулы {aqua:y = 1 - (1 - x)^3} ({white:x}, это заполненность в %)
Каждая проблема обслуживания снижает эффективность на {color_amount:20%}
{hr}
Подача {color_key:хладагента}, {color_key:воды} или обоих сокращает время рецепта на
{color_amount:{var:coolant_speedup}%} / {color_amount:{var:water_speedup}%} / {color_amount:{var:total_speedup}%} от общего времени в секунду
Количество жидкости для максимального бонуса зависит от числа {color_key:шариков TRISO}
{color_amount:{var:coolant_per_ball}} {color_key:хладагента}/тик/шарик и {color_amount:{var:water_per_ball}} {color_key:дистиллированной воды}/тик/шарик