import pickle
def main(A):
    while(True):
        user = input("이름 학번 키 체중 원하는 체중 운동할 기간(분)>> ")
        user = user.split(" ")
        commend = input("명령어를 입력하시오>>")
        parse = commend.split(" ")
        data = []
        global name
        name= user[0]
        global number
        number = user[1]
        global height
        height = user[2]
        global weight
        weight = user[3]
        global wish_weight
        wish_weight = user[4]
        global exercise_minutes
        exercise_minutes = user[5]
        if parse[0] == 'show':
            for i in A:
                if (user[0] in i['name']) and (user[1] in i['number']): #동일인물일 경우
                    data.append(i)
                else: #동일인물이 아닐경우
                    userlist = {"name": name, "number": number, "height": height, "weight": weight,
                                "wish_weight": wish_weight, "exercise_minutes": exercise_minutes}
            return show(data) if data ==[] else show(userlist)
        elif parse[0] == 'quit':
            userlist = {"name": name, "number": number, "height": height, "weight": weight,
                        "wish_weight": wish_weight, "exercise_minutes": exercise_minutes}
            if user[2].isdigit() and user[3].isdigit() and user[1].isdigit() and user[4].isdigit():
                A += [userlist]
            else:
                print("Please enter numbers for number, height, weight, wish_weight and exercise_minutes")
            break
        else:
            print("Invalid command: " + parse[0])

def show(data):
    a = ''
    lose_weight = int(data['weight']) - int(data['wish_weight'])
    fh = open('Met.dat', "rb")
    met = pickle.load(fh)
    fh.close()
    print(met)
    index = 0
    for o in met:
        for p in met[o]:
            if exercise == p: #exercise는 랜덤으로 뽑힐 운동종목
                index = o
    print("감량할 체중은", lose_weight, "kg 입니다")
    print(index* weight*exercise_minutes)
    day = index * (3.5 * weight * exercise_minutes) * 5 / 1000
    print("하루에 해야하는 운동시간은 ", day, "입니다")

main(A)
