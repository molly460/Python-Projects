from googletrans import Translator
phrase = """ Guten Tag
Entschuldigung 
"""
translator = Translator()
result = translator.translate(phrase,dest="en")
print(result)
print(result.text)
