# Day 2: Gift Shop

## Part 1

### Problem Summary
We need to find invalid product IDs in given ranges and sum them up.

An invalid ID is one where some sequence of digits is repeated exactly twice consecutively:
- 55 (5 repeated twice)
- 6464 (64 repeated twice)
- 123123 (123 repeated twice)

Numbers with leading zeros (like 0101) are not considered IDs at all.

### Strategy
1. Parse the input to extract all ranges (format: "start-end")
2. For each range, iterate through all numbers from start to end (inclusive)
3. For each number, check if it's invalid by:
   - Converting the number to a string
   - Checking if any substring starting from position 0 appears immediately after itself
   - Try all possible substring lengths from 1 to half the string length
4. Sum all invalid IDs found across all ranges

### Example
For the range 11-22:
- 11: "11" = "1" + "1" (1 repeated) → invalid
- 22: "22" = "2" + "2" (2 repeated) → invalid
- Others are valid

For the range 95-115:
- 99: "99" = "9" + "9" (9 repeated) → invalid

Total in example: 1227775554

## Part 2

### Problem Summary
The definition of invalid IDs has changed. Now an ID is invalid if some sequence of digits is repeated **at least twice** (not exactly twice).

Examples of invalid IDs:
- 12341234 (1234 repeated 2 times)
- 123123123 (123 repeated 3 times)
- 1212121212 (12 repeated 5 times)
- 11111111 (1 repeated 7 times)

### Strategy
Same approach as Part 1, but modify the validation function:
1. Parse the input to extract all ranges
2. For each range, iterate through all numbers
3. For each number, check if it's invalid by:
   - Converting the number to a string
   - For each possible substring length (1 to length of string)
   - Check if the entire string can be formed by repeating that substring at least 2 times
   - This means: length % sub_len == 0 AND length / sub_len >= 2 AND all repetitions match
4. Sum all invalid IDs found across all ranges

### Example
New invalid IDs found compared to Part 1:
- 111 (1 repeated 3 times)
- 999 (9 repeated 3 times)
- 565656 (56 repeated 3 times)
- 824824824 (824 repeated 3 times)
- 2121212121 (21 repeated 5 times)

Total in example: 4174379265
