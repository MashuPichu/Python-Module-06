# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 18:59:02 by klucchin        #+#    #+#               #
#  Updated: 2026/03/20 00:34:03 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def healing_potion():
    from .elements import create_fire as fire, create_water as water
    return f"Healing potion brewed with {fire()} and {water()}"


def strength_potion():
    from .elements import create_earth, create_fire
    earth = create_earth()
    fire = create_fire()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion():
    from .elements import create_air as air, create_water as water
    return f"Invisibility potion brewed with {air()} and {water()}"


def wisdom_potion():
    from .elements import create_fire, create_water, create_air, create_earth
    fire = create_fire()
    water = create_water()
    air = create_air()
    earth = create_earth()
    return f"Wisdom potion brewed with all elements: {fire}, {water}, {earth}, {air}"