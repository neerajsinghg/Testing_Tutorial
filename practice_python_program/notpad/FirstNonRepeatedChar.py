class FirstNonRepeatedChar:
	def first_non_repeated(text):
		freq = {}

		for ch in text:
			if ch != " ":
				freq[ch] = freq.get(ch, 0) + 1

		for ch in text:
			if ch != " " and freq[ch] == 1:
				return ch

		return None
	
	text = "swiisst"
	print(first_non_repeated(text))


'''
Yes. For:

```python
input = "swwiisst"
```

you want to find the **first non-repeated (first unique) character**.

Let's first understand the expected answer, then I'll show you several approaches from **basic → Pythonic → interview-friendly**.

## 1. Understand the input

```text
s w w i i s s t
```

Character frequencies are:

```text
s → 3
w → 2
i → 2
t → 1
```

Therefore:

```text
First non-repeated character = t
```

The important point is that we need the **first character whose frequency is exactly 1**, not simply the first unique character we encounter.

---

# Approach 1 — Nested loops / `count()`

This is probably the easiest approach to understand.

```python
input = "swwiisst"

for ch in input:
    if input.count(ch) == 1:
        print(ch)
        break
```

Output:

```text
t
```

### How it works

The loop processes:

```text
s
w
w
i
i
s
s
t
```

For each character, we use:

```python
input.count(ch)
```

to count how many times that character occurs.

### Step 1

```python
ch = 's'
```

Check:

```python
input.count('s')
```

Result:

```text
3
```

So:

```python
3 == 1
```

is `False`.

Continue.

### Step 2

```python
ch = 'w'
```

```python
input.count('w')
```

Result:

```text
2
```

Not unique.

Continue.

### Step 3

Again:

```python
ch = 'w'
```

Count is still:

```text
2
```

Continue.

### Step 4

```python
ch = 'i'
```

Count:

```text
2
```

Continue.

### Step 5

Again:

```python
ch = 'i'
```

Count:

```text
2
```

Continue.

### Step 6

```python
ch = 's'
```

Count:

```text
3
```

Continue.

### Step 7

```python
ch = 's'
```

Count:

```text
3
```

Continue.

### Step 8

```python
ch = 't'
```

Count:

```python
input.count('t')
```

Result:

```text
1
```

Therefore:

```python
if input.count(ch) == 1:
```

is `True`.

We execute:

```python
print(ch)
```

Output:

```text
t
```

Then:

```python
break
```

stops the loop.

---

# Approach 2 — Using a dictionary

This is one of the **best approaches for interviews** because it demonstrates your understanding of dictionaries and frequency counting.

```python
input = "swwiisst"

freq = {}

for ch in input:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

for ch in input:
    if freq[ch] == 1:
        print(ch)
        break
```

Output:

```text
t
```

There are **two loops**, and each has a separate responsibility.

### First loop

Build the frequency dictionary.

### Second loop

Find the first character whose frequency is `1`.

---

## Step 1 — Build frequency dictionary

Initially:

```python
freq = {}
```

Process `s`:

```text
s → 1
```

Dictionary:

```python
{'s': 1}
```

Process first `w`:

```python
{'s': 1, 'w': 1}
```

Process second `w`:

```python
{'s': 1, 'w': 2}
```

Process first `i`:

```python
{'s': 1, 'w': 2, 'i': 1}
```

Process second `i`:

```python
{'s': 1, 'w': 2, 'i': 2}
```

Process second `s`:

```python
{'s': 2, 'w': 2, 'i': 2}
```

Process third `s`:

```python
{'s': 3, 'w': 2, 'i': 2}
```

Finally `t`:

```python
{'s': 3, 'w': 2, 'i': 2, 't': 1}
```

So:

```text
s → 3
w → 2
i → 2
t → 1
```

---

## Step 2 — Find first unique character

Now we loop through the **original string again**:

```python
for ch in input:
```

Why the original string?

Because we need to preserve the original order.

First:

```text
s
```

Check:

```python
freq['s'] == 1
```

But:

```text
freq['s'] = 3
```

No.

Next:

```text
w
```

```text
freq['w'] = 2
```

No.

Next:

```text
w
```

Still 2.

Next:

```text
i
```

2.

Next:

```text
i
```

2.

Next:

```text
s
```

3.

Next:

```text
s
```

3.

Finally:

```text
t
```

```text
freq['t'] = 1
```

Therefore:

```python
if freq[ch] == 1:
```

is true.

We print:

```text
t
```

and stop using:

```python
break
```

---

# Approach 3 — Using `dict.get()`

We can make the frequency-counting part cleaner:

```python
input = "swwiisst"

freq = {}

for ch in input:
    freq[ch] = freq.get(ch, 0) + 1

for ch in input:
    if freq[ch] == 1:
        print(ch)
        break
```

This is a very good Python approach.

The important statement is:

```python
freq[ch] = freq.get(ch, 0) + 1
```

Let's understand it.

For the first character:

```text
ch = 's'
```

`freq` is empty.

```python
freq.get('s', 0)
```

returns:

```text
0
```

Then:

```text
0 + 1 = 1
```

So:

```python
freq['s'] = 1
```

Next `w`:

```text
0 + 1 = 1
```

Next `w` again:

```text
1 + 1 = 2
```

And so on.

Final dictionary:

```python
{
    's': 3,
    'w': 2,
    'i': 2,
    't': 1
}
```

Then we find the first key in the original string with frequency `1`.

Answer:

```text
t
```

---

# Approach 4 — Using `collections.Counter`

Python has a built-in frequency counter:

```python
from collections import Counter

input = "swwiisst"

freq = Counter(input)

for ch in input:
    if freq[ch] == 1:
        print(ch)
        break
```

Output:

```text
t
```

`Counter` produces:

```python
Counter({
    's': 3,
    'w': 2,
    'i': 2,
    't': 1
})
```

Then:

```python
freq[ch] == 1
```

identifies the unique character.

---

# Approach 5 — Using a function

For automation/interview coding, I'd recommend putting the logic inside a function:

```python
def first_non_repeated(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


text = "swwiisst"

print(first_non_repeated(text))
```

Output:

```text
t
```

This is better than directly printing inside the function because the function **returns the answer**.

You can then use the result anywhere:

```python
result = first_non_repeated("swwiisst")

print(result)
```

---

# Why do we use two loops?

This is a very important interview concept.

You might ask:

> Why not find the character while creating the dictionary?

Because we need to know the **final frequency** of each character.

For example:

```text
swwiisst
```

When we initially see:

```text
s
```

we don't yet know that `s` will appear 3 times.

Similarly, when we first see:

```text
t
```

we can suspect it is unique, but frequency counting should be completed before making the final decision.

Therefore:

```text
First loop
    ↓
Count every character
    ↓
Frequency dictionary
    ↓
Second loop
    ↓
Preserve original order
    ↓
Find first frequency == 1
```

---

# Why can't we just iterate over the dictionary?

Suppose we have:

```python
freq = {
    's': 3,
    'w': 2,
    'i': 2,
    't': 1
}
```

We could technically do:

```python
for ch in freq:
    if freq[ch] == 1:
        print(ch)
        break
```

This will also give:

```text
t
```

because modern Python dictionaries preserve insertion order.

However, for explaining the algorithm, I prefer:

```python
for ch in text:
```

because the requirement is explicitly:

> **first non-repeated character in the original string**

The second loop over `text` makes that intent very clear.

---

# Approach 6 — Find all non-repeated characters

There is a difference between:

### First non-repeated

```text
t
```

and:

### All non-repeated

For:

```text
swwiisst
```

only:

```text
t
```

is non-repeated.

But consider:

```python
text = "swissabc"
```

Frequencies:

```text
s → 2
w → 1
i → 1
a → 1
b → 1
c → 1
```

All non-repeated characters are:

```text
w i a b c
```

But the **first** non-repeated character is:

```text
w
```

So the word **first** is important.

---

# Approach 7 — What if there is no non-repeated character?

Consider:

```python
text = "aabbcc"
```

Every character repeats.

A good function should return `None`:

```python
def first_non_repeated(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None
```

Then:

```python
print(first_non_repeated("aabbcc"))
```

Output:

```text
None
```

You can also return a message:

```python
return "No non-repeated character"
```

but returning `None` is generally cleaner for reusable code.

---

# Approach 8 — Case-insensitive version

Suppose:

```python
text = "aAbbc"
```

If you want `A` and `a` to be treated as the same character:

```python
def first_non_repeated(text):
    text = text.lower()

    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


print(first_non_repeated("aAbbc"))
```

Output:

```text
c
```

because after converting:

```text
aAbbc
```

to:

```text
aabbc
```

we have:

```text
a → 2
b → 2
c → 1
```

---

# Approach comparison

| Approach     | Code complexity |  Time | Space | Interview value   |
| ------------ | --------------- | ----: | ----: | ----------------- |
| `count()`    | Very easy       | O(n²) |  O(1) | Good for beginner |
| Dictionary   | Easy            |  O(n) |  O(k) | ⭐⭐⭐⭐⭐             |
| `dict.get()` | Easy            |  O(n) |  O(k) | ⭐⭐⭐⭐⭐             |
| `Counter`    | Very easy       |  O(n) |  O(k) | ⭐⭐⭐⭐              |
| Nested loops | Easy            | O(n²) |  O(1) | ⭐⭐⭐               |

Where:

```text
n = length of string
k = number of unique characters
```

---

# ⭐ Best interview solution

For your Python/SDET interview preparation, I would use this:

```python
def first_non_repeated(text):
    freq = {}

    # Step 1: Count frequency
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Find first character with frequency 1
    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


text = "swwiisst"
print(first_non_repeated(text))
```

Output:

```text
t
```

### Interview explanation

> "I use a two-pass approach. In the first pass, I create a frequency dictionary and count how many times each character occurs. In the second pass, I iterate over the original string to maintain the original order and return the first character whose frequency is exactly one. If no such character exists, I return `None`. The time complexity is O(n) because I traverse the string twice, which is still O(n), and the space complexity is O(k), where k is the number of unique characters."

### One key point to remember

```text
First pass  → COUNT
Second pass → FIND
```

For:

```text
s w w i i s s t
```

the count is:

```text
s = 3
w = 2
i = 2
t = 1
```

Therefore:

```text
s ❌
w ❌
w ❌
i ❌
i ❌
s ❌
s ❌
t ✅  ← first non-repeated
```

**Answer = `t`**.
'''

	
	