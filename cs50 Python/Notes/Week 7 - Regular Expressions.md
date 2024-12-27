## re Library
- Allows you to define and check for patterns using regex
- `re.search(pattern, string, flags=0)`
	- Pattern is the pattern you want to search for
	- String is the string you are checking the pattern for
	- Flags are optional to modify the behavior of the function
```
import re

email = input("What's your email? ").strip()

if re.search("@", email):
	print("Valid")
else:
	print("Invalid")
```
## Regular Expression Patterns
- Special symbols
	- `.` -  any character except a newline
	- `*` - 0 or more repetitions
	- `+` -  1 or more repetition
	- `?` - 0 or 1 repetition (i.e. optional)
	- `{m}` - m repetitions
	- `{m-n}` - m-n repetitions
```
import re

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
	print("Valid")
else:
	print("Invalid")
```
- `.*@.*` -  tells the function that you want a string that has at least some chars to the left and some to the right. But `*` means 0 repetitions so a `.+@.+` should be used:
```
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
	print("Valid")
else:
	print("Invalid")
```
- Equivalent to `.+@.+` would be `..*@..*`
```
import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
	print("Valid")
else:
	print("Invalid")
```
- Adding `\.edu` with the `r` at the beginning of the string treats the pattern string as a raw-string and lets you search for a string that will end with ".edu"
## Matching Start and End
- Symbols
	- `^` - matches the start of the string
	- `$` -  matches the end of the string or just before the newline at the end of the string
```
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
	print("Valid")
else:
	print("Invalid")
```
## Sets of Character
- Symbols
	- `[]` - set of characters
	- `[^]` - complementing the set
```
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
	print("Valid")
else:
	print("Invalid")
```
- This expression now is matching a pattern where it begins with any characters except an "@" symbol and is followed by any characters except an "@" symbol and ends with ".edu" similarly you can do this:
```
import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
	print("Valid")
else:
	print("Invalid")
```
## Character Classes
- Symbols
	- `\d` - decimal digit
	- `\D` - not a decimal digit
	- `\s` - whitespace characters
	- `\S` - not a whitespace character
	- `\w` - word character ... as well as numbers and the underscore
	- `\W` - not a word character
```
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email. re.IGNORECASE):
	print("Valid")
else:
	print("Invalid")
```
## Flags
- Flags you can pass:
	- `re.IGNORECASE` - search will ignore case of user's input
	- `re.MULTILINE` - handle user's input that is multiple lines
	- `re.DOTALL` - configure the `.` character as any character INCLUDING a newline
```
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email. re.IGNORECASE):
	print("Valid")
else:
	print("Invalid")
```
## Groups
- Symbols
	- `A|B` - either A or B
	- `(...)` - a group
	- `(?:...)` - non-capturing version
	- 
```
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email. re.IGNORECASE):
	print("Valid")
else:
	print("Invalid")
```
- Above now will allow you to have an optional sub-domain included with the email address with this block `(\w+\.)?`
## match, fullmatch
- `re.match(pattern, string, flags=0)` - like search but you do not have to specify the carrot ("^") symbol at the very beginning 
- `re.fullmatch(pattern, string, flags=0)` - you do not have to include the carrot ("^") or dollar sign symbols ("$")
## format.py
```
name = input("What is your name? ").strip()

if "," in name:
	last, first = name.split(", ")
	name = f"{first} {last}"
	
print(f"hello, {name}")
```
## Capturing Groups
```
import re

name = input("What is your name? ").strip()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
	name = matches.groups(2)} + " " +  {matches.groups(1)}
print(f"hello, {name}")
```
- Using parentheses will return to you as a return value from the function. It allows you to extract information from the user's input. Anything in parentheses will be returned in that order
## Walrus Operator
- `:=` - allows you to assign a value AND ask a boolean question about it
```
import re

name = input("What is your name? ").strip()

if matches :=  re.search(r"^(.+), (.+)$", name)
	name = matches.groups(2)} + " " +  {matches.groups(1)}
print(f"hello, {name}")
```
## Extracting from Strings
- `re.replace(what_you_want_to_replace, what_you_want_to_replace_it_with)` - allows you to do a find and replace
```
import re

url = input("URL: ").strip()

username = re.replace("https://twitter.com/", "")

print(f("Username: {username}))
```
- `re.removeprefix()` - like replace but removes something from the beginning of the string
```
import re

url = input("URL: ").strip()

username = re.replace("https://twitter.com/", "")

print(f("Username: {username}))
```
## re.sub
- `re.sub(pattern, repl, string, count=0, flags=0)`
	- Pattern is the regex you want to look for
	- Repl or replacement string, what you want to replace the pattern with
	- String what you want to perform the regex on
```
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f("Username: {username}))
```
## re.search
```
import re

url = input("URL: ").strip()

matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
	print(f("Username: {matches.group(1)}))
```