import networkx as nx

import matplotlib.pyplot as plt

BASIC_ARROW = "-->"


class MermaidStateDiagram:
    def __init__(self):
        pass

    @staticmethod
    def load_file(path: str) -> nx.MultiDiGraph:
        with open(path) as f:
            lines = f.readlines()
        g = nx.MultiDiGraph()

        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if line == "---":
                continue
            if line.startswith("title:"):
                continue
            if line.startswith("stateDiagram-v2"):
                continue
            line = line.replace(" ", "")
            line = line.split(BASIC_ARROW)
            g.add_node(line[0])
            g.add_edge(line[0], line[1])

        return g


def plot_graph(g: nx.Graph):
    subax1 = plt.subplot(121)
    nx.draw(g, with_labels=True, font_weight="bold")
    plt.show()


def generate_graph(path: str):
    g = MermaidStateDiagram().load_file(path=path)
    plot_graph(g=g)


def main(path: str):
    generate_graph(path=path)


if __name__ == "__main__":
    main(path="mermaid-state-diagram.mmd")
