from dataclasses import dataclass


@dataclass
class GetArtfromAPIResponses:
    art: str
    art_name: str
    art_direction: str
    art_description: str
