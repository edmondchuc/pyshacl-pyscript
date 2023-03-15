from typing import TYPE_CHECKING
from datetime import datetime

from rdflib import Graph
from pyshacl import validate

if TYPE_CHECKING:
    from pyscript import Element, display

import vocpub


def get_html_input_data(html_id: str) -> str:
    return Element(html_id).element.value


def set_html_input_data(html_id: str, value: str) -> str:
    Element(html_id).element.value = value


def validate_button_callback():
    display(
        datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), target="terminal", append=False
    )

    shapes = get_html_input_data("input-shapes")
    data = get_html_input_data("input-data")

    conforms, results_graph, results_text = validate(
        data_graph=Graph().parse(data=data, format="turtle"),
        shacl_graph=Graph().parse(data=shapes, format="turtle"),
    )

    display(results_text, target="terminal", append=True)


def load_vocpub_shapes():
    set_html_input_data("input-shapes", vocpub.shapes)


def load_vocpub_valid_data():
    set_html_input_data("input-data", vocpub.valid)


def load_vocpub_invalid_data():
    set_html_input_data("input-data", vocpub.invalid)
