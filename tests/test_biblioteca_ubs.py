import unittest
import pandas as pd
from typing import List
from src.biblioteca_ubs import GerenciadorTerritorio


class TestGerenciadorTerritorio(unittest.TestCase):
    def setUp(self):
        """
        Configura os dados de teste antes de cada método
        """
        # Criar DataFrame de teste
        self.df_teste = pd.DataFrame(
            {
                "RUA": [
                    "AV MARTE",
                    "RUA MONSENHOR MESSIAS",
                    "AV MARTE",
                    "RUA DOS BELGAS",
                ],
                "NUM": ["545", "123", "565", "456"],
                "IDD": [30, 45, 25, 60],
                "SEXO": ["F", "M", "F", "M"],
            }
        )

        # Inicializar gerenciador
        self.gerenciador = GerenciadorTerritorio(self.df_teste)

    def test_inicializacao(self):
        """Testa a inicialização da classe"""
        # Testa se o DataFrame foi inicializado corretamente
        self.assertIsInstance(self.gerenciador.df, pd.DataFrame)
        self.assertFalse(self.gerenciador.df.empty)

        # Testa se as colunas obrigatórias existem
        colunas_obrigatorias = ["RUA", "NUM", "IDD", "SEXO"]
        for coluna in colunas_obrigatorias:
            self.assertIn(coluna, self.gerenciador.df.columns)

    def test_inicializacao_invalida(self):
        """Testa casos inválidos de inicialização"""
        # Testa DataFrame vazio
        with self.assertRaises(ValueError):
            GerenciadorTerritorio(pd.DataFrame())

        # Testa tipo inválido (lista ao invés de DataFrame)
        dados_invalidos: List[int] = [1, 2, 3]
        with self.assertRaises(TypeError):
            GerenciadorTerritorio(dados_invalidos)  # type: ignore

    def test_processar_ruas(self):
        """
        Testa o processamento de ruas e Av. Marte
        """
        self.gerenciador.processar_ruas()

        # Verifica se df_ruas foi criado
        assert isinstance(self.gerenciador.df_ruas, pd.DataFrame)

        # Verifica se contém as colunas esperadas
        assert "CONTAGEM" in self.gerenciador.df_ruas.columns

        # Verifica se as contagens estão corretas para ruas gerais
        df_ruas: pd.DataFrame = self.gerenciador.df_ruas
        contagem_marte = len(self.df_teste[self.df_teste["RUA"] == "AV MARTE"])
        self.assertEqual(
            df_ruas[df_ruas["RUA"] == "AV MARTE"]["CONTAGEM"].iloc[0], contagem_marte
        )

        # Verifica processamento específico da Av. Marte
        assert isinstance(self.gerenciador.df_marte, pd.DataFrame)
        df_marte: pd.DataFrame = self.gerenciador.df_marte
        numeros_marte = df_marte["NUM"].astype(str).tolist()
        self.assertIn("545", numeros_marte)
        self.assertIn("565", numeros_marte)

    def test_calcular_media_idade(self):
        """Testa o cálculo de média de idade por rua e sexo"""
        self.gerenciador.calcular_media_idade_por_rua_sexo()

        # Verifica se o DataFrame foi criado
        assert isinstance(self.gerenciador.faixa_etaria_por_rua_sexo, pd.DataFrame)

        # Verifica cálculo para um caso específico
        df_faixa_etaria: pd.DataFrame = self.gerenciador.faixa_etaria_por_rua_sexo
        media_marte_f = self.df_teste[
            (self.df_teste["RUA"] == "AV MARTE") & (self.df_teste["SEXO"] == "F")
        ]["IDD"].mean()

        resultado = df_faixa_etaria[
            (df_faixa_etaria["RUA"] == "AV MARTE") & (df_faixa_etaria["SEXO"] == "F")
        ]["MEDIA_IDADE"].iloc[0]

        self.assertAlmostEqual(resultado, media_marte_f)

    def test_categorizar_faixas_etarias(self):
        """Testa a categorização de faixas etárias"""
        self.gerenciador.categorizar_faixas_etarias()

        # Verifica se a coluna foi criada
        self.assertIn("Faixa Etária", self.gerenciador.df.columns)

        # Testa categorização específica
        pessoa_60_anos = self.gerenciador.df[self.gerenciador.df["IDD"] == 60]
        self.assertEqual(
            pessoa_60_anos["Faixa Etária"].iloc[0], "60 anos ou mais (Idosos)"
        )

    def test_visualizacoes(self):
        """
        Testa a geração de gráficos
        """
        # Prepara dados
        self.gerenciador.processar_ruas()  # Agora processa tudo
        self.gerenciador.categorizar_faixas_etarias()

        # Testa diferentes visualizações
        fig_acs = self.gerenciador.plot_usuarios_por_acs()
        self.assertIsNotNone(fig_acs)

        fig_ruas = self.gerenciador.plot_ruas_por_acs()
        self.assertIsNotNone(fig_ruas)

        fig_marte = self.gerenciador.plot_scatter_mulheres("AV MARTE")
        self.assertIsNotNone(fig_marte)


if __name__ == "__main__":
    unittest.main(verbosity=2)
# Para rodar os testes:
# python -m unittest test_biblioteca_ubs.py -v