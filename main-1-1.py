def linear_search_product(productlist,targetproduct):
    indices=[]
    for index,product in enumerate(productlist):
 
        if product== targetproduct:
            indices.append(index)
        return indices
products=['pen','pencil','paper','eraser','book','sharpner'] 
target=input("Enter the element to be searched: ")  
result=linear_search_product(products, target)
print("The index of ",target," is" ,result)          