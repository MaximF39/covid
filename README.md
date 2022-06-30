Разделение на кластеры 
-------
Что делает?
-------
Программа находит среднее значение всех колонок из csv. sum( column / mean_column * coef )
Находит медиану среди всех стран по колонке. Затем делит значение колонки на эту медиану и умножает на коэффициент,
заданный вами<br>
Подробнее: https://github.com/owid/covid-19-data/blob/master/public/data/README.md

Результат
---------
На выходе получается папка, в которой:
файлы с информацией

Settings
-------
В файле config можно настроить коэффициенты:
- max_coef - максимальный коэффициент для колонки<br> 
- categories - tuple, в котором название - является названием категорий.<br>
- Количество категорий - длинна tuple columns_to_coef - словарь с коэффициентами каждой колонки<br>

Настройка выходных файлов:<br>
*Если имя не указано, то файл не будет создан<br>
- r_json_filename - Краткая информация о каждой стране
- r_csv_filename - Результат в формате csv id, country_name, coef
- r_coef_filename - Файл с коэффициентами введёнными
- r_info_filename - Подробная информация о каждой стране и её коэффициентов
- mean_filename - Файл с медианами по колонкам


Visualization:
---------
from visualization import show_corr
show_corr()

![](https://github.com/MaximF39/covid/blob/master/screenshots/corr.png)
