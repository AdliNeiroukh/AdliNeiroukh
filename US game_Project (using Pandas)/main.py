import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_list = []

data = pandas.read_csv("50_states.csv")
state_column = data.state.to_list()
# print(state_column)


while len(answer_list) < 50:
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 States Correct", prompt="What's another state's name?").title()



    if answer_state == "Exit":
        missing_list = []
        missing_states = [ state for state in state_column if state not in answer_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #    It's an old option as now we are using comprehensive list
    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in state_column:
    #         if state not in answer_list:
    #             missing_states.append(state)
    #
    #             new_data = pandas.DataFrame(missing_states)
    #             new_data.to_csv("states_to_learn.csv")

        # break

    if answer_state in state_column:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #To hold a row name
        x_position = state_data.x.item() # Then to hold x row
        y_position = state_data.y.item() # Then to hold y row
        t.goto(x_position, y_position)
        t.write(answer_state)

        # if answer_state not in answer_list:
        #     answer_list.append(answer_state)


# This is extra if we want to update our csv file
# if answer_state == "Exit":
#     missing_states = []
#
#     for state in state_column:
#         if state not in answer_list:
#             missing_states.append(state)
#
#     new_data = pandas.DataFrame(missing_states, columns=["state"])
#     new_data.to_csv("states_to_learn.csv", index=False)
#     break


















# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#


