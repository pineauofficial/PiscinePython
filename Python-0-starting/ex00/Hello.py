ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World" #mutable
ft_tuple = (ft_tuple[0], "France") #immutable, doit etre recreer
ft_set.discard("tutu!") #ordre pas garantie, dot etre recreer
ft_set.add("Paris")
ft_dict["Hello"] = "42 Paris" #mutable, utilise des cles

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
