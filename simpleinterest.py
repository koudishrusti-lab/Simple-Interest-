# simple_interest.py
# Program to calculate Simple Interest

import sys

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest given principal, rate, and time."""
    return (principal * rate * time) / 100

def main():
    print("=== Simple Interest Calculator ===")
    try:
        if len(sys.argv) == 4:
            # Case 1: Arguments passed (for Jenkins or CLI)
            p = float(sys.argv[1])
            r = float(sys.argv[2])
            t = float(sys.argv[3])
        else:
            # Case 2: No arguments passed (for console use)
            p = 100000.0
            r = 5
            t = 1

        print("\n=== Program Parameters ===")
        print(f"Principal Amount : {p}")
        print(f"Rate of Interest : {r}%")
        print(f"Time in years    : {t}")

        interest = calculate_simple_interest(p, r, t)
        print(f"\nSimple Interest = {interest:.2f}")

    except ValueError:
           print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()