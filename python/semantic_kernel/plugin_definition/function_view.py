# Copyright (c) Microsoft. All rights reserved.

from typing import List

from semantic_kernel.kernel_pydantic import KernelBaseModel
from semantic_kernel.plugin_definition.parameter_view import ParameterView
from semantic_kernel.utils.validation import validate_function_name


class FunctionView(KernelBaseModel):
    name: str
    plugin_name: str
    description: str
    is_semantic: bool
    parameters: List[ParameterView]
    is_asynchronous: bool = True

    def __init__(
        self,
        name: str,
        plugin_name: str,
        description: str,
        parameters: List[ParameterView],
        is_semantic: bool,
        is_asynchronous: bool = True,
    ) -> None:
        validate_function_name(name)
        super().__init__(
            name=name,
            plugin_name=plugin_name,
            description=description,
            parameters=parameters,
            is_semantic=is_semantic,
            is_asynchronous=is_asynchronous,
        )
