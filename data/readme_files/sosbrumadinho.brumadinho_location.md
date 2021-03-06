# Brumadinho Location

## Important

* If you're looking for the project to predict victims' location of
  disasters like Dam Collapse go to the project [Victims Location
  Prediction](https://github.com/sosbrumadinho/victims_location_prediction)

* If you want to contribute crawling data related with [Brumadinho dam
  disaster](https://en.wikipedia.org/wiki/Brumadinho_dam_disaster) go to
  the project [Brumadinho
  Crawlers](https://github.com/sosbrumadinho/brumadinho_crawlers)

## English
The aim of this project is to setup a repository of tools to support the search and rescue efforts, currently taking place at Brumadino/MG/Brazil, in response to the [**Brumadinho dam disaster**](https://en.wikipedia.org/wiki/Brumadinho_dam_disaster) occurred on 25 January 2019. As this file is being updated, 65 people have been confirmed dead and over 300 are still missing.

### How to colaborate:
* Please see the list of [Projects](https://github.com/dieegom/brumadinho_location/projects) that are being worked on and their respective issues. Project details are also listed below.
* If you can help with any issue, please add a comment to the issue to indicate that you will work on it. 
* If you are the first to work on any given project, you can choose the language or technology that you are more familiar with.
* If other volunteers are already helping with the project then please contact them to discuss what still needs to be implemented.
* Once your change is complete please submit your Pull Request tagging the associated issue.
* If you would like to suggest other tools for development then please create an issue and tag it with the #suggestion label.

We also have a Telegram discussion group. You can access it in [this link](https://t.me/joinchat/K2pTZk1Xjo0UEzmCzkJvXQ). Anyway, let's keep the discussion here on GitHub and let Telegram only for suggestions and/or others things not related to the code. 

You can fork the project at will. We will continue to improve the code throughout the week.

Join us in this project! This may be useful in the future as well.
Thank you!

### - Location 
This tool calculates the probable location of missing individuals' bodies by taking into consideration their last known location coordinates (i.e. latitude and longitude) and the tailing flows.

The algorithm still needs improvement and to improve it, we will need tailings physical-chemical data, location topographic map (.csv), simulations of the tailing spreading, and, of course, the latitude and longitude coordinates from the victims' cell phones.

The production enviromment is currently live at: https://brumadinho.osei.ong.br

We ask that those contributing to the project submit their Pull Requests as soon as possible to help improve the algorithm and make it available to those responsible for the search and rescue operations.

#### Ideas to be implemented:
*  http://fluidityproject.github.io/
*  http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
*  https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%B5es_de_Navier-Stokes
*  http://rlguy.com/gridfluidsim/
  
### Support material
* Using Python to Solve the Navier-Stokes Equations
  http://www.journalrepository.org/media/journals/JSRR_22/2015/May/Liu732015JSRR17346.pdf
* Grid Fluid Sim 3D Exemples
  https://github.com/rlguy/GridFluidSim3D/tree/master/src/examples/python



### - Where we had searched
This tool provides information regarding  areas that have already been inspected by the search and rescue teams. 

### - Report info
App to report missing people and missing animals.

### - Missing people list
This tool returns an updated .csv with all the names of missing people.

### - Identify the victim body
Through a set of photos provided by victims relatives in [this project](https://github.com/dieegom/brumadinho_location/projects/3) and based on the picture of the body found, identify who is the possible victim.

## Portugu??s
Pretendemos que esse projeto seja um reposit??rio de ferramentas para ajudar no resgate e localiza????o das v??timas atingidas pelo rompimento da barragem que ocorreu recentemente em Brumadinho/MG, onde muitas pessoas morreram e muitas outras ainda est??o desaparecidas. 

>No in??cio da tarde do dia 25 de janeiro de 2019 rompeu-se uma barragem de rejeitos de minera????o controlada pela Vale S.A.,constru??da no ribeir??o Ferro-Carv??o, na localidade de C??rrego do Feij??o.
>
> ??? https://pt.wikipedia.org/wiki/Rompimento_de_barragem_em_Brumadinho

### Como colaborar

* Acesse [Projetos](https://github.com/dieegom/brumadinho_location/projects) e veja a lista de ferramentas que estamos desenvolvendo e suas respectivas issues. Voc?? tamb??m pode ver essa lista logo abaixo. 
* Se voc?? puder ajudar com alguma issue, escreva um coment??rio dizendo que voc?? ir?? trabalhar nela.
* Se voc?? for o primeiro a trabalhar no projeto, voc?? pode escolher a linguagem ou tecnologia que se sinta mais confort??vel.
* Se mais volunt??rios estiverem ajudando, contate-os antes para saber o que ainda precisa ser implementado.
* Quando acabar, fa??am seu Pull Request informando a issue associada.
* Se tiver sugest??o de alguma outra ferramenta, cadastre uma issue usando o label #suggestion


N??s tamb??m temos um grupo de discuss??o no Telegram que pode ser acessado [neste link](https://t.me/joinchat/K2pTZk1Xjo0UEzmCzkJvXQ). De qualquer maneira, vamos manter a discuss??o aqui no GitHub e usar o Telegram apenas para sugest??es e/ou d??vidas n??o relacionadas ao c??digo. 


"Forkem" ?? vontade. Continuaremos melhorando o c??digo ao longo da semana. <br/><br/>
Vamos todos fazer a nossa parte! Isto pode ser ??til no futuro tamb??m.<br/>
Obrigado.

### - Location 

Essa ferramenta requer as coordenadas de latitude e longitude dos desaparecidos para calcular a estimativa baseando-se no fluxo de rejeitos <br/>
O algoritmo precisa ser melhorado (e muito) ainda. Al??m disso, fizemos apenas com os poucos dados que obtivemos. Ideal seria termos dados f??sico-qu??micos do rejeito, mapa topogr??fico (em .csv) do local, simula????es do rejeito se espalhando e, claro, latitude e longitude dos celulares.<br/>

Vamos deixar o sistema atualizado rodando em: https://brumadinho.osei.ong.br  <br/>
Pedimos aos Devs que fa??am seus Pull Requests para que possamos deixar este algoritmo mais robusto e dispon??vel para os respons??veis pelo resgate. "Forkem" ?? vontade. Continuaremos melhorando o c??digo ao longo da semana. <br/><br/>

####  Ideias a serem implementadas: <br/>
*  http://fluidityproject.github.io/ <br/>
*  http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/ <br/>
*  https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%B5es_de_Navier-Stokes <br/>
*  http://rlguy.com/gridfluidsim/<br/><br/>


### Materiais de apoio: 
* Using Python to Solve the Navier-Stokes Equations
  http://www.journalrepository.org/media/journals/JSRR_22/2015/May/Liu732015JSRR17346.pdf
* Grid Fluid Sim 3D Exemplos
  https://github.com/rlguy/GridFluidSim3D/tree/master/src/examples/python



### - Onde j?? foi buscado
Nesta ferramenta locais e equipes de resgatem podem fornecer informa????es de geolocaliza????o sobre as ??reas onde as buscas j?? foram realizadas.

### - Report info
App para relatar informa????es de pessoas e animais desaparecidos


### - Missing people list
Essa ferramenta retorna um arquivo .csv atualizado com todos os nomes das pessoas desaparecidas.


### - Identificar o corpo da v??tima
Utilizando um conjunto de fotos fornecidos por parentes e amigos da v??timas [neste projeto] (https://github.com/dieegom/brumadinho_location/projects/3) e baseado na foto do corpo, identificar quem possivelmente ?? a v??tima.
