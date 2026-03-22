# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 00:35:52 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 14:01:28 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion as heal


def philosopher_stone():
    return f"Philosopher's stone created using {lead_to_gold()} and {heal()}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
