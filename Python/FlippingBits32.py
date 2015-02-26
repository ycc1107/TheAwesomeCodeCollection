def flippingBits(a):
    # format bit. if no longer then 32 bits then fill with 0 
    bitA = [i for i in '{0:032b}'.format(a)]
    mask = [1]*len(bitA)
    resultLst = [ str(int(a)^int(b)) for a,b in zip(bitA,mask)]
    result = int(''.join(resultLst),2)
    return result
