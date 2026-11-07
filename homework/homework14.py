# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False
# YOUR CODE HERE
# Start a while loop that runs while valid is False (while not valid).
while not valid:

    
    
    

    # ---------- PART 2: input and calculation ----------
    # YOUR CODE HERE
    # Start a try block. Inside it:
    try:
        bill = float(input("Enter the bill amount: "))
        discount_percent = float(input("Enter the discount percent: "))
        num_people = int(input("Enter the number of people: "))

        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        amount_per_person = final_bill / num_people

    #   Ask for the bill, and turn it into a number with float().
    #   Ask for the discount percent, and turn it into a number with float().
    #   Ask for the number of people, and turn it into a whole number with int().
    #   Work out the discount amount, the final bill and what each person pays.

    # ---------- PART 3: handle errors ----------
    # YOUR CODE HERE
    except ValueError:
        print("Please type numbers only.")
    except ZeroDivisionError:
        print("The number of people cannot be 0.")
    # except ValueError: print a message about typing numbers only.
    # except ZeroDivisionError: print a message that people cannot be 0.

    # ---------- PART 4: else and finally ----------
    # YOUR CODE HERE
    else:
        print(f"The final bill is: ${final_bill:.2f}")
        print(f"Each person pays: ${amount_per_person:.2f}")
        valid = True
        print("Attempt finished.")
    # else: print the final bill and what each person pays, then set valid = True.
    # finally: print "Attempt finished."
