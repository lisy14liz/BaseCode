from collections import defaultdict, deque


def get_indegree_from_adj_list(adj_list):
    indegree = defaultdict(int)
    for src in adj_list:
        for dst in adj_list[src]:
            indegree[dst] += 1
    return indegree


def reverse_adj_list(adj_list):
    reversed_adj_list = defaultdict(list)
    for src in adj_list:
        for dst in adj_list[src]:
            reversed_adj_list[dst].append(src)
    return reversed_adj_list


def TopoSort(nodes, adj_list, indegree=None):
    if indegree is None:
        indegree = get_indegree_from_adj_list(adj_list)
    # Queue for maintainig list of nodes that have 0 in-degree
    zero_indegree_queue = deque([k for k in nodes if k not in indegree])

    topological_sorted_order = []

    # Until there are nodes in the Q
    while zero_indegree_queue:

        # Pop one node with 0 in-degree
        vertex = zero_indegree_queue.popleft()
        topological_sorted_order.append(vertex)

        # Reduce in-degree for all the neighbors
        if vertex in adj_list:
            for neighbor in adj_list[vertex]:
                indegree[neighbor] -= 1

                # Add neighbor to Q if in-degree becomes 0
                if indegree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)

    succeed = len(topological_sorted_order) == len(nodes)
    return topological_sorted_order, succeed


def TopoSortPrerequisites(nodes, prerequisites):
    """
    210. Course Schedule II: <https://leetcode.com/problems/course-schedule-ii/
    :type nodes: list
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    Input: [0,1], [[1,0]] 
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                 course 0. So the correct course order is [0,1] .
    """

    # Prepare the graph
    adj_list = defaultdict(list)
    indegree = {}
    for dest, src in prerequisites:
        adj_list[src].append(dest)

        # Record each node's in-degree
        indegree[dest] = indegree.get(dest, 0) + 1
    topological_sorted_order, succeed = TopoSort(nodes, adj_list, indegree)
    return topological_sorted_order if succeed else []
