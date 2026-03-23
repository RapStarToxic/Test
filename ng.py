import  logging
from datetime import datetime

logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.FileHandler('seans.log', encoding='utf-8')
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s -%(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

x = int(input("Выберите опцию:\n1: Посмотреть текущее время\n2: Изменить настройки\n0: Выход\n"))
vhod = datetime.now()
logger.info('Вход в систему')
while x!=0:
    if x == 1:
        print(datetime.now())
    if x == 2:
        print("Изменение настроек")
        logger.info('Изменение настроек')
    x = int(input("Выберите опцию:\n1: Посмотреть текущее время\n2: Изменить настройки\n0: Выход\n"))
vihod = datetime.now()
vremya_seansa = vihod - vhod
logger.info('Выход из системы')
logger.info(f'Время сеанса - {vremya_seansa}')

