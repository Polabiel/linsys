\documentclass[11pt]{article}

% line spacing
\linespread{1.5}

% paragraph spacing
\setlength{\parindent}{1.0cm}
\setlength{\parskip}{0.2cm}

% packages
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{amsmath}
\usepackage[brazil]{babel}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{float}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage[utf8]{inputenc}
\usepackage{lipsum}
\usepackage{microtype}
\usepackage{nicefrac}
\usepackage{rotating}
\usepackage{template}
\usepackage{url}
\usepackage{xcolor}

% definitions
\theoremstyle{definition} \newtheorem{definition}{Definição}

% examples
\theoremstyle{definition} \newtheorem{example}{Exemplo}

% colors
\definecolor{javared}{rgb}{0.6,0,0} % for strings
\definecolor{javagreen}{rgb}{0.25,0.5,0.35} % comments
\definecolor{javapurple}{rgb}{0.5,0,0.35} % keywords
\definecolor{javadocblue}{rgb}{0.25,0.35,0.75} % javadoc

% packages settings
\graphicspath{{./images/}}

\hypersetup
{
    colorlinks = true,
    linkcolor = blue,
    citecolor = blue,
    urlcolor = blue,
    bookmarksdepth = 4
}

\title{Projeto Sistemas de equações lineares} 
\author{Gabriel Oliveira dos santos \\ \texttt{cc23600@g.unicamp.br} \And Julia Vitória Santos Bacellar \\ \texttt{cc23526@g.unicamp.br}}

\begin{document}

\maketitle

\section{Introdução}

