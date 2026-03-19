from z3 import *

T = 4

# Variables for a bounded time workflow
Alert = [Bool(f"Alert_{t}") for t in range(T)]
Review = [Bool(f"Review_{t}") for t in range(T)]

s = Solver()

# NOTE - An alert is generated at time 0
s.add(Alert[0] == True)

# No new alerts are generated after time 0
for t in range(1, T):
    s.add(Alert[t] == False)

# NOTE - Temporal ethical rule: G(Alert(x) → F(Review(x)))
s.add(Or([Review[t] for t in range(T)]))

result = s.check()
print("Case 4 result:", result)

if result == sat:
    print(s.model())