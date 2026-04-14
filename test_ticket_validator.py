import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_ticket_is_valid_starting_with_TK():
    result = validate_ticket("TK928134")
    assert result == True

def test_ticket_is_invalid_not_starting_with_TK():
    result = validate_ticket("AB928134")
    assert result == True

def test_ticket_is_invalid_not_having_8_characters():
    result = validate_ticket("TK92134")
    assert result == False

def test_ticket_is_invalid_not_having_last_6_numbers():
    result = validate_ticket("TK92134")
    assert result == False

def test_ticket_is_invalid_not_having_last_6_numbers():
    result = validate_ticket("TK92134B")
    assert result == False

def test_ticket_is_string():
    result = validate_ticket("TK92134")
    assert result == True

def test_ticket_is_not_string():
    with pytest.raises(TypeError):
        validate_ticket(12345678)
        
