from os.path import join
from codecs import open

def load_data(filename, use_vocab=True, data_dir="./data"):
    """ read data """
    assert filename in ['train', 'dev', 'test']
    wlists = []
    tlists = []
    filepath = data_dir + "/" + split + ".char.bmes"
    with open(filepath, 'r', encoding='utf-8') as f:
        wlist = []
        tlist = []
        for lin in f:
            if line != '\n':
                w, t = line.strip('\r\n').split()
                wlist.append(w)
                tlist.append(t)
            else:
                wlists.append(wlist)
                tlists.append(tlist)
                wlist = []
                tlist = []
    if use_vocab:
        word2id = build_map(wlists)
        tag2id = build_map(tlists)
        return wlists, tlists, word2id, tag2id
    else:
        return wlists, tlists

def build_map(lists):
    maps = {}
    for list_ in lists:
        for e in list_:
            if e not in maps:
                maps[e] = len(maps)

    return maps
