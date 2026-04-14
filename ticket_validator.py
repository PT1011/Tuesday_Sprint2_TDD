def validate_ticket(code):
    pass

def get_ticket_tier(code):
    if code[2] == "0" or code[2] == "1" or code[2] == "2" or code[2] == "3":
        return "General"
    elif code[2] == "4" or code[2] == "5" or code[2] == "6":
        return "VIP"
    elif code[2] == "7" or code[2] == "8" or code[2] == "9":
        return "Platinum"
    else:
        raise ValueError("Ticket needs to have a number from 0-9 after TK")

def calculate_total(prices, discount=0):
    pass
