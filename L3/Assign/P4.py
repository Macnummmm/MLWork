def krill_consumption(feeding, whales):
        a = 0
    
        for i in whales:
                if i in feeding:
                        a += feeding[i] * whales[i]
        return a




if __name__ == '__main__':
        feeding = {'Humpback whale': 2000, 'Gray whale': 1500, 'Bowhead whale':
2500, 'Blue whale': 3600}
        whales = {'Humpback whale': 8, 'Gray whale': 3, 'Bowhead whale': 1,
'Blue whale': 12}
        total_consum = krill_consumption(feeding, whales)
        print('Estimate daily consumption: %d kg of krill'%total_consum)

        feeding = {'Humpback whale': 2000, 'Gray whale': 1500, 'Bowhead whale':
        2500, 'Blue whale': 3600}
        whales = {'Bowhead whale': 80000}
        total_consum = krill_consumption(feeding, whales)
        print('Estimate daily consumption: %d kg of krill'%total_consum)
# f = feeding.spilt()
# print(f)