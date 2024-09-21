from typing import List

def is_plantable(flowerbed: List[int], n: int) -> bool:

    plant_in_last_pot = False
    available_space = 0
    
    for i, curr_occupied in enumerate(flowerbed[:-1]):
        curr_free = not plant_in_last_pot and not curr_occupied and not flowerbed[i+1] 
        if curr_free:
            plant_in_last_pot = True
            available_space += 1

        plant_in_last_pot = curr_occupied or curr_free

    if not plant_in_last_pot and not flowerbed[-1]:
        available_space += 1

    return available_space >= n


flowerbed = [0,0,0,0,0]
n = 3
print(is_plantable(flowerbed, n))