from typing import List
from bs4 import BeautifulSoup
import requests

def scrap_project(url: str):
    print("Iniciando scrap do projeto")
    # 1. capturar a pagina
    # 2. extrair a informação
    # 3. retornar um objeto com os dados

    nome = None
    alternativo = None
    estudio = None
    nota = None
    generos = None
    tipo = None
    lancamento = None
    status = None
    endereco_imagem = None

    return {
        "nome": nome,
        "alternativo": alternativo,
        "estudio": estudio,
        "nota": nota,
        "generos": generos,
        "tipo": tipo,
        "lancamento": lancamento,
        "status": status,
        "endereco_imagem": endereco_imagem,
        "endereco_projeto": url
    }


def scrap_projects_page(url: str):
    # 1. capturar a pagina
    requests.get("https://neoxscan.net/manga/page")
    print("Scraping da pagina: "+url)
    site = requests.get(url)
    bs = BeautifulSoup(site.text)

    # 2. listar todas as links das thumbs
    projects_list: List[str] = []

    items = bs.find_all(class_='item-thumb')
    for item in items:
        itemA = item.find_next('a')
        projects_list.append(itemA.attrs.get('href'))

    print("Items obteined:", projects_list)

    # 3. para cada link, fazer o scrap da pagina da thumb
    projects_data_list = []
    for projectItem in projects_list:
        project_data = scrap_project(projectItem)
        projects_data_list.append(project_data)

    return projects_data_list
