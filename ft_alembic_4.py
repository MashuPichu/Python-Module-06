# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:28:00 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:58:53 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"create_earth not found: {e}")


if __name__ == "__main__":
    main()
