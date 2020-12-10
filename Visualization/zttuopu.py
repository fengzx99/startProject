import json
import numpy as np
import pandas as pd


def readJSONFile(path):
    f = open(path, "r")
    return json.load(f)


def Ztopo(path):
    file = ['data_release/train/0.csv',
            'data_release/train/1.csv',
            'data_release/train/10.csv',
            'data_release/train/11.csv',
            'data_release/train/12.csv',
            'data_release/train/13.csv',
            'data_release/train/14.csv',
            'data_release/train/15.csv',
            'data_release/train/16.csv',
            'data_release/train/17.csv',
            'data_release/train/18.csv',
            'data_release/train/19.csv',
            'data_release/train/2.csv',
            'data_release/train/20.csv',
            'data_release/train/21.csv',
            'data_release/train/22.csv',
            'data_release/train/23.csv',
            'data_release/train/24.csv',
            'data_release/train/25.csv',
            'data_release/train/26.csv',
            'data_release/train/27.csv',
            'data_release/train/28.csv',
            'data_release/train/29.csv',
            'data_release/train/3.csv',
            'data_release/train/30.csv',
            'data_release/train/31.csv',
            'data_release/train/32.csv',
            'data_release/train/33.csv',
            'data_release/train/34.csv',
            'data_release/train/35.csv',
            'data_release/train/36.csv',
            'data_release/train/37.csv',
            'data_release/train/38.csv',
            'data_release/train/39.csv',
            'data_release/train/4.csv',
            'data_release/train/40.csv',
            'data_release/train/41.csv',
            'data_release/train/42.csv',
            'data_release/train/43.csv',
            'data_release/train/44.csv',
            'data_release/train/45.csv',
            'data_release/train/46.csv',
            'data_release/train/47.csv',
            'data_release/train/48.csv',
            'data_release/train/49.csv',
            'data_release/train/5.csv',
            'data_release/train/50.csv',
            'data_release/train/51.csv',
            'data_release/train/52.csv',
            'data_release/train/53.csv',
            'data_release/train/54.csv',
            'data_release/train/55.csv',
            'data_release/train/56.csv',
            'data_release/train/57.csv',
            'data_release/train/58.csv',
            'data_release/train/59.csv',
            'data_release/train/6.csv',
            'data_release/train/60.csv',
            'data_release/train/61.csv',
            'data_release/train/62.csv',
            'data_release/train/63.csv',
            'data_release/train/64.csv',
            'data_release/train/65.csv',
            'data_release/train/66.csv',
            'data_release/train/67.csv',
            'data_release/train/68.csv',
            'data_release/train/69.csv',
            'data_release/train/7.csv',
            'data_release/train/70.csv',
            'data_release/train/71.csv',
            'data_release/train/72.csv',
            'data_release/train/73.csv',
            'data_release/train/74.csv',
            'data_release/train/75.csv',
            'data_release/train/76.csv',
            'data_release/train/77.csv',
            'data_release/train/78.csv',
            'data_release/train/79.csv',
            'data_release/train/8.csv',
            'data_release/train/80.csv',
            'data_release/train/81.csv',
            'data_release/train/82.csv',
            'data_release/train/83.csv',
            'data_release/train/84.csv',
            'data_release/train/85.csv',
            'data_release/train/86.csv',
            'data_release/train/87.csv',
            'data_release/train/88.csv',
            'data_release/train/89.csv',
            'data_release/train/9.csv',
            'data_release/train/90.csv',
            'data_release/train/91.csv',
            'data_release/train/92.csv',
            'data_release/train/93.csv',
            'data_release/train/94.csv',
            'data_release/train/95.csv',
            'data_release/train/96.csv',
            'data_release/train/97.csv',
            'data_release/train/98.csv',
            'data_release/train/99.csv']
    nodes_json = readJSONFile("data_release/topology/topology_edges_node2.json")  # 这里换文件了
    train_dic = readJSONFile("./data_release/train_dic.json")
    path = "data_release/train/"+path+".csv"
    train77=pd.read_csv(path,encoding='utf-8')

    z=train77['triggername'].to_frame()
    zz=z.triggername.str.split('\s+').str[0]
    node=zz.to_frame()['triggername'].str[7:]
    nodelist=node.tolist()
    setnodelist=set(nodelist)
    path1=path[19:]
    
    rootrow=train77.loc[train77['is_root'] == 1]
    rootrowcolumn=rootrow['triggername'].to_frame()
    rootrowcolumnnum=rootrowcolumn.triggername.str.split('\s+').str[0]
    rootnode=rootrowcolumnnum.to_frame()['triggername'].str[7:]
    rootnodelist=rootnode.tolist()
    setrootnodelist=set(rootnodelist)
    list_setrootnodelist=list(setrootnodelist)
    if len(list_setrootnodelist)==0:
        alldata=[]
        for name in setnodelist:
            if name in ["50", "0", "58", "4", "83", "33", "17", "31", "15", "73", "93"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":1,'draggable':'true'}
                alldata.append(evdata)
            if name in ["70", "30", "45", "37", "55", "21", "18", "7", "99", "8", "91"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":2,'draggable':'true'}
                alldata.append(evdata)
            if name in ["57", "20", "28", "3", "97", "39", "86", "94"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":3,'draggable':'true'}
                alldata.append(evdata)
            if name in ["72", "34", "81", "36", "62", "77", "69", "13", "9", "19", "27", "5"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":4,'draggable':'true'}
                alldata.append(evdata)
            if name in ["14", "26", "65", "2", "76", "38", "82", "60", "6", "74", "85"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":5,'draggable':'true'}
                alldata.append(evdata)
            if name in ["56", "67", "25", "48", "59", "32", "35", "46", "1", "98"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":6,'draggable':'true'}
                alldata.append(evdata)
            if name in ["63", "53", "61", "89", "54", "24", "23", "51"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":7,'draggable':'true'}
                alldata.append(evdata)
            if name in ["84", "10", "49", "95", "88", "43", "41", "71", "79", "87"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":8,'draggable':'true'}
                alldata.append(evdata)
            if name in ["68", "16", "92", "78", "47", "75", "22", "80", "66", "12", "44"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":9,'draggable':'true'}
                alldata.append(evdata)
            if name in ["29", "64", "96", "42", "90", "11", "52", "40"]:
                evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":10,'draggable':'true'}
                alldata.append(evdata)
        root='wugenyin'
        root_gj='wugenyin'    
    else:
        alldata=[]
        for name in setnodelist:
            if name in ["50", "0", "58", "4", "83", "33", "17", "31", "15", "73", "93"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":1,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":1,'draggable':'true'}
                alldata.append(evdata)
            if name in ["70", "30", "45", "37", "55", "21", "18", "7", "99", "8", "91"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":2,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":2,'draggable':'true'}
                alldata.append(evdata)
            if name in ["57", "20", "28", "3", "97", "39", "86", "94"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":3,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":3,'draggable':'true'}
                alldata.append(evdata)
            if name in ["72", "34", "81", "36", "62", "77", "69", "13", "9", "19", "27", "5"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":4,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":4,'draggable':'true'}
                alldata.append(evdata)
            if name in ["14", "26", "65", "2", "76", "38", "82", "60", "6", "74", "85"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":5,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":5,'draggable':'true'}
                alldata.append(evdata)
            if name in ["56", "67", "25", "48", "59", "32", "35", "46", "1", "98"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":6,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":6,'draggable':'true'}
                alldata.append(evdata)
            if name in ["63", "53", "61", "89", "54", "24", "23", "51"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":7,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":7,'draggable':'true'}
                alldata.append(evdata)
            if name in ["84", "10", "49", "95", "88", "43", "41", "71", "79", "87"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":8,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":8,'draggable':'true'}
                alldata.append(evdata)
            if name in ["68", "16", "92", "78", "47", "75", "22", "80", "66", "12", "44"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":9,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":9,'draggable':'true'}
                alldata.append(evdata)
            if name in ["29", "64", "96", "42", "90", "11", "52", "40"]:
                if name==list_setrootnodelist[0]:
                    evdata={'name':name,"symbolSize": 70,"category":10,'symbol':'arrow','symbolSize':40,'draggable':'true'}
                else:
                    evdata={'name':name,"symbolSize": 40,'symbol':'circle',"category":10,'draggable':'true'}
                alldata.append(evdata)
        root=list_setrootnodelist[0]#对应root
        dingwei=train77.loc[train77['is_root']==1]['triggername'].to_frame()                
        root_gj=dingwei['triggername'].values[0]#对应root_gj

    alllink=[]
    for key in nodes_json:
        for i in nodes_json[key]:
            k=str(key)
            v=str(i)
            if k in setnodelist:
                if v in setnodelist:
                    evlink={'target': v,'source': k}
                    alllink.append(evlink)

                    
    for i in range(len(train_dic)):
        d=train_dic[i]
        for dict_key in d.keys():
            str_dict_key=str(dict_key)
            if(str_dict_key==path1):
                gjxx=d[path1]
#                 print(gjxx)
    returnlist={}
    returnlist['root']=root
    returnlist['root_gj']=root_gj
    returnlist['alldata']=alldata
    returnlist['alllink']=alllink
    returnlist['gjxx']=gjxx
    #print("len:", len(alldata))
    return returnlist

    

