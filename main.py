def isInteger(presunta_stringa: str) -> bool:
    try:
        if not(float(presunta_stringa).is_integer()):
            return False
        return True
    except ValueError:
        return False

def get_integers_list() -> list[int]:
    length:str
    while not (isInteger(length:=input("Enter a valid length: ")) and int(float(length))>=0):
        print("Invalid length!")
    integers_list:list[int]=[]
    while len(integers_list) != int(float(length)):
        if isInteger(integer:=input("Enter an integer: ")):
            integers_list.append(int(float(integer)))
    return integers_list

def isSublist(smaller_list: list[int], larger_list: list[int]) -> bool:
    if len(smaller_list)==0: 
        return True
    if smaller_list[0] not in larger_list: 
        return False        
    for j,i in enumerate(range(len(smaller_list)), larger_list.index(smaller_list[0])):
        if smaller_list[i]!=larger_list[j]:
            return False
    return True

def main():
    print("Enter integers into the smaller list:")
    smaller_list=get_integers_list()
    print("Enter integers into the larger list:")
    larger_list=get_integers_list()
    
    if len(smaller_list)<=len(larger_list):
        if isSublist(smaller_list, larger_list):
            print(f"The list {smaller_list} is a sublist of {larger_list}")  
        else:
            print(f"The list {smaller_list} is not a sublist of {larger_list}")
    else:
        print("The length of the smaller list is greater than that of the larger list!")        

       
if __name__=="__main__":
    main()