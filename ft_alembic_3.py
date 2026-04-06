# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:21:34 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:27:23 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import elements


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...'structure")
    print(f"Testing create_air: {elements.create_air()}")


if __name__ == "__main__":
    main()
