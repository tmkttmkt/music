import numpy as np

#教師データ
date_x=np.array([[0,1,2,3],[1,1,2,3],[0,1,1,0],[1,1,3,2]])
#入力でーた
_y=["a","b","c","d"]

_y_=map(lambda x:ord(x)-ord("a"),_y)
date_y=np.array(list(_y_))
print(date_y)




