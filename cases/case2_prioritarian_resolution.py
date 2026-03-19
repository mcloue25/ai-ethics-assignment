from z3 import *

s = Solver()

# Variables for a two patient one team scenario
Vulnerable_A = Bool("Vulnerable_A")
Vulnerable_B = Bool("Vulnerable_B")
Priority_A_B = Bool("Priority_A_B")
Escalate_A = Bool("Escalate_A")
Escalate_B = Bool("Escalate_B")


# NOTE - If patient A is more vulnerable than patient B, A should be prioritised : MoreVulnerable(x,y) → Priority(x,y))
s.add(Implies(And(Vulnerable_A, Not(Vulnerable_B)), Priority_A_B))
# NOTE - If A has priority over B, then A is escalated and B is not : Priority(x,y) → (Escalate(x) ∧ ¬Escalate(y)))
s.add(Implies(Priority_A_B, And(Escalate_A, Not(Escalate_B))))

# NOTE - Patient A is more vulnerable than patient B
s.add(Vulnerable_A == True)
s.add(Vulnerable_B == False)

result = s.check()
print("Prioritarian result:", result)

if result == sat:
    print(s.model())