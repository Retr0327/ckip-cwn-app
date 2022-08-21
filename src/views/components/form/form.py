from typing import Union
from .form_components import add_text_area


def form_controller(control: str, **kwargs) -> Union[str, int]:
    """The form_controller function builds a form component based on `control`."""
    form_factories = {"text-area": add_text_area}

    return form_factories[control](**kwargs)
