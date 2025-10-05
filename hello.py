import requests

response=requests.get("https://dog.ceo/api/breeds/list/all")

dict=response.json()


gool=[]

with open("dogs.txt", "w") as o:

    f=dict["message"]

    for key,value in dict.items():

        if key == "message":

            for xkeys,xvalue in value.items():

                if f[xkeys] != []:

                    gool.append(f"{xkeys}={f[xkeys]}")

    o.write("\n".join(gool))


