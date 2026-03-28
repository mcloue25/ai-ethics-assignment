from z3 import *

s = Solver()

# Variables for a single-patient uncertainty scenario
# patient actually has LVO
LVO = Bool("LVO")
# AI flags suspected LVO
SuspectedLVO = Bool("SuspectedLVO")
# patient enters urgent review pathway
Escalated = Bool("Escalated")


FalsePositive = Bool("FalsePositive")
FalseNegative = Bool("FalseNegative")

# NOTE - Clinical pathway assumption:
# If AI flags suspected LVO, the patient is escalated for urgent review
s.add(Implies(SuspectedLVO, Escalated))
s.add(Implies(Not(SuspectedLVO), Not(Escalated)))

# False Positive & False Negatives
s.add(FalsePositive == And(SuspectedLVO, Not(LVO)))
s.add(FalseNegative == And(Not(SuspectedLVO), LVO))

# NOTE - Ethical requirement:
# If a patient actually has an LVO, they should be escalated for urgent review
s.assert_and_track(Implies(LVO, Escalated), "Duty_Escalate_True_LVO")

# Violation scenario: patient has LVO but AI misses it
s.add(LVO == True)
s.add(SuspectedLVO == False)

if s.check() == sat:
    print("SAT")
    print(s.model())
else:
    print("UNSAT - False negative violates urgent escalation duty")
    print("Unsat core:", s.unsat_core())