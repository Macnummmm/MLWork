def sailor_mate(wind, boat):
    wind = ((int(wind.split(":")[0]) - 1) * 30) + (int(wind.split(":")[1]) * 0.5)
    boat = ((int(boat.split(":")[0]) - 1) * 30) + (int(boat.split(":")[1]) * 0.5)

    result = abs(wind - boat)
    new_head_dir = ((boat - wind + 180 ) % 360 ) - 180
    if new_head_dir < 0 :
        pass
   
        
    if new_head_dir > 0:
        if result > 0 and result <= 45:
            return "starboard broad reach"
        elif result > 45 and result < 90:
            return "starboard broad reach"
        elif result == 90:
            return "starboard beam reach"
        elif result > 90 and result < 135:
            return "starboard close hauled"
        elif result >= 135 and result <= 180:
            return "tacking"

    elif new_head_dir < 0:
        if result > 0 and result <= 45:
            return "port broad reach"
        elif result > 45 and result < 90:
            return "port broad reach"
        elif result == 90:
            return "port beam reach"
        elif result > 90 and result < 135:
            return "port close hauled"
        elif result >= 135 and result <= 180:
            return "tacking"

    elif new_head_dir == 0:
        return "run"


# Testing the function with the provided code
if __name__ == "__main__":
    r = sailor_mate("9:00", "12:00")
    print("9:00", "12:00", r)

    ticks = ["12:00", "1:30", "1:31", "2:59", "3:00", \
                "3:01", "5:59", "6:00", "6:01", "8:59", "9:00", "9:01", \
                "10:29", "10:30"]

    for b in ticks:
        r = sailor_mate("6:00", b)
        print("6:00", b, r)
