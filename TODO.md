WIP
---

Tweak FUSE usage to make sure mount/unmount works consistently.

BACKLOG
-------
- [ ] update this python-shovel lib to trigger replay via live feed to rebuild IPFS mirror.

- [ ] add a subscriber thread on the Factomd side to push IPFS data when following by minutes.

ICEBOX
------
- [ ] use shovel trigger to push data to ipfs https://github.com/ipfs/go-ipfs/blob/master/docs/add-code-flow.md
- [ ] related open issue: for `ipfs add --nocopy` https://github.com/ipfs/go-ipfs/issues/5986

- [ ] adapt shovel to output a json doc suitable for IPFS
      using FUSE integration instead

DONE
----
- [x] pipe live feed to ELK stack

