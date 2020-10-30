# Kitle varyansının hesaplanması

def Var(data):
    sum_x=0 # X'teki elemanların toplamı
    for i in data:
        sum_x+=i

    x_bar = sum_x/len(data)  # X'in aritmetik ortalaması

    sigma = 0  
    for deger in data:
        sigma+= (deger-x_bar)**2

    varyans = sigma/len(data)

    return varyans







