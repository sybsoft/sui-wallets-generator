from openpyxl import Workbook
from loguru import logger
from constants import SUI_ED25519_SCHEMA, SUI_MNEMONIC_PASSWORD, SUI_PK_PREFIX, WALLETS_SHEET_EXPORT_PATH
from bip_utils import Bip39SeedGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip44Coins, Bip44
from bech32 import bech32_encode, convertbits


def export_json_to_xlsx(data, destination):
    try:
        logger.info(f"Exporting wallets to {WALLETS_SHEET_EXPORT_PATH}")

        workbook = Workbook()
        sheet = workbook.active

        headers = ["Address", "Private key", "Mnemonic"]
        sheet.append(headers)

        for key, value in data.items():
            sheet.append([key, str(value[0]), str(value[1])])

        workbook.save(destination)

    except Exception as e:
        logger.error(f"Error occured while exporting to Excel: {str(e)}")
        exit()

def get_address_pk_from_mnemonic(mnemonic: str, pk_with_prefix=True):
    mnemonic = mnemonic.strip()
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate(SUI_MNEMONIC_PASSWORD)
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SUI).DeriveDefaultPath()
    address = bip44_mst_ctx.PublicKey().ToAddress()
    pk = bip44_mst_ctx.PrivateKey().Raw().ToHex()

    if pk_with_prefix:
        pk_bytes_with_schema = bytes.fromhex(f'{SUI_ED25519_SCHEMA}{pk}')
        pk_bit_arr = convertbits(pk_bytes_with_schema, 8, 5)
        pk = bech32_encode(SUI_PK_PREFIX, pk_bit_arr)

    return address, pk

def generate_mnemonic():
    return str(Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)).strip()

def generate_wallets(count: int):
    wallets = {}

    for _ in range(count):
        mnc = generate_mnemonic()
        addr, pk = get_address_pk_from_mnemonic(mnemonic=mnc, pk_with_prefix=True)
        wallets[addr] = pk, mnc

    logger.info(f"Total generated wallets: {len(wallets.keys())}/{count}")
    export_json_to_xlsx(wallets, WALLETS_SHEET_EXPORT_PATH)
