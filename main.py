
### 2. `main.py`

```python
from evaluator import evaluate_solution, rank_solutions


solution_a = {
    "name": "Solution A",
    "correctness": 10,
    "efficiency": 9,
    "readability": 9,
    "maintainability": 8,
    "edge_cases": 9,
    "notes": "Uses hash map approach with O(n) time complexity."
}

solution_b = {
    "name": "Solution B",
    "correctness": 8,
    "efficiency": 5,
    "readability": 7,
    "maintainability": 7,
    "edge_cases": 6,
    "notes": "Uses nested loops with O(n²) time complexity."
}

solutions = [solution_a, solution_b]

ranked_solutions = rank_solutions(solutions)

print("AI Code Evaluation Results\n")

for solution in ranked_solutions:
    score = evaluate_solution(solution)
    print(f"{solution['name']}")
    print(f"Score: {score}/50")
    print(f"Notes: {solution['notes']}")
    print("-" * 40)

best_solution = ranked_solutions[0]

print(f"\nBest Solution: {best_solution['name']}")
print("Reason: This solution has the highest overall score based on correctness, efficiency, readability, maintainability, and edge case handling.")
