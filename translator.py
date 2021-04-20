from googletrans import Translator

translator=Translator()

v='हैलो एलेक्सा में आपका स्वागत है'

out=translator.translate('हैलो एलेक्सा में आपका स्वागत है', dest='en') 

print(out.text)
