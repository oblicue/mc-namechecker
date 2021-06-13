import requests
with open('./names.txt', 'w') as file:
    file.write('')

times = int(input("how many usernames? "))

writetofile = input("write non-taken users to names.txt? ")

for i in range(times):
    amongnus = input("What username do u wanna check? ")

    r = requests.get("https://api.ashcon.app/mojang/v2/user/" + amongnus)

    if(r.status_code == 404):
        print("Username " + amongnus + " is not in use")
        if(writetofile == "yes"):
            with open('./names.txt', 'a') as file:
                file.write(amongnus + "\n")
    else:
        print("Username is taken.")
