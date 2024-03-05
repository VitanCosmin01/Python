from googletrans import Translator

translator = Translator()
txt = "Comment allez vous?"
output = translator.detect('Comment allez vous?')
print(output)

