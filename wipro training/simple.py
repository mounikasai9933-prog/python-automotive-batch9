def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("----- Simple Interest Calculator -----")
    
    # Taking inputs
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest (% per annum): "))
T = float(input("Enter the time period (years): "))
    
SI = calculate_simple_interest(P, R, T)

print(f"\nSimple Interest for Principal = {P}, Rate = {R}%, Time = {T} years is: {SI}")