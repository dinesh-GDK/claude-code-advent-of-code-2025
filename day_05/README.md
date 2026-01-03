# Day 5: Cafeteria

## Part 1: Count Fresh Ingredients

### Problem Understanding
The Elves have a database that shows which ingredient IDs are fresh and which are spoiled. The database contains:
1. A list of fresh ingredient ID ranges (inclusive)
2. A blank line separator
3. A list of available ingredient IDs

We need to determine how many of the available ingredient IDs are fresh.

### Key Rules
- Ranges are inclusive (e.g., 3-5 includes 3, 4, and 5)
- Ranges can overlap - an ID is fresh if it falls into ANY range
- We need to count how many available IDs are fresh

### Example
Input:
```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

Analysis:
- ID 1: spoiled (not in any range)
- ID 5: fresh (in range 3-5)
- ID 8: spoiled (not in any range)
- ID 11: fresh (in range 10-14)
- ID 17: fresh (in ranges 16-20 AND 12-18)
- ID 32: spoiled (not in any range)

Answer: 3 fresh IDs

### Strategy
1. Parse the input file to separate ranges from available IDs (split on blank line)
2. Parse each range line to get start and end values
3. For each available ID, check if it falls within ANY of the ranges
4. Count how many IDs are fresh
5. Return the count

### Implementation Plan
- Read file and split on blank line
- Parse ranges into list of (start, end) tuples
- Parse available IDs into list of integers
- For each ID, check if start <= ID <= end for any range
- Count matches

**Part 1 Answer: 773**

## Part 2: Count All Fresh IDs

### Problem Understanding
Now we need to ignore the second section (available ingredient IDs) completely. Instead, we need to count ALL ingredient IDs that the fresh ranges consider to be fresh.

### Key Change
- Part 1: Count how many available IDs are fresh
- Part 2: Count the total number of unique IDs covered by ALL ranges

### Example
Ranges: 3-5, 10-14, 16-20, 12-18

All fresh IDs: 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Range 3-5 covers: 3, 4, 5 (3 IDs)
- Range 10-14 covers: 10, 11, 12, 13, 14 (5 IDs)
- Range 16-20 covers: 16, 17, 18, 19, 20 (5 IDs)
- Range 12-18 covers: 12, 13, 14, 15, 16, 17, 18 (7 IDs)
- But ranges overlap! Unique IDs: 14 total

Answer: 14 ingredient IDs

### Strategy
Since ranges can be very large (millions of IDs), we can't iterate through all IDs. We need to:
1. Parse all ranges
2. Merge overlapping and adjacent ranges
3. Sum up the sizes of merged ranges

### Merging Algorithm
1. Sort ranges by start position
2. Iterate through sorted ranges
3. If current range overlaps or is adjacent to previous, merge them
4. Otherwise, start a new merged range
5. Count total IDs in all merged ranges

Range size = end - start + 1 (inclusive)
