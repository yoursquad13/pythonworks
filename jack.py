text = "Chocolatey Salty Balls"

index = 0

for i in text:
    if i == "y":
        break
    index = index + 1

new_text = text[:index] + text[index+1:]
print(new_text)
