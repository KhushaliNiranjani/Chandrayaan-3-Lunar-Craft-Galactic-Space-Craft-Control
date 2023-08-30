from TDD import *

print("Enter Commands")
commands=input()
chandrayaan_3.execute_commands(commands)

final_position = chandrayaan_3.position
final_direction = chandrayaan_3.direction

print("Final Position:", final_position)
print("Final Direction:", final_direction)