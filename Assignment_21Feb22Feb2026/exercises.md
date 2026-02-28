
Build a Decision Tree to Choose a Job Offer
1) Concept (Plain English)
You’ll implement a very simple binary decision tree for yes/no decisions:

Each internal node has:

a criterion (one of: salary, distance, coffee, is_nightshift)

a value (the threshold)

a rule:

go left if feature_value ≤ value
go right if feature_value > value
Each leaf node is a final decision: YES (accept) or NO (reject).

You’ll then:

Define a DecisionTreeNode class.
Build the exact tree shown in the prompt (with minor fixes).
Call .check(job_description) to get True/False.
2) Problem Statement
Your Task
Write a class DecisionTreeNode that can act as either:

a boundary node with boundary, boundary_value, left, right, or
a leaf with a final decision (True for YES, False for NO).
Implement:

check(features: dict) -> bool Traverses from the current node down to a leaf using the rule “go left if features[boundary] ≤ boundary_value, else right”, and returns the leaf’s boolean decision.
Also create two helpers:

YES() → returns a leaf node that decides True
NO() → returns a leaf node that decides False
Then build this tree:

If salary ≤ 1000 → NO
Else (salary > 1000):
    If distance ≤ 40 → YES
    Else → NO
You can extend it later with coffee or nightshift rules in the bonuses.

