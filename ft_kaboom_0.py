# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 13:05:20 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:12:27 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
