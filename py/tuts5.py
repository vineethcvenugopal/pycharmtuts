investment = input('Enter your investment money: ')
interest = input('Enter the expected interest rate: ')

investment = float(investment)
interest = float(interest) * .01

for i in range(10):
    investment = investment + (investment * interest)

print("Your investment after 10 years: {:.2f}".format(investment))
