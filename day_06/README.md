# Day 6: Trash Compactor

## Part 1

### Problem Understanding
The puzzle input represents a "math worksheet" where:
- Each problem consists of numbers arranged vertically in a column
- At the bottom of each problem is an operation symbol (+ or *)
- Problems are separated by full columns of only spaces
- We need to solve each problem by applying the operation to all numbers
- Finally, sum all the individual problem results to get the grand total

### Example Analysis
```
123 328  51 64
 45  64 387 23
  6  98 215 314
  *   +   *   +
```

Four problems:
1. 123 × 45 × 6 = 33210
2. 328 + 64 + 98 = 490
3. 51 × 387 × 215 = 4243455
4. 64 + 23 + 314 = 401

Grand total: 33210 + 490 + 4243455 + 401 = 4277556

### Strategy
1. Parse the input to extract number tokens with their column positions
2. Parse the operator row to find operators and their positions
3. For each operator, find the closest numbers above it (one per row)
4. Apply the operator to those numbers
5. Sum all problem results

## Part 2

### Problem Understanding
The cephalopods forgot to explain how to read their math correctly:
- Numbers are written **vertically in columns** (one number per column)
- Each column represents a single number with digits reading **top-to-bottom**
- Top digit = most significant, bottom digit = least significant
- Problems are processed **RIGHT-TO-LEFT** (not left-to-right)
- Problems are still separated by columns of only spaces
- Operators at the bottom still indicate the operation

### Example Analysis (Same input, different interpretation)
```
123 328  51 64
 45  64 387 23
  6  98 215 314
  *   +   *   +
```

Reading RIGHT-TO-LEFT, each column forms a number:
1. Rightmost problem (+): 4 + 431 + 623 = 1058
   - Column "64\n23\n314" (rightmost) → digits 6,2,3,4 reading top-to-bottom → but separated by spaces
   - Actually: column with "4" → 4, column with "1\n3\n4" → 431 (top-to-bottom), column with "6\n2\n3" → 623
2. Second from right (*): 175 * 581 * 32 = 3253600
3. Third from right (+): 8 + 248 + 369 = 625
4. Leftmost (*): 356 * 24 * 1 = 8544

Grand total: 1058 + 3253600 + 625 + 8544 = 3263827

### Strategy
1. Parse input line by line, preserving column positions
2. For each column index, collect all characters from top-to-bottom (excluding operator row)
3. Non-space characters in a column form a number (read top-to-bottom as digits)
4. Columns with only spaces separate problems
5. Identify operator for each problem group from the operator row
6. Process problems from RIGHT-TO-LEFT
7. Calculate each problem result and sum them all

