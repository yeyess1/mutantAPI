from statistics import mode
from django.db import models

# Create your models here.


class Mutant(models.Model):
    adnMutant = models.JSONField() 
    Human = models.JSONField()
    
    
#---- logica ------------------------------------------------------

def convertoArray(dic):
    arr = list(dic.values())
    return arr[0]
    

def charValidate(arr): #valida el tipo del array
    char = True
    for i in range(len(arr)):
        if type(arr[i]) != str:
            char = False
    return char

def proteinValidate(arr): # valdia el tipo de proteina 
    control = []
    c2 = []
    protein = False
    onlyC = charValidate(arr)
    if onlyC :
        for i in arr:
            for j in i:
                if (j == "A" or j == "T" or j == "C" or j == "G"):
                    control.append(j)
            if len(control)==len(i):
                c2.append(i)
                control.clear()

        if (len(c2) == len(arr)):
            protein = True
    return protein 

def isMutant(adn):
    decision = False
    repeted = []
    adnmutant = []
    mutant = False
    
    
    adn = convertoArray(adn)
    if proteinValidate(adn):

        for row in range(len(adn)):
            for column in range (len(adn[row])):
                repeted.clear()
                if( 
                (column-1 >= -1) & (column+1 <= len(adn[row])) & (row -1 >= -1 ) & (row+1 <= len(adn))
                ):#------------------validar extremos--------------------
                    
                    if column-1 >=0:
                        if adn[row][column] == adn[row][column-1]:
                            repeted.append(adn[row][column-1])
                            repetido = 2
                            if column-repetido>=0:  
                                if adn[row][column] == adn[row][column-repetido]:
                                    repeted.append(adn[row][column-repetido])
                                    repetido = 3                                
                                    if column-repetido>=0:
                                        if adn[row][column] == adn[row][column-repetido]:
                                            repeted.append(adn[row][column-repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False

                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()

                        else:repeted.clear()


                    if column+1 < len(adn[row]):
                        if adn[row][column] == adn[row][column+1]:
                            repeted.append(adn[row][column+1])
                            repetido = 2
                            if column+repetido < len(adn[row]):
                                if adn[row][column] == adn[row][column+repetido]:
                                    repeted.append(adn[row][column+repetido])
                                    repetido = 3
                                    if column+repetido < len(adn[row]):
                                        if adn[row][column] == adn[row][column+repetido]:
                                            repeted.append(adn[row][column+repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False


                                    else:repeted.clear()
                                        
                                else:repeted.clear()

                            else:repeted.clear()

                        else:repeted.clear()
                    
                    if row -1 >= 0: 
                        if adn[row][column] == adn[row-1][column]:
                            repeted.append(adn[row-1][column])
                            repetido = 2
                            if row -repetido >= 0:
                                if adn[row][column] == adn[row-repetido][column]:
                                    repeted.append(adn[row-repetido][column])
                                    repetido = 3
                                    if row -repetido >= 0:
                                        if adn[row][column] == adn[row-repetido][column]:
                                            repeted.append(adn[row-repetido][column])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False

                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()

                        else:repeted.clear()

                    if row+1 < len(adn):
                        if adn[row][column] == adn[row+1][column]:
                            repeted.append(adn[row+1][column])
                            repetido = 2
                            if row+repetido < len(adn):
                                if adn[row][column] == adn[row+repetido][column]:
                                    repeted.append(adn[row+repetido][column])
                                    repetido = 3
                                    if row+repetido < len(adn):
                                        if adn[row][column] == adn[row+repetido][column]:
                                            repeted.append(adn[row+repetido][column])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False
                                        
                                        else:repeted.clear()
                                            
                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()

                    if row -1 >= 0 and column-1 >=0:
                        if adn[row][column] == adn[row-1][column-1]:  
                            repeted.append(adn[row-1][column-1])
                            repetido = 2
                            if row -1 >= 0 and column-1 >=0:
                                if adn[row][column] == adn[row-repetido][column-repetido]:
                                    repeted.append(adn[row-repetido][column-repetido])
                                    repetido = 3
                                    if row -1 >= 0 and column-1 >=0:
                                        if adn[row][column] == adn[row-repetido][column-repetido]:
                                            repeted.append(adn[row-repetido][column-repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False
                                        
                                        else:repeted.clear()
                                            
                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()

                    if row -1 >= 0 and column+1 < len(adn[row]):
                        if adn[row][column] == adn[row-1][column+1]:
                            repeted.append(adn[row-1][column+1])  
                            repetido = 2
                            if (row-repetido >= 0 and column+repetido < len(adn[row])):
                                if adn[row][column] == adn[row-repetido][column+repetido]:
                                    repeted.append(adn[row-repetido][column+repetido])
                                    repetido = 3
                                    if row-repetido >= 0 and column+repetido < len(adn[row]):
                                        if adn[row][column] == adn[row-repetido][column+repetido]:
                                            repeted.append(adn[row-repetido][column+repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False
                                        
                                        else:repeted.clear()
                                            
                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()


                    if row+1 < len(adn) and column-1 >=0:
                        if adn[row][column] == adn[row+1][column-1]:
                            repeted.append(adn[row+1][column-1])
                            repetido = 2
                            if row+repetido < len(adn) and column-repetido >=0:
                                if adn[row][column] == adn[row+repetido][column-repetido]:
                                    repeted.append(adn[row+repetido][column-repetido])
                                    repetido = 3
                                    if row+repetido < len(adn) and column-repetido >=0:
                                        if adn[row][column] == adn[row+repetido][column-repetido]:
                                            repeted.append(adn[row+repetido][column-repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False
                                        
                                        else:repeted.clear()
                                            
                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()

                    if row+1 < len(adn) and column+1 < len(adn[row]):
                        if adn[row][column] == adn[row+1][column+1]:
                            repeted.append(adn[row+1][column+1])
                            repetido = 2
                            if row+repetido < len(adn) and column+repetido < len(adn[row]):
                                if adn[row][column] == adn[row+repetido][column+repetido]:
                                    repeted.append(adn[row+repetido][column+repetido])
                                    repetido = 3
                                    if row+repetido < len(adn) and column+repetido < len(adn[row]):
                                        if adn[row][column] == adn[row+repetido][column+repetido]:
                                            repeted.append(adn[row+repetido][column+repetido])
                                            decision = True if len(repeted) >= 3 else False
                                            adnmutant.extend(repeted) if decision else False
                                            

                                        
                                        else:repeted.clear()
                                            
                                    else:repeted.clear()

                                else:repeted.clear()

                            else:repeted.clear()


                    else:repeted.clear()      
            
            if len(adnmutant)/2 >= 2:
                mutant = True  
                
    return mutant


def saveMutant(adn):
    teamMutant = []
    control = False

    dna = convertoArray(adn)
    if proteinValidate(dna):
        control = isMutant(dna)
        print(control)
        if control:
            teamMutant.extend(dna)

    return {'dnaMutant':teamMutant}