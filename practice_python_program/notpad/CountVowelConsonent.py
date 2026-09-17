class CountVowelConsonent:
	input="automation"
	vowel=0
	cons = 0
	for ch in input.lower():
		if ch in "aeiou":
			vow += 1
		elif ch.isalpha():
			cons += 1
	print(vowel)
	print(cons)


'''
Absolutely. This is another very common **Python interview question**: **count the number of vowels and consonants in a string**.

### Your code

```python
def count_vow_cons(input):
    vow = 0
    cons = 0

    for ch in input:
        if ch in "aeiou":
            vow += 1
        else:
            cons += 1

    return vow, cons


input = "automation"
print(count_vow_cons(input))
```

Output:

```text
(6, 4)
```

That means:

```text
Vowels     = 6
Consonants = 4
```

Let's understand it step by step.

---

# 1. Function definition

```python
def count_vow_cons(input):
```

Here we define a function called:

```text
count_vow_cons
```

It accepts one argument:

```python
input
```

When we call:

```python
count_vow_cons("automation")
```

the string `"automation"` is passed into the function.

Conceptually:

```python
input = "automation"
```

### Better variable name

As with the previous example, `input` is already the name of Python's built-in `input()` function, so it is better to use:

```python
def count_vow_cons(text):
```

We'll continue explaining your original code.

---

# 2. Initialize vowel counter

```python
vow = 0
```

We create a variable called `vow` to store the number of vowels.

Initially:

```text
vow = 0
```

As we find vowels, we increase it:

```python
vow += 1
```

For example:

```text
0 → 1 → 2 → 3 → ...
```

---

# 3. Initialize consonant counter

```python
cons = 0
```

Similarly, `cons` stores the number of consonants.

Initially:

```text
cons = 0
```

Whenever we find a consonant:

```python
cons += 1
```

the value increases.

---

# 4. Start the `for` loop

```python
for ch in input:
```

Our input is:

```text
automation
```

Let's separate the characters:

```text
a
u
t
o
m
a
t
i
o
n
```

There are **10 characters**.

The loop processes each character one by one.

| Iteration | `ch` |
| --------: | :--: |
|         1 |  `a` |
|         2 |  `u` |
|         3 |  `t` |
|         4 |  `o` |
|         5 |  `m` |
|         6 |  `a` |
|         7 |  `t` |
|         8 |  `i` |
|         9 |  `o` |
|        10 |  `n` |

---

# 5. Check whether the character is a vowel

The main condition is:

```python
if ch in "aeiou":
```

This is asking:

> Is the current character present inside `"aeiou"`?

The string:

```text
"aeiou"
```

contains the five lowercase vowels:

```text
a
e
i
o
u
```

For example:

```python
'a' in "aeiou"
```

returns:

```text
True
```

And:

```python
't' in "aeiou"
```

returns:

```text
False
```

So this condition determines whether the current character is considered a vowel.

---

# 6. If it is a vowel

If this condition is true:

```python
if ch in "aeiou":
```

we execute:

```python
vow += 1
```

This is shorthand for:

```python
vow = vow + 1
```

For example, if:

```text
vow = 2
```

then:

```python
vow += 1
```

changes it to:

```text
vow = 3
```

---

# 7. If it is not a vowel

The `else` block is:

```python
else:
    cons += 1
```

This means:

> If the character is not one of `a, e, i, o, u`, count it as a consonant.

For example:

```text
t
m
n
```

are not in `"aeiou"`.

Therefore:

```python
cons += 1
```

is executed.

---

# 8. Complete dry run

Now let's process:

```text
automation
```

Character by character.

### Iteration 1

```text
ch = 'a'
```

Check:

```python
'a' in "aeiou"
```

Result:

```text
True
```

Therefore:

```python
vow += 1
```

Counters:

```text
vow  = 1
cons = 0
```

---

### Iteration 2

```text
ch = 'u'
```

Check:

```python
'u' in "aeiou"
```

Result:

```text
True
```

Therefore:

```text
vow = 2
cons = 0
```

---

### Iteration 3

```text
ch = 't'
```

Check:

```python
't' in "aeiou"
```

Result:

```text
False
```

Therefore:

```python
cons += 1
```

Counters:

```text
vow  = 2
cons = 1
```

---

### Iteration 4

```text
ch = 'o'
```

`o` is a vowel.

```text
vow  = 3
cons = 1
```

---

### Iteration 5

```text
ch = 'm'
```

`m` is not a vowel.

```text
vow  = 3
cons = 2
```

---

### Iteration 6

```text
ch = 'a'
```

`a` is a vowel.

```text
vow  = 4
cons = 2
```

---

### Iteration 7

```text
ch = 't'
```

`t` is a consonant.

```text
vow  = 4
cons = 3
```

---

### Iteration 8

```text
ch = 'i'
```

`i` is a vowel.

```text
vow  = 5
cons = 3
```

---

### Iteration 9

```text
ch = 'o'
```

`o` is a vowel.

```text
vow  = 6
cons = 3
```

---

### Iteration 10

```text
ch = 'n'
```

`n` is a consonant.

```text
vow  = 6
cons = 4
```

---

# 9. Complete execution table

This table is especially useful for interview preparation.

| Step | Character | `ch in "aeiou"` | Action      | Vowels | Consonants |
| ---: | :-------: | :-------------: | ----------- | -----: | ---------: |
|    1 |    `a`    |       True      | `vow += 1`  |      1 |          0 |
|    2 |    `u`    |       True      | `vow += 1`  |      2 |          0 |
|    3 |    `t`    |      False      | `cons += 1` |      2 |          1 |
|    4 |    `o`    |       True      | `vow += 1`  |      3 |          1 |
|    5 |    `m`    |      False      | `cons += 1` |      3 |          2 |
|    6 |    `a`    |       True      | `vow += 1`  |      4 |          2 |
|    7 |    `t`    |      False      | `cons += 1` |      4 |          3 |
|    8 |    `i`    |       True      | `vow += 1`  |      5 |          3 |
|    9 |    `o`    |       True      | `vow += 1`  |      6 |          3 |
|   10 |    `n`    |      False      | `cons += 1` |      6 |          4 |

Final values:

```text
vow  = 6
cons = 4
```

---

# 10. Understanding `return vow, cons`

At the end:

```python
return vow, cons
```

This returns **two values**.

Python actually returns them as a tuple:

```python
(6, 4)
```

So:

```python
result = count_vow_cons("automation")
```

would give:

```python
result = (6, 4)
```

You can also unpack them:

```python
vowels, consonants = count_vow_cons("automation")

print(vowels)
print(consonants)
```

Output:

```text
6
4
```

This is called **tuple unpacking**.

---

# 11. How the `print()` works

Your code:

```python
print(count_vow_cons(input))
```

First Python executes:

```python
count_vow_cons(input)
```

The function returns:

```python
(6, 4)
```

Then `print()` prints that returned tuple:

```text
(6, 4)
```

So the flow is:

```text
input
  ↓
"automation"
  ↓
count_vow_cons()
  ↓
loop through every character
  ↓
count vowels and consonants
  ↓
return (6, 4)
  ↓
print()
  ↓
(6, 4)
```

---

# 12. Why are `vow` and `cons` initialized to 0?

This is very important.

We are creating counters.

Before processing anything:

```python
vow = 0
cons = 0
```

There are no characters processed yet.

So both counters start at zero.

When a vowel is found:

```python
vow += 1
```

When a consonant is found:

```python
cons += 1
```

It's essentially like maintaining two scoreboards:

```text
Vowel counter       Consonant counter
-------------       -----------------
     0                     0
     ↓                     ↓
    +1                    +1
     ↓                     ↓
    +1                    +1
```

---

# 13. Important issue in your code

Your code assumes:

> Every character that isn't a vowel is a consonant.

That's not always correct.

For example:

```python
text = "hello world!"
```

Characters include:

```text
h e l l o [space] w o r l d !
```

Your code would count:

```text
space → consonant
!     → consonant
```

which is logically incorrect.

Similarly, numbers:

```text
"abc123"
```

would cause:

```text
1 → consonant
2 → consonant
3 → consonant
```

That's not correct either.

---

# 14. Better implementation

A more robust solution is:

```python
def count_vow_cons(text):
    vow = 0
    cons = 0

    for ch in text.lower():
        if ch in "aeiou":
            vow += 1
        elif ch.isalpha():
            cons += 1

    return vow, cons


text = "automation"
print(count_vow_cons(text))
```

Output:

```text
(6, 4)
```

The important addition is:

```python
elif ch.isalpha():
```

This ensures that only alphabetic characters are counted as consonants.

---

# 15. Why use `.lower()`?

Suppose the input is:

```text
"Automation"
```

The first character is:

```text
A
```

But your vowel string contains lowercase:

```text
"aeiou"
```

Therefore:

```python
'A' in "aeiou"
```

returns:

```text
False
```

That's a problem.

So we can use:

```python
text.lower()
```

which converts:

```text
Automation
```

into:

```text
automation
```

Now:

```python
'a' in "aeiou"
```

returns:

```text
True
```

This makes the function **case-insensitive**.

---

# 16. What does `isalpha()` do?

```python
ch.isalpha()
```

checks whether the character is an alphabetic letter.

Examples:

```python
'a'.isalpha()      # True
'Z'.isalpha()      # True
'5'.isalpha()      # False
'!'.isalpha()      # False
' '.isalpha()      # False
```

Therefore:

```python
elif ch.isalpha():
    cons += 1
```

means:

> If it isn't a vowel, but it is a letter, count it as a consonant.

---

# 17. Difference between your code and robust code

### Your version

```python
if ch in "aeiou":
    vow += 1
else:
    cons += 1
```

Logic:

```text
Vowel → vowel
Everything else → consonant
```

### Better version

```python
if ch in "aeiou":
    vow += 1
elif ch.isalpha():
    cons += 1
```

Logic:

```text
Vowel → vowel
Letter but not vowel → consonant
Number/symbol/space → ignore
```

For interview purposes, the second approach is more robust.

---

# 18. Example with spaces and numbers

Consider:

```python
text = "hello 123!"
```

Using your original code:

```text
h → consonant
e → vowel
l → consonant
l → consonant
o → vowel
space → consonant ❌
1 → consonant ❌
2 → consonant ❌
3 → consonant ❌
! → consonant ❌
```

That's incorrect.

Using the improved version:

```python
def count_vow_cons(text):
    vow = 0
    cons = 0

    for ch in text.lower():
        if ch in "aeiou":
            vow += 1
        elif ch.isalpha():
            cons += 1

    return vow, cons
```

We get:

```text
Vowels     = 2
Consonants = 3
```

because:

```text
h e l l o
↑ ↑ ↑ ↑ ↑
C V C C V
```

Numbers, spaces and `!` are ignored.

---

# 19. Time complexity

The loop:

```python
for ch in input:
```

visits every character once.

If the input contains `n` characters:

### Time Complexity

```text
O(n)
```

Why?

Because every character is processed exactly once.

For:

```text
automation
```

we process:

```text
10 characters
```

For:

```text
abcdefghijklmnopqrstuvwxyz
```

we process:

```text
26 characters
```

There is no nested loop.

Therefore:

```text
Time = O(n)
```

---

# 20. Space complexity

We only create two integer variables:

```python
vow
cons
```

We don't create another data structure proportional to the input.

Therefore auxiliary space is:

```text
O(1)
```

This is an important difference from your previous **character-frequency dictionary** problem.

### Character frequency

```text
Space = O(k)
```

### Vowel/consonant counter

```text
Space = O(1)
```

because we only maintain two counters.

---

# 21. Interview answer

If the interviewer asks:

> **"Explain your code."**

You can say:

> "I created a function to count vowels and consonants in a given string. I initialized two counters, `vow` and `cons`, to zero. Then I iterate through each character using a `for` loop. If the character exists in the string `aeiou`, I increment the vowel counter. Otherwise, I increment the consonant counter. Finally, I return both values as a tuple. The time complexity is O(n), because every character is processed once, and the space complexity is O(1), because I only use two counters."

For a **more robust production version**, mention:

> "I would additionally convert the input to lowercase and use `isalpha()` so that spaces, numbers, and special characters aren't incorrectly counted as consonants."

That distinction is a good point to mention in a **6–10 year SDET/Python interview**, because it shows you're thinking beyond just making the sample input pass.

'''