import itertools
import numpy as np
from tqdm import tqdm

# A -> 1
# B -> 2
# C -> 3
# D -> 4

all = list(itertools.product([1,2,3,4],repeat=10))

# for ans in tqdm(all):
for ans in all:
    # condition 1
    cond1_flg = True;

    # condition 2
    if(ans[1] == 1):
        cond2_flg = ans[5 - 1] == 3
    elif(ans[1] == 2):
        cond2_flg = ans[5 - 1] == 4
    elif(ans[1] == 3):
        cond2_flg = ans[5 - 1] == 1
    else:
        cond2_flg = ans[5 - 1] == 2

    if(cond2_flg == False): continue

    # condition 3
    set_, indx, count = np.unique([ans[2],ans[5],ans[1],ans[3]], return_counts=True,return_index=True)

    if ((1 not in count) or len(set_)!=2):
        continue
    else:
        index_of_single = count.argmin()
        single_one = indx[index_of_single]
        if (ans[2] == 1):
            cond3_flg = single_one == 0
        elif(ans[2] == 2):
            cond3_flg = single_one == 1
        elif (ans[2] == 3):
            cond3_flg = single_one == 2
        elif (ans[2] == 4):
            cond3_flg = single_one == 3

    if (cond3_flg == False): continue


    # condition 4
    a_true = ans[0] == ans[4]
    b_true = ans[1] == ans[6]
    c_true = ans[0] == ans[8]
    d_true = ans[5] == ans[9]

    if (ans[3] == 1):
        cond4_flg = a_true and (not b_true) and (not c_true) and (not d_true)
    elif(ans[3] == 2):
        cond4_flg = (not a_true)  and ( b_true) and (not c_true) and (not d_true)
    elif (ans[3] == 3):
        cond4_flg = (not a_true)  and (not b_true) and ( c_true) and (not d_true)
    elif (ans[3] == 4):
        cond4_flg = (not a_true) and (not b_true) and (not c_true) and ( d_true)

    if (cond4_flg == False): continue

    # condition 5
    if (ans[4] == 1):
        cond5_flg = ans[4] == ans[7]
    elif(ans[4] == 2):
        cond5_flg = ans[4] == ans[3]
    elif (ans[4] == 3):
        cond5_flg = ans[4] == ans[8]
    elif (ans[4] == 4):
        cond5_flg = ans[4] == ans[6]

    if (cond5_flg == False): continue

    # condition 6
    if (ans[5] == 1):
        cond6_flg = ans[1]==ans[3]==ans[7]
    elif (ans[5] == 2):
        cond6_flg = ans[0]==ans[5]==ans[7]
    elif (ans[5] == 3):
        cond6_flg = ans[2]==ans[9]==ans[7]
    elif (ans[5] == 4):
        cond6_flg = ans[4]==ans[8]==ans[7]

    if (cond6_flg == False): continue

    # condition 7
    set_, indx, count = np.unique(ans,return_index=True,return_counts=True)
    least_selected = set_[np.argmin(count)]
    if (ans[6] == 1):
        cond7_flg = least_selected == 3
    elif (ans[6] == 2):
        cond7_flg = least_selected == 2
    elif (ans[6] == 3):
        cond7_flg = least_selected == 1
    elif (ans[6] == 4):
        cond7_flg = least_selected == 4

    if (cond7_flg == False): continue

    # condition 8

    if(ans[7] == 1):
        cond8_flg = abs(ans[0] - ans[6]) > 1
    elif (ans[7] == 2):
        cond8_flg = abs(ans[0] - ans[4]) > 1
    elif (ans[7] == 3):
        cond8_flg = abs(ans[0] - ans[1]) > 1
    elif (ans[7] == 4):
        cond8_flg = abs(ans[0] - ans[9]) > 1

    if (cond8_flg == False): continue

    # condition 9
    if(ans[8] == 1):
        cond9_flg = ( (ans[0]==ans[5]) != (ans[5]==ans[4]) )
    elif (ans[8] == 2):
        cond9_flg = ((ans[0] == ans[5]) != (ans[9] == ans[4]))
    elif (ans[8] == 3):
        cond9_flg = ((ans[0] == ans[5]) != (ans[1] == ans[4]))
    elif (ans[8] == 4):
        cond9_flg = ((ans[0] == ans[5]) != (ans[8] == ans[4]))

    if (cond9_flg == False): continue

    # condition 10
    set_, count = np.unique(ans,return_counts=True)
    diff = max(count) - min(count)

    if (ans[9] == 1):
        cond10_flg = diff == 3
    elif (ans[9] == 2):
        cond10_flg = diff == 2
    elif (ans[9] == 3):
        cond10_flg = diff == 4
    elif (ans[9] == 4):
        cond10_flg = diff == 1
    if (cond9_flg == False): continue
    else:
        print([chr(64+i) for i in ans])

