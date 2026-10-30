#Food_Waste_Monitoring_System.py
prepared =int(input("Enter the amount of food prepared:"))
served =int(input("Enter the number of plates served:"))
waste = prepared - served
if (waste / prepared) * 100 > 10:
    print("High Wastage Alert!!!!")
else:
    print("Wastage within acceptable limits!!")
