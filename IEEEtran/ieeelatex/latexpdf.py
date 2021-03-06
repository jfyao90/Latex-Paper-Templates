% -*- coding: UTF-8 -*-
\documentclass[UTF8]{ctexart}
\usepackage{multicol}
%数学包，这里没用到
%\usepackage{amsmath}
\usepackage{indentfirst}
%添加作者信息
\usepackage{authblk}
\usepackage{graphicx}
%设置标题字体，因为section一般为粗体。
\usepackage{fontspec}
\setCJKmainfont[BoldFont=KaiTi]{SimSun}
%页码格式
\pagestyle{plain}
%设置书签	
\usepackage[bookmarks=true,colorlinks,linkcolor=black]{hyperref}
%英文摘要
\newcommand{\enabstractname}{Abstract}
\newenvironment{enabstract}{%
\quotation
	\par\small
	\mbox{}\hfill{\bfseries \enabstractname}\hfill\mbox{}\par
	\vskip 2.5ex}{\par\vskip 2.5ex} 

\title{\Huge\CJKfamily{zhkai} 黎曼猜想的证明思路}	
\author{倔强的贝吉塔\textsuperscript{1}\quad 
	迈克尔· 阿提亚\textsuperscript{2}\thanks{英国皇家学会前主席，菲尔兹奖和阿贝尔奖双料得主。}\quad 
	马克思·普朗克\textsuperscript{3}}
\affil{（\textsuperscript{1}{清华大学佛系}\quad \textsuperscript{2}{英国皇家学会}\quad \textsuperscript{3}{德国威廉皇家学会}）}					   								
\date{}		
\begin{document}
	\maketitle
	{
		\footnotetext[1]{清华大学在读研究生。
		}
	}
	\begin{abstract}
		这篇文章和证明黎曼猜想没有任何关系，阿提亚先生也没有参与这篇文章的写作，普朗克前辈更不可能出现，这篇文章的题目，内容以及摘要完全是用来凑字数的。
	
		\textbf{关键字：}黎曼猜想, 凑字数
	\end{abstract}
		
	\begin{enabstract}
		This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.    This is the abstract in English.
			
	\textbf{Keywords:}  number, English\footnote[4]{作者：uncle\_gy, 
			来源：CSDN,  
			原文：https://blog.csdn.net/uncle\_gy/article/details/78305644 }
	\end{enabstract} 
\begin{multicols*}{2}%不平衡双栏，平衡双栏去掉*		
	\section{\CJKfamily{zhkai}前言}					
	黎曼猜想（或称黎曼假设）是关于黎曼$\zeta$ 函数$\zeta(s)$的零点分布的猜想，由数学家波恩哈德·黎曼于1859年提出。德国数学家戴维·希尔伯特在第二届国际数学家大会上提出了20世纪数学家应当努力解决的23个数学问题，其中便包括黎曼假设。现今克雷数学研究所悬赏的世界七大数学难题中也包括黎曼假设。\footnote[5]{Millennium Problems}
	\section{黎曼猜想的数学模型}
	黎曼$\zeta$函数$\zeta(s)$是级数表达式
	$$
	\zeta(s)=\sum_{n=1}^{\infty}{\frac{1}{n^{s}}}\quad {Re(s)>1,n\in N^{+}}
	$$
	在复平面上的解析延拓。

	叙述从简，主要不会。	
\end{multicols*}
\end{document}