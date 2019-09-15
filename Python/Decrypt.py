# https://crypto.interactive-maths.com/hill-cipher.html#decrypt
import sympy as sy

abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
MOD = len(abc)


# Ultra protinga multiplicative modular inverse(a^-1 mod n)
# funkcija isstack overflow :)))))
def MMI(a, n, s=1, t=0, g=0):
    if n < 1:
        return -1
    elif n < 2 and t % g:
        return True
    else:
        return MMI(n, a % n, t, s - a // n * t, g or n)


def mod(element):
    return element % MOD


def hill(text, k):
    key = sy.Matrix([[k[0], k[1]], [k[2], k[3]]])
    key_adjugate = key.T.adjugate().applyfunc(mod)
    key_mod_inverse = (MMI(key.det() % MOD, MOD) * key_adjugate).applyfunc(mod)


    plaintext = ''

    for i, j in zip(text[0::2], text[1::2]):
        pair = sy.MatMul(key_mod_inverse, sy.Matrix([[abc.index(i)], [abc.index(j)]]))
        plaintext += abc[pair[0, 0] % MOD] + abc[pair[1, 0] % MOD]

    return plaintext


# NĖTHI OZKDY LGTEF ŲČKRU MŠRVS
# ĮĘNFI GŪTYC RPYHZ OLIĖ
# raktas=[1, 22, 9, 7]
print(hill("NĖTHIOZKDYLGTEFŲČKRUMŠRVSĮĘNFIGŪTYCRPYHZOLIĖ", [1, 22, 9, 7]))

# Pavyzdys iš https://repl.it/@MariusPozniakov/decoderMIF apačioj
#TABEĖKŽNDPĮOFKVYĮŽVĘSRMŽSCŲBNŠHBYOĘUJŲSĄCHTĘRŠZHLĄ ...
#[15, 26, 13, 29]
print(hill("TABEĖKŽNDPĮOFKVYĮŽVĘSRMŽSCŲBNŠHBYOĘUJŲSĄCHTĘRŠZHLĄ", [15, 26, 13, 29]))
