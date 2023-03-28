car ={}
cars = []

def registration_car (car):
    label = input("label car : ")
    price = input("price car : ")
    wheels = 4
    color = input("color car: ")
    from random import randint
    number = randint(100000000000 , 1000000000000)

    car = {
        "label" : label,
        "price" : price,
        "wheels" : wheels,
        "color" : color,
        "number" : number
        }

    cars.append(car)

def databace_car (cars):

    c = 0
    while c < len(cars):
        car = cars[c]
        print(car)
        c+=1

def filter():

    cheap_car = []
    medium_car = []
    expensive_car = []

    is_runing_car = True
    while is_runing_car:
        print("you want to sort cars : ")
        user_choose = input("""
            1) by price
            2) by color
            3) by label
            4) show all cars 
            5) exit to the previous menu
            : """)
        
        if user_choose == "1":

            for car in cars:

                if int(car["price"]) > 0 and int(car["price"]) <= 20000:
                    cheap_car.append(car)
                elif int(car["price"]) > 20000 and int(car["price"]) <= 100000:
                    medium_car.append(car)
                elif int(car["price"]) >= 100000:
                    expensive_car.append(car)

            print("cheap car")
            c = 0
            while c < len(cheap_car):
                car = cheap_car[c]
                print(car)
                c+=1
            print("\n")

            print("medium car")
            m = 0
            while m < len(medium_car):
                car = medium_car[m]
                print(car)
                m+=1
            print("\n")

            print("expensive car")
            e = 0
            while e < len(expensive_car):
                car = expensive_car[e]
                print(car)
                e+=1

        elif user_choose == "2":

            color_car = []
            user_color_car = []
            for car in cars:
                color_car.append(car["color"])

            print(" In your garage there are cars of the following colors " , (set(color_car)))
            user_color = input("what color car do you want? : ")
            if user_color in color_car:
                for car in cars:
                    if (car["color"]) == user_color:
                        user_color_car.append(car)
                c = 0
                while c < len(user_color_car):
                    car = user_color_car[c]
                    print(car)
                    c+=1

        elif user_choose == "3":
            label_car = []
            user_label_car = []
            for car in cars:
                label_car.append(car["label"])

            print(" In your garage there are cars of the following labels " , (set(label_car)))
            user_label = input("what label car do you want? : ")
            if user_label in label_car:
                for car in cars:
                    if (car["label"]) == user_label:
                        user_label_car.append(car)
                l = 0
                while l < len(user_label_car):
                    car = user_label_car[l]
                    print(car)
                    l+=1
        
        elif user_choose == "4":
            databace_car (cars)
        
        elif user_choose == "5":
            is_runing_car = False


print("Hello, what do you want?")
is_runing = True
while is_runing:
    user_choose = input("""
        1) add a car to the garage
        2) see what cars are in the garage
        3) choose a car from the garage
        4) quit 
        : """)
#   додаємо автомобіль в гараж 
    if user_choose == "1" :

        i = True
        while i :
            if i <= 10:
                print("add a car to the garage : ")
                registration_car (car)
                i+= 1
            elif i > 10:
                print("Еhere are already", i-1 , "cars in your garage. You want to add another car?")
                user_choose = input("""
                y) Yes
                n) No
                """)
                if user_choose == "y":
                    print("add a car to the garage : ")
                    registration_car (car)
                    i+= 1

                elif user_choose == "n":
                    databace_car (cars)
                    i = False

    elif user_choose == "2":
        databace_car (cars)

#   обираємо автомобіль з гаражу за фільтрами
    elif user_choose =="3":
        filter()    

#   завершуємо роботу програми
    elif user_choose =="4":
        break


