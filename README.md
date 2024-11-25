# territorio-ubs
🔧 Requisitos
Para executar o projeto, você precisará das seguintes dependências:

Python 3.8 ou superior
Pandas
Plotly
Dataclasses
Todas as dependências estão listadas no arquivo requirements.txt.

## 🛠️ Instalação
1. Clone o repositório:

```python
git clone https://github.com/seu-usuario/territorio_ubs.git
cd territorio_ubs
```

2. Crie um ambiente virtual:

```python
python -m venv venv
```

3. Ative o ambiente virtual:

No Windows:

```python
.\venv\Scripts\activate
```

No macOS/Linux:

```python
source venv/bin/activate
```

4. Instale as dependências:

```python
pip install -r requirements.txt
```


## 📂 Estrutura do Projeto

```markdown
territorio-ubs/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── publish.yml
│
├── src/
│   └── territorio_ubs/
│       ├── __init__.py
│       ├── biblioteca_ubs.py
│       └── config_logging.py
│
├── tests/
│   ├── __init__.py
│   └── test_biblioteca_ubs.py
│
├── docs/
│   ├── index.md
│   └── api.md
│
├── pyproject.toml
├── setup.cfg
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 Uso

### Inicialização Básica

#### Carregamento de Dados

Para inicializar o gerenciador de território, você precisará de um DataFrame do Pandas
contendo os dados do território. O DataFrame deve conter as colunas RUA, NUM, IDD e SEXO.

```python
import pandas as pd
from src.biblioteca_ubs import GerenciadorTerritorio

# Carregar dados
df = pd.read_csv('dados_territorio.csv')

# Inicializar gerenciador
gerenciador = GerenciadorTerritorio(df)
```

#### Configuração do Gerenciador

O gerenciador de território é configurado automaticamente ao ser inicializado. Ele verifica
a integridade dos dados e configura os logs.

#### Processamento de Dados
- O método processar_ruas processa todas as ruas e suas contagens, incluindo a Av. Marte.

```python
gerenciador.processar_ruas()
```

#### Análise Demográfica
- O método calcular_media_idade_por_rua_sexo calcula a média de idade por rua e sexo.

```python   
gerenciador.calcular_media_idade_por_rua_sexo()
```

#### Faixas Etárias
- O método categorizar_faixas_etarias categoriza os usuários em faixas etárias.

```python
gerenciador.categorizar_faixas_etarias()
```

#### Visualizações

##### Gráficos por ACS
- O método plot_usuarios_por_acs gera um gráfico de pizza para a distribuição de usuários por ACS.

```python   
fig = gerenciador.plot_usuarios_por_acs()
fig.show()
```

##### Distribuição Territorial
- O método plot_ruas_por_acs gera um gráfico de barras para a distribuição de usuários por ACS e rua.

```python   
fig = gerenciador.plot_ruas_por_acs()
fig.show()
```

##### Análises Etárias
- O método plot_scatter_mulheres gera um gráfico de dispersão para faixas etárias de mulheres
em uma rua específica.

```python   
fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
fig.show()
```

### Exemplos de Uso

#### Exemplo 1: Processamento Completo

```python
import pandas as pd
from src.biblioteca_ubs import GerenciadorTerritorio

# Carregar dados
df = pd.read_csv('dados_territorio.csv')

# Inicializar gerenciador
gerenciador = GerenciadorTerritorio(df)

# Processar ruas
gerenciador.processar_ruas()

# Calcular média de idade por rua e sexo
gerenciador.calcular_media_idade_por_rua_sexo()

# Categorizar faixas etárias
gerenciador.categorizar_faixas_etarias()

# Gerar gráfico de usuários por ACS
fig = gerenciador.plot_usuarios_por_acs()
fig.show()

# Gerar gráfico de distribuição de usuários por ACS e rua
fig = gerenciador.plot_ruas_por_acs()
fig.show()

# Gerar gráfico de dispersão para faixas etárias de mulheres em uma rua específica
fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
fig.show()
```

#### Exemplo 2: Análise Específica de uma Rua

```python
import pandas as pd
from src.biblioteca_ubs import GerenciadorTerritorio

# Carregar dados
df = pd.read_csv('dados_territorio.csv')

# Inicializar gerenciador
gerenciador = GerenciadorTerritorio(df)

# Processar ruas
gerenciador.processar_ruas()

# Gerar gráfico de dispersão para faixas etárias de mulheres em uma rua específica
fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
fig.show()

# Gerar gráfico de barras para crianças e idosos em uma rua específica
fig = gerenciador.plot_scatter_criancas_idosos('RUA MONSENHOR MESSIAS')
fig.show()
```

#### Exemplo 3: Salvamento de Dados Combinados

```python
import pandas as pd
from src.biblioteca_ubs import GerenciadorTerritorio

