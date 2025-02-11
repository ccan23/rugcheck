from rugcheck import rugcheck

def test_rugcheck_initialization():
    token = 'D48ayM5GxcXgWiH4afe2U5Zc9Y49akvqgekZT4oDpump'
    rc = rugcheck(token)
    assert rc.token_address == token

def test_rugcheck_dict_conversion():
    token = 'D48ayM5GxcXgWiH4afe2U5Zc9Y49akvqgekZT4oDpump'
    rc = rugcheck(token)
    assert isinstance(rc.to_dict(), dict)
