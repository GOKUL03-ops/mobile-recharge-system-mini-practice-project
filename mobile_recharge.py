class mobile_recharge:

    def __init__(self):
        self.gst_rate=18
        self.plan_amount=0

        self.plans= [
                    {"id": 1, "amount": 199, "validity": 24, "data": 1.0, "talktime": 50},
                    {"id": 2, "amount": 299, "validity": 28, "data": 1.5, "talktime": 100},
                    {"id": 3, "amount": 399, "validity": 56, "data": 2.0, "talktime": 100}]
             
    def get_number(self):
         while True:
            number=input("Enter your mobile number:").strip()
            if number.startswith("9") and len(number)==10 and number.isdigit():
                print("jio")
                break
            elif number.startswith("8") and len(number)==10 and number.isdigit():
                print("Aritel")
                break
            elif number.startswith("7") and len(number)==10 and number.isdigit():
                print("vi")
                break
            elif number.startswith("6") and len(number)==10 and number.isdigit():
                print("BSNL")
                break
        
            else:
                if number not in ('9','8','7','6'):
                    print("invalid sim number")



    def choose_plan(self):
        while True:
            plan_id = int(input("\nChoose Plan ID: "))

            for p in self.plans:
                if p["id"] == plan_id:
                    self.plan_amount = p["amount"]
                    print("\nSelected Plan")
                    print(p)
                    return

            print("Invalid Plan ID")

    def show_plans(self):
        print("\nAvailable Recharge Plans")
        print("-" * 40)

        for p in self.plans:
            print(f"ID:{p['id']} | ₹{p['amount']} | {p['validity']} Days | {p['data']} GB/Day | Talktime ₹{p['talktime']}")




    def calculate_gst(self):

        return (self.plan_amount * self.gst_rate) / 100
    


    def calculate_total(self):
            return self.plan_amount + self.calculate_gst()
                    
                    
    def transaction(self):
        upi = ("GPAY", "PHONEPAY", "PAYTM")

        payment = input("Choose payment method (Gpay/PhonePe/Paytm): ").upper()

        if payment in upi:
            print("\nPayment Successful")
        else:
            print("\nInvalid UPI")
            return

        

        gst = self.calculate_gst()
        total = self.calculate_total()

        print("\n------- BILL -------")
        print(f"Plan Amount : ₹{self.plan_amount}")
        print(f"GST (18%)   : ₹{gst:.2f}")
        print(f"Total Amount: ₹{total:.2f}")
        print("--------------------")
        print("Recharge Successful")


obj = mobile_recharge()
obj.get_number()
obj.show_plans()
obj.choose_plan()
obj.transaction()




                    

