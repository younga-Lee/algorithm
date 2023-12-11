def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    data_name = ['code', 'date' , 'maximum' ,'remain']
    new_data = []
    for i in range(len(data)):
        if data[i][data_name.index(ext)] < val_ext:
            new_data.append(data[i])
    return sorted(new_data, key= lambda x : x[data_name.index(sort_by)])