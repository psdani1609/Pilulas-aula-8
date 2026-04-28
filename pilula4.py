def AtualizarHist(hist,paciente):
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist

def main():
    hist = ['Ana', 'Carlos', 'Beatriz']
    novo = 'Ana'
    print(f'Hist Atual {hist}')
    hist = AtualizarHist(hist, novo)
    print(f'Hist atualizado: {hist}')

main()