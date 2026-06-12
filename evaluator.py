def evaluate_solution(solution):
    """
    Calculates the total score of a code solution.
    Maximum score is 50.
    """

    total_score = (
        solution["correctness"]
        + solution["efficiency"]
        + solution["readability"]
        + solution["maintainability"]
        + solution["edge_cases"]
    )

    return total_score


def rank_solutions(solutions):
    """
    Ranks solutions from best to worst based on total score.
    """

    return sorted(solutions, key=evaluate_solution, reverse=True)
