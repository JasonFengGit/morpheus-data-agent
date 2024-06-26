import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Configuration object
class Config:
    # Model configuration
    MODEL_NAME = "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF"
    MODEL_REVISION = "openhermes-2.5-mistral-7b.Q4_K_M.gguf"
    MODEL_PATH = "model/"+MODEL_REVISION
    DOWNLOAD_DIR = "model"
    # API endpoints
    COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
    DEFILLAMA_BASE_URL = "https://api.llama.fi"
    BLOCKCHAIN_API_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

    # User-facing strings
    PRICE_SUCCESS_MESSAGE = "The price of {coin_name} is ${price:,}"
    PRICE_FAILURE_MESSAGE = "Failed to retrieve price. Please enter a valid coin name."
    FLOOR_PRICE_SUCCESS_MESSAGE = "The floor price of {nft_name} is ${floor_price:,}"
    FLOOR_PRICE_FAILURE_MESSAGE = "Failed to retrieve floor price. Please enter a valid NFT name."
    TVL_SUCCESS_MESSAGE = "The TVL of {protocol_name} is ${tvl:,}"
    TVL_FAILURE_MESSAGE = "Failed to retrieve TVL. Please enter a valid protocol name."
    FDV_SUCCESS_MESSAGE = "The fully diluted valuation of {coin_name} is ${fdv:,}"
    FDV_FAILURE_MESSAGE = "Failed to retrieve FDV. Please enter a valid coin name."
    MARKET_CAP_SUCCESS_MESSAGE = "The market cap of {coin_name} is ${market_cap:,}"
    MARKET_CAP_FAILURE_MESSAGE = "Failed to retrieve market cap. Please enter a valid coin name."
    API_ERROR_MESSAGE = "I can't seem to access the API at the moment."
    
