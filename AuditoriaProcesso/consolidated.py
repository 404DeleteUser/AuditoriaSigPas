import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from .hierarquia import busca_organograma, organograma

# O . antes de hierarquia serve pra o main.py conseguir encontrar o arquivo


def fluxo_auditoria():

    caminho_auditoria = r"C:\Users\08477936137\Downloads\AuditoriaSigPas\PlanilhaBruta\faltas-e-descontos.csv"

    # auditoria le o caminho_auditoria e atribui o DataFrame a ela
    auditoria = pd.read_csv(caminho_auditoria, sep=";", encoding="latin1")

    pasta_raiz = Path(r"C:\Users\08477936137\Downloads\AuditoriaSigPas")

    # definindo o nome do arquivo que será criado na pasta raiz
    caminho_saida = pasta_raiz / "Auditoria.xlsx"

    # limpa o nome das colunas
    auditoria.columns = auditoria.columns.str.strip().str.replace(" ", "_", regex=False)

    # separa a coluna Matricula/Vinculo da planilha usando o delimitador "/"
    auditoria[["Matricula", "Vinculo"]] = auditoria["Matrícula/Vínculo"].str.split(
        "/", expand=True
    )

    # transforma essas colunas citadas em inteiro
    auditoria[["Matricula", "Vinculo"]] = auditoria[["Matricula", "Vinculo"]].astype(
        int
    )

    # remove colunas que não serão necessárias
    auditoria.drop(["CPF", "Órgão", "Matrícula/Vínculo"], axis=1, inplace=True)

    # cria uma variavel que carrega o organograma completo
    hierarquia = organograma()

    # cria a coluna "Gabinete" iterando sobre a coluna "Setor" com apply()
    auditoria["Gabinete"] = auditoria["Setor"].apply(
        lambda setor_name: busca_organograma(hierarquia, setor_name)
    )

    # Renomeia as colunas
    auditoria = auditoria.rename(
        columns={
            "Nome_Usuário": "Servidor",
            "Quantidade_Horas": "SaldoFaltante",
        }
    )

    # filtra apenas as linhas onde a coluna "Gabinete" NÃO está vazia
    orgao_central = auditoria[auditoria["Gabinete"].notna()].copy()

    # Filtra apenas as linhas onde a coluna "Gabinete" está nula
    dre = auditoria[auditoria["Gabinete"].isna()].copy()

    # reorganiza colunas da planilha
    columns = [
        "Gabinete",
        "Setor",
        "Servidor",
        "Matricula",
        "Vinculo",
        "Data",
        "SaldoFaltante",
    ]

    # Reorganiza as colunas
    orgao_central = orgao_central[columns]
    # DRE não precisa por que no código atual não se tem gabinete das DREs

    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as writer:
        orgao_central.to_excel(writer, sheet_name="Orgao Central", index=False)
        dre.to_excel(writer, sheet_name="DRE", index=False)

    print(f"Planilha salva com sucesso em: {caminho_saida}")
