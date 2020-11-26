'''
CIMB: Net Interest Earned = [Average Daily Balance x No. of days in a month / 360]
x Interest Rate P.A. x [1 - Withholding tax (20%)]
Net Base Deposit Interest Payout: Average Daily Balance x No. of days in a month / 360]
x Interest Rate P.A.  (you should subtract 20% for withholding tax)

KOMO:


adb = int(input("What is your Average Daily Balance? \n"))
ipa = int(input("What is the interest rate per annum? \n"))
nmonth = int(input("How many days in this month? \n"))
ndyear = int(input("How many days per year? \n"))

#gross interest for the regular interest per annum
#withholding tax not yet taken out

baseinterest = (adb * nmonth / ndyear) * ipa/100
print("Your base interest is", end=' ')
print(baseinterest)

#net interest for regular interest per annum
#taking out withholding tax of 20% for the Philippines
netinterest = baseinterest * (1-.2)
print("Your net interest is", end =' ')
print(netinterest)

#Will ask if there is a special promo
yn = input("Is there a special promo this month? \n")
if yn.lower() == "no":
    print ("Your yearly net interest is", end=' ')
    print(netinterest*12)
    #if no special promo and just regular rate, will just print net interest rate per year
    # assuming they don't deposit anything after
else:
    sipa= float(input("What is the special promo rate in percent? \n"))
    adinterest = (adb * nmonth / ndyear) * (sipa-ipa)/100 *.8
    print("Your additional net interest is", end=' ')
    print(adinterest)
    #this asks for the special promo rate, and the difference is used to calculate net interest)

    nninterest = (adb * nmonth / ndyear) * (sipa)/100 *.8
    print("Your total net interest is", end=' ')
    print(nninterest)
    #this just shows total interest, so it uses promo rate instead of regular rate
    #also equivalent to net interest + additional net interest

    ynninterest = nninterest * 12
    print("Your total YEARLY net interest is", end=' ')
    print(ynninterest)


def finterest(adb,nmonth,ndyear,ipa):
    return(adb * nmonth / ndyear) * ipa/100 * (0.8)
'''

#VERSION 2
#IMPROVED, COMPLEX OPTION
#WILL FACTOR INTO ACCOUNT THE TYPE OF BANK

bank = input("What bank do you use? \n")
if bank.lower() =="cimb":
    type = input("GSave or UpSave? \n")
month = input("What month is it? \n")
leapyear = input("Is it a leap year? \n")
adb = int(input("What is your Average Daily Balance? \n"))
nmonth = int(input("How many days in this month? \n"))

if bank.lower() =="cimb":
    if type.lower() == "gsave":
        ipa = 3.1
    else:
        ipa = 3
    ndyear = 360

elif bank.lower() =="komo":
    if leapyear.lower() =="yes":
        ndyear = 366
    else:
        ndyear = 365
else:
    ipa = 2.5
    if leapyear.lower() =="yes":
        ndyear = 366
    else:
        ndyear = 365

#gross interest for the regular interest per annum
#withholding tax not yet taken out

baseinterest = (adb * nmonth / ndyear) * ipa/100
print("Your base interest for", month, "is", end=' ')
print(baseinterest)

#net interest for regular interest per annum
#taking out withholding tax of 20% for the Philippines
netinterest = baseinterest * (1-.2)
print("Your net interest for", month, "is", end =' ')
print(netinterest)

#Will ask if there is a special promo
yn = input("Is there a special promo this month? \n")
if yn.lower() == "no":
    print ("Your yearly net interest is", end=' ')
    print(netinterest*12)
    #if no special promo and just regular rate, will just print net interest rate per year
    # assuming they don't deposit anything after
else:
    sipa= float(input("What is the special promo rate in percent? \n"))
    adinterest = (adb * nmonth / ndyear) * (sipa-ipa)/100 *.8
    print("Your additional net interest for", month, "is", end=' ')
    print(adinterest)
    #this asks for the special promo rate, and the difference is used to calculate net interest)

    nninterest = (adb * nmonth / ndyear) * (sipa)/100 *.8
    print("Your total net interest for", month, "is", end=' ')
    print(nninterest)
    #this just shows total interest, so it uses promo rate instead of regular rate
    #also equivalent to net interest + additional net interest

    ynninterest = nninterest * 12
    print("Your total YEARLY net interest is", end=' ')
    print(ynninterest)