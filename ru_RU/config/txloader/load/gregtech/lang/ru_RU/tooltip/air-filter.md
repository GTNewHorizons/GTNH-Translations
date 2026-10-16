Для работы нужна {white:Турбина} в контроллере
Очищает загрязнение в окрестных чанках {green:{var:chunk_size}x{var:chunk_size}}
Во время работы потребляет фиксированные {aqua:{var:eu_usage} EU/t}
{gray:{hr}}
Каждая {white:выхлопная система} убирает из одного чанка в секунду следующее количество загрязнения
{green:{var:global_multiplier} * B * turbineEff * FLOOR({var:scaling_factor}^mufflerTier)}
Бонус тира этого механизма (B) = {green:{var:tier_bonus}}
turbineEff = эффективность {white:турбины}
Эффективный тир {white:выхлопной системы} ограничен тиром {white:энерговвода}
{gray:{hr}}
Подавайте {gold:абсорбирующие фильтр} через {white:входной люк}, чтобы удвоить очистку ({gold:{var:filter_lifespan}} с на фильтр)
Каждая проблема с техобслуживанием снижает очистку на {green:{var:maint_penalty}%}