import locale
from docxtpl import DocxTemplate
from datetime import datetime

class Item:
    def __init__(self, un, qtd, desc, ref):
        self.un = un
        self.qtd = qtd
        self.desc = desc
        self.ref = ref


def main():
    locale.setlocale(locale.LC_ALL, '')
    tpl = DocxTemplate("tbl2.docx")

    context = {
        "contrato_descriçao": "Teste de template DOCX",
        "ETP_just": "Justificativa de ETP",
        "ETP_obj_just": "Objetivo do contrato",
        "contrato_obj": "Comprar Material",
        # "contrato_ata_preço": "Atas de preço SEPLAG",
        # "data": datetime.now().strftime("%d/%m/%Y"),
        "data": datetime.now().strftime("%d de %B de %Y"),
        "tbl_itens": [
            Item("UN", 50, "Mouse", "Mouse generico USB"),
            Item("UN", 75, "Teclado", "Teclado Generico USB"),
            Item("UN", 500, "Conector RJ45", "RJ45 CAT6"),
        ],
    }

    tpl.render(context)
    tpl.save("output2.docx")
    print("Ok!")


if __name__ == "__main__":
    main()
