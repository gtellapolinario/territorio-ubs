import sqlite3
import pandas as pd
import logging

class ConsultasTerritorio:
    def __init__(self, db_path: str):
        """
        Inicializa a classe de consultas com o caminho para o banco de dados SQLite.

        Args:
            db_path (str): Caminho para o arquivo do banco de dados SQLite.
        """
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Inicializando ConsultasTerritorio com banco em {db_path}")

    def conectar(self):
        """
        Estabelece uma conexão com o banco de dados.

        Returns:
            sqlite3.Connection: Objeto de conexão com o banco.
        """
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            self.logger.error(f"Erro ao conectar ao banco: {str(e)}")
            raise

    def consultar_usuarios_por_rua(self) -> pd.DataFrame:
        """
        Retorna o total de usuários por rua.

        Returns:
            pd.DataFrame: DataFrame com ruas e total de usuários.
        """
        query = """
        SELECT RUA, COUNT(*) AS TOTAL_USUARIOS
        FROM territorio
        GROUP BY RUA
        ORDER BY TOTAL_USUARIOS DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_preventivo_por_rua(self) -> pd.DataFrame:
        """
        Retorna o número de mulheres na faixa de preventivo e mamografia por rua.

        Returns:
            pd.DataFrame: DataFrame com ruas e total de mulheres na faixa de preventivo e mamografia.
        """
        query = """
        SELECT RUA, SUM(PREVENTIVO) AS TOTAL_PREVENTIVO, SUM(MAMOGRAFIA) AS TOTAL_MAMOGRAFIA
        FROM territorio
        GROUP BY RUA
        ORDER BY TOTAL_PREVENTIVO DESC, TOTAL_MAMOGRAFIA DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_usuarios_por_micro(self) -> pd.DataFrame:
        """
        Retorna o total de usuários por microárea e a divisão entre ruas.

        Returns:
            pd.DataFrame: DataFrame com microáreas, ruas e total de usuários.
        """
        query = """
        SELECT MICRO, RUA, COUNT(*) AS TOTAL_USUARIOS
        FROM territorio
        GROUP BY MICRO, RUA
        ORDER BY MICRO, TOTAL_USUARIOS DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_comparativo_equipes(self) -> pd.DataFrame:
        """
        Retorna o comparativo de equipes com o total de usuários e métricas.

        Returns:
            pd.DataFrame: DataFrame com equipes e comparativo de métricas.
        """
        query = """
        SELECT EQUIPE, SUM(CONTAGEM) AS TOTAL_USUARIOS, 
               SUM(PREVENTIVO) AS TOTAL_PREVENTIVO, SUM(MAMOGRAFIA) AS TOTAL_MAMOGRAFIA
        FROM territorio
        GROUP BY EQUIPE
        ORDER BY TOTAL_USUARIOS DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_criancas_por_micro(self) -> pd.DataFrame:
        """
        Retorna o número de crianças (0-4 anos) por microárea e equipe.

        Returns:
            pd.DataFrame: DataFrame com microáreas, equipes e total de crianças.
        """
        query = """
        SELECT MICRO, EQUIPE, SUM(DOIS_M + DOIS_F) AS TOTAL_CRIANCAS
        FROM territorio
        GROUP BY MICRO, EQUIPE
        ORDER BY TOTAL_CRIANCAS DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_idosos_por_micro(self) -> pd.DataFrame:
        """
        Retorna o número de idosos (60+) por microárea e equipe.

        Returns:
            pd.DataFrame: DataFrame com microáreas, equipes e total de idosos.
        """
        query = """
        SELECT MICRO, EQUIPE, SUM(IDOSOS_M + IDOSOS_F) AS TOTAL_IDOSOS
        FROM territorio
        GROUP BY MICRO, EQUIPE
        ORDER BY TOTAL_IDOSOS DESC;
        """
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)

    def consultar_dados_completos(self) -> pd.DataFrame:
        """
        Retorna todos os dados completos da tabela.

        Returns:
            pd.DataFrame: DataFrame com todos os registros da tabela.
        """
        query = "SELECT * FROM territorio;"
        with self.conectar() as conn:
            return pd.read_sql_query(query, conn)
