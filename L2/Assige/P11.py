
def perf_note ( lst, number ) :
    for i in lst :
        if i[1] <= number <= i[2] :           
            return i[0]
                 
if __name__ == "__main__":

    pnotes = [['head note', 1, 14],
    ['heart note', 15, 60],
    ['base note', 61, 100]]

    note = perf_note(pnotes,8)
    print(note)
    note = perf_note(pnotes,34)
    print(note)
    note = perf_note(pnotes,78)
    print(note)