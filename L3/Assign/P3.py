
def clean_txt(mg):
    mg = mg.replace('.', ' ')
    mg = mg.replace(';', ' ')
    mg = mg.replace('\n', ' ')
    mg = mg.replace('  ', ' ')

    return mg


def word_freq(mg):

    cleaned = clean_txt(mg)

    wfreq = {}
    c = cleaned.split()

    for i in c:
        if '' or 'a' in wfreq:
            pass
        elif i not in wfreq:
            wfreq[i] = 1
        else:
            wfreq[i] += 1
      

    return wfreq

if __name__ == '__main__':
    txt = "Evil is done by oneself; " + \
          "by oneself is one defiled. \n " + \
          "Evil is left undone by oneself; " + \
          "by oneself is one cleansed. \n " + \
          "Purity and impurity are one's own doing. \n" + \
          "No one purifies another. \n" + \
          "No other purifies one."
          # excerpt from Attavagga: Self, www.accesstoinsight.org

    print(txt)

    wf = word_freq(txt)
    print('\nCount:')
    print(wf)