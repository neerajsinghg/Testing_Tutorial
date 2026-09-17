class CountCharFreq:
	input="banana"
	freq={}
	for ch in input:
		if ch not in freq:
			freq[ch]=1
		else:
			freq[ch]+=1
	print(freq)

'''
Your code is a very common **Python interview question**: **count how many times each character occurs in a string**.

### Your code

```python
def count_char(input):
    freq = {}

    for ch in input:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    return freq


input = "banana"
print(count_char(input))
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

Let's understand it step by step.

---

# 1. Function definition

```python
def count_char(input):
```

Here we create a function named:

```text
count_char
```

It accepts one argument:

```python
input
```

When we call:

```python
count_char("banana")
```

the value `"banana"` is passed into `input`.

Conceptually:

```text
input = "banana"
```

> **Note:** `input` is also the name of Python's built-in `input()` function. It is better to avoid using `input` as a variable name.

A better version would be:

```python
def count_char(text):
```

---

# 2. Create an empty dictionary

```python
freq = {}
```

This creates an empty dictionary.

Initially:

```text
freq = {}
```

We will use this dictionary to store:

```text
character → count
```

For example:

```python
{
    'a': 3,
    'b': 1,
    'n': 2
}
```

means:

```text
a appears 3 times
b appears 1 time
n appears 2 times
```

---

# 3. Start the `for` loop

```python
for ch in input:
```

The string is:

```text
banana
```

Python processes each character one by one.

The characters are:

```text
b
a
n
a
n
a
```

So the loop executes **6 times**.

You can visualize it like this:

| Iteration | `ch` |
| --------: | :--: |
|         1 |  `b` |
|         2 |  `a` |
|         3 |  `n` |
|         4 |  `a` |
|         5 |  `n` |
|         6 |  `a` |

---

# 4. Check whether character exists

Inside the loop:

```python
if ch not in freq:
```

This checks whether the current character is already present in the dictionary.

For example:

```python
ch = 'b'
freq = {}
```

Python asks:

```text
Is 'b' NOT present in freq?
```

Yes.

Therefore:

```python
if ch not in freq:
```

is `True`.

---

# 5. First character: `b`

Initially:

```python
freq = {}
```

Current character:

```python
ch = 'b'
```

Condition:

```python
if 'b' not in freq:
```

This is true.

Therefore:

```python
freq[ch] = 1
```

becomes:

```python
freq['b'] = 1
```

Dictionary becomes:

```python
freq = {
    'b': 1
}
```

Meaning:

```text
b has occurred 1 time
```

---

# 6. Second character: `a`

Next character:

```python
ch = 'a'
```

Current dictionary:

```python
{'b': 1}
```

Python checks:

```python
if 'a' not in freq:
```

`a` is not present.

So:

```python
freq['a'] = 1
```

Dictionary becomes:

```python
{
    'b': 1,
    'a': 1
}
```

---

# 7. Third character: `n`

Now:

```python
ch = 'n'
```

Current dictionary:

```python
{
    'b': 1,
    'a': 1
}
```

Check:

```python
if 'n' not in freq:
```

`n` does not exist.

So:

```python
freq['n'] = 1
```

Now:

```python
{
    'b': 1,
    'a': 1,
    'n': 1
}
```

---

# 8. Fourth character: `a`

Now we encounter `a` again.

```python
ch = 'a'
```

Current dictionary:

```python
{
    'b': 1,
    'a': 1,
    'n': 1
}
```

Python checks:

```python
if 'a' not in freq:
```

But `a` **already exists**.

Therefore the `if` block is skipped.

Python executes:

```python
else:
    freq[ch] += 1
```

Since:

```python
freq['a'] = 1
```

this:

```python
freq['a'] += 1
```

is equivalent to:

```python
freq['a'] = freq['a'] + 1
```

Therefore:

```text
1 + 1 = 2
```

Dictionary becomes:

```python
{
    'b': 1,
    'a': 2,
    'n': 1
}
```

---

# 9. Fifth character: `n`

Current character:

```python
ch = 'n'
```

`n` already exists:

```python
'n': 1
```

So:

```python
freq['n'] += 1
```

becomes:

```python
freq['n'] = 1 + 1
```

Therefore:

```python
{
    'b': 1,
    'a': 2,
    'n': 2
}
```

---

# 10. Sixth character: `a`

Last character:

```python
ch = 'a'
```

`a` already exists:

```python
'a': 2
```

So:

```python
freq['a'] += 1
```

becomes:

```python
freq['a'] = 2 + 1
```

Therefore:

```python
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

---

# 11. Complete execution table

This is the most important part to understand for an interview.

| Step | `ch` | Is character already in `freq`? | Operation   | `freq`                     |
| ---: | :--: | :-----------------------------: | ----------- | -------------------------- |
|    1 |  `b` |                No               | `b = 1`     | `{'b': 1}`                 |
|    2 |  `a` |                No               | `a = 1`     | `{'b': 1, 'a': 1}`         |
|    3 |  `n` |                No               | `n = 1`     | `{'b': 1, 'a': 1, 'n': 1}` |
|    4 |  `a` |               Yes               | `a = 1 + 1` | `{'b': 1, 'a': 2, 'n': 1}` |
|    5 |  `n` |               Yes               | `n = 1 + 1` | `{'b': 1, 'a': 2, 'n': 2}` |
|    6 |  `a` |               Yes               | `a = 2 + 1` | `{'b': 1, 'a': 3, 'n': 2}` |

Finally:

```python
return freq
```

returns:

```python
{'b': 1, 'a': 3, 'n': 2}
```

Then:

```python
print(count_char(input))
```

prints:

```text
{'b': 1, 'a': 3, 'n': 2}
```

---

# 12. Why do we use a dictionary?

The dictionary is ideal for this problem because it stores data as:

```text
key → value
```

Here:

```text
key   = character
value = frequency
```

For `"banana"`:

```python
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

Think of it like a counter table:

```text
Character     Count
---------     -----
b               1
a               3
n               2
```

---

# 13. Understanding `freq[ch]`

This is important.

Suppose:

```python
ch = 'a'
```

Then:

```python
freq[ch]
```

is the same as:

```python
freq['a']
```

If:

```python
freq = {'a': 2}
```

then:

```python
freq[ch]
```

returns:

```text
2
```

Therefore:

```python
freq[ch] += 1
```

means:

```python
freq['a'] = freq['a'] + 1
```

which gives:

```python
freq['a'] = 2 + 1
```

Result:

```python
{'a': 3}
```

---

# 14. Why can't we simply do this?

You might wonder why we don't write:

```python
for ch in input:
    freq[ch] += 1
```

The problem is that initially `freq` is empty:

```python
freq = {}
```

When Python sees:

```python
freq['b'] += 1
```

it first needs the existing value of:

```python
freq['b']
```

But `b` doesn't exist.

This causes:

```text
KeyError: 'b'
```

That's why we first check:

```python
if ch not in freq:
    freq[ch] = 1
```

If the character is new, we create it with count `1`.

If it already exists:

```python
else:
    freq[ch] += 1
```

we increase its count.

---

# 15. Algorithm in simple English

Your program's logic is:

```text
1. Create an empty dictionary.
2. Read each character from the string.
3. Check whether the character exists in the dictionary.
4. If it doesn't exist:
       Add it with count 1.
5. If it already exists:
       Increase its count by 1.
6. Return the dictionary.
```

In pseudocode:

```text
frequency = empty dictionary

for every character:
    if character is not present:
        frequency[character] = 1
    otherwise:
        frequency[character] = frequency[character] + 1

return frequency
```

---

# 16. Dry run with another example

Suppose:

```python
text = "hello"
```

Characters:

```text
h e l l o
```

Execution:

```text
h → {'h': 1}

e → {'h': 1, 'e': 1}

l → {'h': 1, 'e': 1, 'l': 1}

l → {'h': 1, 'e': 1, 'l': 2}

o → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

Result:

```python
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

# 17. What about spaces?

Your code counts **every character**, including spaces.

For:

```python
text = "hello world"
```

the space is also a character.

You could get something like:

```python
{
    'h': 1,
    'e': 1,
    'l': 3,
    'o': 2,
    ' ': 1,
    'w': 1,
    'r': 1,
    'd': 1
}
```

If you don't want to count spaces:

```python
def count_char(text):
    freq = {}

    for ch in text:
        if ch == " ":
            continue

        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    return freq
```

---

# 18. Case sensitivity

Your current code treats uppercase and lowercase as **different characters**.

For:

```python
text = "Apple"
```

you would get:

```python
{
    'A': 1,
    'p': 2,
    'l': 1,
    'e': 1
}
```

`A` and `a` would be different:

```python
"A" != "a"
```

If you want case-insensitive counting:

```python
def count_char(text):
    freq = {}

    for ch in text.lower():
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    return freq
```

---

# 19. A cleaner version

I would recommend renaming `input` to `text`:

```python
def count_char(text):
    freq = {}

    for ch in text:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1

    return freq


text = "banana"
print(count_char(text))
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

This is exactly the same logic, but `text` is a better variable name.

---

# 20. More Pythonic approach

You can also use `dict.get()`:

```python
def count_char(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    return freq
```

The important part is:

```python
freq.get(ch, 0)
```

If the key exists:

```python
freq.get('a', 0)
```

returns its current value.

If it doesn't exist, it returns:

```text
0
```

So:

```python
freq[ch] = freq.get(ch, 0) + 1
```

works like this for `banana`:

```text
b → 0 + 1 = 1
a → 0 + 1 = 1
n → 0 + 1 = 1
a → 1 + 1 = 2
n → 1 + 1 = 2
a → 2 + 1 = 3
```

Final result:

```python
{'b': 1, 'a': 3, 'n': 2}
```

---

# 21. Using `Counter`

Python also provides:

```python
from collections import Counter

text = "banana"

freq = Counter(text)

print(freq)
```

Output:

```text
Counter({'a': 3, 'n': 2, 'b': 1})
```

But **for an interview**, your original implementation is often better because it demonstrates that you understand:

* dictionaries
* loops
* conditions
* key lookup
* updating dictionary values
* frequency counting
* basic algorithmic thinking

---

# 22. Time and space complexity

For your implementation:

```python
for ch in text:
```

If the string contains `n` characters, we visit every character once.

Therefore:

### Time Complexity

```text
O(n)
```

Because we process each character once.

### Space Complexity

```text
O(k)
```

where `k` is the number of **unique characters**.

For `"banana"`:

```text
n = 6
k = 3
```

because unique characters are:

```text
b, a, n
```

So the dictionary stores only 3 entries.

In the general case, we often simplify the auxiliary space to **O(n)**, since there can be up to `n` distinct characters.

---

# 23. Interview explanation

If an interviewer asks:

> **"Explain your code."**

You can answer:

> "I created a function that counts the frequency of each character in a string. 
I use a dictionary where the character is the key and its occurrence count is the value. 
I iterate through each character of the input string. 
If the character is not already present in the dictionary, I initialize its count to 1. 
If it already exists, I increment its count by 1. Finally, I return the dictionary 
containing the frequency of every character. The time complexity is O(n), and 
the space complexity is O(k), where k is the number of unique characters."

That is a strong **SDET/QA Automation interview-level explanation**.

'''