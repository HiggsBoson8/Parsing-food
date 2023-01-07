import json, csv, time, random
from bs4 import BeautifulSoup

# #Прочитали и сохранили HTML в переменную src
with open("11_Овощи-и-зелень.html", "r") as file: 
    src = file.read()
# # print(src)

# #Прочитали в BeautifulSoup src и добавили обработчик lxml 
soup = BeautifulSoup(src, "lxml")
# # print(soup)

# # Мы нашли класс таблицы и нашли внутри thead, а внутри thead нашли tr, а внутри tr нашли th c помощью find_all
# #find_all - мы указываем find_all когда нужно вытащить сразу все схожие значения, и обернуть в список []
# title_table = soup.find(class_ = "mzr-tc-group-table").find("thead").find("tr").find_all("th")
# # print(title_table) 


# title = []

# for item in title_table:
#     title.append(item.text)

# with open("title.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     #writerow записывает не в следующую строку и он принимает 1 аргумент
#     writer.writerow(
#         title
#     )

row_table = soup.find(class_ = "mzr-tc-group-table").find("tbody").find_all("tr")


for item in row_table:
    product_info_item = item.find_all("td")

    product_name = product_info_item[0].text
    product_calories = product_info_item[1].text
    product_proteins = product_info_item[2].text
    product_fats = product_info_item[3].text
    product_carbohydrates = product_info_item[4].text


    with open(f"title.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
        (
            product_name,
            product_calories,
            product_proteins,
            product_fats,
            product_carbohydrates,
        )
    )

