def insert_value_front(tuple_input, value_to_insert):
    return (value_to_insert,) + tuple_input

input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)