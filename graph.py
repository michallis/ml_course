import math
# represent using adjacency list (instead of matrix)
# representing a non-directed cyclic graph
graph = {
    "a": ["b"],
    "b": ["a","c","d","e"],
    "c": ["b","e"],
    "e": ["c","b","d","f"],
    "d": ["b","e","f"],
    "f": ["d","e","g"],
    "g": ["f"],
    "o": ["n"],
    "n": ["o"],
        }

def connectedGraphs(graph):
    # empty set
    visited = set()
    #for node in graph:
    #    graphTraversal(graph, node, visited)
    print(hasPath(graph, "a", "e", visited))

# Traverse the graph, keep state to avoid infinite loop
# Exploration of the graph, typically called in another function
# recursive
def graphTraversal(graph, source, visited):
    if source in visited:
        return False

    visited.add(source)
    print(source)
    for node in graph[source]:
        graphTraversal(graph, node, visited)

    return True

def hasPath(graph, source, dest, visited):
    if source == dest:
        return True
    if source in visited:
        return False
    visited.add(source)
    for node in graph[source]:
        if hasPath(graph, node, dest, visited):
            return True

    return False

connectedGraphs(graph)
