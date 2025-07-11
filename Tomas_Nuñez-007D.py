# Orden de productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...] 
lista_Productos = {
['8475HD','HP','8GB','DD','1TB','Intel Core i5','Nvidia GTX1050']         
['2175HD','Acer','4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050']
['JjfFHD','Asus','16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti']
['fgdxFHD','HP','12GB','DD','1TB','Intel Core i3','integrada']
['GF75HD','Asus','12GB','DD','1TB','Intel Core i7','Nvidia GTX1050']                 
['123FHD','Acer','6GB','DD','1TB','AMD Ryzen 5','integrada']
['342FHD','Acer','8GB','DD','1TB','AMD Ryzen 7','Nvidia GTX1050']
['UWU131HD','dell','8GB','DD','TB','AMD Ryzen 3','Nvidia GTX1050']
}

print(lista_Productos)
#stock = {modelo: [precio, stock], ...] stock = {'8475HD': [387990,10],

lista_Stock = {
['8475HD',387990,10] 
['2175HD',327990,4]  
['JjfFHD',424990,1]               
['fgdxFHD',664990,21] 
['123FHD',290890,32] 
['342FHD',444990,7] 
['GF75HD',749990,2] 
['UWU131HD',349990,1] 
['2175HD',327990,0]
}

#Menu 
opc = int(input())
print("*** MENU PRINCIPAL ***")
print("Selecciona una opcion del menu: ")
print("***************************")
print("1). Stock de la marca   ")
print("2). Busqueda por precio ")
print("3). Eliminar producto   ")
print("4). Salir               ")

if opc == 1:
    input("Ingrese la marca a conusultar: HP ")
    print("El stock es 31 ")
    
elif opc == 1:
    input("Ingrese la marca a conusultar: Acer ")
    print("El stock es 43 ")
    
elif opc == 2:
    print("Ingrese precio minimo: ")
    print("Ingrese precio maximo: ")
    
elif opc == 2:
    print("Ingrese precio minimo: ")

    



