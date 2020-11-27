
def vignere(txt='', key='', typ=''):
    if not txt:
        print ("Veuillez entrer un text.")
        return
    if not key:
        print ("Veuillez fournir une cle.")
        return
    if typ not in ('d', 'e'):
        print ("""Veullez choisir "d" pour decryption ou "e" pour encryption""")
        return

    
    key_to_int = [ord(i) for i in key]
    txt_to_int = [ord(i) for i in txt]
    resultat = ''
    for i in range(len(txt_to_int)):
        shift =key_to_int[i % len(key)]
        if typ == 'd':
            shift *= -1

        v = (txt_to_int[i] - 32 + shift) % 95

        resultat += chr(v + 32)

    return (resultat)
# Driver code 
if __name__ == "__main__": 
    string = "check on the updated code"
    key = "typo"
    q = vignere(string,  key, 'e')
    print(q)
    print (vignere(q, key, 'd'))