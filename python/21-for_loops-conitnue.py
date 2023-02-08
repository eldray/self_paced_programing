#loop control statements = change the normal sewuence of a loop iteration
#continue = used to skip to the next iteration of the loop
phone_number = "123-456-789"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")