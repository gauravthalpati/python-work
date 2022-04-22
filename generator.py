
from jinja2 import Environment, FileSystemLoader
import yaml
import os
import sys
os.path.dirname(sys.executable)

print (os.path.dirname(sys.executable))

file_dir=os.path.dirname(os.path.abspath(__file__))

print(file_dir)

env = Environment(loader=FileSystemLoader(file_dir))

template = env.get_template('templat2.j2')

configfile = open(f"{file_dir}/input1.yaml","r")

config = yaml.safe_load(configfile)

f=open(f"mycode_{config['myword']}.py","w")
f.write(template.render(config))
