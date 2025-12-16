from functools import cache

def parse_graph(content: str) -> dict[str, list[str]]:
    graph = {}

    for line in content.splitlines():
        server, connections = line.split(":")
        graph[server] = connections.strip().split(" ")

    return graph


def enumerate_paths(graph: dict[str, list[str]], source: str, sink: str) -> int:
    if source == sink:
        return 1

    total_paths = 0
    for connection in graph[source]:
        total_paths += enumerate_paths(graph, connection, sink)

    return total_paths


def part_1(content: str) -> str:
    graph = parse_graph(content)

    source = "you"
    sink = "out"

    paths = enumerate_paths(graph, source, sink)

    return str(paths)


def part_2(content: str) -> str:

    graph = parse_graph(content)

    @cache
    def enumerate_paths_with(source: str, sink: str, dac: bool = False, fft: bool = False) -> int:
        if source == sink:
            if dac and fft:
                return 1
            else:
                return 0
            
        if source == "dac":
            dac = True
        
        if source == "fft":
            fft = True

        total_paths = 0
        for connection in graph[source]:
            total_paths += enumerate_paths_with(connection, sink, dac=dac, fft=fft)

        return total_paths
    
    source = "svr"
    sink = "out"

    paths = enumerate_paths_with(source, sink)
    
    return str(paths)
    