from turtle import Turtle, Screen


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_snowflake(order, size=300):
    window = Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake - Level {order}")

    t = Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    print("Drawing complete. Close the window to exit.")
    window.mainloop()


if __name__ == "__main__":
    try:
        user_input = int(input("Enter recursion level (recommended 0-5): "))

        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            draw_snowflake(user_input)
    except ValueError:
        print("Invalid input. Please enter integer.")