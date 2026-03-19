from z3 import *

T = 4

# Variables for a simplified bounded time workflow
Review = [Bool(f"Review_{t}") for t in range(T)]

s = Solver()

# NOTE - No review ever occurs within the time horizon
for t in range(T):
    s.add(Review[t] == False)

# There must be at least one review at some point in the time horizon
s.add(Or([Review[t] for t in range(T)]))

result = s.check()
print("Case 4 violation result:", result)

if result == sat:
    print(s.model())