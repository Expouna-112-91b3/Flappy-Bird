"""
este arquivo é um setup global, executado
antes de todos os outros testes
"""

import unittest

from config import Config


def startTestRun(self):
    """
    aqui, por exemplo, estamos inicializando a configuracao geral do jogo,
    para que os testes unitários tenham uma tela para serem testados
    """
    self.config = Config()
    self.config.start_screen()


unittest.result.TestResult.startTestRun = startTestRun
