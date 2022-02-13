from web3 import Web3
from brownie import BastianToken
from scripts.helpers import get_account
import time

INITIAL_SUPPLY = Web3.toWei(1000, "ether")


def test_deploy_token():
    account = get_account()
    BastianToken.deploy(INITIAL_SUPPLY, {"from": account})
    time.sleep(60)
    assert len(BastianToken) > 0
