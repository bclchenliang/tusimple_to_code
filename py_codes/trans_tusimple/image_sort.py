import os
class BatchRename():
    def __init__(self):
        self.path = r"C:\Users\bcl\Desktop\image"
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
                print(dst)
                #dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')   #0000000.jpg
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d pngs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
