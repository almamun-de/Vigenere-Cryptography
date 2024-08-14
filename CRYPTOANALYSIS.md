# Cryptanalysis of the Vigenère Cipher

## Overview

The Vigenère cipher, while more secure than the Caesar cipher, is still vulnerable to cryptanalysis, especially when the keyword is short or the ciphertext is long. Two common techniques used to break the Vigenère cipher are the **Kasiski test** and the **Kappa test** (Index of Coincidence). This document explains how these tests work and how they can be used to determine the keyword length and decrypt the ciphertext.

## Kasiski Test

### How It Works
The Kasiski test, named after Friedrich Kasiski, is a method of breaking the Vigenère cipher by finding repeating sequences of letters in the ciphertext. The main idea is that if the same sequence of letters appears multiple times in the ciphertext, it may have been encrypted using the same part of the keyword.

### Steps:
1. **Identify Repeated Sequences**: Look for sequences of letters that appear more than once in the ciphertext.
   
2. **Measure the Distances**: For each repeated sequence, measure the distance (in terms of the number of characters) between the occurrences of the sequence.

3. **Find Common Divisors**: The distances are likely to be multiples of the keyword length. By finding the greatest common divisor (GCD) of these distances, you can estimate the keyword length.

### Example:
- Suppose the sequence "XYZ" appears in the ciphertext at positions 10 and 50.
- The distance between them is 40 characters.
- If another sequence "ABC" appears at positions 20 and 60, the distance is also 40 characters.
- The common divisor of these distances suggests that the keyword length might be 4 or 2.

### Limitations:
- The Kasiski test is most effective when the keyword is relatively short compared to the length of the ciphertext.
- If the keyword is long or the ciphertext is short, this method may be less effective.

## Kappa Test (Index of Coincidence)

### How It Works
The Kappa test, also known as the Index of Coincidence (IC), is a statistical measure that can be used to estimate the length of the keyword in a Vigenère cipher. It works by comparing the likelihood of repeated letters in the ciphertext to what would be expected in a random text.

### Steps:
1. **Calculate the Index of Coincidence**: The IC is calculated for the entire ciphertext, and then for multiple subsets of the ciphertext assuming different possible keyword lengths.
   
2. **Analyze IC Values**: For the correct keyword length, the IC for each subset should be close to the IC of natural language (typically around 0.068 for English). When using the wrong keyword length, the IC should be closer to the random text value (approximately 0.0385).

3. **Identify the Keyword Length**: The keyword length that produces the highest average IC across subsets is likely the correct length.

### Example:
- Assume the ciphertext is divided into subsets of length 3, 4, 5, etc.
- The IC is calculated for each subset, and the average IC for each possible keyword length is compared.
- The length with the IC closest to the expected value for natural language is chosen as the most likely keyword length.

### Limitations:
- The Kappa test is more reliable with longer ciphertexts, where the statistical patterns are more apparent.
- For very short ciphertexts, the IC might not provide a clear indication of the keyword length.

## Using Both Tests Together

By combining the Kasiski test and the Kappa test, you can increase the accuracy of your cryptanalysis:

- **Kasiski Test**: Provides an initial estimate of the keyword length.
- **Kappa Test**: Refines the estimate by analyzing the statistical properties of the ciphertext.

### Practical Application
1. **Run the Kasiski Test**: Start by identifying possible keyword lengths using the Kasiski test.
2. **Validate with Kappa Test**: Use the Kappa test to calculate the IC for the suggested keyword lengths.
3. **Choose the Best Fit**: Select the keyword length that best fits both the Kasiski test results and the IC analysis.

## Conclusion

The Kasiski test and Kappa test are powerful tools in the cryptanalysis of the Vigenère cipher. While they each have their strengths and limitations, using them together can help accurately determine the keyword length, making it possible to decrypt the ciphertext without knowing the keyword.

For more practical examples, you can refer to the `kasiski_test.py` and `kappa_test.py` scripts in this repository.

