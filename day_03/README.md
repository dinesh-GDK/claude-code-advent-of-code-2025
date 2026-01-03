# Day 3: Lobby

## Part 1

### Problem Analysis
- We have batteries arranged into banks (each line of input is a bank)
- Each battery has a joltage rating from 1 to 9 (represented as single digits)
- For each bank, we must turn on exactly two batteries
- The joltage produced by a bank equals the 2-digit number formed by the two selected batteries
- Goal: Find the maximum joltage each bank can produce, then sum them all

### Example
```
9876543211111111 → 98 (select 9 and 8)
8111111111111119 → 89 (select 8 and 9)
2342342342342278 → 78 (select 7 and 8)
8181819111121111 → 92 (select 9 and 2)
Total: 98 + 89 + 78 + 92 = 357
```

### Strategy
1. For each line (bank), find the two largest digits
2. Form a 2-digit number with the largest digit in the tens place and the second-largest in the ones place
3. Sum all maximum joltages from all banks

### Algorithm
```
total = 0
for each line in input:
    # Try all pairs (i, j) where i < j
    max_joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            joltage = int(line[i] + line[j])
            max_joltage = max(max_joltage, joltage)
    total += max_joltage
return total
```

## Part 2

### Problem Analysis
- Now we need to turn on exactly **12 batteries** per bank (instead of 2)
- The joltage produced is a 12-digit number formed by the selected batteries (in order)
- Goal: Find the maximum 12-digit number for each bank, then sum them all

### Example
```
9876543211111111 → 987654321111
8111111111111119 → 811111111119
2342342342342278 → 434234234278
8181819111121111 → 888911112111
Total: 3121910778619
```

### Strategy
Use a greedy algorithm to select 12 digits that form the largest possible number:
1. For each position i in the result (0 to 11):
   - Find the largest digit among valid candidates
   - A digit at position j is valid if:
     - j >= last selected position (maintain order)
     - There are enough remaining digits: (len(line) - 1 - j) >= (11 - i)
2. Select that digit and continue

### Algorithm
```
for each line in input:
    result = ""
    last_pos = -1
    for i in range(12):
        max_digit = -1
        max_pos = -1
        # Find the largest digit that leaves enough digits for remaining positions
        for j in range(last_pos + 1, len(line)):
            if (len(line) - 1 - j) >= (11 - i):
                if int(line[j]) > max_digit:
                    max_digit = int(line[j])
                    max_pos = j
        result += line[max_pos]
        last_pos = max_pos
    total += int(result)
```
