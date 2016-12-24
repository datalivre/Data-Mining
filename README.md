# Twitter - 10 Anos a 140 Caracteres?

## Uma Introdução a Mineração de Texto Usando a Twitter Streaming API e a Linguagem de Programação Python

Embora tenha feito um tremendo sucesso entre os anos de 2009 e 2011, o Twitter, que este ano já conta dez velinhas, passou por maus bocados desde a sua criação. O principal problema era o abandono da rede social causado pela incompreensão da proposta do microblog, que na sua concepção seria uma espécie de SMS de 140 caracteres voltado para a internet.

Tal limitação rendeu duras críticas ao Twitter e o abandono da rede social ou proibição de seu uso não se deu apenas entre os usuários comuns, mas também entre os profissionais, como jornalistas ou escritores que necessitam de cliques extras para escrever um texto de qualidade. O prêmio Nobel de Literatura, José Saramago, em entrevista, não economizou no sarcasmo ao fazer uma feroz critica à rede social, segundo ele “_Os tais 140 caracteres reflectem algo que já conhecíamos: a tendência para o monossílabo como forma de comunicação. De degrau em degrau, vamos descendo até o grunhido_”.

É certo que os empresários do Twitter não acompanharam a depreciação da empresa de braços cruzados, em verdade, muito tem se feito para atrair novos usuários ao ninho da empresa. Em setembro de 2013, eles encaminharam à Comissão de Títulos e Câmbio dos Estados Unidos documentos confidenciais para a sua abertura de capital na Bolsa de Valores e já em dezembro daquele mesmo ano anunciavam receita de 243 milhões de dólares. O Twitter obteve o terceiro melhor IPO daquele ano nos EUA vendendo 70 milhões de papéis e movimentando US$1,82 bilhão. Estimasse que o lucro da empresa pode ter chegado a 10 milhões de dólares. Todavia, a rede social ganhou apenas 9 milhões de novos usuários. Com isso, o CEO do Twitter, após o fechamento da Bolsa, garantiu que eles continuarão desenvolvendo novos recursos a fim de capturar novos membros.

Dito e feito, pouco tempo depois os usuários do Twitter foram agraciados com uma completa reformulação que deixou o microblog com a cara do Facebook, mas o melhor foi a flexibilização do limite de caracteres em tweets, implementado em 2016, para facilitar o uso dos novos usuários. Links para fotos, gifs, enquetes e vídeos não contam mais como caractere.

Verdade é que são muitas as novidades desenvolvidas pela equipe do Twitter, mas será que todo este esforço obteve retorno? É isso que vamos investigar com este artigo aplicando técnicas de processamento de linguagem natural, entre outros métodos analíticos, para extrair informações relevantes de dados de texto. Para tanto, foi utilizado 1 milhão de tweets capturados à deriva da rede social, que embora se apresentem ao usuário apenas como um simples campo de texto, constituem de uma fonte rica de informações que pode ser utilizada nas mais diversas análises de sentimento.

Em posse dos dados já devidamente estruturados, foi possível investigar se o antigo problema do microblog foi realmente sanado acessando a data de criação das contas dos usuários e comparando com o total de tweets postados. Como resultado, teremos o número de postagens por data de criação de cada conta e assim saberemos a atividade dos antigos e novos usuários. No mais, ainda será possível verificar:

* A popularidade da rede por país,

* Qual o idioma mais utilizado e

* Qual a média de publicações por usuário.

# Análise de Popularidade do Twitter

Se popularidade é a condição de ser conhecido por um grande número de pessoas, convenhamos que, para uma rede social se tornar realmente popular, cabe a ela adentrar e se espalhar homogeneamente por todas as fronteiras possíveis.

## 1. Qual a popularidade do Twitter por região?

Em nossa primeira análise, vamos desvendar se o Twitter voa por todo o mundo ou se esta aninhado em seu país de criação por ter asas pequenas.

> Para esta etapa, agrupou-se todos os tweets coletados por país de origem, com isso, obteve-se um conjunto para cada. Cada conjunto representa um único país, e a cada novo tweet inserido em um conjunto somou-se mais um.

 <img src="https://github.com/robbierobert/Minerando-o-Twitter/blob/master/1_tweetsCountry.png" alt="tweetsCountry">

Note que o Twitter é verdadeiramente popular nos EUA e no Brasil. Se a intenção fosse avaliar a utilização do Twitter por continente, as Américas estariam isoladas em primeiro lugar, visto que, os Estados Unidos com 57,43% de tweets enviados é a região que mais utiliza o microblog seguido do Brasil que detêm 26,76%. Em quarto lugar estão nossos hermanos Argentinos com 5,34%. Os demais continentes não oberam um resultado muito expressivo.

## 2. Qual o idioma mais utilizado para se escrever um tweet?

Bom, já sabemos que mais de 50 por cento de todos os tweets saem dos Estados Unidos da América e que o Brasil ocupa o segundo lugar no top 5 países que mais utilizam o Twitter, mas será que todos os tweets são escritos no idioma nativo do país de origem?

> Para esta etapa, assim como na anterior, agrupou-se todos os tweets coletados por idioma de origem gerando conjuntos de idiomas distintos. Depois contou-se quantos tweets pertenciam ao mesmo conjunto, o resultado pode ser analisado na imagem que segue:

 <img src="https://github.com/robbierobert/Minerando-o-Twitter/blob/master/2_tweetsLang.png" alt="2_tweetsLang">

A língua predominante no Twitter é definitivamente o inglês, mais de 50 por cento dos 1 milhão de tweets analisados foram escritos neste idioma. Em segundo lugar temos o espanhol, falado na Espanha e nas Américas, e em terceiro, o conjunto da língua portuguesa que tem como membros países como Portugal, Brasil e Angola. Curiosamente, o mandarim que conta com mais de 1 bilhão de falantes por toda a China, Malásia e Taiwan e outros pedaços do mundo, não estrela entre os 5 principais idiomas mais utilizados no Twitter.

## 3. Qual o total de tweets postados por conta de usuário?

E por fim, talvez nossa mais proeminente análise: a análise divisora de águas! Aqui, por meio da contagem de tweets por conta de usuário, investigaremos se realmente os membros do microblog abandonam mesmo a rede social.

> As contas de usuário do Twitter possuem um campo que contém a data de criação da mesma. Se todos os tweets coletados forem filtrados por este campo, teremos como resultado o total de tweets postado por conta.

 <img src="https://github.com/robbierobert/Minerando-o-Twitter/blob/master/3_tweetsData.png" alt="2_tweetsData">

O gráfico é um tanto esclarecedor, percebesse que os usuários do Twitter que criaram conta em 2006 já voaram do ninho e os seguintes, 2007 e 2008, vão seguindo o mesmo caminho. Note que existe uma grande diferença entre a relação das contas criadas em 2016 para as de 2015, seria essa uma evidência de que os usuários abandonam o microblog brevemente?

