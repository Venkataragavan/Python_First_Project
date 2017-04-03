import os

def create_directory(directory):
    if not os.path.exists(directory):
        print("Creating directory"+directory)
        os.makedirs(directory)

def create_files(project_name,base_url):#creating queue files (yet to be crawled) and crawler files(already crawled)
    queue=project_name+"\queue.txt"
    crawlfiles=project_name+"\crawlfile.txt"
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawlfiles):
        write_file(crawlfiles,'')

def write_file(path,data):#write data to the queue and crawl files
    f=open(path,'w')
    f.write(data)
    f.close()

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+"\n")

def delete_contents(path):
    with open(path,'w'):
        pass


