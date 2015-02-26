'''
You will be given a list of 32 bits unsigned integers. 
You are required to output the list of the unsigned integers you get by 
flipping bits in its binary representation 
(i.e. unset bits must be set, and set bits must be unset).
'''

def flippingBits(a):
    # format bit. if no longer then 32 bits then fill with 0 
    bitA = [i for i in '{0:032b}'.format(a)]
    mask = [1]*len(bitA)
    resultLst = [ str(int(a)^int(b)) for a,b in zip(bitA,mask)]
    result = int(''.join(resultLst),2)
    return result
