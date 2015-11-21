# coding: utf-8

import json


def main():
    # Extract general tags (top 200)
    general_tags = []
    with open('tag.json', 'r') as f:
        tags = json.load(f)
        for tag in tags:
            if tag['type'] == 0:
                general_tags.append(tag)
    general_tags.sort(key=lambda x: x['count'], reverse=True)
    general_tags = general_tags[:200]

    tag_name_id_map = {}
    tag_id_name_map = {}
    for tag in general_tags:
        tag_name_id_map[tag['name']] = long(tag['id'])
        tag_id_name_map[long(tag['id'])] = tag['name']

    # Split image by tag
    tagged_illust_ids = {}
    """
    tagged_illust_ids = {
        tag_id_1: [illust_id_10, illust_id_2, ...],
        tag_id_3: [illust_id_11, illust_id_22, ...],
        ...
    }
    """
    bpath = '../yandere-crawler/illust/'
    preview_fpaths = {}
    with open(bpath + 'list.txt', 'r') as list_fp:
        for line in list_fp:
            illust_id, meta_fpath, preview_fpath = line.rstrip().split(' ')
            illust_id = long(illust_id)
            preview_fpaths[illust_id] = preview_fpath

            with open(bpath + meta_fpath) as meta_fp:
                meta = json.load(meta_fp)
                tags = meta['tags'].split(' ')

                for tag_name in tags:
                    if tag_name in tag_name_id_map:
                        tag_id = tag_name_id_map[tag_name]
                        if tag_id not in tagged_illust_ids:
                            tagged_illust_ids[tag_id] = []
                        # TODO: Assign image to most least tag group
                        tagged_illust_ids[tag_id].append(illust_id)
                        break
                    else:
                        # Ignore invalid tag
                        continue

    print tagged_illust_ids

    # Split into training and test dataset
    train_ids = {}
    test_ids = {}
    for tag_id in tagged_illust_ids:
        """
        TODO: Comment in
        if len(tagged_illust_ids[tag_id]) < 10:
            raise Exception('Too little samples')
        """

        pivot = int(len(tagged_illust_ids[tag_id]) * 0.8)

        train_ids[tag_id] = tagged_illust_ids[tag_id][:pivot]
        test_ids[tag_id] = tagged_illust_ids[tag_id][pivot:]

    tag_class_map = {}
    class_id = 0
    for tag_id in tagged_illust_ids:
        tag_class_map[tag_id] = class_id
        class_id += 1

    # Save
    with open('class.txt', 'w') as f:
        for tag_id in tag_class_map:
            class_id = tag_class_map[tag_id]
            tag_name = tag_id_name_map[tag_id]
            f.write('{0} {1} {2}\n'.format(class_id, tag_id, tag_name))
    with open('train.txt', 'w') as f:
        for tag_id in train_ids:
            for illust_id in train_ids[tag_id]:
                f.write('{0} {1}\n'.format(preview_fpaths[illust_id], tag_class_map[tag_id]))
    with open('test.txt', 'w') as f:
        for tag_id in test_ids:
            for illust_id in test_ids[tag_id]:
                f.write('{0} {1}\n'.format(preview_fpaths[illust_id], tag_class_map[tag_id]))


if __name__ == '__main__':
    main()
