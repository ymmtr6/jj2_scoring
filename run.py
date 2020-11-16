# -*- coding: utf-8

from jj2_assert import jj2_assert
import yaml
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("CONFIG", help="採点設定ファイル(yml)")
parser.add_argument("-1", "--pre", action="store_true", help="preを採点する")
parser.add_argument("-2", "--post", action="store_true", help="postを採点する")
parser.add_argument("-3", "--write", action="store_true",
                    help="jsonファイルをexcelファイルに変換する")
parser.add_argument("-4", "--check", action="store_true", help="間違いを確認する")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    with open(args.CONFIG) as f:
        y = yaml.safe_load(f)
    obj = jj2_assert(y["book"])

    if args.pre:
        # pre
        obj.run_v2("pre", kadai=y["kadai"], numbers=y["numbers"],
                   classname=y["classname"], root=y["root"], rooms=y["rooms"])
        # save
        obj.print_status()
        obj.write_scores("{}.pre.json".format(y["kadai"]))
    if args.post:
        obj.load_scores("{}.pre.json".format(y["kadai"]))
        # post
        obj.run_v2("post", kadai=y["kadai"], numbers=y["numbers"],
                   classname=y["classname"], root=y["root"], rooms=y["rooms"])
        # save
        print("""
        #### 結果表示 ####
        """)
        obj.print_status()
        obj.write_scores("{}.post.json".format(y["kadai"]))
        # write excel
        obj.write_excel(y["kadai"], y["book"], y["output"])
        exit()
    if args.write:
        obj.load_scores("{}.post.json".format(y["kadai"]))
        obj.print_status()
        obj.write_excel(y["kadai"], y["book"], y["output"])
        exit()
    if args.check:
        obj.load_scores("{}.post.json".format(y["kadai"]))
        obj.check(kadai=y["kadai"], numbers=y["numbers"],
                  classname=y["classname"], root=y["root"], rooms=y["rooms"])
        exit()
