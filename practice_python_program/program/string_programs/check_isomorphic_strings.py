"""
Interview Question: How do you check if two strings are isomorphic in Python?

Interview Explanation:
"Two strings `s` and `t` are isomorphic if characters in `s` can be mapped 1-to-1 to characters in `t`.
I maintain two dictionaries (`map_s_to_t` and `map_t_to_s`). During iteration, if a character mapping conflicts with a previously stored mapping, I return `False`."
"""

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_st, map_ts = {}, {}
    for char_s, char_t in zip(s, t):
        if (char_s in map_st and map_st[char_s] != char_t) or (char_t in map_ts and map_ts[char_t] != char_s):
            return False
        map_st[char_s] = char_t
        map_ts[char_t] = char_s

    return True

if __name__ == "__main__":
    s1, t1 = "egg", "add"
    s2, t2 = "foo", "bar"
    print(f"Are '{s1}' and '{t1}' isomorphic?", is_isomorphic(s1, t1))
    print(f"Are '{s2}' and '{t2}' isomorphic?", is_isomorphic(s2, t2))
