from z3 import *

s = Solver()

# Variables for a single patient single clinician scenario
Suspected_LVO = Bool("Suspected_LVO")
Alerted = Bool("Alerted")  # clinician alerted
Authorised = Bool("Authorised")  # clinician authorised
Reviewed = Bool("Reviewed")  # clinician reviewed the diagnostic image
System_Failure = Bool('System_Failure')  # system or infrastructure failure

# NOTE - Ethical duties
# if a patient is flagged as suspected LVO an alert must be generated: ∀x(SuspectedLVO(x) → ∃c(Authorized(c) ∧ Alerted(c,x))))
s.assert_and_track(
    Implies(Suspected_LVO, And(Authorised, Alerted)),
    "Duty_Alert"
)

# if an alert is generated it must lead to review by an authorised clinician:  ∀x(∃c Alerted(c,x) → ∃c(Authorized(c) ∧ ReviewedDiagnostic(c,x))))
s.assert_and_track(
    Implies(Alerted, And(Authorised, Reviewed)),
    "Duty_Review"
)

# if system/infrastructure failure, alert can not be delivered
s.assert_and_track(
    Implies(System_Failure, Not(Alerted)),
    "System_Failure"
)

# Patient has suspected LVO and there is system/infrastructure failure
s.add(Suspected_LVO == True)
s.add(System_Failure == True)

if s.check() == sat:
    print("SAT no conflict")
    print(s.model())
else:
    print("UNSAT: duty cannot be met when system failure")
    print("Unsat core: ", s.unsat_core())