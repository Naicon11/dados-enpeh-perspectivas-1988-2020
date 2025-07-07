import os
from pathlib import Path
from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfMerger
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


pastas_origem = [
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_01_forms_prof",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_02_memoria_eh",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_03_livro_didatico",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_04_educacao_historica",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_05_historia e historiografia do EH",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_06_EH_museus e patrimonio",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_07_EH e suas linguagens",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_08_EH_anos iniciais",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_09_historia local e EH",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_10_curriculo e EH",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_11_EH_id_alteridade",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\GT_12_aprendizagem Historica",
    r"C:\Users\naico\OneDrive\Área de Trabalho\enpeh\8o ENPEH - 2008\Gts_consolidados"
]

def aplicar_ocr_pdf(caminho_pdf_original, caminho_pdf_saida):
    try:
        imagens = convert_from_path(caminho_pdf_original, dpi=300)
        pdf_ocr = []

        for imagem in imagens:
            pdf_pesquisavel = pytesseract.image_to_pdf_or_hocr(imagem, lang='por', extension='pdf')
            pdf_ocr.append(pdf_pesquisavel)

        merger = PdfMerger()
        for pagina in pdf_ocr:
            from io import BytesIO
            merger.append(BytesIO(pagina))
        with open(caminho_pdf_saida, 'wb') as f_out:
            merger.write(f_out)
        print(f"OCR salvo em PDF: {caminho_pdf_saida}")

    except Exception as e:
        print(f"Erro ao processar {caminho_pdf_original}:", e)

for pasta_origem in pastas_origem:
    for raiz, dirs, arquivos in os.walk(pasta_origem):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".pdf"):
                caminho_pdf = os.path.join(raiz, arquivo)
                
                raiz_path = Path(raiz)
                raiz_ocr = Path(str(raiz_path).replace("8o ENPEH - 2008", "8o ENPEH - 2008_ocr"))
                raiz_ocr.mkdir(parents=True, exist_ok=True)

                caminho_pdf_saida = raiz_ocr / Path(arquivo).name

                aplicar_ocr_pdf(caminho_pdf, caminho_pdf_saida)




