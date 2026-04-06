# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/06 13:08:32 by klucchin        #+#    #+#               #
#  Updated: 2026/04/06 13:22:33 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        result = dark_spell_record(
            "Mot de l'ombre: douleur", "bats, eye and frogs")
        print(f"Testing record light spell: {result}")
    except ImportError as e:
        print(f"BOOM Circular Curse: {e}")


if __name__ == "__main__":
    main()
