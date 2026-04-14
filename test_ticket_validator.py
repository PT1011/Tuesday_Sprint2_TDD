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

def test_get_ticket_tier_General_works_with_0():
    result = get_ticket_tier("TK012345")
    assert result == "General"

def test_get_ticket_tier_General_works_with_General():
    result = get_ticket_tier("TK112345")
    assert result == "General"

def test_get_ticket_tier_General_works_with_3():
    result = get_ticket_tier("TK312345")
    assert result == "General"

def test_get_ticket_tier_General_works_with_4():
    result = get_ticket_tier("TK412345")
    assert result == "VIP"

def test_get_ticket_tier_General_works_with_VIP():
    result = get_ticket_tier("TK512345")
    assert result == "VIP"

def test_get_ticket_tier_General_works_with_6():
    result = get_ticket_tier("TK612345")
    assert result == "VIP"

def test_get_ticket_tier_General_works_with_7():
    result = get_ticket_tier("TK712345")
    assert result == "Platinum"

def test_get_ticket_tier_General_works_with_Platinum():
    result = get_ticket_tier("TK812345")
    assert result == "Platinum"

def test_get_ticket_tier_General_works_with_9():
    result = get_ticket_tier("TK912345")
    assert result == "Platinum"

def test_get_ticket_tier_invalid_if_num_not_0_to_9():
    with pytest.raises(ValueError):
        get_ticket_tier("TK-12345")
