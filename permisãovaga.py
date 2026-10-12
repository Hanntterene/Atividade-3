from abc import ABC, abstractmethod
 
 
class RegraDeAcesso(ABC):  # Strategy
    @abstractmethod
    def permite(self, perfil):
        ...
 
 
class RegraVagaComum(RegraDeAcesso):  # ConcreteStrategy
    def permite(self, perfil):
        return True
 
 
class RegraVagaFuncionario(RegraDeAcesso):  # ConcreteStrategy
    def permite(self, perfil):
        return perfil == "funcionario"
 
 
class ValidadorDeEstacionamento:  # Context
    def __init__(self):
        self._regras = {
            "comum": RegraVagaComum(),
            "funcionario": RegraVagaFuncionario(),
        }
 
    def pode_estacionar(self, perfil, tipo_vaga):
        regra = self._regras.get(tipo_vaga)
        if regra is None:
            return False
        return regra.permite(perfil)
 