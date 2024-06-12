import pytest
from src.find_players_with_zero_or_one_losses import find_winners


@pytest.mark.parametrize(
    "matches,correct_results",
    (
        pytest.param([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]], id="success-for-max-accessible-values"),
    )
)
def test_find_winners(matches: list[list[int]], correct_results: list[list[int]]) -> None:
    func_results = find_winners(matches)
    assert func_results == correct_results, f"Function output - {func_results}, expected output - {correct_results}"
