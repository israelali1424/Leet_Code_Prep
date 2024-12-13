
# Bit Manipulation

## Overview

- **Purpose**: Provides efficient operations at the bit level, often used for optimizing space and time in algorithms.
- **Concept**:  
  Manipulates individual bits of data using bitwise operators such as AND, OR, XOR, NOT, shifts, etc.
- **Common Use Cases**:  
  - Checking if a number is even or odd  
  - Swapping two numbers without a temporary variable  
  - Counting the number of 1s in a binary representation  
  - Setting, clearing, or toggling specific bits

## Bitwise Operators

- **AND** (`&`): Returns 1 if both bits are 1  
  Example: `5 & 3` → `0101 & 0011` = `0001` (1)

- **OR** (`|`): Returns 1 if at least one bit is 1  
  Example: `5 | 3` → `0101 | 0011` = `0111` (7)

- **XOR** (`^`): Returns 1 if the bits are different  
  Example: `5 ^ 3` → `0101 ^ 0011` = `0110` (6)

- **NOT** (`~`): Inverts the bits  
  Example: `~5` → `~0101` = `1010` (Two's complement)

- **Left Shift** (`<<`): Shifts bits to the left by a specified number of positions  
  Example: `5 << 1` → `0101 << 1` = `1010` (10)

- **Right Shift** (`>>`): Shifts bits to the right by a specified number of positions  
  Example: `5 >> 1` → `0101 >> 1` = `0010` (2)

## Complexity

- **Time Complexity**: O(1) for most bitwise operations
- **Space Complexity**: O(1)

## Interview Relevance

- Often tested in technical interviews for problems related to:
  - Bit masking
  - Parity checks
  - Power of two checks
  - Bit counting or manipulation optimizations

## Example Implementation
