from fastapi_utils.camelcase import snake2camel
from pydantic import BaseConfig, BaseModel,ConfigDict
from pydantic.generics import GenericModel


class CamelCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda field_name: ''.join(
            word.capitalize() if i > 0 else word
            for i, word in enumerate(field_name.split('_'))
        )
    )
