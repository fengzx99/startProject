import pandas as pd


def read_pre_file(files):
    df = pd.read_csv("./data_release/pre_train/"+files+'.csv')
    del df['Unnamed: 0']
    #del df['sysEname']
    del df['is_root']
    df['sysEname'] = df['sysEname'].apply(lambda x: x[2:])
    return df

#采样函数
def Resample(df, T):
    df['time'] = pd.to_datetime(df['time'], format="%Y-%m-%d %X")
    def resample(x, start):
        if (x - start).total_seconds()<=T:
            x = start
        if (x - start).total_seconds()>T:
            start = x
        return x,start
    Times = df['time'].to_list()
    start = Times[0]
    for i in range(1,len(Times)):
        start_ = start
        Times[i], start = resample(Times[i], start)
    df['time'] = Times
    df['count'] = 1
    df = df.groupby(['sysEname', 'time', 'trigger', 'node']).sum().reset_index()
    return df


# 旭日图数据处理
def getSundata(files):
    SunData = []
    df = read_pre_file(files)
    sun_data_df = Resample(df, 30)

    times = list(set(sun_data_df['time']))
    for time in times:
        childs = []
        for sys, da in sun_data_df[sun_data_df['time'] == time].groupby(['sysEname']):
            # print(set(sun_data_df[sun_data_df['time']==time].sysEname))
            # print(sys,da.shape[0])
            childrens = {}
            dic = []
            for n, d in da.groupby(['node']):
                children = {}
                triggers = d['trigger'].to_list()
                # print(triggers)
                di = []
                children.update({
                    'name': n,

                    'itemStyle': {
                        'color': "#3393E2"
                    }
                })
                for name in triggers:
                    di_ = {
                        'name': name,
                        'value': 1,
                        'itemStyle': {
                            'color': "#0078DB"
                        }
                    }
                    di.append(di_)
                    # print(di)
                children.update({
                    'children': di
                })
                dic.append(children)
            childrens.update({
                'name': sys,
                'itemStyle': {
                    'color': "#1B86DF"
                },

                'children': dic
            })
            # print(children)
            childs.append(childrens)
        # print(children)
        # print(childs)
        SunData.append({

            'time': str(time),
            'data': childs
        })
    return SunData

# 时间条形图
# 饼状节点次数图
def get_node_count(files):
    ''' 第一个返回bar图数据，第二个返回值饼图node数据'''
    MapData = []
    node_pie_d = []
    df = read_pre_file(files)
    map_df = Resample(df, 30)
    Times = list(set(map_df['time']))
    #print(len(Times))
    for time in Times:
        Map_ = []
        for n, d in map_df[map_df['time'] == time].groupby(['node']):
            # (n,d)
            # print(str(time),n,d.shape[0])
            Map_.append({
                'name': n,
                'value': d['count'].sum()
            })
        MapData.append({
            'time': str(time),
            'data': Map_
        })
        node_pie_d.append({
            'time': str(time),
            'data': Map_
        })
    return MapData, node_pie_d


def get_trigger_data(files):
    # 饼图
    trigger_pie_df = read_pre_file(files)
    TriggerData = []
    trigger_pie_df = Resample(trigger_pie_df, 30)
    del trigger_pie_df['sysEname']
    Times = list(set(trigger_pie_df['time']))
    #print(len(Times))
    for time in Times:
        Map_ = []
        for n, d in trigger_pie_df[trigger_pie_df['time'] == time].groupby(['trigger']):
            # (n,d)
            # print(str(time),n,d.shape[0])
            Map_.append({
                'name': n,
                'value': d['count'].sum()
            })
        TriggerData.append({
            'time': str(time),
            'data': Map_
        })
    return TriggerData


def move_Line(files):
    # 折线图
    Line_df = read_pre_file(files)
    Line_df = Resample(Line_df, 10)
    del Line_df['sysEname']
    Line_df.head(5)
    Times_ = list(set(Line_df['time']))
    line_data = []
    Times_.sort()
    for time in Times_:
        node_count = len(set(Line_df[Line_df['time'] == time].node))
        trigger_count = len(set(Line_df[Line_df['time'] == time].trigger))
        line_data.append({
            'time': str(time),
            'value': [
                node_count,
                trigger_count
            ]
        })
    return line_data



