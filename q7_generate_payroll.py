# Get user input
name = input("Enter name: ")
hours = input("Enter number of hours worked weekly: ")
pay_rate = input("Enter hourly pay rate: ")
cpf_rate = input("Enter CPF contribution rate (%): ")

# Check if inputs are numbers and convert them to float
def process_input():
    global hours, pay_rate, cpf_rate
    try:
        hours=float(hours)
        pay_rate=float(pay_rate)
        cpf_rate=float(cpf_rate)
        return True
    except ValueError:
        return False

if process_input():

    # Calculations
    gross_pay = hours*pay_rate
    cpf_contribution = (cpf_rate/100)*gross_pay
    net_pay = gross_pay-cpf_contribution

    # Print payroll, monetary and temporal values are to 2 d.p.
    print("\nPayroll statement for {0}\nNumber of hours worked in week: {1:.2f}\nHourly pay rate: ${2:.2f}\nGross pay: ${3:.2f}\nCPF contribution at {4:.0f}%: ${5:.2f}\n\nNet pay: ${6:.2f}".format(name, hours, pay_rate, gross_pay, cpf_rate, cpf_contribution, net_pay))
else:
    print("Invalid input")