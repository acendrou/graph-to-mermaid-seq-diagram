import networkx as nx

import matplotlib.pyplot as plt
from networkx.classes import MultiDiGraph

BASIC_ARROW = "->>"


def create_graph():
    G = MultiDiGraph()
    G.add_node(1, actor_name="Alice")
    G.add_node(2, actor_name="Bob")
    G.add_node(3, actor_name="Charlie")
    G.add_node(4, actor_name="David")
    G.add_node(5, actor_name="Eve")
    G.add_edge(1, 2, text="1 to 2", type_arrow=BASIC_ARROW)
    G.add_edge(2, 3, text="2 to 3", type_arrow=BASIC_ARROW)
    G.add_edge(3, 1, text="3 to 1", type_arrow=BASIC_ARROW)
    G.add_edge(4, 5, text="4 to 5", type_arrow=BASIC_ARROW)
    return G


def plot_graph(G: nx.Graph):
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show()


class MermaidSeqDiagram:
    content: str

    def __init__(self):
        self.content = "sequenceDiagram\n"

    def add_sequence(
        self, actor1: str, actor2: str, type_arrow: str, text: str
    ) -> None:
        content_temp = (
            self.add_tab()
            + str(actor1)
            + type_arrow
            + str(actor2)
            + self.add_colon()
            + text
            + self.add_newline()
        )
        self.content += content_temp

    @staticmethod
    def add_tab() -> str:
        return "    "

    @staticmethod
    def add_colon() -> str:
        return ":"

    @staticmethod
    def add_newline() -> str:
        return "\n"

    def __repr__(self):
        return self.content


def generate_mermaid_seq() -> str:
    c = MermaidSeqDiagram()
    c.add_sequence(
        actor1="Alice", actor2="John", type_arrow="->>", text="Hello John, how are you?"
    )
    c.add_sequence(actor1="John", actor2="Alice", type_arrow="-->>", text="Great!")
    return c


def write_file(content: str):
    with open("mermaid-seq-diagram.mmd", "w") as f:
        f.write(str(content))


def generate_mermaid_seq_diagram_from_graph(G: nx.Graph) -> str:
    c = MermaidSeqDiagram()
    for e in G.edges(data=True):
        print(e)
        c.add_sequence(
            actor1=e[0], actor2=e[1], type_arrow=e[2]["type_arrow"], text=e[2]["text"]
        )
    return str(c)


if __name__ == "__main__":
    g = create_graph()
    plot_graph(g)
    content = generate_mermaid_seq()
    print(content)
    write_file(content)
    print("real graph")
    c = generate_mermaid_seq_diagram_from_graph(g)
    print(c)
    print("Done")
