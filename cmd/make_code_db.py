# coding: utf-8

import cPickle as pickle
"""
TODO: Comment in
import caffe
"""
import util


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

    bpath = '../yandere-crawler/illust/'

    code_db = []

    # TODO: For train.txt
    with open('./test.txt') as f:
        for line in f:
            preview_fpath, _ = line.rstrip().split(' ')
            preview_fpath = bpath + preview_fpath

            print preview_fpath

            # Make BGR 227x227 image
            data = util.load_image(preview_fpath)

            # Make code
            code = util.make_code(net, data)

            code_db.append((code, preview_fpath))

    with open('./code_db.pickle', 'wb') as f:
        pickle.dump(code_db, f)

if __name__ == '__main__':
    main()
