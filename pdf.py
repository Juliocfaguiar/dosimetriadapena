import streamlit as st
import pandas as pd
import sqlite3
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



# Função para gerar o PDF
def gerar_pdf(resultado, pena_provisoria, pena_definitiva):
    """
    Gera um PDF com os dados do acusado e o resultado do cálculo da pena definitiva.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, "Poder Judiciário")
    pdf.drawString(50, 735, "Sentença Criminal Definitiva")
    pdf.drawString(50, 720, "-" * 80)

# Cabeçalho e Dados do Réu
    y = 700
    pdf.drawString(50, y, f"Acusado: {resultado[3]}")
    y -= 20
    pdf.drawString(50, y, f"CPF: {resultado[8]}")
    y -= 20
    pdf.drawString(50, y, f"Endereço: {resultado[9]}, {resultado[10]}, {resultado[11]}, {resultado[12]}, {resultado[13]}")
    y -= 30

# Corpo da sentença
    sentenca = f"""
                Vistos etc.
                
                O Ministério Público ofereceu denúncia contra {resultado[3]}, {resultado[4]}, {resultado[5]}, nascido em {resultado[6]},
                profissão: {resultado[7]}, portador do CPF {resultado[8]}, residente à {resultado[9]}, {resultado[10]}, {resultado[11]}
                {resultado[12]}, {resultado[13]}, pela prática do crime previsto no artigo {resultado[16]} do Código Penal conforme os
                fatos narrados na denúncia.
                
                Recebida a denúncia e realizada a instrução processual, entendo que restou comprovada a materialidade e autoria do delito,
                não havendo causas excludentes da ilicitude ou culpabilidade.
                
                Dessa forma, passo à dosimetria da pena, nos termos do art. 59 do Código Penal.
                
                Pena provisória fixada em: {pena_provisoria}
                Pena definitiva fixada em: {pena_definitiva}
                
                Ante o exposto, JULGO PROCEDENTE a pretensão punitiva estatal para CONDENAR 
                o réu {resultado[3]}, como incurso nas sanções do art. {resultado[16]} do Código Penal, à pena de {pena_definitiva}
                a ser cumprida em regime inicialmente adequado, nos termos do art. 33 do Código Penal.
                
                Publique-se. Registre-se. Intime-se.
                
                [Local], [Data]
                
                Juiz(a) de Direito
                """

# Escrevendo a sentença linha por linha
    for linha in sentenca.strip().split("\n"):
        pdf.drawString(50, y, linha.strip())  # Desenha a linha no PDF
        y -= 10  # Move a posição vertical para baixo
        if y < 50:  # Verifica se chegou ao fim da página
            pdf.showPage()  # Cria uma nova página
            pdf.setFont("Helvetica", 12)  # Redefine a fonte
            y = 750  # Reinicia a posição vertical no topo da nova página

    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()