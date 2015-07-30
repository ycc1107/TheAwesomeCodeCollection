lstNeedOrder = ['usd/yen/','yen/cny','nwd/chf','usd/cny','yen/chf','usd/chf']
lst = ['usd','cny','yen','chf']
order = {ch: i for i, ch in enumerate(lst)}
         
def sort_key(x):
    a, b = x.split('/')
    return order.get(a, len(lst)), order.get(b, len(lst))

res = sorted(lstNeedOrder, key=sort_key)
