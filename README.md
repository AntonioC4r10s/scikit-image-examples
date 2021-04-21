# scikit-image-examples
Aprendizado e teste com a lib scikit-image python.

### 1 - Deconvolução de imagem
  Neste exemplo, deconvolvemos uma versão barulhenta de uma imagem usando Wiener e algoritmos de Wiener não supervisionados. Esses algoritmos são baseados em modelos lineares que não podem restaurar bordas nítidas tanto quanto métodos não lineares (como restauração de TV), mas são muito mais rápidos.
    ### 1.1 - Filtro Wiener
  - [O filtro inverso é baseado no PSF (Point Spread Function), na regularização anterior (penalização de alta frequência) e na compensação entre os dados e a adequação anterior. O   parâmetro de regularização deve ser ajustado manualmente.] 

  ### 1.2 - Wiener não supervisionado
  - [Este algoritmo possui parâmetros de regularização autoajustados com base no aprendizado de dados. Isso não é comum e é baseado na seguinte publicação 1. O algoritmo é baseado em   um amostrador de Gibbs iterativo que extrai amostras alternativas da lei condicional posterior da imagem, a potência do ruído e a potência da frequência da imagem.
]
