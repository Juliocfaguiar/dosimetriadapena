import streamlit as st
import pandas as pd
import sqlite3
import calcular

def calculoPenal():

    df = pd.read_csv("crimes.csv",sep=";")



    for index, row in df.iterrows():
        try:
            if row['art'] == 155:
                if pd.notna(row['anoMax']) and pd.notna(row['anoMin']):
                    result = (row['anoMax'] - row['anoMin']) * 360 
                    result = result * 2/8
                    result = result / 360
                    
                    result_str = str(result)
                    split_result = result_str.split(".")
                    
                    if len(split_result) > 0 and int(split_result[0]) != 0:
                        print(f"O resultado final é: {int(split_result[0])} ano(s)")
                    else:
                        print("A parte inteira do resultado é zero.")
                        
                else:
                    print("anoMax ou anoMin não possuem valor, não é possível realizar o cálculo.")
        except KeyError as e:
            print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
            break

    # prompt: faça a mesma conta a cima ,transforme o resultado em str ,separa o resultado pelo ponto usando split,se o indice [1] não for zero , então transforme em int novamente ,divida ele por 100 e o resultado multiplica por 12 e arredonde o resultado em 2 casas

    for index, row in df.iterrows():
        try:
            if row['art'] == 155:
                if pd.notna(row['anoMax']) and pd.notna(row['anoMin']):
                    result = (row['anoMax'] - row['anoMin']) * 360 
                    result = result * 2/8
                    result = result / 360
                    
                    result_str = str(result)
                    split_result = result_str.split(".")
                    
                    if len(split_result) > 1 and split_result[1] != '0':
                        decimal_part = int(split_result[1])
                        final_result = round((decimal_part / 100) * 12, 2)
                        final_result = round(final_result*10, 2)
                        final_result = int(final_result)
                        print(f"O resultado final é: {final_result} mes(es)")
                    else:
                        print("A parte decimal é zero, não é possível realizar o cálculo.")
                        
                else:
                    print("anoMax ou anoMin não possuem valor, não é possível realizar o cálculo.")
        except KeyError as e:
            print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
            break


   