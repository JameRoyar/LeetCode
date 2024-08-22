import random

def generate_double_color_ball_numbers():
    red_balls = []
    while len(red_balls) < 6:
        random_number = random.randint(1, 33)
        if random_number not in red_balls:
            red_balls.append(random_number)

    blue_ball = random.randint(1, 16)

    return sorted(red_balls), blue_ball

for _ in range(10):
    red_balls, blue_ball = generate_double_color_ball_numbers()
    print(f"Red balls: {red_balls}, Blue ball: {blue_ball}")