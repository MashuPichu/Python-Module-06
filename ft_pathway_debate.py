# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 00:35:07 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 14:01:05 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import elixir_of_life, philosopher_stone
import alchemy.transmutation as transmutation


def main():

    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosopher.stone():", philosopher_stone())
    print("elixir_of_life()", elixir_of_life())

    print("\nTesting Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold():", transmutation.lead_to_gold()
    )
    path_way = "alchemy.transmutation.philosopher_stone():"
    print(path_way, transmutation.philosopher_stone())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
