from streamlit_agraph import agraph, Node, Edge, Config
nodes = []
edges = []

# try
nodes.append( Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=25, 
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

# import pandas as pd
# data = pd.read_excel('old_name.xlsx',sheet_name='data')
# count = len(data)
# for i in range(count):
#     place = str(data.iloc[i]["地点"])
#     lon = str(data.iloc[i]["lon"])
#     lat = str(data.iloc[i]["lat"])
    
#     fname1id = str(data.iloc[i]["曾用名id"])
#     fname1 = str(data.iloc[i]["曾用名1"])
#     stime1 = str(data.iloc[i]["开始时间1"])
#     etime1 = str(data.iloc[i]["结束时间1"])
    
#     fname2id = str(data.iloc[i]["曾用名2id"])
#     fname2 = str(data.iloc[i]["曾用名2"])
#     stime2 = str(data.iloc[i]["开始时间2"])
#     etime2 = str(data.iloc[i]["结束时间2"])
        
#     fname3id = str(data.iloc[i]["曾用名3id"])
#     fname3 = str(data.iloc[i]["曾用名3"])
#     stime3 = str(data.iloc[i]["开始时间3"])
#     etime3 = str(data.iloc[i]["结束时间3"])
    
#     # 地点实体
#     nodes.append(Node(id="{}".format(place), 
#                         label=place, 
#                         size=25, 
#                         shape="circularImage",
#                         image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png",
#                         color ="#689f38" )
#                   )
#     nodes.append(Node(id="{}".format(lon), 
#                         label=lon, 
#                         size=25, 
#                         shape="circularImage",
#                         image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png")
#                   )
#     edges.append(Edge(source="{}".format(place), 
#                         label="经度是", 
#                         target="{}".format(lon))) 
#     nodes.append(Node(id="{}".format(lat), 
#                         label=lat, 
#                         size=25, 
#                         shape="circularImage",
#                         image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png")
#                   )
#     edges.append( Edge(source = "{}".format(place), 
#                         label = "维度是", 
#                         target = "{}".format(lat)
#                         ) 
#                 ) 
#     # 事件实体
#     nodes.append(Node(id="{}".format(fname1id),
#                         label=fname1, 
#                         size=25, 
#                         shape="circularImage",
#                         color ="#ffa000",
#                         image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#     if stime1 != 'nan':
#         nodes.append(Node(id="{}".format(stime1), 
#                             label=stime1, 
#                             size=25, 
#                             shape="circularImage",
#                             image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#         edges.append( Edge(source = "{}".format(fname1id), 
#                             label = "开始时间", 
#                             target = "{}".format(stime1)))
#     if etime1 != 'nan':
#         nodes.append(Node(id="{}".format(etime1), 
#                             label=etime1, 
#                             size=25, 
#                             shape="circularImage",
#                             image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#         edges.append( Edge(source = "{}".format(fname1id), 
#                             label = "结束时间", 
#                             target = "{}".format(etime1)))
#     # 连接事件与地点实体
#     edges.append( Edge(source = "{}".format(place), 
#                         label = "曾用名", 
#                         target = "{}".format(fname1id)))
#     if str(data.iloc[i]["曾用名2"]) != 'nan':
#         # 事件实体
#         nodes.append(Node(id="{}".format(fname2id), 
#                             label=fname2, 
#                             size=25, 
#                             shape="circularImage",
#                             color ="#ffa000",
#                             image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#         if stime2 != 'nan':
#             nodes.append(Node(id="{}".format(stime2), 
#                                 label=stime2, 
#                                 size=25, 
#                                 shape="circularImage",
#                                 image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#             edges.append( Edge(source = "{}".format(fname2id), 
#                                 label = "开始时间", 
#                                 target = "{}".format(stime2)))
#         if etime2 != 'nan':
#             nodes.append(Node(id="{}".format(etime2), 
#                                 label=etime2, 
#                                 size=25, 
#                                 shape="circularImage",
#                                 image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#             edges.append( Edge(source = "{}".format(fname2id), 
#                                 label = "结束时间", 
#                                 target = etime2))
#         # 连接事件与地点实体
#         edges.append( Edge(source = "{}".format(place), 
#                             label = "曾用名", 
#                             target = "{}".format(fname2id)))
#         if str(data.iloc[i]["曾用名3"]) != 'nan':
#             # 事件实体
#             nodes.append(Node(id="{}".format(fname3id), 
#                                 label=fname3, 
#                                 size=25, 
#                                 shape="circularImage",
#                                 color ="#ffa000",
#                                 image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#             if stime3 != 'nan':
#                 nodes.append(Node(id="{}".format(stime3), 
#                                     label=stime3, 
#                                     size=25, 
#                                     shape="circularImage",
#                                     image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#                 edges.append( Edge(source = "{}".format(fname3id), 
#                                     label = "开始时间", 
#                                     target = "{}".format(stime3)))
#             if etime3 != 'nan':
#                 nodes.append(Node(id="{}".format(etime3), 
#                                     label=etime3, 
#                                     size=25, 
#                                     shape="circularImage",
#                                     image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
#                 edges.append( Edge(source = "{}".format(fname3id), 
#                                     label = "结束时间", 
#                                     target = "{}".format(etime3)))
#             # 连接事件与地点实体
#             edges.append( Edge(source = "{}".format(place), 
#                                 label = "曾用名", 
#                                 target = "{}".format(fname3id)))

# config = Config(width=750,
#                 height=950,
#                 directed=True, 
#                 physics=True, 
#                 hierarchical=False,
#                 )

# return_value = agraph(nodes=nodes, 
#                       edges=edges, 
#                       config=config)

# rdf文件解析
# Currently not workin since update to agraph 2.0 - work in progress
# from rdflib import Graph
# from streamlit_agraph import TripleStore, agraph

# graph = Graph()
# graph.parse("old_name.rdf")
# store = TripleStore()

# for subj, pred, obj in graph:
#     store.add_triple(subj, pred, obj, "")

# config = Config(width=750,
#                 height=950,
#                 directed=True, 
#                 physics=True, 
#                 hierarchical=False,
#                 )
    
# agraph(list(store.getNodes()), list(store.getEdges()), config)