def price_of_sell(price, sell = 5,is_vip = False):
    end = None
    procent  = sell*0.01
    if is_vip == True:
        end = price - price * procent
    else:
        end = price
    return end
load = price_of_sell(100,is_vip = True)
print(load)
