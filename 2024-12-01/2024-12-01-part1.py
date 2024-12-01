import sys

def main(filepath):
    list_a = []
    list_b = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            two_strings = line.split("   ")
            if len(two_strings) == 2:
                list_a.append(int(two_strings[0]))
                list_b.append(int(two_strings[1]))
            
    result = 0
    
    if len(list_a) == len(list_b):
        list_a.sort()
        list_b.sort()
        
        for i, a in enumerate(list_a):
            b = list_b[i]
            
            if a > b:
                (a, b) = (b, a)
            result += (b - a)
    
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")