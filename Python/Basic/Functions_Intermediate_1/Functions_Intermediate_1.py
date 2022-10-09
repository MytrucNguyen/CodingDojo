import random

def random_pick(min_num = 0, max_num = 100):
    if(min_num > max_num): 
        return False
    
    num = random.random() * max_num + min_num
    return num

print(random_pick())
print(random_pick(max_num=50))
print(random_pick(min_num=50))
print(random_pick(min_num=50, max_num=500))