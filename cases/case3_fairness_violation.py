from z3 import *

s = Solver()

# Variables for a two patient fairness scenario
Eligible_A = Bool("Eligible_A")
Eligible_B = Bool("Eligible_B")
Clinically_Similar = Bool("Clinically_Similar")
Priority_A_B = Bool("Priority_A_B")
Priority_B_A = Bool("Priority_B_A")

# If two patients are clinically similar and equally eligible neither should be given priority over the other
s.add(Implies(And(Eligible_A, Eligible_B, Clinically_Similar), And(Not(Priority_A_B), Not(Priority_B_A))))

# NOTE - Patients A and B are both eligible and clinically similar
s.add(Eligible_A == True)
s.add(Eligible_B == True)
s.add(Clinically_Similar == True)

# Violation scenario: force an unfair priority ordering
s.add(Priority_A_B == True)

result = s.check()
print("Case 3 violation result:", result)

if result == sat:
    print(s.model())