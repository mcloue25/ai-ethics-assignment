from z3 import *

s = Solver()

# Variables for a two patient fairness scenario
LVO_A = Bool('LVO_A')
LVO_B = Bool('LVO_B')
Detected_A = Bool('Detected_A')
Detected_B = Bool('Detected_B')
RepresentedInTraining_A = Bool('RepresentedInTraining_A')
RepresentedInTraining_B = Bool('RepresentedInTraining_B')
Escalated_A = Bool('Escalated_A')
Escalated_B = Bool('Escalated_B')

# Both patients actually have LVO and are clinically similar
s.add(LVO_A == True)
s.add(LVO_B == True)

# Patient A is represented in training data, B is not
s.add(RepresentedInTraining_A == True)
s.add(RepresentedInTraining_B == False)

# NOTE - Detection depends on representation in training data
s.add(Implies(And(LVO_A, RepresentedInTraining_A), Detected_A))
s.add(Implies(LVO_B, Not(RepresentedInTraining_B)), Not(Detected_B))

# Only detected patients get escalated
s.add(Implies(Not(Detected_A), Not(Escalated_A)))
s.add(Implies(Not(Detected_B), Not(Escalated_B)))

# Fairness both have LVO, both should be escalated
s.assert_and_track(Implies(And(LVO_A, LVO_B), And(Escalated_A, Escalated_B)),"Fairness_Both_Escalated")

if s.check() == sat:
    print("SAT - Fairness")
    print(s.model())
else:
    print("UNSAT - Biased detection violates fairness")
    print("Unsat core:", s.unsat_core())