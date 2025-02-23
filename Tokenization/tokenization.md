# Tokenization

Tokenization is the process of converting text into smaller units, typically called "tokens." These tokens can be words, subwords, or even characters, depending on the level of tokenization. Tokenization is a crucial step in natural language processing (NLP) and text analysis because it allows algorithms to process and analyze text in a structured manner.

Here’s a breakdown of different types of tokenization:

**1. Word Tokenization:** Involves splitting a text into individual words. For example:

- Input: "I love programming!"
- Tokens: ["I", "love", "programming", "!"]

**2. Subword Tokenization:** Involves splitting words into smaller units called subwords. This is useful for handling rare or out-of-vocabulary words. For example:

- Input: "unhappiness"
- Tokens: ["un", "happiness"]

**3. Character Tokenization:** Splits the text into individual characters. This is often used in certain NLP models, like character-level language models.

- Input: "Hi"
- Tokens: ["H", "i"]


Tokenization is an essential step in NLP pipelines for tasks like text classification, sentiment analysis, translation, and language modeling.

## Practical Example: Tokenizing with Python (using libraries like `nltk` or `spaCy`)
Here’s a practical example using Python’s `nltk` library, which provides a simple way to tokenize text.

Code Example for Word Tokenization using NLTK:
```python
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "I love programming!"
tokens = word_tokenize(text)
print(tokens)
```

**OUTPUT :**
```
['I', 'love', 'programming', '!']
```

### Subword Tokenization with Huggingface's Tokenizers

In modern NLP, subword tokenization is often used with models like BERT and GPT. The Huggingface library makes it easy to use this kind of tokenization. Here's an example of using BERT tokenizer:

```python
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
text = "unhappiness"
tokens = tokenizer.tokenize(text)
print(tokens)
```
**OUTPUT :**

```
['un', '##happiness']
```

In this example, "unhappiness" gets split into two subwords: "un" and "##happiness." The “##” symbol indicates that "happiness" is a continuation of the previous word “un.”

### Tokenization in Context (Models, etc.)
In many modern NLP models, tokenization serves as an input to the model. For example:

**BERT:** The input text is first tokenized using WordPiece, which is a form of subword tokenization. The model learns to process tokens to understand language at a contextual level.

**GPT (Generative Pretrained Transformer):** Uses subword tokenization, breaking down text into smaller meaningful pieces that the model learns to predict next-word patterns.

### How Tokenization Helps in NLP Tasks:

- **Machine Translation:** Breaking down text into tokens helps translate more accurately between languages.

- **Sentiment Analysis:** Tokenization enables models to identify individual words or phrases to understand sentiment.

- **Named Entity Recognition (NER):** By tokenizing text, the model can spot entities like names, dates, or locations.

## Why tokenize ? 

- **Easier to map part of speech**: Tokenization breaks text down into smaller units (tokens), which can then be analyzed individually. This makes it easier to map parts of speech (POS) like nouns, verbs, adjectives, etc., because each token represents a potential unit of meaning. The tokenization process helps to identify boundaries between words, which is essential for POS tagging and syntactic analysis.

- **Matching common words** : Tokenization enables the identification and matching of common words (often referred to as "stop words"), such as "the," "is," and "and." Once text is tokenized, we can easily filter out these common words from a text corpus, which can help focus on more meaningful and content-rich words during further processing. It’s also helpful for tasks like building a vocabulary or finding keywords.


- **Removing unwanted tokens** : After tokenizing, it's easier to remove unwanted tokens, such as punctuation, special characters, or irrelevant words. By splitting text into manageable chunks, we can isolate and discard elements that don't contribute to the analysis (e.g., numbers, punctuation, or formatting issues). This step is essential for cleaning data before performing deeper NLP tasks, such as text classification, sentiment analysis, or topic modeling.

In summary, tokenization is key to breaking down text into manageable chunks, helping with tasks like part-of-speech tagging, filtering out unimportant words, and simplifying the overall processing of text.

## We are going to use following libraries

**`sent_tokenize`** : tokenize a documents into sentence.

**`regexp_tokenize`** : tokenize a string or document based on a regular expression pattern

**`TweetTokenizer`** : special class just for tweet tokenization, allowing you to separate hashtags, mentions and lots of exclaimation points!!!

## Regex groups using or "|"

- PR can be represented using `|`
- We can define group using `()`
- We can define explicit character range unsing `[ ]`

````python
import re 

match_words_and_digits = (`\d+|\w+`)
re.findall(match_words_and_digits,'He has 11 cats .')
````

**OUTPUT :**

````
['He', 'has', '11', 'cats']
````

| pattern | matches | example |
|---|---|---|
| `[A-Za-z]+` | upper and lowercase English alphabet | `'ABCDEFghijk'` |
| `[0-9]` | numbers from 0 to 9 | `9` |
| `[A-Za-z\-\.]+` | upper and lowercase English alphabet, `-` and `.` | `'My-Website.com'` |
| `(a-z)` | a, `-` and z | `'a-z'` |
| `(\s+,)` | spaces or a comma | `','` |


### Character range with `re.match()`

````python

import re 

my_str =" match lowercase spaces nums like 12, but no commas" 

print(re.match(r"[a-z0-9 ]+",my_str)) 
````
OUTPUT

````
// <re.Match object; span=(0, 35), match=' match lowercase spaces nums like12'>
````