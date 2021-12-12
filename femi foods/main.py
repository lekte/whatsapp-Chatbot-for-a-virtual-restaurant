from twilio.rest import Client 

    
while True:
    food = input("You: ")
    #total=print(small_zobo,big_zobo)
    if 'hi' in food.lower():
        print("What do you want to order? Here is our menu")
        print("MENU:\nMilk=50 each\nZobo(small)=50\nZobo(big)=100")
    elif 'order' in food.lower():
        small_zobo=input("Input ALL you want to order here: ")
        print(small_zobo)
        print("Confirm this is your order, if it is type yes if not type no")
    elif 'yes' in food.lower():
        print(small_zobo)
        adddress=input("Please insert the address you want your order to be delivered: ")
        print(small_zobo)
        print(adddress)
        Namer=input("Please type in your full name so our delivery man can easily find you: ")
        phone_no=input("Please input your phone number here(for easy contact from our agent: ")
        print(small_zobo)
        print(adddress)
        print(phone_no)
        print(Namer)
    


 

                                   
            
            
            

        method=input("What payment method do you want to use(cash or bank): ")
        if "cash" in method.lower():
            print(small_zobo)
            print(adddress)
            print(phone_no)
            print(Namer)
            #print("Confirm this your order, if it is respond with y if not respond with n")
            if 'y' in food.lower():
                account_sid = 'YOUR SID' 
                auth_token = 'YOUR AUTH TOKEN' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=(small_zobo+' '+ adddress+ " "+phone_no+' '+Namer+" "+ 'CASH'),
                                            to='whatsapp:+2348033335209'
                )
                                    
            print("Your order has been validated")
            print(message.sid)            
            print("We will be at your place very soon\nThanks for shopping with Kudi Gold")        
        elif 'bank' in method.lower():
            print("FCMB\nFirst Bank\nUBA\nAccess bank\nDiamond Bank")
            which_bank=input("Which of this bank is registered with your number: ")
            if "fcmb" in which_bank.lower():
                fcmb=input("Amount here: ")
                print("Dail the code below and make transfer to our bank account(3348)")
                print("Dial " +'*329*'+fcmb+'*3348#')
                account_sid = 'AC83aa161e033a13842ee67b876d325f1d' 
                auth_token = '2fa9f759c051c60b8d2c398780766a91' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=('ORDER:'+small_zobo+' '+'ADDRESS:'+ adddress+ " "+'PHONE NUMBER:'+phone_no+' '+'CUSTOMERS NAME:'+Namer+" "+ "PAYMENT METHOD:"+'BANK: First Bank'),
                                            to='whatsapp:+2348033335209'
                )
                print("Your order is being validated!!\nThanks for shopping with us")
            if "first" in which_bank.lower():
                fcmb=input("Amount here: ")
                print("Dail the code below and make transfer to our bank account(3348)")
                print("Dial " +'*329*'+fcmb+'*3348#')
                account_sid = 'AC83aa161e033a13842ee67b876d325f1d' 
                auth_token = '2fa9f759c051c60b8d2c398780766a91' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=('ORDER:'+small_zobo+' '+'ADDRESS:'+ adddress+ " "+'PHONE NUMBER:'+phone_no+' '+'CUSTOMERS NAME:'+Namer+" "+ "PAYMENT METHOD:"+'BANK: First Bank'),
                                            to='whatsapp:+2348033335209'
                )
                print("Your order is being validated!!\nThanks for shopping with us")
            if "uba" in which_bank.lower():
                fcmb=input("Amount here: ")
                print("Dail the code below and make transfer to our bank account(3348)")
                print("Dial " +'*919*4*'+'*3348*'+fcmb+'#')
                account_sid = 'AC83aa161e033a13842ee67b876d325f1d' 
                auth_token = '2fa9f759c051c60b8d2c398780766a91' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=('ORDER:'+small_zobo+' '+'ADDRESS:'+ adddress+ " "+'PHONE NUMBER:'+phone_no+' '+'CUSTOMERS NAME:'+Namer+" "+ "PAYMENT METHOD:"+'BANK: UBA'),
                                            to='whatsapp:+2348033335209'
                )
                print("Your order is being validated!!\nThanks for shopping with us")
            if "diamond" in which_bank.lower():
                fcmb=input("Amount here: ")
                print("Dail the code below and make transfer to our bank account(3348)")
                print("Dial " +'*426*'+fcmb+'*3348#')
                account_sid = 'AC83aa161e033a13842ee67b876d325f1d' 
                auth_token = '2fa9f759c051c60b8d2c398780766a91' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=('ORDER:'+small_zobo+' '+'ADDRESS:'+ adddress+ " "+'PHONE NUMBER:'+phone_no+' '+'CUSTOMERS NAME:'+Namer+" "+ "PAYMENT METHOD:"+'BANK: DIAMOND BANK'),
                                            to='whatsapp:+2348033335209'
                )
                print("Your order is being validated!!\nThanks for shopping with us")
        '''if "diamond" in which_bank.lower():
                fcmb=input("Amount here: ")
                print("Dail the code below and make transfer to our bank account(3348)")
                print("Dial " +'*426*'+fcmb+'*3348#')
                account_sid = 'AC83aa161e033a13842ee67b876d325f1d' 
                auth_token = '2fa9f759c051c60b8d2c398780766a91' 
                client = Client(account_sid, auth_token) 
                message = client.messages.create(
                                            from_='whatsapp:+14155238886',  
                                            body=('ORDER:'+small_zobo+' '+'ADDRESS:'+ adddress+ " "+'PHONE NUMBER:'+phone_no+' '+'CUSTOMERS NAME:'+Namer+" "+ "PAYMENT METHOD:"+'BANK: DIAMOND BANK'),
                                            to='whatsapp:+2348033335209'
                )
                print("Your order is being validated!!\nThanks for shopping with us")'''
    else:
        print("I don't understand")


        '''big_zobo=input()
    Milk=input()
    
 

 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hi',      
                              to='whatsapp:+2348033335209' 
                          ) 
 
print(message.sid)
    
    '''
