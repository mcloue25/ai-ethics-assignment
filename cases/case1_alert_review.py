from z3 import *

s = Solver()

# Variables for a single patient single clinician scenario
Suspected_LVO = Bool("Suspected_LVO")
Alerted = Bool("Alerted")  # clinician alerted
Authorised = Bool("Authorised")  # clinician authorised
Reviewed = Bool("Reviewed")  # clinician reviewed the diagnostic image

# Rules implementation
# if a patient is flagged as suspected LVO an alert must be generated: ∀x(SuspectedLVO(x) → ∃c(Authorized(c) ∧ Alerted(c,x))))
s.add(Implies(Suspected_LVO, And(Authorised, Alerted)))
# if an alert is generated it must lead to review by an authorised clinician:  ∀x(∃c Alerted(c,x) → ∃c(Authorized(c) ∧ ReviewedDiagnostic(c,x))))
s.add(Implies(Alerted, And(Authorised, Reviewed)))

# Patient is flagged as suspected LVO
s.add(Suspected_LVO == True)

if s.check() == sat:
    print("SAT no conflict")
    print(s.model())
else:
    print("UNSAT: duty cannot be met")
    print("Unsat core: ", s.unsat_core())