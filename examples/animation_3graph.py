from paulie.application.animation import animation_anti_commutation_graph
from paulie.common.pauli_string_factory import get_pauli_string as p 


if __name__ == "__main__":

    animation_anti_commutation_graph(p(["XYI", "IXY", "XZY"]), initGraph=True, storage={"filename":"data/example_a.html", "writer":"html"})
    animation_anti_commutation_graph(p(["XY", "XZ"], n = 4), initGraph=True, storage={"filename": "data/example_b.html", "writer": "html"})
