# # 1 Prepare function
# 3 I will save the vaue of "Juan"
# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}"
# # 2 call the funcion i got the argument zsolt

# username = "Zsolt"
# time_of_day = "morning"

# greeting = greet("Juan", "morning")


# print(greeting)



chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]
# total_eggs = 0
# for chicken in chickens:
#     total_eggs += chicken["eggs"]
# print(f"{total_eggs} eggs collected")

def count_eggs( bird_set ):
    total_eggs = 0

    for bird in bird_set:
        total_eggs += bird["eggs"]

        return total_eggs
