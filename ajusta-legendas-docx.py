"""Separa as legendas de tabela das de figura na saida .docx do livro.

O Quarto marca as legendas de tabela com o mesmo estilo das figuras
("Image Caption"). Como o campo da Lista de Figuras do Word procura esse
estilo e o da Lista de Tabelas procura "Table Caption", sem correcao a
Lista de Figuras engole as tabelas e a Lista de Tabelas sai vazia.

Este script troca o estilo das legendas que comecam com "Tabela" para
"Table Caption", que ja existe no modelo-word.docx e tem a mesma formatacao
do estilo das figuras.

Roda automaticamente como post-render do perfil impresso (ver
_quarto-impresso.yml) e nao faz nada quando a saida nao inclui .docx.
Tambem aceita o caminho de um .docx como argumento:

    python ajusta-legendas-docx.py _docx/Censo-Demografico-no-R.docx
"""

import os
import re
import sys
import zipfile
from pathlib import Path

PARAGRAFO = re.compile(r"<w:p(?:\s[^>]*)?>.*?</w:p>", re.DOTALL)
TEXTO = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.DOTALL)
# O Quarto separa o rotulo do numero com espaco nao separavel ( ).
PREFIXO_TABELA = re.compile("^Tabela[\\s ]")


def ajusta(xml):
    """Devolve o XML com as legendas de tabela reestilizadas e quantas foram."""
    trocas = 0

    def troca(m):
        nonlocal trocas
        p = m.group(0)
        if 'w:val="ImageCaption"' not in p:
            return p
        texto = "".join(TEXTO.findall(p)).lstrip()
        if not PREFIXO_TABELA.match(texto):
            return p
        trocas += 1
        return p.replace('w:val="ImageCaption"', 'w:val="TableCaption"')

    return PARAGRAFO.sub(troca, xml), trocas


def processa(caminho):
    with zipfile.ZipFile(caminho) as z:
        itens = [(i, z.read(i.filename)) for i in z.infolist()]

    total = 0
    temporario = caminho.with_suffix(".docx.tmp")
    with zipfile.ZipFile(temporario, "w", zipfile.ZIP_DEFLATED) as z:
        for info, dados in itens:
            if info.filename == "word/document.xml":
                xml, total = ajusta(dados.decode("utf-8"))
                dados = xml.encode("utf-8")
            z.writestr(info, dados)

    os.replace(temporario, caminho)
    print(f"{caminho.name}: {total} legendas de tabela reestilizadas")


def alvos():
    """Os .docx a corrigir, vindos do argumento ou do post-render do Quarto."""
    if len(sys.argv) > 1:
        return [Path(a) for a in sys.argv[1:]]

    saidas = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "")
    return [Path(l.strip()) for l in saidas.splitlines()
            if l.strip().lower().endswith(".docx")]


def main():
    encontrados = 0
    for caminho in alvos():
        # O Quarto grava o livro na raiz e so depois move para o --output-dir,
        # entao o caminho anunciado pode ainda nao existir na hora do post-render.
        if not caminho.exists():
            caminho = Path.cwd() / caminho.name
        if not caminho.exists():
            print(f"aviso: {caminho.name} nao encontrado, nada a fazer")
            continue
        processa(caminho)
        encontrados += 1

    if not encontrados:
        print("nenhum .docx nesta renderizacao, nada a fazer")


if __name__ == "__main__":
    main()
