# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: moerrais <moerrais@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 08:25:37 by moerrais          #+#    #+#              #
#    Updated: 2025/12/30 18:23:07 by moerrais         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    i = 0
    res = 0
    while i < 3:
        res += int(input(f"Day {i} harvest: "))
        i += 1
    print (f"Total harvest: {res}")