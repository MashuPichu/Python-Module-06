# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_validator.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 13:04:02 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:24:58 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]

    ingredients_lower = ingredients.lower()

    for item in allowed:
        if item in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
