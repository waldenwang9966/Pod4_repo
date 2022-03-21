bill = float(input("Enter meal amt: "))
total_ppl_splitting = int(input("How many people are splitting the bill?: "))
tip = int(input("Enter tip in percentage: "))
tax = .1
# total tip
bill_amt_with_tip = bill * tip/100
# total tax
tax_amt = bill * tax
# total with taxes
total = bill + bill_amt_with_tip + tax_amt
# https: // thepythonguru.com/python-string-formatting/
print(input(f"Your meal is ${bill:.2f} and you chose to give a {tip} percent tip. Which equals to a ${bill_amt_with_tip:.2f} tip."))