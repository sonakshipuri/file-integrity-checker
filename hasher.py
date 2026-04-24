import hashlib, time

def get_hash(path, algo='sha256'):
    h = hashlib.new(algo)
    start = time.time()
    with open(path,'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest(), time.time()-start