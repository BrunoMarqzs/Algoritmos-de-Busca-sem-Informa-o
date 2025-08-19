def send_more_money_dfs():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    usados = set()
    mapping = {}

    def dfs(pos):
        if pos == len(letters):
            s = mapping['S']
            e = mapping['E']
            n = mapping['N']
            d = mapping['D']
            m = mapping['M']
            o = mapping['O']
            r = mapping['R']
            y = mapping['Y']

            send = 1000*s + 100*e + 10*n + d
            more = 1000*m + 100*o + 10*r + e
            money = 10000*m + 1000*o + 100*n + 10*e + y

            if send + more == money:
                return mapping.copy(), send, more, money
            return None

        letra = letters[pos]
        for digito in range(10):
            if digito in usados:
                continue
            if letra in ['S', 'M'] and digito == 0:
                continue  # S e M não podem ser zero
            mapping[letra] = digito
            usados.add(digito)
            resultado = dfs(pos + 1)
            if resultado:
                return resultado
            
            usados.remove(digito)
            del mapping[letra]
        return None

    return dfs(0)

resultado = send_more_money_dfs()
print(resultado)
