# coding: utf-8

import cPickle as pickle

"""
TODO: Comment in
import caffe
"""

import util


def search(code_db, code, num_neighbors):
    dists = []
    for c, fpath in code_db:
        # Calculate hamming distance
        dist = 0
        for i in range(len(code)):
            if c[i] != code[i]:
                dist += 1

        dists.append((dist, c, fpath))

    dists.sort(key=lambda x: x[0])

    return dists[:num_neighbors]


def main():
    # TODO: Erase dummy net
    net = None
    """
    TODO: Comment in
    deploy_fpath = 'deploy.prototxt'
    model_fpath = 'model.protobinary'

    caffe.set_mode_gpu()
    net = caffe.Net(deploy_fpath, model_fpath, caffe.TEST)
    """

    preview_fpath = '../yandere-crawler/illust/preview/335/335201.jpg'
    code_db_fpath = './code_db.pickle'

    code_db = []
    with open(code_db_fpath, 'rb') as f:
        code_db = pickle.load(f)

    data = util.load_image(preview_fpath)
    code = util.make_code(net, data)

    result = search(code_db, code, 5)
    print result

if __name__ == '__main__':
    main()
