'''nums = [12, 7, 5, 18, 21, 30, 11, 4]
Create dictionary:
{
'even':[12,18,30,4],
'odd':[7,5,21,11]
}
Extra requirement:
Lists must be sorted
Must be built using dictionary comprehension'''


nums = [12, 7, 5, 18, 21, 30, 11, 4]

dicto = {
    key : sorted([n for n in nums if (n%2== 0)== (key=="even")])
    for key in ("even","odd")
}

print(dicto)