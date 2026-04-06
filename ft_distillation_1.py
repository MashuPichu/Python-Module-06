# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:59:09 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:43 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strenght potion: {alchemy.strength_potion()}")
    print(f"Testing heal potion: {alchemy.heal()}")


if __name__ == "__main__":
    main()
