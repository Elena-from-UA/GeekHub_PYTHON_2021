import time

lights_for_car = [[5,'Red'],[2,'Yellow'],[5,'Green'],[2,'Yellow']]
lights_for_people = [[7,'Green'],[7,'Red']]

def decorator(func):
    def wrapper():
        print('"For car" - "For people"')
        func()
    return wrapper

def traffic_lights_car():
    active_color = []
    for color in lights_for_car:
        while color[0] > 0: 
            active_color.append(color[1])
            color[0] -= 1
    return active_color


def traffic_lights_people():
    active_color = []
    for color in lights_for_people:
        while color[0] > 0:
            active_color.append(color[1])
            color[0] -= 1
    return active_color
            
@decorator       
def traffic_lights():
    func_result_car = traffic_lights_car()
    func_result_people = traffic_lights_people()
    zipped_list = list(zip(func_result_car,func_result_people))
    while True:
        for i,k in zipped_list:
            print(i,' - ',k)
            time.sleep(1)
    
traffic_lights()
