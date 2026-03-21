from z3 import *

T = 4

# Variables for a bounded time workflow
Alerted = [Bool(f"Alerted_{t}") for t in range(T)]
Reviewed = [Bool(f"Reviewed_{t}") for t in range(T)]
Overloaded = [Bool(f"Overloaded_{t}") for t in range(T)]

s = Solver()

# An alert is generated at time 0
s.add(Alerted[0] == True)

# Must be reviewed at some point: G(Alerted(x) → F(Reviewed(x)))
s.add(Or([Reviewed[t] for t in range(T)]))

# Clinician cannot review if overloaded
for t in range(T):
    s.add(Implies(Overloaded[t], Not(Reviewed[t])))


if s.check() == sat:
    print("SAT - Clinician is not overloaded, so alert is reviewed")
    print(s.model())
else:
    print("UNSAT")