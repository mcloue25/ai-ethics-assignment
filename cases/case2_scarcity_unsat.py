from z3 import *

s = Solver()

# Variables for a two patient one team scenario
LVO_A = Bool("LVO_A")
LVO_B = Bool("LVO_B")
Escalate_A = Bool("Escalate_A")
Escalate_B = Bool("Escalate_B")

# if a patient is flagged as a suspected LVO case, A must be escalated : LVO_A → Escalate_A
s.assert_and_track(Implies(LVO_A, Escalate_A), "Duty_Escalate_A")
s.assert_and_track(Implies(LVO_B, Escalate_B), "Duty_Escalate_B")

# NOTE - Add Resource constraint
# Only one patient can be escalated immediately : ¬(Escalate_A ∧ Escalate_B))
s.assert_and_track(Not(And(Escalate_A, Escalate_B)), "One_Team_Constraint")

# NOTE - Both patients are flagged as suspected LVO cases
s.assert_and_track(LVO_A, "Patient_A_Flagged")
s.assert_and_track(LVO_B, "Patient_B_Flagged")

result = s.check()
print("Case 2 result:", result)

if result == unsat:
    print("UNSAT core:", s.unsat_core())