# Finding state with split ==========================================================================
def get_state(address):
    return address.split(', ')[2].split()[0]

address = "27 O'Brien Place, Brooklyn, NY 11208"
state = get_state(address)
# print(state)

# Making text uppercase and reversed =================================================================
def uppercase_and_reverse(text):
    uppercase_text = text.upper()
    reversed_text = uppercase_text[::-1]
    return reversed_text
    
upper_and_reverse = uppercase_and_reverse("Jo is the best!")
#print(upper_and_reverse)

# Future money value fx ===============================================================================
def future_value(present_value, rate, periods):
    return round(present_value * (1 + rate) ** periods, 2) # round to nearest whole number

# print(future_value(1000, .1, 5))

    # print(round(present_value * (1 + rate) ** periods, 2)) # round to 2 decimal places & print

# future_value(1000, .1, 5)

present_value = float(input("What is the current dollar value? "))
rate = float(input("What is the current rate of return? "))
periods = int(input("How many years will you save this money? "))
print("$", future_value(present_value, rate, periods))