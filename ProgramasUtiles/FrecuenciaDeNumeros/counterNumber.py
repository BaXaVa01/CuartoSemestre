def main():
    list = [77, 18, 63, 84, 38, 54, 50, 59, 54, 56, 36, 26, 50, 34, 44, 41, 58, 58, 53, 51, 62, 43, 52, 53, 63, 62, 62, 65, 61, 52, 60, 60, 45, 66, 83, 71, 63, 58, 61, 71]
    listString =["77 18 63 84 38 54 50 59 54 56 36 26 50 34 44 41 58 58 53 51 62 43 52 53 63 62 62 65 61 52 60 60 45 66 83 71 63 58 61 71"]

    convertirStringALista(listString)
    print(listString)
    counterNumber(list)


def convertirStringALista(listString):
    for i in range(0, len(listString)):
        listString[i] = listString[i].split()
        for j in range(0, len(listString[i])):
            listString[i][j] = int(listString[i][j])

def counterNumber(list):
    counter = [[0],[0],[0],[0],[0],[0],[0]]
    for i in list:
        match i:
            case i if  15 < i <= 25:
                counter[0][0] += 1
                
            case i if  25 < i <= 35:
                counter[1][0] += 1
            case i if  35 < i <= 45:
                counter[2][0] += 1
            case i if  45 < i <= 55:
                counter[3][0] += 1
            case i if  55 < i <= 65:
                counter[4][0] += 1
            case i if  65 < i <= 75:
                counter[5][0] += 1
            case i if  75 < i <= 85:
                counter[6][0] += 1
    print(counter)

main()