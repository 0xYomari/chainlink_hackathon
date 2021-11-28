from scripts.helpful_scripts import get_account
from brownie import NFT

token_uri = "https://ipfs.io/ipfs/QmdmmKZ4hA9ZViEBLK1TkyCpUBewriGKSoQ561hgR9NQNM?filename=nftsample.png"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    nft = NFT.deploy({"from": account})
    tx = nft.createAbstract(token_uri, {"from": account})
    tx.wait(1)
    print(
        f"YOu can view your NFT at {OPENSEA_URL.format(nft.address, nft.tokenCounter()-1)}"
    )


def main():
    deploy_and_create()
