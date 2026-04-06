# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:45:01 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:38 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strenght potion: {potions.strength_potion()}")
    print(f"Testing heal potion: {potions.healing_potion()}")


if __name__ == "__main__":
    main()
