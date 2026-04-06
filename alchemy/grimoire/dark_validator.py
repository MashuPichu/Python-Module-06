# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_validator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 13:07:43 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:25:21 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    ingredients_lower = ingredients.lower()

    for item in allowed:
        if item in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
