import time
import turtle

screen = turtle.Screen()
screen.title("Canada")

img = 'canada-map.gif'
screen.addshape(img)
turtle.shape(img)


def is_ans_in_list(ans, list_prov):
    for index in range(len(list_prov)):
        if ans in list_prov[index]:
            return True, index
    return False, -1


provinces_and_terr = [
    ['Yukon Territory', 'Yukon', 'Yt'],
    ['Northwest Territories', 'Northwest', 'Nt'],
    ['Nunavut', 'Nu'], ['British Columbia', 'Bc'],
    ['Alberta', 'Ab'], ['Saskatchewan', 'Sk'],
    ['Manitoba', 'Mb'], ['Ontario', 'On'],
    ['Quebec', 'Qc'],['New Brunswick', 'Nb'], ['Nova Scotia', 'Ns'],
    ['Prince Edward Island', 'Pe', 'Pei'],
    ['Newfoundland and Labrador', 'Nl', 'Newfoundland']
]

list_of_coordinates = [
    (-346.0, 81.0), (-235.0, 48.0),
    (-69.0, 44.0), (-325.0, -100.0),
    (-236.0, -116.0), (-149.0, -138.0),
    (-71.0, -137.0), (49.0, -181.0),
    (187.0, -129.0), (283.0, -190.0),
    (330.0, -190.0), (326.0, -174.0),
    (367.0, -98.0)
]

is_game_on = True
correct_answers = 0

add_province_text = turtle.Turtle()
add_province_text.penup()
add_province_text.hideturtle()

correct_provinces_idx = []
prompt = "Enter the name of Canada's provinces and territories (type 'Exit' to quit)"
while is_game_on:
    user_answer = turtle.textinput(title=f"{correct_answers}/13 Provinces and territories", prompt=prompt)
    user_input = user_answer.title()
    if user_input == 'Exit':
        for index in range(len(provinces_and_terr)):
            if index not in correct_provinces_idx:
                add_province_text.color("red")
                add_province_text.goto(list_of_coordinates[index])
                add_province_text.write(provinces_and_terr[index][0], font=("Arial", 10, "normal"))
        time.sleep(3)
        is_game_on = False

    is_answer_correct, ind_of_province = is_ans_in_list(user_input, provinces_and_terr)
    # print(is_answer_correct)
    if is_answer_correct:
        correct_answers += 1
        correct_provinces_idx.append(ind_of_province)
        add_province_text.goto(list_of_coordinates[ind_of_province])
        add_province_text.write(provinces_and_terr[ind_of_province][0], font=("Arial", 10, "normal"))
        if correct_answers == 13:
            prompt = "Congratulations!!! You win! (type 'Exit' to quit)"
    time.sleep(0.01)

