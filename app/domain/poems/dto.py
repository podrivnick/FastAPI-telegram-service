from dataclasses import dataclass


@dataclass
class GetPoemfromAPIResponses:
    poem_title: str
    poem_author: str
    poem_text: str
    poem_date: str
