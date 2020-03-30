# Factom-Shovel

Build bridges between distributed event streams with Factom Live Feed Api.
Work sponsored by a grant from the Factom Protocol:

https://factomize.com/forums/threads/matt-york-1-ipfs-bridge.3419/

## Status

Planning & Prototyping.

**under construction**

This repository is a scaffold for testing and replaying events from a local factom network.

TODO: extend to target a private IPFS network

## Motivation

Many current mechanisms to store data for DAPPs make use of IPFS.

Factom is an ideal platform to store and serve 'pinned' data.

Paying for entry storage on the Factom Protocol is price-fixed at $0.001 per-kb.

Using this basic mechanism to provide permanance and anchoring to IPFS based services
extends the reach and utility of the Factom Protocol.

## Development


Enable Experimental Filestore

```
ipfs config --json Experimental.FilestoreEnabled true
```

Start an IPFS node

```
ipfs daemon
```

For integration testing it is convenient not to use docker containers.

The provided `Procfile` starts a local network.

```
factomd: ./factomd --network=LOCAL --enablelivefeedapi --eventformat=json
shovel: python ./shovel/listener.py
wallet: ./factom-walletd
generator: watch -n 1 python test_write.py
```

Honcho is a python package that makes use of Procfile format
It shows joined logs from all services with color-coded output.

```
honcho start
```

### Notes

* Investigate possible filesystem level integration
  * https://github.com/hanwen/go-fuse
  * https://docs.ipfs.io/reference/api/cli/#ipfs-add

* What are other good targets to shovel data?
  * rabbitMQ, kafka
  * added logstash - this may be the best avenue to tap into existing tools
