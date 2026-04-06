# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:17:11 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:27 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
