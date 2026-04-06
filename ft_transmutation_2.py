# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_2.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 12:18:20 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:27:41 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.transmutation.gold()}")


if __name__ == "__main__":
    main()
