# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 18:59:02 by klucchin        #+#    #+#               #
#  Updated: 2026/03/19 19:19:11 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def healing_potion():
	from .elements import create_fire, create_water
	fire = create_fire
	water = create_water
	return f"Healing potion brewed with {fire} and {water}"

def strenght_potion():
	from .elements import create_fire, create_earth
	fire = create_fire
	earth = create_earth
	return f"Strenght potion brewed with {earth} and {fire}"

def invisibility_potion():
	air = alchemy.create_air
	water = alchemy.create_water
	return f"Invisibility potion brewed with {air} and {water}"

def wisdom_potion():
	fire = alchemy.create_fire
	water = alchemy.create_water
	air = alchemy.create_air
	earth = alchemy.create_earth
	return f"Healing potion brewed with {fire} {water} {earth} and {air}"