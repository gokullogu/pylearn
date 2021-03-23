#loop through the tuple using for
fruit=("apple","banana","carrot","beetroot")

for x in fruit:
    print(x)
#apple
#banana
#carrot
#beetroot

#loop through tuple using index numbers
print("for loop by index number:")
for i in range(len(fruit)):
    print(i,"",fruit[i])
#for loop by index number:
#0  apple
#1  banana
#2  carrot

#while to loop through tuple using index
print("while loop by index number:")
i=0
while i <len(fruit):
    print(i,"",fruit[i])
    i+=1
#while loop by index number:
#0  apple
#1  banana
#2  carrot


