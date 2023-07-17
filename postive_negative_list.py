num_list = [-1,-2,-3,1,2,3]

def postive(x): return x > 0
def negative(x): return x < 0

positive_list = list(filter(postive,num_list))
negative_list = list(filter(negative,num_list))

print(positive_list,negative_list)