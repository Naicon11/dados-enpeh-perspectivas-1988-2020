import nltk
import PyPDF2
import re
import matplotlib.pyplot as plt
import pickle
from tqdm import tqdm

perc_aprendizagem = []
perc_ensino = []
edicoes = []
texto_nao_lido = [] 

palavras = ["aprendizagem", "ensino"]
variantes_espanhol = {"aprendizajes": "aprendizagem", "enseñanza": "ensino"}

anos_edicoes = {
    2: 1995,
    3: 1997,
    4: 1999,
    5: 2001,
    6: 2003,
    7: 2006,
    8: 2008,
    9: 2011,
    10: 2013,
    11: 2017,
    12: 2019
}

try:
    with open('progresso.pickle', 'rb') as progresso_file:
        progresso = pickle.load(progresso_file)
except FileNotFoundError:
    progresso = {}

fator_correcao = 1

for i in tqdm(range(2, 13), desc="Processando PDFs"):
    numero_edicao = f"{i:02d}"  

    pdf_file = fr'C:\Users\naico\OneDrive\Área de Trabalho\projetos python\enpeh analise\Por_ano_edição\ENPEH_{numero_edicao}.pdf'

    try:
        pdf = open(pdf_file, "rb")

        pdf_reader = PyPDF2.PdfReader(pdf)

        pdf_text = ""

        caracteres_lidos = 0

        for page in pdf_reader.pages:
            try:
                page_text = page.extract_text()
                pdf_text += page_text
                caracteres_lidos += len(page_text)
            except:
                pass

        pdf.close()

        total_caracteres = len(pdf_text)

        caracteres_nao_lidos = total_caracteres - caracteres_lidos

        pdf_text = re.sub(r"[^\w\s]", "", pdf_text)
        pdf_text = pdf_text.lower()
        pdf_words = nltk.word_tokenize(pdf_text)

        freq_palavras = {palavra: 0 for palavra in palavras}

        for word in pdf_words:
            if word in freq_palavras:
                freq_palavras[word] += fator_correcao
            elif word in variantes_espanhol:
                freq_palavras[variantes_espanhol[word]] += fator_correcao

        total_words = len(pdf_words)

        perc_aprendizagem_edicao = (freq_palavras["aprendizagem"] / total_words) * 100
        perc_ensino_edicao = (freq_palavras["ensino"] / total_words) * 100

        perc_aprendizagem.append(perc_aprendizagem_edicao)
        perc_ensino.append(perc_ensino_edicao)
        edicoes.append(f"{i} ({anos_edicoes[i]})")
        texto_nao_lido.append(caracteres_nao_lidos)

        progresso[i] = {'aprendizagem': perc_aprendizagem_edicao, 'ensino': perc_ensino_edicao}
        with open('progresso.pickle', 'wb') as progresso_file:
            pickle.dump(progresso, progresso_file)

    except Exception as e:
        print(f"Erro ao processar o PDF da edição {i}: {str(e)}")

plt.figure(figsize=(12, 6))  
plt.plot(edicoes, perc_aprendizagem, marker='o', linestyle='-', color="blue", label="Aprendizagem")
plt.plot(edicoes, perc_ensino, marker='o', linestyle='-', color="green", label="Ensino")

plt.xlabel("Edição (Ano)")
plt.ylabel("Porcentagem")

plt.legend()

plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # Garante que os rótulos do eixo x não se sobreponham

for i in range(len(edicoes)):
    print(f"Edição {edicoes[i]}:")
    print(f"Porcentagem de 'aprendizagem': {perc_aprendizagem[i]:.2f}%")
    print(f"Porcentagem de 'ensino': {perc_ensino[i]:.2f}%")
    if i < len(texto_nao_lido):  # Verifica se i é um índice válido em texto_nao_lido
        print(f"Tamanho do texto não lido: {texto_nao_lido[i]} caracteres")
    else:
        print("Tamanho do texto não lido: Dados não disponíveis")
    print()


