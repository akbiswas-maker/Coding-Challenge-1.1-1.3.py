#SpinCycle Rentals wants to give customers a cost estimate for renting a bike.
#Build a program that asks for the type of bike, number of hours, and whether a helmet is needed.
#It should calculate the full cost and display a detailed receipt.
while True:
    h = input("Would you like a standard or ebike? ").lower()
    if h != 'ebike' and h != 'standard':
        print('Please choose either standard or ebike.')
    elif h == 'ebike':
        g = 3
        break
    elif h == 'standard':
        g = 1
        break
while True:
    a = float(input('How many hours would you like to rent it for? '))
    if type(a) == float:
        break
    else:
        print('Please enter a number.')
while True:
    b = input('Would you like a helmet? Please enter "Yes" or "No" ').lower()
    if b == 'yes':
        c = 2
        break
    if b == 'no':
        c = 0
        break
    else:
        print('Please enter "Yes" or "No".')
base=g*a
total=(g*a*1.2)+c
print('Your chosen bike type was $', g, ' for', a, ' hours.')
print('Your base cost is $', base)
if b == 'yes':
    print('The helmet fee is $', c)
print('The VAT is 20% which is added to your total cost.')
print('Your total cost is $', total)
exit()
