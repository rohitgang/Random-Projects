import pandas as pd
import numpy as np
import pickle
import json

def parseOutput (directory, input, output):
    # THE psd_dir SHOULD BE THE DIRECTORY OF THE INPUT FILE FOR MODEL TRAINING
    psd_dir = directory              #'data/' #mrp/2019/training/psd/

    # THE input CAN BE CHANGED TO THE NAME OF THE INPUT FILE
    df = pd.read_json(psd_dir + input, lines=True)

    # THE output FILE SHOULD BE THE MODEL'S OUTPUT
    with open(psd_dir + output, 'rb') as pk:
        data= pickle.load(pk)

    output= list()
    example= r""
    for i in range(len(df)) :
        example= '{"id": "'+df['id'][i]+'", "flavor": 0, "framework": "psd", "version": 1.0, "time": "'+df['time'][i]+'", "input": "' #+ df['input'][i]+'", "nodes":['
        startIndex= df['input'][i].find('"')
        INPUT= ''
        temp = df['input'][i]
        if startIndex != -1:
            temp= temp.replace('\"', '\\"') #"tops": [1], "n
            example = example + temp + '", "tops": [0], "nodes":['
        elif startIndex == -1:
            example = example + temp + '", "tops": [0], "nodes":['
        j= 0
        len_lst= len(data.nodes[i])
        for el in data.nodes[i]:
            example = example + json.dumps(el,ensure_ascii=True)
            if j+1 < len_lst:
                example= example + ','
            j+= 1
        example= example + '], "edges": ['
        for ed in data.edges[i]:
            example= example + json.dumps(ed,ensure_ascii=True)
            example= example + ','
        example= example[:-1]
        example= example + ']}\n'
        output.append(example)
        example= ''

    with io.open('Output_validation.mrp', 'w', encoding="utf-8") as f:
        for el in output:
            f.write(el)
