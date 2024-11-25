import logging
import os
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """
    Configura um logger com handlers para arquivo e console

    Args:
        name: Nome do logger

    Returns:
        Logger configurado
    """
    # Criar pasta de logs se não existir
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Nome do arquivo de log com data
    log_file = f'logs/territorio_{datetime.now().strftime("%Y%m%d")}.log'

    # Criar logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Verificar se o logger já tem handlers para evitar duplicação
    if not logger.handlers:
        # Handler para arquivo
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatação detalhada para arquivo
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # Formatação simplificada para console
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)

        # Adicionar handlers ao logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger