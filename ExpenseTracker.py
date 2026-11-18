import json
expence_data=[{
    "amount":2500,
    "category":"food",
    "description":"coffee and drinks"
}]
newexpence={}



while(1):
    print("\n1. add expence\n","2.view all expencecs and total spent\n","3.exit\n" )
    choice=int(input("\nenter your choice\n"))
    if(choice==1):
        newexpence={}
        newexpence["amount"]=float(input("enter amount yoou spent "))
        newexpence["category"]=input("enter expence category ")
        newexpence["description"]=input("enter the description ")
        expence_data.append(newexpence)
        print("expence updated")
        with open("expence.json","w",newline="")as f:
            json.dump(expence_data,f,indent=4)
    elif(choice==2):
        sum=0
        if not expence_data:
            print("expence list is empty")
        else:
            for expence in expence_data:
                print(expence)
                sum+=expence["amount"]
            print("total expence ",sum)
    elif(choice==3):
        print("program ended !")
        break
    else:
        print("invalid choice! pelase pick 1-3")


# with open("expence.json","r",newline="")as f:
#     loaded_data=json.load(f)
# print(loaded_data)


