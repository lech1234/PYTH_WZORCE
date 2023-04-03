import logging

logging.basicConfig(filename='moj.log',
                    filemode='wt',
                    encoding='utf8',
                    level=logging.ERROR)

lgr = logging.getLogger(__name__)

# Uwaga logger o id: 'sub1.m112'
# odziedziczy ustawienia z loggera o id: 'sub1'

lgr.critical('linia critical')
lgr.error('linia errror')
lgr.warning('linia warning')
lgr.info('linia info')
lgr.debug('linia debug')

lgr.log(logging.ERROR, 'programowo ustawiony poziom')

# logging.CRITICAL - błędy poza kodem - sys operacyjny, pada sprzęt
# logging.ERROR - krytyczne błędy naszego kodu
# logging.WARNING - niekrytyczne błędy kodu
# logging.INFO - często informacje monitoringowe, wydajnościowe
# logging.DEBUG - informacje konieczne do analizy błedów
