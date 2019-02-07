from urllib.request import urlopen
from bs4 import BeautifulSoup

res = urlopen('https://www.spanishdict.com/wordoftheday')
bs = BeautifulSoup(res.read().decode(), 'html.parser')

bs.find('div', 'main-container-video').find('div', 'card').find('div', 'sd-wotd-container')
today = bs.find('div', "sd-wotd-date-today")

date_html, word_html = [c for c in today.parent.parent.children]

word        = word_html.find('h3','sd-wotd-headword').text
translation = word_html.find('div', "sd-wotd-translation").text

examples = [(ex.find('div', "sd-wotd-example-source").text,
             ex.find('div', "sd-wotd-example-translation").text) \
                     for ex in word_html.find('ol',"sd-wotd-examples-list").children]

formatted_example = \
"""
  {}
  {}
"""
formatted_examples = "".join([formatted_example.format(*ex) for ex in examples])
formatted_text = \
"""
---- Palabra -----

  {word}
  {translation}

---- Ejemplos ----
{examples}
"""

print(formatted_text.format(word=word,
                            translation=translation,
                            examples=formatted_examples))
