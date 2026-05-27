def funcao_completa(pam_comp, param_default ="default",*args,**kwargs):
    print(f"\nObrigado por {pam_comp}")
    print(f"Parametro default: {param_default}")
    print(f"Parametro Posicionais: {args}")
    print(f"Parametro Nomeados: {kwargs}")


funcao_completa(10,"personalizado",1,2,3,chave="Dara",chave2="Ohana")