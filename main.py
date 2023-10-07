from src import constant
from src.scrap_projects_page import scrap_projects_page

print("Executando script scrap em "+constant.URL)

infos = scrap_projects_page(constant.URL_MANGA_PAGE)

print("Informação obtida: ")
print(infos)