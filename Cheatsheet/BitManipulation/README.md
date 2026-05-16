# Bit Manipulation

Is a technique used in programming to perform operations at the bit level, which can often lead to more efficient and faster algorithms.

#### When is bit manipulation useful?

Bit manipulation allows us to work directly with the binary representation of numbers, making certain operations more efficient. Common tasks such as setting, clearing, toggling and checking bits can be performed quickly using bitwise operation.

For example, one of the most common space optimization techniques involves using an unsigned 32-bit integer to represent a set of boolean values, where each bit in the integer corresponds to a different boolean value. This allow us to store and manipulate up to 32 states without using a boolean array or hash set.

## Bitwise operators

### NOT (`~`)

Inverts a single bit:

- `~0 = 1`
- `~1 = 0`

| a   | ~a  |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---

### AND (`&`)

Returns `1` **only if both bits are 1**, otherwise `0`.

| a   | b   | a & b |
| --- | --- | ----- |
| 0   | 0   | 0     |
| 0   | 1   | 0     |
| 1   | 0   | 0     |
| 1   | 1   | 1     |

---

### OR (`|`)

Returns `1` **if at least one bit is 1**, otherwise `0`.

| a   | b   | a &#124; b |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

---

### XOR (`^`)

Returns `1` **only if the bits are different**, otherwise `0`.

| a   | b   | a ^ b |
| --- | --- | ----- |
| 0   | 0   | 0     |
| 0   | 1   | 1     |
| 1   | 0   | 1     |
| 1   | 1   | 0     |

Some useful characteristics of the XOR operator are:

- a ^ 0 = a
- a ^ a = 0

---

In addition, it's also important to understand the fundamental shift operators.

Shift operators move the bits of a number **left or right** by a specified number of positions. Zeros are filled in from the opposite end.

We’ll use small values of `a` and shift amounts to keep it simple.

---

### Left Shift (`<<`)

Shifts all bits of `a` **to the left** by `n` positions, adding 0s on the right.  
Each left shift is equivalent to multiplying by `2ⁿ`.

#### Example: `a << 1`

| a (decimal) | a (binary) | a << 1 (binary) | Result (decimal) |
| ----------- | ---------- | --------------- | ---------------- |
| 1           | `0001`     | `0010`          | 2                |
| 2           | `0010`     | `0100`          | 4                |
| 3           | `0011`     | `0110`          | 6                |
| 4           | `0100`     | `1000`          | 8                |

---

### Right Shift (`>>`)

Shifts all bits of `a` **to the right** by `n` positions, discarding bits on the right.  
Each right shift is equivalent to integer division by `2ⁿ`.

Assumes unsigned or logical shift (no sign extension).

#### Example: `a >> 1`

| a (decimal) | a (binary) | a >> 1 (binary) | Result (decimal) |
| ----------- | ---------- | --------------- | ---------------- |
| 1           | `0001`     | `0000`          | 0                |
| 2           | `0010`     | `0001`          | 1                |
| 3           | `0011`     | `0001`          | 1                |
| 4           | `0100`     | `0010`          | 2                |

---

---

### Common Bit Manipulation Techniques

These are foundational bitwise operations frequently used in systems programming, embedded development, competitive programming, and algorithm design:

- **Set the i<sup>th</sup> bit to 1**  
  Force the bit at position `i` to `1` (regardless of its current value).  
  `x |= (1 << i)`

- **Clear the i<sup>th</sup> bit (set to 0)**  
  Force the bit at position `i` to `0`, leaving other bits unchanged.  
  `x &= ~(1 << i)`

- **Toggle the i<sup>th</sup> bit**  
  Flip the bit at position `i`: `1` becomes `0`, and `0` becomes `1`.  
  `x ^= (1 << i)`

- **Check if the i<sup>th</sup> bit is set**  
  Returns true if the bit at position `i` is `1`, false if `0`.  
  `(x & (1 << i)) != 0`

- **Check if a number is even or odd**  
  The least significant bit (LSB) determines parity:

  - `x & 1 == 0` → **even**
  - `x & 1 == 1` → **odd**

- **Check if a number is a power of 2**  
  A power of two has exactly one bit set.  
  `x > 0 && (x & (x - 1)) == 0`

---

## Real-World Application: Networking and Data Integrity

Bit manipulation is essential in low-level systems, especially in networking protocols and data transmission:

- **IP Addressing and Subnetting**  
  Bitwise AND is used to compute network addresses:  
  `IP & SubnetMask` determines if two hosts are on the same network.

- **Error Detection & Correction**  
  Protocols like checksums, CRC, and parity bits use bitwise operations to detect and fix transmission errors with minimal overhead.

- **Protocol Flags and Compression**  
  Flags in protocol headers are packed as bits to save space and processing time. Bit masking efficiently sets, clears, and checks those flags.
