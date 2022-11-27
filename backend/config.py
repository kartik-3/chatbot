import yaml 
path = 'config.yaml'
def read():
    with open(path,'r') as fp:
        cfg = yaml.safe_load(fp)
    return cfg

def write(cfg):
    with open(path,'w') as fp:
        yaml.dump(cfg,fp)

def set_topics(topics):
    cfg = read()
    cfg['topics'] = topics
    write(cfg)
    return ('Success')