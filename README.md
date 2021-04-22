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

Em 2D, as imagens coloridas são frequentemente representadas em RGB - 3 camadas de matrizes 2D, onde as 3 camadas representam os canais (R) ed, (G) reen e (B) lue da imagem. A maneira mais simples de obter uma imagem colorida é definir cada canal RGB para a imagem em tons de cinza dimensionada por um multiplicador diferente para cada canal. Por exemplo, multiplicar os canais verde e azul por 0 deixa apenas o canal vermelho e produz uma imagem vermelha brilhante. Da mesma forma, zerar o canal azul deixa apenas os canais vermelho e verde, que se combinam para formar o amarelo. 
