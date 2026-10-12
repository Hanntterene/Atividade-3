class ValidadorDeEstacionamento:
 
    def pode_estacionar(self, perfil, tipo_vaga):
        if tipo_vaga == "comum":
            return True
        if tipo_vaga == "funcionario":
            return perfil == "funcionario"
        return False
 