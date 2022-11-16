import yaml 
path = 'config.yaml'
def read():
    with open(path,'r') as fp:
        cfg = yaml.safe_load(fp)
    return cfg

def write(cfg):
    with open(path,'w') as fp:
        yaml.dump(cfg,fp)

def toggle(topic):
    cfg = read()
    status = not cfg['topics'][topic]
    if topic == 'All':
        for k,v in cfg['topics'].items():
            cfg['topics'][k] = not v
    else:
        cfg['topics'][topic] = status
    write(cfg)
    return status
