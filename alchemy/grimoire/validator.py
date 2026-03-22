# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 01:12:29 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 12:47:11 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def validate_ingredients(ingredients: str) -> str:
    elements = ["fire", "air", "earth", "water"]
    words = ingredients.split()
    for word in words:
        if word not in elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
