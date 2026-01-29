# AIM: Write a Python program to calculate the gross salary of an employ
# Coder:Tasmin 
# Date:16/01/2026

# write your code here

print("salary calculator:")
BS= float(input("Enter the Basic salary:"))
DA = (70/100)*BS
TA = (30/100)*BS
HRA = (10/100)*BS
Gross_salary =BS+ DA + TA + HRA



print("salary details:")
print( "Basic salary:",BS)
print("DA(70%):", (DA))
print("TA(30%):", (TA))
print("HRA(10%):", (HRA))
print("Gross_salary:", (Gross_salary))
