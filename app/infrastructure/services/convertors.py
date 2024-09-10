from app.domain.arts.dto import GetArtfromAPIResponses


def convert_json_response_to_art_dto(
    response_json,
) -> GetArtfromAPIResponses:
    GetArtfromAPIResponses(
        art=response_json["art"],
        art_name=response_json["art_name"],
        art_direction=response_json["art_direction"],
        art_description=response_json["art_description"],
    )
