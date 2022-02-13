from brownie import BastianToken
from scripts.helpers import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000, "ether")


def deploy():
    token = BastianToken.deploy(INITIAL_SUPPLY, {"from": get_account()})
    print("OurToken has been deployed")
    print(token._name)
    return token


def main():
    deploy()
