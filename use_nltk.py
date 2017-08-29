import nltk
# nltk.download() first time only
from nltk.book import * # necessary each time to put info in memory
print(list(set(text7))[:10])
Last login: Sat Aug 26 10:18:33 on console
Jamess-MBP:~ JamesFangmeyerJr$ cd '/Users/JamesFangmeyerJr/Documents/Python Data Science/Text Mining'
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
Traceback (most recent call last):
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/util.py", line 63, in __load
    try: root = nltk.data.find('corpora/%s' % zip_name)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'corpora/gutenberg.zip/gutenberg/' not found.  Please
  use the NLTK Downloader to obtain the resource:  >>>
  nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "use_nltk.py", line 2, in <module>
    from nltk.book import *
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/book.py", line 20, in <module>
    text1 = Text(gutenberg.words('melville-moby_dick.txt'))
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/util.py", line 99, in __getattr__
    self.__load()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/util.py", line 64, in __load
    except LookupError: raise e
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/util.py", line 61, in __load
    root = nltk.data.find('corpora/%s' % self.__name)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'corpora/gutenberg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
<Text: Moby Dick by Herman Melville 1851>
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
Traceback (most recent call last):
  File "use_nltk.py", line 4, in <module>
    print(sent3)
NameError: name 'sent3' is not defined
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
Traceback (most recent call last):
  File "use_nltk.py", line 4, in <module>
    print(text1)
NameError: name 'text1' is not defined
Jamess-MBP:Text Mining JamesFangmeyerJr$ python
Python 3.5.2 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> esc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'esc' is not defined
>>> q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'q' is not defined
>>> exit()
Jamess-MBP:Text Mining JamesFangmeyerJr$ python
Python 3.5.2 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> use_nltk.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'use_nltk' is not defined
>>> /Users/JamesFangmeyerJr/Documents/Python\ Data\ Science/Text\ Mining/use_nltk.py
  File "<stdin>", line 1
    /Users/JamesFangmeyerJr/Documents/Python\ Data\ Science/Text\ Mining/use_nltk.py
    ^
