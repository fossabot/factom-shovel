factomd: ./factomd --network=LOCAL --enablelivefeedapi --eventformat=json
shovel: python ./shovel/listener.py
wallet: ./factom-walletd
generator: watch -n 1 python test_write.py
