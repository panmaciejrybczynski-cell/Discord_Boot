def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


my_token = "MTU1MjczNTI5MjIyODc3MTkzMQ.GyQUVM.3nb5ba9EOoFXoSbNKwQ5WsdPCuUX9Bs_N1MYS0"