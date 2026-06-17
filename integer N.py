import sys

def print_binary_pattern():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        n = int(input_data[0])
        for i in range(n):
        length = n - i
         if i % 2 == 0:
             char = '1'
             else:
                 char = '0'
                 print(char * length)
                 if __name__ == '__main__':
                     print_binary_pattern()
