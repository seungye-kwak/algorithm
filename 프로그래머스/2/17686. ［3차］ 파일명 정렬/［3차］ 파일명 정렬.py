def solution(files) :
    answer = []
    
    temp = []
    for file in files :
        for w in range(len(file)) :
            if file[w].isdigit() :
                head = file[:w]
                number = file[w:]
                break
            
        for n in range(len(number)) :
            if number[n].isdigit()==False :
                tail = number[n:]
                number = number[:n]
                break
            
        if number == file[w:] :
            tail = ''
        
        temp.append([head, number, tail])
        
    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    print(temp)
    
    for nm in temp :
        new_nm = ''.join(nm)
        answer.append(new_nm)
        
    return answer