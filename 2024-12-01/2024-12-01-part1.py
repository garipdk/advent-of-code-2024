import sys
import bisect

def main(filepath):
    result = 0
    
    with open(filepath) as f:
        if f.readline() != '':
            
            list_a = []
            list_b = []
            
            f.seek(0)
            
            for line in f:
                two_strings = line.split()
                
                if len(two_strings) == 2:
                    bisect.insort(list_a, int(two_strings[0])) 
                    bisect.insort(list_b, int(two_strings[1]))
            
            for i, a in enumerate(list_a):
                b = list_b[i]
                
                (num_min, num_max) = (a, b)
                
                if a > b:
                    (num_min, num_max) = (b, a)
                
                result += (num_max - num_min)

    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")