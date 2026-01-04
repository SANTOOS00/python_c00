# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: santoos <santoos@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 20:18:22 by moerrais          #+#    #+#              #
#    Updated: 2026/01/04 06:16:39 by santoos          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self):
        if self.age <= 60:
            self.height += 1
        else:
            self.height += 0.5
    
    def age_hani(self):
        self.age += 1
    
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    
    def simulate_week(plant):
        tmp = plant.height
        print ("== Day 1 ==")
        print (plant.get_info())
        for _ in range(6):
            plant.age_hani()
            plant.grow()
        print ("== Day 7 ==")
        print (plant.get_info())
        print (f"Growth this week: +{plant.height - tmp}cm")

data1 = Plant("Rose", 25, 30)
data1.simulate_week()