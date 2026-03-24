from z3 import *

# --- Resolution 1: Prioritarian ---
s = Solver()

# Variables for a two patient one team scenario
LVO_A = Bool("Suspected_LVO_A")
LVO_B = Bool("Suspected_LVO_B")
Escalate_A = Bool("Escalate_A")
Escalate_B = Bool("Escalate_B")

# Prioritarian variables
Vulnerable_A = Bool("Vulnerable_A")
Vulnerable_B = Bool("Vulnerable_B")
Priority_A = Bool("Priority_A")

# both have suspected LVO
s.add(LVO_A == True)
s.add(LVO_B == True)

# Constraint: only one team
s.add(Not(And(Escalate_A, Escalate_B)))

# Patient A is more vulnerable than patient B
s.add(Vulnerable_A == True)
s.add(Vulnerable_B == False)
# If patient A is more vulnerable than patient B, A should be prioritised : MoreVulnerable(x,y) → Priority(x,y))
s.add(Implies(And(Vulnerable_A, Not(Vulnerable_B)), Priority_A))
# If A has priority over B, then A is escalated and B is not : Priority(x,y) → (Escalate(x) ∧ ¬Escalate(y)))
s.add(Implies(Priority_A, And(Escalate_A, Not(Escalate_B))))

if s.check() == sat:
    print("SAT - Prioritarian: escalate A (more vulnerable)")
    print(s.model())
else:
    print("UNSAT")


# --- Resolution 2: Utilitarian ---
#  Utilitarianism uses benefit instead of vulnerability
s2 = Solver()

# Utilitarian variables
Benefit_A = Int("Benefit_A")
Benefit_B = Int("Benefit_B")
Util_Priority_A = Bool("Util_Priority_A")

s2.add(LVO_A == True)
s2.add(LVO_B == True)

# Constraint: only one team
s2.add(Not(And(Escalate_A, Escalate_B)))

# Patient B has higher expected benefit
s2.add(Benefit_A == 50)
s2.add(Benefit_B == 100)

# Utilitarian rule: escalate whoever has higher expected benefit
s2.add(Implies(Benefit_A > Benefit_B, Util_Priority_A))
s2.add(Implies(Not(Util_Priority_A), And(Escalate_B, Not(Escalate_A))))

if s2.check() == sat:
    print("\nSAT - Utilitarian: escalate B (higher expected benefit)")
    print(s2.model())
else:
    print("UNSAT")