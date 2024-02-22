sua_vida = int(input())
poder_sua_arma = int(input())
sua_habilidade_luta = int(input())
seu_poder_surpresa = int(input())
poder_arma_mascarado = int(input())
habilidade_luta_mascarado = int(input())
poder_surpresa_mascarado = int(input())
defesa_mascarado = int(input())
poder_arma_novo_mascarado = 0
poder_luta_novo_mascarado = 0
poder_surpresa_novo_mascarado = 0
nova_vida = 0

if poder_sua_arma > poder_arma_mascarado and sua_habilidade_luta > habilidade_luta_mascarado and seu_poder_surpresa > poder_surpresa_mascarado:
    print('Ainda bem que deu tudo certo, está quase em casa')
    poder_arma_novo_mascarado = int(input())
    poder_luta_novo_mascarado = int(input())
    poder_surpresa_novo_mascarado = int(input())
    if poder_sua_arma >= poder_arma_novo_mascarado or sua_habilidade_luta >= poder_luta_novo_mascarado or seu_poder_surpresa >= poder_surpresa_novo_mascarado:
        print('Casa, aqui vou eu')
    else:
        print('Oh, no! Acabou pra mim')
    
else:
    nova_vida = sua_vida - defesa_mascarado
    if nova_vida > 0:
        print('Rápido, corra antes que ele vá atrás de você!')
        poder_sua_arma = poder_sua_arma - (5/100) * poder_sua_arma
        sua_habilidade_luta = sua_habilidade_luta - (5/100) * sua_habilidade_luta
        seu_poder_surpresa = seu_poder_surpresa + (5/100) * seu_poder_surpresa
        poder_arma_novo_mascarado = int(input())
        poder_luta_novo_mascarado = int(input())
        poder_surpresa_novo_mascarado = int(input())
        if poder_sua_arma >= poder_arma_novo_mascarado and sua_habilidade_luta >= poder_luta_novo_mascarado and seu_poder_surpresa >= poder_surpresa_novo_mascarado:
            print('Casa, aqui vou eu')
        else:
            print('Oh, no! Acabou pra mim')
    elif nova_vida <= 0:
        print('Oh, no! Acabou pra mim')





