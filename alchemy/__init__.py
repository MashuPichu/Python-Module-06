# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 16:03:45 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 12:20:47 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air
from .potions import healing_potion as heal, strength_potion
from .transmutation import gold


__version__ = "1.0.0"
__author__ = "Master Pythonicus"

__all__ = ["create_air", "heal", "strength_potion", "gold"]
