# Computação Gráfica e Processamento de Imagens

## PROCESSAMENTO DIGITAL DE IMAGENS

## UNIDADE 4 – SEÇÃO 4.1

*Atividade do 2º Bimestre*

**1. Carregar uma Imagem**

![Coffe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCIDPKMxp1U54zIA_QI2QoolJW721ZAlp-Xw&s)

**2. Aplicar os Filtros:**
    **1. Observar as mudanças na imagem original após a aplicação dos filtros de média, mediana e Sobel.**
   **Observei a necessidade de incluir o filtro de Gaussiano, todavia percebi que é diferente do filtro Mediana, então esse trabalho**
    **inclui 4 filtros sendo media baseado em mediana.**
   
      • Sobel: É um filtro que destaca as bordas da imagem trazendo uma nitidez maior, ele utiliza duas mascaras de convolução(kernels), uma para o eixo y
       e outra para o eixo x. Ele detecta gradiente de intensidade da imagem em ambas direções. É de uso pratico ser usado por exemplo, em uma imagem de
       placa de transito ou para reconhecimento facial.
   
      • Média: Esse filtro suaviza a imagem e reduz os ruídos, o filtro substitui o valor do pixel pela media dos seus vizinhos em uma janela definida
       ele suaviza a imagem mas pode borrar as bordas, faz uma transição mais "suave" entre os pixels. Pode ser util por exemplo em tratar imagens medicas, 
       como tomografias, radiografias e ressonâncias magnéticas, o ruído pode prejudicar a detecção de estruturas ou anomalias ou em outros casos em que 
       seja necessario a remção de ruídos da imagem.
   
      • Mediana: Esse filtro funciona parecido com o media porém, ele substitui pela media dos vizinhos o pixel central e isso significa que ele escolhe 
       o valor central quando todos os valores são ordenados., muito bom para reduzir ruídos como o "sal e pimenta" onde pixels individuais em uma imagem
       são corrompidos por valores muito altos (brancos) ou muito baixos (pretos) onde ficam por exemplo, varios pontinhos preto na tela, ou seja, ele 
       reduzir os ruídos sem borrar tanto as bordas da imagem.
   
      • Gaussiano: O filtro Gaussiano aplica uma suavização suave à imagem usando a distribuição gaussiana (a famosa curva em formato de sino). O filtro 
       Gaussiano aplica a convolução da imagem com um kernel Gaussiano e então calcula a média ponderada de um pixel e seus vizinhos, com os vizinhos mais 
       próximos recebendo pesos maiores que os distantes. Isso faz com que a suavização seja mais natural, sem borrar tanto as bordas. A diferença dele com
       o filtro de mediana é que ele pode borrar as bordas, ele é ideal para reduzir ruidos suaves como o "ruído branco", é uma técnica linear diferente do
       filtro de mediana.

**3. Analisar os Resultados:**
    **1. Responder às seguintes perguntas:**
    **a) Como a imagem original mudou após a aplicação de cada filtro?**
      
      • Sobel: no código aplicado ele inverteu as cores, foi muito discreta a diferença entre eixo x, y e combinado, mas percebe-se uma facilidade maior em 
       encontrar alguns detalhes, como destacou mais os grãos de café na imagem.
   
      • Média: Em relação com a imagem original, quanto maior a janela de pixel (matriz) a imagem fica mais desfocada, trazendo mais suavidade para as bordas
       diminuindo assim sua nitidez sendo 25x25 mal da pra reconhecer os grão de café na imagem.
   
      • Mediana: Assim como na média, a mediana diminui a nitidez da imagem conforme o aumento da janela de pixels, porém dessa vez trazendo uma impressão de 
       borrão na imagem, como um desenho a tinta oléo molhado, ele mantém melhor as bordas na imagem, mas 15x15 e 25x25 mal da pra reconhecer os grão de café.
   
      • Gaussiano: Esse trás um efeito de desfoque assim como a media, mas sem alterar muito os contornos principais do desenho, mantendo bem seu formato mas 
       apenas desfocando a imagem, trazendo uma suavidade para as bordas, mesmo bem desfocada a imagem percebe melhor os detalhes diferente da média.

   **b) Qual filtro foi mais eficaz para suavizar a imagem?**
    
    • Filtro Gaussiano
    
   **c) E qual foi mais eficaz para destacar as bordas?**
    
    • Filtro Sobel
    
   **d) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?**
    
    • Sobel: Para identificação de placa de transito por captura de imagem, ou reconhecimento facial.
    
    • Media: Melhorar a qualidade de uma imagem antes de aplicar algoritmos de detecção de bordas e suavizar texturas em imagens de vídeo ou fotos para
    melhorar a compressão de imagem.

    • Mediana: Limpeza de imagens médicas (como ultrassons), onde bordas e detalhes são cruciais e remoção de ruídos em câmeras de segurança em condições
    de iluminação ruins.

    • Gaussiano: Remoção de ruídos aleatórios comuns em fotografias digitais principalmente em condições de pouca luz e pré-processamento para detecção de
    bordas com operadores como Sobel ou Canny.

**4. Experimentar:**
    **1. Experimentar diferentes tamanhos de kernel nos filtros de média e mediana (por exemplo, (3, 3), (5, 5), etc.) e observar como isso afeta a suavização da imagem.**
    
    • Irei disponibilizar todos os códigos feito e os codigo filtro_media.py e filtro_mediana.py estão alterados em media02.py e mediana02.py
    como esperado a cada aumento da janela de pixels a imagem fica com efeito mais acentuado ficando menos visivel a imagem porém util quando usado
    com uma janela de pixels menor.
