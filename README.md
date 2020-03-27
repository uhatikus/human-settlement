
# Human settlement
(описание на русском языке - ниже)

### Description 

This is the simplest program in python3 used to get the settlements of the given countries that exist in the social network vk.com. Results are saved in mysql database. 

In the folder obtained_mysql_table, there is an example of the resulting table (with human settlements of CIS++ countries) in .zip format, which contains compressed .sql file. 

#### CIS++ countries:
Russia - 1,
Ukraine - 2,
Belarus - 3,
Kazakhstan - 4,
Azerbaijan - 5,
Armenia - 6,
Georgia - 7,
Kyrgyzstan - 11,
Latvia - 12,
Lithuania - 13,
Estonia - 14,
Moldova - 15,
Tajikistan - 16,
Turkmenistan - 17,
Uzbekistan - 18.


### Required python3 packages

`pip3 install vk_api`

`pip3 install pymysql`

`pip3 install pyyaml`

### Before running

Before running, fill in the correct information for mysql and vk databases connections in the file `params.yaml`. Also, fill in the ids of the countries whose human settlements you would like to see in your mysql database. 

### Run

`python3 main.py` 

#### I am not responsible for the accuracy of vk.com data.




# Населённые пункты

### Описание 

Это простейшая программа на python3 для получения населённых пунктов заданных странах, существующих в социальной сети vk.com, и их сохранения в базе данных mysql. 

В папке obtained_mysql_table находится пример полученной таблицы (с населенными пунктами стран СНГ++) в формате .zip, в котором сжат файл .sql. 

#### Страны СНГ++:
Россия - 1,
Украина - 2,
Беларусь - 3,
Казахстан - 4,
Азербайджан - 5,
Армения - 6,
Грузия - 7,
Кыргызстан - 11,
Латвия - 12,
Литва - 13,
Эстония - 14,
Молдова - 15,
Таджикистан - 16,
Туркменистан - 17,
Узбекистан - 18

### Необходимые пакеты python3

`pip3 install vk_api`

`pip3 install pymysql`

`pip3 install pyyaml`

### Перед запуском

Перед запуском заполните достоверную информацию для подключения к базе данных mysql и vk в файле `params.yaml`. А так же заполните id стран, чьи населенные пункты вы хотели бы видеть в своей базе данных. 

### Запуск

`python3 main.py` 

#### За достоверность данных vk.com ответственность не несу.  
