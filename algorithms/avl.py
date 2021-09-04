# https://juppy.hatenablog.com/entry/2019/02/26/python_AVL%E6%9C%A8_%E9%85%8D%E5%88%97ver_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder_

#AVL

##search(0,x):O(logN)
# xがある場合indexを、ない場合Noneを返す
def search(root,key):
    if avl_key[root] > key:
        if avl_left[root] == None:
            return None
        else:
            return search(avl_left[root],key)
    if avl_key[root] < key:
        if avl_right[root] == None:
            return None
        else:
            return search(avl_right[root],key)
    return root


##end_lower/higher:search_lower/higherで使用
def end_lower(root):
    if avl_left[root] == None:
        return avl_key[root]
    else:
        return end_lower(avl_left[root])

def end_higher(root):
    if avl_right[root] == None:
        return avl_key[root]
    else:
        return end_higher(avl_right[root])


##search_lower(0,x,None):O(logN)
# xより小さいものの中で最も大きいものを出力。ない場合はNoneを出力
def search_lower(root,key,lower_key):
    if avl_key[root] > key:
        if avl_left[root] == None:
            return lower_key
        else:
            return search_lower(avl_left[root],key,lower_key)
    if avl_key[root] < key:
        lower_key = avl_key[root]
        if avl_right[root] == None:
            return lower_key
        else:
            return search_lower(avl_right[root],key,lower_key)

    # ==
    if avl_left[root] == None:
        return lower_key
    else:
        if lower_key == None:
            return end_higher(avl_left[root])
        else:
            return max(lower_key,end_higher(avl_left[root]))

##search_higher(0,x,None):O(logN)
# xより大きいものの中で最も小さいものを出力。ない場合はNoneを出力
def search_higher(root,key,higher_key):
    if avl_key[root] > key:
        higher_key = avl_key[root]
        if avl_left[root] == None:
            return higher_key
        else:
            return search_higher(avl_left[root],key,higher_key)
    if avl_key[root] < key:
        if avl_right[root] == None:
            return higher_key
        else:
            return search_higher(avl_right[root],key,higher_key)

    # ==
    if avl_right[root] == None:
        return higher_key
    else:
        if higher_key == None:
            return end_lower(avl_right[root])
        else:
            return min(higher_key,end_lower(avl_right[root]))



##Rotation,replace,insertx:insertで使用
def DoubleRightRotation(x):
    tl = avl_left[x]
    avl_left[x] = avl_right[avl_right[tl]]
    avl_right[avl_right[tl]] = x
    tlr = avl_right[tl]
    avl_right[tl] = avl_left[tlr]
    avl_left[tlr] = tl
    if balance[tlr] == -1:
        balance[avl_right[tlr]] = 1
        balance[avl_left[tlr]] = 0
    elif balance[tlr] == 1:
        balance[avl_right[tlr]] = 0
        balance[avl_left[tlr]] = -1
    else:
        balance[avl_right[tlr]] = 0
        balance[avl_left[tlr]] = 0
    balance[tlr] = 0
    return tlr

def DoubleLeftRotation(x):
    tr = avl_right[x]
    avl_right[x] = avl_left[avl_left[tr]]
    avl_left[avl_left[tr]] = x
    trl = avl_left[tr]
    avl_left[tr] = avl_right[trl]
    avl_right[trl] = tr
    if balance[trl] == 1:
        balance[avl_right[trl]] = 0
        balance[avl_left[trl]] = -1
    elif balance[trl] == -1:
        balance[avl_left[trl]] = 0
        balance[avl_right[trl]] = 1
    else:
        balance[avl_right[trl]] = 0
        balance[avl_left[trl]] = 0
    balance[trl] = 0
    return trl

def SingleLeftRotation(x):
    tr = avl_right[x]
    balance[tr] = 0
    balance[x] = 0
    avl_right[x] = avl_left[tr]
    avl_left[tr] = x
    return tr

def SingleRightRotation(x):
    tl = avl_left[x]
    balance[tl] = 0
    balance[x] = 0
    avl_left[x] = avl_right[tl]
    avl_right[tl] = x
    return tl

def replace(x,p,v):
    if avl_left[p] == x:
        avl_left[p] = v
    else:
        avl_right[p] = v

def insertx(root,p,key):
    if avl_key[root] > key:
        if avl_left[root] == None:
            avl_key.append(key)
            avl_left[root] = len(avl_key)-1
        else:
            if not insertx(avl_left[root],root,key):
                return False
        if balance[root] == 1:
            balance[root] = 0
            return False
        elif balance[root] == 0:
            balance[root] = -1
            return True
        else:
            if balance[avl_left[root]] == 1:
                replace(root,p,DoubleRightRotation(root))
            elif balance[avl_left[root]] == -1:
                replace(root,p,SingleRightRotation(root))
            return False
    if avl_key[root] < key:
        if avl_right[root] == None:
            avl_key.append(key)
            avl_right[root] = len(avl_key)-1
        else:
            if not insertx(avl_right[root],root,key):
                return False
        if balance[root] == -1:
            balance[root] = 0
            return False
        elif balance[root] == 0:
            balance[root] = 1
            return True
        else:
            if balance[avl_right[root]] == -1:
                replace(root,p,DoubleLeftRotation(root))
            elif balance[avl_right[root]] == 1:
                replace(root,p,SingleLeftRotation(root))
            return False
    return False


##insert(0,x):O(logN)
#x追加
def insert(root,key):
    if key < avl_key[root]:
        if avl_left[root] == None:
            avl_key.append(key)
            avl_left[root] = len(avl_key)-1
        else:
            insertx(avl_left[root],root,key)
    elif key > avl_key[root]:
        if avl_right[root] == None:
            avl_key.append(key)
            avl_right[root] = len(avl_key)-1
        else:
            insertx(avl_right[root],root,key)
    else:
        pass
########################################################
##初期化（要素は一つ入れておく）

#avl_key:値,avl_left:左の子のindex,avl_right:右の子のindex
#balance[i]: {"Even":0,"Left":-1,"Right":1}

#avl_keyには初めに何か加えておく
n = 10**5
avl_key = [0]
avl_left = [None]*n
avl_right = [None]*n
balance = [0]*n

for i in range(1,n):
    insert(0,i*2)
for i in range(1,n+1):
  k = search_lower(0,i,None)
