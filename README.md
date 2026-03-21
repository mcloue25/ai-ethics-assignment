# AI-Ethics-Assignment
This repository contains code developed for the AI Ethics assignment. In it we implement ethical scenarios for an AI assisted stroke triage system (Viz LVO) using the Z3 constraint solver.

Each case models an ethical requirement and demonstrates both:
- satisfiable (SAT) scenarios where ethical constraints are met
- unsatisfiable (UNSAT) scenarios where constraints are violated or conflict

## Files

### Case 1: Duty to Alert and Review
- `cases/case1_alert_review.py`  
  Satisfiable case showing that a suspected LVO alert leads to clinician review.

- `cases/case1_alert_review_violation.py`  
  Unsatisfiable case where a system failure violates the ethical constraint.

### Case 2: Scarcity and Prioritarian/Utilitarian Resolutions
- `cases/case2_resolutions.py`  
  Satisfiable cases using prioritarian resolution (favouring the more vulnerable) or a utilitarian resolution (favour the higher expected benefit).

- `cases/case2_scarcity_unsat.py`  
  Unsatisfiable case where two patients require treatment but only one resource is available.

### Case 3: Fairness
- `cases/case3_fairness.py`  
  Satisfiable case where clinically similar patients are treated equally.

- `cases/case3_fairness_violation.py`  
  Unsatisfiable case where a patient not represented in training data is not treated fairly.

### Case 4: Temporal Responsibility
- `cases/case4_temporal_review.py`  
  Satisfiable case where alerts are eventually reviewed.

- `cases/case4_temporal_violation.py`  
  Unsatisfiable case where alerts are never reviewed because clinician is overloaded.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Code

Run each case using Python:

### Case 1:
```bash
python cases/case1_alert_review.py
python cases/case1_alert_review_violation.py
```
### Case 2:
```bash
python cases/case2_resolutions.py
python cases/case2_scarcity_unsat.py
```

### Case 3:
```bash
python cases/case3_fairness.py
python cases/case3_fairness_violation.py
```

### Case 4:
```bash
python cases/case4_temporal_review.py
python cases/case4_temporal_violation.py
```


## Expected Outputs
ToDo - Add results here