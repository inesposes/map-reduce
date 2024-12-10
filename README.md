# MapReduce Tarefa

Este repositorio contén o desenvolvemento dunha serie de exercicios relacionados co uso de MapReduce para procesar datos. A continuación descríbese a estrutura do proxecto e as instruccións básicas.

## Estrutura do Proxecto

- **`0_codigo_orixinal/`**: 
  - Contén os códigos orixinais proporcionados como punto de partida.
  - Inclúe unha mostra reducida do dataset orixinal (purchases.txt) para realizar probas.

- **Exercicios**: Cada exercicio está contido na súa propia carpeta, coa seguinte estrutura:
  - `mapper.py`: Script do mapper.
  - `reducer.py`: Script do reducer.
  - `resultado.txt`: Arquivo cos resultados xerados tras a execución.

## Exercicios

1. **Exercicio 1.1**: Modificar o mapper para descartar liñas cun formato incorrecto.
2. **Exercicio 1.2**: Calcular o total de vendas por categoría.
3. **Exercicio 1.3**: Atopar a venda máis alta por tipo de pago.
4. **Exercicio 1.4**: Obter o máximo absoluto de todas as vendas.
5. **Exercicio 1.5**: Calcular o total de vendas.

Para cada exercicio executar o seguinte comando:
```
mapred streaming -files mapper.py,reducer.py -input purchases.txt -output exercicio -mapper mapper.py -reducer reducer.py
```


