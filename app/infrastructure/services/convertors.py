from domain.arts.dto import GetArtfromAPIResponses
from domain.flowers.dto import GetFlowerfromAPIResponses


def convert_json_art_response_to_art_dto(
    response_json,
) -> GetArtfromAPIResponses:
    GetArtfromAPIResponses(
        art=response_json["art"],
        art_name=response_json["art_name"],
        art_direction=response_json["art_direction"],
        art_description=response_json["art_description"],
    )


def convert_json_flower_response_to_flower_dto(
    response_json,
) -> GetFlowerfromAPIResponses:
    GetFlowerfromAPIResponses(
        flower_name=response_json["flower_name"],
        flower_path=response_json["flower_path"],
    )
