# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 12:14:41 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:48 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {alchemy.transmutation.gold()}")


if __name__ == "__main__":
    main()
