"""
7. Count Vowels and Consonants
Interview Note: Filters for alphabetic characters and checks against vowel set/string.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_vowels_consonants(text: str) -> tuple[int, int]:
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

if __name__ == "__main__":
    text = "automation"
    v, c = count_vowels_consonants(text)
    print("Vowels:", v)
    print("Consonants:", c)
