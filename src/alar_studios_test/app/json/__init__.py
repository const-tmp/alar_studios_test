from threading import Lock, Thread

from flask import Blueprint, url_for, jsonify
from requests import Session

bp = Blueprint('json', __name__, url_prefix='/json')


def fetch_async(session: Session, path: str, data: list, lock: Lock):
    r = session.get(path, timeout=2)
    result = r.json()
    with lock:
        data += result


@bp.route('/')
def get_data():
    data = []
    lock = Lock()

    threads = []
    with Session() as session:
        for i in range(3):
            path = url_for('static', filename=f'json/{i + 1}.json', _external=True)
            t = Thread(target=fetch_async, args=(session, path, data, lock))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    return jsonify(sorted(data, key=lambda d: d['id']))
