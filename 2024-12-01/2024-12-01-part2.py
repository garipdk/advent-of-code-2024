import sys

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
                    list_a.append(int(two_strings[0]))
                    list_b.append(int(two_strings[1]))
            
            for a in list_a:
                num_a_in_list_b = list_b.count(a)
                
                if a != 0 and num_a_in_list_b > 0:
                    result += (a * num_a_in_list_b)
    
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")