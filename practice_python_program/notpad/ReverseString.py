class ReverseString:
	#id="w1ed8mp"
	#rev=""
	#for i in range(len(id)-1,-1,-1):
	#	rev+=id[i]
	#print(rev)


	id="w1ed8mp"
	ch=list(id)
	start=0
	end=len(id)-1
	while(start<end):
		ch[start],ch[end]=ch[end],ch[start]
		start+=1
		end-=1
	print("".join(ch))


'''
Absolutely. This code reverses a string **without using Python's built-in `reversed()` or slicing**. It is a very common Python interview question.

## Your code

```python
def rev_string(input):
    rev = ""

    for ch in range(len(input)-1, -1, -1):
        rev += input[ch]

    return rev


input = "swwiisst"
print(rev_string(input))
```

### Output

```text
tssiiwws
```

Let's understand every part in detail.

---

# 1. What is the objective?

Your input is:

```text
s w w i i s s t
```

You want to reverse it:

```text
t s s i i w w s
```

So:

```text
Original  → swwiisst
Reverse   → tssiiwws
```

---

# 2. Function definition

```python
def rev_string(input):
```

This creates a function named:

```text
rev_string
```

It accepts one parameter:

```text
input
```

When you call:

```python
rev_string("swwiisst")
```

inside the function:

```python
input = "swwiisst"
```

### Better variable name

You should preferably avoid:

```python
input
```

because `input()` is already a Python built-in function.

Better:

```python
def rev_string(text):
```

We'll continue with your original code for explanation.

---

# 3. Create an empty string

```python
rev = ""
```

This variable will store the reversed string.

Initially:

```text
rev = ""
```

As we process characters, we add them to `rev`.

For example:

```text
rev = ""
rev = "t"
rev = "ts"
rev = "tss"
...
```

Eventually:

```text
rev = "tssiiwws"
```

---

# 4. The most important line

This is the key part:

```python
for ch in range(len(input)-1, -1, -1):
```

This line looks complicated initially, so let's break it into pieces.

It contains:

```text
range(start, stop, step)
```

Here:

```python
range(len(input)-1, -1, -1)
```

means:

```text
start = len(input) - 1
stop  = -1
step  = -1
```

---

# 5. Understand `len(input)`

Your input is:

```text
swwiisst
```

Count the characters:

```text
s w w i i s s t
1 2 3 4 5 6 7 8
```

Therefore:

```python
len(input)
```

returns:

```text
8
```

So:

```python
len(input) - 1
```

becomes:

```text
8 - 1 = 7
```

Therefore your range becomes:

```python
range(7, -1, -1)
```

---

# 6. Why does it start from 7?

Python string indexing starts from **0**, not 1.

For:

```text
swwiisst
```

the indexes are:

| Character | Index |
| :-------: | ----: |
|    `s`    |     0 |
|    `w`    |     1 |
|    `w`    |     2 |
|    `i`    |     3 |
|    `i`    |     4 |
|    `s`    |     5 |
|    `s`    |     6 |
|    `t`    |     7 |

So:

```text
First character = index 0
Last character  = index 7
```

That's why we start at:

```python
len(input) - 1
```

which is:

```text
7
```

---

# 7. Understand `range(7, -1, -1)`

Now we have:

```python
range(7, -1, -1)
```

Remember:

```text
range(start, stop, step)
```

So:

```text
start = 7
stop  = -1
step  = -1
```

Because the step is `-1`, we move backward:

```text
7
6
5
4
3
2
1
0
```

### Why doesn't it include `-1`?

Python's `range()` excludes the `stop` value.

So:

```python
range(7, -1, -1)
```

produces:

```text
7, 6, 5, 4, 3, 2, 1, 0
```

It does **not** actually produce `-1`.

This is exactly what we need because the valid string indexes are:

```text
0 through 7
```

---

# 8. What is `ch` actually storing?

This is a small but important point.

You wrote:

```python
for ch in range(len(input)-1, -1, -1):
```

Here `ch` is actually an **index**, not a character.

For example:

```text
ch = 7
ch = 6
ch = 5
...
```

You could name it:

```python
for index in range(len(input)-1, -1, -1):
```

which is clearer.

Then:

```python
rev += input[ch]
```

means:

> Get the character from `input` at the current index and add it to `rev`.

---

# 9. First iteration

Input:

```text
swwiisst
```

First index:

```text
ch = 7
```

Therefore:

```python
input[ch]
```

means:

```python
input[7]
```

Index `7` contains:

```text
t
```

So:

```python
rev += input[ch]
```

becomes:

```python
rev += "t"
```

Initially:

```text
rev = ""
```

After adding `t`:

```text
rev = "t"
```

---

# 10. Second iteration

Next value:

```text
ch = 6
```

So:

```python
input[6]
```

is:

```text
s
```

Therefore:

```python
rev += "s"
```

Current value:

```text
rev = "t"
```

After adding `s`:

```text
rev = "ts"
```

---

# 11. Third iteration

Now:

```text
ch = 5
```

```python
input[5]
```

is:

```text
s
```

So:

```text
rev = "tss"
```

---

# 12. Fourth iteration

```text
ch = 4
```

```python
input[4]
```

is:

```text
i
```

So:

```text
rev = "tssi"
```

---

# 13. Fifth iteration

```text
ch = 3
```

```python
input[3]
```

is:

```text
i
```

So:

```text
rev = "tssii"
```

---

# 14. Sixth iteration

```text
ch = 2
```

```python
input[2]
```

is:

```text
w
```

So:

```text
rev = "tssiiw"
```

---

# 15. Seventh iteration

```text
ch = 1
```

```python
input[1]
```

is:

```text
w
```

So:

```text
rev = "tssiiww"
```

---

# 16. Eighth iteration

```text
ch = 0
```

```python
input[0]
```

is:

```text
s
```

So:

```text
rev = "tssiiwws"
```

Now the loop finishes.

---

# 17. Complete dry run

This table is very useful for interviews:

| Iteration | `ch` / index | `input[ch]` | `rev`        |
| --------: | -----------: | :---------: | :----------- |
|         1 |            7 |     `t`     | `"t"`        |
|         2 |            6 |     `s`     | `"ts"`       |
|         3 |            5 |     `s`     | `"tss"`      |
|         4 |            4 |     `i`     | `"tssi"`     |
|         5 |            3 |     `i`     | `"tssii"`    |
|         6 |            2 |     `w`     | `"tssiiw"`   |
|         7 |            1 |     `w`     | `"tssiiww"`  |
|         8 |            0 |     `s`     | `"tssiiwws"` |

Final:

```text
tssiiwws
```

---

# 18. Understanding `rev += input[ch]`

This statement:

```python
rev += input[ch]
```

is shorthand for:

```python
rev = rev + input[ch]
```

For example:

```python
rev = "tssiiw"
input[ch] = "w"
```

Then:

```python
rev = "tssiiw" + "w"
```

becomes:

```text
tssiiww
```

This continues until every character has been added.

---

# 19. Understanding `return rev`

At the end:

```python
return rev
```

The function returns:

```text
tssiiwws
```

So:

```python
print(rev_string(input))
```

is effectively:

```python
result = rev_string(input)
print(result)
```

The output is:

```text
tssiiwws
```

---

# 20. Complete flow

You can remember the program like this:

```text
Input
  ↓
"swwiisst"
  ↓
Find last index
  ↓
len(input) - 1 = 7
  ↓
Generate indexes backward
  ↓
7 6 5 4 3 2 1 0
  ↓
Read characters
  ↓
t s s i i w w s
  ↓
Build rev
  ↓
"tssiiwws"
  ↓
return
```

---

# 21. Why do we use `len(input)-1`?

This is one of the most common interview questions.

Suppose:

```python
text = "hello"
```

Length:

```text
5
```

Indexes:

```text
h → 0
e → 1
l → 2
l → 3
o → 4
```

The last index is:

```text
length - 1
```

Therefore:

```python
len(text) - 1
```

is:

```text
5 - 1 = 4
```

So to reverse a string using indexes, we start from:

```python
4
```

not:

```python
5
```

If you tried:

```python
text[5]
```

you would get:

```text
IndexError: string index out of range
```

---

# 22. Why is the step `-1`?

Normally:

```python
range(0, 5, 1)
```

moves forward:

```text
0 1 2 3 4
```

But we want to reverse the string, so we need to move backward:

```python
range(4, -1, -1)
```

which gives:

```text
4 3 2 1 0
```

Therefore:

```text
+1 → forward
-1 → backward
```

---

# 23. Approach 2 — Using slicing

Python provides a much simpler way:

```python
text = "swwiisst"

rev = text[::-1]

print(rev)
```

Output:

```text
tssiiwws
```

The syntax:

```python
text[start:stop:step]
```

Here:

```python
text[::-1]
```

means:

```text
start = default
stop  = default
step  = -1
```

So Python traverses the string backward.

### Interview note

If the interviewer asks:

> "How would you reverse a string in Python?"

You can mention:

```python
text[::-1]
```

But if they specifically say:

> "Don't use slicing."

then your original loop approach is excellent.

---

# 24. Approach 3 — Using `reversed()`

Another Python approach:

```python
text = "swwiisst"

rev = ""

for ch in reversed(text):
    rev += ch

print(rev)
```

Output:

```text
tssiiwws
```

Here:

```python
reversed(text)
```

returns the characters from right to left.

---

# 25. Approach 4 — Using `join()`

A more Pythonic version:

```python
text = "swwiisst"

rev = "".join(reversed(text))

print(rev)
```

Output:

```text
tssiiwws
```

---

# 26. Comparing the approaches

| Approach                | Example                    | Interview value |
| ----------------------- | -------------------------- | --------------- |
| Reverse loop            | `range(len(text)-1,-1,-1)` | ⭐⭐⭐⭐⭐           |
| Slicing                 | `text[::-1]`               | ⭐⭐⭐⭐⭐           |
| `reversed()`            | `reversed(text)`           | ⭐⭐⭐⭐            |
| `join()` + `reversed()` | `"".join(reversed(text))`  | ⭐⭐⭐⭐            |

For a coding interview, I would know **all four**, but understand the first one deeply because it demonstrates your knowledge of:

* `len()`
* indexes
* `range()`
* negative step
* string indexing
* loops
* string concatenation
* `return`

---

# 27. Important correction to your variable name

I would rewrite your code as:

```python
def rev_string(text):
    rev = ""

    for index in range(len(text) - 1, -1, -1):
        rev += text[index]

    return rev


text = "swwiisst"
print(rev_string(text))
```

Output:

```text
tssiiwws
```

This is clearer because `index` actually represents an index.

---

# 28. Time complexity

Your algorithm processes every character once:

```python
for index in range(len(text) - 1, -1, -1):
```

If the string has `n` characters, the loop executes `n` times.

So we generally describe the algorithm as:

```text
Time Complexity: O(n)
```

### Space complexity

You create:

```python
rev = ""
```

which stores the reversed string.

Therefore the output itself requires:

```text
O(n)
```

space.

For interview purposes:

```text
Time  = O(n)
Space = O(n)
```

because the reversed string is stored in `rev`.

> A subtle Python detail: repeated `+=` string concatenation can have implementation-dependent performance characteristics. For practical interview discussion, `O(n)` is the standard expected answer for this simple solution; if optimizing construction, `list` + `''.join()` is preferable.

---

# 29. Interview explanation

If the interviewer asks:

> **"Explain your reverse string program."**

You can answer:

> "I initialize an empty string called `rev`. Then I iterate over the input string from the last index to the first index using `range(len(text)-1, -1, -1)`. The starting index is `len(text)-1` because Python uses zero-based indexing, and the step `-1` moves from right to left. During each iteration, I access the character using `text[index]` and append it to `rev`. After processing all characters, I return the reversed string. For an input of `swwiisst`, the output is `tssiiwws`. The time complexity is O(n) and the output space is O(n)."

### The key concept to remember

```text
len(text) - 1 → last index
-1             → move backward
text[index]    → get character
rev +=         → build reversed string
return rev     → return final result
```

For your input:

```text
s w w i i s s t
0 1 2 3 4 5 6 7
              ↓
7 6 5 4 3 2 1 0
              ↓
t s s i i w w s
```

**Final answer: `tssiiwws`**.
'''