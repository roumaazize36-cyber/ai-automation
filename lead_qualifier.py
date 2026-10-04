name = input("What is the lead's name? ")
budget = float(input("What is their budget (€)? "))
ready_to_buy = input("Are they ready to buy? (yes/no) ")
if budget >= 100000 and ready_to_buy == "yes":
    qualification = "HOT"
elif budget >= 50000 or ready_to_buy == "yes":
    qualification = "WARM"
else:
    qualification = "COLD"

print()
print(f"Lead: {name}")
print(f"Qualification: {qualification}")
if qualification == "HOT":
    action = "Contact immediately"
elif qualification == "WARM":
    action = "Follow up within 24 hours"
else:
    action = "Add to nurture list"

print(f"Recommended action: {action}")