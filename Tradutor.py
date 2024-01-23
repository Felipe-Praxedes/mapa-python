from translate import Translator
from DataTk import SelecionarData

def Traduzir_Mapa(mapa):
    translator = Translator(to_lang="pt")
    translation = translator.translate(mapa)

    palavras = mapa.split("\n")

    texto = ""
    for palavra in palavras:
        translation = translator.translate(palavra)
        texto += "\n" + translation

    print(texto)

    dict = {
        "Sun": "Sol",
        "Moon": "Lua",
            }
