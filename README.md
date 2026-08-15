# Iterative vs. Recursive Factorial Calculator

A Python comparative benchmarking script that evaluates factorial calculations ($n!$) using both iterative loop architectures and recursive function calls. Demonstrates key algorithmic paradigms, base-case recursion, and Python's arbitrary-precision integer handling across scaling input lists.

## Technical Highlights

* **Dual Paradigm Architecture:** Implements both iterative $O(n)$ space-optimized looping and recursive $O(n)$ call-stack execution models to contrast memory and control flow differences.
* **Recursion Guard Base-Case:** Features explicit base-case termination logic (`if n == 0: return 1`) to prevent stack overflow errors during recursive call unwinding.
* **Arbitrary-Precision BigInt Execution:** Leverages Python's native dynamic integer scaling to compute massive factorial outputs ($100!$) without integer overflow errors common in statically typed languages.
* **Comparative Execution Driver:** Features an automated testing loop in `main()` running identical input vectors through both algorithmic approaches to verify mathematical parity.

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (requires zero external `pip` dependencies).

## Usage

```bash
python main.py
