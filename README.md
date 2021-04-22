# scikit-image-examples
Aprendizado e teste com a lib scikit-image python.

### 1 - Deconvolução de imagem
  Neste exemplo, deconvolvemos uma versão barulhenta de uma imagem usando Wiener e algoritmos de Wiener não supervisionados. Esses algoritmos são baseados em modelos lineares que não podem restaurar bordas nítidas tanto quanto métodos não lineares (como restauração de TV), mas são muito mais rápidos.
  ### 1.1 - Filtro Wiener
  - O filtro inverso é baseado no PSF (Point Spread Function), na regularização anterior (penalização de alta frequência) e na compensação entre os dados e a adequação anterior. O   parâmetro de regularização deve ser ajustado manualmente. 

  ### 1.2 - Wiener não supervisionado
  - Este algoritmo possui parâmetros de regularização autoajustados com base no aprendizado de dados. Isso não é comum e é baseado na seguinte publicação 1. O algoritmo é baseado em   um amostrador de Gibbs iterativo que extrai amostras alternativas da lei condicional posterior da imagem, a potência do ruído e a potência da frequência da imagem.

### 2 - Colorindo imagens em escala de cinza
Pode ser útil tingir artificialmente uma imagem com alguma cor, seja para destacar regiões específicas de uma imagem ou talvez apenas para animar uma imagem em tons de cinza. Este exemplo demonstra o tingimento da imagem dimensionando os valores RGB e ajustando as cores no espaço de cores HSV.

  - Em 2D, as imagens coloridas são frequentemente representadas em RGB - 3 camadas de matrizes 2D, onde as 3 camadas representam os canais (R) ed, (G) reen e (B) lue da imagem. A   maneira mais simples de obter uma imagem colorida é definir cada canal RGB para a imagem em tons de cinza dimensionada por um multiplicador diferente para cada canal. Por       exemplo, multiplicar os canais verde e azul por 0 deixa apenas o canal vermelho e produz uma imagem vermelha brilhante. Da mesma forma, zerar o canal azul deixa apenas os      canais   vermelho e verde, que se combinam para formar o amarelo. 

### 3 - Usando transformações polares e log-polares para registro
A correlação de fase (registration.phase_cross_correlation) é um método eficiente para determinar o deslocamento de translação entre pares de imagens semelhantes. No entanto, essa abordagem depende de uma quase ausência de diferenças de rotação / escala entre as imagens, que são típicas em exemplos do mundo real.

Para recuperar as diferenças de rotação e escala entre duas imagens, podemos tirar proveito de duas propriedades geométricas da transformada log-polar e da invariância de translação do domínio da frequência. Primeiro, a rotação no espaço cartesiano torna-se translação ao longo do eixo de coordenadas angulares (θθ) do espaço log-polar. Em segundo lugar, a escala no espaço cartesiano torna-se translação ao longo da coordenada radial (ρ = lnx2 + y2 −−−−−−− √ρ = ln⁡x2 + y2) do espaço log-polar. Finalmente, as diferenças na tradução no domínio espacial não impactam o espectro de magnitude no domínio da frequência.

Nesta série de exemplos, construímos esses conceitos para mostrar como a transformada log-polar transform.warp_polar pode ser usada em conjunto com a correlação de fase para recuperar as diferenças de rotação e escala entre duas imagens que também têm um deslocamento de translação.

- Recupere a diferença de rotação com uma transformação polar
  - Neste exemplo, consideramos o caso simples de duas imagens que diferem apenas no que diz respeito à rotação em torno de um ponto central comum. Ao remapear essas imagens no espaço polar, a diferença de rotação se torna uma diferença de translação simples que pode ser recuperada por correlação de fase.
