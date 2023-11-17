def tabla_kirajzol(tabla):
    print(tabla[0])
    print(tabla[1])
    print(tabla[2])

def ell(tabla):
    for i in range(3):
        if tabla[i][0]==tabla[i][1]==tabla[i][2]=="x":
            return "x nyert"
    for i in range(3):
        if tabla[0][i]==tabla[1][i]==tabla[2][i]=="x":
            return "x nyert"
    if tabla[0][0]==tabla[1][1]==tabla[2][2]=="x":
        return "x nyert"
    if tabla[2][0]==tabla[1][1]==tabla[0][2]=="x":
        return "x nyert"

    
    for i in range(3):
        if tabla[i][0]==tabla[i][1]==tabla[i][2]=="o":
            return "o nyert"
    for i in range(3):
        if tabla[0][i]==tabla[1][i]==tabla[2][i]=="o":
            return "o nyert"
    if tabla[0][0]==tabla[1][1]==tabla[2][2]=="o":
        return "o nyert"
    if tabla[2][0]==tabla[1][1]==tabla[0][2]=="o":
        return "o nyert"

    for i in range(3):
        if tabla[0][i]=="-" or tabla[1][i]=="-" or tabla[2][i]=="-":
            return "még tart a játék"
    return "döntetlen"

def lehet_e_ide_rakni(tabla,sor,oszlop):
    if tabla[sor][oszlop]=="-":
        return True
    else:
        return False
def teszunk_lepest(tabla,lepes,jelem):
    tabla[lepes[0]][lepes[1]]=jelem

def tabla_masol(tabla):
    ujtabla=[]
    for i in tabla:
        ujtabla.append(i)
    return ujtabla

def letezo_lepesek_megszerzese(tabla):
    letezo_lepesek=[]
    for i in range(3):
        for j in range(3):
            if lehet_e_ide_rakni(tabla,i,j):
                letezo_lepesek.append((i,j))
    return letezo_lepesek
        
    


        
    

