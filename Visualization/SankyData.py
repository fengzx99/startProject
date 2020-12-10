import pandas as pd
import json

def GetInNode(node):
    with open("./data_release/topology/topology_edges_node.json",'r', encoding='UTF-8') as f:
        Topo = json.load(f) 
        in_node = []
        for key,values in Topo.items():
            if node in values:
                in_node.append(key)
        return in_node
    
def GetOutNode(node):
    with open("./data_release/topology/topology_edges_node.json",'r', encoding='UTF-8') as f:
        Topo = json.load(f) 
        out_node = Topo[node]
        return out_node


def SankitData(path, TYPE='train'):

    if TYPE=='test':
        data = pd.read_csv("./data_release/pre_test/" + path + '.csv')
    else:
        data = pd.read_csv("./data_release/pre_train/" + path + '.csv')
    grouped = data.groupby(['node', 'trigger']).size().reset_index(name='counts')
    grouped['node'] = [node.strip() for node in grouped['node'].to_list()]
    all_nodes = list(set(grouped['node'].to_list()))
    # print(grouped[grouped['node']=='node_4'])
    #print(len(all_nodes)==len(set(data['node'])))
    # 桑吉图词典
    Sankit = {}

    for node in all_nodes:
        # data link list
        data_0 = []
        link_0 = []
        data_1 = []
        link_1 = []
        data_2 = []
        link_2 = []

        # 获取零层节点 node
        node_all_0 = node
        # print(node_all_0)

        # 获取第一层节点
        node_in_1 = list(set(all_nodes).intersection(set(GetInNode(node))))
        node_out_1 = list(set(all_nodes).intersection(set(GetOutNode(node))))
        node_all_1 = list(set(node_in_1 + node_out_1))
        # print(node_all_1)

        # 获取二层节点
        node_in_2 = []
        node_out_2 = []
        for node_2 in node_in_1:
            node_in_2 = node_in_2 + list(set(all_nodes).intersection(set(GetInNode(node_2))))
            node_out_2 = node_out_2 + list(set(all_nodes).intersection(set(GetOutNode(node_2))))
        node_all_2= list(set(node_in_2 + node_out_2))
        if node in node_all_2:
            node_all_2.remove(node)

        # 存放0层数据
        dic_data = {'name': node}
        data_0.append(dic_data)
        for trigger in grouped[grouped['node'] == node]['trigger']:
            # print(trigger)
            v1 = grouped[grouped['node'] == node]
            v2 = v1[v1['trigger'] == trigger]['counts'].to_list()[0]
            dic_data = {'name': trigger}
            dic_link = {'source': node, 'target': trigger, 'value': v2}
            data_0.append(dic_data)
            link_0.append(dic_link)

        #存放1层数据
        trigger_have=[]
        for node_1 in node_all_1:
            dic_data={'name':node_1}
            data_1.append(dic_data)
            for trigger in grouped[grouped['node']==node_1]['trigger']:
                v1 = grouped[grouped['node']==node_1]
                v2 = v1[v1['trigger']==trigger]['counts'].to_list()[0]
                if trigger not in trigger_have:
                    dic_data = {'name':trigger}
                    data_1.append(dic_data)
                    trigger_have.append(trigger)
                dic_link = {'source':node_1,'target':trigger,'value':v2}
                link_1.append(dic_link)
        #print(data_1)
        #print(link_1)
        
        #存放2层数据
        trigger_have=[]
        for node_2 in node_all_2:
            dic_data={'name':node_2}
            data_2.append(dic_data)
            for trigger in grouped[grouped['node']==node_2]['trigger']:
                v1 = grouped[grouped['node']==node_2]
                v2 = v1[v1['trigger']==trigger]['counts'].to_list()[0]
                if trigger not in trigger_have:
                    dic_data = {'name':trigger}
                    data_2.append(dic_data)
                    trigger_have.append(trigger)
                dic_link = {'source':node_2,'target':trigger,'value':v2}
                link_2.append(dic_link)
        #print(data_1)
        #print(link_1)

        dl_0 = {'data': data_0, 'link': link_0}
        dl_1 = {'data': data_1, 'link': link_1}
        dl_2 = {'data': data_2, 'link': link_2}
        dl_all = [dl_0, dl_1, dl_2]

        Sankit[node] = dl_all
    #print(Sankit['node_84'])
    #print("San:", len(all_nodes))
    return Sankit

