import json
import pandas as pd


def readJSONFile(path):
    f = open(path, "r")
    return json.load(f)


def TZtopo(path):
    nodes_json = readJSONFile("data_release/topology/topology_edges_node2.json")  # 这里换文件了
    train_dic = readJSONFile("./data_release/test_dic.json")
    path = 'data_release/test1/'+path+'.csv'
    train77=pd.read_csv(path,encoding='utf-8')
    z=train77['triggername'].to_frame()
    zz=z.triggername.str.split('\s+').str[0]
    node=zz.to_frame()['triggername'].str[7:]
    nodelist=node.tolist()
    setnodelist=set(nodelist)
    path1=path[19:]
    
    rootrow=train77.loc[train77['is_root']==1]
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
    return returnlist

    
