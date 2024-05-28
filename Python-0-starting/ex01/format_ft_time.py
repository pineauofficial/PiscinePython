import time;

current_time = time.time()
formatted_time = "{:,.4f}".format(current_time)
scientific_notation = "{:.3}".format(current_time)
formatted_date = time.strftime("%b %d %Y") #prends le temps actuel si rien n'est specifie

print("Seconds since January 1, 1970:", formatted_time, "or", scientific_notation, "in scientific notation")
print(formatted_date)
