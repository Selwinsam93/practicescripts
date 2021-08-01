def reverse(sentence):
    splitt = sentence.split(' ')
    flag = ' '
    for i in splitt:
        flag = i + flag
    return flag

print(reverse("fake it till you make it"))
