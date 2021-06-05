from translate import Translator

phrase = input("Phrase:")
translate = Translator(to_lang="tamil")
out = translate.translate(phrase)
print(out)
