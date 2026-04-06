# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 18:59:02 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:24:27 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def healing_potion() -> str:
    from alchemy.elements import create_earth as earth, create_air as air
    return f"Healing potion brewed with {earth()} and {air()}"


def strength_potion() -> str:
    from elements import create_fire, create_water
    water = create_water()
    fire = create_fire()
    return f"Strength potion brewed with {water} and {fire}"
