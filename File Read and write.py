wf= open('mysecondfile','w')
wf.write('Hey, this is my huh file')
wf.close()

rf=open('mysecondfile','r')
read_data_from_text=rf.read()
rf.close()
print(read_data_from_text)