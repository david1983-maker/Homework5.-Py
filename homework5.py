#кортежи
imutable_var=("sword", 6, True, 7.3) 
print(imutable_var) 

#кортеж это неизменяемый список элементов. 
imutable_var=("horse", 10, False, 5.7) 
imutable_var.append(20) 
print(imutable_var) 

# создание изменяемых, стуктур данных:списки.
imutable_list=["samurai", 15, True, 9.1]
imutable_list.remove("samurai") 
imutable_list.append("forest") 
print(imutable_list) 
