def validate(params):
    params = params['data']
    raw_entry = params.get('entry')
    raw_entry = bytes.fromhex(raw_entry)

    # Check entry hash https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md
    # Entry Hash = SHA256( SHA512(marshalled entry) + marshalled entry )
    entry_hash_expected = params.get('entry_hash')
    h = sha512(raw_entry).digest()
    entry_hash_observed = sha256(h + raw_entry).hexdigest()
    if entry_hash_expected != entry_hash_observed:
        return {'data': False}

    # Check Merkle path (from entry hash to directory block keymr)
    path_to_dblock = params.get('path_to_dblock')
    if not isinstance(path_to_dblock, list) or len(path_to_dblock) < 1:
        return {'data': False}
    for element in path_to_dblock:
        left = bytes.fromhex(element.get('left'))
        right = bytes.fromhex(element.get('right'))
        top_expected = bytes.fromhex(element.get('top'))
        top_observed = sha256(left + right).digest()
        if top_expected != top_observed:
            return {'data': False}

    # Check last item in Merkle Path is the same as provided directory block keymr
    dblock_keymr = params.get('dblock_keymr')
    if dblock_keymr != path_to_dblock[-1]['top']:
        return {'data': False}
