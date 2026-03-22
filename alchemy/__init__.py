# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/19 16:03:45 by klucchin        #+#    #+#               #
#  Updated: 2026/03/22 13:54:12 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_fire, create_water


__version__ = "1.0.0"
__author__ = "Master Pythonicus"

__All__ = [create_fire, create_water]
