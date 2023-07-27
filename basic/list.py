if __name__ == '__main__':
    N = int(input())
    nmbr_list = []
    
    
    for n in range(N):
        cmd = input()
        if cmd.startswith('append'):
            arr = cmd.split(' ')
            arr.remove(arr[0])
            #list(map(int,x)) converts the list into integer
            p = list(map(int,arr))         
            nmbr_list.append(p[0])
            
        elif cmd.startswith('sort'):
            nmbr_list.sort()
        
        elif cmd.startswith('reverse'):
            nmbr_list.reverse()
    
        elif cmd.startswith('pop'):
            nmbr_list.pop()
    
        elif cmd.startswith('remove'):
            arr = cmd.split(' ') 
            arr.remove(arr[0])
            p = list(map(int,arr))   
            nmbr_list.remove(p[0])
    
        elif cmd.startswith('insert'):
            arr = cmd.split(' ')
            arr.remove(arr[0])
            p = list(map(int,arr))
            nmbr_list.insert(p[0], p[1])
        
        elif cmd.startswith('print'):
            print(nmbr_list) 
    
    
    
