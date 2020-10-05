def molemass(mols):
    mm={"H":1.0079, "C":12.0107, "N":14.0067, "O":15.9994, "P": 30.9738, "S": 32.0660, "K": 39.0983, "F": 18.9984}
    total=0
    #CHHCHH
    for i in mols:
        total+=mm[i]
    return total
