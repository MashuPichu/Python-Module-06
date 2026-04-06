# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:34:12 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:34 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
