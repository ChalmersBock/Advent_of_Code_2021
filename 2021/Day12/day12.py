from collections import defaultdict


def get_unique_paths_for_node(graph, big_caves, name, visited, double_visit):
    visited.append(name)
    paths = []
    for node in graph[name]:
        current_path = []
        for visit in visited:
            current_path.append(visit)
        if node == 'end':
            current_path.append(node)
            paths.append(current_path)
        elif node not in current_path or node in big_caves:
            for path in get_unique_paths_for_node(graph,
                                                  big_caves, node, current_path, double_visit):
                paths.append(path)
        elif node != 'start' and double_visit:
            for path in get_unique_paths_for_node(graph, big_caves, node, current_path, False):
                paths.append(path)

    return paths


def find_number_of_unique_paths(allow_double_visit):
    graph_dict = defaultdict(list)
    big_caves = []
    with open("data", "r", encoding='utf-8') as file:
        for line in [x.strip() for x in file.readlines()]:
            one, two = line.split("-")
            graph_dict[one].append(two)
            graph_dict[two].append(one)
            if one.isupper():
                big_caves.append(one)
            if two.isupper():
                big_caves.append(two)

    paths = get_unique_paths_for_node(graph_dict, big_caves, "start", [], allow_double_visit)

    print(f'Number of paths with double visit set to {allow_double_visit}: {len(paths)}')


if __name__ == '__main__':
    find_number_of_unique_paths(False)
    find_number_of_unique_paths(True)
