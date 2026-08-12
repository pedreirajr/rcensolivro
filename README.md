
<!-- README.md é gerado a partir do README.Rmd. Edite o .Rmd e rode `rmarkdown::render("README.Rmd")`. -->

<img src="img/capa/capa-web.jpg" align="right" width="300" alt="Capa do livro Censo Demográfico no R">

## Censo Demográfico no R

**Conceitos e aplicações para a análise do território brasileiro**

📖 **[Leia o livro online](https://pedreirajr.github.io/rcensolivro/)**

### Para encurtar o caminho entre a pergunta e o dado

O Censo Demográfico é a maior operação estatística do Brasil e a única
fonte que descreve a população e os domicílios do país inteiro em
recortes territoriais de alta resolução. Entretanto, essa riqueza chega
ao usuário fragmentada, distribuída por milhares de tabelas, arquivos
geográficos e registros de endereços. Quem se aproxima desse material
pela primeira vez costuma gastar mais tempo descobrindo onde o dado está
e o que ele significa do que analisando o fenômeno que motivou a busca.

Relatórios técnicos e textos científicos das mais variadas áreas ganham
densidade empírica quando partem de uma caracterização sociodemográfica
prévia com boa resolução geográfica. Um estudo epidemiológico que mapeia
casos de arboviroses precisa saber onde estão as crianças e as pessoas
idosas. Uma avaliação de política habitacional precisa saber onde há
adensamento excessivo e onde há subutilização do estoque habitacional.
Um plano de mobilidade precisa saber quem se desloca por transporte
coletivo e quanto dura a sua viagem. Saúde coletiva, engenharia,
geografia, economia, arquitetura, planejamento urbano, educação,
ciências sociais e estudos ambientais chegam ao Censo por caminhos muito
diferentes e esbarram nas mesmas dificuldades práticas.

É a essas dificuldades que o livro responde, sem supor formação prévia
em estatística, programação ou geoprocessamento. Cada produto censitário
é apresentado com exemplos reais de acesso, processamento, visualização
e mapeamento, todos reprodutíveis em R.

<br clear="all">

## Conteúdo

### Parte 1: Análise Exploratória de Dados com R

Capacitação prévia para quem chega sem experiência na linguagem.

|  | Capítulo |
|----|----|
| 1 | [Introdução ao R](https://pedreirajr.github.io/rcensolivro/1-introducao-ao-r.html) |
| 2 | [Estatística Descritiva](https://pedreirajr.github.io/rcensolivro/2-estatistica-descritiva.html) |
| 3 | [Manipulação de Dados Tabulares](https://pedreirajr.github.io/rcensolivro/3-manipulacao-de-dados-tabulares.html) |
| 4 | [Visualização de Dados Tabulares](https://pedreirajr.github.io/rcensolivro/4-visualizacao-de-dados-tabulares.html) |
| 5 | [Dados Geográficos](https://pedreirajr.github.io/rcensolivro/5-dados-geograficos.html) |

### Parte 2: O Censo Demográfico e seus Produtos

Um capítulo por produto, dos conceitos e da estrutura metodológica das
coletas até o processamento de cada base.

|  | Capítulo |
|----|----|
| 6 | [Censo Demográfico: Conceitos e Métodos](https://pedreirajr.github.io/rcensolivro/6-conceitos-e-metodos-censo.html) |
| 7 | [Agregados por Setor Censitário](https://pedreirajr.github.io/rcensolivro/7-agregados.html) |
| 8 | [Microdados da Amostra](https://pedreirajr.github.io/rcensolivro/8-microdados.html) |
| 9 | [Grade Estatística](https://pedreirajr.github.io/rcensolivro/9-grade-estatistica.html) |
| 10 | [CNEFE](https://pedreirajr.github.io/rcensolivro/10-cnefe.html) |
| 11 | [Características Urbanísticas do Entorno dos Domicílios](https://pedreirajr.github.io/rcensolivro/11-entorno.html) |

### Parte 3: Aplicações Territoriais

Cada capítulo parte de uma pergunta territorial concreta sobre um
município brasileiro e combina dois ou mais produtos do Censo para
respondê-la.

|  | Capítulo | Cidade |
|----|----|----|
| 12 | [Demografia](https://pedreirajr.github.io/rcensolivro/12-demografia.html) | Goiânia |
| 13 | [Habitação](https://pedreirajr.github.io/rcensolivro/13-habitacao.html) | João Pessoa |
| 14 | [Saneamento e Drenagem Urbana](https://pedreirajr.github.io/rcensolivro/14-saneamento.html) | Macapá |
| 15 | [Mobilidade e Acessibilidade](https://pedreirajr.github.io/rcensolivro/15-mobilidade.html) | Salvador |
| 16 | [Renda e Trabalho](https://pedreirajr.github.io/rcensolivro/16-renda-e-trabalho.html) | Manaus |

## Dados usados nos exemplos

Os arquivos de dados dos exemplos e exercícios não são versionados neste
repositório. Eles são distribuídos como assets de um [GitHub
Release](https://github.com/pedreirajr/rcensolivro/releases/tag/dados) e
baixados pelo próprio código dos capítulos, direto da URL. Boa parte dos
dados vem diretamente do IBGE em tempo de execução, pelos pacotes
`censobr` e `geobr`.

## Como renderizar localmente

O livro é escrito em [Quarto](https://quarto.org) com o motor do R. Além
do R e do Quarto, são necessários os pacotes usados ao longo dos
capítulos, entre eles `tidyverse`, `sf`, `geobr`, `censobr`, `srvyr`,
`patchwork`, `mapview`, `cnefetools` e `odbr`.

``` bash
quarto render                 # site HTML completo, em docs/
quarto render 7-agregados.qmd # um capítulo apenas
quarto preview                # preview com recarregamento automático
```

As versões impressas ficam num perfil separado, de modo que o
`quarto render` comum continua produzindo apenas o site.

``` bash
quarto render --profile impresso --to pdf  --output-dir _pdf
quarto render --profile impresso --to docx --output-dir _docx
```

## Organização do repositório

    *.qmd                 capítulos, na ordem da numeração
    index.qmd             prefácio
    _quarto.yml           configuração do livro e da saída HTML
    _quarto-impresso.yml  perfil das saídas em PDF e Word
    references.bib        bibliografia
    custom.css            estilos do site
    img/                  imagens, um diretório por capítulo
    docs/                 site renderizado, publicado pelo GitHub Pages

O `execute: freeze: auto` mantém os resultados congelados em `_freeze/`,
de modo que só os capítulos alterados são reexecutados a cada build.

## Licença

Copyright © 2026 Jorge Ubirajara Pedreira Junior. Todos os direitos
reservados.

O texto, as figuras e o código deste repositório são protegidos pela Lei
nº 9.610/1998. A leitura e a consulta online são livres, assim como a
citação de passagens com indicação da fonte. A reprodução, a
distribuição, a adaptação e a criação de obras derivadas dependem de
autorização prévia e por escrito do autor, que pode ser solicitada [por
aqui](https://pedreirajr.github.io/website/). Os termos completos estão
no arquivo [LICENSE](LICENSE).

Os dados do IBGE usados nos exemplos não são cobertos por esse aviso e
seguem as condições de uso definidas pelo instituto.

## Autor

**Jorge Ubirajara Pedreira Junior**
([pedreirajr.github.io/website](https://pedreirajr.github.io/website/))
