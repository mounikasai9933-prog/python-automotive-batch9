class BankAccount:
    def __init__(self, name, age, principal, time):
        self.name = name
        self.age = age
        self.principal = principal
        self.time = time
        self.rate = 8  # 8% per annum

    def calculate_ci(self):
        try:
            if self.age < 60:
                raise ValueError("Interest is applicable only for senior citizens (age ≥ 60)")

            # CI formula as given
            ci = self.principal + (self.principal * self.rate * self.time) / 100
            return ci

        except ValueError as e:
            return e
try:
    name = input("Enter account holder name: ")
    age = int(input("Enter age: "))
    principal = float(input("Enter principal amount: "))
    time = int(input("Enter time (in years): "))

    account = BankAccount(name, age, principal, time)
    result = account.calculate_ci()

    print("Result:", result)

except Exception as e:
    print("Invalid input:", e)