# Carregar dados
df = pd.read_csv('dados_territorio.csv')

# Inicializar gerenciador
gerenciador = GerenciadorTerritorio(df)

# Processar ruas
gerenciador.processar_ruas()

# Categorizar faixas etárias
gerenciador.categorizar_faixas_etarias()

# Salvar dados combinados em um arquivo CSV
gerenciador.salvar_dados_combinados('dados_combinados.csv')
```

#### Funcionalidades Adicionais

##### Contagem de Usuários por ACS
- O método contar_usuarios_por_acs conta os usuários por ACS e rua.

```python
resultados = gerenciador.contar_usuarios_por_acs()
print(resultados)
```

##### Contagem de Usuários da Av. Marte
- O método contar_usuarios_marte conta os usuários da Av. Marte por ACS.

```python
resultados = gerenciador.contar_usuarios_marte()
print(resultados)
```

##### Criação de DataFrames por ACS
- O método criar_df_por_acs cria DataFrames separados para cada ACS.

```python
# Criar DataFrame para um ACS específico
df_acs = gerenciador.criar_df_por_acs('Elisangela')
print(df_acs)

# Criar DataFrames para todos os ACS
dfs_acs = gerenciador.criar_df_por_acs()
for acs, df in dfs_acs.items():
    print(f"DataFrame para {acs}:")
    print(df)
