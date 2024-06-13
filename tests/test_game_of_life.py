import os
import pytest
from src.game_of_life import GameOfLife


def equals_files(expected: str, result: str) -> bool:
    with open(expected, "r") as file1:
        game_list_expected = file1.readlines()

    with open(result, "r") as file2:
        game_list_result = file2.readlines()

    return game_list_expected == game_list_result


@pytest.mark.parametrize(
    "input_file,output_file,expected_results",
    (
        pytest.param("inputStable1.txt", "outputStable1.txt", "expectedStable1.txt", id="solution-stable-figure"),
        pytest.param("inputStable2.txt", "outputStable2.txt", "expectedStable2.txt", id="solution-stable-figure2"),
        pytest.param("inputOscillator.txt", "outputOscillator.txt", "expectedOscillator.txt", id="solution-oscillator-figure"),
        pytest.param("inputOscillator2.txt", "outputOscillator2.txt", "expectedOscillator2.txt", id="solution-oscillator-figure2"),
        pytest.param("inputGliderEasy.txt", "outputGliderEasy.txt", "expectedGliderEasy.txt", id="solution-glider-figure-easy"),
        pytest.param("inputGlider.txt", "outputGlider.txt", "expectedGlider.txt", id="solution-glider-figure")
    )
)
def test_find_winners(input_file: str, output_file: str, expected_results: str) -> None:
    input_file_path = os.path.join(os.path.dirname(__file__), "resources", input_file)
    output_file_path = os.path.join(os.path.dirname(__file__), "resources", output_file)
    expected_results_path = os.path.join(os.path.dirname(__file__), "resources", expected_results)
    game = GameOfLife()
    game.game(input_file_path, output_file_path)
    assert equals_files(input_file_path, output_file_path)
