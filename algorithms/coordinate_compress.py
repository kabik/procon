# 座標圧縮
def compress(v):
    sorted_v = sorted(list(set(v)))
    num_index = {}
    index_num = {}
    for i in range(len(sorted_v)):
        num_index[sorted_v[i]] = i
        index_num[i] = sorted_v[i]
    return num_index,index_num
