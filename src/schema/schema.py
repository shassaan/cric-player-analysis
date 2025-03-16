from src.schema.player import Player


class Schema:
    def __init__(self):
        self.schema_map = {"json_source": self.map_from_schema_json}

    def map_from_schema_json(self, data):
        bio = data["bio"]
        players = []
        for match in data["match_performance"]:
            players.append(
                Player(
                    name=bio["full_name"],
                    birth_place=bio["birthplace"],
                    batting_style=bio["batting_style"],
                    bowling_style=bio["bowling_style"],
                    country=bio["country"],
                    debut=bio["debut"],
                    role=bio["role"],
                    team=bio["country"],
                    ranking=data["icc_ranking"],
                    match_runs=match["runs"],
                    match_balls_faced=match["balls_faced"],
                    match_fours=match["fours"],
                    match_sixes=match["sixes"],
                    match_dots=match["dot_balls"],
                    match_match_format=match["match_format"],
                    match_dismissal_type=match["dismissal"],
                    match_opposition=match["opposition"],
                    match_ground=match["venue"],
                )
            )

        return players

    def map_to_schema(self, data, source: str):
        if source in self.schema_map:
            return self.schema_map[source](data)
        else:
            raise Exception("Source not supported")
