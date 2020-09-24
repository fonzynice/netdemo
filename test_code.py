from netdemo.mynornir import title, print_title

c = title('Connecting to Cisco Dev-net Sandbox...')
print_title(c)


def test_title():
    # name = 'cisco'
    assert c == 'Connecting to Cisco Dev-net Sandbox...'




