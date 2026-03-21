from z3 import *

T = 4

# Variables for a bounded time workflow
Alerted = [Bool(f"Alerted_{t}") for t in range(T)]
Reviewed = [Bool(f"Reviewed_{t}") for t in range(T)]
Overloaded = [Bool(f"Overloaded_{t}") for t in range(T)]

s = Solver()

# An alert is generated at time 0
s.add(Alerted[0] == True)

# If overloaded the clinician cannot review
for t in range(T):
    s.add(Implies(Overloaded[t], Not(Reviewed[t])))

# Clinician overloaded at every step
for t in range(T):
    s.add(Overloaded[t] == True)

# Ethical req - must be reviewed at some point: G(Alerted(x) → F(Reviewed(x)))
s.assert_and_track(Or([Reviewed[t] for t in range(T)]),"Must_Eventually_Review")

if s.check() == sat:
    print("SAT")
    print(s.model())
else:
    print("UNSAT - Clinician overload prevents review")
    print("Unsat core:", s.unsat_core())