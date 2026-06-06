class Sinal:
    def __init__(self,n,v):
        self.n = n
        self.v = v
        self.resultado = []
        self.lista_plana()

    def lista_plana(self):
        if (isinstance(self.n, int) and self.n >= 1 and
            isinstance(self.v, (list,tuple)) and len(self.v) == self.n):


            self.resultado.append((self.n,self.v))
            return True
        else:
            return False

    def __mul__(self, other):
        # Proteção: Se o filtro não for 3 ou a lista for muito pequena, não filtra
        if other != 3 or len(self.v) < 3:
            return str(self.v).replace(" ", "")

        novo_sinal = []

        # 1. Borda esquerda (primeiro elemento)
        novo_sinal.append(self.v[0])

        # 2. O loop calcula e já guarda cada média imediatamente
        for i in range(1, len(self.v) - 1):
            soma = self.v[i - 1] + self.v[i] + self.v[i + 1]
            media = soma / 3

            # Corrigido: Agora está dentro do loop!
            novo_sinal.append(media)

        novo_sinal.append(self.v[-1])

        # Retorna o resultado limpo como o corretor exige
        return str(novo_sinal).replace(" ", "")
    def __repr__(self):
        return str(self.v).replace(" ","")


# --- Fluxo Principal ---
entrada = input().strip()
partes = entrada.split("*")

texto_limpo = partes[0].replace("(", "").replace(")", "").replace("[", "").replace("]", "")
dados = [int(x) for x in texto_limpo.split(",")]

n = dados[0]
v = dados[1:]

sinal_orig = Sinal(n,v)
tamanho_fix = int(partes[1])
print(sinal_orig * tamanho_fix)