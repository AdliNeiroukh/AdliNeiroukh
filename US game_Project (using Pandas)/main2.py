import turtle
import pandas

screen = turtle.Screen()
screen.title("usa game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_col_list = data.state.to_list()

answer_list = []

while int(len(answer_list)) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/ 50 States Correct", prompt="The answer is").title()


    if answer_state == "Exit":
        missing_state = []
        for state in states_col_list:
            if state not in answer_list:
                missing_state.append(state)
                new_df = pandas.DataFrame(missing_state)
                new_df.to_csv("learing")

        break

    if answer_state in states_col_list:
        # FIX 2: Uncomment this so the count actually increases!
        answer_list.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]

        # Using .item() is correct here to get the raw coordinate
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)



















