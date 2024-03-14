def collect_data():
    ob = []
    cu = []

    while True:
        in_ob = input("Observation:")

        if in_ob == "":
            break
        else:
            in_cu = int(input("Found:"))
            ob.append(in_ob)
            cu.append(in_cu)

    return ob, cu


if __name__ == "__main__":
    observ, counting = collect_data()
    print(observ)
    print(counting)
