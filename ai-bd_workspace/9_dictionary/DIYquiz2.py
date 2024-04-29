# 가장 빠른 길 찾기
# A -5- B -5- D -10- G
# A -5- B -10- E -5- G
# A -10- C -10- E -5- G
# A -10- C -5- F -10- G

# nodes = {"A" : ["B", "C"], "B" : ["D", "E"], "C" : ["E", "F"], "D" : ["G"], "E" : ["G"], "F" : ["G"] };
# distance = {"A" : [5, 10], "B" : [5, 10], "C" : [10, 5], "D" : [20], "E" : [5], "F" : [10] };
# optNode = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0 };
nodes, distance, optNode = {}, {}, {};
nodeCount = int(input());
busCount = int(input());

for i in range(busCount):
    ls = input().split();
    if nodes.get(ls[0]) == None:
        nodes[ls[0]] = [];
        distance[ls[0]] = [];
        optNode[ls[0]] = 0;
    nodes[ls[0]].append(ls[1]);
    distance[ls[0]].append(int(ls[2]));

se = input().split();


resLs = {};
startRoute = "";
curRoute = "";
i = 0;
while True:
    curRoute = "";
    curNode = se[0];
    nextNode = se[0];
    routeDistance = 0;
    while nextNode != se[1]:
        curNode = nextNode;
        curRoute += curNode;
        opt = optNode.get(curNode);
        nextNode = nodes.get(curNode)[opt];
        routeDistance += distance.get(curNode)[opt];

        if opt+1 == len(nodes.get(curNode)):
            optNode[curNode] = 0;
        else:
            optNode[curNode] += 1;
    if i == 0:
        startRoute = curRoute;
    elif startRoute == curRoute:
        break;
    resLs[curRoute] = routeDistance;
    i += 1;
print(min(list(resLs.values())));


