class FiltroPretoBranco:
    def __init__(self, w,h,lista_pixels):
        self.w = w
        self.h = h
        self.pixels = lista_pixels
        self.resultado = []
        # Validação de dados
        self.Validador_pixel()

    def Validador_pixel(self):
        if ((isinstance(self.w, int) and  self.w >=1 and
           isinstance(self.h, int)   and  self.h >= 1 and
           isinstance(self.pixels, (list,tuple)) and len(self.pixels) == self.w * self.h and
           all(0 <= x <= 255 for x in self.pixels))):

           self.resultado.append((self.w,self.h,self.pixels))
           return True

        else:
            return False

    def __sub__(self, limiar):
        lista_final = []
        for pixel in self.pixels:
            if pixel <= limiar:
                lista_final.append(0)
            else:
                lista_final.append(255)
        pass


        return str(lista_final).replace(" ", "")

# --- Fluxo Principal ---"

entrada = input().strip()
partes = entrada.split("-")

texto_limpo = partes[0].replace(" ", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
dados = [int(x) for x in texto_limpo.split(",")]

w = dados[0]
h = dados[1]
lista_pixels = dados[2:]

imagem = FiltroPretoBranco(w,h,lista_pixels)
liminar_fixo = int(partes[1])

print(imagem - liminar_fixo)