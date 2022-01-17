# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from img import settings
import os
import urllib

class ImgPipeline:
    def process_item(self, item, spider):
        dir_path="%s/%s"%(settings.IMAGE_STORE,spider.name)
        print('dir_path='+dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        for image_url in item['image_urls']:
            list_name=image_url.split('/')
            filename = list_name[len(list_name)-1]
            file_path='%s/%s'%(dir_path,filename)
             
            if image_url.find("jpg") >= 0 and image_url.find("http") >= 0:
			#if os.path.exists(file_path):
            #   continue
                with open(file_path,'wb') as file_writer:
                    print("###########################################")
                    print("filename is " + filename)
                    print("imgurl is " + image_url)
                    print("###########################################")
                    conn = urllib.request.urlopen(image_url)
                    file_writer.write(conn.read())
                
                file_writer.close()

        return item
