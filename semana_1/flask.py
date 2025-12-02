def grito_de_torcida(funçao):
    def funçao_decorada (*args, **kwargs):
      print("Vaaaai...", end = " ")
      funçao(*args, **kwargs)
    return funçao_decorada   

@ grito_de_torcida
def grito_da_Lusa():
   print("LUUUUSA!")

@ grito_de_torcida
def grito_do_guarani():
   print("BUUUGRE!")

@ grito_de_torcida
def grito_do_sampaio_correa():
   print("BOLIVIA QUERIDA!")

# >>> grito_da_Lusa()
#Vaaaai... LUUUUSA!
#>>> grito_do_guarani()
#Vaaaai... BUUUGRE!
#>>> grito_do_sampaio_correa()
#Vaaaai... BOLIVIA QUERIDA!
