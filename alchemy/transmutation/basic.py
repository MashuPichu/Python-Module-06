# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 00:35:40 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 13:39:05 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem():
    return f"Stone transmuted to gem using {create_earth()}"
