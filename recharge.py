def recharge(num,plan):
    if len(num)< 10:
        raise ValueError("invalid number")
    elif (plan==149) or (plan==669):
        print("recharge succesful")

recharge("988418092",669)
    
