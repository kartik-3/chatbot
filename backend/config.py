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

def get_topics(mode='active'):
    cfg = read()
    topics = cfg['topics']
    if mode == 'all':
        return topics
    return [topic for topic,status in topics.items() if status]