```

##### Gráfico de Treemap de Usuários
- O método plot_treemap_usuarios gera um gráfico de treemap para a distribuição hierárquica de usuários.

```python
fig = gerenciador.plot_treemap_usuarios()
fig.show()
```

##### Gráfico de Ruas de um ACS Específico
- O método plot_ruas_do_acs gera um gráfico de barras para as ruas de um ACS específico.

```python
fig = gerenciador.plot_ruas_do_acs('Elisangela')
fig.show()
```

# OBS:
    ## Casos de uso para outras UBS:
        ### 🚀 Inicialização Básica

                #### Carregamento de Dados
                
                - Para inicializar o gerenciador de território, você precisará de um DataFrame do Pandas
                contendo os dados do território.
                - O DataFrame deve conter as colunas `RUA`, `NUM`, `IDD` e `SEXO`.

                ```python
                import pandas as pd
                from src.gerenciador_territorio_ubs import GerenciadorTerritorioUBS

                # Carregar dados
                df = pd.read_csv('dados_territorio.csv')

                # Inicializar gerenciador
                gerenciador = GerenciadorTerritorioUBS(df)
                ```
                ### Configuração Interativa de Equipes, Microáreas e Ruas

                A funcionalidade de configuração interativa permite que qualquer UBS personalize o gerenciador de território de acordo com suas próprias equipes, microáreas e ruas. Isso torna a biblioteca extremamente flexível e adaptável às necessidades específicas de cada UBS.

                ### Método configurar_acs_streets
                - O método configurar_acs_streets permite que o usuário configure interativamente os dicionários de ruas por ACS. Durante a inicialização, o usuário será solicitado a fornecer informações sobre o número de equipes, o nome de cada equipe, o número de microáreas em cada equipe e os nomes das ruas em cada microárea.

                ```python
                def configurar_acs_streets(self) -> RuaDict:
                    """
                    Configura os dicionários de ruas por ACS de forma interativa.

                    Returns:
                        RuaDict: Dicionário de ruas por ACS configurado.
                    """
                    acs_streets = {}
                    num_equipes = int(input("Quantas equipes existem? "))

                    for i in range(num_equipes):
                        equipe = input(f"Nome da equipe {i + 1}: ")
                        num_microareas = int(input(f"Quantas microáreas existem na equipe {equipe}? "))
                        ruas = []

                        for j in range(num_microareas):
                            rua = input(f"Nome da rua {j + 1} na microárea {j + 1} da equipe {equipe}: ")
                            ruas.append(rua)

                        acs_streets[equipe] = ruas

                    return acs_streets
                ```

                ### Método atualizar_acs_streets
                - O método atualizar_acs_streets permite atualizar o dicionário de ruas por ACS com um novo dicionário fornecido pelo usuário.
                - Isso é útil para atualizar a configuração sem a necessidade de reinicializar o gerenciador.

                ```python
                def atualizar_acs_streets(self, acs_streets: Dict[str, List[str]]) -> None:
                    """
                    Atualiza o dicionário de ruas por ACS.

                    Args:
                        acs_streets: Novo dicionário de ruas por ACS.
                    """
                    self.logger.info("Atualizando dicionário de ruas por ACS")
                    self.acs_streets = acs_streets
                    self.logger.info(f"Dicionário de ruas por ACS atualizado com {len(self.acs_streets)} ACS")
                ```

                ### Exemplo de Uso

                - UBS Teste tem 3 equipes: Branca, Azul e Verde. 
                - Cada equipe tem 4 microáreas e cada microárea tem 6 ruas de abrangência. .
                
                - Para usar a biblioteca, você terá que configurar as equipes, microáreas e ruas inicialmente. 
                
                **Proceda da seguinte maneira:**

                ```python
                import pandas as pd
                from src.gerenciador_territorio_ubs import GerenciadorTerritorioUBS

                # Carregar dados
                df = pd.read_csv('dados_territorio.csv')

                # Inicializar gerenciador
                gerenciador = GerenciadorTerritorioUBS(df)

                # Configurar equipes, microáreas e ruas interativamente
                gerenciador.configurar_acs_streets()

                # Processar ruas
                gerenciador.processar_ruas()

                # Calcular média de idade por rua e sexo
                gerenciador.calcular_media_idade_por_rua_sexo()

                # Categorizar faixas etárias
                gerenciador.categorizar_faixas_etarias()

                # Gerar gráfico de usuários por ACS
                fig = gerenciador.plot_usuarios_por_acs()
                fig.show()

                # Gerar gráfico de distribuição de usuários por ACS e rua
                fig = gerenciador.plot_ruas_por_acs()
                fig.show()

                # Gerar gráfico de dispersão para faixas etárias de mulheres em uma rua específica
                fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
                fig.show()
                ```
                
                ### Considerações
                - O GerenciadorTerritorioUBS é uma ferramenta poderosa para análise e visualização de dados demográficos em territórios de UBS. Ele oferece uma ampla gama de funcionalidades para processamento de dados, análise demográfica e visualização de resultados. Com uma configuração simples e métodos intuitivos, ele permite que você obtenha insights valiosos sobre a distribuição de usuários em diferentes regiões e ACS.
                
                #### Configuração do Gerenciador
                - O gerenciador de território é configurado automaticamente ao ser inicializado. Ele verifica
                a integridade dos dados e configura os logs. Além disso, ele pergunta ao usuário sobre as equipes, microáreas e ruas durante a inicialização.

                #### Atualização de Dicionários
                - Você pode atualizar o dicionário de ruas por ACS usando o método atualizar_acs_streets.

                ```python
                novo_acs_streets = {
                    "Novo ACS 1": ["RUA A", "RUA B"],
                    "Novo ACS 2": ["RUA C", "RUA D"]
                }
                gerenciador.atualizar_acs_streets(novo_acs_streets)
                ```

                #### Processamento de Dados
                ##### Processamento de Ruas
                - O método processar_ruas processa todas as ruas e suas contagens.

                ```python
                gerenciador.processar_ruas()
                ```

                ##### Análise Demográfica
                - O método calcular_media_idade_por_rua_sexo calcula a média de idade por rua e sexo.

                ```python
                gerenciador.calcular_media_idade_por_rua_sexo()
                ```

                ##### Faixas Etárias
                - O método categorizar_faixas_etarias categoriza os usuários em faixas etárias.

                ```python
                gerenciador.categorizar_faixas_etarias()
                ```

                ##### Visualizações
                ##### Gráficos por ACS
                - O método plot_usuarios_por_acs gera um gráfico de pizza para a distribuição de usuários por ACS.

                ```python
                fig = gerenciador.plot_usuarios_por_acs()
                fig.show()
                ```

                ##### Distribuição Territorial
                - O método plot_ruas_por_acs gera um gráfico de barras para a distribuição de usuários por ACS e rua.

                ```python
                fig = gerenciador.plot_ruas_por_acs()
                fig.show()
                ```

                ##### Análises Etárias
                - O método plot_scatter_mulheres gera um gráfico de dispersão para faixas etárias de mulheres em uma
                rua específica.

                ```python
                fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
                fig.show()
                ```

                ### Exemplos de Uso
                #### Exemplo 1: Processamento Completo

                ```python
                import pandas as pd
                from src.gerenciador_territorio_ubs import GerenciadorTerritorioUBS

                # Carregar dados
                df = pd.read_csv('dados_territorio.csv')

                # Inicializar gerenciador
                gerenciador = GerenciadorTerritorioUBS(df)

                # Processar ruas
                gerenciador.processar_ruas()

                # Calcular média de idade por rua e sexo
                gerenciador.calcular_media_idade_por_rua_sexo()

                # Categorizar faixas etárias
                gerenciador.categorizar_faixas_etarias()

                # Gerar gráfico de usuários por ACS
                fig = gerenciador.plot_usuarios_por_acs()
                fig.show()

                # Gerar gráfico de distribuição de usuários por ACS e rua
                fig = gerenciador.plot_ruas_por_acs()
                fig.show()

                # Gerar gráfico de dispersão para faixas etárias de mulheres em uma rua específica
                fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
                fig.show()
                ```

                #### Exemplo 2: Análise Específica de uma Rua

                ```python
                import pandas as pd
                from src.gerenciador_territorio_ubs import GerenciadorTerritorioUBS

                # Carregar dados
                df = pd.read_csv('dados_territorio.csv')

                # Inicializar gerenciador
                gerenciador = GerenciadorTerritorioUBS(df)

                # Processar ruas
                gerenciador.processar_ruas()

                # Gerar gráfico de dispersão para faixas etárias de mulheres em uma rua específica
                fig = gerenciador.plot_scatter_mulheres('RUA MONSENHOR MESSIAS')
                fig.show()

                # Gerar gráfico de barras para crianças e idosos em uma rua específica
                fig = gerenciador.plot_scatter_criancas_idosos('RUA MONSENHOR MESSIAS')
                fig.show()
                ```	

                #### Exemplo 3: Salvamento de Dados Combinados

                ```python
                import pandas as pd
                from src.gerenciador_territorio_ubs import GerenciadorTerritorioUBS

                # Carregar dados
                df = pd.read_csv('dados_territorio.csv')

                # Inicializar gerenciador
                gerenciador = GerenciadorTerritorioUBS(df)

                # Processar ruas
                gerenciador.processar_ruas()

                # Categorizar faixas etárias
                gerenciador.categorizar_faixas_etarias()

                # Salvar dados combinados em um arquivo CSV
                gerenciador.salvar_dados_combinados('dados_combinados.csv')
                ```
                ##### Contagem de Usuários por ACS
                - O método contar_usuarios_por_acs conta os usuários por ACS e rua.

                ```python
                resultados = gerenciador.contar_usuarios_por_acs()
                print(resultados)
                ```

                ##### Criação de DataFrames por ACS
                - O método criar_df_por_acs cria DataFrames separados para cada ACS.

                ```python
                # Criar DataFrame para um ACS específico
                df_acs = gerenciador.criar_df_por_acs('Elisangela')
                print(df_acs)

                # Criar DataFrames para todos os ACS
                dfs_acs = gerenciador.criar_df_por_acs()
                for acs, df in dfs_acs.items():
                    print(f"DataFrame para {acs}:")
                    print(df)   
                ```

                ##### Gráfico de Treemap de Usuários
                - O método plot_treemap_usuarios gera um gráfico de treemap para a distribuição hierárquica de usuários.

                ```python
                fig = gerenciador.plot_treemap_usuarios()
                fig.show()
                ```

                ##### Gráfico de Ruas de um ACS Específico
                - O método plot_ruas_do_acs gera um gráfico de barras para as ruas de um ACS específico.

                ```python
                fig = gerenciador.plot_ruas_do_acs('Elisangela')
                fig.show()
                ```

Considerações Finais

## 📜 Estrutura do Código


### Classes Principais
- **GerenciadorTerritorio**
    - Classe principal que gerencia o território e processa os dados demográficos.

- **CensoDemografico**
    - Classe utilitária para cálculos demográficos, como porcentagens de etnias.

### Funcionalidades Detalhadas

#### Gerenciamento de Território
    - **Inicialização**: Verifica a integridade dos dados e configura os logs.
    - **Processamento de Ruas**: Processa todas as ruas e suas contagens.
    - **Análise Demográfica**: Calcula médias de idade e categoriza faixas etárias.
    - **Cálculo de Médias**: Média de idade por rua e sexo.
    - **Categorização de Faixas Etárias**: Categoriza usuários em faixas etárias pré-definidas.

#### Processamento da Av. Marte
    - **Contagem de Usuários**: Conta usuários da Av. Marte por ACS.
    - **Verificação de Números**: Verifica números não encontrados na Av. Marte.

### Sistema de Logs

#### Configuração de Logs
- Configuração detalhada de logs para monitoramento e depuração.

#### Logs Detalhados
- Logs detalhados para cada etapa do processamento.

### 🧪 Testes
- Os testes unitários estão localizados no diretório tests e podem ser executados usando o pytest.

```
pytest
```

### 📜 Logs
- Os logs são gerados automaticamente e armazenados no diretório logs. Eles fornecem informações
detalhadas sobre o processamento e quaisquer erros que ocorram.

### 📞 Contato

- Para mais informações, entre em contato com tell.medicina@gmail.com.