SyntaxError: invalid syntax
>>> '/Users/JamesFangmeyerJr/Documents/Python Data Science/Text Mining/use_nltk.py'
'/Users/JamesFangmeyerJr/Documents/Python Data Science/Text Mining/use_nltk.py'
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> sent(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sent' is not defined
>>> text(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'text' is not defined
>>> text1
<Text: Moby Dick by Herman Melville 1851>
>>> sent1
['Call', 'me', 'Ishmael', '.']
>>> print(text1)
<Text: Moby Dick by Herman Melville 1851>
>>> exit()
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
Traceback (most recent call last):
  File "use_nltk.py", line 4, in <module>
    text1
NameError: name 'text1' is not defined
Jamess-MBP:Text Mining JamesFangmeyerJr$ python
Python 3.5.2 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> text1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'text1' is not defined
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> list(set(text7))[:10]
['progress', '14.6', 'ambitious', 'copyrights', 'lowering', 'underwent', 'ground', 'Compound', '*-26', '13.15']
>>> list(set(text7))[:10]
['progress', '14.6', 'ambitious', 'copyrights', 'lowering', 'underwent', 'ground', 'Compound', '*-26', '13.15']
>>> exit() python use_nltk.py
  File "<stdin>", line 1
    exit() python use_nltk.py
                ^
SyntaxError: invalid syntax
>>> exit()
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
Jamess-MBP:Text Mining JamesFangmeyerJr$ python use_nltk.py
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
['Partners', 'Domaine', 'Telephone', 'buys', 'others', 'Buying', 'among', 'situation', 'drooled', 'NL']
Jamess-MBP:Text Mining JamesFangmeyerJr$ python
Python 3.5.2 |Anaconda 4.2.0 (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> dist = FreqDist(text7)
>>> vocab1 = dist.keys()
>>> len(dist)
12408
>>> vocab1[:10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_keys' object is not subscriptable
>>> list(vocab1)[:10]
['outlawing', 'assemble', 'shaky', 'Guarantee', 'Pharaoh', 'taking', 'buildings', 'once', 'Journal', 'appearing']
>>> dist['four']
20
>>>
>>> dist['in']
1572
>>> dist['the']
4045
>>> dist.max()
','
>>> dist.min()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FreqDist' object has no attribute 'min'
>>> dist.median()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FreqDist' object has no attribute 'median'
>>> dist.mean()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FreqDist' object has no attribute 'mean'
>>> dist['outlawing']
1
>>> dist['Pierre']
1
>>> dist['Vinken']
2
>>> dist['years']
115
>>> long_freq_words = [w for w in vocab1 if len(w)>6 and dist[w] > 100]
>>> long_freq_words
['million', 'trading', 'billion', 'because', 'program', 'company', 'president']
>>> long_freq_words = [w for w in vocab1 if len(w)>5 and dist[w] > 100]
>>> long_freq_words
['million', 'trading', 'market', 'billion', 'shares', 'because', 'program', 'company', 'president']
>>> list1 = 'Lists listed lists linsting listless listings'
>>> words = list1.split('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: empty separator
>>> words = list1.split(' ')
>>> words
['Lists', 'listed', 'lists', 'linsting', 'listless', 'listings']
>>> words.lower()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'lower'
>>> words = words.lower()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'lower'
>>> words = list1.lower().split(' ')
>>> words
['lists', 'listed', 'lists', 'linsting', 'listless', 'listings']
>>> porter = nltk.PorterStemmer()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nltk' is not defined
>>> import nltk
>>> porter = nltk.PorterStemmer()
>>> porter.stem(t) for t in words
  File "<stdin>", line 1
    porter.stem(t) for t in words
                     ^
SyntaxError: invalid syntax
>>> [porter.stem(t) for t in words]
['list', 'list', 'list', 'linst', 'listless', 'list']
>>> [porter.stem(s) for t in words]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
NameError: name 's' is not defined
>>> [porter.stem(i) for t in words]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
NameError: name 'i' is not defined
>>> udhr = nltk.corpus.udhr.words('English-Latin')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/plaintext.py", line 89, in words
    in self.abspaths(fileids, True, True)])
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/api.py", line 190, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/api.py", line 190, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 322, in join
    return FileSystemPathPointer(_path)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/compat.py", line 561, in _decorator
    return init_func(*args, **kwargs)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 300, in __init__
    raise IOError('No such file or directory: %r' % _path)
OSError: No such file or directory: '/Users/JamesFangmeyerJr/nltk_data/corpora/udhr/English-Latin'
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> udhr = nltk.corpus.udhr.words('English-Latin')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/plaintext.py", line 89, in words
    in self.abspaths(fileids, True, True)])
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/api.py", line 190, in abspaths
    paths = [self._root.join(f) for f in fileids]
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/corpus/reader/api.py", line 190, in <listcomp>
    paths = [self._root.join(f) for f in fileids]
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 322, in join
    return FileSystemPathPointer(_path)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/compat.py", line 561, in _decorator
    return init_func(*args, **kwargs)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 300, in __init__
    raise IOError('No such file or directory: %r' % _path)
OSError: No such file or directory: '/Users/JamesFangmeyerJr/nltk_data/corpora/udhr/English-Latin'
>>> udhr = nltk.corpus.udhr.words('English-Latin1')
>>> udhr[:20]
['Universal', 'Declaration', 'of', 'Human', 'Rights', 'Preamble', 'Whereas', 'recognition', 'of', 'the', 'inherent', 'dignity', 'and', 'of', 'the', 'equal', 'and', 'inalienable', 'rights', 'of']
>>> [porter.stem(t) for t in udhr[:20]]
['Univers', 'Declar', 'of', 'Human', 'Right', 'Preambl', 'Wherea', 'recognit', 'of', 'the', 'inher', 'digniti', 'and', 'of', 'the', 'equal', 'and', 'inalien', 'right', 'of']
>>> [porter.stem(t) for w in udhr[:20]]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
NameError: name 't' is not defined
>>> [porter.stem(t) for t in udhr[:20]]
['Univers', 'Declar', 'of', 'Human', 'Right', 'Preambl', 'Wherea', 'recognit', 'of', 'the', 'inher', 'digniti', 'and', 'of', 'the', 'equal', 'and', 'inalien', 'right', 'of']
>>> textnow = 'Kids shouldn't drink a sugary water-soda before can't colon:test before bed. . , '
  File "<stdin>", line 1
    textnow = 'Kids shouldn't drink a sugary water-soda before can't colon:test before bed. . , '
                            ^
SyntaxError: invalid syntax
>>> textnow = "Kids shouldn't drink a sugary water-soda before can't colon:test before bed. . , "
>>> textnow.split(' ')
['Kids', "shouldn't", 'drink', 'a', 'sugary', 'water-soda', 'before', "can't", 'colon:test', 'before', 'bed.', '.', ',', '']
>>> nltk.word_tokenize(textnow)
['Kids', 'should', "n't", 'drink', 'a', 'sugary', 'water-soda', 'before', 'ca', "n't", 'colon', ':', 'test', 'before', 'bed', '.', '.', ',']
>>> nltk.sent_tokenize(textnow)
["Kids shouldn't drink a sugary water-soda before can't colon:test before bed.", '.', ', ']
>>> len(nltk.sent_tokenize(textnow))
3
>>> nltk.help.upenn_tagset('MD')
MD: modal auxiliary
    can cannot could couldn't dare may might must need ought shall should
    shouldn't will would
>>> nltk.pos_tag(nltk.word_tokenize(textnow))
[('Kids', 'NNS'), ('should', 'MD'), ("n't", 'RB'), ('drink', 'VB'), ('a', 'DT'), ('sugary', 'JJ'), ('water-soda', 'NN'), ('before', 'IN'), ('ca', 'MD'), ("n't", 'RB'), ('colon', 'VB'), (':', ':'), ('test', 'NN'), ('before', 'IN'), ('bed', 'NN'), ('.', '.'), ('.', '.'), (',', ',')]
>>> lovetext = "Alice loves Bob
  File "<stdin>", line 1
    lovetext = "Alice loves Bob
                              ^
SyntaxError: EOL while scanning string literal
>>> lovetext = "Alice loves Bob"
>>> lovetext = nltk.word_tokenize(lovetext)
>>> grammar = nltk.CFG.fromstring("""
... S-> NP VP
... VP -> V NP
... NP -> "Alice | "Bob"
... V -> "loves"
... """)
Traceback (most recent call last):
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1270, in read_grammar
    productions += _read_production(line, nonterm_parser, probabilistic)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1180, in _read_production
    if not m: raise ValueError('Expected an arrow')
ValueError: Expected an arrow

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 519, in fromstring
    encoding=encoding)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1273, in read_grammar
    (linenum+1, line, e))
ValueError: Unable to parse line 2: S-> NP VP
Expected an arrow
>>> S -> NP VP
  File "<stdin>", line 1
    S -> NP VP
       ^
SyntaxError: invalid syntax
>>> [grammar = nltk.CFG.fromstring("""
  File "<stdin>", line 1
    [grammar = nltk.CFG.fromstring("""
             ^
SyntaxError: invalid syntax
>>> (grammar = nltk.CFG.fromstring("""
  File "<stdin>", line 1
    (grammar = nltk.CFG.fromstring("""
             ^
SyntaxError: invalid syntax
>>> grammar = nltk.CFG.fromstring(""" S -> NP VP VP -> V NP NP -> 'Alice' | "Bob" V -> "loves" """)
Traceback (most recent call last):
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1270, in read_grammar
    productions += _read_production(line, nonterm_parser, probabilistic)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1213, in _read_production
    nonterm, pos = nonterm_parser(line, pos)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1286, in standard_nonterm_parser
    + string[pos:])
ValueError: Expected a nonterminal, found: -> V NP NP -> 'Alice' | "Bob" V -> "loves"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 519, in fromstring
    encoding=encoding)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/grammar.py", line 1273, in read_grammar
    (linenum+1, line, e))
ValueError: Unable to parse line 1: S -> NP VP VP -> V NP NP -> 'Alice' | "Bob" V -> "loves"
Expected a nonterminal, found: -> V NP NP -> 'Alice' | "Bob" V -> "loves"
>>> grammar = nltk.CFG.fromstring("""
... S -> NP VP
... VP -> V NP
... NP -> "Alice" | "Bob"
... V -> "loves"
... """)
>>> parser = nltk.ChartParser(grammar)
>>> trees = parser.parse_all(text15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'text15' is not defined
>>> trees = parser.parse_all(lovetext)
>>> for tree in trees:
... print(tree)
  File "<stdin>", line 2
    print(tree)
        ^
IndentationError: expected an indented block
>>> for tree in trees: print(tree)
...
(S (NP Alice) (VP (V loves) (NP Bob)))
>>> [for tree in trees print(tree)]
  File "<stdin>", line 1
    [for tree in trees print(tree)]
       ^
SyntaxError: invalid syntax
>>> [print(tree) for tree in trees]
(S (NP Alice) (VP (V loves) (NP Bob)))
[None]
>>> teletext = nltk.word_tokenize('I saw the man with the telescope walking')
>>> grammarly = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> grammarly = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> grammar1 = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> grammar1 = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> grammar1 = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> grammar1 = nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> fgrammar1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fgrammar1' is not defined
>>> nltk.data.load('mygrammar.cfg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 801, in load
    opened_resource = _open(resource_url)
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 919, in _open
    return find(path_, path + ['']).open()
  File "/Users/JamesFangmeyerJr/anaconda/lib/python3.5/site-packages/nltk/data.py", line 641, in find
    raise LookupError(resource_not_found)
LookupError:
**********************************************************************
  Resource 'mygrammar.cfg' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Users/JamesFangmeyerJr/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************
>>> nltk.pos_tag(teletext)
[('I', 'PRP'), ('saw', 'VBD'), ('the', 'DT'), ('man', 'NN'), ('with', 'IN'), ('the', 'DT'), ('telescope', 'NN'), ('walking', 'NN')]
