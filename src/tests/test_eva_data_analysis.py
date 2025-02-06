import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size


@pytest.mark.parametrize("input_value, expected_result", [
	("10:00", 10),
	("10:20", pytest.approx(10.33333)),
])
def test_text_to_duration(input_value, expected_result):
	"""
	Test that text_to_duration returns expected value for durations
	with typical whole hour durations
	"""
	actual_result = text_to_duration(input_value)
	assert actual_result == expected_result

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
    ("Yuri Malenchecko;Neil Armstrong;Buzz Aldrin;", 3)    
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result
    
def test_calculate_crew_size_edge_case():
    """
    Test that calculate_crew_size returns None for the edge case of no crew
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None