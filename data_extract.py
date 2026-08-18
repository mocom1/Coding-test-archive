def solution(data, ext, val_ext, sort_by):
    fix_data = [[]]
    new_data = [[]]


    
    if ext == "code":
        target  = 0
    elif ext == "date":
        target = 1
    elif ext == "maximum":
        target = 2
    elif ext == "remain":
        target = 3

    #1 솎아내기
    for i in range(len(data)):
        if data[i][target] < val_ext:
            fix_data.append(data[i])



    #2 정렬하기
    if sort_by == "code":
        sig = 0
    elif sort_by == "date":
        sig = 1
    elif sort_by == "maximum":
        sig = 2
    elif sort_by == "remain":
        sig = 3


    for i in range(len(fix_data)):
        temp_data = fix_data[0]
        storage_num = 0
        for j in range(len(fix_data)):
            if fix_data[j][sig] < temp_data[sig]:
                temp_data = fix_data[j]
                storage_num = j
        new_data.append(temp_data)
        fix_data.pop(storage_num)        

    answer = new_data
    return answer