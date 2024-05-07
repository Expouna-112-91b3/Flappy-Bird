"""
CLASSE PARA QUALQUER TIPO DE TESTE
"""


class Test:
    class logger:
        def log(text):
            print(f"{text}")


Test.logger.log("Hello world!")
