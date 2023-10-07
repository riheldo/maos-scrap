from typing import List

def scrap_project(url: str):
    print("Iniciando scrap do projeto")
    # 1. capturar a pagina
    # 2. extrair a informação
    # 3. retornar um objeto com os dados


def scrap_projects_page(url: str):
    # 1. capturar a pagina
    # 2. listar todas as links das thumbs
    projects_list: List[str] = []

    # 3. para cada link, fazer o scrap da pagina da thumb
    projects_data_list = []
    for projectItem in projects_list:
        project_data = scrap_project(projectItem)
        projects_data_list.append(project_data)

    return projects_data_list
