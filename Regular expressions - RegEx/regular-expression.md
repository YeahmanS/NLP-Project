# Regex in Python: Quick Intro

Regular expressions (regex) are powerful tools used for pattern matching within strings. They allow you to search for, match, and manipulate text in complex ways. Regex uses a sequence of characters that define a search pattern, and this pattern can be used for a variety of tasks like searching for specific text, replacing text, and validating strings (such as email addresses, phone numbers, etc.).

## Regex Symbols Overview

| Symbol | Description                             | Example      | Explanation                                                             |
|--------|-----------------------------------------|--------------|-------------------------------------------------------------------------|
| `\b`   | Word boundary                          | `\bhello\b`  | Matches "hello" only if it's a whole word (surrounded by spaces, punctuation, or start/end of string). |
| `\w`   | Word character (alphanumeric + underscore) | `\w+`        | Matches one or more alphanumeric characters (e.g., letters, numbers, and underscores). |
| `\s`   | Whitespace (spaces, tabs, newlines)     | `\s+`        | Matches one or more whitespace characters.                             |
| `\d`   | Digit                                   | `\d{3}`      | Matches exactly three digits (e.g., "123").                            |
| `.`    | Any character except newline            | `a.b`        | Matches "a" followed by any character and then "b" (e.g., "acb", "a-b"). |
| `+`    | One or more of the previous element     | `\d+`        | Matches one or more digits (e.g., "123", "4567").                      |
| `*`    | Zero or more of the previous element    | `\w*`        | Matches zero or more word characters (e.g., "", "hello", "abc123").     |
| `?`    | Zero or one of the previous element     | `colou?r`    | Matches "color" or "colour".                                           |
| `^`    | Start of the string                     | `^hello`     | Matches "hello" only at the start of the string.                        |
| `$`    | End of the string                       | `world$`     | Matches "world" only at the end of the string.                          |
| `()`   | Grouping                                | `(abc)`      | Groups "abc" as a unit, useful for capturing matches.                   |
| `|`    | OR operator                             | `cat|dog`    | Matches either "cat" or "dog".                                         |


## Examples with Python

### 1. Word Boundaries (`\b`)

```python
import re
text = "Hello world, hello!"
result = re.findall(r'\bhello\b', text, re.IGNORECASE)
print(result)  # ['Hello', 'hello']
```
This matches "hello" as a whole word (case-insensitive).

### 2. Word Characters (`\w`)

```python
text = "hello123 _world"
result = re.findall(r'\w+', text)
print(result)  # ['hello123', '_world']
```
It matches sequences of alphanumeric characters and underscores.

### 3. Whitespace Characters (`\s+`)
```python
text = "Hello   world!"
result = re.findall(r'\s+', text)
print(result)  # ['   ']
```

It matches one or more whitespace characters (spaces in this case).

### 4. Digits (`\d{3}`)
``` python
text = "My number is 123456."
result = re.findall(r'\d{3}', text)
print(result)  # ['123', '456']
```
It matches exactly three consecutive digits.

### 5. Any Character (`.`)
```python
text = "abc xyz"
result = re.findall(r'a.b', text)
print(result)  # ['abc']
It matches "a", any character, and then "b".
```
## More Complex RegEx 

```python
text = "Email: example@example.com, phone: 123-456-7890"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Emails:", emails)  # ['example@example.com']
print("Phones:", phones)  # ['123-456-7890']
```