{Nós estudantes (Gabriel e Julia) do \textit{\href{https://cotuca.unicamp.br/}{Colégio Técnico de Campinas}}, fomos introduzidos a resolver um problema de Sistema de equações lineares utilizado a linguagem \href{https://www.python.org/}{Python} com a biblioteca auxiliar \href{https://scipy.org/}{Scipy}.}
{Sistemas de equações lineares são fundamentais em várias áreas da ciência, tecnologia e engenharia, aparecendo frequentemente em problemas que requerem a determinação de valores que satisfaçam múltiplas condições lineares simultâneas. Para resolver esses sistemas de forma eficiente, o \href{https://pt.wikipedia.org/wiki/Algoritmo_simplex}{Algoritmo Simplex} se destaca como uma técnica robusta de otimização linear. Este método encontra a solução ótima de um problema linearmente restrito de maneira iterativa.}

\subsection{Objetivos}

{E por sua vez, esse relatório tem como objetivo apresentar uma aplicação do Algoritmo Simplex na resolução de sistemas de equações lineares utilizando um software, que foi desenvolvido pelos alunos. bem como analisar os resultados obtidos para diferentes configurações de instâncias.}

\section{Experimentos computacionais}

{Todos os experimentos computacionais foram realizados em um PC com sistema operacional Windows, equipado com um processador \href{https://www.intel.com.br/content/www/br/pt/products/sku/52209/intel-core-i52500-processor-6m-cache-up-to-3-70-ghz/specifications.html}{Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz 3.70 GHz} e 12 GB de memória RAM. O Algoritmo Simplex foi implementado em Python utilizando a biblioteca SciPy.}

\subsection{Implementação}

{Como foi dito no \href{https://cdn.discordapp.com/attachments/990092066694524980/1251955505941839892/projeto2.pdf?ex=667075ec&is=666f246c&hm=c3939979dac83efa757c6360efbd0db8b65ccf560cd1109bc99dcf5f84f42808&}{enuciado}, Para resolver os sistemas de equações lineares, utilizamos a linguagem de programação Python junto com a biblioteca SciPy, que oferece funcionalidades robustas para otimização e resolução de problemas lineares. Abaixo, descrevemos como implementamos o algoritmo Simplex para resolver diferentes problemas de otimização linear:}
\begin{enumerate}
    \item Definição da Função Objetivo: Cada problema requer a definição de uma função objetivo que queremos minimizar ou maximizar. Por exemplo, a função objetivo pode ser algo como "\(\min{ 5x_1 + x_2}\)" ou "\(\max 2x_1 - 3x_2\)".
    \item Restrições: As restrições de cada problema são especificadas em forma de desigualdades (por exemplo, \(2x_1 + x_2 \geq 6\)) e igualdades (por exemplo, \(x_1 + x_2 = 4\)). Essas restrições são transformadas em uma matriz de coeficientes e um vetor de termos independentes.
    \item Limites das Variáveis: Definimos os limites para as variáveis envolvidas no problema. Normalmente, estas variáveis são restritas a valores não-negativos.
    \item Resolução com Simplex: Utilizamos a função linprog da biblioteca SciPy para resolver os problemas de otimização linear utilizando o método Simplex. A função retorna a solução ótima, o valor da função objetivo e informações sobre o processo de otimização.
    \item Análise dos Resultados: Os resultados obtidos são analisados e apresentados para cada problema, incluindo os valores das variáveis, o valor da função objetivo e mensagens de status do algoritmo.
\end{enumerate}

\section{Algoritmo Simplex}

{O Algoritmo Simplex é uma abordagem iterativa para a resolução de problemas de programação linear. Ele inicia a partir de uma solução viável básica e, em cada iteração, se desloca para uma solução adjacente que melhora o valor da função objetivo, até que uma solução ótima seja alcançada. No contexto de sistemas de equações lineares, o Simplex pode ser empregado para encontrar soluções de problemas formulados como programas lineares.}

\section{Resultados}

{No resultado é possivel visualizar dentro do Github as instances com todas as declarações de erro, Os resultados dos experimentos realizados são apresentados na Tabela \ref{tab:resultados}. Esta tabela mostra o gap, a função objetivo, o valor capturado e a equação realizada para cada instância testada.

\begin{table}[H]
    \centering
    \begin{tabular}{cccc}
        \toprule
        \textbf{Gap} & \textbf{Função Objetivo} & \textbf{Valor Capturado} & \textbf{Equação Realizada} \\
        \midrule
        & & & \\
        & & & \\
        & & & \\
        & & & \\
        \bottomrule
    \end{tabular}
    \caption{Resultados dos experimentos realizados}
    \label{tab:resultados}
\end{table}
}

\section{Conclusões}

{O Algoritmo Simplex demonstrou-se eficaz na resolução de sistemas de equações lineares, proporcionando soluções ótimas de forma eficiente. Os resultados obtidos para a instância de teste validam a precisão e a eficiência do método. Para problemas de maior escala, o Simplex continua sendo uma ferramenta poderosa, embora técnicas adicionais possam ser necessárias para melhorar o desempenho computacional.

Em conclusão, o Algoritmo Simplex é uma abordagem robusta para resolver sistemas de equações lineares, sendo amplamente aplicável em diversas áreas que requerem soluções ótimas para problemas lineares.}

\begin{table}[ht]
    \centering
    \caption{Resultados dos Problemas de Otimização}
    \begin{tabular}{p{2cm} p{8cm} p{4cm}}
        \toprule
        \textbf{Problema} & \textbf{Resultado} & \textbf{Arquivo Markdown} \\
        \midrule
        1 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 0.0\\
        x2 = 6.0\\
        Função objetivo = 6.0\\
        Status = 0\\
        
        A solução ótima deste problema é x$^*$ = (0, 6) com f(x$^*$) = 6\\
        Solução Adquirida = [0. 6.]
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_1.md \\
        \midrule
        2 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 4.0\\
        x2 = 0.0\\
        Função objetivo = -8.0\\
        Status = 0\\
        
        Iterações = 1\\
        A solução ótima deste problema é x$^*$ = (4, 0) com f(x$^*$) = 8\\
        Solução Adquirida = [4. 0.]
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_2.md \\
        \midrule
        3 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 1.0\\
        x2 = 1.0\\
        Função objetivo = -56.0\\
        Status = 0\\
        
        A solução ótima deste problema é x$^*$ = (1, 1, 0) com f(x$^*$) = 56\\
        Solução Adquirida = [1. 1. 0.]
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_3.md \\
        \midrule
        4 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 400.0\\
        x2 = 0.0\\
        Função objetivo = 0.0\\
        Status = 0\\
        
        A solução ótima deste problema é x$^*$ = (400, 0, 0, 0) com f(x$^*$) = 0\\
        Solução Adquirida = [400. 0. 0. 0.]
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_4.md \\
        \midrule
        5 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 0.0\\
        x2 = 1.0\\
        Função objetivo = -33.0\\
        Status = 0\\
        
        A solução ótima deste problema é x$^*$ = (0, 1, 11) com f(x$^*$) = 36\\
        Solução Adquirida = [0. 1. 11.]
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_5.md \\
        \midrule
        6 & 
        \begin{tabular}[t]{@{}l@{}}
        O problema não foi resolvido pois não foi especificado no enunciado.
        \end{tabular} & 
        D:\textbackslash linsys-1\textbackslash src\textbackslash..\textbackslash instances\textbackslash markdown\_Problema\_6.md \\
        \midrule
        7 & 
        \begin{tabular}[t]{@{}l@{}}
        x1 = 8.318765740446844\\
        x2 = 0.0\\
        Função objetivo = -74.8688916640216\\
        Status = 0\\
        
        Iterações = 15\\
        A solução ótima deste problema é x$^*$ = (0, 1, 11) com f(x$^*$) = 36\\
        Solução Adquirida = [8.31876574 0.]
        \end{tabular} & 
        - \\
        \bottomrule
    \end{tabular}
\end{table}

\end{document}