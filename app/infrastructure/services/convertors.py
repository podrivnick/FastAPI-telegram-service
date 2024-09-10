from domain.arts.dto import GetArtfromAPIResponses
from domain.flowers.dto import GetFlowerfromAPIResponses


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
    response_json,
) -> GetFlowerfromAPIResponses:
    return GetFlowerfromAPIResponses(
        flower_name=response_json["flower_name"],
        flower_path=response_json["flower_path"],
    )
