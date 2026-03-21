from z3 import *

s = Solver()

# Variables for a single patient single clinician scenario
suspected_lvo = Bool("suspected_lvo")
clinician_alerted = Bool("clinician_alerted")
clinician_authorized = Bool("clinician_authorized")
clinician_reviews = Bool("clinician_reviews")
system_failure = Bool('system_failure')

# Ethical duties
# if a patient is flagged as suspected LVO an alert must be generated: ∀x(SuspectedLVO(x) → ∃c(Authorized(c) ∧ Alerted(c,x))))
s.assert_and_track(
    Implies(suspected_lvo, And(clinician_authorized, clinician_alerted)),
    "Duty_Alert"
)

# if an alert is generated it must lead to review by an authorised clinician:  ∀x(∃c Alerted(c,x) → ∃c(Authorized(c) ∧ ReviewsDiagnostic(c,x))))
s.assert_and_track(
    Implies(clinician_alerted, And(clinician_authorized, clinician_reviews)),
    "Duty_Review"
)

# if system/infrastructure failure, alert can not be delivered
s.assert_and_track(
    Implies(system_failure, Not(clinician_alerted)),
    "System_Failure"
)

# Patient has suspected LVO and there is system failure
s.add(suspected_lvo == True)
s.add(system_failure == True)

if s.check() == sat:
    print("SAT no conflict")
    print(s.model())
else:
    print("UNSAT: duty cannot be met when system failure")
    print("Unsat core: ", s.unsat_core())