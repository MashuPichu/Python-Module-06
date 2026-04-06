# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_0.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 11:11:16 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:23:21 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using 'import...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
