import json

class FuncDB:
    def __init__(self,filename_personal,filename_wish):
        self.filename_personal = filename_personal
        self.filename_wish = filename_wish

    def search(self, name, number,resdefault):  # 동일인물일 경우 이전에 측정해둔 몸무게값과 랜덤으로 받았던 운동종목 반환
        for i in resdefault:
            if name in i.values() and number in i.values():
                return [i["weight"], i["exercise"]]
    def read(self):
        info_peronal = []
        info_wish = []
        fh = open(self.filename_personal, "r")
        try:
            info_personal = json.load(fh)
        except json.JSONDecodeError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_personal = []
            pass
        fh.close()
        fo = open(self.filename_wish, "r")
        try:
            info_wish = json.load(fo)
        except json.JSONDecodeError:  # 프로그램을 처음 시작할때 빈 파일을 읽게 되어 에러 발생-> 빈 리스트를 반환해주어 해결
            info_wish = []
            pass
        fo.close()
        return [info_personal, info_wish]
    def write(self,resdefault,reswish):
        fh = open(self.filename_personal, "w")
        json.dump(resdefault, fh, indent="\t")
        fh.close()
        fo = open(self.filename_wish, "w")
        json.dump(reswish, fo, indent="\t")
        fo.close()