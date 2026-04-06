# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 13:07:25 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:25:52 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({result})"
