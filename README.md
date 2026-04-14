"# Python_regex_challenge" 
# Challenge 1: Basic Pattern Matching (Digits Extractor)

## Goal
Write a Python program that uses regular expressions (`re` module) to extract all numbers from a string.

---

## Inputs / Outputs

- **Input:** A string containing letters, spaces, and numbers  
- **Output:** A list of all numbers found in the string (as strings)

---

## Constraints

- Use Python’s built-in `re` module  
- Do NOT use loops to manually check each character  
- Use at least one regex function (`re.findall`, `re.search`, etc.)  
- Assume numbers are integers only (no decimals)

---

## Test Cases

1.  
**Input:**  
`"I have 2 apples and 10 bananas"`  

**Output:**  
`['2', '10']`

---

2.  
**Input:**  
`"No numbers here!"`  

**Output:**  
`[]`

---

3.  
**Input:**  
`"2024 is coming after 2023"`  

**Output:**  
`['2024', '2023']`

---

4.  
**Input:**  
`"Room 101, Floor 5"`  

**Output:**  
`['101', '5']`

---

## Notes / Hint

- `\d` → matches a digit  
- `+` → means "one or more"  
- Example pattern: `\d+`