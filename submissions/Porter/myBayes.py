import traceback

from submissions.Porter import billionaires



class DataFrame:
    data = []
    feature_names = []
    target = []
    target_names = []

Frame = DataFrame()
Frame.data = []




billionaires = billionaires.get_billionaires()


'''
Build the input frame, row by row.
'''
# for countyST in intersection:
#     # choose the input values
#     billionairesPIG.data.append([
#         # countyST,
#         # intersection[countyST]['ST'],
#         # intersection[countyST]['Trump'],
#         intersection[countyST]['Elderly'],
#         intersection[countyST]['College'],
#         intersection[countyST]['Home'],
#         intersection[countyST]['Poverty'],
#     ])

def gender(string):
    if string == "male":
        return 1
    if string == "female":
        return 2
    else:
        return 0
def political(value):
    if value:
        return 1
    else:
        return 0
# def worth(number):
#     if value
#         return 1
#     else:
#         return 0



for x in billionaires:
    Frame.target.append(gender(x['demographics']['gender']))
    if x['wealth']['worth in billions'] > 2:
        Frame.data.append([
        political(x['wealth']['how']['was political']),
        1,
            0
        ])
    else:
        Frame.data.append([
            political(x['wealth']['how']['was political']),
            0,
            1,
        ])



Frame.feature_names = ['Political','Worth > 2 billion','Worth <= 2 billion']

'''
Build the target list,
one entry for each row in the input frame.

The Naive Bayesian network is a classifier,
i.e. it sorts data points into bins.
The best it can do to estimate a continuous variable
is to break the domain into segments, and predict
the segment into which the variable's value will fall.
In this example, I'm breaking Trump's % into two
arbitrary segments.
'''
# billionairesPIG.target = []

# def trumpTarget(percentage):
#     if percentage > 45:
#         return 1
#     return 0

# for countyST in intersection:
#     # choose the target
#     tt = trumpTarget(intersection[countyST]['Trump'])
#     trumpECHP.target.append(tt)

Frame.target_names = ['Male', 'Female', 'Not Stated']

Examples = {
    'Billionaires': Frame
}