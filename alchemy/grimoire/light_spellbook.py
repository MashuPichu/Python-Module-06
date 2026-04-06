# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 12:31:53 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:26:03 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({result})"
