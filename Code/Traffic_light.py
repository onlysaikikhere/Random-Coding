def update_light(current):
    y=current.lower()
    if y == "green" :
        return ("yellow")
    elif y == "yellow" :
        return ("red")
    elif y == "red" :
        return ("green")
x = "green"
print(update_light(x))