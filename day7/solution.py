import re
import networkx as nx


def read(path):
    with open(path, "r") as f:
        data = f.readlines()
    return data


def create_graph(data):
    graph = nx.DiGraph()
    for line in data:
        line = line.replace(",", "").replace(".", "").replace("bags", "").replace("bag", "")
        reg = re.match(r"(.*) contain (.*)", line)
        if reg:
            parent = reg.group(1)
            child_group = reg.group(2)
            childs = re.findall(r"(\d|no) ([^\d]*)", child_group)
            for child in childs:
                if child[0] in "no":
                    n = 0
                else:
                    n = int(child[0])
                graph.add_edge(parent.replace(" ", ""), child[1].replace(" ", ""), weight=n)
    return graph


def countBags(bag, graph):
    bags = 0
    for color, n in graph[bag].items():
        bags += n["weight"] + n["weight"] * countBags(color, graph)
    return bags


def main():
    graph = create_graph(read("input.txt"))
    print("Part 1 solution: ", len(nx.ancestors(graph, "shinygold")))
    print("Part 2 solution: ", countBags("shinygold", graph))


if __name__ == "__main__":
    main()
