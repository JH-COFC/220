def calc_monthly_interest():
    print("This program computes the monthly interest charge of an account.")
    interest=eval(input("What is the % APR?"))/1200
    billing_cycle = eval(input("How many days are in the billing cycle?"))
    net_balance = eval(input("What is the net balance of the account?"))
    net_payment = eval(input("What amount was the net payment recieved?"))
    payment_date = (eval(input("What day was the payment recieved?")))
    step1 = net_balance * billing_cycle
    step2 = net_payment * (billing_cycle - payment_date)
    step3 = step1-step2
    average = step3/billing_cycle
    print("The monthly interest charge is: $",(average*interest))