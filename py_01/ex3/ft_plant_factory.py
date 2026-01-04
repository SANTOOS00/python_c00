# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: santoos <santoos@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 20:18:19 by moerrais          #+#    #+#              #
#    Updated: 2026/01/04 09:18:32 by santoos          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def print_data(self):
        return f"{self.name} ({self.height})cm, {self.age} days"

plant_data = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]
]
plants = []
for name, h, a in plant_data:
    plant = Plant(name,h ,a)
    plants.append(plant)
for plant in plants:
    print(f"Created: {plant.print_data()}")