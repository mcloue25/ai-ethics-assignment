from z3 import *

s = Solver()

# Variables for a two patient fairness scenario
Eligible_A = Bool("Eligible_A")
Eligible_B = Bool("Eligible_B")
Clinically_Similar = Bool("Clinically_Similar")
Priority_A_over_B = Bool("Priority_A_over_B")
Priority_B_over_A = Bool("Priority_B_over_A")

# Patients A and B are both eligible and clinically similar
s.add(Eligible_A == True)
s.add(Eligible_B == True)
s.add(Clinically_Similar == True)

# NOTE - If two patients are clinically similar and equally eligible neither should be given priority over 
# the other: (Eligible(x) ∧ Eligible(y) ∧ ClinicallySimilar(x,y)) → (¬Priority(x,y) ∧ ¬Priority(y,x)))
s.add(Implies(And(Eligible_A, Eligible_B, Clinically_Similar), And(Not(Priority_A_over_B), Not(Priority_B_over_A))))

s.assert_and_track(Priority_A_over_B, "Unfair_Priority_A")


if s.check() == sat:
    print("SAT - Unfair priority allowed")
else:
    print("UNSAT - Fairness constraint blocks unequal priority")
    print("Unsat core:", s.unsat_core())