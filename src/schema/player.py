from pydantic import BaseModel


class Player(BaseModel):
    name: str
    age: int = None
    birth_place: str
    team: str
    debut: str
    role: str
    batting_style: str
    bowling_style: str
    country: str
    ranking: int
    match_runs: int
    match_balls_faced: int
    match_fours: int
    match_sixes: int
    match_dots: int
    match_match_format: str
    match_dismissal_type: str
    match_opposition: str
    match_ground: str