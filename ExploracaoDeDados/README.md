**Sobre o Dataset**
- Escolhemos o AWS Honeypot Attack Data, um dataset que registra tentativas de ataques interceptados por honeypots. Possui 451,581 linhas de dados coletados entre 21:53 do dia 3 de março até 05:55 de 8 de setembro.

- As colunas são:

  - Date
  - Host
  - Source
  - Protocol
  - Type
  - Source Port
  - Dest Port
  - Source IP
  - Country Acronym
  - Country Name
  - City
  - City Abbreviation
  - Postal Code
  - Longitude
  - Latitude


**Tipos de Dados**
- O Dataset escolhido tem números de colunas iguais de atributos numéricos e textuais sendo 7 para cada. Por fim, possui uma única coluna no formato de datas.

**Objetivo**
- Analizar dados sobre ataques realizados e apresentar, de maneira gráfica, suas tendências, como locais mais atacados, horas em que mais ataques são realizados, países mais atigindos e outras especifidades. Por fim, pode-se pensar sobre usar o dataset para criar um algoritmo prediditivo de ameaças cibernéticas (com base nos atributos disponíveis).

**Rotulação do Dataset**
- Os rótulos são baseados no host do honeypot que recebe o ataque. Portanto, cada entrada corresponde a um ataque nos seguintes hosts:
  - groucho-oregon
  - groucho-us-east
  - groucho-singapore
  - groucho-tokyo
  - groucho-sa
  - zeppo-norcal
  - groucho-eu
  - groucho-norcal
  - groucho-sidney


**Distribuição do Dataset**
- As 15 colunas do Dataset são distribuídas da maneira a seguir:
  - Country Acronym: os 6 termos mais frequentes estão abaixo, enquanto todos os demais 172 possíveis valores ocorrem 10.000 vezes ou menos, dentre as 451.000 linhas.
    - CN: 191394.
    - US: 90005.
    - JP: 17204.
    - IR: 13042.
    - TW: 12150.
   
  - Country: da mesma forma que _Country Acronym_.
  
  - Type:
    ![type](https://user-images.githubusercontent.com/71611489/109509697-ef59b100-7a7f-11eb-906a-984661d3297f.png)
  
  - Source Port: as portas utilizadas variam de valores próximos a 0 até 65535 (eixo X), já que diferentes protocolos são utilizados. O eixo Y corresponde ao número de vezes que cada porta foi utilizada.
    ![spt](https://user-images.githubusercontent.com/71611489/109510515-ddc4d900-7a80-11eb-8884-a33892182a01.png)
  
  - Dest Port: Mesmo racíocínio de _Source Port_:
    ![dpt](https://user-images.githubusercontent.com/71611489/109511006-65aae300-7a81-11eb-98f7-d92f878d2a6c.png)
    
  - Date: segue a distribuição de dados por mês.
    ![date](https://user-images.githubusercontent.com/71611489/109512204-9d665a80-7a82-11eb-9283-6ea56344b468.png)
    
  - 

  


**Dados a Retirar/Manter**
- Seria interessante retirar a coluna **Type**, visto que esta não é valorada para a maior parte dos registros do dataset. 
- As colunas que guardam o nome das cidades e países de maneira abreviada (**Locale Abbreviation, Country Acronym**) dificilmente serão utilizadas para alguma análise, já que temos os dados na íntegra. 
- **Postal Code** (cep), **Latitude** e **Longitude** também poderiam ser descartados, visto que não estamos interessados na localização em que ataques ocorreram de forma tão detalhada.
- **Date** será quebrada em duas colunas, onde uma terá o formato dd/mm/aaaa e a outra a hora e minuto, ao invés de um único campo multivalorado contendo ambas informaçoes.
