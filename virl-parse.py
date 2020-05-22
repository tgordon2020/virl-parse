from lxml import etree as ET
import glob
import re
import os

file_pattern = input("pattern to search: ")
file_list = glob.glob(f'*{file_pattern}*.virl')

for file_name in file_list:
    with open(file_name) as file:
        virl_xml = file.read()
    directory = file_name.replace(".", "_")
    try:
        os.mkdir(directory)
    except:
        pass

    root = ET.fromstring(bytes(virl_xml, encoding='utf-8'))

    nodenumber = 0
    node = []
    nodetype = {}
    interface = {}
    connections = []

    for x in root:
        if "node" in x.tag:
            node.append(x.get('name'))
            nodenumber += 1
            interface[x.get('name')] = [y.get('name') for y in x if 'extensions' not in y.tag]
            nodetype[x.get('name')]=x.get('subtype')
            try:
                device_config = (x[0][0].text)
                with open(f"{directory}\/{x.get('name')}.txt", "w") as config:
                    config.write(device_config)
            except Exception as e:
                print(e)

        elif "connection" in x.tag:
            dst= x.get('dst')
            src =x.get('src')
            dstint = re.findall("[0-9]{1,2}", dst)
            srcint = re.findall("[0-9]{1,2}", src)
            condst = (int(dstint[0])-1),(int(dstint[1])-1)
            consrc = (int(srcint[0])-1),(int(srcint[1])-1)
            dstnode=node[condst[0]]
            dstinter=interface[dstnode][condst[1]]
            srcnode=node[consrc[0]]
            srcinter=interface[srcnode][consrc[1]]
            connections.append(f"{dstnode} {dstinter} -- {srcnode} {srcinter}")

        else:
            pass

    with open(f"{directory}\/devices.txt",'w') as device_info:
        for k,v in interface.items():
            device_info.write(f'{k} : {nodetype[k]}\n')
            for a in v:
                device_info.write(f'    {a}\n')

    with open(f"{directory}\/connections.txt",'w') as device_link:
        for con in connections:
            device_link.write(f'{con}\n')
