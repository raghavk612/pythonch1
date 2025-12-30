print("Program started")

message_list = list(input())
position1 = int(input())
position2 = int(input())

def swap(position1, position2):
    global message_list
    message_list[position1], message_list[position2] = (
        message_list[position2],
        message_list[position1]
    )

swap(position1, position2)
print("".join(message_list))

