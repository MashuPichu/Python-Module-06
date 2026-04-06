# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 12:03:05 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:24:43 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..elements import create_air as air
from alchemy.potions import strength_potion as strenght
from elements import create_fire as fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{air()}' "
            f"and '{strenght()}' mixed with '{fire()}'")
