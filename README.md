# Factom-Shovel

Build bridges between distributed event streams with Factom Live Feed Api.
Work sponsored by a grant from the Factom Protocol:

https://factomize.com/forums/threads/matt-york-1-ipfs-bridge.3419/

## Status

Planning & Protyping.

**under construction**

This repository is a scaffold for testing and replaying events from a local factom network.

TODO: extend to target a private IPFS network

## Motivation

Many current mechanisms to store data for DAPPs make use of IPFS.

Factom is an ideal platform to store and serve 'pinned' data.

Paying for entry storage on the Factom Protocol is a price-fixed at $0.001 per-kb.

Using this basic mechanism to provide permanance and anchoring to IPFS based services
extends the reach and utility of the Factom Protocol.


### Notes

* Investigate possible filesystem level integration
  * https://github.com/hanwen/go-fuse
  * https://docs.ipfs.io/reference/api/cli/#ipfs-add
