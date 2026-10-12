from permissao_vaga import ValidadorDeEstacionamento
 
 
def test_aluno_pode_estacionar_em_vaga_comum():
    validador = ValidadorDeEstacionamento()
    assert validador.pode_estacionar("aluno", "comum") is True
 
 
def test_aluno_nao_pode_estacionar_em_vaga_de_funcionario():
    validador = ValidadorDeEstacionamento()
    assert validador.pode_estacionar("aluno", "funcionario") is False
 
 
def test_funcionario_pode_estacionar_em_vaga_de_funcionario():
    validador = ValidadorDeEstacionamento()
    assert validador.pode_estacionar("funcionario", "funcionario") is True
 