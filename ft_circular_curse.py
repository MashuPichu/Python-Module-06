# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 01:11:44 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 13:34:58 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients as validate
from alchemy.grimoire import record_spell as re


def main():

    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredients validation:")
    print("validate_ingredients('fire air'):", validate("fire air"))
    print("validate_ingredients('dragon scales'):", validate("dragon scales"))

    print("\nTesting spell recording with validation:")
    print("record_spell('Fireball', 'fire air'):", re("Fireball", "fire air"))
    print("record_spell('Dark Magic', 'shadow'):", re("Dark magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell('Lightning', 'air'):", re("Fireball", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
