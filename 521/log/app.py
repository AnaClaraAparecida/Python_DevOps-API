import logging
import logging.config

logging.config.fileConfig('logging.ini')

logger = logging.getLogger(__name__)
#logging.basicConfig(
    #level=logging.DEBUG,
    #format='%(asctime)s - %(levelname)s - %(name)s - %(message)s ',
    #filename='app.log'
#)

while True:
    try:
        n1 = int(input('n1 :'))
        n2 = int(input('n2 :'))

        res = n1 / n2
        
    except ZeroDivisionError:
        print('Nao divir por zero')
        logger.warning(f'tentativa de divisao por zero - n1:{n1}, n2:{n2}')
    except ValueError:
        print('informe apenas numeros')
        logger.warning(f'entrada incorreta - n1:{n1}, n2:{n2}')
    except Exception as e:
        print('erro inseperado, tente novamente')
        logger.critical(f'erro inesperado {e}', exc_info=True)
    else:
        print(f'resultado da operaçao: {n1}/{n2}={res}')
        logger.info(f'Operaçao realizada com sucesso: {n1} / {n2} = {res}')
