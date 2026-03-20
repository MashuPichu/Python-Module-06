# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 00:35:07 by klucchin        #+#    #+#               #
#  Updated: 2026/03/20 01:10:57 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import elixir_of_life, philosopher_stone
import alchemy.transmutation as transmutation

def main():

    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold():", lead_to_gold())
    print(f"stone_to_gem():", stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosopher.stone():", philosopher_stone())
    print(f"elixir_of_life()", elixir_of_life())
    
    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold():", transmutation.lead_to_gold())
    print(f"alchemy.transmutation.philosopher_stone():", transmutation.philosopher_stone())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")

if __name__ == "__main__":
    main()
