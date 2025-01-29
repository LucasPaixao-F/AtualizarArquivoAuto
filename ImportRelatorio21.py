from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date
from time import sleep
import os
import shutil

origem = "C:/Users/TLPL - 1404/Downloads"
# destino =  "C:/Users/lucas/Documents/Automaçoes/download/relatorio" "C:/Users/lucas/Downloads"
# destino real = "C:/Users/TLPL - 1404/OneDrive - TLP SERVIÇOS/Dados BI/TREINAMENTO 2" C:/Users/TLPL - 1404/Downloads
destino = "C:/Users/TLPL - 1404/OneDrive - TLP SERVIÇOS/Dados BI/TREINAMENTO 2"


def limpar_pasta(caminho_pasta):
    try:
        # Verifique se o caminho é um diretório
        if os.path.isdir(caminho_pasta):
            # Percorra todos os arquivos na pasta
            for arquivo in os.listdir(caminho_pasta):
                caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                # Verifique se é um arquivo e o exclua
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
            print(f"Conteúdo da pasta {caminho_pasta} foi excluído com sucesso.")
        else:
            print(f"{caminho_pasta} não é um diretório válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao limpar a pasta: {e}")


caminho_da_pasta = "C:/Users/TLPL - 1404/OneDrive - TLP SERVIÇOS/Dados BI/TREINAMENTO 2"


def mover_arquivos_para_destino(origem, destino):
    try:
        lista = os.listdir(origem)
        for arquivo in lista:
            if arquivo.endswith("v6.xlsx"):
                origem_arquivo = os.path.join(origem, arquivo)
                destino_arquivo = os.path.join(destino, arquivo)
                shutil.move(origem_arquivo, destino_arquivo)
                print(
                    f"Arquivo '{arquivo}' movido de {origem} para {destino} com sucesso!"
                )
    except Exception as e:
        print(f"Erro ao mover os arquivos: {e}")


login = "coord.tlpservicos"
senha = "123456"

hoje = date.today()
data_atual = hoje.strftime("%d/%m/%Y")

data_padrao = "01/09/2023"

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get(
    "https://tlpservicos.afferolablms.com.br/youknow/loginYouKnow.seam?cid=1557238"
)

navegador.find_element("xpath", '//*[@id="login:username"]').send_keys(login)
navegador.find_element("xpath", '//*[@id="login:password"]').send_keys(senha)
navegador.find_element("xpath", '//*[@id="login:login-button"]').click()
navegador.implicitly_wait(2)
navegador.find_element(
    "xpath", "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/a[2]"
).click()
navegador.implicitly_wait(2)
navegador.find_element(
    "xpath",
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[5]/a[1]/div[1]/div[1]",
).click()
navegador.implicitly_wait(2)
navegador.find_element(
    "xpath",
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/form[1]/div[2]/div[1]/div[2]/a[1]",
).click()

# colcoar a data#
navegador.find_element(
    "xpath",
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[4]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span[1]/input[1]",
).send_keys(data_padrao)

navegador.find_element(
    "xpath",
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[4]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/span[1]/input[1]",
).send_keys(data_atual)

navegador.find_element(
    "xpath",
    "/html[1]/body[1]/div[2]/div[2]/div[1]/div[4]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/button[1]",
).click()

navegador.find_element(
    "xpath", "/html[1]/body[1]/div[2]/div[2]/div[1]/div[4]/form[1]/div[3]/input[1]"
).click()

sleep(80)

limpar_pasta(caminho_da_pasta)

mover_arquivos_para_destino(origem, destino)
