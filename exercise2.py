import os

kitty = 500


#Read load_requests.txt into a list & remove carraige returns
with open("C:/Users/clair/OneDrive/Documents/Python Course 2025/loan_requests.txt") as requestsFile:
    requests = requestsFile.readlines()
    requests = [line.strip() for line in requests]

#Run program until kitty cleared to zero
while kitty > 1 :
    #Open file in append mode to write to bottom of file
    with open("C:/Users/clair/OneDrive/Documents/Python Course 2025/loan_requests.txt","a") as requestsFile:
        
        for request in requests:
            request = int(request)
            # full payment available
            if request  < kitty:
                print(f"{request} - Paid!")
                requestsFile.write(f"Request of {request} paid in full.\n")
                kitty = kitty - request
                
            elif kitty != 0:
            # part payment available
                print(f"{request} request cannot be processed in full (Insufficient funds available). Amount paid : {kitty}")
                requestsFile.write(f"Request of {request} could not be paid in full. Partial payment of {kitty} made.\n")
                kitty = 0
                
            else:
            # no payment available
                print(f"Request of {request} is UNPAID")
                requestsFile.write(f"Outstanding Request: {request}\n")












            

    

