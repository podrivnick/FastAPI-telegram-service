from domain.arts.dto import GetArtfromAPIResponses
from domain.flowers.dto import GetFlowerfromAPIResponses
from domain.poems.dto import GetPoemfromAPIResponses


def convert_json_art_response_to_art_dto(
    response_json: dict,
) -> GetArtfromAPIResponses:
    return GetArtfromAPIResponses(
        art=response_json["art"]["value"],
        art_name=response_json["art_name"]["value"],
        art_direction=response_json["art_direction"]["value"],
        art_description=response_json["art_description"]["value"],
    )


def convert_json_flower_response_to_flower_dto(
    response_json: dict,
) -> GetFlowerfromAPIResponses:
    return GetFlowerfromAPIResponses(
        flower_name=response_json["flower_name"]["value"],
        flower_path=response_json["flower_path"]["value"],
    )


def convert_json_poem_response_poem_dto(
    response_json: dict,
) -> GetPoemfromAPIResponses:
    return GetPoemfromAPIResponses(
        poem_title=response_json["poem_title"]["value"],
        poem_author=response_json["poem_author"]["value"],
        poem_text=response_json["poem_text"]["value"],
        poem_date=response_json["poem_date"]["value"],
    )
