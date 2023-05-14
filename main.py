def main():

    names = "Caio Araújo,Alexia Freitas,Sra. Nicole Nogueira,Dr. Noah Oliveira,Ana Carolina Barros,Giovanna Rezende,Maria Eduarda Silva,André Nogueira,Ana Lívia Correia,Marina Moura,João Gabriel Almeida,Leonardo Almeida,Ana Beatriz Santos,Rafael Cardoso,Fernanda Castro,Emilly Correia,Luiz Fernando Porto,João Felipe Sales,Arthur Farias,Dr. Renan Novaes,Bernardo Vieira,Sr. Lucas da Mota,Maysa Cardoso,Caroline Rodrigues,Maria Eduarda Almeida,Manuela da Conceição,Kaique da Cruz,Bryan Ribeiro,Vitor Gabriel da Cunha,Cecília das Neves,Gabriela Barros,Mariane Nunes,Fernando Sales,Joana Lima,Isabella Azevedo,Luiz Miguel da Rocha,Luiz Fernando Mendes,Dr. Cauã Peixoto,Ana Laura Correia,Luna Duarte,Maria Eduarda Freitas,Dr. Leonardo Jesus,Laís Melo,Isabelly Melo,João Gabriel Fernandes,Pietro Ferreira,Natália Novaes,Cecília da Luz,Maria Clara Pinto,Maria Monteiro,Juliana Azevedo,Helena Souza,Dr. Paulo Rezende,Emanuel da Rocha,Maria Vitória Freitas,João Vitor Moreira,Valentina Pires,Ryan da Mata,Igor Gomes,Sr. Renan Peixoto,João Pedro Pinto,Ana Laura Ramos,Augusto Cardoso,Catarina Duarte,Luigi da Paz,Marina da Cruz,Felipe da Costa,Dr. Thales Duarte,Lívia Araújo,Joana da Cruz,Bernardo Farias,Ana Julia Mendes,Emanuella Araújo,Dra. Alícia Melo,Samuel das Neves,Otávio Santos,Emanuel da Mota,Diego Cardoso,Clarice Moura,Milena Barbosa,Vitor da Luz,Leonardo Teixeira,Lara Pires,Ana Beatriz da Cruz,Sra. Clara Moraes,João Vitor Monteiro,Rafael Carvalho,Mariane Jesus,Ana Vitória Lopes,Pietro Barbosa,Camila Barros,Camila Mendes,Francisco Costela,Ana Sophia Peixoto,Breno Rezende,Yasmin Monteiro,Sra. Alexia Pereira,Catarina Mendes,Marina Lopes,Luiz Henrique Moura"
    names = names.split(',')

    l1 = [*"Gabriel"]
    l2 = [*"Floriano"]
    l3 = [*"Gabriel Fernando Floriano"]

    C1 = set(l1)
    C2 = set(l2)
    C3 = set(l3)

    print("")

    print("Lista1:", l1, end="\n")
    print("Lista2:", l2, end="\n")
    print("Lista3:", l3, end="\n")

    print("")

    print("Conjunto1:", C1, end="\n")
    print("Conjunto2:", C2, end="\n")
    print("Conjunto3:", C3, end="\n")

    print("")

    print("Tamanho de L1 & Elementos em C1:", comp(l1, C1), end="\n")
    print("Tamanho de L2 & Elementos em C2:", comp(l2, C2), end="\n")
    print("Tamanho de L3 & Elementos em C3:", comp(l3, C3), end="\n")

    print("")

    if (comp(l1, C1) == comp(l2, C2) == comp(l3, C3)):
        print("Os elementos são iguais")
    else:
        print("Os elementos não são iguais, pois:")
        len1, elm1 = comp(l1, C1)
        len2, elm2 = comp(l2, C2)
        len3, elm3 = comp(l3, C3)

        print("   O tamanho da lista nº1 é {}, enquantos os tamanhos das listas nº2 e nº3 são {} e {}".format(
            len1, len2, len3))
        print("")
        print("   Os elementos de C1 são {}\n   Os elementos de C2 são são {} \n   Os elementos de C3 são {}".format(
            elm1, elm2, elm3))

    print("")

    print("LisUnião é: {}".format(concat(l1, l2)))

    print("")

    print("ConjUnião é: {}".format(asmset(C1, C2)))

    print("")

    print("ListInter de L1 e L2 é: {}".format(bindlist(l1, l2)))

    print("")

    print("ConjInter de C1 e C2 é: {}".format(setinter(C1, C2)))

    print("")

    print("Um possível nome com o mesmo tamanho do conjunto é: {}".format(
        get_name(asmset(C1, C2), names)))


def comp(lx, Cx):
    return len(lx), Cx


def concat(l1, l2):
    new_list = l1 + l2
    return new_list


def asmset(c1, c2):
    new_set = c2.union(c1)
    new_set = set(new_set)
    return new_set


def bindlist(l1, l2):
    binded_list = list(set().union(l1, l2))
    return binded_list


def setinter(c1, c2):
    intersec = c1.intersection(c2)
    return intersec


def get_name(con, names):
    for name in names:
        if (len(con) == len(name)):
            return name


main()
