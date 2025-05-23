import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Inscrição duplicada
]

# Função assíncrona para inscrever um aluno
async def inscrever(aluno):
    nome = aluno["nome"]
    curso = aluno["curso"]
    turma = cursos[curso]

    # Simula um pequeno atraso de rede/processamento
    await asyncio.sleep(0.1)

    if nome in turma["inscritos"]:
        print(f"{nome} já está inscrito(a) no curso {curso}. Inscrição rejeitada.")
        return

    if turma["vagas"] > 0:
        turma["inscritos"].append(nome)
        turma["vagas"] -= 1
        print(f"{nome} foi inscrito(a) com sucesso no curso {curso}.")
    else:
        print(f"Turma lotada! {nome} não pôde se inscrever no curso {curso}.")

# Função principal que dispara todas as inscrições em paralelo
async def main():
    await asyncio.gather(*(inscrever(aluno) for aluno in alunos))

# Executa o sistema
asyncio.run(main())