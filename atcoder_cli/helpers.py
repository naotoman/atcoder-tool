from typing import Dict, Tuple, Any, Union
import requests
from requests.sessions import Session
import json
from bs4 import BeautifulSoup
from pathlib import Path
import pickle


conf_dir = Path.home()/'.atcoder_cli_info'

def dump_session(session: Session) -> None:
    with open(conf_dir/'cookie.pkl', 'wb') as f:
        pickle.dump(session, f)

def get_session() -> Session:
    ck = conf_dir/'cookie.pkl'
    if ck.exists():
        with open(ck, 'rb') as f:
            return pickle.load(f)
    else:
        return requests.Session()

def load_conf() -> Dict[str, Any]:
    cf = conf_dir/'conf.json'
    with open(cf, 'r') as f:
        return json.load(f)

def dump_conf(data: Dict[str, Any]) -> None:
    cf = conf_dir/'conf.json'
    with open(cf, 'w') as f:
        json.dump(data, f, indent=4)

def get_lang_info(lang: str) -> Tuple[str, str]:
    lang_info = {}
    lang_info['python'] = ('3023', 'py')
    lang_info['rust'] = ('3504', 'rs')
    return lang_info[lang]