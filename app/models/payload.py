from typing import List
from pydantic import BaseModel


class Payload(BaseModel):
    culmen_length: float
    culmen_depth: float
    flipper_length: float
    body_mass: float
    species_adelie: int
    species_chinstrap: int
    species_gentoo: int
    island_biscoe: int
    island_dream: int
    island_torgersen: int


def payload_to_list(payload: Payload) -> List:
    payload_list = [
        payload.culmen_length,
        payload.culmen_depth,
        payload.flipper_length,
        payload.body_mass,
        payload.species_adelie,
        payload.species_chinstrap,
        payload.species_gentoo,
        payload.island_biscoe,
        payload.island_dream,
        payload.island_torgersen,
    ]
    return payload_list
