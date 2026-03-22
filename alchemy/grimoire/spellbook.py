# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 01:12:20 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 13:30:11 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
