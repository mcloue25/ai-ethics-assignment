from z3 import *

s = Solver()

# Variables for a two patient one team scenario
LVO_A = Bool("Suspected_LVO_A")
LVO_B = Bool("Suspected_LVO_B")
Escalate_A = Bool("Escalate_A")
Escalate_B = Bool("Escalate_B")

# NOTE - if a patient is flagged as a suspected LVO case, they must be escalated : LVO_A --> Escalate_A
s.assert_and_track(Implies(LVO_A, Escalate_A), "Duty_Escalate_A")
s.assert_and_track(Implies(LVO_B, Escalate_B), "Duty_Escalate_B")

# Add Resource constraint
s.assert_and_track(Not(And(Escalate_A, Escalate_B)), "One_Team_Constraint")

# Both patients are flagged as suspected LVO cases
s.add(LVO_A == True)
s.add(LVO_B == True)

if s.check() == sat:
    print("SAT")
    print(s.model())
else:
    print("UNSAT - Deontological deadlock")
    print("Unsat core:", s.unsat_core())