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

def test_calculate_total_works():
    result = calculate_total([1.23,4.56,2.12,8.21], 0.2)
    assert result == 12.90

def test_calculate_total_works_no_discount():
    result = calculate_total([1.23,4.56,2.12,8.21], 0.0)
    assert result == 16.12

def test_calculate_total_works_with_full_discount():
    result = calculate_total([1.23,4.56,2.12,8.21], 1.0)
    assert result == 0

def test_calculate_total_doesnt_work_with_no_items():
    with pytest.raises(ValueError):
        calculate_total([], 0.1)

def test_calculate_total_doesnt_work_with_discount_out_of_range():
    with pytest.raises(ValueError):
        calculate_total([1.23,4.56,2.12,8.21], 1.2)

def test_calculate_total_doesnt_work_if_prices_not_list():
    with pytest.raises(TypeError):
        calculate_total((1.23,1.22,1.24), 1.2)
