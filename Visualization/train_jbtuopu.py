import json
import numpy as np
import pandas as pd

def readJSONFile(path):
    f = open(path, "r")
    return json.load(f)





def Jtopo(path):# 1 6 7 8 9 10 12 13 15 16
    # 有根因的文件路径
    trainrootfile = ['data_release/train/0.csv',
                     'data_release/train/2.csv',
                     'data_release/train/3.csv',
                     'data_release/train/5.csv',
                     'data_release/train/7.csv',
                     'data_release/train/9.csv',
                     'data_release/train/11.csv',
                     'data_release/train/13.csv',
                     'data_release/train/15.csv',
                     'data_release/train/17.csv',
                     'data_release/train/19.csv',
                     'data_release/train/21.csv',
                     'data_release/train/24.csv',
                     'data_release/train/25.csv',
                     'data_release/train/27.csv',
                     'data_release/train/29.csv',
                     'data_release/train/31.csv',
                     'data_release/train/33.csv',
                     'data_release/train/35.csv',
                     'data_release/train/37.csv',
                     'data_release/train/39.csv',
                     'data_release/train/41.csv',
                     'data_release/train/43.csv',
                     'data_release/train/46.csv',
                     'data_release/train/47.csv',
                     'data_release/train/49.csv',
                     'data_release/train/51.csv',
                     'data_release/train/53.csv',
                     'data_release/train/55.csv',
                     'data_release/train/57.csv',
                     'data_release/train/59.csv',
                     'data_release/train/61.csv',
                     'data_release/train/63.csv',
                     'data_release/train/65.csv',
                     'data_release/train/68.csv',
                     'data_release/train/69.csv',
                     'data_release/train/71.csv',
                     'data_release/train/73.csv',
                     'data_release/train/75.csv',
                     'data_release/train/77.csv',
                     'data_release/train/79.csv',
                     'data_release/train/81.csv',
                     'data_release/train/83.csv',
                     'data_release/train/85.csv',
                     'data_release/train/87.csv',
                     'data_release/train/90.csv',
                     'data_release/train/92.csv',
                     'data_release/train/94.csv',
                     'data_release/train/96.csv',
                     'data_release/train/98.csv']
    path = "data_release/train/" + path + '.csv'
    train77 = pd.read_csv(path, encoding='utf-8')
    z = train77['triggername'].to_frame()
    zz = z.triggername.str.split('\s+').str[0]
    node = zz.to_frame()['triggername'].str[7:]
    nodelist = node.tolist()
    setnodelist = list(set(nodelist))
    path1 = path[19:]
    nodes_json = readJSONFile("data_release/topology/topology_edges_node2.json")  # 这里换文件了
    train_dic = readJSONFile("./data_release/train_dic.json")

    rootrow = train77.loc[train77['is_root'] == 1]
    rootrowcolumn = rootrow['triggername'].to_frame()
    rootrowcolumnnum = rootrowcolumn.triggername.str.split('\s+').str[0]
    rootnode = rootrowcolumnnum.to_frame()['triggername'].str[7:]
    rootnodelist = rootnode.tolist()
    setrootnodelist = set(rootnodelist)
    list_setrootnodelist = list(setrootnodelist)
    if len(list_setrootnodelist) == 0:
        ztalldata = []
        for name in setnodelist:
            if name in ["50", "0", "58", "4", "83", "33", "17", "31", "15", "73", "93"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 1, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["70", "30", "45", "37", "55", "21", "18", "7", "99", "8", "91"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 2, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["57", "20", "28", "3", "97", "39", "86", "94"]:
                evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 3, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["72", "34", "81", "36", "62", "77", "69", "13", "9", "19", "27", "5"]:
                evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 4, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["14", "26", "65", "2", "76", "38", "82", "60", "6", "74", "85"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 5, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["56", "67", "25", "48", "59", "32", "35", "46", "1", "98"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 6, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["63", "53", "61", "89", "54", "24", "23", "51"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 7, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["84", "10", "49", "95", "88", "43", "41", "71", "79", "87"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 8, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["68", "16", "92", "78", "47", "75", "22", "80", "66", "12", "44"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 9, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["29", "64", "96", "42", "90", "11", "52", "40"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 10, 'draggable': 'true'}
                ztalldata.append(evdata)
        root = 'wugenyin'
        root_gj = 'wugenyin'
    else:
        ztalldata = []
        for name in setnodelist:
            if name in ["50", "0", "58", "4", "83", "33", "17", "31", "15", "73", "93"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 1, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 1, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["70", "30", "45", "37", "55", "21", "18", "7", "99", "8", "91"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 2, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 2, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["57", "20", "28", "3", "97", "39", "86", "94"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 3, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 3, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["72", "34", "81", "36", "62", "77", "69", "13", "9", "19", "27", "5"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 4, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 4, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["14", "26", "65", "2", "76", "38", "82", "60", "6", "74", "85"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 5, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 5, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["56", "67", "25", "48", "59", "32", "35", "46", "1", "98"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 6, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 6, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["63", "53", "61", "89", "54", "24", "23", "51"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 7, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 7, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["84", "10", "49", "95", "88", "43", "41", "71", "79", "87"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 8, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 8, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["68", "16", "92", "78", "47", "75", "22", "80", "66", "12", "44"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 9, 'symbol': 'arrow', 'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 9, 'draggable': 'true'}
                ztalldata.append(evdata)
            if name in ["29", "64", "96", "42", "90", "11", "52", "40"]:
                if name == list_setrootnodelist[0]:
                    evdata = {'name': name, "symbolSize": 70, "category": 10, 'symbol': 'arrow',
                              'draggable': 'true'}
                else:
                    evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 10, 'draggable': 'true'}
                ztalldata.append(evdata)
        root = list_setrootnodelist[0]  # 对应root
        dingwei = train77.loc[train77['is_root'] == 1]['triggername'].to_frame()
        root_gj = dingwei['triggername'].values[0]  # 对应root_gj

    myreturnlist = {}

    for count in range(len(setnodelist)):
        key = setnodelist[count]
        mydict = {}
        # for key in nodes_json:
        #     key=setnodelist[0]

        #         print(key)
        for valuelayp1 in nodes_json[key]:
            #         print(key+i)
            if key in setnodelist and valuelayp1 in setnodelist:
                #         print(key+valuelayp1)
                mydict.setdefault(key, []).append(valuelayp1)
                for valuelayp2 in nodes_json[valuelayp1]:
                    if valuelayp2 in setnodelist:
                        mydict.setdefault(valuelayp1, []).append(valuelayp2)
                        for valuelayp3 in nodes_json[valuelayp2]:
                            if valuelayp3 in setnodelist:
                                mydict.setdefault(valuelayp2, []).append(valuelayp3)

        mydictm = {}
        for valuelaym1 in nodes_json:
            if valuelaym1 in setnodelist:
                for value1 in nodes_json[valuelaym1]:
                    root1 = key
                    if value1 == root1:
                        mydictm.setdefault(valuelaym1, []).append(value1)

                        for valuelaym2 in nodes_json:
                            if valuelaym2 in setnodelist:
                                for value2 in nodes_json[valuelaym2]:
                                    root2 = valuelaym1
                                    if value2 == root2:
                                        mydictm.setdefault(valuelaym2, []).append(value2)

                                        for valuelaym3 in nodes_json:
                                            if valuelaym3 in setnodelist:
                                                for value3 in nodes_json[valuelaym3]:
                                                    root3 = valuelaym2
                                                    if value3 == root3:
                                                        mydictm.setdefault(valuelaym3, []).append(value3)

        for kk in mydictm:
            setvalue = set(mydictm[kk])
            mydictm[kk] = setvalue

        p = []
        for i in mydict:
            p.append(i)
            for j in mydict[i]:
                p.append(j)
        pset = set(p)
        plist = list(pset)

        q = []
        for i in mydictm:
            q.append(i)
            for j in mydictm[i]:
                q.append(j)
        qset = set(q)
        qlist = list(qset)

        pqlist = plist + qlist

        setpqlist = list(set(pqlist))

        alldata = []
        for name in setpqlist:
            if name in ["50", "0", "58", "4", "83", "33", "17", "31", "15", "73", "93"]:
                evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 1, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["70", "30", "45", "37", "55", "21", "18", "7", "99", "8", "91"]:
                evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 2, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["57", "20", "28", "3", "97", "39", "86", "94"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 3, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["72", "34", "81", "36", "62", "77", "69", "13", "9", "19", "27", "5"]:
                evdata = {'name': name, "symbolSize": 40,'symbol':'circle', "category": 4, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["14", "26", "65", "2", "76", "38", "82", "60", "6", "74", "85"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 5, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["56", "67", "25", "48", "59", "32", "35", "46", "1", "98"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 6, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["63", "53", "61", "89", "54", "24", "23", "51"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 7, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["84", "10", "49", "95", "88", "43", "41", "71", "79", "87"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 8, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["68", "16", "92", "78", "47", "75", "22", "80", "66", "12", "44"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 9, 'draggable': 'true'}
                alldata.append(evdata)
            if name in ["29", "64", "96", "42", "90", "11", "52", "40"]:
                evdata = {'name': name, "symbolSize": 40, 'symbol':'circle',"category": 10, 'draggable': 'true'}
                alldata.append(evdata)
        returnlist = {}
        returnlist['alldata'] = alldata
        myreturnlist[key] = returnlist

    for i in range(len(train_dic)):
        d = train_dic[i]
        for dict_key in d.keys():
            str_dict_key = str(dict_key)
            if (str_dict_key == path1):
                gjxx = d[path1]
    #                 print(gjxx)
    myreturnlist['gjxx'] = gjxx
    myreturnlist['ztalldata'] = ztalldata
    myreturnlist['root'] = root
    myreturnlist['root_gj'] = root_gj
    #print(myreturnlist)
    return myreturnlist
