def ranking(pacientes):
    RankingPacientes = []
    for paciente in pacientes:
        pontos = 0
        if paciente['gravidade'] >= 4:
            pontos += 3
        elif paciente['gravidade'] >= 2:
            pontos += 2
        if paciente['idade'] >= 60:
            pontos += 2

        RankingPacientes.append({'nome': paciente['nome'],'pontos': pontos})

        for i in range(len(RankingPacientes)):
            for j in range(i + 1, len(RankingPacientes)):
                if RankingPacientes[i]['pontos'] < RankingPacientes[j]['pontos']: RankingPacientes[i], RankingPacientes[j] = RankingPacientes[j], RankingPacientes[i]
                

#print
        for item in range(len(RankingPacientes)):
            print(f'{RankingPacientes[item]['nome']},{RankingPacientes[item]['pontos']}')
              
def main():
    pacientes = [
        {'nome':'Ana'      , 'idade': 70, 'gravidade':3},
        {'nome':'Carlos'   , 'idade': 40, 'gravidade':5},
        {'nome':'Beatriz'  , 'idade': 65, 'gravidade':2},
        {'nome':'João'     , 'idade': 30, 'gravidade':1}
    ]
    ranking(pacientes)
main()