# Sistema de perguntas e respostas
# Utilizando o dicionário como estrutura

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '0'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é  18/3?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
            'd': '6'
        },
        'resposta_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'O ano bissexto tem quantos dias ?',
        'respostas': {
            'a': '364',
            'b': '366',
            'c': '368',
            'd': '365'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 4': {
        'pergunta': 'Uma hora tem quantos segundos?',
        'respostas': {
            'a': '60',
            'b': '1000',
            'c': '3600',
            'd': '1800'
        },
        'resposta_certa': 'c'
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print('Escolha a resposta abaixo')
    for kr, vr in pv['respostas'].items():
        print(f"[{kr}] {vr}")

    resposta_user = input('Digite a sua resposta.\n')

    if resposta_user == pv['resposta_certa']:
        print('Muito bem !!!!!!, Vc acertou passa para próxima pergunta.')
        respostas_certas += 1
    else:
        print('Deu ruim vc errou ')
    print()

    quantidade_perguntas = len(perguntas)
    percentual_acerto = (respostas_certas/quantidade_perguntas)*100

    print(f'Seu percentual de acerto {percentual_acerto}%.')
