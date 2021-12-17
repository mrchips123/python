# this is a tax calculator
# you can enter the purchase amount
# it will calculate the amount with a tax of 6%

condition = bool(True)
while condition:

    print('- - - starting calculator - - -')
    amount = int(input('Enter the purchase amount: '))
    tax = .06
    total = amount + amount*tax
    print(total)

    print('Hit \'0\' to exit')
    print('Hit any number to go again')

    recon = int(input())

    if recon != 0:
        continue
    elif recon == 0:
        condition = bool(False)
        break
print("Thanks for using me ...")