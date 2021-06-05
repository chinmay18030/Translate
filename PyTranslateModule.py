from translate import Translator


class PyTran:
    def __init__(self,from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translateFunc(self,phrase):
        translate = Translator(self.to_lang,self.from_lang)
        out = translate.translate(phrase)
        return out



