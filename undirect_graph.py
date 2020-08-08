from collections import defaultdict, deque


def edges2adjList(edges): #代码没测试
	adj_list = defaultdict(list)
	for e in edges:
	adj_list[e[0]] = e[1]
	adj_list[e[1]] = e[0]
	return adj_list


def undirectGraph2treeArray(adj_list, root):#代码没测试
	added = set([])
	stack = [root]
	childsArray = defaultdict(list)
	while stack:
	node = stack.pop()
	for adj_node in adj_list[node]:
	if adj_node not in added:
	childsArray[node].append(adj_node)
	added.add(adj_node)
	return childsArray

def findLongestPath(childsArray,root):#代码没测试
    two_longest_path_next_childs={}
    two_longest_path_lengths={}
    def findLongestPathStartFromRoot(childsArray,root):
        for child in childsArray[root]:
            sub_child,sub_length=findLongestPathStartFromRoot(child)
            # replace
            if sub_length>two_longest_path_length[0]:
                two_longest_path_next_childs[0]=child
            elif sub_length>two_longest_path_length[1]:
                two_longest_path_next_childs[1]=child
        return two_longest_path_next_childs[0],two_longest_path_length[0],



